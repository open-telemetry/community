# CI/CD Observability SIG Phase 2

<!-- TODO: Potentially create a new project board -->
[**CI/CD Project Board**](https://github.com/orgs/open-telemetry/projects/79)

## Overview

The initial founding of the CI/CD Observability SIG produced multiple outcomes
and improvements in the OpenTelemetry space. To capture a few, the group:

- Created multiple foundational sets of attributes related to CI/CD in the
  registry across multiple versions of Semantic Conventions.
- Added span attribute conventions for CI/CD pipelines.
- Added metric attribute conventions around CI/CD systems.
- Created the OTEP for Environment Variable Context Propagation and drove it
  through approval.
- Based on the OTEP, updated the specification to include support with
  supplementary guidance. 
- Wrote a Python draft prototype to implement the specification.
- Updated and supported the GitHub and GitLab OpenTelemetry Collector
  components.
- Delivered multiple talks around the CI/CD SIG.
- Worked with Jenkins, Team City, and OpenTofu around adoption within those
  technologies.

There is still a lot of things to accomplish, and as such, we propose
implementing phase two of the CI/CD Observability SIG.

### Phase Two Goals

This phase targets three core areas for immediate impact:

1. **SDK Environment Variable Context Propagation**: Implement the spec across
   multiple OpenTelemetry languages for first class, native support.
2. **Enhanced Signal Attribute Conventions**: Establish additional attribute
   conventions for CI/CD-specific signals including build metadata, deployment
   context, issues, incidents, and pipeline execution details.
3. **Beta Stabilization**: Move core CI/CD semantic conventions and SDK
   implementations from experimental to beta status
4. **Increase Adoption**: Work towards getting one or more key technologies
   adoption of the OpenTelemetry conventions.

## Phase 2 Staffing & Responsibilities

### TC Sponsorship

<!-- TODO: Vet that they still want to be sponsors -->
* @carlosalberto (TC Sponsor)
* @jsuereth (TC Sponsor)

### Phase 2 Team Structure

**Project Leadership**:
* @horovits Project Lead (AWS)
* @adrielp Project Lead (Liatrio)

### Phase 2 Resource Requirements

**Critical Needs**:
- [ ] SDK maintainer commitment for environment variable context propagation
  implementation
- [ ] Platform integration testing resources

**Success Dependencies**:
- Dedicated engineering time from SDK teams (guesstimated 2-3 months per SDK)
- Platform vendor collaboration for integration testing
- Community feedback and early adoption validation

## Meeting Times

This SIG will meeting weekly on Wednesdays at 06:00 PT. (Tentative)

## Phase 2 Timeline

**Duration**: 6 months (targeting completion by end of 2025)

> Note: Timeline is aggressive but achievable with focused scope and dedicated
> resources and we will continue to be agile/nimble.

## Labels

* cicd
