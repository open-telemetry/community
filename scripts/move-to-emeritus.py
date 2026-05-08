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
    "opentelemetry-proto-java", # Inherits maintainers/approvers from other repos
    "opentelemetry-java-examples", # Inherits maintainers/approvers from other repos
    "semantic-conventions-java", # Inherits maintainers/approvers from other repos
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
    "opentelemetry-collector-releases": ["helm", "collector-contrib"], # Those teams are able to review PRs, but have low activity level
    "weaver": ["semconv"], # Semconv team is a complex team that won't always be active, so we skip it for now
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
            remaining = resp.headers.get("x-ratelimit-remaining")
            if remaining is not None and int(remaining) < 100:
                print(f"  [WARN] Rate limit low: {remaining} requests remaining")
            return resp
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                remaining = e.headers.get("x-ratelimit-remaining", "?")
                retry_after = e.headers.get("retry-after")
                reset_time = e.headers.get("x-ratelimit-reset")
                if retry_after:
                    wait = int(retry_after)
                elif reset_time:
                    wait = max(0, int(reset_time) - int(time.time())) + 1
                else:
                    wait = 60
                wait = min(wait, MAX_RATE_LIMIT_WAIT)
                print(f"Rate limited ({remaining} remaining). Waiting {wait}s before retry...")
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

_all_teams_cache = None

def _get_all_teams():
    global _all_teams_cache
    if _all_teams_cache is None:
        _all_teams_cache = paginate_rest(f"{REST_API}/orgs/{ORG}/teams")
    return _all_teams_cache

def get_teams_by_role(role_keyword):
    """Get all org teams with the given keyword in the name."""
    return [t for t in _get_all_teams() if role_keyword in t["name"].lower()]

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


def _check_comments(remaining, repo, cutoff, comment_type=None, exclude_pr=None):
    """Check for comment activity using cached repo data. Returns dict of {username: [numbers]}.

    comment_type: None = all, "pr" = only PR comments, "issue" = only issue comments.
    exclude_pr: PR number to ignore (activity on the move-to-emeritus PR itself doesn't count).
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
        if exclude_pr is not None:
            numbers = [n for n in numbers if n != exclude_pr]
        if numbers:
            active[user] = numbers
    return active


def _check_events(remaining, repo, cutoff, event_types, exclude_pr=None):
    """Check for issue event activity using cached repo data.

    Returns dict of {username: [(event_type, issue_number), ...]}.
    exclude_pr: issue/PR number to ignore.
    """
    all_events = _get_repo_events(repo, cutoff)
    active = {}
    found = set()
    for actor, event_type, issue_number in all_events:
        if actor in remaining and actor not in found and event_type in event_types:
            if exclude_pr is not None and issue_number == exclude_pr:
                continue
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


def _check_reviews_paginated(user, repo, cutoff, start_cursor, exclude_pr=None):
    """Paginate through remaining GraphQL results for a single user.

    Called only when the batched first page didn't confirm activity.
    Returns a PR number with confirmed review, or None.
    exclude_pr: PR number to skip.
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
        if exclude_pr is not None:
            candidate_prs = [n for n in candidate_prs if n != exclude_pr]

        pr = _verify_review_candidates(user, candidate_prs, repo, cutoff)
        if pr is not None:
            return pr

        page_info = result.get("pageInfo", {})
        if not page_info.get("hasNextPage"):
            break
        cursor = page_info.get("endCursor")

    return None


def _check_reviews(remaining, repo, cutoff, exclude_pr=None):
    """Check for PR review activity. Returns dict of {username: [pr_numbers]}.

    Batches the first GraphQL page for up to 10 users at a time, then
    REST-verifies candidates. Users not confirmed active from the first page
    are paginated individually through remaining results.
    exclude_pr: PR number to skip (activity on the move-to-emeritus PR itself doesn't count).
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
            if exclude_pr is not None:
                candidate_prs = [n for n in candidate_prs if n != exclude_pr]

            pr = _verify_review_candidates(user, candidate_prs, repo, cutoff)
            if pr is not None:
                active[user] = [pr]
                continue

            # First page didn't confirm activity — paginate if more pages exist
            page_info = result.get("pageInfo", {})
            if page_info.get("hasNextPage"):
                cursor = page_info.get("endCursor")
                pr = _check_reviews_paginated(user, repo, cutoff, cursor, exclude_pr=exclude_pr)
                if pr is not None:
                    active[user] = [pr]

    return active


def check_triager_activity(usernames, repos, cutoff, exclude_pr=None):
    """Check if triagers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    A triager is considered active if they did any of the following
    on ANY repo in the team:
      - Added a comment on an issue or PR
      - Added or removed a label
      - Closed an issue
    Short-circuits: once a user is found active on one repo, they are
    not checked on the remaining repos.
    exclude_pr: PR number to exclude from activity (e.g. the move-to-emeritus PR itself).
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check comments via REST API
        found = _check_comments(remaining, repo, cutoff, exclude_pr=exclude_pr)
        for user, numbers in found.items():
            debug(f"triager {user} active on {repo}: commented on issue/PR{_fmt_numbers(numbers)}")
        active.update(found.keys())
        remaining -= found.keys()
        if not remaining:
            return active

        # 2. Check label changes and issue closes via cached issue events
        found_events = _check_events(remaining, repo, cutoff, {"labeled", "unlabeled", "closed"}, exclude_pr=exclude_pr)
        for actor, event_list in found_events.items():
            event_type, issue_num = event_list[0]
            debug(f"triager {actor} active on {repo}: {event_type} event #{issue_num}")
            active.add(actor)
            remaining.discard(actor)

    for user in remaining:
        debug(f"triager {user}: not active")
    return active

def check_approver_activity(usernames, repos, cutoff, exclude_pr=None):
    """Check if approvers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    An approver is considered active if they did any of the following
    on ANY repo in the team:
      - Added a comment on a PR
      - Approved / reviewed a PR
      - Added a comment on an issue
    Short-circuits: once a user is found active on one repo, they are
    not checked on the remaining repos.
    exclude_pr: PR number to exclude from activity (e.g. the move-to-emeritus PR itself).
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check PR comments via REST (avoids updated:>= false positives)
        found_pr = _check_comments(remaining, repo, cutoff, comment_type="pr", exclude_pr=exclude_pr)
        for user, numbers in found_pr.items():
            debug(f"approver {user} active on {repo}: PR comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 2. Check issue comments via REST
        found_issue = _check_comments(remaining, repo, cutoff, comment_type="issue", exclude_pr=exclude_pr)
        for user, numbers in found_issue.items():
            debug(f"approver {user} active on {repo}: issue comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 3. Check PR reviews via REST
        found_reviews = _check_reviews(remaining, repo, cutoff, exclude_pr=exclude_pr)
        for user, numbers in found_reviews.items():
            debug(f"approver {user} active on {repo}: PR reviews{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

    for user in remaining:
        debug(f"approver {user}: not active")
    return active


def check_maintainer_activity(usernames, repos, cutoff, exclude_pr=None):
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
    exclude_pr: PR number to exclude from activity (e.g. the move-to-emeritus PR itself).
    """
    if not usernames or not repos:
        return set()

    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        # 1. Check PR comments via REST (avoids updated:>= false positives)
        found_pr = _check_comments(remaining, repo, cutoff, comment_type="pr", exclude_pr=exclude_pr)
        for user, numbers in found_pr.items():
            debug(f"maintainer {user} active on {repo}: PR comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 2. Check issue comments via REST
        found_issue = _check_comments(remaining, repo, cutoff, comment_type="issue", exclude_pr=exclude_pr)
        for user, numbers in found_issue.items():
            debug(f"maintainer {user} active on {repo}: issue comments{_fmt_numbers(numbers)}")
            active.add(user)
            remaining.discard(user)
        if not remaining:
            return active

        # 3. Check PR reviews via REST
        found_reviews = _check_reviews(remaining, repo, cutoff, exclude_pr=exclude_pr)
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
            found_merged = _check_events(remaining, repo, cutoff, {"merged"}, exclude_pr=exclude_pr)
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
ISSUE_TITLE = "chore: Remove inactive members from teams and channels"

EMERITUS_INFO = (
    "For more information about the emeritus role, see the\n"
    "[community repository]"
    "(https://github.com/open-telemetry/community/blob/main/guides/contributor/"
    "membership.md#emeritus-maintainerapprovertriager)."
)

_emeritus_pr_cache = {}  # repo -> PR number or None


def _get_emeritus_pr_number(repo):
    """Return the open move-to-emeritus PR number for repo, or None if there isn't one.

    Searches by head branch name rather than fork owner so it works regardless of
    which user created the fork (e.g. local runs vs CI using opentelemetrybot).
    """
    if repo in _emeritus_pr_cache:
        return _emeritus_pr_cache[repo]
    result = None
    try:
        url = f"{REST_API}/repos/{ORG}/{repo}/pulls?state=open&per_page=100"
        while url:
            resp = request_with_retry("GET", url)
            for pr in read_json(resp):
                if pr.get("head", {}).get("ref") == BRANCH_NAME:
                    result = pr["number"]
                    break
            if result:
                break
            link = resp.headers.get("Link", "")
            url = None
            for part in link.split(","):
                if 'rel="next"' in part:
                    url = part.split("<")[1].split(">")[0]
    except Exception:
        pass
    _emeritus_pr_cache[repo] = result
    return result


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
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        raise


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
        r'^[-*+] \[([^\]]+)\]\(https://github\.com/([^)]+)\)(?:,\s*(.+))?$',
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


def _detect_list_marker(section_text):
    """Return the list marker used in section_text ('-', '*' or '+', default '-')."""
    m = re.search(r'^([-*+]) \[', section_text, re.MULTILINE)
    return m.group(1) if m else "-"


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
        rf'^[-*+] \[[^\]]+\]\(https://github\.com/{re.escape(username)}\).*\n?',
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

        # Skip if user already present (match by username URL, not display name)
        username_match = re.search(r'https://github\.com/([^)]+)', member_entry)
        if username_match and re.search(
            rf'https://github\.com/{re.escape(username_match.group(1))}[)/]',
            section_text,
            re.IGNORECASE,
        ):
            return readme

        lines = section_text.split("\n")

        # Separate member lines from non-member lines
        member_lines = [l for l in lines if re.match(r'^[-*+] \[', l)]
        member_lines.append(member_entry)

        # Sort alphabetically by display name (text inside [...])
        def _sort_key(line):
            m = re.match(r'^[-*+] \[([^\]]+)\]', line)
            return m.group(1).lower() if m else line.lower()
        member_lines.sort(key=_sort_key)

        # Rebuild: header + blank lines, then sorted members, then trailing content
        first_member_idx = None
        last_member_idx = None
        for i, line in enumerate(lines):
            if re.match(r'^[-*+] \[', line):
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


def _to_emeritus_entry(username, role_label, display_name=None, marker="-"):
    """Create an emeritus entry line with previous role."""
    if not display_name:
        display_name = _get_display_name(username)
    name = display_name or f"@{username}"
    return f"{marker} [{name}](https://github.com/{username}), {role_label}"


# ---------------------------------------------------------------------------
# Branch / PR creation via GitHub API (fork-based)
# ---------------------------------------------------------------------------

_fork_owner_cache = None

def _get_fork_owner():
    """Return the login of the authenticated user (used as the fork owner)."""
    global _fork_owner_cache
    if _fork_owner_cache is None:
        resp = request_with_retry("GET", f"{REST_API}/user")
        _fork_owner_cache = read_json(resp)["login"]
    return _fork_owner_cache


def _ensure_fork(repo):
    """Fork repo under the authenticated user's account, waiting until git is ready."""
    owner = _get_fork_owner()
    fork_url = f"{REST_API}/repos/{owner}/{repo}"

    fork_exists = False
    try:
        data = read_json(request_with_retry("GET", fork_url))
        if data.get("fork") and (data.get("parent") or {}).get("full_name") == f"{ORG}/{repo}":
            fork_exists = True
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    if not fork_exists:
        print(f"  Forking {ORG}/{repo} to {owner}...", flush=True)
        request_with_retry("POST", f"{REST_API}/repos/{ORG}/{repo}/forks", data={})
        for _ in range(12):
            time.sleep(5)
            try:
                if read_json(request_with_retry("GET", fork_url)).get("fork"):
                    fork_exists = True
                    break
            except urllib.error.HTTPError as e:
                if e.code != 404:
                    raise
        if not fork_exists:
            raise RuntimeError(f"Fork of {ORG}/{repo} did not appear after 60s")

    # A fork's git objects are initialised asynchronously — the repo endpoint
    # returns 200 before refs are accessible.  Poll until refs respond.
    refs_url = f"{REST_API}/repos/{owner}/{repo}/git/refs/heads"
    for attempt in range(1, 13):
        try:
            request_with_retry("GET", refs_url)
            return
        except urllib.error.HTTPError as e:
            if e.code in (404, 409) and attempt < 12:
                print(f"  Waiting for fork git to be ready (attempt {attempt}/12)...", flush=True)
                time.sleep(5)
            else:
                raise


def _get_default_branch_sha(repo):
    """Return (sha, default_branch_name) for the upstream repo."""
    url = f"{REST_API}/repos/{ORG}/{repo}"
    resp = request_with_retry("GET", url)
    data = read_json(resp)
    default_branch = data["default_branch"]

    ref_url = f"{REST_API}/repos/{ORG}/{repo}/git/ref/heads/{default_branch}"
    ref_resp = request_with_retry("GET", ref_url)
    ref_data = read_json(ref_resp)
    return ref_data["object"]["sha"], default_branch


def _ensure_branch(owner, repo, branch, base_sha):
    """Create or force-update a branch on owner/repo to point at base_sha."""
    ref_url = f"{REST_API}/repos/{owner}/{repo}/git/refs/heads/{branch}"

    branch_exists = False
    try:
        refs = read_json(request_with_retry("GET", ref_url))
        # GitHub returns an empty array (200) when no refs match a path with slashes
        # in the branch name, rather than a 404.
        branch_exists = bool(refs)
    except urllib.error.HTTPError as e:
        if e.code != 404:
            raise

    if branch_exists:
        request_with_retry("PATCH", ref_url, data={"sha": base_sha, "force": True})
    else:
        request_with_retry("POST", f"{REST_API}/repos/{owner}/{repo}/git/refs", data={
            "ref": f"refs/heads/{branch}",
            "sha": base_sha,
        })


def _update_file(owner, repo, path, content, sha, branch, message):
    """Update a file on a branch in owner/repo via the Contents API."""
    url = f"{REST_API}/repos/{owner}/{repo}/contents/{path}"
    encoded = base64.b64encode(content.encode("utf-8")).decode("ascii")
    payload = {"message": message, "content": encoded, "sha": sha, "branch": branch}
    try:
        request_with_retry("PUT", url, data=payload)
    except urllib.error.HTTPError as e:
        if e.code != 422:
            raise
        # SHA mismatch — re-fetch the current file SHA from the branch and retry
        resp = request_with_retry("GET", f"{url}?ref={branch}")
        payload["sha"] = read_json(resp)["sha"]
        request_with_retry("PUT", url, data=payload)


def _create_pr(repo, head_owner, branch, base, title, body):
    """Open a cross-repo PR from head_owner/repo:branch into ORG/repo:base.

    If a PR for that branch already exists, update its title and body instead.
    """
    url = f"{REST_API}/repos/{ORG}/{repo}/pulls"
    head = f"{head_owner}:{branch}"
    try:
        resp = request_with_retry("POST", url, data={
            "title": title,
            "body": body,
            "head": head,
            "base": base,
        })
        return read_json(resp).get("html_url", "")
    except urllib.error.HTTPError as e:
        if e.code == 422:
            # PR likely already exists — find and update it
            list_url = f"{REST_API}/repos/{ORG}/{repo}/pulls?head={head}&state=open"
            prs = read_json(request_with_retry("GET", list_url))
            if prs:
                pr_number = prs[0]["number"]
                patch_url = f"{REST_API}/repos/{ORG}/{repo}/pulls/{pr_number}"
                request_with_retry("PATCH", patch_url, data={"title": title, "body": body})
                return prs[0].get("html_url", "")
            detail = e.read().decode("utf-8", errors="replace")
            print(f"  [ERROR] PR creation 422, no open PR found. GitHub said: {detail}", file=sys.stderr)
        raise


# ---------------------------------------------------------------------------
# Orchestration: process repos and open PRs
# ---------------------------------------------------------------------------

def _build_pr_body(repo, changes, cutoff, warning=None):
    """Build the PR body markdown for a repo."""
    body = "## Move inactive members to emeritus\n\n"
    if warning:
        body += f"> [!CAUTION] \n> {warning}\n\n"
    body += (
        f"The following members have had no activity in `{ORG}/{repo}` "
        f"since **{cutoff}** and are being moved to emeritus:\n\n"
    )

    for user, role_label, teams in sorted(changes):
        teams_str = ", ".join(teams)
        body += f"- @{user} ({role_label}, Remove from team(s): {teams_str})\n"
    body += "\n"

    body += (
        "> [!IMPORTANT]\n"
        "> Before merging, a Maintainer should remove the user(s) from:\n"
        f"> - [ ] The listed team(s) in [GitHub](https://github.com/orgs/{ORG}/teams)\n"
        "> - [ ] Any relevant private channels on Slack\n"
        "> - [ ] Any relevant package managers used for publishing\n\n"
        "This PR was automatically generated by the "
        "[move-to-emeritus workflow]"
        f"(https://github.com/{ORG}/community/actions/workflows/"
        "move-to-emeritus.yml). "
        "For guidance on how to handle this PR, see the "
        f"[move-to-emeritus documentation](https://github.com/{ORG}/community/blob/main/move-to-emeritus.md).\n"
    )
    return body


def _build_issue_body(changes):
    """Build the issue body for the follow-up cleanup issue."""
    body = "## Remove inactive members from teams and channels\n\n"
    body += (
        "The following members have already been moved to emeritus in the README,"
        " but still need to be removed from teams and channels.\n\n"
    )
    for user, role_label, teams in sorted(changes):
        teams_str = ", ".join(teams)
        body += f"- @{user} ({role_label}, Remove from team(s): {teams_str})\n"
    body += "\n"
    body += (
        "> [!IMPORTANT]\n"
        "> A Maintainer should remove the user(s) from:\n"
        f"> - [ ] The listed team(s) in [GitHub](https://github.com/orgs/{ORG}/teams)\n"
        "> - [ ] Any relevant private channels on Slack\n"
        "> - [ ] Any relevant package managers used for publishing\n\n"
        "This issue was automatically generated by the "
        "[move-to-emeritus workflow]"
        f"(https://github.com/{ORG}/community/actions/workflows/"
        "move-to-emeritus.yml). "
        "For guidance on how to handle this issue, see the "
        f"[move-to-emeritus documentation](https://github.com/{ORG}/community/blob/main/move-to-emeritus.md).\n"
    )
    return body


def _create_followup_issue(repo, changes):
    """Create a follow-up issue when the README is already up to date.

    If an open issue with the same title already exists, update its body instead.
    Returns the issue URL.
    """
    body = _build_issue_body(changes)
    issues_url = f"{REST_API}/repos/{ORG}/{repo}/issues"

    # Look for an existing open issue to update rather than creating a duplicate
    url = f"{issues_url}?state=open&per_page=100"
    while url:
        resp = request_with_retry("GET", url)
        for issue in read_json(resp):
            if issue.get("title") == ISSUE_TITLE and not issue.get("pull_request"):
                issue_number = issue["number"]
                request_with_retry("PATCH", f"{issues_url}/{issue_number}", data={"body": body})
                return issue.get("html_url", "")
        link = resp.headers.get("Link", "")
        url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                url = part.split("<")[1].split(">")[0]

    resp = request_with_retry("POST", issues_url, data={"title": ISSUE_TITLE, "body": body})
    return read_json(resp).get("html_url", "")


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
            # Try to find display name and detect list marker from any role section
            display_name = None
            marker = "-"
            for role_label in info["roles"]:
                section_name = ROLE_SECTIONS.get(role_label)
                if not section_name:
                    continue
                section = _find_section(readme, section_name)
                if section:
                    start, end, header_level = section
                    section_text = readme[start:end]
                    for m in _parse_members(section_text):
                        if m["username"].lower() == user.lower():
                            display_name = m["name"]
                            marker = _detect_list_marker(section_text)
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
            entry = _to_emeritus_entry(user, highest_role, display_name, marker=marker)
            readme = _add_to_emeritus(readme, EMERITUS_SECTION, entry, header_level)
            changes.append((user, highest_role, sorted(info["teams"])))

        if readme == original_readme:
            print("  No README changes needed.")
            if changes:
                try:
                    issue_url = _create_followup_issue(repo, changes)
                    print(f"  Issue: {issue_url}")
                except Exception as e:
                    print(f"  ERROR creating issue for {ORG}/{repo}: {e}", file=sys.stderr)
            continue

        # Fork repo, create branch on fork, commit, and open cross-repo PR
        try:
            fork_owner = _get_fork_owner()
            base_sha, default_branch = _get_default_branch_sha(repo)
            print(f"  Ensuring fork...", flush=True)
            _ensure_fork(repo)
            print(f"  Syncing fork with upstream...", flush=True)
            try:
                request_with_retry("POST",
                    f"{REST_API}/repos/{fork_owner}/{repo}/merge-upstream",
                    data={"branch": default_branch})
            except urllib.error.HTTPError as e:
                print(f"  [WARN] Could not sync fork with upstream: HTTP {e.code}", flush=True)
            _ensure_branch(fork_owner, repo, BRANCH_NAME, base_sha)
            _update_file(
                fork_owner, repo, file_path, readme, file_sha, BRANCH_NAME,
                "chore: Move inactive members to emeritus",
            )

            warning = repo_warnings.get(repo)
            # Strip leading whitespace/WARNING: prefix for cleaner PR body
            if warning:
                warning = warning.strip().removeprefix("WARNING: ")

            pr_body = _build_pr_body(repo, changes, cutoff, warning)
            pr_url = _create_pr(
                repo, fork_owner, BRANCH_NAME, default_branch,
                "chore: Move inactive members to emeritus",
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
    args = parser.parse_args()
    DEBUG = args.debug

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
        # Exclude the existing move-to-emeritus PR so users who only commented/approved
        # that PR are not mistakenly counted as active contributors.
        emeritus_pr = _get_emeritus_pr_number(repo)
        active_on_repo = set()
        for role_label in ["Maintainer", "Approver", "Triager"]:
            users = list(repo_role_users[repo].get(role_label, []))
            if not users:
                continue
            check_fn = check_fns[role_label]
            active = check_fn(users, [repo], cutoff, exclude_pr=emeritus_pr)
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

    if args.create_prs:
        create_emeritus_prs(inactive_report, repo_warnings, cutoff)


if __name__ == "__main__":
    main()
