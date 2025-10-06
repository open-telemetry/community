# Service and Deployment Semantic Conventions

## Background and Description

Cloud providers have long supported customer-defined tags (key-value metadata) as a mechanism to organize resources, manage cost, apply governance controls, and enable automation. These tag, such as environment=prod or costCenter=acme-digital, are widely used across platforms like AWS, Azure, and GCP to group and manage infrastructure, and are leveraged by services including identity and access management, billing systems, policy engines, and security tooling.

Despite their ubiquity, these tags are not standardized across providers and often lack well-defined semantics. Different users may express the same concept in different ways (e.g., env=prod vs. environment=production), and tools consuming these tags must implement custom logic to interpret them. This fragmentation makes it difficult to reason about infrastructure consistently, especially in multi-cloud and hybrid environments where teams rely on observability and automation platforms to derive insights from tags.

Note: These metadata fields are commonly referred to as tags by cloud providers like AWS, Azure, and GCP. However, to remain consistent with OpenTelemetry conventions, we will refer to them as attributes throughout this proposal.

This SIG proposes to define semantic conventions for a scoped set of commonly used resource attributes across three phases:

- Phase 1: Extend the Service entity with new attributes (service.owner, service.criticality).
- Phase 2: Stabilize deployment.environment.name attribute and finish model for deployment related entities.
- Phase 3: Formulate a plan for tagging resources with sensitivity labels, and interaction with other telemetry.

Standardizing the meaning of these attributes will allow telemetry pipelines to treat them as first-class, interoperable metadata. For example, resource detectors in OpenTelemetry can surface these resource attributes from platform metadata, making them accessible to downstream tools in a consistent format. With shared semantics in place, observability and security platforms can enable features like governance-aware dashboards, default security posture suggestions, and cross-cloud resource attribution without relying on cloud- or vendor-specific integrations.

### Current Challenges

- **No shared semantics**: Common resource attributes like `owner`, or `criticality` are widely used but lack standardized meaning, leading to inconsistent usage and interpretation.

- **Cross-cloud fragmentation**: Implemented differently across providers, making it hard to reason about resources in a consistent way across clouds and tools.

- **Limited utility in observability**: Attributes show up in telemetry, but their ambiguous structure makes them hard to use for dashboards, alerting, or policy logic.

### Goals, objectives, and requirements

The goal of this project is to define a shared understanding for a set of commonly used resource attributes. Initial areas of work include:

- Define the scoped set of resource attributes and their recommended values
- Ensure alignment with existing OpenTelemetry resource attributes where applicable
- Collaborate with the open source community and other cloud providers for cross-domain alignment

## Initial Attribute Scope and Proposals

This section outlines the initial set of resource-level attributes, their expected types, example values, and rationale. Where applicable, we build on existing OTel attributes; in other cases, we propose new attributes/namespaces.

## Initial Attribute Scope

| Entity     | Attribute    | Allowed Values                                                            | OpenTelemetry Attribute       | Status                  |
|------------|-----------------------------|------------------------------------------------------------|-------------------------------|-------------------------|
| Service    | owner                       | Dynamic values (e.g., "team@example.com", "team-id")       | `service.owner`               | Proposed                |
| Service    | criticality                 | "mission_critical", "high", "medium", "low"                | `service.criticality`         | Proposed                |
| Service    | deployment.environment.name | "production", "staging", "development", "testing"          | `deployment.environment.name` | Existing (to stabilize) |
| Data       | sensitivity                 | "high", "medium", "low"                                    | `data.sensitivity`            | Proposed (new entity)   |

## Deliverables

Initial deliverables will include:

- A specification defining semantic conventions for the scoped set of resource attributes including a classification of these attributes by domain (e.g., Operations, Security, Finance).
- Recommended value sets and usage guidance for applicable resource attributes
- Alignment with existing OpenTelemetry resource attributes where relevant
- Build prototype ResourceDetectors that retrieve standardized attributes from platform metadata services and surface these attributes as part of OpenTelemetry resource data.
- A classification and normalization rubric that:
  - Helps in mapping common tag variants used across providers and organizations to canonical OpenTelemetry attributes
  - Provides normalization guidance to support consistent implementation (e.g., enum values, casing, value translation)
- Documentation and examples for adoption by cloud providers, observability platforms, and security tools

## Staffing / Help Wanted

We are seeking domain experts to work on the definition, alignment, and adoption of standardized resource attributes across cloud platforms and observability systems.

The goal is to follow @tedsuo's proposed [Semantic Convention Process](https://docs.google.com/document/d/1ghvajKaipiNZso3fDtyNxU7x1zx0_Eyd02OGpMGEpLE/edit#heading=h.xc2ft2cddhny), with the following stages:

- **Stage 1: Working Group Preparation** — Define scope, gather contributors, and align on the initial set of attributes.
- **Stage 2: Prototyping and Finalizing Semantic Conventions Proposal** — Build prototypes using the proposed attributes and refine the semantic conventions for final review and submission.
- **Stage 3: Implementation**

### Required staffing

**Project Leads:**

- @janhvi31 (Google)

**Domain Experts:**

- @ralf0131 (Alibaba)
- @horovits (Amazon)
- @ymotongpoo (Amazon)
- @reyang (Microsoft)

**Sponsors:**

- @trask (Microsoft) — GC Sponsor
- @jsuereth (Google) — TC Sponsor (escalating sponsorship level)

**Semantic Convention Maintainers:**

- @trask (Microsoft)
- @jsuereth (Google)
- @joaopgrassi (Dynatrace)

## Timeline

Stage 1 (Working Group Preparation) is currently underway. We are aligning on the initial scoped set of attributes, gathering contributors, and identifying sponsors and maintainers.

Stage 2 (Stabilizing the Specification) will begin once we have adequate staffing and have aligned on a meeting schedule (currently targeting bi-weekly sessions).

Stage 3 (Implementation) will begin after the initial tag set is reviewed and marked stable.

## GitHub Project

[Project Board](https://github.com/orgs/open-telemetry/projects/168)

## SIG Meetings and Communication

- **Meeting cadence**: Biweekly
- **Time**: This meeting will alternate between two slots to accommodate global time zones:
  - **Slot A (PT-Friendly):** Thursdays at 8:00 AM PT
  - **Slot B (Asia-Friendly):** Thursdays at 5:30 PM IST
- **Slack**: [#otel-service-and-deployment-semconv-sig](https://cloud-native.slack.com/archives/C09HLNSSJSE)
- **Notes and recordings**: Will be maintained publicly and shared via the OpenTelemetry community calendar
