# Resources and Entities

## Description

OpenTelemetry's usage of Resource has a number of known problems (see listed below). The Project's and the SIG's charter is to solve these and related problems. 

The background work on these problems and coming up with potential solutions have been in progress for more than a year now, with participation of the listed sponsors and other interested contributors. We have been waiting until there is sufficient understanding of what and how we would like to solve these problems and also until we are certain there is significant available contributing capacity and interest.

We believe we have arrived at that point and now is the time to start this project.

### Problem 1: Commingling of Entities

A Resource [is defined as](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/resource/sdk.md) a "representation of the entity producing telemetry". Note that the spec speaks about one particular producing entity. In practice we commingle multiple entities into one Resource. The spec then shows a clear example that talks about multiple entities (Process, Container, Pod, etc) in one Resource:

>For example, a process producing telemetry that is running in a container on Kubernetes has a Pod name, it is in a namespace and possibly is part of a Deployment which also has a name. All three of these attributes can be included in the Resource.

The problem with such usage is that by looking at the Resource attributes it is impossible to tell which of the represented entities is *the entity*, i.e. the entity which produced the telemetry.

### Problem 2: Lack of Precise Identity

The Resource is one set of attributes, which contains all attributes of all entities that the Resource represents. It is impossible to tell which of these attributes identify the entity (or entities) and which are non-identifying, i.e. purely descriptive.

This lack of precise identity makes it difficult or impossible to identify the same entities reported in different Resources. 

### Problem 3: Lack of Mutable Attributes

Resource is defined to be immutable in the OpenTelemetry SDK. This does not align well with the fact that non-identifying attributes of entities may change over time. For example OpenTelemetry Collector collects data about Pods and adds Pod labels as Resource attributes. Pod labels are mutable in Kubernetes and can change over time, while the Pod's identity remains immutable. Here is another example where [mutable Service attributes](https://github.com/open-telemetry/opentelemetry-specification/issues/3401#issuecomment-1511770735) are desirable.

With the current definition of the Resource we are forced to either leave out any attributes that may ever change over time or violate the spec definition.

Additionally, OpenTelemetry currently lacks the ability to provide resource attributes that require some kind of delayed lookup that may fail (see [this issue](https://github.com/open-telemetry/opentelemetry-specification/issues/1298)). Today, there are a variety of ad-hoc solutions across OpenTelemetry for dealing with these attributes, which may include delaying startup, forcing an external party to lookup the attributes or simply failing to provide the attributes.

In reality, OpenTelemetry SDKs can also easily violate the definition as soon as we consider mutability from a recipient's perspective. SDKs only guarantee immutability during a single process session. As soon as the process is restarted and the SDK is newly initialized, there is no guarantee that the Resource will have the same set of attributes (e.g. because `process.id` can be one of the Resource attributes).
It is clear that the strictly "immutable" definition of the Resource is not sufficient for what we are trying to model.

### Problem 4: Metric Cardinality Problem

Today every attribute in an OpenTelemetry Resource, according to the metric data model, is used to determine the identity of a metric. Given known issues in metric time-series database implementations around cardinality, this can cause major issues if Resources are allowed to leverage high cardinality attributes.

Given many Resource attribute semantic conventions today were defined for tracing instrumentation, we do find many high cardinality definitions, e.g. the [Process](https://github.com/open-telemetry/semantic-conventions/blob/main/docs/resource/process.md#process) resource includes `pid` and and `parent_pid`, which are known to churn between instances of an application and would lead to higher cardinality streams. 

Many metric backends are simply erasing resource attributes from metrics to workaround the issue.  Here's an example [solution for prometheus](https://github.com/open-telemetry/opentelemetry-specification/issues/1782), and [another proposal for yet another point-fix for prometheus](https://github.com/open-telemetry/opentelemetry-specification/pull/2736).

However, these workarounds prevent Metrics users from regaining descriptive attributes (and benefits) of current Otel Resource detection.

Source: [see this issue](https://github.com/open-telemetry/opentelemetry-specification/issues/2775).

### Further Reading 

For more details on the problems and proposed solutions please [see this document](https://docs.google.com/document/d/1VUdBRInLEhO_0ABAoiLEssB1CQO_IcD5zDnaMEha42w/edit).

## Deliverables

We plan to deliver the following:

- A specification of a new [concept of Entities](https://docs.google.com/document/d/1VUdBRInLEhO_0ABAoiLEssB1CQO_IcD5zDnaMEha42w/edit#heading=h.psbmkrtahy3d) and a definition of telemetry's Producing Entity concept.
- A backward-compatible extension of the concept of the Resource that seamlessly integrates with the concept of Entities.
- Precise solutions that target each of the problems listed above.
- A new entity signal, represented as events that describe how entities change over time. All other signals (logs, traces, metrics) will be correlated with entity signals, allowing to answer new interesting questions.
- An [extension of OTLP](https://docs.google.com/document/d/1VUdBRInLEhO_0ABAoiLEssB1CQO_IcD5zDnaMEha42w/edit#heading=h.dovorfw3l4sf) retaining full interoperability with existing senders and receivers. OTLP will allow recording extended resources and the new entity signal.
- A definition and implementation of new behaviors for the Collector that leverage newly available entity information:
  - To produce information about entities it observes.
  - To [enrich telemetry](https://docs.google.com/document/d/1VUdBRInLEhO_0ABAoiLEssB1CQO_IcD5zDnaMEha42w/edit#heading=h.ij8yjheo645z) that passes through it by additional entity-related information it possesses.
- A set of core Entities and stable semantic conventions for those entities
  - To bootstrap consistent identity for Otel users: Service, Process, Host, Container and k8s.
  - A set of prototype resource/entity detection code in multiple languages.

A set of prototypes has been implemented that demonstrate what these deliverables look like in practice:

### Go SDK Prototype:

See https://github.com/tigrannajaryan/opentelemetry-go/pull/244

### Collector Prototype

See https://github.com/tigrannajaryan/opentelemetry-collector/pull/4

### Collector Contrib Prototype

See https://github.com/tigrannajaryan/opentelemetry-collector-contrib/pull/1/files

### OTLP Protocol Buffer changes

See: https://github.com/tigrannajaryan/opentelemetry-proto/pull/2/files

## Staffing / Help Wanted

The project has 2 TC sponsors: Tigran Najaryan and Josh Suereth. The sponsors will also actively lead and contribute to the project. We are looking for other contributors that have expertise and interest in the project.

## Required staffing

Project leads and TC sponsors: Tigran Najaryan and Josh Suereth

Engineers willing to write prototypes and contribute:

- Go - Tigran Najaryan, Tyler Yahn (maintainer)
- Java - Josh Suereth, Jack Berg (maintainer)
- Rust - Josh Suereth
- Collector - Tigran Najaryan, Bogdan Drutu (maintainer), Dmitrii Anoshin (maintainer).

## Meeting Times
Once a project is started, the working group should meet regularly for discussion. These meeting times should be posted on the OpenTelemetry public calendar.

## Timeline

We expect the SIG to start working immediately. We will aim to deliver the initial design proposal by the end of the first half of 2024 and minimal working implementations by the end of 2024.

## Labels

The specification will use a new label "spec:entities" for this project.

## Linked Issues and PRs

All PRs, Issues, and OTEPs related to the project should link back to the tracking issue, so that they can be easily found.

## Project Board

Once approved by TC, a project should be managed using a GitHub project board. This project board should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

A Technical Committee (TC) member associated with the project can create the board, along with a new project-specific GitHub label to automatically associate issues and PRs with the project. The project lead and all other relevant project members should have edit access to the board.

Once created, please link to the project board here.
