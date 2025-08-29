# Project Management

The OpenTelemetry community has limited bandwidth for managing changes which expand the scope of OpenTelemetry, or impact many SIGs (Special Interest Groups) within OpenTelemetry.
In addition to gaining wider support from the community, projects help increase awareness across the industry, encouraging participation and improving collaboration.

These are common scenarios which have this kind of impact:

* Non-trivial changes to the [OpenTelemetry Specification](https://github.com/open-telemetry/opentelemetry-specification).
* Non-trivial changes to the [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions).
  * Non-trivial being: introducing new conventions, forming a new SIG around a subject, topic or technology, and stabilization efforts.
* A new SIG being formed, focusing on an initial set of deliverables before stabilizing.
* An existing SIG taking on new work which will affect the OpenTelemetry project as a whole, and will need review from the broader community.

Any changes which fall into one of the above categories must first create a project proposal and gain approval from the GC (Governance Committee) and TC (Technical Committee) before work begins.

The list of current projects is available in the [projects](./projects) directory.
Their most recent status, along with other roadmap items is available on the [OpenTelemetry Roadmap](https://github.com/orgs/open-telemetry/projects/158).

Project proposals currently under review can be tracked via their respective [open pull requests](https://github.com/open-telemetry/community/pulls?q=is%3Aopen+is%3Apr+label%3Aarea%2Fproject-proposal).

## Relation to SIGs, GitHub Projects, and Roadmap
### SIGs

A project is generally required to form a new SIG.
When a project is created to form a new SIG, it should focus on an initial set of deliverables.
After these are completed, the SIG may decide to transition to permanent operation, or dissolve if no more work is required in that area.

A new SIG is not required for every project.
Some projects that require coordination across multiple areas of OpenTelemetry may be led by existing SIGs.
In this case, projects help coordinate resources across SIGs, e.g. reviewing prototypes.

### GitHub Projects (i.e. Boards)

As documented under [Project Lifecycle](#project-lifecycle), all projects require a [GitHub project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) (i.e. a board), and for this to be kept up to date to communicate the status towards milestones and deliverables.

Existing SIGs may also to use GitHub projects freely and independently, to track their ongoing work or communicate status of individual milestones.
This is considered a good practice to provide a clear view of work in progress to the community.

The use of GitHub projects for this purpose does not require the creation of project proposals or approval from GC or TC.

### OpenTelemetry Roadmap

The [OpenTelemetry Roadmap](https://github.com/orgs/open-telemetry/projects/158) contains a high-level view of all major deliverables across the whole project.
This roadmap view is built from the information and status contained in specific GitHub projects across OpenTelemetry.

All approved proposals under the [projects](./projects) directory are implicitly part of the OpenTelemetry Roadmap, along with other SIG-specific projects explicitly added to said roadmap.

For more info see [Roadmap Management](./roadmap-management.md).

## Project Proposal

Projects require the following resources to be successful:

* A clearly defined set of problems to solve, goals, and deliverables.
* Expected timelines for when the deliverables will be ready for review by the broader community.
* Project leads and contributors willing to work on the project, see [Project Staffing](#project-staffing).
* Sponsorship from OpenTelemetry leadership, see [Project Sponsorship](#project-sponsorship).

To propose a project, a **project document** must be created using the [project proposal template](project-template.md) as a guide. This document will be used as the initial proposal for the project.
With the exception of sections labeled as "Optional" or "Post-Approval", all sections of the template must be filled out.

A project proposal can then be submitted by placing the project document in the [projects](projects/) folder and making a pull request against the `community` repo.

As the project progresses, the project document should be kept up to date, and the community [README](README.md) should be updated to include any new project meeting information (see [contributing guide](https://github.com/open-telemetry/community/blob/main/CONTRIBUTING.md#updating-sig-information-on-the-readmemd)).

The project template may be updated and new or existing sections may become required for new projects. Existing projects are not required to update their project documents to the latest template.

Project leads are encouraged to define timelines for any work which will require public review, and to provide updates to the community in the form of [GitHub project updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates). We have found that having scoped deliverables leads to an increased cadence in project work, and helps resolve debate. Timelines also help with getting a more coherent public review, as they allow the review community to plan on making themselves available. If timelines prove to be unrealistic, they can be always be updated.

## Project Staffing

The following staffing requirements must be met for any project proposal.

* Project lead(s), who are willing to bottom line the project and address any issues which are not handled by other project members.
  * If the project requires the creation of a new SIG, these will become SIG maintainers, or approvers for a new Semantic Conventions SIG.
* A set of contributors willing to work on the deliverables outlined in the project proposal.
* If appropriate to ensure success for project (e.g. large spec changes):
  * Engineers willing to write prototypes in at least two languages. Languages should be fairly different from each other, for example Java and Python.
  * Maintainers or approvers from other SIGs committed to reviewing the prototypes.

## Project Sponsorship

All projects require sponsorship, ensuring those leading and working on the project are supported and set up for success.

If a project proposal is led by an existing SIG, TC sponsor and GC liaison for that SIG are assumed to be the sponsor and liaison for the new project.
However, before approving the project, TC sponsorship level must be reviewed by the current TC sponsor.
This ensures that the existing SIG is sufficiently supported if its scope is extended.

If a project involves the creation of a new SIG, it cannot be started until the following have been agreed:

* A [TC](community-members.md#technical-committee) sponsor according to [TC sponsorship requirements](tech-committee-charter.md#sponsorship-requirements).
  * In the case of semantic convention SIGs, [semantic convention maintainers](https://github.com/orgs/open-telemetry/teams/specs-semconv-maintainers) or community members delegated by them can act as sponsors, supported by a _TC Escalation Sponsor_.
* A [GC](community-members.md#governance-committee) liaison to facilitate this SIG's health and ensure project scope remains true to the project description (see [GC check-ins](./gc-check-ins.md)).

## Project Lifecycle

All projects progress through a lifecycle. Each individual project is tracked using a specific [GitHub project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) created for this purpose after the proposal is approved.
Project leads should use it to plan work and communicate status updates to the community. These will be automatically rolled up to the wider OpenTelemetry Roadmap (see [Roadmap Management](./roadmap-management.md) for more info).

The project lifecycle is as follows:

* A **Project Proposal** pull request is created, as described above. The pull request should be labeled as `area/project-proposal`, which opens it up for community review.
  * For a project to be approved, its pull request **must be approved by a majority of GC members**. If a project is approved, and all merge requirements are met, the pull request is merged.
* One a project is **Approved**, project leads create the corresponding GitHub project and set up meetings and other logistics as documented in the project proposal template.
* For the duration of the project, project leads, along with their GC liaisons, are expected to regularly (at minimum quarterly) [share project updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates) to communicate the status of the project to the wider community. The list of possible statuses any given project is static, and it represents the following:
  * **_Inactive_**: The project has been approved, but its start date is in the future and no work has commenced. Although allocating a future start date is not required, it lets potential contributors know when they need to make themselves available, and get prepared to begin their work. Subject matter experts and participants who plan to do a lot of work – such as building prototypes – benefit greatly from having a start date, as they can plan for their participation with their employers and coworkers. Projects may remain in _inactive_ state until defined start date is reached.
  * **_On Track_**: The project is making progress, and leads consider the timelines currently defined in the project document achievable with the current resources. Updates may contain information about recent achievements on the project.
  * **_At Risk_**: The project is at risk of not meeting its currently defined timelines. Leads and their GC liaison should discuss actions to bring the project back on track, which may include extending previously agreed timelines or re-scoping deliverables.
  * **_Off Track_**: The project does not have the necessary resources to continue to meet the desired deliverables in a timeline manner, or participation is too low to continue. Leads and their GC liaison should address the level of interest and commitment from the community to re-scope deliverables and timelines, and consider closing the project if not satisfactory, removing the project document from the list of active projects and cancelling meetings and other logistics (e.g. GitHub teams).
  * **_Completed_**: The project is complete. The project document is moved to the [completed projects](projects/completed-projects/) folder, meetings and other logistics are cancelled, and the corresponding GitHub project is closed.
