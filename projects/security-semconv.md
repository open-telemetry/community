# Security Semantic Conventions

## Description

The purpose of this project is to bring in the security domain for the OpenTelemetry community. 

As outlined in the [ECS OTEP](https://github.com/open-telemetry/oteps/blob/main/text/0199-support-elastic-common-schema-in-opentelemetry.md), the Elastic Common Schema (ECS) is currently being contributed to the semantic conventions schema. Given the significance of security within ECS, establishing this SIG is crucial as it will expedite the donation of ECS fields tailored to security use cases. Beyond expanding the schema, our aim is to craft a clear vision for the instrumentation required.

## Deliverables

* Our current focus is on defining essential semantic conventions for security use cases.
  * This includes but is not limited to the following namespaces:
    * [`Code signature`](https://www.elastic.co/guide/en/ecs/current/ecs-code_signature.html)
    * [`DLL`](https://www.elastic.co/guide/en/ecs/current/ecs-dll.html)
    * [`DNS`](https://www.elastic.co/guide/en/ecs/current/ecs-dns.html)
    * [`File`](https://www.elastic.co/guide/en/ecs/current/ecs-file.html)
    * [`Group`](https://www.elastic.co/guide/en/ecs/current/ecs-group.html)
    * [`Hash`](https://www.elastic.co/guide/en/ecs/current/ecs-hash.html)
    * [`Host`](https://www.elastic.co/guide/en/ecs/current/ecs-host.html)
    * [`Network`](https://www.elastic.co/guide/en/ecs/current/ecs-network.html)
    * [`Operating System`](https://www.elastic.co/guide/en/ecs/current/ecs-os.html)
    * [`Package`](https://www.elastic.co/guide/en/ecs/current/ecs-package.html)
    * [`Process`](https://www.elastic.co/guide/en/ecs/current/ecs-process.html)
    * [`Registry`](https://www.elastic.co/guide/en/ecs/current/ecs-registry.html)
    * [`Risk information`](https://www.elastic.co/guide/en/ecs/current/ecs-risk.html)
    * [`Rule`](https://www.elastic.co/guide/en/ecs/current/ecs-rule.html)
    * [`Threat`](https://www.elastic.co/guide/en/ecs/current/ecs-threat.html)
    * [`TLS`](https://www.elastic.co/guide/en/ecs/current/ecs-tls.html)
    * [`User`](https://www.elastic.co/guide/en/ecs/current/ecs-user.html)
    * [`Vulnerability`](https://www.elastic.co/guide/en/ecs/current/ecs-vulnerability.html)
  * Please note that some of the above-mentioned namespaces are already a part of the Semantic Conventions schema. The goal is to expand these namespaces to include additional fields that are relevant to security use cases.

* As new use cases and namespaces are introduced to the semantic conventions, there may be a need for additional instrumentation to accommodate them. It is anticipated that this aspect will expand through an iterative process.

## Staffing / Help Wanted

We are seeking security experts to collaborate with us in expanding the security domain within the community.  

### Required staffing

There is an open [PR](https://github.com/open-telemetry/semantic-conventions/issues/580) to create a `semconv-security-approver` group for all PRs related to security fields.  

* project lead: @trisch-me (Elastic)
* domain expert: @mjwolf (Elastic)
* domain expert: @raesene (Datadog)
* domain expert: @lambdanis (Isovalent)
* domain expert: @mdelfabro (Dynatrace)
* domain expert: @kelnage (Grafana Labs)
* domain expert: @alexvanboxel (Collibra)

* TC sponsor: @reyang
* TC sponsor: @jsuereth

Need more 
- [ ] domain experts
- [ ] potentially, maintainers of language-specific instrumentation may be needed if the need arises.


## Meeting Times

There is an allocated time in the Semantic Conventions SIG for this project.
- Mondays at 8 AM PST

For async conversation please use #otel-semconv-security slack channel from official CNCF slack workspace.

## Security dashboard

[Main dashboard](https://github.com/orgs/open-telemetry/projects/104/views/1) with all the issues and PRs related to the project.

## Timeline

The goal is to have the security semantic conventions implemented by the end of 2024.

The timeline for this project is as follows:
December 2023: Initial Draft
April 2024: Review and Refinement
May 2024-December 2024: Introducing the Security Semantic Conventions


## Labels

* security

## Linked Issues and PRs

* [Donating ECS to OpenTelemetry](https://github.com/open-telemetry/oteps/blob/main/text/0199-support-elastic-common-schema-in-opentelemetry.md)
* [Creation of semconv-security-approver group](https://github.com/open-telemetry/semantic-conventions/issues/580)
