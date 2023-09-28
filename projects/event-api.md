### Description

The Client / RUM Sig is looking to finalize, complete and resolve the outstanding issues / PR's that exist around the Event API / SDK and the Semantic Conventions that defines what an "event" is.

* Defined, identifying an `event`)
* Created (API / Sdk)
* will be created from Describe the goals, objectives, and requirements for the project. This include the motivations for starting the project now, as opposed to later.

### Project Board

Once approved by TC, a project should be managed using a GitHub project board. This project board should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

A [Technical Committee](https://github.com/open-telemetry/community/blob/main/community-members.md#technical-committee) (TC) member associated with the project can create the board, along with a new project-specific GitHub label to automatically associate issues and PRs with the project. The project lead and all other relevant project members should have edit access to the board.

Once created, please link to the project board here.

Preemptively created a board with the relevant and related issues
https://github.com/orgs/open-telemetry/projects/65

### Deliverables

Resolve the outstanding Event Issues / PR's which will define
* What is an event? What does an event look like (what attributes identify it as an event) so that vendors, backends can perform any necessary routing, translation or storage.
* How are events transported (Logs Only, Logs / Span Event, etc)
* The semantic conventions to follow for defining "known" events
  * Reserved (known) prefix's (either as the domain or name prefix) (possible known prefixes: `otel.`, `k8s.`, `azure.`, `aws.`, `ecs.`, `browser.`, `mobile.`, etc) all other "unknown" domains should/can be considered as "custom" by venders / backends.
  * How / where are these are defined in semantic conventions (.yml)
  * Updating tooling to properly handle the conventions
  * Note: This group is not responsible for definition the semantic conventions of All domain specific events, only "how" those events will be represented / transported as an "event".
* Define when an event should be used vs a `Span` or `LogRecord`

We have been working on the definition already as part of the Client / RUM Sig and prototypes current exist in JavaScript in the web sandbox repo using `event.data` as the transport mechanism for the "Payload" of the event.

* JS prototype of setting data https://github.com/open-telemetry/opentelemetry-sandbox-web-js/blob/auto-instrumentation-poc/pkgs/api-events/src/types/Event.ts#L34 
* Swift setData() API https://github.com/open-telemetry/opentelemetry-swift/blob/main/Sources/OpenTelemetrySdk/Logs/LogRecordBuilderSdk.swift#L66 

### Staffing / Help Wanted

Who is currently planning to work on the project? If a project requires specialized domain expertise, please list it here. If a project is missing a critical mass of people in order to begin work, please clarify.

#### Required staffing

* Need: TC members (At least two sponsoring TC members.)
* Need: Scheduled meeting where TC members and domain experts can attend
* Need: more domain experts willing to define the OTel Event standard
* Need: engineers willing to write prototypes in at least one more language other than JavaScript. Language should be fairly different from JavaScript.
* Need: maintainers or approvers from those languages committed to reviewing the prototypes.

@MSNev Nev Wylie - FTE project lead / browser domain expert
@martinkuba Martin Kuba - Domain expert  and Maintainer / approver for JS
@scheler Santosh Cheler - Domain expert
@dennisme Matthew Dennison - Golang sdk
@patrickhousley Patrick Housley - Event domain expert
@breedx-splk Jason Plumb - Event domain expert

### Meeting Times

__Once a project is started, the working group should meet regularly for discussion. These meeting times should be posted on the OpenTelemetry public calendar.__

TBD

### Timeline

As several items are already underway, here is the optimistic (Ideal) timelines

By End of 2023

* Define the shape of an event (attributes that represent an event)
* General of the semantic conventions (known/reserved domains)
* Location of domain specific semantic conventions
* Accepted definition of Event API / SDK
* Resolved whether Span Events will / can also represent an Event (Not necessarily "how", just a go/no-go call)
* How Application / Custom Events will be supported
* Initial Domain specific events using the Event API/SDK in multiple languages (this is already underway)

By end of June 2024

* Updated tooling for semantic conventions, supporting generation for domain specific events
* Multiple implementations of Event API / SDK
* Mark the Event API/SDK as Stable

Dissolve this specific working group.

### Linked Issues and PRs

See the project board for a collection of Issues related to the project.

### Labels

Additional labels to be able to identify "Event" related Issues / PR's would be ideal to help with tracking.
