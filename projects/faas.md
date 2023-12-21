# FAAS SIG

## Description

The initial goal of this project is to put Lambda monitoring into a consistently good state. Across vendors, customers consistently struggle to instrument their Lambdas and identify the best practices way to monitor a Lambda. Lambda layer behavior differs by language, context propagation is frequently broken, and cold starts are a known issue.

This SIG will also look beyond Lambdas and to more broadly Functions as a Service.

We want to ensure:

* The FAAS spec has been reviewed, assessed to apply generically, and stabilized
* Consistent lambda layer behavior by language and uniform conformance to the spec
* There is clear community guidance on how to monitor Lambdas
* End to end context propagation using community protocols / propagation across typical Lambda architectures (e.g async)
* Cold start data capture and submission
* The new TelemetryAPI is properly integrated and utilized by OpenTelemetry

**This SIG will also serve as a working group for all FAAS topics going forward.**

## Deliverables

* Stabilized FAAS semantic conventions
* Updated Lambda Layer extensions that follow consistent trace propagation and have consistent behavior across languages.
* Cold start processor for the collector
* The first 2 language implementations will be Node.JS and Python.

## Staffing / Help Wanted

The following vendors are interested in improving this area.:

* Lightstep
* AWS
* Splunk (@tsloughter)
* Cisco (@arbiv)
* Honeycomb (@cartermp)

While Lambdas are the focus of this effort we need other Functions As A Service (FAAS) experts to ensure we're building conventions that make sense for the stateless function space in general. GCP or Azure participation would be welcome.

## Required staffing

Project Lead:
@Aneurysm9

Sponsoring TC Members:
* @carlosalberto
* TBA

Implementation Engineers:
* @tylerbenson
* @codeboten
* Cisco contributors (@arbiv)
* Honeycomb contributors (@cartermp)
* @tsloughter
* @xoscar

Implementation Maintainers or Approvers:
* JavaScript - @mwear
* Python - @ocelotl

Lambda SME(s):
@Aneurysm9 to add

## Meeting Times

To deliver the improvements promptly we propose meeting at least 2 days a week for the 6 week planning cycle as specified in the new Semantic Conventions Process Doc

Meeting Times:

PST Option: Tuesday @ 12 pm PST
CET Option: Wednesday @ 7 am PST

## Timeline

1. New working group will be kicked off in January
2. The WG has 6 weeks to propose improvements to the specification and solutions - Beginning of March
3. OTeps and the first implementation in JavaScript will be reviewed by the community - All of March
4. Implementation - we want to start with JavaScript and Python as our first target implementation languages - Beginning of April

## Repo

https://github.com/open-telemetry/opentelemetry-lambda