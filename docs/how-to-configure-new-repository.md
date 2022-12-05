# How we configure repositories

## Naming

Most repositories have a name pattern like this:
`open-telemetry/opentelemetry-foo`. The reason to include `opentelemetry` in the
name of the repository is to simplify repositories distinction in forks. So when
one will fork the repository - fork's name will still indicate that this
repository is from OpenTelemetry organization.

## Teams

Documents [Community Membership](../community-membership.md) and
[CONTRIBUTING](../CONTRIBUTING.md) define how permissions are typically set up
for the repository.

1. Every repository has three teams associated with it. Typically for the
   repository `opentelemetry-foo` they will be named `foo-triagers`, `foo-approvers`,
   and `foo-maintainers`. `foo-maintainers` is a child of `foo-approvers`, and
   `foo-approvers` is a child of `foo-triagers`, as it each group always contains
   a subset of people and defines a larger scope of privileges.
2. Every member of `foo-maintainers` should be included in
   `foo-approvers` and `foo-triagers` explicitly, with the "Maintainer" GitHub
   privileges. This allows repository maintainers to invite new approvers and
   triagers to the team.
3. The team `foo-triagers` has `Triage` permissions for the repository. If repository
   is using the Project Boards, `foo-triagers` should have `Write` permissions to
   have access to the Project Boards. Note, by not adding members of `foo-triagers` to
   CODEOWNERS file, repository restricts triagers from counting a triagers approvals for
   PRs. See the [Policies](#policies) section that suggest to ensure that `Require
   review from Code Owners` is checked.

## Repository settings

See [default-repository-settings.md](default-repository-settings.md).

## EasyCLA

Every repository MUST enforce the CNCF `EasyCLA` check under the
`Require status checks to pass before merging` section.
If the check isn't showing, have a CLA manager
[enable the check for the repo](https://project.lfcla.com/#/project/a0941000002wBz4AAE/cla).
Check with the OpenTelemetry's [EasyCLA admins](../assets.md#easy-cla).

## CODEOWNERS

Root-level `CODEOWNERS` file on the repository should include superset of
people from both `foo-approvers` and `foo-maintainers`.

## Best practices

It is recommended to follow these best practices:

1. Set up a security scanning tool like, for example, [Github CodeQL](https://docs.github.com/en/code-security/secure-coding/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning).
2. Set up a test coverage scanning tool like, for example, [Codecov](https://codecov.io/).
3. Add status badges for passing builds and scans to the root README.

## Admin permissions

If requested, `foo-maintainers` will be granted `Admin` permissions, but in return
they must document all changes that are made to the [default-repository-settings.md](default-repository.settings.md)
in a file named `.github/repository-settings.md` in their repository.

## Permission changes

In order to change repository permissions (e.g., for temporary or permanent admin access,
adding branch protection rules, or adding a new triagers team),
an issue in the community repository needs to be created to keep track of changes.
Please use the "Repository Maintenance Request" issue template for such requests.
For temporary permission changes, the issue should be kept open until the work is finished and permissions can be reverted again.
