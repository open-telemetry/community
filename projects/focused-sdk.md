# OpenTelemetry SDK Wrapper

## Background and description

This project started as an investigation to mitigate some issues identified around memory allocations and global interpreter lock (GIL) contention in Python. As a result of testing an implementation that binds [Python to a C++ SDK](https://github.com/open-telemetry/community/issues/3483), a potential reduction in heap allocations by 10-15% and as much as 40% was observed.

The project proposed here provides the performance benefits of an underlying SDK across Python initially and possibly other languages in the future. A secondary benefit, though not a goal, would be to allow end users and API implementers to experiment with features already supported in the underlying SDK, that may not yet be implemented in a native SDK.

### Current challenges

Reference implementation SDKs in every language offer the flexibility that includes every feature supported by OpenTelemetry. In some implementations, this comes at the cost of:

* increased resource consumption (memory usage, artifact size)
* added complexity

* in Python specifically, the contention with the global interpreter lock which may cause instrumented applications to introduce latency into the application

This impacts end users by increasing the overhead required to use OpenTelemetry out of the box.

### Goals, objectives, and requirements

The OTel community is currently working across many languages to support reference implementations of all the features in every language. We have always proposed that the API/SDK separation would make it possible for end-users to swap SDKs without having to re-instrument their application/instrumentations code. The proposal for this project is to leverage that model as well as existing OpenTelemetry component to provide alternative SDKs for specific use-cases.

An objective is to prove this approach as part of the project. A requirement of the project is that the performance improvements be worth the investment of time to produce and maintain artifacts moving forward. If the investigations from the project finds that the performance improvements are only applicable to one language or the improvements are negligible, then the deliverables may be changed.

A non-goal of this project is to replace existing SDK implementations. There are always different use-cases for end users and a native implementation that offers flexibility is likely to always be needed.

## Deliverables

There are a few different approaches available to solve the issue. Phase 1 of the project will provide:

* a library or artifact that can be used behind an existing language API. The initial proposal is to support at least Python, but support for other languages is not out of scope.
* benchmarks to compare the existing native SDK with the proposed alternative artifact
* documentation of the opinions and limitations of what this artifact supports, including decisions made to not support certain protocols or features of the native SDK


## Staffing / Help Wanted

### Industry outreach (Optional)

The following vendors are interested in improving this area:

* Dash0 (@ocelotl)
* Grafana Labs (@codeboten)
* Honeycomb (@MikeGoldsmith)

### SIG

New SIG needed with a new name

### Required staffing

#### Project Leads(s)

* Alex Boten (@codeboten)
* Diego Hurtado (@ocelotl)

#### Other Staffing

Engagement with the backing SDK is expected, level of involvement TBD.

### Sponsorship
See [Project Sponsorship](/project-management.md#project-sponsorship)

#### TC Sponsor

Alex Boten (@codeboten)
Reiley Yang (@reyang)

#### GC Liaison

TODO

## Expected Timeline

* Months 1-3: investigate various approaches to solving the problem and produce benchmarks for each comparing the performance in Python, Ruby, and Node
* Months 4-12: produce artifacts capable of providing users with alternative implementations

## Labels (Optional)

TODO

## GitHub Project (Post-Approval)

TODO: add project link

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

TODO: add details here
