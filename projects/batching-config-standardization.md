# Batching Configuration Standardization

## Description

The Batching Configuration Standardization project is a collaborative effort between the OpenTelemetry Collector and OpenTelemetry Configuration projects to come up with a standard agreement on functional configuration for batching. The goal is to come up with a configuration that addresses user needs for batching in the Collector and in SDKs, which can be communicated to users in a unified way.

## Background

The idea for this project began when groups in [the Collector](https://github.com/open-telemetry/opentelemetry-collector/issues/15132) and [the SDK](https://github.com/open-telemetry/opentelemetry-specification/issues/5068) proposed major changes to batching configuration around the same time. We decided to join forces and come up with a core specification for batching capabilities and configuration surface that can be shared by SDK Configuration and the Collector.

## Why It Matters

This aligns closely with the new [General Availability for OpenTelemetry](https://github.com/open-telemetry/community/pull/3452) project. There is a desire across the project to present more unified and cohesive experience between different OpenTelemetry tools. Batching is a fundamental building block of both the Collector and SDKs, and is a complicated topic for new users. A unified specification for how to configure batching that can apply to the Collector and to SDKs means that users don't need to learn batching strategies twice to have a solid end-to-end understanding of their OpenTelemetry deployments.

A centralized definition within the specification of batching configuration (and expected behaviour under that configuration) also makes the experience more consistent for users leveraging AI Agents; the batching details will be part of the overall specification that agents may be using as context/training data. 

## Deliverables

This is intended to be a short-term project with a single goal and definitive successful ending (it will not be an ongoing SIG). The results of this project will likely be:

* Consensus on batching config specification
    - This will manifest first as an [OTEP](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps#opentelemetry-enhancement-proposal-otep)
    - Some central specification entry so there is a generic place that SDKs and the Collector can agree on fundamental batching principles
    - The necessary modifications will be made to the relevant areas of the SDK specification that already exist on batching (such as the [Batching processor section of the Trace SDK Specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/sdk.md#batching-processor) along with equivalent sections for each signal type)
* At least two successful reference implementations of the specification
    - At least one staffed language to serve as the first wave of SDK reference implementations of the spec (we may end up staffed to do multiple languages in the first wave)
    - The OpenTelemetry Collector will be a unique implementation that aligns with the specification as much as possible within the `sending_queue::batch` section of the `exporterhelper` shared batching configuration section
* Languages that may be unstaffed at the start will follow as a long tail following the success of initial reference implementations

## Staffing/Help Wanted

### Required Staffing

Project Lead: Braydon Kains (@braydonk)

TC Sponsor: Josh MacDonald (@jmacd)

GC Liaison: Pablo Baeyens (@mx-psi)

Participators:

* Braydon Kains (@braydonk)
* Ida Hou (@xuechunhou)
* Israel Blancas (@iblancasa)
* Josh MacDonald (@jmacd)
* David Ashpole (@dashpole)
* Cijo Thomas (@cijothomas)
* More needed!

Implementers:

* Collector
    - Ida Hou (@xuechunhou) (Collector)
    - Braydon Kains (@braydonk) (Collector)
* Go
    - Israel Blancas (@iblancasa) (Go)
    - David Ashpole (@dashpole) (Go)
* Rust
    - Cijo Thomas (@cijothomas) (Rust)
* More needed for other languages!

## Timeline

* Gather Specification Requirements
    - Initial meetings to collect batching requirements and start refining the design
* Write OTEP
    - Once there is consensus among the project group, an OTEP will be co-authored
* Change Specification
    - If the OTEP is accepted by the broader approval group, the necessary additions/changes will be made to the specification
* Initial Implementation
    - The initial reference implementations (at least one language, the Collector) will be initially implemented likely as a proof-of-concept for the OTEP, but once the specification is finalized the implementations can be refined and merged
* Blog Post
    - A public blog post will be created explaining the new unified batching configuration experience across the Collector and languages
* Remaining language implementations
    - Any languages that were unstaffed during the initial project operation can follow as a long tail following the specification changes and initial reference implementations
