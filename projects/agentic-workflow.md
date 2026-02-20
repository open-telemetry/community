# OpenTelemetry Collector Agentic Workflows

## Background and description

The OpenTelemetry project consists of a large number of components, including collector, SDKs, and instrumentation libraries, which are often configured and managed separately. This distribution of components poses a major operational challenge which is universally recognized by the community [1](https://opentelemetry.io/blog/2025/otel-rocks/), [2](https://www.youtube.com/watch?v=xEu8_Aeo_-o).

Large language models (LLMs) and Agentic Workflows present a significant opportunity to simplify the adoption, implementation, and management of the OpenTelemetry stack. An AI agent could, for example, facilitate configuration changes, resolve deployment issues, or assist and simplify the instrumentation process.

At the moment, the OpenTelemetry project does not have official support for these workflows. This has led to the creation of several independent, open-source projects (MCP servers) to fill the gap.
The [Can AI instrument OpenTelemetry](https://quesma.com/benchmarks/otel/) Benchmark demonstrates the complexity of instrumentation process and shows the gap of successfully using AI agents with OpenTelemetry.

As AI tooling becomes a standard part of developer workflows. Users, which are looking to extend their agents with tooling optimized for OpenTelemetry, have no easy way to discover what's available in the ecosystem. There's no central place to learn which MCP servers or other tools exist, what capabilities they offer, or where to file issues/requests.

This project is also motivated by the need to support the [Stability Proposal](https://opentelemetry.io/blog/2025/stability-proposal-announcement/) and [[Graduation] OpenTelemetry Graduation Application](https://github.com/cncf/toc/issues/1739). While the [OTEP: Stable by Default](https://github.com/open-telemetry/opentelemetry-specification/pull/4813) initiative aims to default to stable components, a large portion of the ecosystem—including the majority of collector components—remains in alpha or beta, creating complexity for users around potential breaking changes. This project aims to bridge this gap without adding core functionality or duplicating documentation. Instead, it focuses on making OpenTelemetry easier to use and more stable by enriching the ecosystem with new agentic workflows.

### Existing OpenTelemetry MCP Servers

The proliferation of these projects demonstrates strong community interest and the clear potential of this technology:

* [open-telemetry/weaver](https://github.com/open-telemetry/weaver): MCP server for the OpenTelemetry Weaver
* [pavolloffay/opentelemetry-mcp-server](https://github.com/pavolloffay/opentelemetry-mcp-server): Focuses on collector configuration.
* [austinlparker/otel-mcp](https://github.com/austinlparker/otel-mcp): Handles collector configuration and data profiling.
* [mottibec/otelcol-mcp](https://github.com/mottibec/otelcol-mcp): Focuses on collector configuration.
* [shiftyp/otel-mcp-server](https://github.com/shiftyp/otel-mcp-server): Provides data profiling, but requires OpenSearch.
* [liatrio-labs/otel-instrumentation-mcp](https://github.com/liatrio-labs/otel-instrumentation-mcp): Manages instrumentation.
* [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server): Provides data profiling by connecting to Jaeger, Tempo and Traceloop.

Each of these servers uses a different approach, particularly for collector configuration and data profiling.
This fragmentation creates confusion for users regarding installation and configuration. Furthermore, using multiple competing tools is inefficient as they consume the context window with overlapping functionality.

### Current challenges

Adopting OpenTelemetry presents several significant challenges. Many users lack deep observability expertise, and enabling it is often treated as an afterthought.

The sheer size and velocity of the OpenTelemetry ecosystem add to this difficulty. The project encompasses instrumentation for over 12 languages and includes diverse components like the Collector, OpAMP, and Weaver. Each component is released independently with its own setup requirements and release schedule. For example, the Collector is released bi-weekly, while auto-instrumentation libraries follow different schedules.

Maintenance is also complex. The ecosystem evolves rapidly, introducing frequent breaking changes. Our analysis of the Collector changelogs indicates that approximately 29% of changes are breaking. Keeping up with these updates requires significant manual effort to review release notes, update configuration files, and modify code.

## Project Scope and Architecture

The scope of this project is to enable **Agentic Workflows** to simplify deployment, configuration, and day-2 operations for the OpenTelemetry collector.
Additional components (e.g., SDKs, instrumentation, semantic conventions) could be added in phased approach in the future.

To support this workflow, a standardized interface is required for Agents and LLMs to interact with the OpenTelemetry ecosystem. The project will focus on [The Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and [Agent Skills](https://agentskills.io/home) concepts to provide this interface for agents to interact with the OpenTelemetry project.

The goal of this project is to deliver an initial implementation of MCP server(s) and/or Agent Skills for the OpenTelemetry collector in coordination with the collector SIG.

### Goals, objectives, and requirements

#### Collector

The Collector follows a fast two-week release cadence, which requires constant maintenance to stay up to date and avoid breaking changes. Additionally configuring the collector correctly and writing valid OTTL statements is important for effective usage, but requires domain expertise and isn't always trivial. General-purpose coding agents struggle here because they lack up-to-date knowledge of recent releases and aren't specialized for Collector workflows.

* Enable agents to read and write valid Collector configuration.
* Enable agents to handle API breaking changes (e.g. deprecations, removals, renaming) in the configuration and collector Golang API.
* Enable agents to upgrade collector.
* Enable agents to write valid OpenTelemetry Transformation Language (OTTL).
* Enable agents to troubleshoot collector issues.

The mentioned goals might require enhancements in the collector repositories. We expect to make improvements in the documentation as it is the primary source for building skills and knowledge base for the agents.
Another example is improvements in the collector configuration schema which is already being worked on in the collector SIG.

#### Documentation and distribution

Coherent documentation and distribution of the agentic workflows are required to enable users install and manage the agentic workflows.

* Introduce documentation for the Agentic Workflows.
* Align distribution and installation of the components with the Agentic Workflows.
* Agentic workflow documentation will be part of the existing [OpenTelemetry documentation](https://opentelemetry.io/docs/) and will not duplicate any existing content.

### Non Goals

* The project will not implement any telemetry backends.
* The project will not maintain a separate documentation knowledge base; it will leverage existing OpenTelemetry documentation.

## Deliverables

The following deliverables can change based on the project progress, community feedback and validation of the agentic workflows.
The deliverables are ordered based on the priority the project team deems them to be.

* MCP server or agentic skill to facilitate deployment, configuration and day-2 operations of the collector.
* MCP server or agentic skill to troubleshoot collector issues.

## Staffing / Help Wanted

This project requires a blend of OpenTelemetry collector, documentation and instrumentation expertise and expertise in building MCP server(s).

### SIG

This effort will be hosted in the existing Collector SIG.

Sponsors for this effort are:

* [@dmitryax](https://github.com/dmitryax) (Splunk)
* [@codeboten](https://github.com/codeboten) (OHoneycomb)

### Required staffing

#### Project Leads(s)

* [@pavolloffay](https://github.com/pavolloffay) (Red Hat)
* [@niwoerner](https://github.com/niwoerner) (OllyGarden)

#### TC Sponsor

Existing Collector SIG TC sponsor.

#### GC Liaison

Existing Collector SIG liaison.

#### Engineers

* [@adrielp](https://github.com/adrielp)
* [@shiftyp](https://github.com/shiftyp)
* [@johannaojeling](https://github.com/johannaojeling)
* [@vitorvasc](https://github.com/vitorvasc)
* [@nr-nfajardo](https://github.com/nr-nfajardo)

#### Other Staffing

### Industry outreach (Optional)

The following users have built OpenTelemetry MCP servers:

* [@austinlparker](https://github.com/austinlparker) - author of [otel-mcp](https://github.com/austinlparker/otel-mcp)
* [@mottibec](https://github.com/mottibec) - author of [otelcol-mcp](https://github.com/mottibec/otelcol-mcp)
* [@shiftyp](https://github.com/shiftyp) - author of [otel-mcp-server](https://github.com/shiftyp/otel-mcp-server)

There will be [OpenTelemetry MCP call for contributors post](https://github.com/open-telemetry/opentelemetry.io/pull/8629) to promote the project.

## Expected Timeline

This timeline assumes project approval and resource allocation as outlined in the staffing section. Until staffing is
confirmed and expected time commitments are known, this timeline is in flux.

## Labels

`agentic-workflow`, `mcp` for all PRs and issues related to this project.

## GitHub Project (Post-Approval)

TBD

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

All communication will be done in the existing Collector SIG.