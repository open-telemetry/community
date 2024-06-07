# Convenience Project

## Background and description

Convenience as a SIG was initially proposed by Ted Young back in 2021. It
was postponed to prioritize completion of signal specs and stabilization. A
document was written at this time describing user research to do and a
brainstorming session,
https://docs.google.com/document/d/1bjiw5L4E8FztRtfsy4Nu9A6qSP-BJlK6BBzl6Rea-Ds/edit#heading=h.b7qckyjgu28i

### Current challenges

Currently the various language implementations resolve user convenience
individually and this can lead to drift between different implementations and
with the spec. An example would be how to handle marking a code block as
`untraced` which has implementations in at least Java, Ruby and Javascript, each
done differently, named differently and with no specification.

### Goals, objectives, and requirements

With the 3 main signals going stable the time is right to circle back and
address issues users may have faced over the years they've now been using
OpenTelemetry.

This project aims to identify developer experience issues with using
OpenTelemetry, to select 3 that are concerns which can be addressed through
updates to the specification and resolve them.

## Deliverables

The first deliverable will be an end user survey. Assuming the agreement and
participation of the End User SIG this will be done in cooperation with them. A
write-up of the results will follow, along with the group's decision on the top 3
issues for the group to work on.

Prototypes of resolutions will be developed and, depending on the scope of the
identified problem, OTEP's will be created where appropriate before opening PR's
to the specification.

## Staffing / Help Wanted

- Project Lead: Tristan Sloughter (MyDecisiveAI)

- TC sponsors: 
  - Austin Parker (Honeycomb)
  - TBA

- Needed: Engineers and maintainers/approvers for multiple languages to develop
  solutions and do prototypes.

## Meeting Times

Weekly meetings TBA.

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

TBA
