# Security Semantic Conventions Working Group

## Description

The purpose of this working group is to bring in the security domain for the OpenTelemetry community. 

As outlined in the [ECS OTEP](https://github.com/open-telemetry/oteps/blob/main/text/0199-support-elastic-common-schema-in-opentelemetry.md), the Elastic Common Schema (ECS) is currently being contributed to the semantic conventions schema. Given the significance of security within ECS, establishing this working group is crucial as it will expedite the donation of ECS fields tailored to security use cases. Beyond expanding the schema, our aim is to craft a clear vision for the instrumentation required.

## Deliverables

* Our current focus is on defining essential semantic conventions for security use cases. 
* As new use cases and namespaces are introduced to the semantic conventions, there may be a need for additional instrumentation to accommodate them. It is anticipated that this aspect will expand through an iterative process.

## Staffing / Help Wanted

We are seeking security experts to collaborate with us in expanding the security domain within the community.  

### Required staffing

There is an open [PR](https://github.com/open-telemetry/semantic-conventions/issues/580) to create a `semconv-security-approver` group for all PRs related to security fields.  

* project lead: @trisch-me (Elastic)
* domain expert: @mjwolf (Elastic)
* domain expert: @raesene (Datadog)
* domain expert: @lambdanis (Isovalent)

* TC sponsor: @reyang
* TC sponsor: vacant

Need more 
- [ ] domain experts
- [ ] TC 
- [ ] potentially, maintainers of language-specific instrumentation may be needed if the need arises.


## Meeting Times

TBD

Once a project is started, the working group should meet regularly for discussion. These meeting times should be posted on the OpenTelemetry public calendar.

## Timeline

TBD

What is the expected timeline the project will aim to adhere to, and what resources and deliverables will be needed for each portion of the timeline? If the project has not been started, please describe this timeline in relative terms (one month in, two weeks later, etc). If a project has started, please include actual dates.

## Labels

* security

## Linked Issues and PRs

* [Donating ECS to OpenTelemetry](https://github.com/open-telemetry/oteps/blob/main/text/0199-support-elastic-common-schema-in-opentelemetry.md)
* [Creation of semconv-security-approver group](https://github.com/open-telemetry/semantic-conventions/issues/580)


## Project Board

Once approved by TC, a project should be managed using a GitHub project board. This project board should be pre-populated with issues that cover all known deliverables, organized by timeline milestones. Once created, please link to the project board here.