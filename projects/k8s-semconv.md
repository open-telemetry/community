# K8s Conventions SIG

## Background and description

Kubernetes is the leading platform for Opentelemetry Collector deployment (80.6%) according
to a recent [survey](https://opentelemetry.io/blog/2024/otel-collector-survey/#otel-components-usage).
The OpenTelemetry community would like to stabilize k8s semantic conventions including k8s/container metrics
in order to help the adoption of the respective OTel Collector receivers and processors.
The goal of this SIG project is to work towards this direction.

### Current challenges

At the moment there is no specific effort to align the Collector's implementation with
the K8s Semantic Conventions and at the same time there is no big trust that the K8s Semantic Conventions
can be considered as stable.

### Goals, objectives, and requirements

The primary goal of this project is to focus on the defining a solid base in the K8s Semantic Conventions
and work on adopting the Collector accordingly. Some of the issues that the group will be focusing are the following:

* [META: Define Semantic Conventions for k8s metrics](https://github.com/open-telemetry/semantic-conventions/issues/1032)
* [Clarify the brief of container.image.id](https://github.com/open-telemetry/semantic-conventions/issues/1236)
* [Define rules for Kubernetes name and uid resource attributes](https://github.com/open-telemetry/semantic-conventions/issues/430)
* [Add k8s.pod.ip attribute](https://github.com/open-telemetry/semantic-conventions/issues/1160)
* [k8s: add metric for pod status conditions](https://github.com/open-telemetry/semantic-conventions/issues/1398)
* [Proposal: Define mapping from k8s well-known labels to semconv](https://github.com/open-telemetry/semantic-conventions/issues/236)
* [k8s: new attributes: CSI driver and volume handle](https://github.com/open-telemetry/semantic-conventions/issues/1119)
* [[k8sclusterreceiver] refactoring pod status phase](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/24425)
* [Align K8s SemConv with Entities work](https://github.com/open-telemetry/semantic-conventions/issues/1420)
* [Associate K8s metrics with resource attributes](https://github.com/open-telemetry/semantic-conventions/issues/1421)
* TBA

## Deliverables

* Introduce and stabilize k8s semantic conventions.
* Update existing OpenTelemetry Collector components to conform with the stable conventions.

## Staffing / Help Wanted

We are seeking domain experts to work on the introduction and stability of the K8s Semantic Conventions.

The goal is to follow @tedsuo's proposed [Semantic Convention Process](https://docs.google.com/document/d/1ghvajKaipiNZso3fDtyNxU7x1zx0_Eyd02OGpMGEpLE/edit#heading=h.xc2ft2cddhny).

- Stage 1: SIG Preparation
- Stage 2: Stabilizing the Specification
- Stage 3: Implementation

## Timeline

Timeline
Stage 1 (SIG Preparation) is happening now.

Stage 2 (Stabilizing the Specification) will begin as soon as we have adequate
staffing for this project, and we coordinate weekly
meeting times (currently targeting X).

Stage 3 (Implementation) will begin as soon as the k8s metrics and resource attributes are marked stable,
and it should be relatively short we only need to update conformance to the specification for a few collector components.

## Labels

* area:k8s
* area:containers

### Required staffing

**Project Leads:**

- @ChrsMark (Elastic)
- @dashpole (Google)

**Domain Experts:**

- @dmitryax (Splunk/Cisco)
- @TylerHelmuth (Honeycomb)
- @rogercoll (Elastic)
- @jaronoff97 (Lightstep)
- @povilasv (Coralogix)
- @jinja2 (Splunk/Cisco)
- ...

**Sponsors:**

- @jsuereth (Google)
- @AlexanderWert (Elastic)

**GC liaison:**

- TBA

**SemConv Maintainers:**

- @open-telemetry/semconv-k8s-approvers

**Collector's components code-owners:**

- @dmitryax (Splunk/Cisco)
- @TylerHelmuth (Honeycomb)
- @povilasv (Coralogix)
- @ChrsMark (Elastic)

**Language specific maintainers:**

## Project Board

[K8s SemConv SIG project board](https://github.com/orgs/open-telemetry/projects/114)

## SIG Meetings and Other Info

*meeting time*: biweekly on Tuesday 7:30am PDT

*meeting-notes*: [Agenda](https://docs.google.com/document/d/17DqFVlLvO43neXXTwlSd1zcKjSRA8P3d0Y444QNwUTQ)

*cncf-slack*: For async conversation please use [#otel-k8s-semconv-sig](https://cloud-native.slack.com/archives/C07Q1L0FGKX) slack channel from official CNCF slack workspace.
