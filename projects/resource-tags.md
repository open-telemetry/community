# Resource Tags Working Group

## Background and Description

Cloud providers have long supported customer-defined tags (key-value metadata) as a mechanism to organize resources, manage cost, apply governance controls, and enable automation. These tag, such as environment=prod or costCenter=acme-digital, are widely used across platforms like AWS, Azure, and GCP to group and manage infrastructure, and are leveraged by services including identity and access management, billing systems, policy engines, and security tooling.

Despite their ubiquity, these tags are not standardized across providers and often lack well-defined semantics. Different users may express the same concept in different ways (e.g., env=prod vs. environment=production), and tools consuming these tags must implement custom logic to interpret them. This fragmentation makes it difficult to reason about infrastructure consistently, especially in multi-cloud and hybrid environments where teams rely on observability and automation platforms to derive insights from tags.

This Working Group proposes to define semantic conventions for a set of commonly used resource tags, such as environment, application, owner, and data_sensitivity etc and incorporate them into the OpenTelemetry specification. Standardizing the meaning of these tags will allow telemetry pipelines to treat them as first-class, interoperable metadata. For example, resource detectors in OpenTelemetry can surface these tags from platform metadata, making them accessible to downstream tools in a consistent format. With shared semantics in place, observability and security platforms can enable features like governance-aware dashboards, suggest default security postures, cross-cloud resource attribution etc without relying on cloud- or vendor-specific integrations.

---

### Current Challenges

- **No shared semantics**: Common tags like `environment`, `owner`, or `cost_center` are widely used but lack standardized meaning, leading to inconsistent usage and interpretation.

- **Cross-cloud fragmentation**: Tags are implemented differently across providers, making it hard to reason about resources in a consistent way across clouds and tools.

- **Limited utility in observability**: Tags show up in telemetry, but their ambiguous structure makes them hard to use for dashboards, alerting, or policy logic.

---

### Goals, objectives, and requirements

The goal of this project is to define a shared understanding for a set of commonly used resource tags, such as `environment`, `owner`, `cost_center` etc. These definitions will make it easier for OpenTelemetry and related tools to interpret and act on tag metadata consistently—supporting better automation, governance, and observability across environments. Initial areas of work include:

* [Define the initial set of standardized tags and their recommended structure or values]
* [Ensure alignment with existing OpenTelemetry resource attributes where applicable]
* [Collaborate with the open source community and other cloud providers for cross-domain alignment]

---
## Deliverables
Initial deliverables will include:

* A specification defining common resource tags such as `environment`, `application`, `owner`, `cost_center`, `business_unit`, `data_sensitivity` etc
* Recommended value sets and usage guidance for applicable tags 
* Alignment with existing OpenTelemetry resource attributes where relevant
* Documentation and examples for adoption by cloud providers, observability platforms, and security tools

As adoption grows, we expect to expand this set iteratively based on feedback from users and collaborators across the ecosystem.

---
## Staffing / Help Wanted

We are seeking domain experts to work on the definition, alignment, and adoption of standardized resource tags across cloud platforms and observability systems.

The goal is to follow @tedsuo's proposed [Semantic Convention Process](https://docs.google.com/document/d/1ghvajKaipiNZso3fDtyNxU7x1zx0_Eyd02OGpMGEpLE/edit#heading=h.xc2ft2cddhny), with the following stages:

- **Stage 1: Working Group Preparation** — Define scope, gather contributors, and align on the initial set of tags.
- **Stage 2: Stabilizing the Specification** — Draft and iterate on proposed tag definitions, value guidance
- **Stage 3: Implementation** 

---
### Required staffing

TBD
---


## Timeline

Stage 1 (Working Group Preparation) is currently underway. We are finalizing the initial scope, gathering contributors, and identifying sponsors and maintainers.

Stage 2 (Stabilizing the Specification) will begin once we have adequate staffing and have aligned on a meeting schedule (currently targeting bi-weekly sessions). 

Stage 3 (Implementation) will begin after the initial tag set is reviewed and marked stable. 

---

## GitHub Project

To be created once proposal is approved.

---

## SIG Meetings and Communication

- **Meeting cadence**: Biweekly
- **Time**: TBD
- **Slack**: Proposed new channel `#otel-resource-tags-sig` on CNCF Slack
- **Notes and recordings**: Will be maintained publicly and shared via the OpenTelemetry community calendar

