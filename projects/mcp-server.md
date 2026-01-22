# OpenTelemetry Agentic Workflows

## Background and description

The OpenTelemetry project consists of a large number of components, including collector, SDKs, and instrumentation libraries, which are often configured and managed separately. This distribution of components poses a major operational challenge which is universally recognized by the community [1](https://opentelemetry.io/blog/2025/otel-rocks/), [2](https://www.youtube.com/watch?v=xEu8_Aeo_-o).

Large language models (LLMs) and Agentic Workflows present a significant opportunity to simplify the adoption, implementation, and management of the OpenTelemetry stack. An AI agent could, for example, facilitate configuration changes, resolve deployment issues, or assist and simplify the instrumentation process.

At the moment, the OpenTelemetry project does not have official support for these workflows. This has led to the creation of several independent, open-source projects (MCP servers) to fill the gap.

As AI tooling becomes a standard part of developer workflows. Users, which are looking to extend their agents with tooling optimized for OpenTelemetry, have no easy way to discover what's available in the ecosystem. There's no central place to learn which MCP servers or other tools exist, what capabilities they offer, or where to file issues/requests.

### Existing OpenTelemetry MCP Servers

The proliferation of these projects demonstrates strong community interest and the clear potential of this technology:

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

The scope of this project is to enable **Agentic Workflows** for OpenTelemetry to simplify deployment, configuration, and day-2 operations across the OpenTelemetry project (collectors, SDKs, instrumentation, semantic conventions). To support this workflow, a standardized interface is required for Agents and LLMs to interact with the OpenTelemetry ecosystem. The projet will focus on [The Model Context Protocol (MCP)](https://modelcontextprotocol.io/) and [Agent Skills](https://agentskills.io/home) concepts to provide this interface for agents to interact with the OpenTelemetry projects. 

The goal of this SIG is to deliver reference implementation of MCP server(s) and/or Agent Skills for the OpenTelemetry project in coordination with existing SIGs to ensure coherent behaviour and end user experience. We will establish bi-directional collaboration to ensure implementation ownership is mutually agreed upon, such that each new component has a clear owner/maintainer aligned with best practices of the targeted SIGs.

### Goals, objectives, and requirements

Our goals are categorized by the OpenTelemetry components they integrate with agentic workflows. Since deploying a telemetry pipeline typically involves multiple components (instrumentation, semantic conventions, collector, etc.), agentic workflows must be able to span across them.

The initial focus will be on integrating the following areas:

#### Collector

The Collector follows a fast two-week release cadence, which requires constant maintenance to stay up to date and avoid breaking changes. Additionally configuring the collector correctly and writing valid OTTL statements is important for effective usage, but requires domain expertise and isn't always trivial. General-purpose coding agents struggle here because they lack up-to-date knowledge of recent releases and aren't specialized for Collector workflows.

* Enable agents to read and write valid Collector configuration.
* Enable agents to handle API breaking changes (e.g. deprecations, removals, renaming) in the configuration and collector Golang API.
* Enable agents to upgrade collector.
* Enable agents to write valid OpenTelemetry Transformation Language (OTTL).
* Enable agents to troubleshoot collector issues.

#### Semantic Conventions

The Semantic Convention registry contains a large number of entries. They can be hard to grasp, easy to miss, and sometimes difficult to find. An agent can provide concrete recommendations about which attributes to use and which to avoid, but this requires tooling that condenses the registry into context-optimized pieces to avoid polluting the context window.

* Provide context-optimized querying of the Semantic Conventions registry.
* Enable agents to assist with maintaining codebases to add and update semantic conventions, potentially integrating with [Weaver](https://github.com/open-telemetry/weaver).

#### Instrumentation & SDKs

Instrumentation involves SDK setup, configuration, and code. Each step has its own challenges, and comes with a certain complexity. OpenTelemetry's documentation covers these topics extensively, but isn't an AI agent friendly format to provide those information efficiently. Surfacing the right documentation alongside code analysis can make the instrumentation process easier and assist with producing valid code.

* Enable agents to discover and configure SDK and auto-instrumentation.
* Enable agents to analyze instrumentation quality (detecting broken traces, missing context).
* Enable agents to surface relevant documentation during instrumentation workflows.

#### Documentation and distribution

Coherent documentation and distribution of the agentic workflows are required to enable users to efficiently manage the context window and avoid overlapping functionality.

* Introduce documentation for the Agentic Workflows.
* Align distribution and installation of the components with the Agentic Workflows.
* Agentic worflow documentation will be part of the existing [OpenTelemetry documentation](https://opentelemetry.io/docs/) and will not duplicate any existing content.

### Non Goals

* The project will not implement any telemetry backends.
* The project will not maintain a separate documentation knowledge base; it will leverage existing OpenTelemetry documentation.

## Deliverables

The following deliverables can change based on the project progress, community feedback and validation of the agentic workflows.
The deliverables are ordered based on the priority the project team deems them to be.

### 1. Collector
* MCP server or agentic skill to facilitate deployment, configuration and day-2 operations of the collector.
* MCP server or agentic skill to troubleshoot collector issues.

### 2. Semantic Conventions
* MCP server or agentic skill to query the Semantic Conventions registry.

### 3. Instrumentation & SDKs
* MCP server or agentic skill to discover and configure SDK and auto-instrumentation.
* MCP server or agentic skill to analyze instrumentation quality (detecting broken traces, missing context).

## Staffing / Help Wanted

This project requires a blend of OpenTelemetry collector, documentation and instrumentation expertise and expertise in building MCP server(s).

### SIG

This project will be led by a cross-cutting effort coordinating with the Collector, documentation, and language SIGs. 

This effort will be hosted in the existing Developer Experience SIG.

### Required staffing

#### Project Leads(s)

* [@pavolloffay](https://github.com/pavolloffay) (Red Hat)
* [@niwoerner](https://github.com/niwoerner) (OllyGarden)

#### TC Sponsor

Existing Developer Experience SIG TC sponsor.

#### GC Liaison

Existing SIG Developer Experience liaison - [@austinlparker](https://github.com/austinlparker) (Austin Parker - Honeycomb).

#### Engineers

* [@adrielp](https://github.com/adrielp)
* [@shiftyp](https://github.com/shiftyp)
* [@johannaojeling](https://github.com/johannaojeling)
* [@vitorvasc](https://github.com/vitorvasc)

#### Other Staffing

### Industry outreach (Optional)

The following users have built OpenTelemetry MCP servers:

* [@austinlparker](https://github.com/austinlparker) - author of [otel-mcp](https://github.com/austinlparker/otel-mcp)
* [@mottibec](https://github.com/mottibec) - author of [otelcol-mcp](https://github.com/mottibec/otelcol-mcp)
* [@shiftyp](https://github.com/shiftyp) - author of [otel-mcp-server](https://github.com/shiftyp/otel-mcp-server)

There will be [OpenTelemetry MCP call for contributors post](https://github.com/open-telemetry/opentelemetry.io/pull/8629) which promote the project.

## Expected Timeline

This timeline assumes project approval and resource allocation as outlined in the staffing section. Until staffing is
confirmed and expected time commitments are known, this timeline is in flux.

Phase 1: Collector use-cases
Phase 2: Semantic conventions use-cases
Phase 3: Instrumentation use-cases

## Labels

`agentic-workflow`, `mcp` for all PRs and issues related to this project.

## GitHub Project (Post-Approval)

TBD

## GitHub Repository

* Request: https://github.com/open-telemetry/community/issues/3198

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

[Developer Experience SIG](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-devex)