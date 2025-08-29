# OpenTelemetry Roadmap Management

The **[OpenTelemetry Roadmap](https://github.com/orgs/open-telemetry/projects/158)** provides a high-level, cross-cutting view of major initiatives, their status, and target completion dates across the entire project.
This consolidated view, managed by the GC (Governance Committee) and TC (Technical Committee), helps community members and adopters understand the project's direction and when to expect key deliverables.

## Consolidated Roadmap View

Publicly available at **[OpenTelemetry Roadmap](https://github.com/orgs/open-telemetry/projects/158)**, this view is currently backed by issues in the [open-telemetry/.roadmap](https://github.com/open-telemetry/.roadmap) repository.
These issues are populated automatically from a selected subset of GitHub [projects](https://github.com/orgs/open-telemetry/projects?query=is%3Aopen) in order to overcome [limitations](https://github.com/orgs/community/discussions/157993) in GitHub's native [project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects) functionality.

Some of these projects correspond to initiatives entirely driven within the scope of specific SIGs (Special Interest Groups), and some correspond to cross-cutting initiatives that require SIGs –existing or needing creation– to follow the [Project Management](./project-management.md) process.

Individual OpenTelemetry projects are managed by their leads independently, with the support from their TC sponsor and GC liaison, as documented in their respective charters.
Jointly, they are responsible for keeping the project details up-to-date.

Specifically, the following project details are synced into their corresponding `.roadmap` issues, for presentation purposes:

* **Project Name**: The name of the project, representing the overall initiative.
* **README**: A summary of the project's goals and deliverables.
* **Status Update**: The latest reported [project update](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/sharing-project-updates). In particular:
  * **Status**: e.g., _On Track_, _At Risk_, _Completed_, etc.
  * **Start Date**: The projected start of the work.
  * **Target Date**: The expected completion date.

Other information, like the SIG leading a project, is collected from [sigs.yml](./sigs.yml).

Project leads may use any other GitHub project features like short descriptions, milestones, etc. to manage individual projects. 

This mechanism allows for a centralized roadmap view while letting individual project teams manage their work and status independently in their own projects.

## Roadmap Item Selection

For a project to appear on the official roadmap, its ID must be added to [sigs.yml](./sigs.yml) in the list of `roadmapProjectIDs` under its corresponding SIG.
This is an opt-in process, coordinated by GC and TC.

Current and potential roadmap items are evaluated by TC and GC, in collaboration with all SIGs, on an ongoing basis, and collectively reviewed at the annual OpenTelemetry Leadership Meeting.
