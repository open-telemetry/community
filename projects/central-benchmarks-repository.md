# Central OpenTelemetry Benchmarks Repository

## Description

This project establishes
`open-telemetry/benchmarks` as
the project-owned home for cross-language performance scenarios, with a public
dashboard that tracks release-over-release results.

The initial scope is intentionally narrow: stand up the repository, land one
shared scenario (S1: counter API call), and publish a dashboard with data
points from 2-3 language implementations. Working prototypes for .NET, Rust,
and Java already exist at
[`cijothomas/otel-benchmarks`](https://github.com/cijothomas/otel-benchmarks)
with a live dashboard at
<https://cijothomas.github.io/otel-benchmarks/>, so v1 is essentially a move
and a permissions handshake.

## Background

The technical proposal is captured in
[OTEP 5109](https://github.com/open-telemetry/opentelemetry-specification/pull/5118).
Today many language SIGs run their own benchmarks, in their own repos, on
their own schedules, with no cross-language view. A central repository
gives the project a single, citable answer to "how does OTel perform across
languages, and how is that changing over time?" without each SIG having to
give up its own internal CI benchmarking.

Most language SIGs already run their own benchmarks; a few (e.g. JavaScript
and Python) also publish them to their language docs on opentelemetry.io.
This project does not change that: each SIG continues to own and run its own
benchmarks, and may publish them to its language docs as it sees fit. The
central repository adds one common, cross-language page built on standardized
scenarios (starting with S1), so the same scenario can be compared across
implementations. Migrating existing per-language benchmark pages into the
central dashboard is out of scope for v1. The Collector benchmark is likewise
out of scope: this project covers language API/SDK implementations.

## Why It Matters

OpenTelemetry's
[mission](https://github.com/open-telemetry/community/blob/main/mission-vision-values.md)
is to make high-quality telemetry a built-in feature of cloud-native software.
Performance directly determines whether that adoption actually happens —
library authors will not instrument with OTel natively if doing so adds
meaningful overhead, and operators will not enable signals that cost too
much. A central, public benchmarks repository is how the project shows the
world that we walk the talk on performance: results are visible, comparable
across languages, and tracked release-over-release.

Concretely:

- **Cross-language visibility**: today there is no single place to see, for
  the same scenario, how each language implementation performs.
- **Release-over-release trend**: per-release data points show whether the
  project is getting faster or slower over time, per language.
- **Library author confidence**: scenarios like S1 (cost of a counter API
  call when no SDK is wired up) let library authors evaluate the cost of
  instrumenting their libraries natively with OTel.

## Deliverables

This is a short project with a definitive ending. v1 is done when:

1. `open-telemetry/benchmarks` exists, with the layout from
   [OTEP 5109](https://github.com/open-telemetry/opentelemetry-specification/pull/5118)
   and `CODEOWNERS` set up.
2. Scenario S1 is implemented and published for at least 2 languages.
3. The dashboard is public and reachable from the repo README.

Everything beyond this (more scenarios, more languages, demo-based e2e
scenarios) is deliberately out of scope for v1 and tracked as future work in
the OTEP.

## Staffing

This is a small project; staffing is intentionally minimal.

### TC Sponsor

- David Ashpole ([@dashpole](https://github.com/dashpole))

### GC Sponsor

- Trask Stalnaker ([@trask](https://github.com/trask))

### Repository maintainers

- Cijo Thomas ([@cijothomas](https://github.com/cijothomas))
- Martin Costello ([@martincostello](https://github.com/martincostello))

The maintainers will provide guidance to language SIGs on contributing a
harness for their implementation, and to anyone proposing a new scenario
(scope, methodology, expected outputs). Ownership follows the same model
as [`opentelemetry.io`](https://github.com/open-telemetry/opentelemetry.io):
the repository has its own maintainers (above) for shared content
(scenarios, workflows, top-level docs), while each per-language harness
folder is owned via `CODEOWNERS` by the approvers of the corresponding
language SIG. This means onboarding a new language does not require any
additional project-level staffing.

While the v1 deliverables are time-boxed, the repository and dashboard are
long-lived and need ongoing maintenance once v1 ships: the shared parts
(scenarios, workflows, dashboard, top-level docs) are maintained by the
repository maintainers above, and each per-language harness is maintained by
its SIG's approvers via `CODEOWNERS`. Maintainers can be added as interest
grows, and the standard emeritus process applies if one steps down, so the
shared infrastructure stays staffed beyond the initial v1 effort.

## Timeline

Once OTEP 5109 is accepted, the repository can be created and v1 wrapped
up in 1-2 weeks of elapsed effort. The prototypes already work end-to-end;
this project is mostly the move and the `CODEOWNERS` setup.

## Future Possibilities

Out of scope for v1, but plausible follow-ups (also captured in the OTEP):

- Additional scenarios (span/log emission, sampled-out fast path, exporter
  cost, enrichment cost, etc.).
- Onboarding additional languages.
- End-to-end scenarios run against the OpenTelemetry Demo (e.g. measuring
  the cost of moving span filtering between SDK and Collector).

If any of those grow large enough to need their own staffing or governance,
they can be proposed as separate projects at that time.
