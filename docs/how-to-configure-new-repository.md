# How we configure repositories

## Naming

Most repositories have a name pattern like this:
`open-telemetry/opentelemetry-foo`. The reason to include `opentelemetry` in the
name of the repository is to simplify repositories distinction in forks. So when
One will fork the repository - fork's name will still indicate that this
repository is from OpenTelemetry organization.

## Permissions

Documents [Community Membership](../community-membership.md) and
[CONTRIBUTING](../CONTRIBUTING.md) define how permissions are typically set up
for the repository.

1. Every repository has two teams associated with it. Typically they will be
   named `foo-approvers` and `foo-maintainers`. `foo-maintainers` is a child of
   `foo-approvers` as it always contains subset of people and defines larger
   scope of privileges.
2. Both teams has `Write` permissions for the repository.
3. Root-level `CODEOWNERS` file on the repository should include superset of
   people from both teams.
4. Every repository has Admins group defined as Admins for the repository.
5. Some repositories may include more individuals outside of approvers and
   maintainers teams with the `Write` permissions. Typically for issues tracking
   and triage purpose.
6. Some repositories may include more individuals with `Admin` permissions.
   Typically to help set up repository, CI, web hooks or other administrative
   work.

![image](https://user-images.githubusercontent.com/9950081/57563719-d7b6b300-7355-11e9-9ebb-3c4f549336bc.png)

## Policies

Typically `master` branch is set as default. And protected with the following
policies:

1. Enable `Require pull request reviews before merging` setting. Make sure
   `Require review from Code Owners` is checked.
2. Every repo MUST enforce `cla/linuxfoundation` check for `Require status
   checks to pass before merging` section.
3. It is a good practice to check the `Include administrators` setting.
4. Repository MUST enforce `Restrict who can push to matching branches` setting
   to only allow the members of `foo-maintainers` to push to the `master`
   branch.

![image](https://user-images.githubusercontent.com/9950081/57563714-c5d51000-7355-11e9-80c8-68374e2de2f6.png)
