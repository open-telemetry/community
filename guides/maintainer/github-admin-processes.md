# GitHub Administration Process

This document outlines how the GitHub administration process is handled within the OpenTelemetry organization.

## Principles

1. **Transparency**: Document and communicate all changes
2. **Collaboration**: Involve affected SIGs in decision-making processes
3. **Responsiveness**: Move quickly on maintainer requests

## Guidelines

When possible, changes should be implemented by sending a PR to [open-telemetry/admin](https://github.com/open-telemetry/admin) (updating the appropriate Terraform files).

These changes include:

- Repository settings (general, collaborators and teams, branch protections)
- Basic GitHub team information (name, description, parent team)

Other changes should be requested or documented via a [community issue](https://github.com/open-telemetry/community/issues).

These include:

- Installing apps
- Repository secrets and variables
- Organization settings

**Note**: GitHub team memberships can be updated directly by maintainers and do not require a community issue.

### Organization-Level Changes

For changes that affect all repositories in the organization, the admin PR or community issue should be left open for **a minimum of one week** to allow for community feedback before implementation.

Potentially disruptive changes should also be posted to the [#otel-maintainers](https://cloud-native.slack.com/archives/C01NJ7V1KRC) Slack channel when the community issue or admin PR is opened.

### Single Repository Changes

For changes affecting a single repository:
- **If a repository maintainer** opens the admin PR or community issue, the change will be implemented as soon as possible
- **If a GitHub admin** opens the admin PR or community issue and a repository maintainer approves it (including via positive emoji on the issue), the change will be implemented as soon as possible
- **If a GitHub admin** opens the admin PR or community issue and no maintainer replies, the PR or issue should be left open for **a minimum of one week** before implementation
- **If someone else** opens the community issue and a repository maintainer approves it (including via positive emoji on the issue), the change will be implemented as soon as possible
- **If another maintainer objects after implementation** and asks to revert the change, it will be reverted until there is agreement on moving forward (following the [conflict resolution process](conflict-resolution.md) if necessary)
