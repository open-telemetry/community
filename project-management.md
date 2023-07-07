# Project Management

Some specification changes are small enough in scope such that they can be resolved with a single PR or an OTEP written by a single person. However, this is rarely the case for large, meaningful changes. Most spec work ends up being organized into projects.

At minimum, projects require the following resources to be successful:

* A group of designers and subject matter experts need to dedicate a significant amount of their work time to the project. These participants are needed to design the spec, write a set of OTEPs, and create multiple prototypes. This group needs to meet with each other (and  with TC members) on a regular basis to develop a successful set of proposals.
* A portion of the TC needs to be aware of and participate in the development of the project, to review the proposals and help guide the participants through the specification process.
* Spec approvers and the broader community need to be aware of progress being made on the project, so they can be prepared to participate when proposals are ready for review.

## Project Document

Every project must have a high level **Project Document**, which describes the project. This document will be used as the initial proposal for the project. Once a project is approved, the document should be frequently edited and kept up to date as the project progresses. 

## Project Proposal

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
