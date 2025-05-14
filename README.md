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

For those who are brand new to OpenTelemetry and want to chat or get redirected to the appropriate place for a specific question, feel free to join [the CNCF OpenTelemetry Slack channel](https://cloud-native.slack.com/archives/CJFCJHG4Q). If you are new, you can create a CNCF Slack account [here](https://slack.cncf.io/).

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
cncf-opentelemetry-community@lists.cncf.io    | [Here](https://lists.cncf.io/g/cncf-opentelemetry-community)    | anyone                 | GC and TC         | anyone           | <details><summary>Notes</summary>The community mailing list is for anybody who wants to monitor the latest news from the project. It is used to send updates on community meetings and announcements about new projects and SIGs. There is minimal moderation for a new user to reduce spam, and new users are approved after one post.</details>
cncf-opentelemetry-contributors@lists.cncf.io | [Here](https://lists.cncf.io/g/cncf-opentelemetry-contributors) | anyone                 | anyone            | anyone           | <details><summary>Notes</summary>The discussions mailing list is for anyone who is interested in contributing to OpenTelemetry or has questions (related to the contribution, technical issues,etc) they’d like to discuss. Will be used to announce updates related to how the project is being developed and ask general contribution questions related to the contribution processes. No approval is required to join.</details>
cncf-opentelemetry-tc@lists.cncf.io           | N/A                                                             | TC                     | anyone            | members          | <details><summary>Notes</summary>Used by the OpenTelemetry Technical Committee for internal communication. This mailing list should be used sparingly as we strive to keep all communication public. It only should be used to contact the Technical Committee with questions that cannot be discussed publicly on GitHub, GitHub discussions, or the community or contributors' mailing lists.</details>
cncf-opentelemetry-governance@lists.cncf.io   | N/A                                                             | GC                     | anyone            | members          | <details><summary>Notes</summary>Used by the OpenTelemetry GC for internal communication. Additionally, contact the GC for questions that cannot be discussed publicly on GitHub, GitHub discussions, or other mailing lists. For instance, members could use this for issues related to improper applications of our community membership guidance.</details>
cncf-opentelemetry-comms@lists.cncf.io        | [Here](https://lists.cncf.io/g/cncf-opentelemetry-comms)        | GC and open for anyone | anyone            | anyone           | <details><summary>Notes</summary>Mailing list to notify and request reviews of upcoming announcements, or request a post on the OpenTelemetry Twitter account or other public channels.</details>

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
repository](https://github.com/cncf/artwork/tree/master/projects/opentelemetry). In addition, a [Google Slides template](https://docs.google.com/presentation/d/1Neab3OZ3c-m5kOE37iZXEVpK4Pjj6xGTJEUuUzLQJvk/edit?usp=sharing) is also available.

## How to

- [Get access and manage meetings](docs/how-to-handle-public-calendar.md).
- [Request GitHub extension or create a bit](docs/using-github-extensions.md).
- [Configure new repository](docs/how-to-configure-new-repository.md): listing settings TC members set when creating the new repository.

## Special Interest Groups

We organize the community into Special Interest Groups (SIGs) to
improve our workflow and more efficiently manage a community project. While meetings are expected to happen regularly, they are subject to contributors' availability and may be rescheduled or changed at time. Check our [public calendar](https://github.com/open-telemetry/community#calendar) and SIG-specific GitHub discussions for meeting changes and cancellations. All meetings happen over Zoom, have a meeting notes document, and are recorded and [available on Zoom cloud](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).

Please do not hesitate to contact SIG owners if the proposed time of the
meeting or tools used is unavailable for you. For instance, it is a good
practice to alternate morning/evening meetings once SIG has representatives
from 3 largely distinct timezones. The best way to report it and suggest an
alternative is to file an issue on this repository or discuss it in
SIG-specific GitHub discussions.

> [!NOTE]
> The meeting times in the tables below are given in 24-hour notation.
> Meetings are either in Pacific Time (PT), with Daylight Saving Time, or UTC+8, without Daylight Saving Time.

<!-- sigs -->
### Specification SIGs

| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Sponsors](./project-management.md#project-proposal) | [Governance Committee](./community-members.md#governance-committee) Liaison |
|------|--------------|---------------|---------------|-----------------|--------------------------------|--------------------------------|
| <a id="sig-specification"></a>Specification: General + OTel Maintainers Sync | Tuesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo) | [#otel-specification](https://cloud-native.slack.com/archives/C01N7PP1THC) | [calendar-spec-general](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-general) |  |  | 
| <a id="sig-sampling"></a>Specification: Sampling | Thursday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/1gASMhmxNt9qCa8czEMheGlUW2xpORiYoD7dBD7aNtbQ) | [#otel-sampling](https://cloud-native.slack.com/archives/C027DS6GZD3) | [calendar-spec-sampling](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-sampling) | [Josh MacDonald](https://github.com/jmacd) | [Juraci Paixão Kröhling](https://github.com/jpkrohling) | 
| <a id="sig-config-file"></a>Specification: Configuration | Every other Monday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/1uNgWQLQZcSVfBLRXfW9XCVJmKa5NH9R15fSOXhmpGWw) | [#otel-config-file](https://cloud-native.slack.com/archives/C0476L7UJT1) | [calendar-spec-config](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-config) | [Carlos Alberto](https://github.com/carlosalberto),<br/>[Jack Berg](https://github.com/jack-berg) | [Daniel Gomez Blanco](https://github.com/danielgblanco) | 
| <a id="sig-spec-logs"></a>Specification: Logs | Tuesday at 10:00 PT | [Google Doc](https://docs.google.com/document/d/1BKjQWP32FXL9g1cGbyj7DMXV1Uq_RL8_78rWaMBhN0A) | [#otel-spec-logs](https://cloud-native.slack.com/archives/C062HUREGUV) | [calendar-spec-logs](https://groups.google.com/a/opentelemetry.io/g/calendar-spec-logs) | [Ted Young](https://github.com/tedsuo),<br/>[Trask Stalnaker](https://github.com/trask) | [Ted Young](https://github.com/tedsuo) | 
| <a id="sig-semantic-conventions"></a>Semantic Conventions: General | Monday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/10xG7DNKWRhxNmFGt3yYd3980a9uwS8lMl2LvQL3VNK8) | [#otel-semantic-conventions](https://cloud-native.slack.com/archives/C041APFBYQP) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Armin Ruech](https://github.com/arminru),<br/>[Josh Suereth](https://github.com/jsuereth),<br/>[Reiley Yang](https://github.com/reyang) | [Trask Stalnaker](https://github.com/trask) | 
| <a id="sig-system-metrics"></a>Semantic Conventions: System Metrics | Thursday at 07:30 PT | [Google Doc](https://docs.google.com/document/d/1p5TH57t43XpxA48onLzX4PIr3g6ydYKCtR_AUlsCnQk) | [#otel-system-metrics](https://cloud-native.slack.com/archives/C05CTFE9U4A) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Josh Suereth](https://github.com/jsuereth) | [Pablo Baeyens](https://github.com/mx-psi) | 
| <a id="sig-k8s-semconv-sig"></a>Semantic Conventions: K8s | Every other Wednesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/17DqFVlLvO43neXXTwlSd1zcKjSRA8P3d0Y444QNwUTQ) | [#otel-k8s-semconv-sig](https://cloud-native.slack.com/archives/C07Q1L0FGKX) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Josh Suereth](https://github.com/jsuereth),<br/>[Alexander Wert](https://github.com/AlexanderWert) | [Alolita Sharma](https://github.com/alolita) | 
| <a id="sig-genai-instrumentation"></a>Semantic Conventions and Instrumentation: GenAI | Every Tuesday 9:00 PT and every other Thursday 14:00 UTC+8 | [Google Doc](https://docs.google.com/document/d/1EKIeDgBGXQPGehUigIRLwAUpRGa7-1kXB736EaYuJ2M) | [#otel-genai-instrumentation](https://cloud-native.slack.com/archives/C06KR7ARS3X) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Ted Young](https://github.com/tedsuo),<br/>[Liudmila Molkova](https://github.com/lmolkova) | [Ted Young](https://github.com/tedsuo) | 
| <a id="sig-cicd"></a>Semantic Conventions: CI/CD | Every Thursday at 06:00 PT | [Google Doc](https://docs.google.com/document/d/1CdzXD16QpayEpPxae_3u-7BLyzv0GgzZrKvV7tTFDr0) | [#otel-cicd](https://cloud-native.slack.com/archives/C0598R66XAP) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Josh Suereth](https://github.com/jsuereth),<br/>[Carlos Alberto](https://github.com/carlosalberto) | [Daniel Gomez Blanco](https://github.com/danielgblanco) | 
| <a id="sig-semconv-security"></a>Semantic Conventions: Security | Meets during Semantic Conventions: General | [Google Doc](https://docs.google.com/document/d/10xG7DNKWRhxNmFGt3yYd3980a9uwS8lMl2LvQL3VNK8) | [#otel-semconv-security](https://cloud-native.slack.com/archives/C0715DWUW7L) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Josh Suereth](https://github.com/jsuereth) | [Trask Stalnaker](https://github.com/trask) | 
| <a id="sig-ff-semconv"></a>Semantic Conventions: Feature Flags | Every other Monday at 07:30 PT | [Google Doc](https://docs.google.com/document/d/1x9hprUaUNlVCZMtFAqBcj6h50ukpT0hCAli7BzgWsTQ) | [#otel-ff-semconv](https://cloud-native.slack.com/archives/C07AES1JN56) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Daniel Dyla](https://github.com/dyladan),<br/>[Alexander Wert](https://github.com/AlexanderWert) | [Pablo Baeyens](https://github.com/mx-psi) | 
| <a id="sig-entities"></a>Specification: Entities | Every other Thursday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/15Yt9ss2_EhuFPqItPbk4vjfpeRDAQ5WCUVuY_kCeOAo) | [#otel-entities](https://cloud-native.slack.com/archives/C06QEG97W7L) | [calendar-entities](https://groups.google.com/a/opentelemetry.io/g/calendar-entities) | [Josh Suereth](https://github.com/jsuereth),<br/>[Tigran Najaryan](https://github.com/tigrannajaryan) | [Severin Neumann](https://github.com/svrnm) | 
| <a id="sig-opamp"></a>OpAMP | Every other Wednesday at 11:00 PT | [Google Doc](https://docs.google.com/document/d/19WA5-ex8rNFIBIyVb5VqMXfWNmUQwppGhN8zBeNG0f4) | [#otel-opamp](https://cloud-native.slack.com/archives/C02J58HR58R) | [calendar-opamp](https://groups.google.com/a/opentelemetry.io/g/calendar-opamp) | [Tigran Najaryan](https://github.com/tigrannajaryan) | [Ted Young](https://github.com/tedsuo) | 
| <a id="sig-prometheus"></a>Prometheus Interoperability | Every other Wednesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/19bnXziPn2MZ9wO6684UoI4D-LCjGL5bTJkGhux29bx8) | [#otel-prometheus](https://cloud-native.slack.com/archives/C01LSCJBXDZ) | [calendar-prometheus](https://groups.google.com/a/opentelemetry.io/g/calendar-prometheus) |  | [Alolita Sharma](https://github.com/alolita) | 
| <a id="sig-faas"></a>Functions as a Service (FAAS) | Every other Wednesday at 8:00 PT | [Google Doc](https://docs.google.com/document/d/187XYoQcXQ9JxS_5v2wvZ0NEysaJ02xoOYNXj08pT0zc) | [#otel-faas](https://cloud-native.slack.com/archives/C04HVBETC9Z) | [calendar-faas](https://groups.google.com/a/opentelemetry.io/g/calendar-faas) |  | [Austin Parker](https://github.com/austinlparker) | 
| <a id="sig-profiles"></a>Profiling | Every other Thursday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/19UqPPPlGE83N37MhS93uRlxsP1_wGxQ33Qv6CDHaEp0) | [#otel-profiles](https://cloud-native.slack.com/archives/C03J794L0BV) | [calendar-profiling](https://groups.google.com/a/opentelemetry.io/g/calendar-profiling) | [Josh Suereth](https://github.com/jsuereth),<br/>[Tigran Najaryan](https://github.com/tigrannajaryan) | [Morgan McLean](https://github.com/mtwo) | 
| <a id="sig-mainframes"></a>OpenTelemetry on Mainframes | Tuesday at 10:00 PT | [Google Doc](https://docs.google.com/document/d/14p-bpofozTL4n3jy6HZH_TKjoOXvog18G1HBRqq6liE) | [#otel-mainframes](https://cloud-native.slack.com/archives/C05PXDFTCPJ) | [calendar-mainframe](https://groups.google.com/a/opentelemetry.io/g/calendar-mainframe) | [Alolita Sharma](https://github.com/alolita),<br/>[Daniel Dyla](https://github.com/dyladan),<br/>[Morgan McLean](https://github.com/mtwo) | [Morgan McLean](https://github.com/mtwo) | 
| <a id="sig-client-side-telemetry"></a>Client Instrumentation | Tuesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/16Vsdh-DM72AfMg_FIt9yT9ExEWF4A_vRbQ3jRNBe09w) | [#otel-client-side-telemetry](https://cloud-native.slack.com/archives/C0239SYARD2) | [calendar-client-side](https://groups.google.com/a/opentelemetry.io/g/calendar-client-side) |  | [Daniel Gomez Blanco](https://github.com/danielgblanco) | 

### Implementation SIGs

| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Governance Committee](./community-members.md#governance-committee) Liaison |
|------|--------------|---------------|---------------|-----------------|--------------------------------|
| <a id="sig-android"></a>Android: SDK + Automatic Instrumentation | Tuesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/1W72oElAJuYx3efM9wkH5l1iksdfwmTSkVl-H7KHTLnY) | [#otel-android](https://cloud-native.slack.com/archives/C05J0T9K27Q) | [calendar-android](https://groups.google.com/a/opentelemetry.io/g/calendar-android) | [Trask Stalnaker](https://github.com/trask) |
| <a id="sig-arrow"></a>Arrow | Alternating between Tuesday at 16:00 PT and Thursday at 8:00 PT | [Google Doc](https://docs.google.com/document/d/1z8_Ra-ALDaYNa88mMj1gOZtOpLZLRk0-dZEmDjPmcUs) | [#otel-arrow](https://cloud-native.slack.com/archives/C07S4Q67LTF) | [calendar-arrow](https://groups.google.com/a/opentelemetry.io/g/calendar-arrow) | [Trask Stalnaker](https://github.com/trask) |
| <a id="sig-collector"></a>Collector | Alternating between Tuesday at 17:00 PT, Wednesday at 09:00 PT, and Wednesday at 05:00 PT | [Google Doc](https://docs.google.com/document/d/1r2JC5MB7GupCE7N32EwGEXs9V_YIsPgoFiLP4VWVMkE) | [#otel-collector](https://cloud-native.slack.com/archives/C01N6P7KR6W) | [calendar-collector](https://groups.google.com/a/opentelemetry.io/g/calendar-collector) | [Pablo Baeyens](https://github.com/mx-psi) |
| <a id="sig-cpp"></a>C++: SDK | Alternating between Monday at 13:00 PT and Wednesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1i1E4-_y4uJ083lCutKGDhkpi3n4_e774SBLi9hPLocw) | [#otel-cpp](https://cloud-native.slack.com/archives/C01N3AT62SJ) | [calendar-cpp](https://groups.google.com/a/opentelemetry.io/g/calendar-cpp) | [Severin Neumann](https://github.com/svrnm) |
| <a id="sig-dotnet-auto-instr"></a>.NET: Automatic Instrumentation | Wednesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1dYdwRQVE3zu0vlp_lqGctNm0dCQUkDo2LfScUJzpuT8) | [#otel-dotnet-auto-instr](https://cloud-native.slack.com/archives/C01NR1YLSE7) | [calendar-dotnet](https://groups.google.com/a/opentelemetry.io/g/calendar-dotnet) | [Morgan McLean](https://github.com/mtwo) |
| <a id="sig-dotnet"></a>.NET: SDK | Tuesday at 11:00 PT | [Google Doc](https://docs.google.com/document/d/1yjjD6aBcLxlRazYrawukDgrhZMObwHARJbB9glWdHj8) | [#otel-dotnet](https://cloud-native.slack.com/archives/C01N3BC2W7Q) | [calendar-dotnet](https://groups.google.com/a/opentelemetry.io/g/calendar-dotnet) | [Morgan McLean](https://github.com/mtwo) |
| <a id="sig-erlang-elixir"></a>Erlang/Elixir: SDK | Every other Thursday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1EbBiRjBc_cBf0T_B5OtNRPhbD4jdBrVYJAy8euCDrUI) | [#otel-erlang-elixir](https://cloud-native.slack.com/archives/C01N75YMZCN) | [calendar-erlang](https://groups.google.com/a/opentelemetry.io/g/calendar-erlang) | [Austin Parker](https://github.com/austinlparker) |
| <a id="sig-go"></a>GoLang: SDK | Thursday alternating between 09:00 PT and 10:00 PT | [Google Doc](https://docs.google.com/document/d/1E5e7Ld0NuU1iVvf-42tOBpu2VBBLYnh73GJuITGJTTU) | [#otel-go](https://cloud-native.slack.com/archives/C01NPAXACKT) | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [Ted Young](https://github.com/tedsuo) |
| <a id="sig-go-instrumentation"></a>GoLang: Automatic Instrumentation | Every other Tuesday at 09:30 PT | [Google Doc](https://docs.google.com/document/d/1P6am_r_cxCX1HcpDQlznrTrTOvwN2whshL0f58lXSWI) | [#otel-go-instrumentation](https://cloud-native.slack.com/archives/C03S01YSAS0) | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [Juraci Paixão Kröhling](https://github.com/jpkrohling) |
| <a id="sig-go-compile-instrumentation"></a>GoLang: Compile-Time Instrumentation | Every other Thursday at 08:00 UTC | [Google Doc](https://docs.google.com/document/d/1XkVahJfhf482d3WVHsvUUDaGzHc8TO3sqQlSS80mpGY) | [#otel-go-compile-instrumentation](https://cloud-native.slack.com/archives/C088D8GSSSF) | [calendar-go](https://groups.google.com/a/opentelemetry.io/g/calendar-go) | [Juraci Paixão Kröhling](https://github.com/jpkrohling) |
| <a id="sig-java"></a>Java: SDK + Instrumentation | Thursday at 09:00 PT, and every other Thursday at 09:00 UTC+8 | [Google Doc](https://docs.google.com/document/d/1D7ZD93LxSWexHeztHohRp5yeoTzsi9Dj1HRm7Tad-hM) | [#otel-java](https://cloud-native.slack.com/archives/C014L2KCTE3) | [calendar-java](https://groups.google.com/a/opentelemetry.io/g/calendar-java) | [Trask Stalnaker](https://github.com/trask) |
| <a id="sig-js"></a>JavaScript: SDK | Wednesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1tCyoQK49WVcE-x8oryZOTTToFm7sIeUhxFPm9g-qL1k) | [#otel-js](https://cloud-native.slack.com/archives/C01NL1GRPQR) and [GitHub Discussions](https://github.com/open-telemetry/opentelemetry-js/discussions) | [calendar-js](https://groups.google.com/a/opentelemetry.io/g/calendar-js) | [Pablo Baeyens](https://github.com/mx-psi) |
| <a id="sig-php"></a>PHP: SDK | Wednesday at 10:30 PT | [Google Doc](https://docs.google.com/document/d/1WLDZGLY24rk5fRudjdQAcx_u81ZQWCF3zxiNT-sz7DI) | [#otel-php](https://cloud-native.slack.com/archives/C01NFPCV44V) | [calendar-php](https://groups.google.com/a/opentelemetry.io/g/calendar-php) | [Severin Neumann](https://github.com/svrnm) |
| <a id="sig-python"></a>Python: SDK | Thursday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1CIMGoIOZ-c3-igzbd6_Pnxx1SjAkjwqoYSUWxPY8XIs) | [#otel-python](https://cloud-native.slack.com/archives/C01PD4HUVBL) | [calendar-python](https://groups.google.com/a/opentelemetry.io/g/calendar-python) | [Daniel Gomez Blanco](https://github.com/danielgblanco) |
| <a id="sig-ruby"></a>Ruby: SDK | Tuesday at 10:00 PT | [Google Doc](https://docs.google.com/document/d/1EaIbfDE1elWTWt3bhilggki_OCRJZoFCSYZJXgc9KsM) | [#otel-ruby](https://cloud-native.slack.com/archives/C01NWKKMKMY) and [GitHub Discussions](https://github.com/open-telemetry/opentelemetry-ruby/discussions) | [calendar-ruby](https://groups.google.com/a/opentelemetry.io/g/calendar-ruby) | [Ted Young](https://github.com/tedsuo) |
| <a id="sig-rust"></a>Rust: SDK | Tuesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/12upOzNk8c3SFTjsL6IRohCWMgzLKoknSCOOdMakbWo4) | [#otel-rust](https://cloud-native.slack.com/archives/C03GDP0H023) and [Gitter](https://gitter.im/open-telemetry/opentelemetry-rust) | [calendar-rust](https://groups.google.com/a/opentelemetry.io/g/calendar-rust) | [Ted Young](https://github.com/tedsuo) |
| <a id="sig-swift"></a>Swift: SDK | Thursday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1LugL8r4bAkbTxZ1Gq_6j_8SDv1LuZaNeUdR-QLN4d48) | [#otel-swift](https://cloud-native.slack.com/archives/C01NCHR19SB) | [calendar-swift](https://groups.google.com/a/opentelemetry.io/g/calendar-swift) | [Alolita Sharma](https://github.com/alolita) |
| <a id="sig-ebpf"></a>eBPF | Tuesday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/13GK915hdDQ9sUYzUIWi4pOfJK68EE935ugutUgL3yOw) | [#otel-ebpf](https://cloud-native.slack.com/archives/C02AB15583A) | [calendar-ebpf](https://groups.google.com/a/opentelemetry.io/g/calendar-ebpf) | [Ted Young](https://github.com/tedsuo) |
| <a id="sig-ebpf-instrumentation"></a>eBPF Instrumentation | Wednesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/1ZkmUT2EHKfgtLqrgx3WI8aBy2QNyZeTwSKXxe3DI6Pw) | [#otel-ebpf-instrumentation](https://cloud-native.slack.com/archives/C08P9L4FPKJ) | [calendar-ebpf-instrumentation](https://groups.google.com/a/opentelemetry.io/g/calendar-ebpf-instrumentation) | [Severin Neumann](https://github.com/svrnm) |
| <a id="sig-operator"></a>Kubernetes Operator | Thursday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1Unbs2qp_j5kp8FfL_lRH-ld7i5EOQpsq0I4djkOOSL4) | [#otel-operator](https://cloud-native.slack.com/archives/C033BJ8BASU) | [calendar-k8s-operator](https://groups.google.com/a/opentelemetry.io/g/calendar-k8s-operator) | [Juraci Paixão Kröhling](https://github.com/jpkrohling) |
| <a id="sig-community-demo"></a>Community Demo Application | Wednesday at 08:00 PT | [Google Doc](https://docs.google.com/document/d/16f-JOjKzLgWxULRxY8TmpM_FjlI1sthvKurnqFz9x98) | [#otel-community-demo](https://cloud-native.slack.com/archives/C03B4CWV4DA) | [calendar-demo-app](https://groups.google.com/a/opentelemetry.io/g/calendar-demo-app) | [Austin Parker](https://github.com/austinlparker) |
| <a id="sig-weaver"></a>Semantic Conventions: Tooling | Wednesday at 07:00 PT | [Google Doc](https://docs.google.com/document/d/1ygwXgOFRF01UfUOgMr_ElyL7fSDPchTKSrqfj-_HeyA) | [#otel-weaver](https://cloud-native.slack.com/archives/C0697EXNTL3) | [calendar-semconv](https://groups.google.com/a/opentelemetry.io/g/calendar-semconv) | [Trask Stalnaker](https://github.com/trask) |

### Cross-Cutting SIGs

| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Governance Committee](./community-members.md#governance-committee) Liaison |
|------|--------------|---------------|---------------|-----------------|--------------------------------|
| <a id="sig-comms"></a>Communications (Website, [Documentation](https://opentelemetry.io/docs/), etc.) | Every other Wednesday at 10:00 PT | [Google Doc](https://docs.google.com/document/d/1wW0jLldwXN8Nptq2xmgETGbGn9eWP8fitvD5njM-xZY) | [#otel-comms](https://cloud-native.slack.com/archives/C02UN96HZH6) | [calendar-comms](https://groups.google.com/a/opentelemetry.io/g/calendar-comms) | [Severin Neumann](https://github.com/svrnm) |
| <a id="sig-end-user"></a>End-User SIG | Every other Thursday at 10:00 PT | [Google Doc](https://docs.google.com/document/d/1e-UNZA3Tuno9b53RQbe--whUcO0VIXF3P81oXsrBK6g) | [#otel-sig-end-user](https://cloud-native.slack.com/archives/C01RT3MSWGZ) | [calendar-sig-end-user](https://groups.google.com/a/opentelemetry.io/g/calendar-sig-end-user) | [Daniel Gomez Blanco](https://github.com/danielgblanco) |
| <a id="sig-security"></a>Security | Every Monday at 09:00 PT | [Google Doc](https://docs.google.com/document/d/1P2xejC7lEkOV_Z-8E0oZPXLK5HOnUPNuRqKP0ZQ5fpg) | [#otel-sig-security](https://cloud-native.slack.com/archives/C05A85QC281) | [calendar-sig-security](https://groups.google.com/a/opentelemetry.io/g/calendar-sig-security) | [Trask Stalnaker](https://github.com/trask) |
| <a id="sig-project-infra"></a>Project Infrastructure | Thursday at 11:00 PT | [Google Doc](https://docs.google.com/document/d/1_dTP2XIaZoFjNiipkeMaGJN10NrhS20FiBTTJoQJeVM) | [#otel-project-infra](https://cloud-native.slack.com/archives/C07BPU981PV) | [calendar-project-infra](https://groups.google.com/a/opentelemetry.io/g/calendar-project-infra) | [Austin Parker](https://github.com/austinlparker) |
| <a id="sig-contributor-experience"></a>Contributor Experience | Monday alternating between 10:00 PT and 17:00 UTC+8 | [Google Doc](https://docs.google.com/document/d/1CTQI0p3QF8JP8reV8z_ggcs8KE5YVPpQGvAQknw4qP0) | [#otel-contributor-experience](https://cloud-native.slack.com/archives/C06TMJ2R0SK) | [calendar-contributor-experience](https://groups.google.com/a/opentelemetry.io/g/calendar-contributor-experience) | [Juraci Paixão Kröhling](https://github.com/jpkrohling) |
| <a id="sig-devex"></a>Developer Experience | Wednesday 11:00 PT and 17:00 UTC+8 | [Google Doc](https://docs.google.com/document/d/1QDZYAvGJbqgodJaTxRPmRZh-fEJjb6XstvPUst6h50w) | [#otel-devex](https://cloud-native.slack.com/archives/C01S42U83B2) | [calendar-developer-experience](https://groups.google.com/a/opentelemetry.io/g/calendar-developer-experience) | [Austin Parker](https://github.com/austinlparker) |

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
