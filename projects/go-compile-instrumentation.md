# Bootstrap Go compile time instrumentation

## Description

The primary objective of the Go Compile time Instrumentation SIG is to streamline and automate the code instrumentation process around the Go compiler. By integrating automatic instrumentation into the Go compilation process, we aim to provide developers a seamless, efficient, and safe way to instrument their Go applications for observability (and more).

This SIG will focus on:

- Developing compiler plugins or enhancements that inject instrumentation code automatically, ensuring minimal runtime performance overhead and compatibility with existing Go projects.
- Providing standardized instrumentation patterns aligned with OpenTelemetry and other monitoring frameworks.

We want to ensure:

- Comprehensive Coverage: Automatic instrumentation covers common frameworks and libraries used in Go applications, fully compatible with OpenTelemetry’s APIs and SDKs.
- Performance Efficiency: Instrumentation introduces minimal runtime overhead, maintaining the high-performance standards of Go applications while utilizing OpenTelemetry’s optimized data collection mechanisms.
- Ease of Use: Developers can enable instrumentation with simple/zero configuration changes without manual code modifications.
- Extensibility: The instrumentation framework can be extended to support new libraries and frameworks as they emerge in the Go ecosystem, ensuring ongoing compatibility with the evolving OpenTelemetry landscape.
- Flexibility: Developers are enabled to control their tracing experience (i.e, specifying custom span tags in certain places; opting certain code paths or instances out of tracing, etc...), which can be delivered via a declarative/programmable scheme.

By closely aligning with OpenTelemetry, the Go Compile Instrumentation SIG ensures that Go applications benefit from standardized, vendor-neutral, high-quality observability solutions that are both robust and easy to implement. Having one single, standard tool removes decision points from prospective developers, which makes the path to observability shorter & easier.

## Project Board
Project Board: https://github.com/orgs/open-telemetry/projects/130

## Deliverables

- A flexible and extensible instrumentation framework for Go at compile time
- Out-of-box instrumentation for common libraries and frameworks in Go application. Initial support will be provided for key areas, each with one or two libraries. The proposed initial support for library instrumentation includes as follows and is subject to change:
  - HTTP/RPC: gin, grpc
  - Messaging: kafka
  - Database: mysql
  - NoSQL: redis
- Comprehensive documentation that covers a wide array of topics, including how to use the framework, configuration options, advanced usage scenarios, and answers to FAQs

## Staffing/Help Wanted
The following vendors are interested in improving this area:

- Alibaba
- Datadog
- QuesmaOrg

We also welcome everyone interested in this area to participate in the discussion.

### Required staffing

- Project Lead: @ralf0131(Alibaba), @dineshg13(Datadog), @pdelewski(QuesmaOrg)
- Sponsoring GC Members: @jpkrohling

Additionally, the following people will participate in the SIG and be added as approvers once they are OpenTelemetry Github org members:

- Future Approvers: @yiyang0(Alibaba), @123liuziming(Alibaba), @RomainMuller(Datadog)

## Meeting Times

- Biweekly Meetings: Every Thursday
- China (UTC+8): 16:00 – 17:00
- Europe (UTC+2): 10:00 – 11:00
- UTC: 08:00 – 09:00

Note that members from UTC-5 would not be able to attend the meeting, so the project members will try and make things work asynchronously as possible.

## Timeline

- Step 1: SIG Formation and Initial Setup
- Step 2: Collaborative Architectural Design (1-2 months)
- Step 3: Assignment of Implementation Owners
- Step 4: Implementation and Integration (1-2 months)

## Repo

open-telemetry/opentelemetry-go-compile-instrumentation

## Reference
The project is a joint effort of donation proposal coming from Alibaba and Datadog to replace [Instrgen](https://github.com/open-telemetry/opentelemetry-go-contrib/tree/v1.34.0/instrgen). The proposals are listed as follows:
- https://github.com/open-telemetry/community/issues/2344
- https://github.com/open-telemetry/community/issues/2497
