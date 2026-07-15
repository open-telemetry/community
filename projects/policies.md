# Initial Policies Implementation

## Background and description

With the recent merge of the
[Policies OTEP](https://github.com/open-telemetry/opentelemetry-specification/pull/4738),
there is significant interest in implementing Policies across the OpenTelemetry
ecosystem. Policies introduce an intent-based specification for configuring how
telemetry components process data. A Policy is an atomic, self-contained rule
that declares a single intent — "match specific telemetry and apply an action" —
and can be evaluated identically regardless of where it runs.

Policies are self-contained, independent, and can be evaluated in parallel and
scaled to thousands of rules without degradation. The same policy behaves the
same way whether it executes inside an SDK, a Collector, or any other
specification-compliant component, and policies are designed to be defined
centrally and distributed to running systems.

This project coordinates the initial work needed to move Policies from an
accepted OTEP into stable, usable policies people can rely on across
OpenTelemetry. Concretely, that means defining the data model and enforcement
specifications, defining the canonical Protobuf schemas, and shipping an **alpha
OpenTelemetry Collector component** that natively interprets and enforces
Policies. There are existing policy implementations already found in
[java-contrib](https://github.com/open-telemetry/opentelemetry-java-contrib) and
Tero's Policy work ([1](https://github.com/usetero/policy),
[2](https://github.com/usetero/policy-go),
[3](https://github.com/usetero/policy-zig)) that this project can build on as a
second implementation. "Done" for this project is a small set of stable policies
you can interact with; the components and features we need fall out from making
those policies successful.

### Current challenges

Configuring telemetry processing today is fragmented and component-specific.
Operators who want to filter, sample, redact, or transform telemetry must learn
a different configuration surface for each component — OTTL and processors in
the Collector, sampler configuration in each SDK, and vendor-specific mechanisms
elsewhere. A rule that drops debug logs or redacts PII has to be re-expressed,
re-tested, and re-maintained for every place it needs to run.

Existing configuration problems:

- **No portability.** A processing rule written for the Collector cannot be
  moved closer to the source (into an SDK) without a rewrite, even though moving
  it upstream is often the cheaper and safer place to enforce it.
- **No central management.** OpAMP exists to provide the capabilities for remote
  management, however, without a consistent configuration method, there is no
  way to centrally manage your telemetry infrastructure.
- **Ordering and coupling.** Existing pipeline configuration is order-dependent
  and stateful, which makes rules hard to reason about in isolation and hard to
  scale as their number grows.
- **Safety.** A malformed processing rule can break a pipeline and cause
  telemetry loss.

If nothing is done, users continue to hand-maintain overlapping, non-portable
configuration in every component, and the ecosystem lacks a common, governable
way to express telemetry-processing intent.

### Goals, objectives, and requirements

The aim of this project is to deliver an initial, working implementation of
Policies along with the specification and schemas that support it, proving the
intent-based model end to end in at least one component (the Collector) as a
foundation the rest of the ecosystem can build on.

**Goals:**

- Deliver a small scoped set of stable policies — **sampling, filtering, and
  transformation** — that work consistently across OpenTelemetry. Additional
  policy types can be added iteratively once these are successful.
- Split and stabilize the specification into two documents: a **data model**
  specification (the policy schema, matchers, and actions) and an
  **enforcement** specification (how a component evaluates policies, including
  the two-stage match then keep & transform model and the core guarantees).
  Enforcment should also describe and require a set of conformance tests to
  ensure that implementations are consistent.
- Define the canonical Protobuf schema for Policies, with a human-authorable
  YAML representation and bidirectional conversion (including shorthand forms).
- Ship an alpha OpenTelemetry Collector component that **natively interprets and
  enforces** policies (rather than translating them into existing Collector
  configuration), honoring the core guarantees: atomicity, fail-open behavior,
  idempotence, and data-model-based field references for portability.
- Use the host component's existing self-observability (e.g. Collector processor
  self-obs metrics) to expose policy match tracking (hits/misses) so operators
  can observe policy effectiveness, and scope out how a component reports
  _which_ policies are applied (e.g. an OpAMP status tagged by policy
  version/UUID, or self-observability signals for SDKs).

**Requirements the model must preserve:**

- **Fail-open:** an invalid policy becomes inert rather than breaking valid
  policies or dropping telemetry.
- **Atomic and self-contained:** one matcher set, one action set, no references
  to other policies, no ordering dependency.
- **Portable:** field references use the OpenTelemetry data model so a policy
  runs identically across conformant runtimes.

**Why now:** the OTEP has just merged and there is broad interest across SIGs.
Coordinating the specification, schema, and an alpha Collector component now
delivers immediately on the goals of the OTEP. Delivering this gives
OpenTelemetry a common, governable way to express telemetry-processing intent
that can be enforced anywhere in the pipeline.

## Deliverables

- **Data model specification.** The policy schema itself: the matcher system
  (field selectors, match types, options, `AttributePath` nested traversal),
  actions, keep/sampling semantics for logs, metrics, and traces, and precedence
  (most-restrictive-wins).
- **Enforcement specification.** How a component evaluates policies: the
  two-stage execution model (match; then keep & transform), the core guarantees
  (atomicity, fail-open, idempotence, portability), and the error-handling
  taxonomy (parse, compilation, runtime).
- **Canonical Protobuf schema** for Policies, plus the YAML authoring format and
  documented bidirectional conversion including shorthand forms.
- **Alpha Collector component** that natively interprets and enforces policies
  across logs, metrics, and traces (not a translation into existing Collector
  configuration), including fail-open handling and match tracking.
- **Experimental policies** for the initial scope: **sampling, filtering, and
  attribute sanitization**. These are the crisp deliverables that let us prove
  the model quickly; transformation and other policy types are deferred and
  added iteratively.
- **Applied-policy reporting.** Scope and formalize how a component reports
  which policies are actually in effect — for example an OpAMP status tagged by
  policy version/UUID, or self-observability signals for SDKs — so operators can
  see what is applied to a given instance.
- **Integration direction** documenting how Policies relate to distribution
  mechanisms (e.g. OpAMP, the OpenTelemetry Operator) and to policy composition
  ("merger") — with dynamic distribution intentionally kept separate from core
  policy semantics so both can iterate independently.

Following OpenTelemetry specification practice, the alpha component(s) — the
Collector component here, plus the existing java-contrib implementation as a
second — come before the specification is formalized. These requirements should
be discussed with a TC member before submitting any follow-on OTEP.

## Staffing / Help Wanted

### Industry outreach (Optional)

The Policies concept originated in discussions at KubeCon NA 2025 on
policy-based control of telemetry. Interested parties across the SDK, Collector,
Operator, and OpAMP SIGs, as well as vendors building telemetry-processing
products, should be aware of this effort and are invited to participate.

### SIG

A new Policies SIG will lead this work. Initial coordination and the alpha
Collector component will happen in collaboration with the Collector SIG.

### Required staffing

See [Project Staffing](/project-management.md#project-staffing)

#### Project Leads(s)

- **@jaronoff97** (Tero) – Maintainer; Operator, Helm, Injector
- **@jsuereth** (Google) – Maintainer; Specification, Collector
- **@dashpole** (Google) – Maintainer; Specification, Collector, Prometheus
- **@menderico** (Google) – Maintainer; Collector
- **@jackshirazi** (Elastic) – Maintainer; Java SDK/agent, author of the
  existing policy implementation in
  [java-contrib](https://github.com/open-telemetry/opentelemetry-java-contrib)

#### Other Staffing

Contributors from the Collector, SDK, Configuration, OpAMP, and Operator SIGs
are being recruited. Maintainers/approvers from those SIGs committed to
reviewing the specification and alpha components will be listed here as they
commit.

### Sponsorship

See [Project Sponsorship](/project-management.md#project-sponsorship)

#### TC Sponsor

- @dashpole (Google)

#### Delegated TC Sponsor (Optional)

N/A

#### GC Liaison

TBD

## Expected Timeline

Relative to project start:

- **Start:** form the Policies SIG, set up meetings and community table entries,
  and lock the initial policy scope (sampling, filtering, attribute
  sanitization).
- **~1 month in:** first draft of the canonical Protobuf schema and YAML
  representation, and the data model / enforcement specification split,
  circulated for review.
- **~2 months in:** alpha Collector component enforcing the initial policies,
  covering the match and keep stages for logs, metrics, and traces.
- **~3–4 months in:** match tracking and applied-policy reporting in the alpha
  component; experimental policies published.
- **Following:** align the java-contrib implementation as a second
  implementation of the same policies, and document integration with
  distribution mechanisms (OpAMP/Operator).

The SIG will give regular (roughly monthly) updates to the Maintainer and
Specification SIGs. After the project starts, specific target dates will be
tracked via GitHub project updates (see
[Project Lifecycle](project-management.md#project-lifecycle)).

## Labels (Optional)

- `policies`
- `spec:policies`
- `area:collector`

## GitHub Project (Post-Approval)

To be created from the
[GitHub Project template](https://github.com/orgs/open-telemetry/projects/140)
once the project is approved, pre-populated with issues covering the
deliverables above and organized by the timeline milestones. Link to be added
here.

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

Meeting times, Slack channel, and meeting notes will be posted on the
[OpenTelemetry public calendar](https://github.com/open-telemetry/community#calendar)
and added to the community SIG tables via [workstreams.yml](./workstreams.yml)
(running `make generate`), including the GitHub project ID as a `roadmapProject`
entry so the project appears in the OpenTelemetry Roadmap.
