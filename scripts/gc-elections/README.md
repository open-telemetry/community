# GC Election Voter Roll Generation
These helper scripts are used to generate the initial voter roll for the OpenTelemetry Governance Committee elections, before any exemptions to the automatic process are considered.

Two environment variables are used across these scripts to configure output files for voters rolls:

* `VOTERS_ROLL_PATH`: the path to the output CSV file with the voters roll and number of contributions (defaults to `./voters-roll.csv`).
* `VOTERS_ROLL_HELIOS_PATH`: the path to the output CSV file with the voters roll in a format accepted by Helios Voting (defaults to `./voters-roll-helios.csv`).

## 1. Generate the voters roll
The `generate-voters-roll.py` script generates a CSV file with the GitHub logins and contributions of the eligible voters for the upcoming elections. It queries the PostgreSQL Data Source backing `opentelemetry.devstats.cncf.io` to get the list of contributors eligible for voting. It then uses the GitHub REST API to get the GitHub login (capitalized) for each user.

Although not required, it is recommended to set a `GITHUB_TOKEN` environment variable with a token with minimal permissions. This avoids GitHub's limits for unauthenticated requests.

Example usage:
```bash
export GITHUB_TOKEN=your_token_here
python generate-voters-roll.py
```

## 2. Create GitHub comments
Using the generated voters roll file indicated by `$VOTERS_ROLL_PATH`, the `create-github-comments.sh` script tags eligible voters on a given GitHub issue, inviting them to vote in the next election.

To workaround limits of mentions on a single comment, the script creates multiple comments in batches of 50 voters.

This script takes two arguments:
* `-i issue_url`: the GitHub issue URL to add comments to (e.g. `https://github.com/open-telemetry/community/issues/1173`)
* `-d bool`: dry-run mode, which only prints the comments that would be created without actually creating them (defaults to `true`).

For this script to work, you must have the GitHub CLI (`gh`) installed and authenticated.

Example usage:
```bash
./create-github-comments.sh -i https://github.com/open-telemetry/community/issues/1173 -d true
```

## 3. Convert voters roll to Helios format
The `convert-voters-roll-to-helios.py` script converts the voters roll file indicated by `$VOTERS_ROLL_PATH` to a format accepted by Helios Voting. It generates a new CSV file in `$VOTERS_ROLL_HELIOS_PATH`  with the GitHub logins of the eligible voters for the upcoming elections.

Example usage:
```bash
python convert-voters-roll-to-helios.py
```