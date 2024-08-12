# Developer Experience Project

## Background and description

Convenience as a SIG was initially proposed by [Ted
Young](https://github.com/tedsuo) back in 2021. It was postponed to prioritize
completion of signal specs and stabilization. A document was written at this
time describing the intent to do user research and a brainstorming session,
https://docs.google.com/document/d/1bjiw5L4E8FztRtfsy4Nu9A6qSP-BJlK6BBzl6Rea-Ds/edit#heading=h.b7qckyjgu28i.
This brainstorm resulted in a list of some existing convenience functions
languages have and proposed ones, like a `start` which takes the tracer from the
active span in the current context, and proposals for defining annotations for
easier instrumentation.

### Current challenges

We know users can find the API and SDK to be complex and daunting, the challenge
is to collect actionable feedback on this issues. That information is spread
across various languages' issues, blog posts and other online commentary.
Performing an end user survey will help collect some of this knowledge into a
central place that is actionable.

When developer experience issues are encountered and addressed they are
currently done in the various language implementations individually and this can
lead to drift between different implementations and with the spec. An example
would be how to handle marking a code block as `untraced` which has
implementations in at least Java, Ruby and Javascript, each done differently,
named differently and with no specification. This means users working across
languages experience different results for similar features and other language
SIG's aren't necessarily even aware of the pain point that their users may
actually be experiencing.

### Goals, objectives, and requirements

With the 3 main signals going stable the time is right to circle back and
address issues users may have faced over the years they've now been using
OpenTelemetry.

This project aims to identify developer experience issues with using
OpenTelemetry, to select 3 that are concerns which can be addressed through
updates to the specification and resolve them.

## Deliverables

The first deliverable will be the collection of experience in dealing with
developer experience issues by each existing language SIG. This means not only
additions to the API/SDK or libraries developed to enhance the experience for
users but any that may be planned or are being thought about because of a
frequent request from their users. A report of the findings will be shared with
the whole community.

Utilizing the knowledge gained from the first deliverable on potential areas of
improvement the next deliverable will be an end user survey. Assuming the agreement and
participation of the End User SIG this will be done in cooperation with them. A
write-up of the results will follow, along with the group's decision on the top 3
issues for the group to work on.

Prototypes of resolutions will be developed and, depending on the scope of the
identified problem, OTEP's will be created where appropriate before opening PR's
to the specification.

## Staffing / Help Wanted

- Project Lead: Tristan Sloughter (MyDecisiveAI)

- GC sponsors: 
  - @austinlparker (Honeycomb)
  - @tedsuo (Lightstep)
      
- TC sponsors:
  - @lmolkova (Microsoft)

- Maintainers, approvers and contributors:
  - @dmathieu (Elastic)
  - @julianocosta89 (Datadog)
  - @martinjt (Honeycomb)
  - @samsp-msft (Microsoft)
  - @stevejgordon (Elastic)

## Meeting Times

Wednesday 11:00 PT and 17:00 UTC+8

## Timeline

Work with End User SIG: Weeks but start time of this depends on their
availability.

Identifying priorities: Weeks

Working on priorities: Weeks to months per.

## Labels

TBA

## Linked Issues and PRs

TBA

## Project Board

https://github.com/orgs/open-telemetry/projects/105
