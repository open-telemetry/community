# How we configure repositories

## Naming

Most repositories have a name pattern like this:
`open-telemetry/opentelemetry-foo`. The reason to include `opentelemetry` in the
name of the repository is to simplify repositories distinction in forks. So when
one will fork the repository - fork's name will still indicate that this
repository is from OpenTelemetry organization.

## Permissions

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
3. The team `foo-triagers` has `Triage` permissions for the repository.
4. The team `foo-approvers` has `Write` permissions for the repository.
5. The team `foo-maintainers` has `Maintain (beta)` permissions for the
   repository.
6. Root-level `CODEOWNERS` file on the repository should include superset of
   people from both `foo-approvers` and `foo-maintainers`.
7. Every repository has Admins group defined as Admins for the repository.
8. Some repositories may include more individuals with `Admin` permissions.
   Typically to help set up repository, CI, web hooks or other administrative
   work.

![image](https://user-images.githubusercontent.com/9950081/57563719-d7b6b300-7355-11e9-9ebb-3c4f549336bc.png)

## Policies

Typically `master` branch is set as default. And protected with the following
policies:

1. Enable `Require pull request reviews before merging` setting. Make sure
   `Require review from Code Owners` is checked.
2. The default setting for `Required approving reviews` is `1` approval. Individual 
   repositores may opt-in for bigger number of required reviews.
3. Every repo MUST enforce the CNCF `EasyCLA` check under the
   `Require status checks to pass before merging` section.
4. It is a good practice to check the `Include administrators` setting.
5. Repository MUST enforce `Restrict who can push to matching branches` setting
   to only allow the members of `foo-maintainers` to push to the `master`
   branch.

![image](https://user-images.githubusercontent.com/9950081/57563714-c5d51000-7355-11e9-80c8-68374e2de2f6.png)

## Best practices

It is recommended to set the following settings:

1. Only set "Allow squash merging" for the Merge button. It will ensure clean
   history for the repository.
