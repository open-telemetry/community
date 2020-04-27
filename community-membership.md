# Community membership

Last updated: 2020-03-04

This doc outlines the various responsibilities of contributor roles in
OpenTelemetry. The OpenTelemetry project is subdivided into subprojects under
(predominantly, but not exclusively) language-focused SIGs (Special Interest
Group). Responsibilities for most roles are scoped to these subprojects (repos).

The OpenTelemetry Governance Committee owns this document and process until
delegated. They can be reached via e-mail cncf-opentelemetry-governance@lists.cncf.io.

| **Role**   | **Responsibilities**                                  | **Requirements**                                             | **Defined by**                                               |
| ---------- | ----------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| member     | active contributor in the community.  reviewer of PRs | sponsored by 2 approvers or maintainers. multiple contributions to the project. | OpenTelemetry GitHub org member.                             |
| approver   | approve accepting contributions                       | highly experienced and active reviewer + contributor to a subproject | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners) in GitHub |
| maintainer | set direction and priorities for a subproject         | demonstrated responsibility and excellent technical judgement for the subproject | [CODEOWNERS](https://help.github.com/en/articles/about-code-owners), GitHub Team and repo ownership in GitHub |

## New contributors

New contributors should be welcomed to the community by existing members, helped
with PR workflow, and directed to relevant documentation and communication
channels.

## Established community members

Established community members are expected to demonstrate their adherence to the
principles in this document, familiarity with project organization, roles,
policies, procedures, conventions, etc., and technical and/or writing ability.
Role-specific expectations, responsibilities, and requirements are enumerated
below.

## Member

Members are continuously active contributors in the community. They can have
issues and PRs assigned to them. Members are expected to participate in SIG or
SIGs and remain active contributors to the community.  

Defined by: Member of the OpenTelemetry GitHub organization

### Requirements

- Enabled [two-factor
  authentication](https://help.github.com/articles/about-two-factor-authentication)
  on their GitHub account
- Have made multiple contributions to the project or community. Contributions
  may include, but is not limited to:
  - Authoring or reviewing PRs on GitHub
  - Filing or commenting on issues on GitHub
  - Contributing to SIGs, subprojects, or community discussions (e.g. meetings,
    chat, email, and discussion forums)
- [Joined the gitter channel ](https://gitter.im/open-telemetry/community)
- Have read the [contributor
  guide](https://github.com/open-telemetry/community/blob/master/CONTRIBUTING.md)
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
  - Complete every item on the checklist ([preview the current version of the
    template](https://github.com/open-telemetry/community/blob/master/.github/ISSUE_TEMPLATE/membership.md))
  - Make sure that the list of contributions included is representative of your
    work on the project.
- Have your sponsoring reviewers reply confirmation of sponsorship: `+1`
- Once your sponsors have responded, your request will be reviewed by the
  Governance Committee.  Any GC member can review the requirements and add
  Members to the GitHub org. 

### Responsibilities and privileges

- Responsive to issues and PRs assigned to them
- Active owner of code they have contributed (unless ownership is explicitly
  transferred)
  - Code is well tested
  - Tests consistently pass
  - Addresses bugs or issues discovered after code is accepted
- Members can review and approve via the GitHub workflow.  This review work is
  not sufficient to merge a PR.  There will still need to be a review by an
  *approver*.
- Members can be assigned to issues and PRs, and people can ask members for
  reviews with a `/cc @username`.

Note: members who frequently contribute code are expected to proactively perform
code reviews and work towards becoming an *approver* for the subproject that
they are active in.  Acceptance of code contributions requires at least one
approver in addition to the reviews by *members.*

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
core components may have higher bar of becoming an approver. Some approvers may
only be doing issues triage and have no approval rights.

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

### Requirements

The process for becoming a Maintainer should be defined in the SIG charter of
the SIG owning the subproject. Unlike the roles outlined above, the Owners of a
subproject are typically limited to a relatively small group of decision makers
and updated as fits the needs of the subproject.

The following apply to the subproject for which one would be an owner.

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

### Responsibilities and privileges

The following apply to the subproject for which one would be an owner.

- Make and approve technical design decisions for the subproject.
- Set technical direction and priorities for the subproject.
- Define milestones and releases.
  - Decides on when PRs are merged to control the release scope. 
- Mentor and guide approvers, reviewers, and contributors to the subproject.
- Escalate *reviewer* and *maintainer* workflow concerns (i.e. responsiveness,
  availability, and general contributor community health) to the TC.
- Ensure continued health of subproject:
  - Adequate test coverage to confidently release
  - Tests are passing reliably (i.e. not flaky) and are fixed when they fail
- Ensure a healthy process for discussion and decision making is in place.
- Work with other maintainers to maintain the project's overall health and
  success holistically.
