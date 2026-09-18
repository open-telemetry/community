import csv
import datetime
import os
import time

import requests

VOTERS_ROLL_PATH = os.getenv('VOTERS_ROLL_PATH', './voters-roll.csv')
GH_TOKEN = os.getenv('GITHUB_TOKEN')
PROJECT = os.getenv("PROJECT", "opentelemetry")
SERVER = f"{PROJECT}.devstats.cncf.io"

LFX_PROJECT = os.getenv("LFX_PROJECT", "opentelemetry")
LFX_URL = "https://insights.linuxfoundation.org/api/widget/contributors/contributor-leaderboard"
LFX_PAGE_SIZE = 1000
_today = datetime.date.today()
LFX_END_DATE = os.getenv("LFX_END_DATE", _today.isoformat())
LFX_START_DATE = os.getenv("LFX_START_DATE", (_today - datetime.timedelta(days=365)).isoformat())


# Get GitHub login from lowercase username
def get_github_login(username):
    print(f"Getting GitHub login for {username}")
    time.sleep(0.1)  # Sleep for 100ms to avoid rate limiting
    url = f'https://api.github.com/users/{username}'
    headers = {}
    if GH_TOKEN:
        headers = {
            'Authorization': f'token {GH_TOKEN}'
        }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['login']
    else:
        print(f"Failed to retrieve login for {username}: {response.status_code}")
        return None


# Use devstats to get users and contributions with more than 20 contributions in the last year
def get_users_and_contributions():
    print(f"Getting contributions data from {SERVER}")
    # Define the URL and headers
    url = f"https://{SERVER}/api/ds/query"
    headers = {
        'Accept': 'application/json',
        'content-type': 'application/json'
    }

    # Define the JSON payload
    payload = {
        "queries": [
            {
                "datasource": {
                    "uid": "P172949F98CB31475",
                    "type": "postgres"
                },
                "rawSql": "select sub.name as name, sub.value as contributions from (select split_part(name, '$$$', 1) as name, sum(value) as value from shdev where series = 'hdev_contributionsopentelemetryall' and period = 'y' group by split_part(name, '$$$', 1) ) sub where sub.value >= 20 order by name",
                "format": "table"
            }
        ],
        "range": {
            "from": "now",
            "to": "now"
        }
    }

    # Make the HTTP POST request
    response = requests.post(url, headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve contributions data: {response.status_code}")
        return None


# Build the devstats-derived list of [login, contributions] rows
def build_devstats_rows(data):
    frames = data['results']['A']['frames']
    rows = []

    for frame in frames:
        values = frame['data']['values']
        names = values[0]
        contributions = values[1]
        for i in range(len(names)):
            login = get_github_login(names[i])
            if login:
                rows.append([login, contributions[i]])

    return rows


# Fetch the full paginated LFX contributor list for the configured date range
def get_lfx_contributors():
    print(f"Getting LFX contributors for {LFX_PROJECT} from {LFX_START_DATE} to {LFX_END_DATE}")
    contributors = []
    offset = 0
    while True:
        params = {
            "project": LFX_PROJECT,
            "startDate": LFX_START_DATE,
            "endDate": LFX_END_DATE,
            "limit": LFX_PAGE_SIZE,
            "offset": offset,
        }
        response = requests.get(LFX_URL, params=params, timeout=30)
        response.raise_for_status()
        payload = response.json()
        contributors.extend(payload["data"])
        next_offset = payload["meta"]["offset"] + payload["meta"]["limit"]
        if next_offset >= payload["meta"]["total"]:
            break
        offset = next_offset

    print(f"Retrieved {len(contributors)} LFX contributors")
    return contributors


# Merge LFX contributors into the devstats rows.
# For each LFX contributor:
#   - skip if their contribution count is below the threshold (50)
#   - skip if they have no GitHub handle at all
#   - skip if any of their handles is already present (case-insensitive)
#   - otherwise add only the first handle in the array
def merge_lfx_contributors(rows, lfx_contributors):
    existing = {row[0].lower() for row in rows}
    added = 0

    for c in lfx_contributors:
        if (c.get("contributions") or 0) < 50:
            continue
        handles = c.get("githubHandleArray") or []
        if not handles:
            continue
        if any(h.lower() in existing for h in handles):
            continue
        primary = handles[0]
        rows.append([primary, c["contributions"]])
        existing.add(primary.lower())
        added += 1

    print(f"Added {added} new contributors from LFX")


# Write the merged list, sorted case-insensitively by GitHub login
def write_voters_rolls(rows):
    rows.sort(key=lambda r: r[0].lower())
    print(f"Writing data to {VOTERS_ROLL_PATH}")
    with open(VOTERS_ROLL_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        file.write('\n')


devstats_data = get_users_and_contributions()
rows = build_devstats_rows(devstats_data)
merge_lfx_contributors(rows, get_lfx_contributors())
write_voters_rolls(rows)
