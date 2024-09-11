# GitHub Issue Follow-up Labeler

This script automates the process of adding a "triage:followup" label to GitHub issues that require attention after a period of inactivity. It's designed to help maintainers keep track of issues that have been in a decision-making phase for more than two weeks without recent activity.

## Features

- Analyzes open issues in a specified GitHub repository
- Considers both events and comments as meaningful activity
- Adds "triage:followup" label to issues that meet specific criteria
- Supports dry-run mode for testing
- Allows testing of individual issues

## Prerequisites

- Python 3.6+
- PyGithub library
- GitHub Personal Access Token with appropriate permissions

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/github-issue-followup-labeler.git
   cd github-issue-followup-labeler
   ```

2. Install the required dependencies:
   ```
   pip install PyGithub pytz
   ```

3. Set up your GitHub Personal Access Token as an environment variable:
   ```
   export GITHUB_TOKEN=your_token_here
   ```

## Usage

### Running the script

```
python app.py owner/repo [--dry-run]
```

- Replace `owner/repo` with the GitHub repository you want to analyze (e.g., `octocat/Hello-World`).
- Use the `--dry-run` flag to run the script without making any changes to issues.

### Testing a specific issue

```
python app.py owner/repo --test-issue ISSUE_NUMBER
```

- Replace `ISSUE_NUMBER` with the number of the issue you want to analyze.

## How it works

The script:

1. Fetches open issues from the specified repository.
2. For each issue with a "triage:deciding:*" label:
   - Retrieves all events and comments associated with the issue.
   - Checks if the issue has had any meaningful activity since the last triage occurred.
   - If recent activity is found and other criteria are met, adds the "triage:followup" label.
