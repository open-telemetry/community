# Client Instrumentation

## Description

We believe that in order for OpenTelemetry to be adopted across the board, it needs to have a good support for client applications. Client instrumentation has some unique challenges that are currently not well supported.

Our initial goals include

* define which signal(s) are used for different types of client telemetry
* define semantic conventions for different types of client events
* define semantic conventions for client-specific resources
* define how sessions are handled in SDKs and represented across the wire

Beyond these, we expect that this will be a long-term ongoing project, which might include development of client-optimized SDKs. Also, given that there are many types of client applications/environments, this group may branch into multiple groups over time.

## Project Board

https://github.com/orgs/open-telemetry/projects/19/views/1

## Deliverables

* Semantic conventions for (most common) client events
  * [draft PR for two browser events](https://github.com/martinkuba/opentelemetry-specification/pull/1)
* Semantic conventions for (most common) client resources
  * [Ephemeral Resources OTEP](https://github.com/open-telemetry/oteps/pull/208)
* Logs/Events API + SDK in the Javascript SDK
  * [specification PR](https://github.com/open-telemetry/opentelemetry-specification/pull/2676)
  * [API draft implementation in JS](https://github.com/open-telemetry/opentelemetry-js/pull/3117)
* Logs/Events API + SDK for Android
* Logs/Events API + SDK for Swift
* Implementation of sessions in the Javascript SDK
* Research + proposal for how browser SDK should be optimized
  * [sandbox repository for experimentation](https://github.com/open-telemetry/opentelemetry-sandbox-web-js)

## Staffing / Help Wanted

Expertise required: browser instrumentation, mobile instrumentation

The group currently has several regular contributors who have expertise in browser instrumentation. Most of the focus so far has been on browser and shared concerns across all types of client applications. We need more participation from mobile in order to move mobile instrumentation forward.

### Required staffing

Project lead(s): @martinkuba, @scheler, @MSNev

TC sponsoring members:
Josh Suereth, Jack Berg

## Meeting Times

SIG meeting times: Mondays 12:30am PT
Secondary meeting times: Tuesdays 9am PT
Timeline

##  Timeline
6 - 12 months

