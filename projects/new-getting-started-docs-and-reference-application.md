# New Getting Started Documentation and Reference Application

## Background and description

This project aims to deliver a new learning experience on [opentelemetry.io](https://opentelemetry.io) for OpenTelemetry end users, combined with a "reference application" that serves as both the foundation of this experience and a demonstration tool for SIGs to showcase feature implementations.

This proposal is a continuation of the following existing discussions and documents:

- [Restructure Language SDK & API documentation information architecture](https://github.com/open-telemetry/opentelemetry.io/discussions/4853)
- [Nice to have: a tutorials section on opentelemetry.io where folks can easily access tutorials](https://github.com/open-telemetry/opentelemetry.io/discussions/4475)
- [Visualizations we support in the documentation](https://github.com/open-telemetry/opentelemetry.io/discussions/5040), following up on a conversation with .NET SIG in
  [this issue](https://github.com/open-telemetry/opentelemetry-dotnet/pull/5779).
- [Learn OpenTelemetry: New Getting Started & Best Practices](https://github.com/open-telemetry/opentelemetry.io/pull/5376)

### Current challenges

Currently, almost all languages have a "getting started" documentation on <https://opentelemetry.io/docs>. However, end users frequently report a lack of a robust, complete reference implementation that demonstrates OpenTelemetry concepts in their chosen programming language. The "getting started" guides typically focus on a quick setup experience—often using zero-code solutions like the Java Agent—and many subsequent pages lack the in-depth information needed to address specific issues that users encounter.

In recent years, we in SIG Comms have aimed to simplify the documentation by standardizing it across languages. While this has improved consistency, it has not fully resolved user challenges. A primary issue is that our current documentation combines best practices guides with technical references. For example, the documentation for "manual instrumentation" attempts to cover all available methods for setting up the SDK, performing tracing, capturing metrics, logging, etc., using the same sample application. Similarly, the pages on exporters list standard exporters—such as Console, OTLP, Prometheus, and ZipKin—and include Docker setup instructions. This overloads end users looking for a point to get started and also does not serve advanced users that want to dive into more technical details and solve specific
problems.

Following [this discussion](https://github.com/open-telemetry/opentelemetry.io/discussions/4853), the [Java Documentation](https://opentelemetry.io/docs/languages/java/) was updated to focus on technical reference material. This revision better aligns it with the structure of the Specification, separating API usage ("Record Telemetry with the API") from SDK management ("Manage Telemetry with the SDK") instead of mixing multiple concepts together.

While we plan to apply these documentation changes across other languages, this proposal focuses on developing "best practices guides". These guides will provide an end-to-end learning journey for users, allowing them to grasp key concepts without delving into extensive details. For instance, we could focus on a single method for setting up the SDK, one approach to capturing traces, and using console and OTLP exporters, rather than covering all possible options in one place.

By offering a structured learning path, as outlined in this document, we aim to meet end users' need for a comprehensive reference implementation while also equipping maintainers with a tool to demonstrate feature implementations in their specific language.

### Goals, objectives, and requirements

The improved "getting started" experience for OpenTelemetry end users will consist of two parts:

- A reference application available in all major languages
- A language agnostic test suite for spec validation (like [W3C Distributed Tracing Validation Service](https://github.com/w3c/trace-context/tree/main/test))
- A guide that leads users through the process of instrumenting this reference application

While members of SIG Comms can create the guide, the reference application will require collaboration across SIGs. This need for cross-SIG collaboration is a key reason behind this project proposal.

The first step is to create a "specification" for this application. This involves defining the type of application we will use and how it should function. An example can be found in the [newrelic-opentelemetry-examples](https://github.com/newrelic/newrelic-opentelemetry-examples) repository, specifically in the [demo-app-specification.md](https://github.com/newrelic/newrelic-opentelemetry-examples/blob/main/getting-started-guides/demo-app-specification.md):

```markdown
# Specification for the Getting Started Guide demo applications

## Application

1. Must use port 8080

2. User must be able to access the endpoint http://localhost:8080/fibonacci?n=[input], and endpoint should return the following JSON response:

- For valid input, `{"n":5,"result":5}`
- For invalid input, `{"message":"n must be 1 <= n <= 90."}`
```

This specification will outline an application that demonstrates a wide range of OpenTelemetry features. Unlike the [Demo](https://github.com/open-telemetry/opentelemetry-demo/), this will be a single, straightforward application implemented in all supported languages, with simple business logic (e.g., Fibonacci calculations or a "roll the dice" feature).

In the second step, this specification should be expanded to include instructions for the "Instrumentation Journey." This will outline the abstract, language-agnostic steps an end user will follow to integrate the OpenTelemetry SDK into the application, add instrumentation, export telemetry, and more.

Once the specification is available, each SIG that implements the API and SDK in their respective language can provide the application in both uninstrumented and instrumented forms as examples in their repository.

Once at least one SIG provides this application, the documentation can be updated to include the new learning experience, utilizing this application. We will leverage existing tools to [extract code excerpts](https://github.com/open-telemetry/opentelemetry.io/tree/main/tools) from external repositories and import the code directly into the website.

## Deliverables

- A specification for the reference application
- Implementations of the reference application across all supported languages
- Prose detailing the new learning experience on the OpenTelemetry website

## Staffing / Help Wanted

This project is a collaboration between SIG Communications (Docs Contributors) and the SIGs responsible for implementing the API and SDK in their respective languages. No new SIGs need to be formed; however, we do need individuals to sign up and support this effort:

- Staffing from SIG Communications
  - [@svrnm](https://github.com/svrnm) (Project Lead)

- Staffing from SIG Java
  - [@jack-berg](https://github.com/jack-berg)
  - [@lof000](https://github.com/lof000)

- Staffing from SIG Ruby
  - [@kaylareopelle](https://github.com/kaylareopelle)

- Staffing from `Language SIG 3`
  - `tbd`

- GC/TC Sponsors
  - [@svrnm](https://github.com/svrnm)
  - [@jack-berg](https://github.com/jack-berg)

## Timeline

The timeline is provided in "quarters," referring to the quarters after the project is approved.

- Q1: Deliver the specification for the reference application
- Q2: Provide a first implementation of the reference application
- Q3: Provide the tutorial on [opentelemetry.io](https://opentelemetry.io)

## Resources

Existing solutions, that can be used as a basis for the reference application:

- The existing `rolldice` app in the Getting Started guides at <https://opentelemetry.io>
- [newrelic-opentelemetry-examples](https://github.com/newrelic/newrelic-opentelemetry-examples)
- [OpenTelemetry instrumentation workshops](https://github.com/honeycombio/workshop-advanced-instrumentation) by Honeycomb

## Project Board

to be created

## SIG Meetings and Other Info

to be done
