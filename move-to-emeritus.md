# Move to Emeritus

This document describes the automated process for identifying inactive community members and moving them to Emeritus status.

## Overview

The [`move-to-emeritus` workflow](.github/workflows/move-to-emeritus.yml) runs monthly and checks whether members of each repo's Maintainer, Approver, and Triager teams have been active in the past **4 months**. For each repo where inactive members are found, the workflow either:

- Opens a **pull request** to move the inactive members to the `Emeritus` section of the repo's README, or
- Opens a **follow-up issue** if the README is already up to date but the members still need to be removed from GitHub teams, Slack channels, and package managers.

The workflow uses the `opentelemetrybot` account to create a fork, push the change, and open the cross-repo PR.

## Schedule

The workflow runs automatically at **05:00 UTC on the 1st of every month**. It can also be triggered manually via [workflow dispatch](https://github.com/open-telemetry/community/actions/workflows/move-to-emeritus.yml).

## Activity checks

The inactivity window is a rolling **4-month** period. A member is considered active if they performed any of the role-appropriate actions below on any repository assigned to their team during that window.

### Triager

A triager is considered active if they:

- Added a comment on an issue or pull request
- Added or removed a label on an issue or pull request
- Closed an issue

### Approver

An approver is considered active if they:

- Added a comment on a pull request
- Added a comment on an issue
- Submitted a review on a pull request

### Maintainer

A maintainer is considered active if they:

- Added a comment on a pull request
- Added a comment on an issue
- Submitted a review on a pull request
- Authored a pull request
- Merged a pull request

### Activity exclusion

Comments, reviews, or events on the move-to-emeritus PR itself (e.g. a member replying to or approving their own removal PR) are **not** counted as activity. This prevents members from staying active solely by reacting to the PR that proposes their transition.

## Repos checked

The workflow checks all public repositories assigned to a team, subject to the following filters.

### Repos skipped entirely

The following repos are excluded because they are either very low traffic, stable without regular commits, managed outside GitHub, or inherit their membership from other repos:

- `community`
- `cpp-build-tools`
- `govanityurls`
- `opentelemetry-go-build-tools`
- `opentelemetry-network`
- `opentelemetry-specification`
- `semantic-conventions`
- `opentelemetry-proto`
- `opentelemetry-proto-java`
- `opentelemetry-java-examples`
- `semantic-conventions-java`
- `sig-contributor-experience`
- `sig-developer-experience`
- `sig-end-user`

### Repos with restricted team checks

For some repos only specific teams are checked (all other teams assigned to the repo are ignored):

| Repo | Teams checked |
|------|---------------|
| `opentelemetry.io` | `docs-triagers`, `docs-approvers`, `docs-maintainers`, `blog-approvers` |

### Teams skipped per repo

For some repos, teams whose name contains certain keywords are skipped:

| Repo | Skipped team keywords | Reason |
|------|-----------------------|--------|
| `opentelemetry-js` | `browser` | Browser team is not required to be active in this repo |
| `opentelemetry-js-contrib` | `browser`, `javascript-contrib-triagers` | Contrib triager works similarly to CODEOWNERS |
| `opentelemetry-collector-releases` | `helm`, `collector-contrib` | Low activity level by design |
| `weaver` | `semconv` | Complex team that won't always be active |

## What the workflow does

1. **Fetches all teams** in the `open-telemetry` org matching the role keywords (`maintainer`, `approver`, `triager`).
2. **Checks activity** for every member of each team across all repos assigned to that team, using the role-appropriate criteria above.
3. **For each repo with inactive members**, fetches the repo's README and attempts to:
   - Remove the member from their current role section (Maintainers, Approvers, or Triagers).
   - Add them to the `Emeritus` section.
4. **If the README was modified**, opens (or updates) a pull request from `opentelemetrybot`'s fork with the title `chore: Move inactive members to emeritus`.
5. **If the README was already up to date** (the member is already in Emeritus), opens (or updates) a follow-up issue titled `chore: Remove inactive members from teams and channels` to remind maintainers to complete the off-boarding steps.

## How maintainers should address the PRs

When a `chore: Move inactive members to emeritus` PR is opened in your repo:

1. **Review the list of flagged members.** Confirm that the listed members have genuinely been inactive. The PR body includes the cutoff date so you can cross-check their recent activity on GitHub.

2. **Reach out if needed.** Before merging, consider pinging the member. They may be on leave or contributing in ways not captured by GitHub activity.

3. **Wait at least 14 days before merging**, to give flagged members a chance to respond (e.g. if they are on vacation). The PR can be merged sooner if:
   - All flagged members have approved the PR or otherwise acknowledged the transition, or
   - The maintainers already know the member can no longer contribute.

4. **Do not merge solely to dismiss the PR.** The PR also carries a checklist of off-boarding steps that must be completed:
   - [ ] Remove the member from the listed GitHub team(s) at [github.com/orgs/open-telemetry/teams](https://github.com/orgs/open-telemetry/teams)
   - [ ] Remove the member from any relevant private Slack channels
   - [ ] Remove the member from any relevant package managers used for publishing

5. **Complete all checklist items before or immediately after merging.** If the README update is merged but the checklist is skipped, the automated script will detect this on the next run and open a follow-up issue.

6. **For complex situations**, such as uncertainty about a member's status or special circumstances, reach out to your [GC liaison](./community-members.md) for guidance.

## How maintainers should address the follow-up issues

If the README already reflects the member's Emeritus status but a `chore: Remove inactive members from teams and channels` issue is opened, it means the off-boarding tasks were not completed after the last PR was merged. A maintainer should:

1. Remove the listed members from their GitHub teams.
2. Remove them from any relevant private Slack channels.
3. Remove them from any package managers used for publishing.
4. Close the issue once all items are done.

## Running the script locally

```bash
# Check all repos and print an activity report (read-only, no changes made)
GITHUB_TOKEN=<token> python scripts/move-to-emeritus.py

# Check only specific repos
GITHUB_TOKEN=<token> python scripts/move-to-emeritus.py --repo opentelemetry-collector opentelemetry-python

# Show why each member was marked active or inactive
GITHUB_TOKEN=<token> python scripts/move-to-emeritus.py --debug

# Create PRs and issues (requires a token with fork + PR creation access)
GITHUB_TOKEN=<token> python scripts/move-to-emeritus.py --create-prs
```

The script is safe to re-run: it will update existing open PRs/issues rather than create duplicates.
