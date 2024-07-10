# How we configure repositories

## Naming

Most repositories have a name pattern like this:
`open-telemetry/opentelemetry-foo`. The reason to include `opentelemetry` in the
name of the repository is to simplify repositories distinction in forks. So when
one will fork the repository - fork's name will still indicate that this
repository is from OpenTelemetry organization.

## Repository settings

### General

Everything not mentioned is left at the GitHub default.

* Merging pull requests
  * Allow merge commits: `unchecked`
  * Allow squash merging: :heavy_check_mark:
  * Allow rebase merging: `unchecked`
  * (only allowing squash merging to ensure a clean history)
* Automatically delete head branches: :heavy_check_mark:
  * (so that merged branches are not left lying around)

**A note on discussions**: Discussions are disabled by default when creating a
new repository. Maintainers may enable discussions, but in doing so take on the
responsibility of moderating conversations in accordance with
the [code of conduct](../code-of-conduct.md). Maintainers who enable discussions
are encouraged to configure the discussion categories to suit their needs, e.g.
by removing categories which overlap with issues.

### Collaborators and Teams

* Every repository has three teams associated with it. Typically for the
  repository `opentelemetry-foo` they will be named `foo-triagers`, `foo-approvers`,
  and `foo-maintainers`.
* The `foo-maintainers` team should be a member of the `foo-approvers` team,
  and the `foo-approvers` team should be a member of the `foo-triagers` team.
* Every member of `foo-maintainers` should be included explicitly in `foo-approvers`
  and `foo-triagers` with the "Maintainer" GitHub privileges. This allows
  repository maintainers to invite new approvers and triagers to the team.
* The team `foo-triagers` has `Triage` permissions for the repository. If repository
  is using the Project Boards, `foo-triagers` should have `Write` permissions to
  have access to the Project Boards. Do not add members of `foo-triagers` to
  the CODEOWNERS file, as their approvals should not count towards the required
  number of approvals for merging.
* The team `foo-approvers` has `Write` permissions for the repository.
* The team `foo-maintainers` has `Maintain` permissions for the repository.

If requested, `foo-maintainers` will be granted `Admin` permissions, and in return
they must document any changes they make to the repository settings in a file named
`.github/repository-settings.md` in their repository (other than temporarily
disabling "Do not allow bypassing the above settings", see branch protection rules
below).

### Branches

Default branch: `main`

### Branches > Branch protection rules

The order of branch protection rules is important, from [docs.github.com](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule#about-branch-protection-rules):

> If a repository has multiple protected branch rules that affect the same branches, the rules that include a specific branch name have the highest priority.
>
> Protected branch rules that mention a special character, such as `*`, `?`, or `]`, are applied in the order they were created, so older rules with these characters have a higher priority.

#### Branch protection rule: `main`

Everything not mentioned is unchecked.

* Require a pull request before merging: :heavy_check_mark:
  * Require approvals: :heavy_check_mark:
    * Required number of approvals before merging: `1`
  * Require review from Code Owners: :heavy_check_mark:
* Require status checks to pass before merging: :heavy_check_mark:
  * Require branches to be up to date before merging: :heavy_check_mark:
  * Status checks that are required:
    * `EasyCLA`
* Do not allow bypassing the above settings: :heavy_check_mark:
* Restrict who can push to matching branches: :heavy_check_mark:
  * `Organization administrators, repository administrators, and users with the Maintain role`

**Important:** the only ones of these rules which may be changed are
* Required number of approvals before merging
  * (this can also be more than `1`)
* Require branches to be up to date before merging
  * (this can also be `unchecked`)
* Status checks that are required
  * More status checks can be added, but EasyCLA cannot be removed
* Do not allow bypassing the above settings
  * Maintainers may temporarily disable this

**Note:** `EasyCLA` check should show up automatically. If it doesn't, open a
[Jira ticket](https://jira.linuxfoundation.org/plugins/servlet/desk/portal/4/create/143)
with the EasyCLA team.

#### Branch protection rule: `dependabot/**/**`

Everything not mentioned is unchecked.

* Allow force pushes: :heavy_check_mark:
  * `Everyone` (all users with push access)
    * (so that dependabot can rebase its pull requests)
* Allow deletions: :heavy_check_mark:
  * (so that branches can be deleted after merging)

**Note:** "Require a pull request before merging" and
"Require status checks to pass before merging" both need to be `unchecked` so that
these branches can be directly updated (without going through a pull request).

#### Branch protection rule: `renovate/**/**`

Same as for [`dependabot/**/**`](#branch-protection-rule-dependabot) above.

This branch protection rule is not set up automatically, but can be added for any
repositories that are using [Renovate](https://github.com/apps/renovate).

#### Branch protection rule: `**/**`

Same as for [`main`](#branch-protection-rule-main) above.

### Actions > General

* Fork pull request workflows from outside collaborators
  * `Require approval for first-time contributors who are new to GitHub`
    * (this can also be `Require approval for first-time contributors`)

## CODEOWNERS

Root-level `CODEOWNERS` file on the repository should include superset of
people from both `foo-approvers` and `foo-maintainers`.

## Best practices

It is recommended to follow these best practices:

1. Set up a security scanning tool like, for example, [Github CodeQL](https://docs.github.com/en/code-security/secure-coding/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning).
2. Set up a test coverage scanning tool like, for example, [Codecov](https://codecov.io/).
3. Add status badges for passing builds and scans to the root README.

## Permission changes

In order to change repository permissions (e.g., for temporary or permanent admin access,
adding branch protection rules, or adding a new triagers team),
an issue in the community repository needs to be created to keep track of changes.
Please use the "Repository Maintenance Request" issue template for such requests.
For temporary permission changes, the issue should be kept open until the work is finished and permissions can be reverted again.
