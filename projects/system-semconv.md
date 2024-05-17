# System Semantic Conventions stability

## Description

The OpenTelemetry Collector community would like to stabilize system semantic conventions including system metrics in order to help the adoption of the OTel [hostmetricsreceiver](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/65a1dea390881aad43f5252d730ece36d9c094b5/receiver/hostmetricsreceiver).

## Project Board

See: <https://github.com/orgs/open-telemetry/projects/55/views/3>

### Roadmap

- <https://github.com/open-telemetry/semantic-conventions/issues/127>
- ([@ChrsMark]) <https://github.com/open-telemetry/semantic-conventions/issues/130>
- ([@mx-psi](https://github.com/mx-psi)) <https://github.com/open-telemetry/semantic-conventions/issues/131>
- ([@frzifus](https://github.com/frzifus)) <https://github.com/open-telemetry/semantic-conventions/issues/73>
- ([@dineshg13](https://github.com/dineshg13)) <https://github.com/open-telemetry/semantic-conventions/issues/647>
- <https://github.com/open-telemetry/semantic-conventions/issues/649>
- ([@braydonk](https://github.com/braydonk)) <https://github.com/open-telemetry/opentelemetry-collector-contrib/issues/7417>
- <https://github.com/open-telemetry/semantic-conventions/issues/226>

### done

- ([@frzifus](https://github.com/frzifus)) <https://github.com/open-telemetry/semantic-conventions/issues/98>

#### Optional

- <https://github.com/open-telemetry/semantic-conventions/issues/648>
- <https://github.com/open-telemetry/semantic-conventions/issues/531>

### Finally

- Stabilize existing semantic conventions (system metrics)

## Deliverables

- Mark the [system semantic conventions](https://github.com/open-telemetry/opentelemetry-specification/blob/37ab6b056172ad36d31ce217927e47bbe031d831/specification/metrics/semantic_conventions/system-metrics.md#semantic-conventions-for-system-metrics) as stable.
- Update existing OpenTelemetry Collector hostmetricsreceiver to conform with the stable conventions.

## Staffing / Help Wanted

The goal is to follow [@tedsuo](http://github.com/tedsuo)'s proposed [Semantic Convention Process](https://docs.google.com/document/d/1ghvajKaipiNZso3fDtyNxU7x1zx0_Eyd02OGpMGEpLE/edit#heading=h.xc2ft2cddhny).

- **Stage 1**: SIG Preparation
- **Stage 2**: Stabilizing the Specification
- **Stage 3**: Implementation

### Required staffing

- [@mx-psi](https://github.com/mx-psi), [@frzifus](https://github.com/frzifus) project leads
- [@jsuereth](https://github.com/jsuereth) technical committee sponsor
- domain experts:
  - [@MovieStoreGuy](https://github.com/MovieStoreGuy)
  - [@dmitryax](https://github.com/dmitryax)
  - [@gbbr](https://github.com/gbbr)
  - [@sallyom](https://github.com/sallyom)
  - [@ChrsMark](https://github.com/ChrsMark)
  - [@kaiyan-sheng](https://github.com/kaiyan-sheng)
  - [@braydonk](https://github.com/braydonk)
  - [@bertysentry](https://github.com/bertysentry)
  - [@dineshg13](https://github.com/dineshg13)

## Meetings

*cncf-slack* [#otel-system-metrics](https://cloud-native.slack.com/archives/C05CTFE9U4A)
*meeting-notes* [google-doc](https://docs.google.com/document/d/1p5TH57t43XpxA48onLzX4PIr3g6ydYKCtR_AUlsCnQk)

## Timeline

**Stage 1** (SIG Preparation) is happening now.

**Stage 2** (Stabilizing the Specification) will begin as soon as we have adequate staffing for this project, and we coordinate a weekly meeting times (currently targeting mid-july).

**Stage 3** (Implementation) will begin as soon as the system metrics are marked stable, and it should be relatively short we only need to update conformance to the specification for a single collector package.

## Labels

*The tracking issue should be properly labeled to indicate what parts of the specification it is focused on.*

## Linked Issues and PRs

*All PRs, Issues, and OTEPs related to the project should link back to the tracking issue, so that they can be easily found.*
