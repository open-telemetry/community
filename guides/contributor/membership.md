# Membership, Roles, and Responsibilities

OpenTelemetry is a project by, and for, its community. This document outlines
the various roles and responsibilities of members, as well as the requirements
for achieving each role. We encourage you to consider becoming a long-term
contributor to the project, and moving up the ladder from member, all the way to
maintainer!

## Membership Levels

| **Role**              | **Responsibilities**                                              | **Requirements**                                                                                                                                 | **Defined by**                                                                                                 |
|-----------------------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| member                | active contributor in the community.  reviewer of PRs             | sponsored by 2 approvers or maintainers. multiple contributions to the project.                                                                  | OpenTelemetry GitHub org member.                                                                               |
| triager               | assist with project management and backlog organization.          | nominated by a maintainer. help with issues for one month.                                                                                       | CONTRIBUTING, CODEOWNERS, or the README.                                                                       |
| approver              | approve incoming contributions                                    | highly experienced and active reviewer + contributor to a subproject                                                                             | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners) in GitHub                                  |
| maintainer            | set direction and priorities for a subproject                     | demonstrated responsibility and excellent technical judgement for the subproject                                                                 | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners), GitHub Team and repo ownership in GitHub  |
| emeritus              | position of honor for former maintainers, approvers, and triagers | must have previously held a community role and not have been removed from that role for a [Code of Conduct](../../code-of-conduct.md) violation. | Listed as an emeritus maintainer/approver/triager in CONTRIBUTING, CODEOWNERS, or README                       |
| specification sponsor | trusted collaborators for the specification                       | nominated by [Technical Committee][]                                                                                                             | Listed in [Community Members -> Specification and Protos](../../community-members.md#specifications-and-proto) |

## New contributors

If you're a new contributor reading this guide -- welcome! We're excited you're
here. New contributors should be welcomed and encouraged to participate in the
project. Remember, contributions aren't limited to writing code, either --
reporting bugs, writing documentation, working on the website, or being a part
of our community management are all valuable.

## Established contributors

Established community members are expected to demonstrate their adherence to the
principles in this document, familiarity with project organization, roles,
policies, procedures, conventions, etc., and technical and/or writing ability.
Role-specific expectations, responsibilities, and requirements are enumerated
below.

## Member

Members are continuously active contributors in the community. They can have
issues and PRs assigned to them. Members are expected to participate in SIG or
SIGs and remain active contributors to the community.

Members can vote in the [Governance Committee][] elections.

Defined by: Member of the OpenTelemetry GitHub organization

### Requirements

- Enabled [two-factor
  authentication](https://help.github.com/articles/about-two-factor-authentication)
  on their GitHub account
- Have made multiple contributions to the project or community. Contributions
  may include, but is not limited to:
  - Authoring or reviewing PRs on GitHub
  - Filing or commenting on issues on GitHub
  - Organizing and running activities (e.g. events, surveys) within the OpenTelemetry community
  - Contributing to SIGs, subprojects, or community discussions (e.g. meetings,
    chat, email, and discussion forums)
- [Joined the Slack channel](https://cloud-native.slack.com/archives/CJFCJHG4Q)
  - [Get an invite to join CNCF](https://slack.cncf.io/)
- Have read the [contributor guide](../../guides/contributor)
- Actively contributing to 1 or more subprojects.
- Sponsored by 2 approvers. Note the following requirements for sponsors:
  - Sponsors must have close interactions with the prospective member - e.g.
    code/design/proposal review, coordinating on issues, etc.
  - Sponsors must be approvers or maintainers in at least 1 CODEOWNERS file
    in any repo in the OpenTelemetry org.
  - Sponsors must be from multiple member companies to demonstrate integration
    across community.
- [Open an
  issue](https://github.com/open-telemetry/community/issues/new?template=membership.md&title=REQUEST%3A%20New%20membership%20for%20%3Cyour-GH-handle%3E)
  against the
  [OpenTelemetry/community](https://github.com/open-telemetry/community) repo
  - Ensure your sponsors are `@mentioned` on the issue
  - Complete every item on the checklist
    ([preview the current version of the template](../../.github/ISSUE_TEMPLATE/membership.md))
  - Make sure that the list of contributions included is representative of your
    work on the project.
- Have your sponsoring reviewers reply confirmation of sponsorship: `I support`
- Once your sponsors have responded, your request will be reviewed by the
  Technical Committee (TC).  Any TC member can review the requirements and add
  Members to the GitHub org.

### Responsibilities and privileges

- Responsive to issues and PRs assigned to them
- Active owner of code they have contributed (unless ownership is explicitly
  transferred)
  - Code is well tested
  - Tests consistently pass
  - Addresses bugs or issues discovered after code is accepted
- Can vote in the [Governance Committee][] elections (see [Members of Standing][])
- Members can review and approve via the GitHub workflow.  This review work is
  not sufficient to merge a PR.  There will still need to be a review by an
  *approver*.
- Members can be assigned to issues and PRs, and people can ask members for
  reviews with a `/cc @username`.

Note: members who frequently contribute code are expected to proactively perform
code reviews and work towards becoming an *approver* for the subproject that
they are active in.  Acceptance of code contributions requires at least one
approver in addition to the reviews by *members.*

## Triager

Triagers assist the maintainers and approvers with project management and
backlog organization. The specific workflows and triage requirements depend on
the project, and are set by the project maintainers.

Defined by: [Triage permissions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization#permissions-for-each-role),
with the names of the current Triagers committed to git, either in CONTRIBUTING,
CODEOWNERS, or the bottom of the README.

Triagers may be code contributors, but writing code is not a requirement for
becoming a triager. Triagers are encouraged to be active participants in project
meetings, chat rooms, and other discussion forums.

Triagers belong to a specific [SIG][].
There can be multiple triager groups in a single SIG. For example, there can be
different triager groups for different repositories owned by a SIG, or different
triager groups for different areas of expertise (e.g. different languages in the
documentation). A SIG can set up additional triager groups for organizational
purposes to help make it easier to refer to a group of contributors, such as for
ownership within a repository, through requesting PR reviews, or for contacting
elsewhere on GitHub.

### Requirements

- Nominated by a maintainer, with no objections from other maintainers.
- Consistently interact with the community and help with issues for at least 1 month.

### Responsibilities and privileges

- Have an understanding of the goals and workflows defined by the maintainers.
- Respond to new PRs and Issues by asking clarifying questions.
- Organize the backlog by applying labels, milestones, assignees, and projects.

## Approver

Code approvers are able to both review and approve code contributions, as well
as help maintainers triage issues and do project management.

While code review is focused on code quality and correctness, approval is
focused on holistic acceptance of a contribution including: backwards/forwards
compatibility, adhering to API and flag conventions, subtle performance and
correctness issues, interactions with other parts of the system, etc.

Defined by: [CODEOWNERS
workflow](https://help.github.com/en/articles/about-code-owners).

Approver status can be scoped to a part of the codebase. For example, critical
core components may have higher bar for becoming an approver.

Approvers belong to a specific [SIG][].
There can be multiple approver groups in a single SIG. For example, there can be
different approver groups for different repositories owned by a SIG, or different 
approver groups for different areas of expertise (e.g. different languages in the
documentation). A SIG can set up additional approver groups for organizational
purposes to help make it easier to refer to a group of contributors, such as for
ownership within a repository, through requesting PR reviews, or for contacting
elsewhere on GitHub.


### Requirements

The following apply to the part of the codebase for which one would be an
approver in the `CODEOWNERS` files.

- Reviewer of the codebase for at least 1 month
- Reviewer for or author of at least 10 substantial PRs to the codebase,
  with the definition of substantial subject to the maintainer's discretion
  (e.g. refactors/adds new functionality rather than one-line pulls).
- Nominated by a maintainer
  - With no objections from other maintainers
  - Done through PR to update the `CODEOWNERS`.

### Responsibilities and privileges

The following apply to the part of the codebase for which one would be an
approver in the `CODEOWNERS` files.

- Approver status may be a precondition to accepting large code contributions
- Demonstrate sound technical judgement (may be asked to step down by a maintainer if they lose confidence of the maintainers)
- Responsible for project quality control via code reviews
  - Focus on holistic acceptance of contribution such as dependencies with other
    features, backwards / forwards compatibility, API and flag definitions, etc
- Responsible for technical quality control of the [documentation](http://docs.opentelemetry.io/), related to their project
- Expected to be responsive to review requests (inactivity for more than 1 month may result in suspension until active again)
- Mentor contributors and reviewers
- May approve code contributions for acceptance

## Maintainer

Note: This is a generalized high-level description of the role, and the
specifics of the maintainer role's responsibilities and related processes *MUST*
be defined for individual SIGs or subprojects.

Maintainers are the technical authority for a subproject in the OpenTelemetry
project. They *MUST* have demonstrated both good judgement and responsibility
towards the health of that subproject. Maintainers *MUST* set technical
direction and make or approve design decisions for their subproject - either
directly or through delegation of these responsibilities.

Defined by: GitHub organization ownership, permissions and entry in `CODEOWNERS`
files.

Maintainers belong to a specific [SIG][].
There can be multiple maintainer groups in a single SIG. For example, there can be
different maintainer groups for different repositories owned by a SIG, or different 
maintainer groups for different areas of expertise (e.g. different languages in the
documentation). A SIG can set up additional maintainer groups for organizational
purposes to help make it easier to refer to a group of contributors, such as for
ownership within a repository, through requesting PR reviews, or for contacting
elsewhere on GitHub.

### Requirements

Unlike the roles outlined above, the maintainers of a subproject are typically
limited to a relatively small group of decision makers and updated as fits
the needs of the subproject.

The following apply to the subproject for which one would be a maintainer.

- Deep understanding of the technical goals and direction of the subproject
- Deep understanding of the technical domain (specifically the language) of the
  subproject
- Sustained contributions to design and direction by doing all of:
  - Authoring and reviewing proposals
  - Initiating, contributing and resolving discussions (emails, GitHub issues,
    meetings)
  - Identifying subtle or complex issues in designs and implementation PRs
- Directly contributed to the subproject through implementation and / or review
- Aligning with the overall project goals, specifications and design principles
  defined by Technical Committee (TC). Bringing general questions and requests
  to the discussions as part of specifications project.
- Scheduling SIG meetings using the [OpenTelemetry Public
  Calendar](../../docs/how-to-handle-public-calendar.md).

### Responsibilities and privileges

The following apply to the subproject for which one would be a maintainer.

- Make and approve technical design decisions for the subproject.
- Set technical direction and priorities for the subproject.
- Define milestones and releases.
  - Decides on when PRs are merged to control the release scope.
- Mentor and guide approvers, reviewers, and contributors to the subproject.
- Escalate *reviewer*, *approver*, *maintainer* and other concerns to leadership
  via appropriate channels:
  - Workflow concerns (i.e. responsiveness, availability, and general
    contributor community health) should be escalated to the corresponding GC
    liaison for the subproject, either as part of regular
    [GC check-ins](../../gc-check-ins.md) or ad-hoc.
  - [Code of Conduct](../../code-of-conduct.md) violations, following documented
    process, should be reported to the GC.
  - Technical conflicts, after other internal approaches have been exhausted,
    should be escalated to the TC (see relevant
    [guidance](../maintainer/conflict-resolution.md)).
- Ensure continued health of subproject:
  - Adequate test coverage to confidently release
  - Tests are passing reliably (i.e. not flaky) and are fixed when they fail
  - Up-to-date and accurate [documentation](http://docs.opentelemetry.io/)
- Ensure a healthy process for discussion and decision making is in place.
- Work with other maintainers to maintain the project's overall health and
  success holistically.

See also the blog post [A day in the life of an OpenTelemetry
maintainer](https://opentelemetry.io/blog/2025/day-opentelemetry-maintainer/)
for more details on the day-to-day tasks required of maintainers.

### Becoming a Maintainer

Unless stated otherwise in a SIG charter ratified by the Technical Committee,
a new maintainer is elected by vote of the existing maintainers of the SIG.
The vote is officially started when a pull request to add a new maintainer
is opened, and ends when the pull request is merged. The pull request may be
merged when the following conditions are met:

- The person being nominated has accepted the nomination by approving the pull request
- All maintainers have approved the pull request OR a majority of maintainers
  have approved the pull request and no maintainer has objected by requesting
  changes on the pull request. In the case that all maintainers have not given
  approval, the pull request should stay open for a minimum of 5 days before merging.

The nominee is considered a maintainer after the pull request is merged.

#### Self-nomination is encouraged

If you feel like you meet the requirements above and are willing to take on the
additional responsibilities and privileges of being a maintainer, it is
recommended that you approach an existing maintainer about sponsoring your bid
to become a maintainer. After you and your sponsor have discussed the role
and its additional requirements and responsibilities, they may approach the other
maintainers about a vote to confirm you as a new maintainer. If the maintainer
does not believe you are ready for the role, or the subproject is not in need
of additional maintainers, they may suggest an alternate role or growth areas
in order to improve your chances to become a maintainer in the future.

## Emeritus Maintainer/Approver/Triager

For any healthy open source project, it is inevitable that contributors may move
on, step down, or otherwise reduce their role in the project for some period of
time. These people may have expertise in one or more area of the project, but no
longer have time to actively contribute or approve contributions. They are
encouraged to reflect this by adding themselves to the `emeritus` section of the
CONTRIBUTING, CODEOWNERS, or README of the subproject they are stepping away
from. Company affiliations should be removed at this time as they may change
and may not be reflected accurately in the future. GitHub usernames listed under the
`emeritus` section should be removed from the approvers list, and will no longer
have any official responsibilities with the project. When a contributor returns
to being more active, they may be promoted back to their previous position at
the discretion of the current maintainers following the process defined above.

## Specification Sponsor

Specification sponsors are trusted collaborators of the technical committee, and
work to review, approve, and sponsor [opentelemetry-specification][] issues and
PRs.

Members are defined
in [Community Members -> Specification and Protos](../../community-members.md#specifications-and-proto)
and are members of the `spec-sponsors` team (TODO: add link to github team when
available). Specification sponsors SHOULD list
their [areas of interest](../../areas-of-interest.md).

### Requirements

Specification sponsors are trusted to drive specification work which can be
complex and highly impactful to downstream language SIGs and to the
OpenTelemetry project as a whole. Approvals from specification sponsors count
towards the approvals required to merge specification PRs. Therefore, there is a
high bar to becoming a specification sponsor.

- Contributor to OpenTelemetry project for at least 1 year
- Has been the reviewer or author (through the sponsorship of another
  specification sponsor) of at least 10 substantial PRs to specification or
  related repositories
- Demonstrated sound technical judgement, and a deep understanding of the
  specification and the OpenTelemetry project
- Nominated by technical committee member (
  see [becoming a specification sponsor](#becoming-a-specification-sponsor))

### Responsibilities and privileges

- Review, respond to, and approve issues / PRs when tagged or when within areas
  of interest.
- Sponsor issues, taking responsibility to be point on requirement gathering,
  developing solutions and prototypes, writing PRs, and responding to /
  incorporating PR feedback. This can be done by the sponsor themselves, or by
  another collaborator who is sponsored. If sponsoring another collaborator, the
  sponsor should work with them to ensure the work is consistent with existing
  specification.
- Demonstrate sound technical judgement.
- Frequently attend the specification SIG meeting where issues and PRs are
  synchronously discussed.

Sponsors who are unable to fulfill their responsibilities (e.g. no longer have
time available to commit) are expected to be moved
to [emeritus](#emeritus-maintainerapprovertriager) sponsors. The TC may also
vote to move a sponsor to emeritus.

### Becoming a Specification Sponsor

Technical committee members nominate specification sponsors by opening a PR to
the community repo to add the nominee to the specification sponsor list. The
vote is officially started when a pull request is opened, and ends when the pull
request is merged. The pull request may be merged when the following conditions
are met:

- The person being nominated has accepted the nomination by approving the pull
  request.
- All TC members have approved the pull request or a majority of TC members have
  approved the pull request and no other TC member has objected by requesting
  changes on the pull request. In the case that all TC members have not given
  approval, the pull request should stay open for a minimum of 10 days before
  merging.

The nominee is considered a specification sponsor after the pull request is
merged. The merger should update the `spec-sponsors` team with the new member.

[Governance Committee]: ../../governance-charter.md
[Technical Committee]: ../../tech-committee-charter.md
[opentelemetry-specification]: https://github.com/open-telemetry/opentelemetry-specification
[Members of Standing]: ../../governance-charter.md#members-of-standing
[SIG]: ./processes.md#special-interest-groups-sigs
