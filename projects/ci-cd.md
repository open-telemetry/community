# CI/CD Observability Semantic Conventions Working Group

## Description

The goal of this working group is define the semantic conventions for CI/CD Observability and outline 
a path forward for the OpenTelemetry community. 

### Why

The goal of this project is to establish standard semantic conventions specification for Continuous
Integration (CI) and Continuous Delivery (CD) observability. This will provide a common language
and standardized formats for CI/CD observability, enabling the community to observe CI/CD systems.

This will broaden the target audience of OpenTelemetry to Release Engineering, Platform Engineering, and DevOps teams,
further cementing OpenTelemetry as the industry standard Observability framework.

The timing is ripe to start now. The [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files)
has been open since January of 2023 and with the recent changes to the OTEP process, the KubeCon talk, and vendor acknowledgements, there's momentum available to carry this forward. The industry 
is heavily looking for solutions and watching the related OTEP with interest.

## Deliverables

The CI/CD observability working group is planning to deliver the [CI/CD Observability OTEP](https://github.com/open-telemetry/oteps/pull/223/files) with prototypes in the following areas:

Only a few technologies are named here, so this is not all encompassing. As we build out these conventions, specifications, and prototypes we'll want to ensure that Observability is done within:

* The CI system (SCMs like GitHub/GitLab)
* The tools used within the CI system (Maven/Go)
* The CD system (SCMs if handling deploys / Keptn / ArgoCD)

Current, non-complete list of Deliverables:

* Semantic Convention Updates
* Specification Updates (as applicable)
* [GitHub](https://github.com)
* [GitLab](https://gitlab.com)
* [Jenkins](https://www.jenkins.io/)
* [Keptn](https://lifecycle.keptn.sh/)

> Working prototypes are partially available in these systems, but have been done outside of the context of this semantic conventions. Thus these prototypes would be updated based on semantic conventions defined.

### Related OTEP(s)

A related OTEP that is of great interest to the CI/CD OTEP is that of [Environment Variables as Context Propagators](https://github.com/open-telemetry/opentelemetry-specification/issues/740).
This OTEP might be driven through other working groups, and isn't the direct focus of this working group, but is has wide arching impacts to enabling distributed tracing in batch systems. 
As we work to define semantic conventions for CI/CD observability, this OTEP will without a doubt come into play in some form and thus is being listed as related but not a direct deliverable.


### Existing Related Solutions

The following is a list of prototypes, plugins, components, and CI/CD related tooling that attempt to address CI/CD observability in some form. 

> This is not a complete list but can be used for reference.

| Related Vendor | Prototype                                                                                                                                                   | Related Resources                                                                                  | Comments                                                      |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| GitHub         | [GitHub Actions Receiver](https://github.com/krzko/opentelemetry-collector-contrib/tree/feat-add-githubactionseventreceiver/receiver/githubactionsreceiver) | [OTEL Issue 27460](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/27460) | * Event logs to traces                                        |
| GitHub/GitLab  | [Git Provider Receiver](https://github.com/liatrio/liatrio-otel-collector/tree/main/receiver/gitproviderreceiver)                                           | [OTEL Issue 22028](https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/22028) | * Delivery metrics by scraping Git vendors                    |
| K8S            | [Keptn](https://lifecycle.keptn.sh/)                                                                                                                        | [Keptn GitHub Repo](https://github.com/keptn/lifecycle-toolkit)                                    | * Focused on observability in Kubernetes deployments          |
| Jenkins        | [OpenTelemetry plugin](https://plugins.jenkins.io/opentelemetry/)                                                                                           | [Plugin GitHub Repo](https://github.com/jenkinsci/opentelemetry-plugin)                            | * Tracing of Jenkins pipelines                                |
| Jenkins        | [OpenTelemetry Agent Host Metrics](https://plugins.jenkins.io/opentelemetry-agent-metrics/)                                                                 |                                                                                                    | * Metrics for Jenkins hosts                                   |
| CLI            | [OTEL CLI](https://github.com/equinix-labs/otel-cli)                                                                                                        |                                                                                                    | * Tracing through a CLI wrapper                               |
| GitHub         | [OpenTelemetry Export Trace - Inception health](https://github.com/marketplace/actions/opentelemetry-export-trace)                                          | [GitHub Action Repo](https://github.com/inception-health/otel-export-trace-action)                 | * Traces via a GitHub action                                  |
| GitHub         | [OpenTelemetry Actions Exporter - New Relic](https://github.com/marketplace/actions/new-relic-opentelemetry-github-actions-exporter)                        | [GitHub Action Repo](https://github.com/newrelic-experimental/gha-new-relic-exporter)              | * Metrics on workflow runs                                    |
| GitHub         | [Run with Telemetry GitHub Action](https://github.com/krzko/run-with-telemetry)                                                                             |                                                                                                    | * Traces via GitHub action                                    |
| GitLab         | [Distributed Tracing](https://docs.gitlab.com/ee/operations/tracing.html)                                                                                   |                                                                                                    | * Tracing in GitLab pipelines                                 |
| pytest         | [pyTest OpenTelemetry plugin](https://pypi.org/project/pytest-otel/)                                                                                        |                                                                                                    | * Tracing of Python test                                      |
| Maven          | [Maven OpenTelemetry extension](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/maven-extension/README.md)                           |                                                                                                    | * Tracing of Maven builds                                     |
| Ansible        | [Ansible OpenTelemetry Callback Plugin](https://docs.ansible.com/ansible/latest/collections/community/general/opentelemetry_callback.html)                  |                                                                                                    | * Tracing in Ansible playbooks                                |
| JUnit          | [JUnit to OpenTelemetry](https://github.com/mdelapenya/junit2otlp)                                                                                          |                                                                                                    | * Tracing of JUnit test results                               |
| Eiffel         | [Eiffel CI/CD Event Protocol](https://eiffel-community.github.io/)                                                                                          |                                                                                                    | * Event protocol for CI/CD observability and interoperability |
| CDEvents       | [CD Event Protocol](https://cdevents.dev/)                                                                                                                  |                                                                                                    | * Event protocol for CI/CD observability and interoperability |
| Tekton         | [Tracing Tekton Enhancement Proposal](https://github.com/tektoncd/community/blob/main/teps/0124-distributed-tracing-for-tasks-and-pipelines.md)             |                                                                                                    | * Tekton Task and Pipeline Tracing                            |

## Staffing / Help Wanted

### TC Sponsorship

* @carlosalberto (TC Sponsor)
* @jsuereth (TC Sponsor)

### Required staffing

All stages will require a project lead, domain experts, and engineers at a minimum. 

* @horovits Project Lead (Logz.io)
* @adrielp (Liatrio)
* @thisthat (Dynatrace, Keptn)
* @acramsay (Liatrio)
* @krzko (ANZ Bank)
* @Elfo404 (Grafana Labs)
* @dsotirakis (Grafana Labs)
* @xibz (Apple)
* @e-backmark-ericsson (Ericsson)
* @dnsmichi (GitLab)
* @kamphaus (Jemmic)
* @magnusbaeck (Axis Communications)
* @darren17082 (GitLab)
* @sguyon (GitLab)
* @kuisathaverat (Elastic)
* @mhausenblas (AWS, ADOT)
* @afrittoli (IBM, Tekton, CDEvents)
* @pmpaulino (Liatrio)
* @ericchapman80 (Liatrio)
* @oleg-nenashev (Gradle, Jenkins)
* @lucavallin (GitHub)

Need more:

- [x] domain experts
- [x] engineers
- [x] TCs 
- [ ] potentially maintainers/approvers in the event that we build language specific prototypes

## Meeting Times

This SIG will begin meeting during the regular Monday Semantic Conventions SIG calls that already exists.
This group will start meeting independently in the future as the project progresses.

## Timeline

Estimated time-frame: 6-12 Months

* Q1 Focus
    * Kickoff
    * Strategy
    * Research and discovery
    * OTEP Approval
* Q2 Focus
    * Semantic Conventions
    * Specifications
    * Prototype Developments
* Q3 TBD
* Q4 TBD

> Note: The working groups intent is to be nimble and able to adjust quickly.

## Labels

* cicd
