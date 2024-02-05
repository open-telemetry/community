<!--- Hugo front matter used to generate the website version of this page:
linkTitle: Roadmap
aliases: [/roadmap]
github_repo: &repo https://github.com/open-telemetry/community
path_base_for_github_subdir: tmp/community
github_project_repo: *repo
weight: 20
--->

# OpenTelemetry Project Roadmap

OpenTelemetry is a healthy open source community, and contributors are free to
propose new work streams or work on any part of the project that they desire.
However, there's also value in the project focusing community members of
specific bodies of work and releases, as this allows us to form a more cohesive
set of capabilities (unified semantics, single implementations for each
language, etc.) and to ship the project in a more impactful way (new signal
types release across multiple languages at once, etc.).

This roadmap is not _law_, and it is not meant to be used to force people to
work on specific projects -- this is an open source project and we (community
members, the governance committee, etc.) are not anyone's boss. Rather, it
exists to provide direction to new contributors, to the public and end users who
want to know what's coming next, and to attempt to channel the bulk of our
concentration and development efforts into the areas where they are most needed.

## What We've Accomplished

OpenTelemetry was started in 2019 with the promise of making it easy and
consistent for developers to capture distributed traces and metrics from their
applications and infrastructure using SDKs, the Collector, and OTLP. Since then,
we've delivered:

- A specification for distributed traces and metrics, which defines the objects
  used to represent each, how to interact with them, and the types of data that
  are expected for different sources.
- Semantic conventions for metadata, which define how resources and other
  components are represented. This is applied consistently across all signal
  types, which allows traces, metrics, and other signals to be processed
  consistently and correlated.
- SDKs for twelve languages that allow developers to capture telemetry from
  their services and to create their own custom telemetry.
- Automatic instrumentation for \_\_ languages, which allow anyone to capture
  telemetry from their services without making code changes or redeploying.
- Instrumentation libraries for thousands of pieces of software, including
  operating systems, container runtimes, databases, language runtimes, and
  libraries, all of which allow the Collector (for infrastructure and
  third-party applications), and SDKs and automatic instrumentation agents (for
  custom applications) to capture signals, capture metadata, and propagate
  context automatically.
- A protocol, OTLP, for transmitting telemetry and metadata between
  OpenTelemetry components and to backends for processing.

## Major Priorities

All of the following work streams are major areas of investment for
OpenTelemetry: all of them have large groups of people already focused on them.
Their priorities primarily reflect the ordering of when we expect them to be
released.

These priorities are most useful when comparing them against each other. For
example, P0 entries are more critical than P1 entries, which are in turn more
critical than P2s. We do have some basic definitions of each priority level,
however:

- P0: We must do this within the specified time frame (if there is one), or we
  will fail as a project
- P1: This is one of our most important major initiatives, and it will have a
  major impact on the project
- P2: This work is important enough to be tracked and prioritized and is more
  important than items not on this list, but it is currently lower urgency or
  criticality than P0 and P1 entries

### P0: Continued Investment in OpenTelemetry Artifacts

The project's top priority will always be ensuring that the capabilities and
robustness of our existing artifacts (the Collector, SDKs, language agents,
etc.) remain excellent. This work takes place in each language SIG and in the
Collector SIG, and includes continual improvement to these components, making
them even easier to use, providing and integrating more instrumentation
libraries, working with the suppliers of telemetry sources to use the
OpenTelemetry APIs natively, and more.

### P1: Logs

OpenTelemetry established a logging SIG in mid-2020, with two goals:

1. Providing a performant path for capturing logs from existing sources
   (typically text files on disk), where all captured logs have OpenTelemetry's
   metadata consistently applied to them.
2. Providing a new, strongly-typed and extremely high-performance logging path
   for new applications, which allows logs to be authored and transmitted
   without being parsed from text, and which enforces the consistency of all
   metadata.

Much progress has been made on the first item, particularly through the donation
of the Stanza logging agent into the OpenTelemetry Collector, and by the
investments that the project has made in defining and stabilizing a data model
and OTLP format for logs. However much still remains before we can declare our
logging work generally available:

- We must extend the Collector's support for existing log sources to satisfy the
  requirements of more users.
- Elastic donated the Elastic Common Schema to OpenTelemetry's semantic
  conventions. We must fully integrate this.
- We must prototype the new logging path within our SDKs, update the designs
  based on feedback from the prototyping effort, build integrations for existing
  logging components and telemetry sources, implement these designs across all
  languages (as we did for traces and metrics), and test and revise these
  implementations from beta through GA.

### P1: Further Stabilizing Semantic Conventions

OpenTelemetry's consistent semantic conventions across all data types are a
major source of the project's value, as they allow end-users and observability
systems to both correlate related signals and set expectations about the
metadata that should be present on telemetry captured from specific sources or
types of interactions. For example, OpenTelemetry's semantics describe the
expected metadata for traces, metrics, and logs captured as part of an HTTP 4xx
response.

However we still need to define the semantic conventions for more scenarios, so
that instrumentation authors can release stable instrumentation libraries and so
that end-users and observability systems can make firmer dependencies on
OpenTelemetry's metadata.

### P2: Client Instrumentation (RUM)

We want OpenTelemetry to provide true end-to-end visibility to service owners,
including E2E latency (including client app and internet latency) and the chain
of backend service events and infrastructure-side performance stats that take
place from a single user interaction. This requires OpenTelemetry to start
supporting webpage JS, mobile applications, and desktop applications.
OpenTelemetry JS has technically supported capturing spans from web browsers
since its first releases, however this behavior was mostly unspecified, and
there was no equivalent functionality for other types of client applications
like those on Android, iOS, or Windows.

In late 2021, the Client Instrumentation SIG (often called the RUM SIG) was
established, which seeks to specify client instrumentation behavior so that
there is consistency in the data captured from and in the developer-facing
telemetry interfaces in different types of client applications. This SIG is
currently completing its first round of spec work, which will need to be
implemented by the JS, Swift, Java, and other SIGs once it is complete.

### P2: Profiling

Distributed profiling has been a long-standing topic of discussion within
OpenTelemetry, and contributors to other profiling projects have advocated for
it to be added to OpenTelemetry as an additional signal type. In May of 2022,
this work commenced within OpenTelemetry's profiling SIG.

Sampled heap and CPU profiles will allow OpenTelemetry to extend end-users'
visibility to the performance of their actual code. While other profiling
solutions allow this kind of inspection today, few are able to properly
correlate profiles with application and infrastructure resource metadata, and
even fewer are able to correlate profiling telemetry with distributed traces or
other signals. Adding this to OpenTelemetry will allow analysis solutions and
end-users to find instances of poor performance between services and then
immediately chase these down to their root cause within code.

### P2: OpenTelemetry Demo

OpenTelemetry launched a community demo SIG in May 2022, which will provide
sample applications that demonstrate OpenTelemetry's capabilities to prospective
end users, and also allow the community to better perform automated testing of
OpenTelemetry components. The project's first release occurred in October 2022,
and we will be further investing in the demo throughout 2023 and beyond.

### P2: OpenTelemetry Control Plane

Since OpenTelemetry's initiation, end-users and vendors have expressed a desire
to (a) understand what SDKs, language agents, and Collectors are deployed within
their environment (along with their status), and to (b) be able to make changes
to the configuration of these artifacts or possibly even update agent binaries.

Specification work is already underway to address both of these needs, and the
agent management SIG has already produced a specification for OpAMP, the
protocol that will drive these interactions. Over time, the SIGs that develop
various OpenTelemetry artifacts will need to implement OpAMP to enable these
scenarios.

## Backlog

These topics have been discussed in the past, but have either been deliberately
prioritized beneath the project's major ongoing priorities, or have yet to have
a large group of contributors form up behind them.

- eBPF instrumentation (in-progress for the Collector via a small group of
  contributors).
- Production debugging / dynamic log injection.
- Automatically configuring the Collector to capture data from more sources.
- Capturing telemetry (with appropriate semantics) from CI / CD systems.
- Semantics for describing cloud spend and the environmental impact of cloud
  resource usage.
- Enhanced user / organization extensibility of OpenTelemetry's semantic
  conventions.
