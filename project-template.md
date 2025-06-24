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

### Industry outreach

Who (people, companies) in the industry should be aware of this effort? Was there an attempt to get them onboard? What did they say?

### Required staffing

Who is planning to work on the project? If a project requires specialized domain expertise, please list it here. If an existing or new SIG is missing a critical mass of people in order to begin work, please clarify in the "other staffing" section below. See [project proposal](project-management.md#project-proposal) for more details.

(For projects driven by existing SIGs)
#### SIG(s)
<SIG NAME>

#### Other Staffing

(For projects that require a new SIG)
#### Project Leads(s)
<NAMES>

#### TC Sponsor
<NAME>

#### Delegated TC Sponsor (Optional)
<NAME>

#### GC Liaison
<NAME>

#### Other staffing
<NAMES>

## Timeline

What is the expected timeline the project will aim to adhere to, and what resources and deliverables will be needed for each portion of the timeline? If the project has not been started, please describe this timeline in relative terms (one month in, two weeks later, etc). If a project has started, please include actual dates.

## Labels

Issues should be properly labeled to indicate what parts of the specification it is focused on. List here the labels applicable to this project, and consider adding them to corresponding GitHub Project automation to include them automatically into the project backlog.

## GitHub Project

Once approved, a project should be managed using a GitHub project (see [open projects](https://github.com/open-telemetry/community/projects?query=is%3Aopen)). This project should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

Any [member](./guides/contributor/membership.md) associated with the project can create the board. Please use the existing [GitHub Project template](https://github.com/orgs/open-telemetry/projects/140) to create your project, replacing `{project_name}` where appropriate.

Once created, the creator of the board should:

- Assign `Admin` privileges on the project to the relevant project members (using a new or existing GitHub team).
- Change the visibility of the project to `Public` in order to share project status and priorities outside of the OpenTelemetry organization.
- Configure project workflows to automatically add issues and PRs to the board based on repositories and labels.

See [project management](project-management.md#project-lifecycle) for more information about sharing project updates and status.

Once created, please add a link to the project board here.

## SIG Meetings and Other Info (New SIGs Only)

Once a project is started, its corresponding SIG should meet regularly for discussion. These meeting times should be posted on the [OpenTelemetry public calendar](https://github.com/open-telemetry/community#calendar) and automatically recorded.

Any relevant information related to the SIG (e.g. sponsors, meeting times, Slack channels, meeting notes, etc.) must be publicly available in the [community](https://github.com/open-telemetry/community) SIG tables, which can be updated via the [sigs.yml](./sigs.yml) file and running `make table-generation`.

See [How to create and configure meetings](./docs/how-to-handle-public-calendar.md) for updating the public calendar or open an issue in the community repository so it's taken care of.
