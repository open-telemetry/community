#!/usr/bin/env python3
import argparse
from ghapi.all import GhApi
from tabulate import tabulate

def get_all_issues(api, owner, repo, filter_expression):
    issues = []
    page = 1

    while True:
        query = f"repo:{owner}/{repo} {filter_expression}"
        response = api.search.issues_and_pull_requests(q=query, state='open', per_page=100, page=page)
        if 'items' in response and response['items']:
            issues.extend(response['items'])
            page += 1
        else:
            break

    return issues

def close_issues_with_filter(token, owner, repo, filter_expression, close_message, dry_run):
    api = GhApi(token=token)

    issues = get_all_issues(api, owner, repo, filter_expression)
    
    if dry_run:
        print(f"===DRY RUN MODE===\n")
        print(f"Number of issues matched: {len(issues)}\n")
        print(f"The following issues would be closed:\n")
        table = []
        for issue in issues:
            table.append([issue['number'], issue['title'], issue['created_at'], issue['html_url']])
        print(tabulate(table, headers=["Number", "Title", "Created At", "URL"]))
    else:
        for issue in issues:
            # Add a comment before closing the issue
            api.issues.create_comment(owner, repo, issue['number'], close_message)
            
            # Close the issue
            api.issues.update(owner, repo, issue['number'], state='closed')
            print(f'Closed issue #{issue["number"]}')

def main():
    parser = argparse.ArgumentParser(description='Close issues based on a filter expression in a GitHub repository.')
    parser.add_argument('-token', type=str, help='GitHub personal access token')
    parser.add_argument('-owner', type=str, help='Owner of the repository')
    parser.add_argument('-repo', type=str, help='Name of the repository')
    parser.add_argument('-filter_expression', type=str, help='GitHub filter expression to select issues to close')
    parser.add_argument('-close_message', type=str, help='Message to add when closing the issue')
    parser.add_argument('-dry-run', action='store_true', help='Run the script in dry run mode to see which issues would be impacted')

    args = parser.parse_args()

    close_issues_with_filter(args.token, args.owner, args.repo, args.filter_expression, args.close_message, args.dry_run)

if __name__ == '__main__':
    main()
