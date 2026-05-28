# GitHub Administration Processes

This document outlines how GitHub administration processes are handled within the OpenTelemetry organization.

## Principles

1. **Transparency**: Document and communicate all changes
2. **Collaboration**: Involve affected SIGs in decision-making processes
3. **Responsiveness**: Respond quickly to maintainer requests

## Guidelines

When possible, changes should be implemented by sending a PR to
[open-telemetry/admin](https://github.com/open-telemetry/admin) (updating the appropriate Terraform
files). This private repository limits security exposure while remaining accessible to all
maintainers. To maintain a single source of truth, manual changes to settings should be avoided
whenever possible.

Changes that can be made via the admin repository include:

- Repository settings (general, collaborators and teams, branch protections)
- Basic GitHub team information (name, description, parent team)

Other changes should be requested or documented via a
[community issue](https://github.com/open-telemetry/community/issues):

- Installing apps
- Repository secrets and variables
- Organization settings

**Note**: Repository-specific GitHub team memberships (e.g., approvers) can be updated directly by
maintainers and do not require a community issue.

### Organization-Level Changes

For changes that affect all repositories in the organization, the admin PR or community issue
should be left open for **a minimum of one week** to allow for community feedback before
implementation.

Potentially disruptive changes should also be posted to the
[#otel-maintainers](https://cloud-native.slack.com/archives/C01NJ7V1KRC) Slack channel when the
community issue or admin PR is opened.

### Single Repository Changes

For changes affecting a single repository owned by a single SIG:
- **If a repository maintainer** opens the admin PR or community issue, the change will be
  implemented as soon as possible
- **If a GitHub admin** opens the admin PR or community issue and a repository maintainer
  approves it (including via positive emoji on the issue), the change will be implemented as soon
  as possible
- **If a GitHub admin** opens the admin PR or community issue and no maintainer replies, the PR
  or issue should be left open for **a minimum of one week** before implementation
- **If someone else** opens the community issue and a repository maintainer approves it
  (including via positive emoji on the issue), the change will be implemented as soon as possible
- **If another maintainer objects after implementation** and asks to revert the change, it will
  be reverted until there is agreement on moving forward (following the
  [conflict resolution process](conflict-resolution.md) if necessary). When requesting a revert,
  maintainers are encouraged to commit to a specific timeline for resolving the underlying issue
  (e.g., "we would like to revert this change; we will work on fixing this problem within the
  next two weeks").

  Changes that affect a single repository owned by multiple SIGs should follow the same
  process, but the change should have the approval of at least one maintainer from each
  affected SIG.

### Request Repository Admin Permissions

By default, maintainers of a repository have the `Maintain` permission instead
of the `Admin` permission. This is to protect the maintainers from making
accidental/unintended changes that are sensitive and/or destructive.

There are cases when the maintainers would want to have `Admin` permission:

- Make necessary changes that are not currently supported by the
  [open-telemetry/admin](https://github.com/open-telemetry/admin) PR process.
- Handle (e.g., accept, publish, merge fixes from a private fork/branch, etc.)
  security advisories.
- Manage environment secrets (i.e. for restricting secret access to protected branches).

Maintainers can request temporary or permanent `Admin` permissions by the
[open-telemetry/admin](https://github.com/open-telemetry/admin) PR process and
get approval from one other repository maintainer (approval from a GitHub Org
Admin is not required). Follow the steps documented
[here](https://github.com/open-telemetry/admin#need-temporary-admin-rights). If
requested, the maintainer will be granted `Admin` permissions, and in return
they must document any changes they make to the repository settings in a file
named `.github/repository-settings.md` in their repository (other than bypassing
branch protection rules in order to merge a security fix from a temporary
private fork).
