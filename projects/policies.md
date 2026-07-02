# Initial Policies Implementation

## Background and description

With the recent merge of the
[Policies OTEP](https://github.com/open-telemetry/opentelemetry-specification/pull/4738),
there is significant interest in implementing Policies across the OpenTelemetry
ecosystem. Policies introduce an intent-based specification for configuring how
telemetry components process data. A Policy is an atomic, self-contained rule
that declares a single intent — "match specific telemetry and apply an action" —
and can be evaluated identically regardless of where it runs.

Because Policies are self-contained, independent, and can be evaluated in
parallel and scaled to thousands of rules without degradation. The same policy
behaves the same way whether it executes inside an SDK, a Collector, or any
other specification-compliant component, and policies are designed to be defined
centrally and distributed to running systems.

This project coordinates the initial work needed to move Policies from an
accepted OTEP to an accepted specification: defining the specification, defining
the canonical Protobuf schemas, and building an initial prototype in the
Collector for validation.

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

- Refine and stabilize the Policy specification so that it is general, minimal,
  and implementable consistently across logs, metrics, and traces.
- Define the canonical Protobuf schema for Policies, with a human-authorable
  YAML representation and bidirectional conversion (including shorthand forms).
- Build an initial prototype in the OpenTelemetry Collector that evaluates
  policies through the two-stage model (match, then keep & transform) and honors
  the core guarantees: atomicity, fail-open behavior, idempotence, and
  data-model-based field references for portability.
- Establish match tracking (hits/misses) so operators can observe policy
  effectiveness.
- Validate that the same policy semantics can later be implemented in SDKs.

**Requirements the model must preserve:**

- **Fail-open:** an invalid policy becomes inert rather than breaking valid
  policies or dropping telemetry.
- **Atomic and self-contained:** one matcher set, one action set, no references
  to other policies, no ordering dependency.
- **Portable:** field references use the OpenTelemetry data model so a policy
  runs identically across conformant runtimes.

**Why now:** the OTEP has just merged and there is broad interest across SIGs.
Coordinating the specification, schema, and a reference prototype now delivers
immediately on the goals of the OTEP. Delivering this gives OpenTelemetry a
common, governable way to express telemetry-processing intent that can be
enforced anywhere in the pipeline.

## Deliverables

- **Policy specification refinements.** Iterate on the merged OTEP into
  specification text covering the two-stage execution model (match; keep &
  transform), the matcher system (field selectors, match types, options,
  `AttributePath` nested traversal), keep/sampling semantics for logs, metrics,
  and traces, transform operations (remove, redact, rename, add), precedence
  (most-restrictive-wins), and the error-handling taxonomy (parse, compilation,
  runtime).
- **Canonical Protobuf schema** for Policies, plus the YAML authoring format and
  documented bidirectional conversion including shorthand forms.
- **Collector prototype** implementing policy evaluation across logs, metrics,
  and traces, including fail-open handling and match tracking.
- **Example policies** demonstrating transformation, sampling, and attribute
  sanitization/redaction.
- **Integration direction** documenting how Policies relate to distribution
  mechanisms (e.g. OpAMP, the OpenTelemetry Operator) and to policy composition
  ("merger") — with dynamic distribution intentionally kept separate from core
  policy semantics so both can iterate independently.

Per OTEP requirements, specification work will be backed by working prototypes
in at least two languages/components before an OTEP for any follow-on refinement
is accepted. These requirements should be discussed with a TC member before
submitting.

## Staffing / Help Wanted

### Industry outreach (Optional)

The Policies concept originated in discussions at KubeCon NA 2025 on
policy-based control of telemetry. Interested parties across the SDK, Collector,
Operator, and OpAMP SIGs, as well as vendors building telemetry-processing
products, should be aware of this effort and are invited to participate.

### SIG

A new Policies SIG will lead this work. Initial coordination and the reference
prototype will happen in collaboration with the Collector SIG.

### Required staffing

See [Project Staffing](/project-management.md#project-staffing)

#### Project Leads(s)

- **@jaronoff97** (Tero) – Maintainer
- **@jsuereth** (Google) – Maintainer
- **@dashpole** (Google) – Maintainer
- **@jackshirazi** (Elastic) – Maintainer

#### Other Staffing

Contributors from the Collector, SDK, Configuration, OpAMP, and Operator SIGs
are being recruited. Maintainers/approvers from those SIGs committed to
reviewing the specification and prototypes will be listed here as they commit.

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
  and align on the specification scope carried over from the OTEP.
- **~1 month in:** first draft of the canonical Protobuf schema and YAML
  representation circulated for review.
- **~2 months in:** initial Collector prototype covering the match and keep
  stages for logs, metrics, and traces.
- **~3–4 months in:** transform operations and match tracking in the prototype;
  example policies published.
- **Following:** validate the model with a second implementation (SDK) toward
  meeting the two-language prototype requirement, and document integration with
  distribution mechanisms (OpAMP/Operator).

After the project starts, specific target dates will be tracked via GitHub
project updates (see
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
