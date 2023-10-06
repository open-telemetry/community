### Description

The Client / RUM Sig is looking to finalize, complete and resolve the outstanding issues / PR's that exist around the Event API / SDK and the Semantic Conventions that defines what an "event" is.

* Defined, identifying an `event`
* Created (API / SDK)

### Project Board

Once approved by TC, a project should be managed using a GitHub project board. This project board should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

A [Technical Committee](https://github.com/open-telemetry/community/blob/main/community-members.md#technical-committee) (TC) member associated with the project can create the board, along with a new project-specific GitHub label to automatically associate issues and PRs with the project. The project lead and all other relevant project members should have edit access to the board.

Project Board: https://github.com/orgs/open-telemetry/projects/65

### Deliverables

Resolve the outstanding Event Issues / PR's which will define

* Refine / stabilize event data model describing what an event is, the semantic meaning of event fields, and how they are sent over the network.
* Pave the way for defining event semantic conventions, allowing their schemas to be described in YAML and incorporated into build-tools.
* Define select event semantic conventions, establishing patterns for future event semantic conventions to follow.
* Refine / stabilize event API and any associated features in the SDK.

#### Required staffing

* Need: TC members (At least two sponsoring TC members.)
* Need: Scheduled meeting where TC members and domain experts can attend
* Need: more domain experts willing to define the OTel Event standard
* Need: engineers willing to write prototypes in at least one more language other than JavaScript. Language should be fairly different from JavaScript.
* Need: maintainers or approvers from those languages committed to reviewing the prototypes.

Project lead(s):

* @MSNev (JavaScript)

Sponsoring TC Members:

* @tigrannajaryan
* @jack-berg

Contributing Engnieers:

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

__Once a project is started, the working group should meet regularly for discussion. These meeting times should be posted on the OpenTelemetry public calendar.__

TBD

### Timeline

By end of 2023

* Refine data model (By end of 2023)
* Accommodate events in semantic conventions
* Refine / stabilize API & SDKs

### Linked Issues and PRs

See the project board for a collection of Issues related to the project.

### Labels

Additional labels to be able to identify "Event" related Issues / PR's would be ideal to help with tracking.
