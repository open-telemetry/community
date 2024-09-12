# React Native SIG

## Background and description

As OpenTelemetry continues to mature around client-side instrumentation React Native poses a unique challenge. While the
existing JS packages are sufficient for most web development in React, React Native developers often cannot use them as
they are built to assume either a server-side Node environment or a client-side Browser environment. In addition, while
the JS layer provides a useful abstraction there are often situations where the underlying mobile devices must be taken
into account to provide a complete observability picture.

This proposal seeks to form a special interest group with expertise across mobile and JS development to address these
challenges and make it easier for React Native developers to instrument their applications.

### Current challenges

- React Native developers do not have working OpenTelemetry instrumentation examples for mobile apps.
  - For example the [OpenTelemetry Demo](https://github.com/open-telemetry/opentelemetry-demo) does not currently 
include a mobile app
- The existing OTel Javascript packages can be used for React Native, but require workarounds that are subject to change
  with minor version updates.
  - For example the Performance API is used in the opentelemetry-sdk-trace-web package as well as
opentelemetry-instrumentation-fetch. This API has broad support across modern browsers, so it makes sense for the web
packages to rely on it, however it is not implemented in React Native environments so developers there either need to
polyfill it or carefully use the web packages in such a way that calls to this API are avoided. A small change to any
web packages that used this API in a new spot could be breaking for instrumented RN apps.
- The OTel Javascript packages leave gaps for telemetry coming from mobile devices, which React Native developers wish
to capture.
  - For example the OpenTelemetry Android SDK provides ANR detection as a feature. It would be useful for a React Native
developer to be able to gather this telemetry from the native layer and be able to connect it with a particular operation
or view rendered on the JS layer to uncover performance issues.

### Goals, objectives, and requirements

The goal of this project is to establish a SIG that will build on the existing OTel Javascript packages to provide
instrumentation for app developers that build in React Native. As OpenTelemetry grows to capture telemetry from new
systems and types of applications, it should provide tooling for these types of hybrid mobile applications that are
not directly built in the Android and iOS ecosystems.

React Native presents a unique scenario for OpenTelemetry: a seemingly-familiar ecosystem, written in Javascript, with
tooling that might not be appropriate for the core OTel JavaScript packages. A separate SIG could decide the proper way to
build on top of the Javascript repos to provide mobile-specific instrumentation.

## Deliverables

- Add a React Native example application to the opentelemetry-demo repo (to evolve as further deliverables are completed)
- A strategy for re-using packages from the JS repos in a RN environment
  - an implementation of this strategy for the existing JS tracer provider and fetch/xhr instrumentations
- React-friendly wrappers over the existing OpenTelemetry JS API (using hooks, components, etc.)
- JS Wrappers over the OpenTelemetry Android and Swift SDKs to allow them to be used in a RN app as Native Modules
- A resource detector to automatically pull mobile client information for RN apps
- Instrumentation libraries for popular React Native frameworks (Redux, React Navigation)

## Staffing

GC/TC sponsors:

TBD

Maintainers, approvers, and contributors:

- @facostaembrace
- @jpmunz
- ...
- TBD

## Timeline

- One month in
  - SIG established
  - React Native demo added showing the current state of tooling available
  - Remaining deliverables prioritized
- Six months in
  - React Native tooling released to aid instrumentation on both the JS and native mobile sides
  - Automatic instrumentations for popular React Native frameworks stabilized
  - Demo app updated showing a simple setup of instrumentation free of workarounds
- Beyond
  - Feedback gathered from React Native developers on initial deliverables
  - Longer term roadmap established to continue to serve the React Native community

## Project Board

TBD

## SIG Meetings and Other Info

TBD
