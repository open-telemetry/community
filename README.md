# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry community content

<details>
<summary>
Table of Contents
</summary>

* [Get Involved](#get-involved)
* [Governing Bodies](#governing-bodies)
* [Areas of Interest](#areas-of-interest)
* [Communication](#communication)
  * [Slack](#slack)
  * [Calendar](#calendar)
  * [Mailing Lists](#mailing-lists)
  * [Media](#media)
* [License](#license)
* [Logos and Brand Guide](#logos-and-brand-guide)
* [How to](#how-to)
* [Special Interest Groups](#special-interest-groups)
  * [Specification SIGs](#specification-sigs)
  * [Implementation SIGs](#implementation-sigs)
  * [Cross-Cutting SIGs](#cross-cutting-sigs)
  * [Localization Teams (part of SIG Communications)](#localization-teams-part-of-sig-communications)
* [Related groups](#related-groups)
  * [W3C - Distributed Tracing Working Group](#w3c---distributed-tracing-working-group)
  * [Erlang Ecosystem Foundation – Observability Working Group](#erlang-ecosystem-foundation--observability-working-group)
  * [CNCF TAG Observability - Technical Advisory Group](#cncf-tag-observability---technical-advisory-group)
  * [K8s SIG - Instrumentation Special Interest Group](#k8s-sig---instrumentation-special-interest-group)
  * [OpenMetrics](#openmetrics)
  * [eBPF Foundation](#ebpf-foundation)

</details>

## Get Involved

There is a lot to do! If you are interested in getting involved, here's how you can start:

1. Check out our [contributor guide](./guides/contributor) to learn about our contribution process.
2. Join our [Slack](#slack) and attend our [community meetings](#calendar).
3. If you're interested in contributing to a specific part of the project, join the appropriate [Special Interest Group (SIG)](#special-interest-groups).

Details for all of these items are below. We are a friendly, collaborative group and look forward to working together!

## Governing Bodies

* Governance Committee (GC): [Charter](./governance-charter.md), [Members](./community-members.md#governance-committee)
* Technical Committee (TC): [Charter](./tech-committee-charter.md), [Members](./community-members.md#technical-committee)

Both committees meet regularly, and the respective meeting notes are publicly available in the [GC meeting notes](https://docs.google.com/document/d/1-23Sf7-xZK3OL5Ogv2pK0NP9YotlSa0PKU9bvvtQwp8) and the [TC meeting notes](https://docs.google.com/document/d/1hOHPCu5TGenqTeWPB9qQB_qd33uITZBcvK1FnWxYJAw) Google Docs. The Governance Committee and Technical Committee meetings are also recorded (although occasionally the meetings are not recorded due to the discussion of sensitive topics).
If you want to check out the recordings, head to the [meeting recordings](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).

## Areas of Interest

Technical committee members, maintainers, and approvers are encouraged
to list their [areas of interest in this
document](areas-of-interest.md) to help community members find
interested parties and form new special interest groups.

## Communication

### Slack

Those who are brand new to OpenTelemetry and want to connect with other contributors, get guidance on contribution etiquette, or learn about development processes are encouraged to join the CNCF OpenTelemetry Slack channel [#opentelemetry-new-contributors](https://cloud-native.slack.com/archives/C09H3MNMBQV).

To follow project developments or chat about OpenTelemetry in general, feel free to join the [#opentelemetry](https://cloud-native.slack.com/archives/CJFCJHG4Q) Slack channel.

If you are new to the CNCF Slack community, you can [create an account](https://slack.cncf.io/).

### Calendar

The shared community calendar contains all public OpenTelemetry meetings,
including weekly SIG meetings, monthly community meetings, etc. You
can access it via:

* [Web](https://calendar.google.com/calendar/embed?src=c_2bf73e3b6b530da4babd444e72b76a6ad893a5c3f43cf40467abc7a9a897f977%40group.calendar.google.com)
* [Google
Calendar](https://calendar.google.com/calendar?cid=c_2bf73e3b6b530da4babd444e72b76a6ad893a5c3f43cf40467abc7a9a897f977@group.calendar.google.com)
* [iCalendar](https://calendar.google.com/calendar/ical/c_2bf73e3b6b530da4babd444e72b76a6ad893a5c3f43cf40467abc7a9a897f977%40group.calendar.google.com/public/basic.ics)

The best way to subscribe to specific OpenTelemetry meeting series is to join the associated
[calendar-...@opentelemetry.io meeting invite groups below](#special-interest-groups).
This will invite you to the specific OpenTelemetry meetings, correctly block time for
accepted meetings, and keep your calendar in sync with new and updated events.

Alternatively, if you wish to subscribe to all OpenTelemetry meeting series you can subscribe to [calendar-all@opentelemetry.io](https://groups.google.com/a/opentelemetry.io/g/calendar-all).

### Mailing Lists

List Name                                     | Signup                                                          | Membership             | Write Permissions | Read Permissions | Notes
----------------------------------------------|-----------------------------------------------------------------|------------------------|-------------------|------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
cncf-opentelemetry-announce@lists.cncf.io     | [Here](https://lists.cncf.io/g/cncf-opentelemetry-announce)     | anyone                 | GC                | anyone           | <details><summary>Notes</summary>Used for announcements.</details>
cncf-opentelemetry-tc@lists.cncf.io           | N/A                                                             | TC                     | anyone            | members          | <details><summary>Notes</summary>Used by the OpenTelemetry Technical Committee for internal communication. This mailing list should be used sparingly as we strive to keep all communication public. It only should be used to contact the Technical Committee with questions that cannot be discussed publicly on GitHub, GitHub discussions, or the community or contributors' mailing lists.</details>
cncf-opentelemetry-governance@lists.cncf.io   | N/A                                                             | GC                     | anyone            | members          | <details><summary>Notes</summary>Used by the OpenTelemetry GC for internal communication. Additionally, contact the GC for questions that cannot be discussed publicly on GitHub, GitHub discussions, or other mailing lists. For instance, members could use this for issues related to improper applications of our community membership guidance.</details>

### Media

For PR & Marketing inquiries, please contact [pr@cncf.io](mailto:pr@cncf.io).

## License

All OpenTelemetry projects are shipped under the permissive Apache 2.0 license
as CNCF IP Policy
[dictates](https://github.com/cncf/foundation/blob/master/charter.md#11-ip-policy).
This [blog post](https://www.cncf.io/blog/2017/02/01/cncf-recommends-aslv2/)
explains the reasoning behind choosing this license.

## Logos and Brand Guide

The OpenTelemetry logos and brand guide can be found in the [CNCF artwork
repository](https://github.com/cncf/artwork/tree/master/projects/opentelemetry). In addition, a [Google Slides template](https://docs.google.com/presentation/d/16Dnax74oG7i_zBEpYQBGlf8mX72pRWehYz1LrIqlTvw/edit?slide=id.g3d3aa3b316c_0_0) is also available.

## How to

- [Get access and manage meetings](docs/how-to-handle-public-calendar.md).
- [Request GitHub extension or create a bit](docs/using-github-extensions.md).
- [Configure new repository](docs/how-to-configure-new-repository.md): listing settings TC members set when creating the new repository.

## Special Interest Groups

We organize the community into Special Interest Groups (SIGs) to
improve our workflow and more efficiently manage a community project. While meetings are expected to happen regularly, they are subject to contributors' availability and may be rescheduled or changed at time. Check our [public calendar](https://github.com/open-telemetry/community#calendar) and SIG-specific GitHub discussions for meeting changes and cancellations. All meetings happen over Zoom, have a meeting notes document, and are recorded and [available in the meeting recordings spreadsheet](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).

Please do not hesitate to contact SIG owners if the proposed time of the
meeting or tools used is unavailable for you. For instance, it is a good
practice to alternate morning/evening meetings once SIG has representatives
from 3 largely distinct timezones. The best way to report it and suggest an
alternative is to file an issue on this repository or discuss it in
SIG-specific GitHub discussions.

> [!NOTE]
> The meeting times in the tables below are given in 24-hour notation.
> Meetings are either in Pacific Time (PT), with Daylight Saving Time, or UTC+8, without Daylight Saving Time.

> [!NOTE]
> **All SIG meetings listed below are open to anyone.** Whether you're a
> seasoned OpenTelemetry contributor, just starting your journey, or simply
> curious about the work we do, you are more than welcome to join.

Detailed SIG information, including meeting notes, repositories, sponsors, and liaisons, is available in [sigs.md](./sigs.md).

<!-- The tables below are auto-generated. To make changes, see CONTRIBUTING.md#updating-sig-information -->
<!-- sigs -->
### Specification SIGs

| Name | Meeting Time | Meeting Invites Group | Slack Channel | Details |
|------|--------------|-----------------------|---------------|---------|
| Specification: General + OTel Maintainers Sync | Tuesday at 08:00 PT | [calendar-spec-general](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-general) | [#otel-specification](https://cloud-native.slack.com/archives/C01N7PP1THC) | [Details](./sigs.md#specification-general--otel-maintainers-sync) |
| Specification: Sampling | Thursday at 08:00 PT | [calendar-spec-sampling](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-sampling) | [#otel-sampling](https://cloud-native.slack.com/archives/C027DS6GZD3) | [Details](./sigs.md#specification-sampling) |
| Specification: Logs | Tuesday at 10:00 PT | [calendar-spec-logs](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-logs) | [#otel-spec-logs](https://cloud-native.slack.com/archives/C062HUREGUV) | [Details](./sigs.md#specification-logs) |
| Semantic Conventions: General | Monday at 08:00 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-semantic-conventions](https://cloud-native.slack.com/archives/C041APFBYQP) | [Details](./sigs.md#semantic-conventions-general) |
| Semantic Conventions: System Metrics | Thursday at 07:30 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-system-metrics](https://cloud-native.slack.com/archives/C05CTFE9U4A) | [Details](./sigs.md#semantic-conventions-system-metrics) |
| Semantic Conventions: K8s | Every other Tuesday at 07:30 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-k8s-semconv-sig](https://cloud-native.slack.com/archives/C07Q1L0FGKX) | [Details](./sigs.md#semantic-conventions-k8s) |
| Semantic Conventions and Instrumentation: GenAI | General GenAI topics: every Tuesday 9:00 PT, every other Tuesday 9:00 UTC+8; agent-related topics: every Monday 9:00 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-genai-instrumentation](https://cloud-native.slack.com/archives/C06KR7ARS3X) | [Details](./sigs.md#semantic-conventions-and-instrumentation-genai) |
| Semantic Conventions: CI/CD | Every Tuesday at 07:00 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-cicd](https://cloud-native.slack.com/archives/C0598R66XAP) | [Details](./sigs.md#semantic-conventions-cicd) |
| Semantic Conventions: RPC | Every Wednesday at 17:00 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-semconv-rpc-stability](https://cloud-native.slack.com/archives/C09D3TRKMED) | [Details](./sigs.md#semantic-conventions-rpc) |
| Semantic Conventions: Service and Deployment | Alternating between Thursday at 08:00 PT and Thursday at 12:00 UTC | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-service-and-deployment-semconv-sig](https://cloud-native.slack.com/archives/C09HLNSSJSE) | [Details](./sigs.md#semantic-conventions-service-and-deployment) |
| Specification: Entities | Every Monday at 09:30 PT | [calendar-entities](https://groups.google.com/a/opentelemetry.io/g/calendar-entities) | [#otel-entities](https://cloud-native.slack.com/archives/C06QEG97W7L) | [Details](./sigs.md#specification-entities) |
| OpAMP | Every other Tuesday at 09:00 PT | [calendar-opamp](https://groups.google.com/a/opentelemetry.io/g/calendar-opamp) | [#otel-opamp](https://cloud-native.slack.com/archives/C02J58HR58R) | [Details](./sigs.md#opamp) |
| Prometheus Interoperability | Every other Friday at 08:00 PT | [calendar-prometheus](https://groups.google.com/a/opentelemetry.io/g/calendar-prometheus) | [#otel-prometheus](https://cloud-native.slack.com/archives/C01LSCJBXDZ) | [Details](./sigs.md#prometheus-interoperability) |
| Functions as a Service (FAAS) | Every other Thursday at 8:00 PT | [calendar-faas](https://groups.google.com/a/opentelemetry.io/g/calendar-faas) | [#otel-faas](https://cloud-native.slack.com/archives/C04HVBETC9Z) | [Details](./sigs.md#functions-as-a-service-faas) |
| Profiling | Every other Thursday at 08:00 PT | [calendar-profiling](https://groups.google.com/a/opentelemetry.io/g/calendar-profiling) | [#otel-profiles](https://cloud-native.slack.com/archives/C03J794L0BV) | [Details](./sigs.md#profiling) |
| OpenTelemetry on Mainframes | Wednesday at 10:00 PT | [calendar-mainframe](https://groups.google.com/a/opentelemetry.io/g/calendar-mainframe) | [#otel-mainframes](https://cloud-native.slack.com/archives/C05PXDFTCPJ) | [Details](./sigs.md#opentelemetry-on-mainframes) |
| Client Instrumentation | Every other Tuesday at 09:00 PT | [calendar-client-side](https://groups.google.com/a/opentelemetry.io/g/calendar-client-side) | [#otel-client-side-telemetry](https://cloud-native.slack.com/archives/C0239SYARD2) | [Details](./sigs.md#client-instrumentation) |

### Implementation SIGs

| Name | Meeting Time | Meeting Invites Group | Slack Channel | Details |
|------|--------------|-----------------------|---------------|---------|
| Android: SDK + Automatic Instrumentation | Tuesday at 08:00 PT | [calendar-android](https://groups.google.com/a/opentelemetry.io/g/calendar-android) | [#otel-android](https://cloud-native.slack.com/archives/C05J0T9K27Q) | [Details](./sigs.md#android-sdk--automatic-instrumentation) |
| Arrow | Alternating between Tuesday at 16:00 PT and Thursday at 8:00 PT | [calendar-arrow](https://groups.google.com/a/opentelemetry.io/g/calendar-arrow) | [#otel-arrow](https://cloud-native.slack.com/archives/C07S4Q67LTF) | [Details](./sigs.md#arrow) |
| Browser | Thursday at 8:30 PT | [calendar-browser](https://groups.google.com/a/opentelemetry.io/g/calendar-browser) | [#otel-browser](https://cloud-native.slack.com/archives/C093P0AMP0T) | [Details](./sigs.md#browser) |
| Collector | Alternating between Tuesday at 17:00 PT, Wednesday at 09:00 PT, and Wednesday at 05:00 PT | [calendar-collector](https://groups.google.com/a/opentelemetry.io/g/calendar-collector) | [#otel-collector](https://cloud-native.slack.com/archives/C01N6P7KR6W) | [Details](./sigs.md#collector) |
| C++: SDK | Alternating between Monday at 13:00 PT and Wednesday at 09:00 PT | [calendar-cpp](https://groups.google.com/a/opentelemetry.io/g/calendar-cpp) | [#otel-cpp](https://cloud-native.slack.com/archives/C01N3AT62SJ) | [Details](./sigs.md#c-sdk) |
| .NET: Automatic Instrumentation | Wednesday at 09:00 PT | [calendar-dotnet](https://groups.google.com/a/opentelemetry.io/g/calendar-dotnet) | [#otel-dotnet-auto-instr](https://cloud-native.slack.com/archives/C01NR1YLSE7) | [Details](./sigs.md#net-automatic-instrumentation) |
| .NET: SDK | Tuesday at 11:00 PT | [calendar-dotnet](https://groups.google.com/a/opentelemetry.io/g/calendar-dotnet) | [#otel-dotnet](https://cloud-native.slack.com/archives/C01N3BC2W7Q) | [Details](./sigs.md#net-sdk) |
| Erlang/Elixir: SDK | Every other Thursday at 09:00 PT | [calendar-erlang](https://groups.google.com/a/opentelemetry.io/g/calendar-erlang) | [#otel-erlang-elixir](https://cloud-native.slack.com/archives/C01N75YMZCN) | [Details](./sigs.md#erlangelixir-sdk) |
| GoLang: SDK | Thursday alternating between 09:00 PT and 10:00 PT | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [#otel-go](https://cloud-native.slack.com/archives/C01NPAXACKT) | [Details](./sigs.md#golang-sdk) |
| GoLang: Automatic Instrumentation | Every other Tuesday at 09:30 PT | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [#otel-go-instrumentation](https://cloud-native.slack.com/archives/C03S01YSAS0) | [Details](./sigs.md#golang-automatic-instrumentation) |
| GoLang: Compile-Time Instrumentation | Every Thursday at 08:00 UTC | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [#otel-go-compile-instrumentation](https://cloud-native.slack.com/archives/C088D8GSSSF) | [Details](./sigs.md#golang-compile-time-instrumentation) |
| Injector | Thursday at 08:00 PT | [calendar-injector](https://groups.google.com/a/opentelemetry.io/g/calendar-injector) | [#otel-injector](https://cloud-native.slack.com/archives/C09025GKPAL) | [Details](./sigs.md#injector) |
| Java: SDK + Instrumentation | Thursday at 09:00 PT, and every other Thursday at 09:00 UTC+8 | [calendar-java](https://groups.google.com/a/opentelemetry.io/g/calendar-java) | [#otel-java](https://cloud-native.slack.com/archives/C014L2KCTE3) | [Details](./sigs.md#java-sdk--instrumentation) |
| JavaScript: SDK | Wednesday at 09:00 PT | [calendar-js](https://groups.google.com/a/opentelemetry.io/g/calendar-js) | [#otel-js](https://cloud-native.slack.com/archives/C01NL1GRPQR) | [Details](./sigs.md#javascript-sdk) |
| Kotlin: SDK | Monday at 09:00 PT | [calendar-kotlin](https://groups.google.com/a/opentelemetry.io/g/calendar-kotlin) | [#otel-kotlin](https://cloud-native.slack.com/archives/C08NRCD4R4G) | [Details](./sigs.md#kotlin-sdk) |
| Packaging | Wednesday at 10:00 PT | [calendar-packaging](https://groups.google.com/a/opentelemetry.io/g/calendar-packaging) | [#otel-packaging](https://cloud-native.slack.com/archives/C0AD17NMBLZ) | [Details](./sigs.md#packaging) |
| PHP: SDK | Wednesday at 08:00 EST | [calendar-php](https://groups.google.com/a/opentelemetry.io/g/calendar-php) | [#otel-php](https://cloud-native.slack.com/archives/C01NFPCV44V) | [Details](./sigs.md#php-sdk) |
| Python: SDK | Thursday at 09:00 PT | [calendar-python](https://groups.google.com/a/opentelemetry.io/g/calendar-python) | [#otel-python](https://cloud-native.slack.com/archives/C01PD4HUVBL) | [Details](./sigs.md#python-sdk) |
| Ruby: SDK | Tuesday at 10:00 PT | [calendar-ruby](https://groups.google.com/a/opentelemetry.io/g/calendar-ruby) | [#otel-ruby](https://cloud-native.slack.com/archives/C01NWKKMKMY) | [Details](./sigs.md#ruby-sdk) |
| Rust: SDK | Alternating between Tuesday at 09:00 AM PT and Wednesday at 8:00 AM PT | [calendar-rust](https://groups.google.com/a/opentelemetry.io/g/calendar-rust) | [#otel-rust](https://cloud-native.slack.com/archives/C03GDP0H023) | [Details](./sigs.md#rust-sdk) |
| Swift: SDK | Thursday at 09:00 PT | [calendar-swift](https://groups.google.com/a/opentelemetry.io/g/calendar-swift) | [#otel-swift](https://cloud-native.slack.com/archives/C01NCHR19SB) | [Details](./sigs.md#swift-sdk) |
| Network | Tuesday at 09:00 PT | [calendar-network](https://groups.google.com/a/opentelemetry.io/g/calendar-network) | [#otel-network](https://cloud-native.slack.com/archives/C02AB15583A) | [Details](./sigs.md#network) |
| eBPF Instrumentation | Wednesday at 08:00 PT | [calendar-ebpf-instrumentation](https://groups.google.com/a/opentelemetry.io/g/calendar-ebpf-instrumentation) | [#otel-ebpf-instrumentation](https://cloud-native.slack.com/archives/C08P9L4FPKJ) | [Details](./sigs.md#ebpf-instrumentation) |
| Kubernetes Operator | Thursday at 09:00 PT | [calendar-k8s-operator](https://groups.google.com/a/opentelemetry.io/g/calendar-k8s-operator) | [#otel-operator](https://cloud-native.slack.com/archives/C033BJ8BASU) | [Details](./sigs.md#kubernetes-operator) |
| Kubernetes Helm Charts | Meets during OpenTelemetry Operator and OpenTelemetry Collector | [calendar-k8s-operator](https://groups.google.com/a/opentelemetry.io/g/calendar-k8s-operator) | [#otel-helm](https://cloud-native.slack.com/archives/C03HVLM8LAH) | [Details](./sigs.md#kubernetes-helm-charts) |
| Community Demo Application | Wednesday at 08:00 PT | [calendar-demo-app](https://groups.google.com/a/opentelemetry.io/g/calendar-demo-app) | [#otel-community-demo](https://cloud-native.slack.com/archives/C03B4CWV4DA) | [Details](./sigs.md#community-demo-application) |
| Semantic Conventions: Tooling | Wednesday at 07:00 PT | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [#otel-weaver](https://cloud-native.slack.com/archives/C0697EXNTL3) | [Details](./sigs.md#semantic-conventions-tooling) |

### Cross-Cutting SIGs

| Name | Meeting Time | Meeting Invites Group | Slack Channel | Details |
|------|--------------|-----------------------|---------------|---------|
| Communications (Website, [Documentation](https://opentelemetry.io/docs/), etc.) | Every other Tuesday at 09:00 PT | [calendar-comms](https://groups.google.com/a/opentelemetry.io/g/calendar-comms) | [#otel-comms](https://cloud-native.slack.com/archives/C02UN96HZH6) | [Details](./sigs.md#communications-website-documentation-etc) |
| End-User SIG | Alternating between Monday at 09:00 PT (Blueprints) and Thursday at 10:00 PT (General) | [calendar-sig-end-user](https://groups.google.com/a/opentelemetry.io/g/calendar-sig-end-user) | [#otel-sig-end-user](https://cloud-native.slack.com/archives/C01RT3MSWGZ) | [Details](./sigs.md#end-user-sig) |
| Security | Every other Monday at 09:00 PT | [calendar-sig-security](https://groups.google.com/a/opentelemetry.io/g/calendar-sig-security) | [#otel-sig-security](https://cloud-native.slack.com/archives/C05A85QC281) | [Details](./sigs.md#security) |
| Contributor Experience | Every other Monday at 10:00 PT | [calendar-contributor-experience](https://groups.google.com/a/opentelemetry.io/g/calendar-contributor-experience) | [#otel-contributor-experience](https://cloud-native.slack.com/archives/C06TMJ2R0SK) | [Details](./sigs.md#contributor-experience) |
| Developer Experience | Wednesday 11:00 PT and 17:00 UTC+8 | [calendar-developer-experience](https://groups.google.com/a/opentelemetry.io/g/calendar-developer-experience) | [#otel-devex](https://cloud-native.slack.com/archives/C01S42U83B2) | [Details](./sigs.md#developer-experience) |

### Localization Teams (part of SIG Communications)

| Name | Meeting Time | Meeting Invites Group | Slack Channel | Details |
|------|--------------|-----------------------|---------------|---------|
| Bengali (bn) |  |  | [#otel-localization-bn](https://cloud-native.slack.com/archives/C08TBCSAY1F) | [Details](./sigs.md#bengali-bn) |
| Chinese (zh-CN) |  |  | [#otel-localization-zhcn](https://cloud-native.slack.com/archives/C08SSK25Y7L) | [Details](./sigs.md#chinese-zh-cn) |
| French (fr-FR) |  |  | [#otel-localization-fr](https://cloud-native.slack.com/archives/C07THD60YLF) | [Details](./sigs.md#french-fr-fr) |
| Japanese (ja-JA) | Every third Wednesday at 01:00pm JST | [calendar-localization-ja](https://groups.google.com/a/opentelemetry.io/g/calendar-localization-ja) | [#otel-localization-ja](https://cloud-native.slack.com/archives/C08SGPBN44E) | [Details](./sigs.md#japanese-ja-ja) |
| Polish (pl-PL) |  |  | [#otel-localization-pl](https://cloud-native.slack.com/archives/C0ALHN9V7PT) | [Details](./sigs.md#polish-pl-pl) |
| Portuguese (pt-BR) |  |  | [#otel-localization-ptbr](https://cloud-native.slack.com/archives/C076LET8YSK) | [Details](./sigs.md#portuguese-pt-br) |
| Romanian (ro-RO) | Monthly on a different day, at a different time (see Slack channel) |  | [#otel-localization-ro](https://cloud-native.slack.com/archives/C09E9KNNLP4) | [Details](./sigs.md#romanian-ro-ro) |
| Spanish (es-ES) | Every second Friday at 8:30am UTC-3 | [calendar-localization-es](https://groups.google.com/a/opentelemetry.io/g/calendar-localization-es) | [#otel-localization-es](https://cloud-native.slack.com/archives/C07PVQVCHA6) | [Details](./sigs.md#spanish-es-es) |
| Ukrainian (uk-UA) |  |  | [#otel-localization-uk](https://cloud-native.slack.com/archives/C097ZNPM3LK) | [Details](./sigs.md#ukrainian-uk-ua) |

<!-- endsigs -->
## Related groups

### W3C - Distributed Tracing Working Group

Join W3C [Distributed Tracing Working Group](https://www.w3.org/2018/distributed-tracing/) to discuss standardization efforts in distributed tracing space.

### Erlang Ecosystem Foundation – Observability Working Group

The Erlang and Elixir API and SDK are maintained by the Erlang Ecosystem Foundation Observability Working Group members.
See the [Observability Working Group](https://erlef.org/wg/observability) page on the EEF website for details.

### CNCF TAG Observability - Technical Advisory Group

The CNCF TAG Observability is a technical advisory group for observability that focuses on topics pertaining to the observation of cloud native workloads.
Check out the [CNCF TAG Observability](https://github.com/cncf/tag-observability) page for details.

### K8s SIG - Instrumentation Special Interest Group

The [K8s SIG](https://github.com/kubernetes/community/tree/master/sig-instrumentation) Instrumentation special interest group coordinates metric requirements of different SIGs for other components through finding common APIs.
This group also covers best practices for cluster observability through metrics, logging, and events across all Kubernetes components.
See the [Instrumentation Special Interest Group](https://github.com/kubernetes/community/tree/master/sig-instrumentation) for details on joining this group.

### OpenMetrics

OpenMetrics is an effort to create an open standard for transmitting metrics at scale, supporting text representation and Protocol Buffers.
See the [OpenMetrics](https://openmetrics.io/) page for details.

### eBPF Foundation

The eBPF foundation aims to facilitate collaboration between eBPF projects, and to ensure good maintenance and clear roadmap for eBPF core.
See the [eBPF Foundation](https://ebpf.io/foundation/) page for more details.
