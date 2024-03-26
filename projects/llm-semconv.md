# LLM Observability Semantic Conventions

## Description

This workgroup aims to identify and define a standardized vocabulary and specification for observability of Large Language Model (LLM) based applications. The effort would explore various LLM-based application APIs, LLM tasks and LLM workflows for multistage reasoning. Key areas include:

- Evaluating existing vendor-specific conventions (which may not be currently standardized but implementation specific)
- Developing a standardized vocabulary for observability specific semantic conventions for single stage and multistage LLM workflows
- Initial scope focused on metrics and traces (which could later be expanded to other telemetry data signals)

Example Use Cases:

- **Debugging**: Standardizing log data and error reporting for efficient error resolution in LLM applications.
- **Evaluation**: Collecting signal for evaluation of LLM performance, including response accuracy, context retention, and user feedback.
- **Cost Tracking**: Monitoring operational costs like computation time and API calls for resource optimization.
- **AI Safety**: Monitoring for ethical LLM use, including privacy compliance, bias detection, and secure data handling.

For Spans: Instrumentation and debugging guidance for multi-step LLM applications, with recommendations on user privacy and intellectual property security, marking sensitive attributes and events as opt-in.

For Metrics: Tracking model performance by collecting and correlating data like model names, versions, parameters, latency, and evaluation scores.

## Deliverables

- Semantic conventions for LLMs, allowing flexibility for evolution in this fast-paced field.
- Reference prototypes demonstrating the application of these conventions in data collection, processing, and analysis.
- Recommended practices for monitoring LLM applications, including implementation strategies.

## Staffing / Help Wanted

We will gather further staff as the project is established. We need to 
make sure there is enough representation across both vendors and customers
who will benefit from these semantic conventions.

**Project Leads:**

- @drewby
- @nirga

**Sponsoring Members:**

- @lmolkova
- @alolita

**Engineers:**

- @nirga
- @sudivate
- @cartermp
- @gyliu513
- *Positions open for more engineers*

**Maintainers:**

- To be determined

## Meeting Times

Alternating weekly meetings to accommodate different time zones:

- Week 1: Wednesdays at 8 AM PST
- Week 2: Wednesdays at 4 PM PST

### Meeting Links

- Meeting Calendar: [calendar-semconv@opentelemetry.io](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv)
- Meeting Notes: [Google Doc](https://docs.google.com/document/d/1EKIeDgBGXQPGehUigIRLwAUpRGa7-1kXB736EaYuJ2M)

## Discussion 

* Slack: [#otel-llm-semconv-wg](https://cloud-native.slack.com/archives/C06KR7ARS3X)

## Timeline

1. Initial Draft: February 2024
1. Review and Refinement: April 2024
1. Prototypes for .NET, Python, JS: June 2024 
1. Initial Merge Target: July 2024
1. Ongoing Review for Stability: Date TBD

## Labels

- `LLM`

## Linked Issues and PRs

- Issue: [Introduce semantic conventions for modern AI (LLMs, vector databases, etc.) #327](https://github.com/open-telemetry/semantic-conventions/issues/327)
- PR: [LLM Semantic Conventions: Initial PR #825](https://github.com/open-telemetry/semantic-conventions/pull/825)
- PR: [Add LLM semantic conventions #639](https://github.com/open-telemetry/semantic-conventions/pull/639) - Closed/Replaced with 825

## Project Board

* Project Board: [LLM Client Semantic Conventions](https://github.com/orgs/open-telemetry/projects/82)
