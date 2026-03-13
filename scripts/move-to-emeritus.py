#!/usr/bin/env python3
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from datetime import datetime, timedelta, timezone

ORG = "open-telemetry"
INACTIVITY_MONTHS = 4

# Repos to skip entirely
IGNORED_REPOS = {
    "admin",
    "community",
    "opentelemetry-ebpf-profiler-ghsa-7jcw-7r7m-wp3p",
    "sig-contributor-experience",
    "sig-developer-experience",
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

def get_team_repos(team_slug):
    """Get all repos assigned to a team."""
    repos = paginate_rest(f"{REST_API}/orgs/{ORG}/teams/{team_slug}/repos")
    return [r["name"] for r in repos]

def fetch_repo_issue_events(repo, cutoff):
    """Fetch issue events (labeled, unlabeled, closed) from a repo since cutoff.

    Returns a list of (actor_login, event_type) tuples.
    Stops paginating once events are older than the cutoff date.
    """
    results = []
    url = f"{REST_API}/repos/{ORG}/{repo}/issues/events"
    params = {"per_page": 100}
    query_string = urllib.parse.urlencode(params)
    url = f"{url}?{query_string}"

    relevant_events = {"labeled", "unlabeled", "closed"}

    while url:
        resp = request_with_retry("GET", url)
        events = read_json(resp)

        for event in events:
            created = event.get("created_at", "")[:10]
            if created < cutoff:
                # Events are returned newest-first; stop once we pass cutoff
                return results
            if event.get("event") in relevant_events:
                actor = (event.get("actor") or {}).get("login", "")
                if actor:
                    results.append((actor, event["event"]))

        link = resp.headers.get("Link", "")
        next_url = None
        for part in link.split(","):
            if 'rel="next"' in part:
                next_url = part.split("<")[1].split(">")[0]
        url = next_url

    return results

def _check_comments_graphql(remaining, repo, cutoff):
    """Check for comment activity via GraphQL. Returns set of active usernames."""
    active = set()
    remaining_list = list(remaining)
    batch_size = 10
    for i in range(0, len(remaining_list), batch_size):
        batch_users = [u for u in remaining_list[i : i + batch_size] if u in remaining]
        if not batch_users:
            continue

        aliases = []
        for user in batch_users:
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            comment_q = f'repo:{ORG}/{repo} commenter:{user} updated:>={cutoff}'
            aliases.append(
                f'{safe}_comments: search(query: "{comment_q}", type: ISSUE, first: 1) {{ issueCount }}'
            )

        query = "query { " + "\n".join(aliases) + " }"
        resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
        data = read_json(resp)
        if "errors" in data:
            print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
            sys.exit(1)

        for user in batch_users:
            safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
            comments = (data["data"].get(f"{safe}_comments") or {}).get(
                "issueCount", 0
            )
            if comments > 0:
                active.add(user)

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

        # 1. Check comments via GraphQL search
        found = _check_comments_graphql(remaining, repo, cutoff)
        active.update(found)
        remaining -= found
        if not remaining:
            return active

        # 2. Check label changes and issue closes via REST issue events
        events = fetch_repo_issue_events(repo, cutoff)
        for actor, _ in events:
            if actor in remaining:
                active.add(actor)
                remaining.discard(actor)
                if not remaining:
                    break

    return active

def check_approver_activity(usernames, repos, cutoff):
    """Check if approvers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    An approver is considered active if they did any of the following
    on ANY repo in the team:
      - Added a comment on a PR
      - Approved / reviewed a PR
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

        remaining_list = list(remaining)
        batch_size = 10
        for i in range(0, len(remaining_list), batch_size):
            batch_users = [u for u in remaining_list[i : i + batch_size] if u in remaining]
            if not batch_users:
                continue

            aliases = []
            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                pr_comment_q = f'type:pr repo:{ORG}/{repo} commenter:{user} updated:>={cutoff}'
                review_q = f'type:pr repo:{ORG}/{repo} reviewed-by:{user} updated:>={cutoff}'
                aliases.append(
                    f'{safe}_pr_comments: search(query: "{pr_comment_q}", type: ISSUE, first: 1) {{ issueCount }}'
                )
                aliases.append(
                    f'{safe}_reviews: search(query: "{review_q}", type: ISSUE, first: 1) {{ issueCount }}'
                )

            query = "query { " + "\n".join(aliases) + " }"
            resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
            data = read_json(resp)
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                sys.exit(1)

            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                pr_comments = (data["data"].get(f"{safe}_pr_comments") or {}).get(
                    "issueCount", 0
                )
                reviews = (data["data"].get(f"{safe}_reviews") or {}).get(
                    "issueCount", 0
                )
                if pr_comments > 0 or reviews > 0:
                    active.add(user)
                    remaining.discard(user)

            if not remaining:
                return active

    return active


def check_maintainer_activity(usernames, repos, cutoff):
    """Check if maintainers are active across any of the given repos since cutoff.

    Returns a set of usernames that have been active.
    A maintainer is considered active only if they satisfy BOTH:
      - (reviewed PRs OR commented on PRs OR merged PRs)  AND
      - authored PRs
    Criteria accumulate across repos in the same team.
    Short-circuits once a user satisfies both sides.
    """
    if not usernames or not repos:
        return set()

    # Track which criteria each user has met
    has_engagement = set()  # reviewed OR commented
    has_authored = set()
    active = set()
    remaining = set(usernames)

    for repo in repos:
        if not remaining:
            break

        remaining_list = list(remaining)
        batch_size = 10
        for i in range(0, len(remaining_list), batch_size):
            batch_users = [u for u in remaining_list[i : i + batch_size] if u in remaining]
            if not batch_users:
                continue

            aliases = []
            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                review_q = f'type:pr repo:{ORG}/{repo} reviewed-by:{user} updated:>={cutoff}'
                comment_q = f'type:pr repo:{ORG}/{repo} commenter:{user} updated:>={cutoff}'
                author_q = f'type:pr repo:{ORG}/{repo} author:{user} created:>={cutoff}'
                aliases.append(
                    f'{safe}_reviews: search(query: "{review_q}", type: ISSUE, first: 1) {{ issueCount }}'
                )
                aliases.append(
                    f'{safe}_pr_comments: search(query: "{comment_q}", type: ISSUE, first: 1) {{ issueCount }}'
                )
                aliases.append(
                    f'{safe}_authored: search(query: "{author_q}", type: ISSUE, first: 1) {{ issueCount }}'
                )

            query = "query { " + "\n".join(aliases) + " }"
            resp = request_with_retry("POST", GRAPHQL_API, data={"query": query})
            data = read_json(resp)
            if "errors" in data:
                print(f"GraphQL errors: {data['errors']}", file=sys.stderr)
                sys.exit(1)

            for user in batch_users:
                safe = "u_" + re.sub(r"[^a-zA-Z0-9]", "_", user)
                reviews = (data["data"].get(f"{safe}_reviews") or {}).get(
                    "issueCount", 0
                )
                pr_comments = (data["data"].get(f"{safe}_pr_comments") or {}).get(
                    "issueCount", 0
                )
                authored = (data["data"].get(f"{safe}_authored") or {}).get(
                    "issueCount", 0
                )
                if reviews > 0 or pr_comments > 0:
                    has_engagement.add(user)
                if authored > 0:
                    has_authored.add(user)
                if user in has_engagement and user in has_authored:
                    active.add(user)
                    remaining.discard(user)

            if not remaining:
                return active

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
    cutoff = get_cutoff_date()
    print(f"Checking for inactivity since {cutoff} ...\n")

    # Results: repo -> list of (username, team_name, role_label)
    inactive_report = {}

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
            repos = get_team_repos(slug)

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

    total_inactive = 0
    seen = set()
    for repo, inactive in sorted(inactive_report.items()):
        print(f"\n{ORG}/{repo}:")
        for user, team_name, role_label in sorted(inactive):
            print(f"  - @{user}  ({role_label}, team: {team_name})")
            if (user, team_name) not in seen:
                total_inactive += 1
                seen.add((user, team_name))

    print(f"\nTotal: {total_inactive} inactive member(s) across team(s)")


if __name__ == "__main__":
    main()
