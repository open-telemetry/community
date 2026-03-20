#!/usr/bin/env python3
import argparse
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
    "opentelemetry-network", # Low traffic and stable repo
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
    "opentelemetry-js-contrib": ["browser"],
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

def request_with_retry(method, url, data=None, retries=3):
    for attempt in range(1, retries + 1):
        req = urllib.request.Request(url, headers=HEADERS, method=method)
        if data is not None:
            req.add_header("Content-Type", "application/json")
            body = json.dumps(data).encode("utf-8")
        else:
            body = None
        try:
            resp = urllib.request.urlopen(req, body)
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
                print(f"Rate limited. Waiting {wait}s before retry...")
                time.sleep(wait)
                continue
            print(f"Attempt {attempt} failed: HTTP {e.code}")
            if attempt < retries:
                time.sleep(1)
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


def _check_reviews(remaining, repo, cutoff):
    """Check for PR review activity. Returns dict of {username: [pr_numbers]}.

    Uses GraphQL to find candidate PRs (reviewed-by + updated:>=), then
    verifies actual review dates via REST on only those specific PRs.
    """
    if not remaining:
        return {}

    active = {}
    remaining_set = set(remaining)
    remaining_list = list(remaining_set)
    batch_size = 10

    for i in range(0, len(remaining_list), batch_size):
        batch_users = [u for u in remaining_list[i : i + batch_size] if u in remaining_set]
        if not batch_users:
            continue

        # GraphQL: find candidate PRs per user
        aliases = []
        for user in batch_users:
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            review_q = f'type:pr repo:{ORG}/{repo} reviewed-by:{user} updated:>={cutoff}'
            aliases.append(
                f'{safe}_reviews: search(query: "{review_q}", type: ISSUE, first: 5) '
                f'{{ nodes {{ ... on PullRequest {{ number }} }} }}'
            )

        query = "query { " + "\n".join(aliases) + " }"
        resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
        data = read_json(resp)
        if "errors" in data:
            print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
            sys.exit(1)

        # For each user with candidates, verify review dates via REST
        for user in batch_users:
            if user not in remaining_set:
                continue
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            result = data["data"].get(f"{safe}_reviews") or {}
            candidate_prs = [n["number"] for n in result.get("nodes", []) if "number" in n]

            for pr_number in candidate_prs:
                reviews_url = f"{REST_API}/repos/{ORG}/{repo}/pulls/{pr_number}/reviews"
                rev_resp = request_with_retry("GET", reviews_url)
                reviews = read_json(rev_resp)

                for review in reviews:
                    submitted = review.get("submitted_at", "")[:10]
                    reviewer = (review.get("user") or {}).get("login", "")
                    if reviewer == user and submitted >= cutoff:
                        active.setdefault(user, [])
                        if pr_number not in active[user]:
                            active[user].append(pr_number)
                        remaining_set.discard(user)
                        break
                if user not in remaining_set:
                    break

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


def main():
    global DEBUG
    parser = argparse.ArgumentParser(description="Check for inactive org members")
    parser.add_argument("--debug", action="store_true",
                        help="Print why each member was marked as active")
    args = parser.parse_args()
    DEBUG = args.debug

    cutoff = get_cutoff_date()
    print(f"Checking for inactivity since {cutoff} ...\n")

    # Results: repo -> list of (username, team_name, role_label)
    inactive_report = {}
    # Track total maintainer count per repo (across all maintainer teams)
    repo_maintainer_count = {}

    for role in ROLES:
        keyword = role["keyword"]
        label = role["label"]
        check_fn = role["check_fn"]

        teams = get_teams_by_role(keyword)
        if not teams:
            print(f"No {label.lower()} teams found.\n")
            continue

        for team in teams:
            slug = team["slug"]
            name = team["name"]
            team_name_lower = name.lower()
            members = get_team_members(slug)
            repos = get_team_repos(slug, cutoff)

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

            active_users = check_fn(members, repos, cutoff)
            inactive = [u for u in members if u not in active_users]
            if inactive:
                for repo in repos:
                    inactive_report.setdefault(repo, [])
                    for user in inactive:
                        inactive_report[repo].append((user, name, label))

        print()

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
                repo_warnings[repo] = f"  WARNING: {total} -> 0 maintainers (repo will have NO maintainers!)"
            else:
                repo_warnings[repo] = f"  WARNING: {total} -> {remaining} maintainer (repo will have only 1 maintainer!)"

    total_inactive = 0
    seen = set()
    for repo, inactive in sorted(inactive_report.items()):
        print(f"\n{ORG}/{repo}:")
        if repo in repo_warnings:
            print(repo_warnings[repo])
        for user, team_name, role_label in sorted(inactive):
            print(f"  - @{user}  ({role_label}, team: {team_name})")
            if (user, team_name) not in seen:
                total_inactive += 1
                seen.add((user, team_name))

    print(f"\nTotal: {total_inactive} inactive member(s) across team(s)")


if __name__ == "__main__":
    main()
