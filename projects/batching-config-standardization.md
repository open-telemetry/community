# Batching Configuration Standardization

## Description

The Batching Configuration Standardization project is a collaborative effort between the Collector, SDK, Declarative Configuration projects to come up with a standard agreement on functional configuration for batching. The goal is to come up with a configuration that addresses user needs for batching in the Collector and in SDKs, which can be communicated to users in a unified way.

## Background

The idea for this project began when groups in [the Collector](https://github.com/open-telemetry/opentelemetry-collector/issues/15132) and [the SDK](https://github.com/open-telemetry/opentelemetry-specification/issues/5068) proposed major changes to batching configuration around the same time. We decided to join forces and come up with a core specification for batching capabilities and configuration surface that can be shared by SDK Configuration and the Collector.

## Project Goals

There is a desire across the project to present more unified and cohesive experience between different OpenTelemetry tools, and batching is a fundamental building block of both the Collector and SDKs. A unified specification for how to configure batching that can apply to the Collector and to SDKs means that users don't need to learn different batching principles to be able to configure end-to-end resiliency of their OpenTelemetry deployments.

It will likely be impossible to make batching configuration **literally** identical between the Collector and SDK declarative config, as the foundational config mechanisms are completely distinct between them. The goal is to make it so that in both scenarios, the available behaviours to configure are clear and as similar as possible, and should feel familiar for users crossing over between the different configuration experiences.

## Deliverables

This is intended to be a short-term project with a single goal and definitive successful ending (it will not be an ongoing SIG). The results of this project will likely be:

* Consensus on batching config specification
    - This will manifest first as an [OTEP](https://github.com/open-telemetry/opentelemetry-specification/tree/main/oteps#opentelemetry-enhancement-proposal-otep)
    - Some central specification entry so there is a generic place that SDKs and the Collector can agree on fundamental batching principles
    - The necessary modifications will be made to the relevant areas of the SDK specification that already exist on batching (such as the [Batching processor section of the Trace SDK Specification](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/trace/sdk.md#batching-processor) along with equivalent sections for each signal type)
* At least three successful reference implementations of the specification
    - At least two staffed languages to serve as the first wave of SDK reference implementations of the spec (we may end up staffed to do multiple languages in the first wave)
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
* Aaron Abbott (@aabmass)
* More needed!

Implementers:

* Collector
    - Ida Hou (@xuechunhou)
    - Braydon Kains (@braydonk)
* Go
    - Israel Blancas (@iblancasa)
    - David Ashpole (@dashpole)
* Rust
    - Cijo Thomas (@cijothomas)
* Python
    - Aaron Abbott (@aabmass)
* More needed for other languages!

## Where We Operate

The primary activity will be a Slack channel and ad-hoc organized meetings while we are in the initial design phase of the project. When concrete tasks exist, we may provision a GitHub Project Board if it seems appropriate.

## Timeline

We anticipate the effort of this project to be around 6 months. (This is purely an estimate of effort and not a declaration of how long the project will take; individual availability and potential pivots during the RFC period will likely make this project take longer)

1. Gather Specification Requirements (2-3 Weeks)
    - Initial meetings for open discussion on what the OTEP and spec updates need to address
1. Write OTEP (2 Months)
    - Once there is consensus among the project group, an OTEP will be co-authored
    - Large time estimate given for open RFC period
1. Change Specification (2 months)
    - If the OTEP is accepted by the broader approval group, the necessary additions/changes will be made to the specification
1. Initial Implementation (2 months, parallel with previous steps)
    - The initial reference implementations (at least two languages and the Collector) will be initially implemented as a proof-of-concept for the OTEP, but once the specification is finalized the implementations can be refined and merged
1. Blog Post (1 week)
    - A public blog post will be created explaining the new unified batching configuration experience across the Collector and languages
1. Remaining language implementations (ongoing)
    - Any languages that were unstaffed during the initial project operation can follow as a long tail following the specification changes and initial reference implementations
