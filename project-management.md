# Project Management

The OpenTelemetry community has limited bandwidth for managing changes which expand the scope of OpenTelemetry, or impact many SIGs (Special Interest Groups) within OpenTelemetry.

These are common scenarios which have this kind of impact:

* Non-trivial changes to the [OpenTelemetry Specification](https://github.com/open-telemetry/opentelemetry-specification).
* Non-trivial changes to the [OpenTelemetry Semantic Conventions](https://github.com/open-telemetry/semantic-conventions).
  * Non-trivial being: introducing new conventions, forming a new SIG around a subject, topic or technology and stabilization efforts.
* A new SIG being formed.
* An existing SIG taking on new work which will affect the OpenTelemetry project as a whole, and will need review from the broader community.

Any changes which fall into one of the above categories must first create a project proposal and gain approval from the GC (Governance Committee) and TC (Technical Committee) before work begins.

The list of current projects, along with their most recent status, is available in our [community projects](https://github.com/open-telemetry/community/projects?query=is%3Aopen) page, which the community can use to get a high-level view of the OpenTelemetry roadmap. Project proposals currently under review can be tracked via their respective [open pull requests](https://github.com/open-telemetry/community/pulls?q=is%3Aopen+is%3Apr+label%3Aarea%2Fproject-proposal).

## Project Proposal

At minimum, projects require the following resources to be successful:

* A clearly defined set of goals and deliverables.
* Timelines for when the deliverables will be ready for review by the broader community.
* Two TC/GC members, or community members delegated by them, to sponsor the project.
  These two sponsors should be from different companies.
* A group of designers and subject matter experts, dedicating a significant amount of their work time to the project. These participants are needed to design the spec, write a set of OTEPs, and create multiple prototypes. This group needs to meet with each other (and with their sponsors) on a regular basis to develop a successful set of proposals.

To propose a project, a**project document** must be created using the [project proposal template](project-template.md) as a guide. This document will be used as the initial proposal for the project.

A project proposal can then be submitted by placing the project document in the [projects](projects/) folder and making a pull request against the community repo.

As the project progresses, the project document should be kept up to date, and the community [README](README.md) should be updated to include any new project meeting information (see [contributing guide](https://github.com/open-telemetry/community/blob/main/CONTRIBUTING.md#updating-sig-information-on-the-readmemd)).

Project leads are encouraged to define timelines for any work which will require public review, and to provide updates to the community in the form of [GitHub Project updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates). We have found that having scoped deliverables leads to an increased cadence in project work, and helps resolve debate. Timelines also help with getting a more coherent public review, as they allow the review community to plan on making themselves available. If timelines prove to be unrealistic, they can be always be updated.

## Project Lifecycle

All projects progress through a lifecycle. Each individual project is tracked using a specific [GitHub Project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) created for this purpose after the proposal is approved. Project leads should use it to plan work and communicate status updates to the community.

The project lifecycle is as follows:

* A **Project Proposal** pull request is created, as described above. The pull request should be labeled as `area/project-proposal`, which opens it up for community review.
  * For a project to be approved, its pull request **must be approved by a majority of GC members**. If a project is approved, and all merge requirements are met, the pull request is merged.
* One a project is **Approved**, project leads create the corresponding GitHub Project and set up meetings and other logistics as documented in the project proposal template.
* For the duration of the project, project leads, along with their GC liaisons, are expected to regularly (at minimum quarterly) [share project updates](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates) to communicate the status of the project to the wider community. The list of possible statuses any given project is static, and it represents the following in OpenTelemetry projects:
  * **_Inactive_**: The project has been approved, but its start date is in the future and no work has commenced. Although allocating a future start date is not required, it lets potential contributors know when they need to make themselves available, and get prepared to begin their work. Subject matter experts and participants who plan to do a lot of work – such as building prototypes – benefit greatly from having a start date, as they can plan for their participation with their employers and coworkers. Projects may remain in _inactive_ state until defined start date is reached.
  * **_On Track_**: The project is making progress, and leads consider the timelines currently defined in the project document achievable with the current resources. Updates may contain information about recent achievements on the project.
  * **_At Risk_**: The project is at risk of not meeting its currently defined timelines. Leads and their GC liaison should discuss actions to bring the project back on track, which may include extending previously agreed timelines or re-scoping deliverables.
  * **_Off Track_**: The project does not have the necessary resources to continue to meet the desired deliverables in a timeline manner, or participation is too low to continue. Leads and their GC liaison should address the level of interest and commitment from the community to re-scope deliverables and timelines, and consider closing the project if not satisfactory, removing the project document from the list of active projects and cancelling meetings and other logistics (e.g. GitHub teams).
  * **_Completed_**: The project is complete. The project document is moved to the [completed projects](projects/completed-projects/) folder, meetings and other logistics are cancelled, and the corresponding GitHub project is closed.