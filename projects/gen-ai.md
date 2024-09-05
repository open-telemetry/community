# Generative AI Observability

>[!IMPORTANT] This project extends LLM Semantic Conventions project

## Description

Generative AI observability is evolving fast. The industry is still learning how to use GenAI products which creates new opportunities and challenges in the observability space. GenAI observability is focused on development time and verbose telemetry. Non-deterministic nature of GenAI creates the need to measure the quality and safety of responses which become part of observability.

There are multiple GenAI-focused observability projects out there such as [Arize Phoenix](https://docs.arize.com/phoenix), [Langfuse](https://langfuse.com/), [LangSmith](https://www.langchain.com/langsmith), [Langtrace](https://langtrace.ai/), [OpenLit](https://github.com/openlit/openlit), [Traceloop](https://www.traceloop.com/docs/introduction) and many others.

Some of these projects are based on OpenTelemetry, others are "inspired by" it, but don't have out-of-the-box integration with OTel.

The scope of GenAI observability includes instrumentations of various GenAI clients, frameworks, response evaluations, as well as model (server-side) instrumentations.

Example Use Cases:

- **Debugging**: Standardizing log data and error reporting for efficient error resolution in LLM applications.
- **Evaluation**: Collecting signal for evaluation of LLM performance, including response accuracy, context retention, and user feedback.
- **Cost Tracking**: Monitoring operational costs like computation time and API calls for resource optimization.
- **AI Safety**: Monitoring for ethical LLM use, including privacy compliance, bias detection, and secure data handling.

For Spans: Instrumentation and debugging guidance for multi-step LLM applications, with recommendations on user privacy and intellectual property security, marking sensitive attributes and events as opt-in.
For Metrics: Tracking model performance by collecting and correlating data like model names, versions, parameters, latency, and evaluation scores.

### Current challenges

Existing GenAI observability projects are driven independently by individual vendors which don't have a common space to collaborate on common instrumentation libraries.

[OpenLLMetry](https://github.com/traceloop/openllmetry) project was created with the intention [to create space under CNCF](https://github.com/cncf/sandbox/issues/67) and gave a start to OTel [LLM Semantic Convention](https://github.com/open-telemetry/community/blob/main/projects/llm-semconv.md) project.

OpenLLMetry provides general-purpose OTel instrumentations for GenAI clients, frameworks and related components; they are governed by [Traceloop](https://www.traceloop.com/docs/introduction).

By providing GenAI community with the space under OpenTelemetry we will be able to start hosting vendor-agnostic instrumentation libraries (such as WIP one [OpenAI Python](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2759)) and eventually we will be able to move popular OpenLLMetry-owned `opentelemetry-instrumentation-*` libraries to OTel (or to upstream libraries).

It helps GenAI observability community to

- find solutions for new observability problems such as verbose events or correlation with async response evaluations
- discuss implementation challenges
- coordinate and prioritize common efforts

### Goals, objectives, and requirements

GenAI observability project is a new OTel cross-cutting SIG that intends to provide the GenAI community with a space to evolve and maintain GenAI related instrumentations in a **vendor-agnostic way**.

It includes:

- LLM Semantic Conventions
- Instrumentations for GenAI client libraries, frameworks, or other components.

The eventual goal is to contribute instrumentation libraries to upstream components or to otel-contrib repos when upstream contributions are not possible.

During initial development and experimentation, we may need to release libraries more frequently than it's possible for contrib and then may temporarily host instrumentation libraries in a `opentelemetry-{language}-genai` repository(ies).

This would help GenAI observability vendors that will depend on these libraries to patch issues and adapt to external changes.

## Deliverables

- develop common instrumentation libraries for popular GenAI clients and frameworks
- suggest and, when possible, contribute them to upstream libraries
- define and evolve GenAI Semantic Conventions
- propose and implement changes in the OTel API/SDK/contrib/etc that are necessary for GenAI efforts

## Staffing / Help Wanted

The initial set of approvers for each language must include:

- representatives of at least 2 different observability vendors that are active members of OTel LLM SemConv WG
- at least one existing approver or maintainer of the contrib, instrumentation or core OTel repo in the corresponding language

**Project Leads:**

- @drewby
- @nirga

**Sponsoring Members:**

- @lmolkova
- TBD

**Engineers:**
- Python
  - maintainers/approvers:
    - @drewby
    - @karthikscale3
    - @lzchen
    - @nirga
    - @xrmx 
  - contributors:
    - @alizenhom
    - @lmolkova
    - *looking for more contributors*
- JS
  - maintainers/approvers:
    - @drewby
    - @karthikscale3
    - @nirga
    - *looking for existing OTel JS approvers/maintainers for general JS & OTel feedback*
  - contributors:
    - @alizenhom
    - *looking for more contributors*
- Other languages: not in the scope (yet).

## Meeting Times

Alternating weekly meetings to accommodate different time zones:

- Week 1: Wednesdays at 10 AM PST
- Week 2: Wednesdays at 11 PM PST

(will likely add more slots depending on the demand)

### Meeting Links

- Meeting Calendar: [calendar-semconv@opentelemetry.io](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv)
- Meeting Notes: [Google Doc](https://docs.google.com/document/d/1EKIeDgBGXQPGehUigIRLwAUpRGa7-1kXB736EaYuJ2M)

## Discussion

* Slack: [#otel-llm-semconv-wg](https://cloud-native.slack.com/archives/C06KR7ARS3X)
(TODO: rename to `#otel-gen-ai-wg`)

## Timeline

- Semantic Conventions for GenAI clients
  - Experimental, covering most important features: Apr 2025
  - Stable conventions: Date TBD
- Official OTel Instrumentation libraries for popular clients in JS and Python:
  - OpenAI instrumentation library shipped: Nov 2024
  - Other popular client instrumentations supported by OpenLLMetry: Apr 2025

## Labels

- `gen-ai`

## Linked Issues and PRs

- Issue: [Introduce semantic conventions for modern AI (LLMs, vector databases, etc.) #327](https://github.com/open-telemetry/semantic-conventions/issues/327)
- PR: [LLM Semantic Conventions: Initial PR #825](https://github.com/open-telemetry/semantic-conventions/pull/825)
- PR: [Add LLM semantic conventions #639](https://github.com/open-telemetry/semantic-conventions/pull/639) - Closed/Replaced with 825
- PR: [[WIP] Add Initial Support for Instrumenting OpenAI Python Library - Chat Completion Create](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2759)
## Project Board

* Project Board: [LLM Client Semantic Conventions](https://github.com/orgs/open-telemetry/projects/82)
(TODO: rename to `GenAI Client Instrumentation`)