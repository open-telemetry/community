# OpenTelemetry Support Maturity Model

## Background and description

OpenTelemetry has become the de facto standard for producing telemetry in cloud native systems, and a growing number of cloud native projects emit their telemetry through it. This proposal is about the maturity of *that* support: how well projects across the ecosystem integrate with OpenTelemetry. It is not about the maturity of OpenTelemetry itself. The aim is to give the ecosystem a shared way to talk about what "supports OpenTelemetry" really means in any given project, and to make the bar for that support easier to see and harder to fudge.

Users expect projects to plug into OpenTelemetry pipelines cleanly, follow semantic conventions, correlate signals, and behave predictably across environments. But support is rarely all-or-nothing. Projects mature unevenly: integration surfaces, semantics, configuration, trace modeling, and multi-signal workflows tend to evolve on different timelines, and today there is no structured way to describe how that mixed picture looks.

Nearly half of respondents in the latest CNCF survey report using OpenTelemetry in production. At that scale, the distance between "supports OpenTelemetry" as a binary label and what it actually delivers in a given project has turned into real friction, especially for platform teams that need to integrate across many projects at once. In practice, that means hitting projects where traces flow via OTLP but metrics are still Prometheus-only, where semantic conventions are several versions out of date, or where the standard `OTEL_*` configuration is quietly ignored in favor of project-specific flags. Each integration becomes its own learning curve, and what works for one project rarely carries cleanly to the next.

The idea was discussed openly in [community issue #3247](https://github.com/open-telemetry/community/issues/3247), where maintainers, end-user representatives, and other contributors signalled interest in turning it into a formal project. The OpenTelemetry Governance Committee then asked that it go through the formal proposal process. The timing is reinforced by OpenTelemetry reaching CNCF Graduated status: now that it has graduated, "supports OpenTelemetry" becomes a claim that users and downstream projects increasingly take at face value. A descriptive maturity model is one way to keep that claim honest.

### Current challenges

- Support is described as present or absent, with no way to say how deep, consistent, or intentional it actually is. Users cannot evaluate what "supports OpenTelemetry" means for a given project.
- Different projects implement OpenTelemetry support at very different depths. Some push traces via OTLP while metrics stay Prometheus-only. Some use outdated semantic conventions. Some ignore standard `OTEL_*` environment variables. Adopters discover these inconsistencies after the fact.
- Maintainers who want to improve their OpenTelemetry support lack a structured way to identify gaps or prioritize work. "Better telemetry" stays an ad-hoc conversation, project by project.
- Platform teams building stacks across multiple CNCF projects cannot easily compare integration effort. Every project gets evaluated from scratch.
- Existing community efforts, such as the [Instrumentation Score](https://github.com/instrumentation-score/) specification for rule-based signal-quality checks and the [OpenTelemetry Ecosystem Explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer) for component discovery and cataloging, address adjacent concerns but operate independently. Nothing connects design intent, evolution patterns, and signal quality into a coherent picture.

### Goals, objectives, and requirements

The goal of this project is to develop and publish a descriptive maturity model for OpenTelemetry support in cloud native projects (and potentially beyond), giving the community a shared framework for evaluating and discussing how that support evolves.

Objectives:

1. Define a multi-dimensional maturity model that captures how OpenTelemetry support typically evolves across the dimensions listed below.
2. Validate the model against real projects by applying it to cloud native projects in different categories (ingress controllers, service meshes, application runtimes, and so on), and check whether the dimensions and levels hold up in practice.
3. Publish the model as an OpenTelemetry community resource (for example on opentelemetry.io), with explicit positioning as a descriptive tool, not a certification, compliance, or ranking program.
4. Develop evaluation guidance, including question-based checklists, so reviewers can apply the model consistently across projects.
5. Position the model as complementary to other ecosystem efforts (Instrumentation Score, Ecosystem Explorer), and describe how those tools relate to each other.

Dimensions in scope:

The draft model evaluates OpenTelemetry support across seven dimensions. The wording, granularity, and number of dimensions are open for community refinement during the project. The current draft covers:

1. **Integration Surface**: how users connect a project to their observability pipelines, and how strongly telemetry is coupled to specific tools or vendors.
2. **Semantic Conventions**: how consistently telemetry meaning aligns with OpenTelemetry semantic conventions, and how domain-specific extensions are introduced and stewarded.
3. **Resource Attributes & Configuration**: how identity, scope, and configuration are handled across environments, including correct use of resource attributes and standard `OTEL_*` configuration.
4. **Trace Modeling & Context Propagation**: how traces are structured and how context flows through synchronous and asynchronous execution paths.
5. **Multi-Signal Observability**: how traces, metrics, and logs are supported together and correlated.
6. **Audience & Signal Quality**: who telemetry is designed for, how noisy it is by default, and how well it communicates meaningful system behavior.
7. **Stability & Change Management**: how telemetry evolves over time and how changes are communicated and managed once users depend on it.

Each dimension is described across four global maturity levels: Level 0 (Instrumented), Level 1 (OpenTelemetry-Aligned), Level 2 (OpenTelemetry-Native), and Level 3 (OpenTelemetry-Optimized). There is no overall maturity score by design; each dimension stands on its own.

What this project explicitly is not:

- A specification, standard, or policy proposal.
- A certification or conformance program.
- A ranking or comparison mechanism for CNCF projects.
- A requirement for cloud native or OpenTelemetry projects.

Why now:

- Adoption has reached a point where the quality and consistency of OpenTelemetry support matters as much as its presence.
- OpenTelemetry just reached CNCF Graduated status, which raises what users and downstream projects assume "supports OpenTelemetry" means. A shared vocabulary is easier to establish now than to retrofit later.
- The draft framework has already been applied to real projects (Kubernetes ingress controllers including Traefik, Istio Gateway, Contour, Emissary, and kgateway). That exercise sharpened the boundary between project maturity and Collector pipeline capability, tightened the Level 3 definition for Semantic Conventions, clarified what is expected at the source versus what can be derived in the pipeline for Resource Attributes, and produced a question-based evaluation appendix.
- Conversations with project maintainers (Dapr, kgateway, and others) show that going through the model can lead to real changes, including upstream dependency work that kicked off as a direct result of an evaluation.
- The OpenTelemetry Governance Committee has indicated that this work should go through the formal project process for broader community input.
- The work fits the wider goal of strengthening OpenTelemetry's role as an integration layer across CNCF, and picks up a thread from the cross-project collaboration track at Maintainer Summit NA.

## Deliverables

1. **Maturity model document**: a published, community-reviewed maturity model describing OpenTelemetry support across the defined dimensions and global maturity levels. This includes:
   - Global maturity level definitions (Level 0: Instrumented, Level 1: OpenTelemetry-Aligned, Level 2: OpenTelemetry-Native, Level 3: OpenTelemetry-Optimized).
   - Per-dimension descriptions with characteristics and example scenarios at each level.
   - Guidance on how to use the model (for maintainers, contributors, users, and platform teams).
   - Explicit positioning relative to other community efforts (Instrumentation Score, Ecosystem Explorer).
   - A clear statement on the boundary between project-emitted telemetry and downstream Collector pipeline capabilities.
2. **Evaluation checklist / reference guide**: a question-based evaluation checklist for each dimension and maturity level, designed for consistent, repeatable assessments. The current draft already includes an appendix that will be refined and validated through further use.
3. **Category assessment**: application of the model to at least one category of cloud native projects (for example ingress controllers, service meshes, or application runtimes) to capture the current state of OpenTelemetry support across that space. This both validates the model and demonstrates its value.
4. **Publication on opentelemetry.io**: the maturity model and supporting materials published as community documentation on the OpenTelemetry website, with clear positioning as a descriptive framework maintained by the community.
5. **Companion blog post(s)**: blog post(s) announcing the project and explaining the model's purpose to the broader community.

Note: this project does not propose changes to the OpenTelemetry Specification or Semantic Conventions. No OTEPs are required. The deliverables are documentation and guidance artifacts.

## Staffing / Help Wanted

### Industry outreach (Optional)

The following people and groups should be aware of this effort. Some have already been engaged; the rest are targets for outreach:

- **Cloud native project maintainers**: initial conversations have taken place with maintainers of Traefik, Linkerd, Dapr, and kgateway. Further outreach is needed for maintainers in other categories (databases, service meshes, CI/CD tools, and so on).
- **CNCF TAG Operational Resilience**: as the TAG responsible for observability guidance across CNCF, their input matters.
- **CNCF TCG Platform Engineering**: the maturity model is structurally inspired by the [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/), which was developed by WG Platform Engineering under TAG App Delivery.
- **CNCF TAG Developer Experience**: can provide input and help validate the current status of projects.
- **OpenTelemetry End User SIG**: end users have the strongest perspective on what "OpenTelemetry support" should mean in practice.
- **Observability vendors and platform teams**: companies building on OpenTelemetry that work across many CNCF projects can offer practical feedback.

### SIG

This project is cross-cutting. It touches documentation, semantic conventions, ecosystem tooling, and end-user concerns. Two viable paths:

- Lead under an existing SIG (for example SIG Communications or SIG End User), with explicit coordination touchpoints to SIG Docs and SIG Semantic Conventions.
- Form a dedicated working group with representation from multiple SIGs.

Recommendation: discuss with TC and GC during proposal review. A working group under SIG Communications, mirroring how the Ecosystem Explorer project is organized, seems like a sensible fit given the documentation- and ecosystem-facing nature of the deliverables.

### Required staffing

#### Project Lead(s)

- **Kasper Borg Nissen** ([@kaspernissen](https://github.com/kaspernissen)), Dash0: author of the draft maturity model. Has been developing and validating the framework through blog posts, talks, and direct engagement with cloud native projects.
- _Seeking one additional co-lead_: ideally from a different company and with complementary expertise (for example semantic conventions, OpenTelemetry SDK development, or an end-user/platform team perspective).

#### Interested contributors

The following people publicly expressed interest in contributing during the discussion on [issue #3247](https://github.com/open-telemetry/community/issues/3247). Specific roles and commitments will be confirmed as part of the proposal review:

- **Michael Hausenblas** ([@mhausenblas](https://github.com/mhausenblas)): end-user perspective; committed to participating as an OpenTelemetry end user.
- **Mauricio Salatino** ([@salaboy](https://github.com/salaboy)): cross-project experience (Dapr, Knative); willing to help develop checklists and evaluations.
- **Mehmet Baykara** ([@mbaykara](https://github.com/mbaykara)): working on an adjacent observability maturity model effort; willing to compare notes, review dimension wording, and contribute enterprise/customer adoption examples.
- **Severin Neumann** ([@svrnm](https://github.com/svrnm)): SIG Communications / Docs perspective; expressed support for hosting on opentelemetry.io and helped frame the ownership question.
- **Henrik Rexed** ([@henrikrexed](https://github.com/henrikrexed)): provided detailed feedback on the developer-facing actionability of the model and on the per-signal scoring trade-off; willing to do a thorough pass on the document.

_Additional contributors actively sought:_

- **Assessment authors**: contributors willing to apply the model to CNCF projects they maintain or use, so the set of reference assessments grows beyond ingress controllers.
- **Documentation contributors**: contributors to help shape the model for publication on opentelemetry.io.
- **Semantic conventions reviewers**: reviewers from SIG Semantic Conventions to align the semantic conventions dimension with the project's direction, including Weaver-based workflows.

### Sponsorship

#### TC Sponsor

_To be confirmed._ Seeking a TC sponsor with interest in ecosystem integration, instrumentation quality, or cross-project OpenTelemetry support.

#### GC Liaison

_To be confirmed._ Seeking a GC liaison to keep the project healthy and the scope true to the proposal.

## Expected Timeline

The project is structured in three phases.

### Phase 1: Community review and model refinement (Month 1–2)

- Submit the project proposal for GC/TC review.
- Solicit community feedback on the draft maturity model through the proposal PR and community meetings.
- Refine dimensions, maturity levels, and evaluation checklists based on feedback.
- Recruit additional contributors, confirm staffing, and agree on SIG ownership.

### Phase 2: Validation and documentation (Month 3–4)

- Apply the refined model to at least one category of CNCF projects.
- Develop the model into publishable documentation for opentelemetry.io.
- Coordinate with SIG Docs on publication format and placement.
- Coordinate with related efforts (Instrumentation Score, Ecosystem Explorer) on complementary positioning.

### Phase 3: Publication and handoff (Month 5–6)

- Publish the maturity model and category assessment on opentelemetry.io.
- Establish ongoing maintenance ownership (SIG or working group).
- Decide whether the project transitions to ongoing SIG work or wraps up.

## Labels (Optional)

- `area/maturity-model`
- `area/ecosystem`

## GitHub Project (Post-Approval)

_To be set up after approval._

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

_To be set up after approval._

## Related work and references

- [Community issue #3247: Draft proposal — OpenTelemetry Support Maturity Model for CNCF projects](https://github.com/open-telemetry/community/issues/3247)
- [Draft maturity model document](https://docs.google.com/document/d/1KvRtYqdSR1ii-SLV2wEv0MH-j9Mh5xA5u7f51kO6xpw/edit?usp=sharing)
- [CNCF Platform Engineering Maturity Model](https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/) (structural inspiration)
- [Instrumentation Score](https://github.com/instrumentation-score/) (complementary: rule-based signal quality checks)
- [OpenTelemetry Ecosystem Explorer](https://github.com/open-telemetry/opentelemetry-ecosystem-explorer) (complementary: component discovery and cataloging)
- [OpenTelemetry Ecosystem Integrations](https://opentelemetry.io/ecosystem/integrations/) (23+ CNCF projects listed)
- [OpenTelemetry Weaver](https://github.com/open-telemetry/weaver) (tooling referenced for semantic extensions at Level 3)
- [Prometheus Conformance Program](https://github.com/cncf/prometheus-conformance) (reference for a possible future, separate conformance effort)
