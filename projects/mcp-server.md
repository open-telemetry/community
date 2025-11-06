# OpenTelemetry Collector Model Context Protocol (MCP) Server

## Background and description

The OpenTelemetry project consists of a large number of components, including collector, SDKs, and instrumentation libraries, which are often configured and managed separately. This distribution of components poses a major operational challenge which is universally recognized by the community [1], [2].

Large language models (LLMs), present a significant opportunity to simplify the adoption, implementation, and management of the OpenTelemetry stack. An AI agent could, for example, analyze telemetry data, facilitate configuration changes, or assist and simplify the instrumentation process.

However, to support this process, a standardized interface is required for LLMs to interact with the OpenTelemetry ecosystem. The Model Context Protocol (MCP) provides an idiomatic approach for this interaction.

At the moment, the OpenTelemetry project does not have an official, standard MCP server. This has led to the creation of several independent, open-source projects to fill the gap.

### Existing OpenTelemetry MCP Servers

The proliferation of these projects demonstrates strong community interest and the clear potential of this technology:

* [pavolloffay/opentelemetry-mcp-server](https://github.com/pavolloffay/opentelemetry-mcp-server): Focuses on collector configuration.
* [austinlparker/otel-mcp](https://github.com/austinlparker/otel-mcp): Handles collector configuration and data profiling.
* [mottibec/otelcol-mcp](https://github.com/mottibec/otelcol-mcp): Focuses on collector configuration.
* [shiftyp/otel-mcp-server](https://github.com/shiftyp/otel-mcp-server): Provides data profiling, but requires OpenSearch.
* [liatrio-labs/otel-instrumentation-mcp](https://github.com/liatrio-labs/otel-instrumentation-mcp): Manages instrumentation.
* [traceloop/opentelemetry-mcp-server](https://github.com/traceloop/opentelemetry-mcp-server): Provides data profiling by connecting to Jaeger, Tempo and Traceloop.

Each of these servers uses a different approach, particularly for collector configuration and data profiling.
This fragmentation creates confusion for users in terms of installation and configuration. It is less effective
as multiple competing tools fill up context window and provide overlapping functionality.

### Project Scope and Architecture

The scope of this project is to create OpenTelemetry MCP server(s) to simplify deployment and day-2 operations.
The MCP server should also provide data profiling/intelligence capabilities to support the day-2 operation use-cases.

### Goals, objectives, and requirements

The goals are divided into categories. However, some common goals apply to all created MCP(s):

* A common installation and configuration

#### Collector

* Deployment, configuration and management
* Simplify writing OpenTelemetry Transformation Language (OTTL)
* Simplify writing PII rules based on the received data

#### Instrumentation

* SDK configuration
* Auto-instrumentation configuration
* Identify instrumentation issues: single span traces, broken traces, high cardinality attributes

#### Semantic conventions

* Weaver schema generation
* Context optimized querying of the official semantic conventions registry

## Deliverables

* Collector MCP server
  * Configuration use-cases
  * Data profiling use-cases: writing PII rules, high cardinality attributes, broken traces, single span traces
* Standalone MCP Server
  * Instrumentation use-cases
  * Collector provisioning and configuration use-cases
  * Understanding changes in released artifacts

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

Not needed.

#### GC Liaison
 
* [@austinlparker](https://github.com/austinlparker) (Austin Parker - Honeycomb) - existing SIG developer experience liaison.

#### Engineers

* [@adrielp](https://github.com/adrielp)
* [@shiftyp](https://github.com/shiftyp)

#### Other Staffing

### Industry outreach (Optional)

The following users have built OpenTelemetry MCP servers:

* [otel-mcp](https://github.com/austinlparker) - author of [otel-mcp](https://github.com/austinlparker/otel-mcp)
* [mottibec](https://github.com/mottibec) - author of [otelcol-mcp](https://github.com/mottibec/otelcol-mcp)
* [shiftyp](https://github.com/shiftyp) - author of [otel-mcp-server](https://github.com/shiftyp/otel-mcp-server)

There will be [OpenTelemetry MCP blog post](https://github.com/open-telemetry/opentelemetry.io/pull/8331/) which promote the SIG.

## Expected Timeline

This timeline assumes project approval and resource allocation as outlined in the staffing section. Until staffing is
confirmed and expected time commitments are known, this timeline is in flux.

Phase 1: Static collector configuration (Months 1-2)
- OpenTelemetry collector configuration

Phase 2: Data profiling via collector (Months 1-2)
- OpenTelemetry collector extension which provides API to query and profile the processed telemetry data
- Data volume attribution

Phase 3: Instrumentation (Months 1-2)
- Identify broken traces
- Identify single span traces
- Identify high cardinality traces
- Instrumentation configuration

## Labels

`mcp` for all PRs and issues related to this project.

## GitHub Project (Post-Approval)

TBD

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

[Developer Experience SIG](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-devex)