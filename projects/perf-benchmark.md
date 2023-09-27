### Description

As the adoption of OpenTelemetry grows and larger enterprises continue to deepen
their usage of project components there are persistent and ongoing end user
questions about the OpenTelemetry performance impact. End user performance
varies due to the quirks of their environment but without a project performance
standard and historical data record no one really knows if the numbers they're
seeing are abnormal or expected. Additionally, there is no comprehensive
documentation available on tuning project components or the performance
trade-offs available to users which results in a reliance on vendor support.

The project needs to be able to track the current state of our
components while preventing any performance regressions when making new
releases. Customers need to be able to get a general sense of potential
OpenTelemetry performance impact and the certainty that OpenTelemetry takes
performance and customer resources seriously. Performance tracking and
quantification is a general need that should be addressed by a project wide
effort and automated tooling that minimizes repo owner effort while providing
valuable new data points for all project stakeholders.  

### Project Board

### SIG Charter

[charter](https://docs.google.com/document/d/1W0hLqHrUNtS2yclORTNtFZ-lXDblMzUYrp1PCSyzJr8/edit?usp=sharing)

### Deliverables

This is intended to be an iterative process.

* Develop automated tooling that can be used across project repos to report
  current performance numbers and track changes as new features / PRs are
  merged.
* Basic implementation of the existing specification and repo specific desired
  tests in the Collector and 3 language repos.
* Provide ongoing maintenance as needed on automated tooling and own the
  underlying assets

Initial implementation scope would be the core Collector components (main repo),
JavaScript / Java / Python SDKs and their core components. No contrib or
instrumentation.

### Staffing / Help Wanted

Anyone with an opinion on performance standards and testing.

Language contributors as the SIG will be tasked with implementing the changes
and following through on the process. Maintainers or approvers can optionally
participate or consult the SIG on how to use the provided tooling.

#### Required staffing

lead - tbd @jpkrohling domain expert
@cartersocha contributor
@mwear collector sig
@codeboten collector sig implementation
@ocelotl python sig
@martinkuba javascript sig
@tylerbenson java sig
@brettmc php sig

@jpkrohling - GC sponsor
@alolita  - GC sponsor

Need: more performance domain experts, language implementers

### Meeting Times

TBD

### Timeline

Initial scope is for the Collector and 3 SDKs. Output should be by KubeCon NA
November 6, 2023

### Labels

tbd

### Linked Issues and PRs

<https://opentelemetry.io/docs/collector/benchmarks/>
<https://github.com/cncf/cluster/issues/245>
<https://github.com/cncf/cluster/issues/182>
<https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/performance-benchmark.md>
<https://opentelemetry.io/docs/specs/otel/performance-benchmark/>
