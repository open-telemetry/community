# OTel Blueprints

## Background and description

This project aims to deliver a set of architecture blueprints, with the goal of facilitating and guiding adoption of best practices when deploying OpenTelemetry on a defined set of common environments.
We'd like these blueprints to be backed by evidence in the form of reference architectures shared by end users.

The end-goal is to provide holistic, incremental, high-level guidance that any adopter can apply across their environments, resulting in mature architectures ready for production use, at scale.

### Current challenges

These are some of the high-level adoption challenges that this project aims to help with, some of which are unique to OpenTelemetry as a cross-cutting concern.

#### Adopting OpenTelemetry is a cross-functional effort, likely involving many roles

Adopting OpenTelemetry implies changes in multiple parts of an organization.
The components required for a complete implementation are naturally distributed across different areas of responsibility.

For instance, application teams or library maintainers interact with the OpenTelemetry API to add domain-specific instrumentation.
Platform teams often aim to provide consistent SDK configuration, while supporting centralized telemetry pipelines.
While infrastructure teams may be responsible for ensuring telemetry from hosts and other devices is collected in a standard fashion.

When these efforts are not coordinated, the resulting telemetry can become fragmented, and adoption suffers, failing to deliver the end-to-end observability part of OTel's core promise.

#### There is no "one-size-fits-all" architecture

While OTel adoption may trigger new conversations about platform engineering strategy (i.e. [Reverse Conway Maneuver](https://www.agileanalytics.cloud/blog/team-topologies-the-reverse-conway-manoeuvre)), the project's goal is to cater to all organizational structures, not to force a specific one.

The resulting architectures will (and should) look different depending on the organization's model. For instance:

- A company with federated, autonomous teams might favour a pattern of team-level Collectors routing to a central gateway.
- An organization with a strong central platform team might provide a "paved road" via a fully managed Collector layer and base SDK configurations.

Both are valid approaches. The challenge is that our guidance must be flexible enough to present these different patterns, acknowledging that a "one-size-fits-all" deployment model will not work.

#### Documentation is typically focused on specific solutions, not challenges

The existing OpenTelemetry user documentation is rightly focused on providing and describing solutions.
It's great at explaining what a specific component is, how to configure an SDK, or how to deploy a Collector at scale.
This is essential for a technical project.

The gap, however, is in connecting these solutions to a path forward for common adoption challenges.
Adopters often start with a problem, such as "How do I provide stable SDK config across multiple languages?" or "How do I build a scalable, multi-tenant gateway?".

Blueprints must bridge this gap, starting from the problem and mapping it to a set of principles and actionable patterns.

#### Feedback is often component-specific, not strategic
Currently, feedback in OpenTelemetry is mainly gathered via surveys and interviews conducted by the End-User SIG.
These are normally focused on specific components, or helping specific SIGs prioritize work.

This creates a risk that development efforts in different parts of OTel are not always informed by the most pressing optimizations from the perspective of adoption.
We may be optimizing components in a silo, while a user's main pain point is connecting them.
These blueprints, by capturing common patterns, can serve as that feedback mechanism to help guide the project's priorities.

### Goals, objectives, and requirements
#### Goals

The high-level goals of this project are to:

- Enable scalable adoption of OpenTelemetry by providing clear, challenge-oriented guidance.
- Create a formal feedback loop from end-users to the project, capturing common patterns and challenges to help guide future development.

#### Objectives

To achieve these goals, this project will:

- Define a standard, repeatable process for capturing and publishing end-user reference architectures.
- Define a standard, strategic template for authoring blueprints that map common challenges to OTel-based solutions.
- Publish an initial set of 5 (TBD) reference architectures from end users that have successfully adopted OpenTelemetry at scale.
- Identify most common 3 (TBD) environments and challenges as the base for an initial set of blueprints.
- Publish this initial set of 3 (TBD) blueprints, collating best practices as seen in the field.
- Establish a clear, discoverable location for this content on the OpenTelemetry website, managed by the End-User SIG.

#### Why now?

OpenTelemetry has successfully moved passed the "early adopter" stage.
New waves of adopters are typically composed of platform teams in large organizations.
They require common, vendor-neutral guidance to piece together a large-scale strategy from low-level component documentation.
They need a "paved road" and a set of proven best practices.
Providing this guidance is one of the biggest levers we can pull to accelerate widespread, successful adoption.

## Deliverables

This project will output two types of deliverables:

- **Reference architectures**: Similar to [CNCF reference architectures](https://architecture.cncf.io/architectures), scoped to OpenTelemetry (potentially cross-shared between these).
These will share how different companies or institutions, under different organizational structures and technology stacks, are approaching OpenTelemetry adoption, and the outcomes it has delivered.
- **Blueprints**: Focused on a given environment, these will give specific guidance to solve common challenges.
The format of these blueprints will be discussed as part of this project, however the general proposal is to follow popular forms of [strategic documentation](https://itsadeliverything.com/good-strategy-bad-strategy-the-difference-and-why-it-matters-by-richard-rumelt).
For each of them, we'll identify:
  1. The main challenges the blueprint will solve, and the scope it applies to.
  2. The guiding principles and best practices that solve these challenges.
  3. Individual actions to implement these best practices, linking to more specific guidance in order to avoid duplication of existing parts of the OpenTelemetry documentation (e.g. getting started, SDK config, Collector deployment patterns, etc).

For both of these, this project aims to define templates and processes in order to make it easier to contribute both new reference architectures or blueprints.

After this project is complete, the End User SIG will expand the library of reference architectures and blueprints as part of their BAU operation.

## Staffing / Help Wanted

### Industry outreach (Optional)

**TO-DO** (this PR is raised in draft state to help socialize with end users and industry before continuing)

### SIG
End-User SIG

### Required staffing
See [Project Staffing](/project-management.md#project-staffing)

#### Project Leads(s)
Dan Gomez Blanco (@danielgblanco)

#### Other Staffing

- Members of End-User SIG willing to help coordinate with end-users, create templates, analyze reference architectures, and write up blueprints:
  - TBD
- End-Users willing to contribute reference architectures:
  - TBD
- Maintainers/approvers from Comms SIG to help reviewing and copy editing
  - TBD
- Others

### Sponsorship
See [Project Sponsorship](/project-management.md#project-sponsorship)

#### TC Sponsor
TBD

#### Delegated TC Sponsor (Optional)
TBD

#### GC Liaison
Dan Gomez Blanco

## Expected Timeline

First month: Decide on initial format for reference architectures and blueprint documents.
6-9 moths: Gather and document reference architectures from end users, identify most common challenges, and collate blueprints.

## Labels (Optional)

`otel-blueprints`

## GitHub Project (Post-Approval)

**TO-DO**

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

* Slack channel: [#otel-sig-end-user](https://cloud-native.slack.com/archives/C01RT3MSWGZ)
* Meeting notes:  [End-User SIG Meeting Notes](https://docs.google.com/document/d/1e-UNZA3Tuno9b53RQbe--whUcO0VIXF3P81oXsrBK6g)
* Meeting times: Every other Thursday at 10:00 PT

**TO-DO**: Roadmap item will be added after new GH project is created.
