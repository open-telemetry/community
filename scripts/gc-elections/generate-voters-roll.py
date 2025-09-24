import csv
import os
import time

import requests

VOTERS_ROLL_PATH = os.getenv('VOTERS_ROLL_PATH', './voters-roll.csv')
GH_TOKEN = os.getenv('GITHUB_TOKEN')
PROJECT = os.getenv("PROJECT", "opentelemetry")
SERVER = f"{PROJECT}.devstats.cncf.io"


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


# Create a CSV file with the voters rolls
def create_voters_rolls(data):
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

    # Write the data to a CSV file
    print(f"Writing data to {VOTERS_ROLL_PATH}")
    with open(VOTERS_ROLL_PATH, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        file.write('\n')


# Call the function
devstas_data = get_users_and_contributions()
create_voters_rolls(devstas_data)
