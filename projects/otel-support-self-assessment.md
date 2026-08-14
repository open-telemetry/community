# OpenTelemetry Support Self-Assessment and Maintainer Guidance

## Background and description

OpenTelemetry has become the de facto standard for producing telemetry in cloud native systems, and a growing number of projects across the ecosystem emit their telemetry through it. But "supports OpenTelemetry" has become a binary claim that hides enormous variance in what a project actually delivers, and adopters absorb the cost of that variance when they integrate.

This project aims to help maintainers close that gap themselves. It has two parts: opt-in tooling a maintainer can run against their own project's telemetry to get a factual report of what is emitted and where the gaps are, and maintainer-facing guidance on what good OpenTelemetry support looks like for different classes of projects.

> **Revision note.** An earlier version of this proposal described a descriptive maturity model with 0–3 levels per dimension, applied by this project to other cloud native projects and published as a comparative assessment. Review feedback made clear that OpenTelemetry should not be in the business of evaluating or labeling other projects, which is also consistent with CNCF guidance that projects avoid judging one another. That framing has been removed. The proposal now centers on self-assessment tooling and maintainer guidance, with the original dimensions retained only as internal scaffolding for what the tooling checks and the guides cover. See the discussion on [PR #3435](https://github.com/open-telemetry/community/pull/3435).

Support is rarely all-or-nothing. Projects mature unevenly: integration surfaces, semantics, configuration, trace modeling, and multi-signal workflows tend to evolve on different timelines. In practice, adopters hit projects where traces flow via OTLP but metrics are still Prometheus-only, where semantic conventions are several versions out of date, or where standard `OTEL_*` configuration is quietly ignored in favor of project-specific flags. Each integration becomes its own learning curve, and what works for one project rarely carries cleanly to the next.

Nearly half of respondents in the latest CNCF survey report using OpenTelemetry in production. At that scale, and now that OpenTelemetry has reached CNCF Graduated status, the claim "supports OpenTelemetry" is increasingly taken at face value. Without guidance, projects will keep arriving at their own definitions of what it means, and adopters will keep discovering the differences after the fact.

The idea originated in [community issue #3247](https://github.com/open-telemetry/community/issues/3247) and was refined substantially through review on [PR #3435](https://github.com/open-telemetry/community/pull/3435).

### Current challenges

- There is no shared definition of what "supports OpenTelemetry" means, so projects define it for themselves and adopters cannot tell what a given claim covers.
- Maintainers who want to improve their OpenTelemetry support have no way to check their project's actual telemetry output against current conventions and expectations. Gaps are found by users, not by maintainers.
- Maintainers also lack guidance on what good looks like for their kind of project. The considerations for a library differ substantially from those for a database, a message broker, or a gateway, and generic advice does not carry across those classes.
- Instrumentation quality problems surface late. Semantic convention drift, missing resource attributes, unsupported standard configuration, and inconsistent context propagation are all discoverable from a project's own telemetry, but nothing packages those checks for maintainers today.
- Existing community efforts, such as the [Instrumentation Score](https://github.com/instrumentation-score/) specification for rule-based signal-quality checks and the [OpenTelemetry Ecosystem Explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer) for component discovery and cataloging, address adjacent concerns. Neither gives a maintainer an actionable, project-level answer to "what is missing in my integration, and what should I do next?"

### Goals, objectives, and requirements

The goal of this project is to make it easier for maintainers of projects outside OpenTelemetry to build and improve high-quality OpenTelemetry support, by giving them tooling they run themselves and guidance written for their kind of project.

Objectives:

1. **Opt-in self-assessment tooling.** Build tooling a maintainer runs against their own project's emitted telemetry, producing a factual report: what signals are emitted, which semantic conventions are followed, which standard configuration is honored, and where the gaps are. The output is diagnostic information and next steps, not a score, and it belongs to whoever ran it.
2. **Maintainer-facing guidance by project type.** Publish guides covering what good OpenTelemetry support looks like, the common pitfalls, and how to get there, differentiated by class of project (see Deliverables).
3. **Ground the guidance in real cases.** Work with maintainers who want help, use what those engagements surface to decide what the guides and the tooling need to cover, and feed improvements back upstream.
4. **Position clearly relative to adjacent efforts.** Reuse [Instrumentation Score](https://github.com/instrumentation-score/) rules where they apply rather than duplicating them, coordinate with the [Ecosystem Explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer), and stay aligned with SIG Semantic Conventions tooling, including Weaver-based workflows.

#### What this project explicitly is not

This is worth stating plainly, because an earlier draft of this proposal was read otherwise:

- **OpenTelemetry does not evaluate, score, rank, or label other projects as part of this work.** No assessment of a third-party project is produced or published by this project. The tooling is run by maintainers on their own projects, and the results are theirs to use or share as they see fit.
- It is not a certification, conformance, or badging program. 
- It is not a comparison mechanism, an industry analysis, or an input to one.
- It is not a specification, standard, or policy proposal, and it is not a requirement for any project.
- It does not propose changes to the OpenTelemetry Specification or Semantic Conventions. No OTEPs are required.

#### Assessment dimensions (internal scaffolding)

The earlier draft organized OpenTelemetry support into seven dimensions. Those dimensions are retained as internal structure for deciding what the tooling checks and what the guides must cover. They are not a public grading rubric, and the associated 0–3 maturity levels have been dropped.

1. **Integration surface**: how users connect a project to their observability pipelines, and how strongly telemetry is coupled to specific tools or vendors.
2. **Semantic conventions**: how consistently telemetry meaning aligns with OpenTelemetry semantic conventions, and how domain-specific extensions are introduced and stewarded.
3. **Resource attributes and configuration**: how identity, scope, and configuration are handled across environments, including correct use of resource attributes and standard `OTEL_*` configuration.
4. **Trace modeling and context propagation**: how traces are structured and how context flows through synchronous and asynchronous execution paths.
5. **Multi-signal observability**: how traces, metrics, and logs are supported together and correlated.
6. **Audience and signal quality**: who telemetry is designed for, how noisy it is by default, and how well it communicates meaningful system behavior.
7. **Stability and change management**: how telemetry evolves over time and how changes are communicated and managed once users depend on it.

The wording, granularity, and number of dimensions remain open for refinement as the tooling and guides are built. If a dimension does not earn its place in either deliverable, it should be dropped.

## Deliverables

1. **Self-assessment tooling.** Tooling a maintainer can point at their project's telemetry output and get back a report covering emitted signals, semantic convention alignment, resource attributes, standard configuration support, and context propagation, with concrete next steps and links into the guides. Delivered incrementally, starting with a prototype validated against volunteer projects. Requirements:
   - Deterministic and objective. Where a check cannot be made automatically and objectively, it belongs in a guide, not in the tool's output.
   - No score, grade, or level in the output.
   - Run locally by the maintainer. This project does not host, collect, or publish results.
   - Reuses existing rule sets, notably Instrumentation Score, rather than restating them.

2. **Maintainer guides by project type.** Guidance on what good OpenTelemetry support looks like, with common pitfalls and worked examples:
   - **Libraries**: adding native instrumentation, API-vs-SDK boundaries, and what to expose to the embedding application.
   - **Services and infrastructure components** (databases, message brokers, proxies and gateways, controllers): emitting OTLP, writing and stewarding federated semantic conventions, and exposing standard configuration.

   OpenTelemetry Collector distributions are deliberately out of scope here; that class is covered by the separate Collector certification effort.

3. **Publication on opentelemetry.io.** The guides published as community documentation, coordinated with SIG Docs on format and placement.

4. **Companion blog post(s).** Announcing the guidance and tooling to the broader community, aimed at maintainers of projects that integrate with OpenTelemetry.

## Staffing / Help Wanted

### SIG

No new SIG is proposed. A working group will be formed under **SIG Communications**, mirroring how the [Ecosystem Explorer project](./ecosystem-explorer.md) is organized, with SIG Communications meetings used for project updates and coordination.

Coordination touch points:

- **SIG Semantic Conventions**, on convention alignment, federated conventions, and Weaver-based tooling.
- **SIG Docs / Communications**, on publication of the guides.
- **Instrumentation Score** and **Ecosystem Explorer** maintainers, on complementary positioning and rule reuse.

### Required staffing

#### Project Lead(s)

- **Kasper Borg Nissen** ([@kaspernissen](https://github.com/kaspernissen)), Dash0: author of the original draft; has been developing and validating the underlying framework through blog posts, talks, and direct engagement with cloud native projects.
- **Graziano Casto** ([@graz-dev](https://github.com/graz-dev)), Akamas: proposed the opt-in self-assessment framing that this revision is built around, and has volunteered to co-drive the work. Also Tech Lead in CNCF TAG Developer Experience, which is a useful channel for validating the guides with maintainers.

_Pending confirmation:_ **Michael Hausenblas** ([@mhausenblas](https://github.com/mhausenblas)) volunteered to co-lead the earlier version of this proposal. Given the change in scope, he is being asked whether he wants to continue in that role.

#### Interested contributors

The following people expressed interest during the discussion on [issue #3247](https://github.com/open-telemetry/community/issues/3247) and [PR #3435](https://github.com/open-telemetry/community/pull/3435). Specific roles will be confirmed as the working group forms:

- **Mauricio Salatino** ([@salaboy](https://github.com/salaboy)): cross-project experience (Dapr, Knative); has already started work on evaluation automation, which maps directly onto the self-assessment tooling deliverable.
- **Severin Neumann** ([@svrnm](https://github.com/svrnm)): SIG Communications / Docs perspective; supports hosting the guidance on opentelemetry.io and framed the ownership question.
- **Henrik Rexed** ([@henrikrexed](https://github.com/henrikrexed)): provided detailed feedback on developer-facing actionability; willing to do a thorough review pass.
- **Mehmet Baykara** ([@mbaykara](https://github.com/mbaykara)): working on an adjacent observability maturity effort; willing to compare notes and contribute adoption examples.

_Additional contributors actively sought:_

- **Tooling contributors** to build and validate the self-assessment prototype.
- **Guide authors**, particularly maintainers who have added native instrumentation to a library or a data service and can write up what they learned.
- **Volunteer projects** willing to run the prototype against their own telemetry and give feedback on whether the report is actionable.

### Sponsorship

#### TC Sponsor

_To be confirmed._ Per review feedback, this project would benefit from a TC sponsor at the guiding or leading level, since the work touches semantic conventions, docs, and ecosystem tooling across several SIGs.

#### GC Liaison

_To be confirmed._

### Industry outreach (Optional)

- **Cloud native project maintainers**: conversations have taken place with maintainers of Traefik, Linkerd, Dapr, and kgateway, several of which led to upstream changes. These engagements are the source material for the first guides. Further outreach is needed across other classes of projects.
- **OpenTelemetry End User SIG**: end users have the strongest perspective on what "OpenTelemetry support" should mean in practice.
- **CNCF TAG Operational Resilience** and **CNCF TAG Developer Experience**: relevant for observability guidance and for validating the guides against maintainer needs.

## Expected Timeline

### Phase 1: Scope confirmation and staffing (Month 1–2)

- Establish the working group under SIG Communications and use its meetings for coordination.
- Confirm leads, contributors, TC sponsor, and GC liaison.
- Agree the checklist content per project class: what the tooling can verify objectively, and what belongs in a guide.

### Phase 2: Prototype and first guide (Month 3–4)

- Build a self-assessment prototype covering the objectively verifiable checks.
- Validate it against volunteer projects, with maintainer consent, and iterate on whether the report is actionable.
- Draft the first maintainer guide.

### Phase 3: Publication (Month 5–6)

- Publish the guides on opentelemetry.io.
- Release the self-assessment tooling for maintainers to run.
- Companion blog post.
- Decide whether the work continues as ongoing SIG Communications work or wraps up.

## Labels (Optional)

- `area/ecosystem`

## GitHub Project (Post-Approval)

_To be set up after approval._

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

_To be set up after approval._

## Related work and references

- [Community issue #3247: Draft proposal — OpenTelemetry Support Maturity Model for CNCF projects](https://github.com/open-telemetry/community/issues/3247)
- [PR #3435 discussion](https://github.com/open-telemetry/community/pull/3435) (where the scope of this proposal was reframed)
- [Instrumentation Score](https://github.com/instrumentation-score/) (complementary: rule-based signal quality checks)
- [OpenTelemetry Ecosystem Explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer) (complementary: component discovery and cataloging)
- [OpenTelemetry Ecosystem Integrations](https://opentelemetry.io/ecosystem/integrations/)
- [OpenTelemetry Weaver](https://github.com/open-telemetry/weaver) (tooling for semantic convention workflows)
- [OpenTelemetry Collector Distribution definition](https://github.com/open-telemetry/opentelemetry-collector/tree/main/docs#opentelemetry-collector-distribution)
