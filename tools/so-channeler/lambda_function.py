import os
import json
import requests
from datetime import datetime
from boto3 import client

STACK_OVERFLOW_API = "https://api.stackexchange.com/2.3/search"
SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']
S3_BUCKET_NAME = os.environ['S3_BUCKET_NAME']
S3_OBJECT_KEY = "latest_question_timestamp.txt"

def get_latest_question_timestamp(s3_client):
    try:
        response = s3_client.get_object(Bucket=S3_BUCKET_NAME, Key=S3_OBJECT_KEY)
        return int(response['Body'].read().decode('utf-8'))
    except Exception as e:
        return 0

def update_latest_question_timestamp(s3_client, latest_timestamp):
    s3_client.put_object(Bucket=S3_BUCKET_NAME, Key=S3_OBJECT_KEY, Body=str(latest_timestamp))

def fetch_questions(latest_timestamp):
    params = {
        "tagged": "open-telemetry",
        "sort": "creation",
        "site": "stackoverflow",
        "fromdate": latest_timestamp
    }
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

def lambda_handler(event, context):
    s3_client = client('s3')
    latest_timestamp = get_latest_question_timestamp(s3_client)
    questions = fetch_questions(latest_timestamp)

    for question in questions:
        message = format_question(question)
        post_to_slack(message)
        latest_timestamp = max(latest_timestamp, question['creation_date'])

    update_latest_question_timestamp(s3_client, latest_timestamp)