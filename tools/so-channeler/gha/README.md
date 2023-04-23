# StackOverflow to Slack GitHub Action

This GitHub Action fetches new StackOverflow questions tagged with `open-telemetry` and posts them to a Slack channel. It runs on an hourly schedule.

## Setup

1. Clone this repository or create a new repository with the provided `github_action.py` script and `.github/workflows/main.yml` workflow file.

2. Create a Slack [incoming webhook URL](https://api.slack.com/messaging/webhooks) for the Slack channel where you want to post new questions.

3. Add the webhook URL as a secret in your GitHub repository. Go to the "Settings" tab of your GitHub repository, then click "Secrets" in the left sidebar. Click "New repository secret" and add a secret with the name `SLACK_WEBHOOK_URL` and the webhook URL value.

4. Commit an empty `state.txt` file in the same directory as your `github_action.py` script. This file will store the timestamp of the latest fetched question.

5. Update the paths in the `.github/workflows/main.yml` file to match the locations of your `github_action.py` and `state.txt` files.

6. Push your changes to the repository. The GitHub Action will start running on an hourly schedule.

## How it works

The GitHub Action runs the following steps:

1. Checks out the repository code.

2. Sets up Python 3.8 and installs the `requests` package.

3. Runs the `github_action.py` script, which fetches new questions from StackOverflow, posts them to Slack, and updates the `state.txt` file with the latest question timestamp.

4. Commits and pushes the updated `state.txt` file to the repository, which allows the action to track the latest fetched question across runs.
