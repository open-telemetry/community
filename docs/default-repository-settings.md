# Default repository settings

## General

Everything not mentioned is left at the GitHub default.

* Merging pull requests
  * Allow merge commits: `unchecked`
  * Allow squash merging: :heavy_check_mark:
  * Allow rebase merging: `unchecked`
  * (only allowing squash merging to ensure a clean history)
* Automatically delete head branches: :heavy_check_mark:
  * (so that merged branches are not left lying around)

## Collaborators and Teams

* The team `foo-triagers` has `Triage` permissions for the repository. If repository
  is using the Project Boards, `foo-triagers` should have `Write` permissions to
  have access to the Project Boards. Do not add members of `foo-triagers` to
  the CODEOWNERS file, as their approvals should not count towards the required
  number of approvals for merging.
* The team `foo-approvers` has `Write` permissions for the repository.
* The team `foo-maintainers` has `Maintain` permissions for the repository.

## Branches

Default branch: `main`

## Branches > Branch protection rules

The order of branch protection rules is important, from [docs.github.com](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule#about-branch-protection-rules):

> If a repository has multiple protected branch rules that affect the same branches, the rules that include a specific branch name have the highest priority.
>
> Protected branch rules that mention a special character, such as `*`, `?`, or `]`, are applied in the order they were created, so older rules with these characters have a higher priority.

### Branch protection rule: `main`

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
  * This can also be more than `1`
* Require branches to be up to date before merging
  * This can also be `unchecked`
* Status checks that are required
  * More status checks can be added, but EasyCLA cannot be removed
* Do not allow bypassing the above settings
  * Maintainers may temporarily disable this

### Branch protection rule: `dependabot/**/**`

Everything not mentioned is unchecked.

* Allow force pushes: :heavy_check_mark:
  * `Everyone` (all users with push access)
    * (so that dependabot can rebase its pull requests)
* Allow deletions: :heavy_check_mark:  
  * (so that branches can be deleted after merging)

### Branch protection rule: `**/**`

Same as for [`main`](#branch-protection-rule-main) above.
