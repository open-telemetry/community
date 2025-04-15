# OpenTelemetry Sampling

## Description

The OpenTelemetry Sampling project aims to improve sampling support in
OpenTelemetry through protocol, API, and SDK features. This project
works with the W3C trace context group to coordinate distributed
tracing protocols across the observability industry.

The project aims to complete the OpenTelemetry SDK specification with
support for consistent probability head sampling with configurable SDK
samplers.

## Project board

https://github.com/orgs/open-telemetry/projects/133

## Deliverables

The Sampling project has several OTEPs to develop the foundation
for probability sampling in OpenTelemetry.

- [OTEP 168](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/trace/0168-sampling-propagation.md)
- [OTEP 170](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/trace/0170-sampling-probability.md)
- [OTEP 235](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/trace/0235-sampling-threshold-in-trace-state.md)
- [OTEP 250](https://github.com/open-telemetry/opentelemetry-specification/blob/main/oteps/trace/0250-Composite_Samplers.md)

The project coordinates development of SDK and Collector prototypes
and support libraries.

Maintainership of [Collector-Contrib sampling package](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/pkg/sampling), [Collector-Contrib probabilistic logs/span sampler](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/processor/probabilisticsamplerprocessor).

## Community

We welcome contributors.  Users of OpenTelemetry with an interest in
sampling of all kinds, please join our SIG or #otel-sampling channel
to discuss.

## Required staffing

Sponsor

* @jpkrohling

Engineers contributing to the SIG

* @jmacd
* @oertl
* @PeterF778
* @kentquirk
* @yuanyuanzhao3

## Meeting times

Every other Thursday at 8AM PT.

## Timeline

2021-22: Experimental specification based on `p`-value and `r`-value with power-of-two support.
2023-24: Modern specification based on `th`-value and `rv`-value with 56 bit support.
2024-25: Composable sampler definition, configuration support.
