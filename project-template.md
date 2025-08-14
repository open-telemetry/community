# <<PROJECT NAME>>

Name your project here. This should be a short, descriptive name that describes the main goal of the project, or the main deliverable, not the SIG that may be formed as part of it.

For instance, if the project is aimed at the first set of deliverables for the Foo SIG, name the project "Foo SIG Bootstrap" or "Initial Foo Implementation", not "Foo SIG".

## Background and description

Add any background that may be needed to introduce the scope of this project.

### Current challenges
List the current challenges that this project aims to solve. Focus on the problem here, how it affects users and what the downsides are if nothing is done, rather than the solution.

### Goals, objectives, and requirements
Describe the aim of this project, including the goals, objectives and requirements needed to solve the challenges presented in the previous section. Include here the motivations for starting the project now, as opposed to later. Call out the benefits for the OpenTelemetry project when this project is completed.

## Deliverables

A description of what this project is planning to deliver, or is in the process of delivering. This includes all OTEPs and their associated prototypes.

In general, OTEPs are not accepted unless they come with working prototypes available to review in at least two languages. Please discuss these requirements with a TC member before submitting an OTEP.

## Staffing / Help Wanted

### Industry outreach (Optional)

Who (people, companies) in the industry should be aware of this effort? Was there an attempt to get them onboard? What did they say?

### SIG
Name of the SIG that will lead this work.
If this project requires the creation of a new SIG, specify the name here.

### Required staffing
See [Project Staffing](/project-management.md#project-staffing)

#### Project Leads(s)
Name(s) of project lead(s)

#### Other Staffing
Names and expected contribution of any other contributors.
Please also include maintainers or approvers from other SIGs committed to reviewing prototypes.

### Sponsorship
See [Project Sponsorship](/project-management.md#project-sponsorship)

#### TC Sponsor
Name of TC sponsor

#### Delegated TC Sponsor (Optional)
Name of delegated TC sponsor

#### GC Liaison
Name of GC liaison

## Expected Timeline

What is the expected timeline the project will aim to adhere to, and what resources and deliverables will be needed for each portion of the timeline?
Please describe this timeline in relative terms here (one month in, two weeks later, etc).

After the project has started, please use GitHub project updates to set specific target start and completion dates (see [Project Lifecycle](project-management.md#project-lifecycle) for more information).

## Labels (Optional)

Issues should be properly labeled to indicate what parts of the specification it is focused on. List here the labels applicable to this project, and consider adding them to corresponding GitHub Project automation to include them automatically into the project backlog.

## GitHub Project (Post-Approval)

Once approved, a project should be managed using a [GitHub project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). This project should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

Any [member](./guides/contributor/membership.md) associated with the project can create the board.
Please use the existing [GitHub Project template](https://github.com/orgs/open-telemetry/projects/140) to create your project, replacing placeholders as appropriate.

Once created, the creator of the board should:

- Assign `Admin` privileges on the project to the relevant project members (using a new or existing GitHub team).
- Change the visibility of the project to `Public` in order to share project status and priorities outside the OpenTelemetry organization (default in template).
- Configure project workflows to automatically add issues and PRs to the board based on repositories and labels.

See [Project Lifecycle](project-management.md#project-lifecycle) for more information about sharing project updates and status.

Once created, please add a link to the project board here.

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

Once a project is started, its corresponding SIG should meet regularly for discussion. These meeting times should be posted on the [OpenTelemetry public calendar](https://github.com/open-telemetry/community#calendar) and automatically recorded.

Any relevant information related to the SIG (e.g. sponsors, meeting times, Slack channels, meeting notes, etc.) must be publicly available in the [community](https://github.com/open-telemetry/community) SIG tables, which can be updated via the [sigs.yml](./sigs.yml) file and running `make table-generation`.
Please ensure that GitHub project ID is added to `roadmap_project_ids` to include this project in the OpenTelemetry Roadmap (see [Roadmap Management](./roadmap-management.md) for more information).

See [How to create and configure meetings](./docs/how-to-handle-public-calendar.md) for updating the public calendar or open an issue in the community repository so it's taken care of.
