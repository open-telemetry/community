import requests
import json
import subprocess
import pprint

# Replace these variables with your GitHub organization and personal access token
ORG_NAME = 'open-telemetry'
ACCESS_TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True).stdout.decode('utf-8').strip()


# Define headers with the access token
headers = {
    'Authorization': f'token {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

def fetch_paginated_data(url):
    """Fetch data from paginated API endpoints."""
    data = []
    while url:
        response = requests.get(url, headers=headers)
        data += response.json()
        link_header = response.headers.get('Link')
        if link_header:
            links = link_header.split(',')
            for link in links:
                if 'rel="next"' in link:
                    next_url = link.split(';')[0].strip().strip('<>').strip()
                    url = next_url
                    break
            else:
                url = None
        else:
            url = None
    return data


# Get organization members
members_url = f'https://api.github.com/orgs/{ORG_NAME}/members'
members_data = fetch_paginated_data(members_url)
members = [{"username": member["login"], "role": "member"} for member in members_data]

# Get organization teams and their members
teams_url = f'https://api.github.com/orgs/{ORG_NAME}/teams'
teams_data = fetch_paginated_data(teams_url)

sigs = {}

# Construct the SIG map
for team in teams_data:
    team_name = team['name']
    sig_name = team_name
    role = ""
    if team_name.endswith('-triagers'):
        sig_name = team_name[:-len('-triagers')]
        role = 'triagers'
    elif team_name.endswith('-approvers'):
        sig_name = team_name[:-len('-approvers')]
        role = 'approvers'
    elif team_name.endswith('-maintainers'):
        sig_name = team_name[:-len('-maintainers')]
        role = 'maintainers'
    else:
        print(f"unknown team structure {team_name}")
        role = 'unknown'
    if sig_name not in sigs:
        sigs[sig_name] = {
            "name": sig_name,
            "triagers": set(),
            "approvers": set(),
            "maintainers": set(),
            "unknown": set()
        }

    team_members_url = team['members_url'].replace('{/member}', '')  # Remove placeholder
    team_members_data = fetch_paginated_data(team_members_url)
    team_members = [member["login"] for member in team_members_data]
    sigs[sig_name][role] = set(team_members)

# Dedupe the groups
for name, sig in sigs.items():
    sig["triagers"] = list(sig["triagers"] - sig["approvers"] - sig["maintainers"])
    sig["approvers"] = list(sig["approvers"] - sig["maintainers"])
    sig["maintainers"] = list(sig["maintainers"])
    sig["unknown"] = list(sig["unknown"])


member_tmpl = """
module "{username}_membership" {{
    source = "./modules/member"
    username = "{username}"
    role = "{role}"
}}
"""

sig_tmpl = """
module "{name}_sig" {{
    source = "./modules/sig"
    name = "{name}"
    triagers = {triagers}
    approvers = {approvers}
    maintainers = {maintainers}
}}
"""

# GENERATE TF FILE
with open('output.tf', 'w') as f:
    for m in members:
        f.writelines(member_tmpl.format(**m))
    for name, sig in sigs.items():
        if len(sig["unknown"]):
            print('not working on', sig)
            continue
        f.writelines(sig_tmpl.format(**sig).replace("'", '"')) # arcane words to replace single quotes with double quotes


# output = {"members": members, "sigs": sigs}

# with open('output.json', 'w') as f:
#     json.dump(output, f, indent=4)
