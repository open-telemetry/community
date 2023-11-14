import requests
import subprocess
import json
import json

# Replace these variables with your GitHub organization and personal access token
ORG_NAME = 'open-telemetry'
ACCESS_TOKEN = subprocess.run(["gh", "auth", "token"], capture_output=True).stdout.decode('utf-8').strip()

# Define the API endpoint URLs
org_url = f'https://api.github.com/orgs/{ORG_NAME}'
members_url = f'https://api.github.com/orgs/{ORG_NAME}/members'
teams_url = f'https://api.github.com/orgs/{ORG_NAME}/teams'

# Define headers with the access token
headers = {
    'Authorization': f'token {ACCESS_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Get organization details
org_response = requests.get(org_url, headers=headers)
org_data = org_response.json()

# Get organization members and their roles
members_response = requests.get(members_url, headers=headers)
members_data = members_response.json()

print("Retrieving members and teams from GitHub organization...")

members = []
while True:
    for member in members_data:
        members.append(member["login"])

    # Check if there are more pages of data to retrieve
    link_header = members_response.headers.get('Link')
    if not link_header or 'rel="next"' not in link_header:
        break

    # Get the URL for the next page of data
    next_page_url = None
    for link in link_header.split(','):
        if 'rel="next"' in link:
            next_page_url = link[link.index('<') + 1:link.index('>')]
            break

    # Retrieve the next page of data
    members_response = requests.get(next_page_url, headers=headers)
    members_data = members_response.json()

teams = []
# Get organization teams and their members
teams_response = requests.get(teams_url, headers=headers)
teams_data = teams_response.json()

while True:
    for team in teams_data:
        team_name = team['name']
        team_members = []
        team_members_url = team['members_url'].replace('{/member}', '')  # Remove placeholder
        team_members_response = requests.get(team_members_url, headers=headers)
        team_members_data = team_members_response.json()
        for team_member in team_members_data:
            team_members.append(team_member["login"])
        teams.append({"name": team_name, "members": team_members})

    # Check if there are more pages of data to retrieve
    link_header = teams_response.headers.get('Link')
    if not link_header or 'rel="next"' not in link_header:
        break

    # Get the URL for the next page of data
    next_page_url = None
    for link in link_header.split(','):
        if 'rel="next"' in link:
            next_page_url = link[link.index('<') + 1:link.index('>')]
            break

    # Retrieve the next page of data
    teams_response = requests.get(next_page_url, headers=headers)
    teams_data = teams_response.json()

output = {"members": members, "teams": teams}

with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)

