import os
import json
import requests
from datetime import datetime

STACK_OVERFLOW_API = "https://api.stackexchange.com/2.3/search"
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
STATE_FILE = "state.txt"

def get_latest_question_timestamp():
    try:
        with open(STATE_FILE, 'r') as f:
            return int(f.read().strip())
    except FileNotFoundError:
        return 0

def update_latest_question_timestamp(latest_timestamp):
    with open(STATE_FILE, 'w') as f:
        f.write(str(latest_timestamp))

def fetch_questions(latest_timestamp):
    params = {
        "tagged": "open-telemetry",
        "sort": "creation",
        "site": "stackoverflow"
    }
    if latest_timestamp > 0:
        params["min"] = latest_timestamp + 1

    response = requests.get(STACK_OVERFLOW_API, params=params)
    response.raise_for_status()
    return response.json().get('items', [])

def format_question(question):
    title = question['title']
    link = question['link']
    return f"New question: <{link}|{title}>"

def post_to_slack(message):
    headers = {"Content-Type": "application/json"}
    data = {"text": message}
    response = requests.post(SLACK_WEBHOOK_URL, headers=headers, data=json.dumps(data))
    response.raise_for_status()

def main():
    latest_timestamp = get_latest_question_timestamp()
    questions = fetch_questions(latest_timestamp)

    for question in questions:
        message = format_question(question)
        post_to_slack(message)
        latest_timestamp = max(latest_timestamp, question['creation_date'])

    update_latest_question_timestamp(latest_timestamp)

if __name__ == "__main__":
    main()
