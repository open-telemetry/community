# Feature Flag Semantic Conventions

OpenFeature is a CNCF Incubating project aiming to standardize feature flags.
They currently provide 11 open source SDKs in various languages and support more than 10 feature flagging backends.
OpenFeature has had contributions from over 50 companies and is actively developed by a combination of end users, feature flagging vendors, and platform providers.

OpenFeature provides observability data via OpenTelemetry hooks.
A hook is an OpenFeature plugin which may execute logic at various stages of the feature flag evaluation process.
Currently, those hooks use the experimental feature flagging semantic convention.

OpenFeature is looking to expand their observability solution either by improving the currently available hooks or by providing native instrumentation within the OpenFeature SDK itself.
In order to support that effort, OpenFeature requires a stable semantic convention to build instrumentation around.
This project aims to develop and stabilize feature flag semantic conventions, using the existing experimental semantic conventions as a starting point.

## Problem 1: Determining Flag Impact

Currently, it is impossible to determine the impact a feature flag has on key metrics for your services.
For example, if a feature flag is enabled for 25% of users, additional data is required to know if that subset of users is experiencing faster, slower, or unchanged response times.
This problem can become exponentially more challenging if multiple feature flags are evaluated over the course of a single transaction.

Further, it may also be difficult or impossible to know exactly how many users are being affected by a particular feature flag.
For example, if a feature flag targets users with a particular email domain, it may require additional monitoring data to determine what portion of your users or traffic is receiving a particular experience.

## Problem 2: Flag management separate from monitoring data

Feature flags are typically managed outside your monitoring tooling.
There is no standardized way for a flag management system to notify a monitoring system that a feature flag ruleset is changed, or if a rule is enabled or disabled.
This lack of standardization means that even if a flag management system emits a flag change event, the monitoring tool may not be able to correlate that change with the services that it impacts.
It also means that a person responsible for monitoring an application often has to check two separate tools in order to determine if a flag change was the root cause of a change in service metrics or behavior.
Because rulesets and monitoring data are managed in separate tools, it may be difficult to determine exactly which ruleset was used and if it has been changed between when it was evaluated and when a person investigating an issue is looking at the monitoring data.

## Target Use Cases

- Analyze the impact a feature flag has on key service metrics such as response time and failure rate.
  If a feature variant is enabled for some subset of users, it is necessary to be able to distinguish those transactions from other transactions in your monitoring backend.
- Associating a flag change with a change in key service metrics.
  This is useful additional context during root cause analysis.
  One example of when this is useful may be determining the ruleset that was evaluated in order to determine the flag variant.
- Determine how many users are experiencing a particular flag variant.
  In many feature flagging services it is possible to target a flag variant by some attribute of context such as the user’s email domain, however it may be difficult or impossible to know what percentage of your traffic falls into the cohort.
- Determining why a particular flag evaluation returned the variant that it did.
  For example, a ruleset may depend on contextual info such as the currently logged in user, their user-agent, or their geographic location in order to determine the flag variant.
- Identify which services are evaluating a specific feature flag.
  This is useful for the process of removing flags from your code and feature flagging service, an important part of the flag lifecycle.
- Analyzing the impact of the actual flag evaluation.
  Some feature flag libraries and services do async work such as database or remote calls to decide which variant of a feature flag should be returned.

## Deliverables

The project deliverable will be a stable feature flag semantic convention for flag evaluations, also called impressions, and feature flag changes.
Both client and server uses should be considered, and prototypes should be created for at least one server and at least one client use case.

While prototypes will be delivered as a part of the development effort of this project, stable instrumentation is out of scope of this project and is expected to come from the OpenFeature project in the form of OpenFeature hooks or native instrumentation in OpenFeature SDKs.
Any use of baggage, including propagating fields to be used in feature flag evaluation context, is also out of scope.

## Staffing

The project is expected to be mainly staffed by OpenFeature contributors representing a strong subsection of the feature flagging vendor and user community.
This group will provide the domain expertise to ensure the feature flag observability meets the requirements of feature flag vendors and users.

This project also includes Dan Dyla acting as one of the project leads.
Dan is a member of the GC, maintainer of OTel JS, and has experience developing semantic conventions.
Dan will provide the necessary expertise to ensure the proposed semantic conventions meet the standards and expectations of the OpenTelemetry community and semantic conventions SIG.

TODO: list engineers committed to working on the project

### Required staffing

**Project Leads:** Daniel Dyla and Michael Beemer (OpenFeature co-founder/GC member)

**Engineers willing to write and review prototypes:**

TODO: list prototype languages and engineers

- JS - Daniel Dyla (Maintainer)

## Meeting Times

This project expects to meet every 2 weeks until this charter is fulfilled.
The exact time and date of the meeting will be determined after the project is approved.

## Timeline

We expect the project to take about 1 calendar quarter. The OpenFeature project is currently targeting Kubecon NA 2024 to announce stable OpenTelemetry support.

- 2-4 weeks - First experimental semantic convention built on pre-exising feature flag semantic conventions
- 2-4 weeks - Prototype implementation and review
- 2-4 weeks - Incorporate feedback from prototype implementers
- 2-4 weeks - Final review period including the greater spec and maintainer community

## Labels

This project will use the label [`area:feature-flag`](https://github.com/open-telemetry/semantic-conventions/labels/area%3Afeature-flag) to track issues and pull requests in the semantic conventions repository.

## Project Board

Once the project is approved a project board will be created and linked here.
The project lead and all other relevant project members should have edit access to the board.
The board will be pre-populated with at least the following issues to track deliverables and the timeline.

- **signal type for feature flag impressions** - agree on which signal type or types should be used to represent feature flag impressions.
- **signal type for feature flag changes** - agree on which signal type or types should be used to represent feature flag changes.
- **semantic conventions for feature flag impressions** - make any necessary additions to the semantic conventions to support feature flag impressions
- **semantic conventions for feature flag changes** - make any necessary additions to the semantic conventions to support feature flag change events
- **prototype feature flag impressions**
- **prototype feature flag change events** - feature flag change events may not be generated by SDKs or instrumentations, but by the feature flag management tools.