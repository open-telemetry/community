# CI/CD Observability Semantic Conventions Working Group

## Description

The goal of this working group is define the semantic conventions for CI/CD Observability and outline 
a path forward for the OpenTelemetry community. 

### Why

The goal of this project is to establish standard semantic conventions for Continuous
Integration (CI) and Continuous (CD) observability. This will provide a common language
and standardized formats for CI/CD observability, enabling the community to observe CI/CD systems.

This will broaden the target audience of OpenTelemetry to Release Engineering and DevOps teams,
further cementing OpenTelemetry as the industry standard Observability framework.

The timing is ripe to start now. The [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files)
has been open since January of 2023 and with the recent changes to the OTEP process, the KubeCon talk, and vendor acknowledgements, there's momentum available to carry this forward. The industry 
is heavily looking for solutions and watching the related OTEP with interest.

## Deliverables

The CI/CD observability working group is planning to deliver the [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files) with prototypes in at least two major vendors:

* [GitHub](https://github.com)
* [GitLab](https://gitlab.com)
* [Jenkins](https://www.jenkins.io/)
* [Keptn](https://lifecycle.keptn.sh/)

A related OTEP that is of great interest to the CI/CD OTEP is that of [Environment Variables as Context Propagators](https://github.com/open-telemetry/opentelemetry-specification/issues/740) which this working group would be available to help with.

> Note: The environment variables as context propagators enables batch systems as a whole, and not just CI/CD systems. We're here to support and will leverage, but it's possible that other working groups already have that OTEP on their radar.

Working prototypes are partially available in these two systems, but have been done outside of the context of this semantic conventions. Thus these prototypes would be updated based on semantic conventions defined.

The following is a current snapshot of prototypes, plugins, components, and CI/CD related tooling that attempt to address CI/CD observability in some form.

| Related Vendor | Prototype                                                                                                                                                   | Related Resources                                                                                  | Comments                                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| GitHub         | [GitHub Actions Receiver](https://github.com/krzko/opentelemetry-collector-contrib/tree/feat-add-githubactionseventreceiver/receiver/githubactionsreceiver) | [OTEL Issue 27460](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/27460) | * Event logs to traces                                                        |
| GitHub/GitLab  | [Git Provider Receiver](https://github.com/liatrio/liatrio-otel-collector/tree/main/pkg/receiver/gitproviderreceiver)                                       | [OTEL Issue 22028](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/22028) | * Delivery metrics by scraping Git vendors                                    |
| K8S            | [Keptn](https://lifecycle.keptn.sh/)                                                                                                                        | [Keptn GitHub Repo](https://github.com/keptn/lifecycle-toolkit)                                    | * Focused on observability in Kubernetes deployments                          |
| Jenkins        | [OpenTelemetry plugin](https://plugins.jenkins.io/opentelemetry/)                                                                                           | [Plugin GitHub Repo](https://github.com/jenkinsci/opentelemetry-plugin)                            | * Tracing of Jenkins pipelines                                                |
| CLI            | [OTEL CLI](https://github.com/equinix-labs/otel-cli)                                                                                                        |                                                                                                    | * Tracing through a CLI wrapper                                               |
| GitHub         | [OpenTelemetry Export Trace - Inception health](https://github.com/marketplace/actions/opentelemetry-export-trace)                                          | [GitHub Action Repo](https://github.com/inception-health/otel-export-trace-action)                 | * Traces via a GitHub action                                                  |
| GitHub         | [OpenTelemetry Actions Exporter - New Relic](https://github.com/marketplace/actions/new-relic-opentelemetry-github-actions-exporter)                        | [GitHub Action Repo](https://github.com/newrelic-experimental/gha-new-relic-exporter)              | * Metrics on workflow runs                                                    |
| GitHub         | [Run with Telemetry GitHub Action](https://github.com/krzko/run-with-telemetry)                                                                             |                                                                                                    | * Traces via GitHub action                                                    |


## Staffing / Help Wanted

The goal of this project will consist of three stages:

1. Working group preparation
2. Specification
3. Implementation

### Required staffing

All stages will require a project lead, domain experts, and engineers at a minimum. 

* @horovits (tentative project lead)
* @adrielp
* @thisthat

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
