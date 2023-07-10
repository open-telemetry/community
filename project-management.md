# Project Management

The OpenTelemetry has limited bandwith for managing changes which expand the scope of OpenTelemetry, or impact many SIGs within OpenTelemetry. There are three common scenarios which have this kind of impact.
* Non-trivial changes to the OpenTelemetry specification.
* A new SIG being formed.
* An existing SIG taking on new work which will affect the OpenTelemetry as a whole, and will need review from the broader community.

Any changes which fall into one of the above categories must first create a project proposal and gain approval from the GC and TC before work begins.

## Project Proposal

At minimum, projects require the following resources to be successful:

* A clearly defined set of goals and deliverables.
* Deadlines for when the deliverables will be ready for review by the broader community.
* A group of designers and subject matter experts need to dedicate a significant amount of their work time to the project. These participants are needed to design the spec, write a set of OTEPs, and create multiple prototypes. This group needs to meet with each other (and  with TC members) on a regular basis to develop a successful set of proposals.
* Two TC members, or community members delegated by the TC, to sponsor the project.

To propose a project, please create a **project document** using the [project template](project-template.md) as a guide. This document will be used as the initial proposal for the project.

You can then submit the proposal by placing the project document in the [projects](projects/) folder and making a pull request against the community repo. A project is officially approved by merging the pull request.

As the project progresses, the project document should be kept up to date, and the community [README](README.md) should be updated to include any new project meeting information.

## Project Lifecycle

All projects progess through a lifecycle. Projects are tracked on the [Project Board](https://github.com/orgs/open-telemetry/projects/29), which the community can use to get a high-level view of the OpenTelemetry roadmap.

The project lifecycle is as follows:

* A **Project Proposal** pull request is created, as described above.
* If a project is approved, the pull request is merged. The project is then added to the list of **Potential Projects**. This list is roughly ordered based on priority.
* Potential projects are moved to the list of **Scheduled Projects** once they have a planned start date. Having a planned start date lets potential contributors know when they need to make themselves available, and get prepared to begin their work. Subject matter experts and participants who plan to do a lot of work – such as building prototypes – benefit greatly from having a start date, as they can plan for their participantion with their employers and coworkers.
* Once a project is begun, it is moved to the list of **Current Projects**. Projects are only started when the necessary resources are available to move them quickly to completion. This means that the necessary subject matter experts have been identified, and at least two TC members are committed to review and guide the project through the specification process.
* Once work is complete, and the working group is no longer meeting, the project document is moved to the [completed projects](projects/completed-projects/) folder.
