import requests
import json
import subprocess

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
members = [member["login"] for member in members_data]

# Get organization teams and their members
teams_url = f'https://api.github.com/orgs/{ORG_NAME}/teams'
teams_data = fetch_paginated_data(teams_url)

flat_teams = []
for team in teams_data:
    team_name = team['name']
    team_slug = team['slug']
    
    # Check if 'parent' key exists and is not None, then extract 'slug'
    parent_info = team.get('parent')
    parent_slug = parent_info.get('slug') if parent_info else None

    team_members_url = team['members_url'].replace('{/member}', '')  # Remove placeholder
    team_members_data = fetch_paginated_data(team_members_url)
    team_members = [member["login"] for member in team_members_data]

    flat_teams.append({"name": team_name, "members": team_members, "parent": parent_slug})

output = {"members": members, "teams": flat_teams}

with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)
