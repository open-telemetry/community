### Description

The Client / RUM Sig is looking to finalize, complete and resolve the outstanding issues / PR's that exist around the Event API / SDK and the Semantic Conventions that defines what an "event" is.

### Project Board

Project Board: https://github.com/orgs/open-telemetry/projects/65

### Deliverables

Resolve the outstanding Event Issues / PR's which will define

* Refine / stabilize event data model describing what an event is, the semantic meaning of event fields, and how they are sent over the network.
* Pave the way for defining event semantic conventions, allowing their schemas to be described in YAML and incorporated into build-tools.
* Define select event semantic conventions, establishing patterns for future event semantic conventions to follow.
* Refine / stabilize event API and any associated features in the SDK.

#### Required staffing

* Need: more domain experts willing to define the OTel Event standard
* Need: engineers willing to write prototypes in at least one more language other than JavaScript. Language should be fairly different from JavaScript.
* Need: maintainers or approvers from those languages committed to reviewing the prototypes.

Project lead(s):

* @MSNev (JavaScript)

Sponsors:

* @trask
* @tedsuo

Contributing Engineers:

* @martinkuba (JavaScript)
* @scheler
* @patrickhousley
* @breedx-splk

Implementation Engineers:
* @dennisme (Golang)

Implementation Maintainers / Approvers:

* @MSNev
* @martinkuba
* @scheler

### Meeting Times

SIG meeting times: Friday 10am - 11am PT

### Timeline

Completed:
* [Provider based EventLogger API](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/logs/event-api.md)

Q2 2024

* Define EventLogger SDK
* Deliver API & SDK prototype for Web JS
* Define how the contents of the log body field are described as semantic conventions

Q3 2024
* Define the relationship between OTel Events and CloudEvents
* Project completed, Event SIG disbanded

### Linked Issues and PRs

See the project board for a collection of Issues related to the project.

### Labels

The `spec:events` label is used to describe all spec Issues and PRs related to events.
