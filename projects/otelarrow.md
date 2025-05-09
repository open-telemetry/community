# OpenTelemetry Protocol with Apache Arrow ("OTel-Arrow")

## Description

The OpenTelemetry Protocol with Apache Arrow ("OTel-Arrow") project is
currently in Phase 2.

In Phase 1, we built a reference implementation for streaming
OpenTelemetry data using Apache Arrow IPC between two Collectors to
achieve significant network savings through a compression "bridge".
The project's OpenTelemetry Collector components are maintained in the
Collector-Contrib repository and are [production ready, as summarized
in our blog post](https://opentelemetry.io/blog/2024/otel-arrow-production).

In Phase 2, we are building a reference implementation for improving
efficiency inside the Collector using Apache Arrow data frames as the
pipeline data object.  We aim to establish a foundation for working
with OTel-Arrow data in the Collector, for access to the Arrow
ecosystem.

## Project board

https://github.com/orgs/open-telemetry/projects/139

## Project governance

[See the success criteria, restrictions, and governance items listed in
our project phases document](https://github.com/open-telemetry/otel-arrow/blob/main/docs/project-phases.md).

## Deliverables

The Phase 2 deliverables are listed below:

- In-process OTAP pipeline implemented as Rust libraries. We view this
  as an appropriate choice, as stated in the [Phase 2 design
  rationale](https://github.com/open-telemetry/otel-arrow/blob/main/docs/phase2-design.md#choice-of-rust)
  ([discussion](https://github.com/open-telemetry/otel-arrow/issues/294)).
- Explore API design for column-oriented pipeline data object based on
  OTAP data frames. We will investigate how to work with OpenTelemetry
  data in a column-oriented way.
- Prototype for DataFusion integration with OpenTelemetry data. We
  will study the feasibility of an OTTL-transform implementation in
  DataFusion, specifically.
- Benchmarks measuring OTAP and OTLP pipelines in Rust and Golang. We
  aim to deliver a 2x to 10x performance improvement for OpenTelemetry
  processing pipelines.

## Community

We welcome contributors.  Users of OpenTelemetry with an interest in
connection OpenTelemetry data with the Apache Arrow ecosystem are
welcome to join and share their use-cases.

## Required staffing

Project leads / maintainers

* @jmacd
* @lquerel

Sponsoring TC members

* @reyang

Engineers contributing to the SIG

* @v0y4g3r
* @jaronoff97

Project approvers

* @drewrelmas
* @moh-osman3

## Meeting times

Bi-weekly Thursday at 08:00 PT.

Bi-weekly Tuesday at 16:00 PT.

See the [Calendar](../README.md#calendar) to find upcoming meetings.

## Timeline

Starting in April 2025, the team will spend 6 months on this investigation.
