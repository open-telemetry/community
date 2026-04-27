#!/usr/bin/env python3
# Usage:
#     # Check all repos and print report
#     python move-to-emeritus.py
#
#     # Check all repos with debug output (shows why each member was marked active/inactive)
#     python move-to-emeritus.py --debug
#
#     # Check only specific repo(s)
#     python move-to-emeritus.py --repo opentelemetry-collector
#     python move-to-emeritus.py --repo opentelemetry-collector opentelemetry-python
#
#     # Create PRs to move inactive members to emeritus (after verifying the report)
#     python move-to-emeritus.py --create-prs
#
# Note: the script can be safely re-run multiple times. If a PR already exists for a repo, its body will be updated with the latest info.
#
import argparse
import base64
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone

DEBUG = False

def debug(msg):
    if DEBUG:
        print(f"  [DEBUG] {msg}")

def _search_fields():
    """Return the GraphQL fields to request inside a search() block."""
    if DEBUG:
        return "issueCount nodes { ... on Issue { number } ... on PullRequest { number } }"
    return "issueCount"

def _extract_numbers(search_result):
    """Extract issue/PR numbers from a GraphQL search result dict."""
    if not search_result:
        return []
    return [n["number"] for n in search_result.get("nodes", []) if "number" in n]

def _fmt_numbers(numbers):
    """Format a list of issue/PR numbers for debug display."""
    if not numbers:
        return ""
    return " #" + ", #".join(str(n) for n in numbers)

ORG = "open-telemetry"
INACTIVITY_MONTHS = 4

# Repos to skip entirely
IGNORED_REPOS = {
    "community",
    "cpp-build-tools", # Low traffic and stable repo
    "govanityurls", # Low traffic repo
    "opentelemetry-go-build-tools", # Low traffic repo
    "opentelemetry-network", # Low traffic and stable repo
    "opentelemetry-specification", # Too complex for simple checks. More checks can be added in the future
    "semantic-conventions", # Too complex for simple checks. More checks can be added in the future
    "opentelemetry-proto", # Too complex for simple checks. More checks can be added in the future
    "opentelemetry-proto-java", # Too complex for simple checks. More checks can be added in the future
    "sig-contributor-experience", # Majority of work is done outside of github
    "sig-developer-experience", # Majority of work is done outside of github
    "sig-end-user", # Majority of work is done outside of github
}

# For these repos, only check the listed team slugs (all others are ignored)
REPO_ALLOWED_TEAMS = {
    "opentelemetry.io": {
        "docs-triagers",
        "docs-approvers",
        "docs-maintainers",
        "blog-approvers",
    },
}

# For these repos, ignore teams whose name contains any of the listed keywords
REPO_IGNORED_TEAM_KEYWORDS = {
    "opentelemetry-js": ["browser"],
    "opentelemetry-js-contrib": ["browser", "javascript-contrib-triagers"], # Contrib triager is a complex team working similar to codeowners, so we skip it for now
}

token = os.environ.get("GITHUB_TOKEN")
if not token:
    print("GITHUB_TOKEN environment variable is required.", file=sys.stderr)
    sys.exit(1)

HEADERS = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "move-to-emeritus-script",
    "Accept": "application/vnd.github+json",
}
REST_API = "https://api.github.com"
GRAPHQL_API = "https://api.github.com/graphql"

def get_cutoff_date():
    now = datetime.now(timezone.utc)
    cutoff = now - timedelta(days=INACTIVITY_MONTHS * 30)
    return cutoff.strftime("%Y-%m-%d")

MAX_RATE_LIMIT_WAIT = 300  # cap waits at 5 min to avoid token expiry

def request_with_retry(method, url, data=None, retries=5):
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers=HEADERS, method=method)
        if data is not None:
            req.add_header("Content-Type", "application/json")
            body = json.dumps(data).encode("utf-8")
        else:
            body = None
        try:
            resp = urllib.request.urlopen(req, body, timeout=30)
            return resp
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                retry_after = e.headers.get("retry-after")
                reset_time = e.headers.get("x-ratelimit-reset")
                if retry_after:
                    wait = int(retry_after)
                elif reset_time:
                    wait = max(0, int(reset_time) - int(time.time())) + 1
                else:
                    wait = 60
                wait = min(wait, MAX_RATE_LIMIT_WAIT)
                print(f"Rate limited. Waiting {wait}s before retry...")
                time.sleep(wait)
                continue
            if 500 <= e.code < 600:
                # Transient server error — retry with backoff
                print(f"Attempt {attempt} failed: HTTP {e.code}")
                if attempt < retries:
                    time.sleep(2 ** attempt)
                else:
                    raise
                continue
            # 4xx (other than 429/403): deterministic — don't retry
            raise
        except (TimeoutError, OSError) as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(2)
            else:
                raise
    return None

def read_json(resp):
    return json.loads(resp.read().decode("utf-8"))

def paginate_rest(url, params=None):
    results = []
    params = params or {}
    params.setdefault("per_page", 100)
    # Add params to the initial URL
    if params:
        query_string = urllib.parse.urlencode(params)
        url = f"{url}?{query_string}"
    while url:
        resp = request_with_retry("GET", url)
        results.extend(read_json(resp))
        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                next_url = part.split("<")[1].split(">")[0]
        url = next_url
    return results

def get_teams_by_role(role_keyword):
    """Get all org teams with the given keyword in the name."""
    teams = paginate_rest(f"{REST_API}/orgs/{ORG}/teams")
    return [t for t in teams if role_keyword in t["name"].lower()]

def get_team_members(team_slug):
    """Get all members of a team."""
    members = paginate_rest(f"{REST_API}/orgs/{ORG}/teams/{team_slug}/members")
    return [m["login"] for m in members]

def get_team_repos(team_slug, cutoff):
    """Get all public repos assigned to a team, excluding repos created after cutoff."""
    repos = paginate_rest(f"{REST_API}/orgs/{ORG}/teams/{team_slug}/repos")
    return [
        r["name"] for r in repos
        if not r.get("private", False)
        and r.get("created_at", "")[:10] <= cutoff
    ]

# ---------------------------------------------------------------------------
# Cached per-repo data (fetched once, reused across all role checks)
# ---------------------------------------------------------------------------
_repo_comments_cache = {}   # repo -> {user: {"pr": [numbers], "issue": [numbers]}}
_repo_events_cache = {}     # repo -> [(actor, event_type, issue_number), ...]
_user_display_names = {}    # username -> display name (from GitHub API)

def _get_repo_commenters(repo, cutoff):
    """Fetch and cache all commenters on a repo since cutoff.

    Returns dict: {username: {"pr": [numbers], "issue": [numbers]}}
    """
    if repo in _repo_comments_cache:
        return _repo_comments_cache[repo]

    commenters = {}
    url = f"{REST_API}/repos/{ORG}/{repo}/issues/comments"
    params = {"since": f"{cutoff}T00:00:00Z", "per_page": 100, "sort": "created", "direction": "desc"}
    query_string = urllib.parse.urlencode(params)
    url = f"{url}?{query_string}"

    while url:
        resp = request_with_retry("GET", url)
        comments = read_json(resp)

        for comment in comments:
            created = comment.get("created_at", "")[:10]
            if created < cutoff:
                _repo_comments_cache[repo] = commenters
                return commenters

            user = (comment.get("user") or {}).get("login", "")
            if not user:
                continue

            html_url = comment.get("html_url", "")
            is_pr = "/pull/" in html_url
            kind = "pr" if is_pr else "issue"

            issue_url = comment.get("issue_url", "")
            number = int(issue_url.rstrip("/").split("/")[-1]) if issue_url else 0

            commenters.setdefault(user, {"pr": [], "issue": []})
            if number and number not in commenters[user][kind]:
                commenters[user][kind].append(number)

        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                next_url = part.split("<")[1].split(">")[0]
        url = next_url

    _repo_comments_cache[repo] = commenters
    return commenters


def _get_repo_events(repo, cutoff):
    """Fetch and cache all issue events for a repo since cutoff.

    Returns list of (actor, event_type, issue_number) tuples.
    """
    if repo in _repo_events_cache:
        return _repo_events_cache[repo]

    results = []
    url = f"{REST_API}/repos/{ORG}/{repo}/issues/events"
    params = {"per_page": 100}
    query_string = urllib.parse.urlencode(params)
    url = f"{url}?{query_string}"

    while url:
        resp = request_with_retry("GET", url)
        events = read_json(resp)

        for event in events:
            created = event.get("created_at", "")[:10]
            if created < cutoff:
                _repo_events_cache[repo] = results
                return results
            actor = (event.get("actor") or {}).get("login", "")
            issue_number = (event.get("issue") or {}).get("number", "")
            if actor:
                results.append((actor, event.get("event", ""), issue_number))

        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                next_url = part.split("<")[1].split(">")[0]
        url = next_url

    _repo_events_cache[repo] = results
    return results


def _check_comments(remaining, repo, cutoff, comment_type=None):
    """Check for comment activity using cached repo data. Returns dict of {username: [numbers]}.

    comment_type: None = all, "pr" = only PR comments, "issue" = only issue comments.
    """
    commenters = _get_repo_commenters(repo, cutoff)
    active = {}
    for user in remaining:
        if user not in commenters:
            continue
        data = commenters[user]
        if comment_type == "pr":
            numbers = data["pr"]
        elif comment_type == "issue":
            numbers = data["issue"]
        else:
            numbers = data["pr"] + data["issue"]
        if numbers:
            active[user] = numbers
    return active


def _check_events(remaining, repo, cutoff, event_types):
    """Check for issue event activity using cached repo data.

    Returns dict of {username: [(event_type, issue_number), ...]}.
    """
    all_events = _get_repo_events(repo, cutoff)
    active = {}
    found = set()
    for actor, event_type, issue_number in all_events:
        if actor in remaining and actor not in found and event_type in event_types:
            active.setdefault(actor, [])
            active[actor].append((event_type, issue_number))
            found.add(actor)
    return active


def _verify_review_candidates(user, candidate_prs, repo, cutoff):
    """Verify candidate PRs via REST to confirm actual review dates.

    Returns the first PR number with a confirmed recent review, or None.
    """
    for pr_number in candidate_prs:
        reviews_url = f"{REST_API}/repos/{ORG}/{repo}/pulls/{pr_number}/reviews"
        rev_resp = request_with_retry("GET", reviews_url)
        reviews = read_json(rev_resp)
        for review in reviews:
            submitted = review.get("submitted_at", "")[:10]
            reviewer = (review.get("user") or {}).get("login", "")
            if reviewer == user and submitted >= cutoff:
                return pr_number
    return None


def _check_reviews_paginated(user, repo, cutoff, start_cursor):
    """Paginate through remaining GraphQL results for a single user.

    Called only when the batched first page didn't confirm activity.
    Returns a PR number with confirmed review, or None.
    """
    safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
    review_q = f'type:pr repo:{ORG}/{repo} reviewed-by:{user} updated:>={cutoff}'
    cursor = start_cursor

    while cursor:
        query = (
            f'query {{ {safe}_reviews: search(query: "{review_q}", type: ISSUE, first: 10, after: "{cursor}") '
            f'{{ pageInfo {{ hasNextPage endCursor }} nodes {{ ... on PullRequest {{ number }} }} }} }}'
        )
        resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
        data = read_json(resp)
        if "errors" in data:
            print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
            sys.exit(1)

        result = data["data"].get(f"{safe}_reviews") or {}
        candidate_prs = [n["number"] for n in result.get("nodes", []) if "number" in n]

        pr = _verify_review_candidates(user, candidate_prs, repo, cutoff)
        if pr is not None:
            return pr

        page_info = result.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info.get("endCursor")

    return None


def _check_reviews(remaining, repo, cutoff):
    """Check for PR review activity. Returns dict of {username: [pr_numbers]}.

    Batches the first GraphQL page for up to 10 users at a time, then
    REST-verifies candidates. Users not confirmed active from the first page
    are paginated individually through remaining results.
    """
    if not remaining:
        return {}

    active = {}
    remaining_list = list(remaining)
    batch_size = 10
    page_size = 10

    for i in range(0, len(remaining_list), batch_size):
        batch_users = remaining_list[i : i + batch_size]
        if not batch_users:
            continue

        # Batched first-page GraphQL query for all users in this batch
        aliases = []
        for user in batch_users:
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            review_q = f'type:pr repo:{ORG}/{repo} reviewed-by:{user} updated:>={cutoff}'
            aliases.append(
                f'{safe}_reviews: search(query: "{review_q}", type: ISSUE, first: {page_size}) '
                f'{{ pageInfo {{ hasNextPage endCursor }} nodes {{ ... on PullRequest {{ number }} }} }}'
            )

        query = "query { " + "\n".join(aliases) + " }"
        resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
        data = read_json(resp)
        if "errors" in data:
            print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
            sys.exit(1)

        # Verify candidates and paginate if needed
        for user in batch_users:
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            result = data["data"].get(f"{safe}_reviews") or {}
            candidate_prs = [n["number"] for n in result.get("nodes", []) if "number" in n]

            pr = _verify_review_candidates(user, candidate_prs, repo, cutoff)
            if pr is not None:
                active[user] = [pr]
                continue

            # First page didn't confirm activity — paginate if more pages exist
            page_info = result.get("pageInfo", {})
            if page_info.get("hasNextPage"):
                cursor = page_info.get("endCursor")
                pr = _check_reviews_paginated(user, repo, cutoff, cursor)
                if pr is not None:
                    active[user] = [pr]

    return active


def check_triager_activity(usernames, repos, cutoff):
    """Check if triagers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    A triager is considered active if they did any of the following
    on ANY repo in the team:
      - Added a comment on an issue or PR
      - Added or removed a label
      - Closed an issue
    Short-circuits: once a user is found active on one repo, they are
    not checked on the remaining repos.
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check comments via REST API
        found = _check_comments(remaining, repo, cutoff)
        for user, numbers in found.items():
            debug(f"triager {user} active on {repo}: commented on issue/PR{_fmt_numbers(numbers)}")
        active.update(found.keys())
        remaining -= found.keys()
        if not remaining:
            return active

        # 2. Check label changes and issue closes via cached issue events
        found_events = _check_events(remaining, repo, cutoff, {"labeled", "unlabeled", "closed"})
        for actor, event_list in found_events.items():
            event_type, issue_num = event_list[0]
            debug(f"triager {actor} active on {repo}: {event_type} event #{issue_num}")
            active.add(actor)
            remaining.discard(actor)

    for user in remaining:
        debug(f"triager {user}: not active")
    return active

def check_approver_activity(usernames, repos, cutoff):
    """Check if approvers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    An approver is considered active if they did any of the following
    on ANY repo in the team:
      - Added a comment on a PR
      - Approved / reviewed a PR
      - Added a comment on an issue
    Short-circuits: once a user is found active on one repo, they are
    not checked on the remaining repos.
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check PR comments via REST (avoids updated:>= false positives)
        found_pr = _check_comments(remaining, repo, cutoff, comment_type="pr")
        for user, numbers in found_pr.items():
            debug(f"approver {user} active on {repo}: PR comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 2. Check issue comments via REST
        found_issue = _check_comments(remaining, repo, cutoff, comment_type="issue")
        for user, numbers in found_issue.items():
            debug(f"approver {user} active on {repo}: issue comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 3. Check PR reviews via REST
        found_reviews = _check_reviews(remaining, repo, cutoff)
        for user, numbers in found_reviews.items():
            debug(f"approver {user} active on {repo}: PR reviews{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

    for user in remaining:
        debug(f"approver {user}: not active")
    return active


def check_maintainer_activity(usernames, repos, cutoff):
    """Check if maintainers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    A maintainer is considered active if they did ANY of the following
    on any repo in the team:
      - Reviewed PRs
      - Commented on PRs
      - Merged PRs
      - Authored PRs
      - Commented on issues
    Short-circuits once a user is found active.
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check PR comments via REST (avoids updated:>= false positives)
        found_pr = _check_comments(remaining, repo, cutoff, comment_type="pr")
        for user, numbers in found_pr.items():
            debug(f"maintainer {user} active on {repo}: PR comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 2. Check issue comments via REST
        found_issue = _check_comments(remaining, repo, cutoff, comment_type="issue")
        for user, numbers in found_issue.items():
            debug(f"maintainer {user} active on {repo}: issue comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 3. Check PR reviews via REST
        found_reviews = _check_reviews(remaining, repo, cutoff)
        for user, numbers in found_reviews.items():
            debug(f"maintainer {user} active on {repo}: PR reviews{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 4. Check authored PRs via GraphQL (author + created:>= is accurate)
        remaining_list = list(remaining)
        batch_size = 10
        for i in range(0, len(remaining_list), batch_size):
            batch_users = [u for u in remaining_list[i : i + batch_size] if u in remaining]
            if not batch_users:
                continue

            aliases = []
            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                author_q = f'type:pr repo:{ORG}/{repo} author:{user} created:>={cutoff}'
                fields = _search_fields()
                aliases.append(
                    f'{safe}_authored: search(query: "{author_q}", type: ISSUE, first: 1) {{ {fields} }}'
                )

            query = "query { " + "\n".join(aliases) + " }"
            resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
            data = read_json(resp)
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                sys.exit(1)

            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                authored_result = data["data"].get(f"{safe}_authored") or {}
                authored = authored_result.get("issueCount", 0)
                if authored > 0:
                    debug(f"maintainer {user} active on {repo}: authored PRs ({authored}){_fmt_numbers(_extract_numbers(authored_result))}")
                    active.add(user)
                    remaining.discard(user)

            if not remaining:
                return active

        # 5. Check who merged PRs via cached issue events
        if remaining:
            found_merged = _check_events(remaining, repo, cutoff, {"merged"})
            for actor, event_list in found_merged.items():
                _, issue_num = event_list[0]
                debug(f"maintainer {actor} active on {repo}: merged PR #{issue_num}")
                active.add(actor)
                remaining.discard(actor)

    for user in remaining:
        debug(f"maintainer {user}: not active")
    return active


ROLES = [
    {
        "keyword": "triager",
        "label": "Triager",
        "check_fn": check_triager_activity,
    },
    {
        "keyword": "approver",
        "label": "Approver",
        "check_fn": check_approver_activity,
    },
    {
        "keyword": "maintainer",
        "label": "Maintainer",
        "check_fn": check_maintainer_activity,
    },
]

# Mapping from role label to README section name for the active role
ROLE_SECTIONS = {
    "Maintainer": "Maintainers",
    "Approver": "Approvers",
    "Triager": "Triagers",
}

EMERITUS_SECTION = "Emeritus"

BRANCH_NAME = "otelbot/move-inactive-to-emeritus"

EMERITUS_INFO = (
    "For more information about the emeritus role, see the\n"
    "[community repository]"
    "(https://github.com/open-telemetry/community/blob/main/guides/contributor/"
    "membership.md#emeritus-maintainerapprovertriager)."
)


# ---------------------------------------------------------------------------
# README parsing and modification
# ---------------------------------------------------------------------------

def fetch_readme(repo):
    """Fetch README.md from a repo via the Contents API.

    Returns (content_string, sha, path) or None if not found.
    """
    url = f"{REST_API}/repos/{ORG}/{repo}/readme"
    try:
        resp = request_with_retry("GET", url)
        data = read_json(resp)
        content = base64.b64decode(data["content"]).decode("utf-8")
        return content, data["sha"], data["path"]
    except urllib.error.HTTPError:
        return None


def _find_section(readme, section_name):
    """Find a section in the README by name (case-insensitive).

    Returns (start, end, header_level) or None.
    start/end are character offsets into the readme string.
    """
    pattern = re.compile(
        rf'^(#{{{2},3}})\s+{re.escape(section_name)}\s*$',
        re.MULTILINE | re.IGNORECASE,
    )
    match = pattern.search(readme)
    if not match:
        return None

    header_level = len(match.group(1))
    start = match.start()

    # End at the next header at same or higher level
    end_pattern = re.compile(rf'^#{{{1},{header_level}}}(?!#)\s', re.MULTILINE)
    end_match = end_pattern.search(readme, match.end())
    end = end_match.start() if end_match else len(readme)

    return start, end, header_level


def _parse_members(text):
    """Parse member entries from a README section text.

    Returns list of dicts: {"name", "username", "line"}
    """
    member_re = re.compile(
        r'^- \[([^\]]+)\]\(https://github\.com/([^)]+)\)(?:,\s*(.+))?$',
        re.MULTILINE,
    )
    members = []
    for m in member_re.finditer(text):
        members.append({
            "name": m.group(1),
            "username": m.group(2),
            "line": m.group(0),
        })
    return members


def _remove_member_line(readme, section_name, username):
    """Remove a member's line from a section by GitHub username.

    Returns modified readme, or None if the user was not found in the section.
    """
    section = _find_section(readme, section_name)
    if not section:
        return None

    start, end, _ = section
    section_text = readme[start:end]

    member_re = re.compile(
        rf'^- \[[^\]]+\]\(https://github\.com/{re.escape(username)}\).*\n?',
        re.MULTILINE | re.IGNORECASE,
    )
    match = member_re.search(section_text)
    if not match:
        return None

    new_section = section_text[: match.start()] + section_text[match.end() :]
    return readme[:start] + new_section + readme[end:]


def _add_to_emeritus(readme, emeritus_title, member_entry, header_level=3):
    """Add a member entry to an emeritus section. Creates the section if needed.

    Returns the modified readme string.
    """
    section = _find_section(readme, emeritus_title)

    if section:
        start, end, _ = section
        section_text = readme[start:end]

        # Skip if already present
        if member_entry in section_text:
            return readme

        lines = section_text.split("\n")

        # Separate member lines from non-member lines
        member_lines = [l for l in lines if l.startswith("- [")]
        member_lines.append(member_entry)

        # Sort alphabetically by display name (text inside [...])
        def _sort_key(line):
            m = re.match(r'^- \[([^\]]+)\]', line)
            return m.group(1).lower() if m else line.lower()
        member_lines.sort(key=_sort_key)

        # Rebuild: header + blank lines, then sorted members, then trailing content
        first_member_idx = None
        last_member_idx = None
        for i, line in enumerate(lines):
            if line.startswith("- ["):
                if first_member_idx is None:
                    first_member_idx = i
                last_member_idx = i

        if first_member_idx is not None:
            new_lines = lines[:first_member_idx] + member_lines + lines[last_member_idx + 1:]
        else:
            # No members yet — insert after header + blank line
            insert_idx = 1
            while insert_idx < len(lines) and lines[insert_idx].strip() == "":
                insert_idx += 1
            new_lines = lines[:insert_idx] + member_lines + lines[insert_idx:]

        new_section = "\n".join(new_lines)
        return readme[:start] + new_section + readme[end:]

    # Section doesn't exist — create it
    hashes = "#" * header_level
    new_section = f"\n{hashes} {emeritus_title}\n\n{member_entry}\n\n{EMERITUS_INFO}\n"

    # Try to insert before "Learn more about roles"
    idx = readme.find("\nLearn more about roles")
    if idx >= 0:
        return readme[:idx] + new_section + "\n" + readme[idx + 1 :]

    # Try before ## Licenses / ## License
    for marker in ["\n## Licenses", "\n## License"]:
        idx = readme.find(marker)
        if idx >= 0:
            return readme[:idx] + new_section + readme[idx:]

    return readme + new_section


def _get_display_name(username):
    """Fetch and cache a user's display name from the GitHub API.

    Returns the display name, or None if not available.
    """
    if username in _user_display_names:
        return _user_display_names[username]

    try:
        url = f"{REST_API}/users/{username}"
        resp = request_with_retry("GET", url)
        data = read_json(resp)
        name = data.get("name") or None
        _user_display_names[username] = name
        return name
    except Exception:
        _user_display_names[username] = None
        return None


def _to_emeritus_entry(username, role_label, display_name=None):
    """Create an emeritus entry line with previous role."""
    if not display_name:
        display_name = _get_display_name(username)
    name = display_name or f"@{username}"
    return f"- [{name}](https://github.com/{username}), {role_label}"


# ---------------------------------------------------------------------------
# Branch / PR creation via GitHub API
# ---------------------------------------------------------------------------

def _get_default_branch_sha(repo):
    """Return (sha, default_branch_name) for a repo."""
    url = f"{REST_API}/repos/{ORG}/{repo}"
    resp = request_with_retry("GET", url)
    data = read_json(resp)
    default_branch = data["default_branch"]

    ref_url = f"{REST_API}/repos/{ORG}/{repo}/git/ref/heads/{default_branch}"
    ref_resp = request_with_retry("GET", ref_url)
    ref_data = read_json(ref_resp)
    return ref_data["object"]["sha"], default_branch


def _ensure_branch(repo, branch, base_sha):
    """Create or force-update a branch to point at base_sha."""
    ref_url = f"{REST_API}/repos/{ORG}/{repo}/git/refs/heads/{branch}"
    try:
        request_with_retry("GET", ref_url)
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise
        # Branch doesn't exist — create it
        create_url = f"{REST_API}/repos/{ORG}/{repo}/git/refs"
        request_with_retry("POST", create_url, data={
            "ref": f"refs/heads/{branch}",
            "sha": base_sha,
        })
        return
    # Branch exists — force-update it
    request_with_retry("PATCH", ref_url, data={"sha": base_sha, "force": True})


def _update_file(repo, path, content, sha, branch, message):
    """Update a file on a branch via the Contents API."""
    url = f"{REST_API}/repos/{ORG}/{repo}/contents/{path}"
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    request_with_retry("PUT", url, data={
        "message": message,
        "content": encoded,
        "sha": sha,
        "branch": branch,
    })


def _create_pr(repo, branch, base, title, body):
    """Create a PR. If one already exists for the branch, update its body."""
    url = f"{REST_API}/repos/{ORG}/{repo}/pulls"
    try:
        resp = request_with_retry("POST", url, data={
            "title": title,
            "body": body,
            "head": branch,
            "base": base,
        })
        pr = read_json(resp)
        return pr.get("html_url", "")
    except urllib.error.HTTPError as e:
        if e.code == 422:
            # PR likely already exists — find and update it
            list_url = (
                f"{REST_API}/repos/{ORG}/{repo}/pulls"
                f"?head={ORG}:{branch}&state=open"
            )
            resp = request_with_retry("GET", list_url)
            prs = read_json(resp)
            if prs:
                pr_number = prs[0]["number"]
                patch_url = f"{REST_API}/repos/{ORG}/{repo}/pulls/{pr_number}"
                request_with_retry("PATCH", patch_url, data={
                    "title": title,
                    "body": body,
                })
                return prs[0].get("html_url", "")
        raise


# ---------------------------------------------------------------------------
# Orchestration: process repos and open PRs
# ---------------------------------------------------------------------------

def _build_pr_body(repo, changes, cutoff, warning=None):
    """Build the PR body markdown for a repo."""
    body = "## Move inactive members to emeritus\n\n"
    if warning:
        body += f"> **Warning:** {warning}\n\n"
    body += (
        f"The following members have had no activity in `{ORG}/{repo}` "
        f"since **{cutoff}** and are being moved to emeritus:\n\n"
    )

    for user, role_label, teams in sorted(changes):
        teams_str = ", ".join(teams)
        body += f"- @{user} ({role_label}, Remove from team(s): {teams_str})\n"
    body += "\n"

    body += (
        "**Note:** After merging, remove the users from the listed team(s) in GitHub and from any relevant private channels on Slack.\n\n"
        f"This PR was automatically generated by the "
        f"[move-to-emeritus workflow]"
        f"(https://github.com/{ORG}/community/actions/workflows/"
        f"move-to-emeritus.yml).\n"
    )
    return body


def create_emeritus_prs(inactive_report, repo_warnings, cutoff):
    """For each repo with inactive members, modify its README and open a PR."""
    print("\n" + "=" * 60)
    print("CREATING PULL REQUESTS")
    print("=" * 60)

    for repo, inactive_list in sorted(inactive_report.items()):
        print(f"\nProcessing {ORG}/{repo}...")

        # Fetch README
        result = fetch_readme(repo)
        if result is None:
            print(f"  Could not fetch README for {ORG}/{repo}, skipping.")
            continue
        readme, file_sha, file_path = result
        original_readme = readme

        # Consolidate: per user, pick highest role and collect all role sections
        role_priority = {"Triager": 0, "Approver": 1, "Maintainer": 2}
        user_info = {}  # user -> {"role": str, "roles": set, "teams": list}
        for user, team_name, role_label in inactive_list:
            if user not in user_info:
                user_info[user] = {"role": role_label, "roles": {role_label}, "teams": [team_name]}
            else:
                user_info[user]["roles"].add(role_label)
                if team_name not in user_info[user]["teams"]:
                    user_info[user]["teams"].append(team_name)
                if role_priority.get(role_label, -1) > role_priority.get(user_info[user]["role"], -1):
                    user_info[user]["role"] = role_label

        changes = []  # (username, role_label) for PR body
        header_level = 3  # default
        for user, info in sorted(user_info.items()):
            # Try to find display name from any role section
            display_name = None
            for role_label in info["roles"]:
                section_name = ROLE_SECTIONS.get(role_label)
                if not section_name:
                    continue
                section = _find_section(readme, section_name)
                if section:
                    start, end, header_level = section
                    for m in _parse_members(readme[start:end]):
                        if m["username"].lower() == user.lower():
                            display_name = m["name"]
                            break
                    if display_name:
                        break

            # Remove from ALL role sections the user appears in
            for role_label in info["roles"]:
                section_name = ROLE_SECTIONS.get(role_label)
                if not section_name:
                    continue
                modified = _remove_member_line(readme, section_name, user)
                if modified is not None:
                    readme = modified

            # Add to single Emeritus section with highest role
            highest_role = info["role"]
            entry = _to_emeritus_entry(user, highest_role, display_name)
            readme = _add_to_emeritus(readme, EMERITUS_SECTION, entry, header_level)
            changes.append((user, highest_role, sorted(info["teams"])))

        if readme == original_readme:
            print("  No README changes needed, skipping.")
            continue

        # Create branch, commit, and PR
        try:
            base_sha, default_branch = _get_default_branch_sha(repo)
            _ensure_branch(repo, BRANCH_NAME, base_sha)
            _update_file(
                repo, file_path, readme, file_sha, BRANCH_NAME,
                "Move inactive members to emeritus",
            )

            warning = repo_warnings.get(repo)
            # Strip leading whitespace/WARNING: prefix for cleaner PR body
            if warning:
                warning = warning.strip().removeprefix("WARNING: ")

            pr_body = _build_pr_body(repo, changes, cutoff, warning)
            pr_url = _create_pr(
                repo, BRANCH_NAME, default_branch,
                "Move inactive members to emeritus",
                pr_body,
            )
            print(f"  PR: {pr_url}")
        except Exception as e:
            print(f"  ERROR creating PR for {ORG}/{repo}: {e}", file=sys.stderr)


def main():
    global DEBUG
    parser = argparse.ArgumentParser(description="Check for inactive org members")
    parser.add_argument("--debug", action="store_true",
                        help="Print why each member was marked as active")
    parser.add_argument("--create-prs", action="store_true",
                        help="Create PRs to move inactive members to emeritus in each repo")
    parser.add_argument("--repo", nargs="+", default=None,
                        help="Only check specific repo(s) (e.g. opentelemetry-python opentelemetry-collector)")
    parser.add_argument("--output", type=str, default=None,
                        help="Save the inactive report to a JSON file (skips PR creation)")
    parser.add_argument("--input", type=str, default=None,
                        help="Load a previously saved report and create PRs (skips activity checking)")
    args = parser.parse_args()
    DEBUG = args.debug

    # --input: skip activity checking and go straight to PR creation
    if args.input:
        with open(args.input) as f:
            saved = json.load(f)
        cutoff = saved["cutoff"]
        inactive_report = {repo: [tuple(e) for e in entries]
                           for repo, entries in saved["inactive_report"].items()}
        repo_warnings = saved["repo_warnings"]
        print(f"Loaded report from {args.input} (cutoff: {cutoff})")
        if args.create_prs:
            create_emeritus_prs(inactive_report, repo_warnings, cutoff)
        return

    cutoff = get_cutoff_date()
    print(f"Checking for inactivity since {cutoff} ...\n")

    role_priority = {"Triager": 0, "Approver": 1, "Maintainer": 2}
    check_fns = {
        "Triager": check_triager_activity,
        "Approver": check_approver_activity,
        "Maintainer": check_maintainer_activity,
    }

    # Phase 1: Collect all user-team-repo relationships
    # user -> {"role": highest role, "entries": [(team_name, role_label)],
    #          "team_repos": {team_name: set(repos)}}
    all_user_data = {}
    team_repos_map = {}  # team_name -> set(repos)
    repo_maintainer_count = {}

    for role in ROLES:
        keyword = role["keyword"]
        label = role["label"]

        print(f"Fetching {label.lower()} teams...")
        teams = get_teams_by_role(keyword)
        if not teams:
            print(f"No {label.lower()} teams found.\n")
            continue

        for team in teams:
            slug = team["slug"]
            name = team["name"]
            team_name_lower = name.lower()
            print(f"  Fetching members and repos for '{name}'...")
            members = get_team_members(slug)
            repos = get_team_repos(slug, cutoff)

            # Filter to a list of repos if --repo is specified
            if args.repo:
                repos = [r for r in repos if r in args.repo]

            # Filter out ignored repos
            repos = [r for r in repos if r not in IGNORED_REPOS]

            # For repos with allowed-teams lists, skip this team if not allowed
            filtered_repos = []
            for r in repos:
                if r in REPO_ALLOWED_TEAMS:
                    if slug not in REPO_ALLOWED_TEAMS[r]:
                        continue
                if r in REPO_IGNORED_TEAM_KEYWORDS:
                    if any(kw in team_name_lower for kw in REPO_IGNORED_TEAM_KEYWORDS[r]):
                        continue
                filtered_repos.append(r)
            repos = filtered_repos

            print(f"Team '{name}': {len(members)} member(s), {len(repos)} repo(s)")

            if not members or not repos:
                continue

            # Track maintainer counts per repo
            if keyword == "maintainer":
                for repo in repos:
                    repo_maintainer_count.setdefault(repo, set())
                    repo_maintainer_count[repo].update(members)

            # Record team -> repos mapping
            team_repos_map[name] = set(repos)

            # Record user data
            for user in members:
                if user not in all_user_data:
                    all_user_data[user] = {
                        "role": label,
                        "priority": role_priority[label],
                        "entries": [],
                        "team_repos": {},
                    }
                all_user_data[user]["entries"].append((name, label))
                all_user_data[user]["team_repos"].setdefault(name, set()).update(repos)
                if role_priority[label] > all_user_data[user]["priority"]:
                    all_user_data[user]["role"] = label
                    all_user_data[user]["priority"] = role_priority[label]

        print()

    if not all_user_data:
        print("No users found to check.")
        return

    # Phase 2: Check activity per repo using the user's highest role for that repo.
    # If a user is on X-maintainer and X-approver (both covering repo X),
    # they are checked with maintainer criteria only. Activity on any repo in a
    # team satisfies that team.

    # Step 2a: For each user+repo, determine the highest role across all teams
    # user_repo_role: {user -> {repo -> highest_role}}
    user_repo_role = {}
    for user, data in all_user_data.items():
        for team_name, role_label in data["entries"]:
            for repo in data["team_repos"].get(team_name, set()):
                user_repo_role.setdefault(user, {})
                current = user_repo_role[user].get(repo)
                if current is None or role_priority[role_label] > role_priority[current]:
                    user_repo_role[user][repo] = role_label

    # Step 2b: Group by (repo, role) for batched checking
    repo_role_users = {}  # repo -> {role_label -> set(usernames)}
    for user, repo_roles in user_repo_role.items():
        for repo, role_label in repo_roles.items():
            repo_role_users.setdefault(repo, {})
            repo_role_users[repo].setdefault(role_label, set()).add(user)

    # Step 2c: Check activity per repo
    repo_active = {}  # repo -> set of active usernames
    all_repos = sorted(repo_role_users.keys())
    print(f"Checking activity across {len(all_repos)} repo(s)...")
    for repo in all_repos:
        active_on_repo = set()
        for role_label in ["Maintainer", "Approver", "Triager"]:
            users = list(repo_role_users[repo].get(role_label, []))
            if not users:
                continue
            check_fn = check_fns[role_label]
            active = check_fn(users, [repo], cutoff)
            active_on_repo.update(active)
        repo_active[repo] = active_on_repo

    # Step 2d: Map repo-level activity back to teams.
    # A user is active for a team if they are active on ANY of that team's repos.
    team_active = {}  # team_name -> set of active usernames
    for user, data in all_user_data.items():
        for team_name in data["team_repos"]:
            for repo in data["team_repos"][team_name]:
                if user in repo_active.get(repo, set()):
                    team_active.setdefault(team_name, set()).add(user)
                    break

    # Phase 3: Build inactive report
    # repo -> list of (username, team_name, role_label)
    # A user is flagged on a repo only if they are inactive for the team
    # that links them to that repo.
    inactive_report = {}
    for user, data in all_user_data.items():
        for team_name, role_label in data["entries"]:
            if user in team_active.get(team_name, set()):
                continue
            # User is inactive for this team — flag on all of the team's repos
            for repo in data["team_repos"].get(team_name, set()):
                inactive_report.setdefault(repo, [])
                inactive_report[repo].append((user, team_name, role_label))

    # Print report
    if not inactive_report:
        print("All members have been active. Nothing to report.")
        return

    print("=" * 60)
    print("INACTIVE MEMBERS REPORT")
    print(f"(no activity since {cutoff})")
    print("=" * 60)

    # Pre-compute maintainer health warnings per repo
    repo_warnings = {}
    for repo, inactive in inactive_report.items():
        if repo not in repo_maintainer_count:
            continue
        inactive_maintainers = {
            user for user, _, role_label in inactive
            if role_label == "Maintainer"
        }
        if not inactive_maintainers:
            continue
        total = len(repo_maintainer_count[repo])
        remaining = total - len(inactive_maintainers & repo_maintainer_count[repo])
        if remaining <= 1:
            if remaining == 0:
                repo_warnings[repo] = f"  WARNING: {total} -> 0 maintainers. Repo will have NO maintainers! Consider adding new maintainers before merging this PR."
            else:
                repo_warnings[repo] = f"  WARNING: {total} -> {remaining} maintainer. Repo will have only 1 maintainer! Consider adding new maintainers before merging this PR."

    total_inactive = 0
    for repo, inactive in sorted(inactive_report.items()):
        print(f"\n{ORG}/{repo}:")
        if repo in repo_warnings:
            print(repo_warnings[repo])

        # Consolidate: per user, pick highest role and collect all teams
        user_info = {}  # user -> {"role": str, "teams": list}
        for user, team_name, role_label in inactive:
            if user not in user_info:
                user_info[user] = {"role": role_label, "teams": [team_name]}
            else:
                if team_name not in user_info[user]["teams"]:
                    user_info[user]["teams"].append(team_name)
                if role_priority.get(role_label, -1) > role_priority.get(user_info[user]["role"], -1):
                    user_info[user]["role"] = role_label

        for user in sorted(user_info):
            info = user_info[user]
            teams = ", ".join(sorted(info["teams"]))
            print(f"  - @{user}  ({info['role']}, team(s): {teams})")

        total_inactive += len(user_info)

    print(f"\nTotal: {total_inactive} inactive member(s) across repo(s)")

    # Save report to file if requested
    if args.output:
        with open(args.output, "w") as f:
            json.dump({
                "cutoff": cutoff,
                "inactive_report": {repo: [list(e) for e in entries]
                                    for repo, entries in inactive_report.items()},
                "repo_warnings": repo_warnings,
            }, f, indent=2)
        print(f"Report saved to {args.output}")

    # Create PRs if requested
    if args.create_prs:
        create_emeritus_prs(inactive_report, repo_warnings, cutoff)


if __name__ == "__main__":
    main()
