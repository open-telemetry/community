# OpenTelemetry on Mainframe

## Description

As we see a growing interest from customers to use OpenTelemetry on the mainframe, we'd like to propose a working group to define and stabilize semantic conventions supporting the observability of the mainframe and to introduce instrumentation for programming languages present on the mainframe.

This proposal has been created as result of a [series of meetings](https://docs.google.com/document/d/14p-bpofozTL4n3jy6HZH_TKjoOXvog18G1HBRqq6liE/edit?pli=1#heading=h.pss2tdsd549w) for the topic “OpenTelemetry on Mainframe” with contributions from participants of multiple vendors and is based on [this document](https://docs.google.com/document/d/1SM5BmM4st8n4giWuqe1shqN98d37VG9C_-di1hG6sbg/edit#heading=h.q3h9nwmyzjva).  

### Goals

-   Mainframe users can capture infrastructure metrics and logs with OpenTelemetry and can export these to the tools of their choice.
-   Mainframe users can capture application spans (traces), metrics, logs, and (eventually) profiles from their applications with OpenTelemetry and can export these to the tools of their choice.
    -   Context propagation works across different parts (subsystems) of each mainframe application, akin to how requests are traced across distributed services running on hosts and containers.
-   All captured telemetry has appropriate resource and interaction metadata attached to it, and this metadata conforms to the OpenTelemetry semantic conventions.
-   Capturing infrastructure and application telemetry from a mainframe incurs a minimal performance impact and allows for different deployment scenarios of the OpenTelemetry Collector to minimize both mainframe CPU costs and mainframe network egress costs.

## Deliverables

-   Definition of semantic conventions that capture the concepts of the mainframe including hardware, virtualization, z/OS and subsystems, Linux on IBM Z by aligning to and extending the existing semantic conventions across resources, metrics, logs, and traces. The enhancements of the semantic conventions are assumed to be generically applicable to the mainframe and apply to any OS on the mainframe incl. TPF and z/VSE. The approach for enhancing the semantic conventions will be based on the existing definitions and the on-going work for converging with the Elastic Common Schema (ECS), define rules for mapping the concepts of the mainframe to the existing conventions and extend them with additional attributes where needed, e.g., for representing the different types of CPU utilization in the multi-layer environment of the mainframe. 
-   Alignment of semantic conventions for virtualization between mainframe and other virtualizations solutions, as far as feasible and reasonable
-   Description of mapping between names and mainframe terms (for conventions not specifically defined as mainframe extensions)
-   Definition of a curated, most meaningful set of metrics (out of the thousands of available metrics) to be fully supported by the semantic conventions.
-   Description and definition of semantic conventions for metrics determined as result from aggregation across system topology to simplify handling in observability backends
-   Definition of approach for supporting instrumentation of mainframe-specific programming languages
-   Definition of approach for supporting instrumentation of mainframe-specific logs
-   Definition of approach for supporting trace context propagation
-   Code instrumentation (SDKs) for mainframe-specific programming languages and runtimes

## Staffing / Help wanted

Based on previous participation in the meeting for preparing this proposal, we foresee continued contributions from 12 to 15 people. In addition, this group will welcome contributors from various areas:
-   We look for participation from mainframe experts of all kinds: observability and monitoring experts, performance experts, virtualization experts, architects, and users of observability solutions for the mainframe and those who want to extend, simplify, and improve their current observability solution to the mainframe.
-   We welcome developers working with Assembler, COBOL, PL/1, and REXX, and engineers willing to contribute with the instrumentation for mainframe-specific programming languages.
-   We invite everybody to join who is passionate about the mainframe.
-   Two project leads who are willing to drive the project and address any issues which are not handled by other project members.
-   At least two sponsoring TC (Technical Committee) members. TC sponsors are dedicated to attending meetings, reviewing proposals, and in general being aware of the state of the project and its technical details. TC sponsors guide the project through the spec process, keep the tracking issue up to date, and help to ensure that relevant community members provide input at the appropriate times.
-   Contributors from Semantic Conventions WG: \<to be added\>
-   Maintainers or approvers: \<to be added\>

### Project Leads
[\@rrschulze](https://github.com/rrschulze) <br />
[\@youngaaronm](https://github.com/youngaaronm) 

### Staffing 
[\@MacNale](https://github.com/MacNale) <br />
[\@davdai01](https://github.com/davdai01) <br />
[\@jimporell](https://github.com/jimporell) <br />
[\@msomasu](https://github.com/msomasu) <br />
[\@jackjia-ibm](https://github.com/jackjia-ibm) 

#### GC sponsors 
[\@mtwo](https://github.com/mtwo) <br />
[\@alolita](https://github.com/alolita) <br />
[\@dyladan](https://github.com/dyladan)

#### TC support
The TC is supportive of the mainframe effort given that it doesn’t stretch existing OTel technical leadership. This means:
-   No major semantic changes are required in the short-term, the focus should be on fitting mainframe telemetry metadata into the existing OTel semantics
-   There are net-new people to OTel leading this.

### Slack Channel
[https://cloud-native.slack.com/archives/C05PXDFTCPJ](https://cloud-native.slack.com/archives/C05PXDFTCPJ)

## Meeting Times 
-   For now, proposing: Tuesdays at 10 a.m. PDT.

## Timeline
Start of workgroup in January 2024. The focus is on the implementation of three topics in separate tracks: Semantic Conventions, Code Instrumentation and Collector Enhancements. All three tracks are of equal importance, whereby some of the activities for the track Collector Enhancements rely on the results of the track Semantic Conventions, e.g., when metrics about the virtualization layers of the mainframe have to be gathered. Based on the learnings from the SDK implementation for COBOL, the track for Code instrumentation will provide further SDK implementations for other mainframe-specific languages.

### Track: Semantic Conventions
The focus of this track will be on mapping the mainframe concepts and metrics on the currently defined semantic conventions. Where no mapping can be done using the existing conventions, the corresponding requirements will be documented and they will be subject to enhancements of the conventions at a later stage.
-   Stage 1: Semantic conventions for basic mainframe concepts - 1H2024
-   Stage 2: Semantic conventions for curated list of metrics - 3Q2024

### Track: Code Instrumentation
-   Stage 1: Definition of approach for supporting instrumentation of mainframe-specific programming languages - 1Q2024.
-   Stage 2: SDK for COBOL - 2H2024
-   Stage 3: SDKs for other languages, e.g. PL/1, REXX or JCL - 1H2025

### Track: Collector Enhancements
-   Stage 1: Make the Collector compatible (runnable) within mainframe environments and support resource detection. Should be able to run from Linux on IBM Z, the Container Extension of z/OS (zCX) and the z/OS Unix System Services (USS). (Note: s390x support for Linux on IBM Z and zCX is already addressed by this [PR](https://github.com/open-telemetry/opentelemetry-collector-releases/pull/384)).
-   Stage 2: Make the Collector capture resource metrics from mainframes for z/OS and Linux on IBM Z, considering both agent and gateway deployments of the Collector.
-   Stage 3: Make the Collector capture logs from mainframes for z/OS and Linux on IBM Z, considering both agent and gateway deployments of the Collector.

## Examples: Enhancements of Semantic Conventions

### Metrics examples

[Metrics Semantic Conventions](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/)

| **Metrics**   | **Enhancements**  | **OS**           |
|------------- |-----------------|--------------|
| [system.cpu. - Processor metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/system-metrics/)    | Multiple types of processor (e.g., CP, IFL,..) <br /> Support of partitioning and virtualization (LPAR, VM)                                                                                                                               | z/OS, Linux |
| [system.memory. - Memory metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/system-metrics/)  | Several types of storage = memory, support of detailed metrics                                                                                                             | z/OS  |
| [process. - Process metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/process-metrics/)                                                              | Similar to z/OS address space but different <br /> Support of Control Block metrics  | z/OS and z/OS USS |
| [hw. - Common hardware metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/hardware-metrics/) | Detailed level mapping required (e.g., add type=crypto) | z/OS, Linux       |
| [hw.cpu. - Physical processor metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/hardware-metrics/)  | Multiple types of processors (e.g., CP, IFL, ...) <br /> Support of physical processor utilization| z/OS, Linux  |
| [hw.host. - Physical host metrics](https://opentelemetry.io/docs/specs/otel/metrics/semantic_conventions/hardware-metrics/) | For instance, LPAR power metrics  | z/OS and Linux    |
|      | Support of I/O Channels, FC, DASD, Crypto | z/OS, Linux       |
|      | Sysplex & CF, Workload Management    | z/OS              |
|      | Subsystem support | z/OS              |
| [Hostmetrics receiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/receiver/hostmetricsreceiver/internal/scraper/processscraper/documentation.md) <br /> process.command <br /> process.command_line  <br /> process.executable.name  <br /> process.executable.path | Because of concept differences, sometimes cannot be fully conformed. If we match process as z/OS address space, it's hard to follow exactly since the terms are different. | z/OS  |

### Resource examples

[Resource Semantic Conventions](https://opentelemetry.io/docs/specs/otel/resource/semantic_conventions/)

| **Metrics**   | **Enhancements**  | **OS**           |
|------------- |-----------------|--------------|
|  [service. - Service metrics](https://opentelemetry.io/docs/specs/otel/resource/semantic_conventions/)  | How to describe where the data is originally created?         |      z/OS, Linux |
| | How to describe resource relationships and relationships between infrastructure components (host to LPARs to VMs)?   | z/OS, Linux |

### Log Attribute examples

[Log Attribute Semantic Conventions](https://opentelemetry.io/docs/specs/otel/logs/semantic_conventions/)

| **Metrics**   | **Enhancements**  | **OS**           |
|------------- |-----------------|--------------|
| [event. - Event attributes](https://opentelemetry.io/docs/specs/otel/logs/semantic_conventions/events/)  |  Many other attributes other than the suggested one, e.g., for correlation to other signal types  | z/OS |

#### z/OS syslog Write-to-Operator (WTO) example
![zos_logs3](https://github.com/open-telemetry/community/assets/140042958/02e74fc0-b8fe-4e23-9aaf-67aab28d4a18)
