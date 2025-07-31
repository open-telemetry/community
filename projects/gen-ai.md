# Generative AI Observability

> [!IMPORTANT]
> This project extends LLM Semantic Conventions project

## Description

Generative AI observability is evolving fast. The industry is still learning how to use GenAI products which creates new opportunities and challenges in the observability space. GenAI observability is focused on development time and verbose telemetry. Non-deterministic nature of GenAI creates the need to measure the quality and safety of responses which become part of observability.

There are multiple GenAI-focused observability projects out there such as [Arize Phoenix](https://arize.com/docs/phoenix), [Langfuse](https://langfuse.com/), [LangSmith](https://www.langchain.com/langsmith), [Langtrace](https://langtrace.ai/), [OpenLit](https://github.com/openlit/openlit), [Traceloop](https://www.traceloop.com/docs/introduction) and many others.

Some of these projects are based on OpenTelemetry, others are "inspired by" it, but don't have out-of-the-box integration with OTel.

The scope of GenAI observability includes instrumentations of various GenAI clients, frameworks, response evaluations, as well as model (server-side) instrumentations.

Example Use Cases:

- **Debugging**: Tracing provides causality for multi-step LLM applications allowing to understand the operation flow and root-cause errors.
- **Evaluation**: Prompt/completion events record non-deterministic model responses that can be used for debugging or automated evaluations
  measuring LLM response accuracy and other quality characteristics. In addition to automated analysis, recording user feedback tied to LLM outputs
  can provide insights into the quality of model outputs and how they affect user engagement.
- **AI Safety**: GenAI telemetry, along with specialized evaluators, can help ensure ethical use of LLMs, maintain privacy compliance, detect bias, and safeguard data security.
- **Cost Tracking**: Usage metrics based on model self-reporting capabilities provide insights into operational costs.
- **Performance optimization**: Latency, throughput, and error rate of LLM operations provide traditional performance monitoring layer for
   applications running in production.
- **Incident Response Automation**: Integrating observability data with AI operations platforms can enable automated incident responses,
  such as restarting failing model components or scaling up resources in response to increased demand, without manual intervention.
- **Version Control and Rollback**: Tracking model versions in observability data helps monitor the performance impact of model updates,
  allowing quick rollback to previous versions in case a new release introduces errors or degradations in quality.

### Current challenges

Existing GenAI observability projects are driven independently by individual vendors which don't have a common space to collaborate on common instrumentation libraries.

[OpenLLMetry](https://github.com/traceloop/openllmetry) project was created with the intention [to create space under CNCF](https://github.com/cncf/sandbox/issues/67) and gave a start to OTel [LLM Semantic Convention](https://github.com/open-telemetry/community/pull/1928) project.

GenAI Instrumentation libraries like OpenLLMetry, OpenLIT, LangTrace and other provides general-purpose OTel instrumentations for GenAI clients, frameworks and related components.

By providing GenAI community with the space under OpenTelemetry we will be able to start hosting vendor-agnostic instrumentation libraries (such as WIP one [OpenAI Python](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2759)) and [OpenAI JS](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2402) and eventually we will be able to move instrumentations from current GenAI Observability tools to OTel (or to upstream libraries).

It helps GenAI observability community to

- find solutions for new observability problems such as verbose events or correlation with async response evaluations
- discuss implementation challenges
- coordinate and prioritize common efforts

### Goals, objectives, and requirements

GenAI observability project is a new OTel cross-cutting SIG that intends to provide the GenAI community with a space to evolve and maintain GenAI related instrumentations in a **vendor-agnostic way**.

It includes:

- GenAI Semantic Conventions
- Instrumentations for GenAI client libraries, frameworks, or other components.

The eventual goal is to contribute instrumentation libraries to upstream components. When it's not possible or when libraries need some time to mature,
these libraries will evolve in contrib repositories.

JS contrib provides component-ownership model with high level of [autonomy](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/CONTRIBUTING.md#component-ownership).
We can explore if this can be applied to Python.

> [!NOTE]
> The release cadence of contrib repo needs to support releasing components relatively frequently to
> patch issues and adapt to upstream changes so that GenAI observability vendors could depend on them.

Python contrib repo is going to support [per-package release](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2875) soon.
JS contrib release is automated with Release Please - TBD.

## Deliverables

Immediate term:
- Ship OTel instrumentation libraries for OpenAI (or any other GenAI client) in Python and JS following existing conventions

Middle term:
- Ship OpenTelemetry (or native) instrumentations for popular GenAI client libraries in Python and JS covering chat calls
- Evolve GenAI semantic conventions to cover other popular GenAI operations such as embeddings, image or audio generation

As a result we should have feature parity with the instrumentations of existing GenAI Observability vendors for a set of client
instrumentation libraries that all vendors can depend upon.

Long term:
- Implement instrumentations for GenAI orchestrators and GenAI frameworks for popular libraries in different languages
- Evolve GenAI and other relevant conventions (DB) to cover complex multi-step scenarios such as RAG
- Propose mature instrumentations to upstream libraries/frameworks

## Staffing / Help Wanted

The development will start in the OTel contrib repositories and/or in upstream libraries following ownership model that exist in this repo.

Some of the repositories (such as opentelemetry-js-contrib) provide a lot of autonomy to the [component owners](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/CONTRIBUTING.md#component-ownership).

**Project Leads:**

- @drewby
- @nirga

**Sponsoring Members:**

- @lmolkova
- @tedsuo

**Engineers:**

| Alias | Language | Company/Project | Time commitment |
| ----- | -------- | ----------------|---------------- |
| @adharshctr | JS & Python | IBM | |
| @AmanAgarwal041 | JS & Python | OpenLIT | |
| @alizenhom  | JS & Python | Langtrace | |
| @codefromthecrypt | JS & Python | Elastic | 4 hours/week |
| @drewby  | JS & Python | Microsoft | |
| @galkleinman | JS & Python | Traceloop | |
| @gyliu513 | JS & Python | IBM | |
| @karthikscale3 | JS & Python | Langtrace | |
| @LakshmiSujith | JS & Python | IBM | |
| @lmolkova | Python | Microsoft | 16 hours/week |
| @lzchen | Python | Microsoft | 4 hours/week |
| @madhutadiparthi4ibm | JS & Python | IBM | |
| @NehaGhongade | JS & Python | IBM | |
| @nirga  | JS & Python | Traceloop | |
| @patcher9 | JS & Python | OpenLIT | |
| @trentm | JS | Elastic | |
| @xrmx | Python | Elastic | |

*looking for more contributors*

Other languages are not in the scope (yet).

## Meeting Times

We'll use GenAI Semantic Convention meetings until more suitable time for new participants is determined:

- **Every other week**: Thursday at 10 AM PST
- **Every other week**: Thursday 14:00 UTC+8

### Meeting Links

- Meeting Calendar: [calendar-semconv@opentelemetry.io](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv)
- Meeting Notes: [Google Doc](https://docs.google.com/document/d/1EKIeDgBGXQPGehUigIRLwAUpRGa7-1kXB736EaYuJ2M)

## Discussion

* Slack: [#otel-genai-instrumentation-wg](https://cloud-native.slack.com/archives/C06KR7ARS3X)

## Timeline

- Semantic Conventions for GenAI clients
  - Experimental, covering most important features: Apr 2025
  - Stable conventions: Date TBD
- Official OTel Instrumentation libraries for popular clients in JS and Python:
  - OpenAI instrumentation library shipped: Nov 2024
  - Other popular client instrumentations supported by GenAI observability vendors: Apr 2025

## Labels

- `gen-ai`

## Linked Issues and PRs

- Issue: [Introduce semantic conventions for modern AI (LLMs, vector databases, etc.) #327](https://github.com/open-telemetry/semantic-conventions/issues/327)
- PR: [LLM Semantic Conventions: Initial PR #825](https://github.com/open-telemetry/semantic-conventions/pull/825)
- PR: [Add LLM semantic conventions #639](https://github.com/open-telemetry/semantic-conventions/pull/639) - Closed/Replaced with 825
- PR: [[WIP] Add Initial Support for Instrumenting OpenAI Python Library - Chat Completion Create](https://github.com/open-telemetry/opentelemetry-python-contrib/pull/2759)
- PR: [[WIP] Add Initial Support for Instrumenting OpenAI JS Library - Chat Completion Create](https://github.com/open-telemetry/opentelemetry-js-contrib/pull/2402)

## Project Board

* Project Board: [GenAI Client Semantic Conventions](https://github.com/orgs/open-telemetry/projects/82)

