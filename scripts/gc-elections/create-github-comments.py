"""Tag eligible voters on a GitHub issue for the OpenTelemetry GC election.

Behaviour:
- If the issue has no existing voter-notification comments, post one comment
  per batch of 50 voters from the roll file.
- If the issue already has voter-notification comments, reconcile with the
  current roll file:
    * Remove `@handle` lines from existing comments for handles no longer in
      the roll. If a comment loses all its voters, delete it.
    * Post additional comments (batched by 50) for handles in the roll that
      are not yet mentioned in any existing voter-notification comment.

Voter-notification comments are identified by an exact match on the header
string, so unrelated conversation comments are left untouched.
"""

import argparse
import csv
import json
import os
import re
import subprocess
import sys

VOTERS_ROLL_PATH = os.environ.get('VOTERS_ROLL_PATH', './voters-roll.csv')
BATCH_SIZE = 50
HEADER = (
    "We invite the people mentioned in this comment to vote in the "
    "OpenTelemetry Governance Committee, as they have provided more than 20 "
    "contributions to the project over the last year via GitHub. Your "
    "contributions were comments, code reviews, pull requests, among others. "
    "Thank you!"
)

MENTION_RE = re.compile(r'^\* @([A-Za-z0-9][A-Za-z0-9-]*)\s*$', re.MULTILINE)
ISSUE_URL_RE = re.compile(r'^https?://github\.com/([^/]+)/([^/]+)/issues/(\d+)/?$')


def parse_bool(v):
    return str(v).strip().lower() in ('true', '1', 'yes', 'y')


def parse_issue_url(url):
    m = ISSUE_URL_RE.match(url.strip())
    if not m:
        sys.exit(f"invalid issue URL: {url}")
    return m.group(1), m.group(2), m.group(3)


def load_voters(path):
    handles = []
    with open(path, newline='') as f:
        for row in csv.reader(f):
            if not row:
                continue
            handle = row[0].strip()
            if handle:
                handles.append(handle)
    return handles


def gh_json(args):
    r = subprocess.run(['gh'] + args, capture_output=True, text=True, check=True)
    out = r.stdout.strip()
    if not out:
        return []
    return json.loads(out)


def gh_run(args, input_text=None):
    subprocess.run(['gh'] + args, input=input_text, text=True, check=True)


def build_body(handles):
    return HEADER + "\n\n" + "\n".join(f"* @{h}" for h in handles)


def extract_mentions(body):
    return MENTION_RE.findall(body or "")


def remove_handle_line(body, handle):
    pattern = re.compile(
        rf'^\* @{re.escape(handle)}\s*(?:\n|$)',
        re.MULTILINE | re.IGNORECASE,
    )
    return pattern.sub('', body)


def post_batches(issue_url, handles, dryrun):
    if not handles:
        return
    for i in range(0, len(handles), BATCH_SIZE):
        batch = handles[i:i + BATCH_SIZE]
        body = build_body(batch)
        if dryrun:
            print(f"--- would post comment with {len(batch)} voter(s) ---")
            print(body)
            print()
        else:
            gh_run(['issue', 'comment', issue_url, '-F', '-'], input_text=body)


def sync(owner, repo, issue_url, voter_comments, file_handles, dryrun):
    file_lower = {h.lower() for h in file_handles}

    tagged_lower = set()
    for c in voter_comments:
        for m in extract_mentions(c.get('body') or ''):
            tagged_lower.add(m.lower())

    # Remove stale @handle lines from each existing voter comment.
    total_removed = 0
    for c in voter_comments:
        original = c.get('body') or ''
        new_body = original
        removed = []
        for m in extract_mentions(original):
            if m.lower() not in file_lower:
                new_body = remove_handle_line(new_body, m)
                removed.append(m)
        if not removed:
            continue

        cid = c['id']
        mentions = ', '.join('@' + h for h in removed)
        verb_remove = 'would remove' if dryrun else 'removing'
        verb_delete = 'would delete' if dryrun else 'deleting'

        if not extract_mentions(new_body):
            print(f"Comment {cid}: all {len(removed)} voter(s) stale ({mentions}) — {verb_delete}")
            if not dryrun:
                gh_run(['api', '-X', 'DELETE',
                        f'/repos/{owner}/{repo}/issues/comments/{cid}'])
        else:
            print(f"Comment {cid}: {verb_remove} {len(removed)} stale voter(s): {mentions}")
            if dryrun:
                print("--- updated body would be ---")
                print(new_body)
                print()
            else:
                payload = json.dumps({'body': new_body})
                gh_run(
                    ['api', '-X', 'PATCH',
                     f'/repos/{owner}/{repo}/issues/comments/{cid}',
                     '--input', '-'],
                    input_text=payload,
                )
        total_removed += len(removed)

    if total_removed:
        print(f"{'Would remove' if dryrun else 'Removed'} {total_removed} stale voter(s) in total")
    else:
        print("No stale voters to remove")

    # Post new voters that are in the file but not yet tagged.
    to_add = [h for h in file_handles if h.lower() not in tagged_lower]
    print(f"{'Would add' if dryrun else 'Adding'} {len(to_add)} new voter(s)")
    post_batches(issue_url, to_add, dryrun)


def main():
    parser = argparse.ArgumentParser(description=(
        "Tag eligible voters on a GitHub issue. "
        "Reconciles existing voter-notification comments with the current voter roll."
    ))
    parser.add_argument('-i', '--issue', required=True, help='GitHub issue URL')
    parser.add_argument('-d', '--dry-run', default='true',
                        help='dry-run mode (true/false, default: true)')
    args = parser.parse_args()

    if not os.path.isfile(VOTERS_ROLL_PATH):
        sys.exit(f"voters roll not found at {VOTERS_ROLL_PATH}")

    owner, repo, num = parse_issue_url(args.issue)
    dryrun = parse_bool(args.dry_run)

    print(f"Reading voters from {VOTERS_ROLL_PATH}")
    voters = load_voters(VOTERS_ROLL_PATH)
    print(f"Loaded {len(voters)} voter(s)")

    print(f"Fetching comments on {args.issue}")
    all_comments = gh_json(['api', '--paginate',
                            f'/repos/{owner}/{repo}/issues/{num}/comments'])
    voter_comments = [c for c in all_comments if HEADER in (c.get('body') or '')]
    print(f"Found {len(voter_comments)} existing voter-notification comment(s)")

    if not voter_comments:
        print(f"No existing voter-notification comments — posting all {len(voters)} voter(s)")
        post_batches(args.issue, voters, dryrun)
    else:
        sync(owner, repo, args.issue, voter_comments, voters, dryrun)


if __name__ == '__main__':
    main()
