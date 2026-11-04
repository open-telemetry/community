# FaaS Stability Progression

The FaaS stability progression project is focussed on progressing, the stability of the telemetry emitted by FaaS platforms with a focus on
HTTP and messaging invocations.

## Background and description

The faas conventions were initially added in 0.7.0 (Nov 5 2020) and over the next 6 years there has been very little progression on stabilizing those conventions and until recently a number of these attributes were not following naming conventions.

### Current challenges

Due to the current developmental status of the faas conventions those conventions can not be considered as stable, hence does not inspire trust that they won't change overtime. By working towards stabilizing the conventions instrumentations can be aligned further signaling that the conventions can be trusted.

### Goals, objectives, and requirements

The primary goal of this sub-project is to review the existing state of conventions/instrumentation and use that knowledge to build a strong base for stabilizing the conventions.

To ensure a more structured project, the delivery will be completed in stages

#### Stage 1

- Review of existing conventions, identifying attributes to be renamed
- Defining of entities to describe what is being run and where it is being run
- Promotion of the attributes from development to alpha/beta to signal when they have been reviewed and confirmed
- Update of span definitions for http & messaging server use cases

Out of scope

- Metric changes

#### Stage 2

- Metric review and promotion
- Aligning of collector metric scrappers/receivers with conventions
- Promotion of entities based of metric implementation findings

#### Stage 3

- Stabilize the conventions which have been reviewed and instrumentation have confirmed their viability.

#### Out of scope

The cron & event driven (ie file changes) span invocations are classed as out of scope for this project as this requires a dedicated project which looks at workflows more broadly as in those cases the workflow run is the initiator for the function as opposed to a http or messaging request.

## Deliverables

- Stabilized faas semantic conventions
- Updated collector receivers & instrumentation

## Staffing / Help Wanted

### Industry outreach (Optional)

Who (people, companies) in the industry should be aware of this effort? Was there an attempt to get them onboard? What did they say?

### SIG

lambda-extensions

### Required staffing

See [Project Staffing](/project-management.md#project-staffing)

#### Project Leads(s)

- @thompson-tomo

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

- Stage 1: has commenced with the focus being the review of existing state. Key need is reviewers of semconv
- Stage 2: aim to commence 2 months in to the project. Resource needed is collector component owners to update the collector.
- Stage 3: aim to commence 1.5 months after start of stage 2 and after entity has been promoted.

After the project has started, please use GitHub project updates to set specific target start and completion dates (see [Project Lifecycle](project-management.md#project-lifecycle) for more information).

## Labels (Optional)

- area:faas

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
