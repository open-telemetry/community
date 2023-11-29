# CI/CD Observability Semantic Conventions Working Group

## Description

The goal of this working group is define the semantic conventions for CI/CD Observability and outline 
a path forward for the Open Telemetry community. 

### Why

The goal of this project is to establish standard semantic conventions for Continuous
Integration (CI) and Continuous (CD) observability. This will provide a common language
and standardized formats for CI/CD observability, enabling the community to observe CI/CD systems.

This will broaden the target audience of Open Telemetry to Release Engineering and DevOps teams,
further cementing Open Telemetry as the industry standard Observability framework.

The timing is ripe to start now. The [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files)
has been open since January of 2023 and with the recent changes to the OTEP process, the Kubecon talk, and vendor acknowledgements, there's momentum available to carry this forward. The industry 
is heavily looking for solutions and watching the related OTEP with interest.

## Deliverables

The CI/CD observability working group is planning to deliver the [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files) with prototypes in at least two major vendors:

* [GitHub](https://github.com)
* [GitLab](https://gitlab.com)

A related OTEP that is of great interest to the CI/CD OTEP is that of [Environment Variables as Context Propagators](https://github.com/open-telemetry/opentelemetry-specification/issues/740) which this working group would be available to help with.

> Note: The environment variables as context propagators enables batch systems as a whole, and not just CI/CD systems. We're here to support and will leverage, but it's possible that other working groups already have that OTEP on their radar.

Working prototypes are partially available in these two systems, but have been done outside of the context of this semantic conventions. Thus these prototypes would be updated based on semantic conventions defined.

## Staffing / Help Wanted

The goal of this project will consist of three stages:

1. Working group preparation
2. Specification
3. Implementation

### Required staffing

All stages will require a project lead, domain experts, and engineers at a minimum. 

* @horovits (tentative project lead)
* @adrielp

Need more:

* domain experts
* engineers
* potentially TC's and maintainers/approvers in the event that we build language specific prototypes

> Note: We are working on gathering a huddle with some folks in the industry so between that call and this PR we should be able to fill up and better define staffing and stages. At that point we will remove this message.

## Meeting Times

Once a project is started, the working group should meet regularly for discussion. These meeting times should be posted on the OpenTelemetry public calendar.

## Timeline

What is the expected timeline the project will aim to adhere to, and what resources and deliverables will be needed for each portion of the timeline? If the project has not been started, please describe this timeline in relative terms (one month in, two weeks later, etc). If a project has started, please include actual dates.

## Labels

* cicd
