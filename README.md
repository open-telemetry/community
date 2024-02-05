# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> OpenTelemetry community content

<details>
<summary>
Table of Contents
</summary>

* [Get Involved](#get-involved)
* [Governing Bodies](#governing-bodies)
* [Areas of Interest](#areas-of-interest)
* [Communication](#communication)
  * [Discussions](#discussions)
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

There is a lot to do! If you are interested in getting involved, please join
the mailing lists and attend the community meetings. If you're interested in
contributing to a specific part of the project, please join the appropriate
special interest group (SIG). Details for all of these items are below. We are
a friendly, collaborative group and look forward to working together!

## Governing Bodies

* Governance Committee (GC): [Charter](./governance-charter.md), [Members](./community-members.md#governance-committee)
* Technical Committee (TC): [Charter](./tech-committee-charter.md), [Members](./community-members.md#technical-committee)

Both committees meet regularly, and the respective meeting notes are publicly available in the [GC meeting notes](https://docs.google.com/document/d/1-23Sf7-xZK3OL5Ogv2pK0NP9YotlSa0PKU9bvvtQwp8) and the [TC meeting notes](https://docs.google.com/document/d/1hOHPCu5TGenqTeWPB9qQB_qd33uITZBcvK1FnWxYJAw) Google Docs. The Governance Committee meetings are also recorded.
If you want to check out the recordings, head to the [meeting recordings](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s).

## Areas of Interest

Technical committee members, maintainers, and approvers are encouraged
to list their [areas of interest in this
document](areas-of-interest.md) to help community members find
interested parties and form new special interest groups.

## Communication

### Discussions

We use [GitHub discussions](https://github.com/open-telemetry/community/discussions) for most communications. Please join us there!

For those who are brand new to OpenTelemetry and want to chat or get redirected to the appropriate place for a specific question, feel free to join [the CNCF OpenTelemetry Slack channel](https://cloud-native.slack.com/archives/CJFCJHG4Q). If you are new, you can create a CNCF Slack account [here](https://slack.cncf.io/).

### Calendar

The shared community calendar contains all public OpenTelemetry meetings,
including weekly SIG meetings, monthly community meetings, etc. You
can access it via:

* [Web](https://calendar.google.com/calendar/embed?src=google.com_b79e3e90j7bbsa2n2p5an5lf60%40group.calendar.google.com)
* [Google
Calendar](https://calendar.google.com/calendar?cid=Z29vZ2xlLmNvbV9iNzllM2U5MGo3YmJzYTJuMnA1YW41bGY2MEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
* [iCalendar](https://calendar.google.com/calendar/ical/google.com_b79e3e90j7bbsa2n2p5an5lf60%40group.calendar.google.com/public/basic.ics)
(syncs with Outlook)

The best way to subscribe to OpenTelemetry events is to join the [calendar updates Google
Group](https://groups.google.com/forum/#!forum/opentelemetry-calendar). This will invite you to every OpenTelemetry call and correctly block time for
accepted events, and it will keep your calendar in sync with new and updated events.

(Internal Note: When creating or updating a calendar event in the `OpenTelemetry Public Calendar`, please ensure that `opentelemetry-calendar@googlegroups.com`
is added as an attendee to the meeting invite.  This is what allows updates to the calendar to be synchronized to other attendees.)

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
Refer to [CONTRIBUTING.md](https://github.com/open-telemetry/community/blob/master/CONTRIBUTING.md#code-attribution)
for details on code attribution.

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

### Specification SIGs

| Name                                 | Meeting Time                         | Meeting Notes                                                                                      | Slack Channel                                                                        | [Technical Committee](./community-members.md#technical-committee) Sponsors                                                            |
|--------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| Specification: General               | Every Tuesday at 08:00 PT            | [Google Doc](https://docs.google.com/document/d/1pdvPeKjA8v8w_fGKAN68JjWBmVJtPCpqdi9IZrd6eEo/edit) | [#otel-specification](https://cloud-native.slack.com/archives/C01N7PP1THC)           |                                                                                                                                       |
| Specification: Logs                  | Merged into "Specification: General" | See above                                                                                          | [#otel-logs](https://cloud-native.slack.com/archives/C01N5UCHTEH)                    | [Tigran Najaryan](https://github.com/tigrannajaryan)                                                                                  |
| Specification: Sampling              | Every Thursday at 08:00 PT           | [Google Doc](https://docs.google.com/document/d/1gASMhmxNt9qCa8czEMheGlUW2xpORiYoD7dBD7aNtbQ/)     | [#otel-sampling](https://cloud-native.slack.com/archives/C027DS6GZD3)                | [Josh MacDonald](https://github.com/jmacd)                                                                                            |
| Specification: Configuration         | Every other Monday at 8:00 PT        | [Google Doc](https://docs.google.com/document/d/1uNgWQLQZcSVfBLRXfW9XCVJmKa5NH9R15fSOXhmpGWw/edit) | [#otel-config-file](https://cloud-native.slack.com/archives/C0476L7UJT1)             | [Carlos Alberto](https://github.com/carlosalberto)<br/>[Jack Berg](https://github.com/jack-berg)                                                                               |
| Specification: Events                | Every Friday at 10:00 AM PT          | [Google Doc](https://docs.google.com/document/d/1BKjQWP32FXL9g1cGbyj7DMXV1Uq_RL8_78rWaMBhN0A/edit) | [#otel-event](https://cloud-native.slack.com/archives/C062HUREGUV)                   |                                      |
| Semantic Conventions: General        | Every Monday at 08:00 PT             | [Google Doc](https://docs.google.com/document/d/10xG7DNKWRhxNmFGt3yYd3980a9uwS8lMl2LvQL3VNK8)      | [#otel-semantic-conventions-wg](https://cloud-native.slack.com/archives/C041APFBYQP) | [Armin Ruech](https://github.com/arminru)<br/>[Josh Suereth](https://github.com/jsuereth)<br/>[Reiley Yang](https://github.com/reyang) |
| Semantic Conventions: Messaging      | Every Thursday at 8:00 PT            | [Google Doc](https://docs.google.com/document/d/1dWHhyXnfVife-cQ2DW5-d5Ldp1Lq8Rre2UsHpyo8cEE/)     | [#otel-messaging](https://cloud-native.slack.com/archives/C02Q4AAHDSA)               |                                                                                                                                       |
| Semantic Conventions: System Metrics | Every Thursday at 08:30 PT           | [Google Doc](https://docs.google.com/document/d/1p5TH57t43XpxA48onLzX4PIr3g6ydYKCtR_AUlsCnQk)      | [#otel-system-metrics-wg](https://cloud-native.slack.com/archives/C05CTFE9U4A)       | [Josh Suereth](https://github.com/jsuereth)                                                                                           |

### Implementation SIGs

| Name                                  | Meeting Time                                                                                               | Meeting Notes                                                                                                             | Slack Channel                                                                                                                                                |
|---------------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Maintainers Meeting                   | Every Monday at 09:00PT                                                                                    | [Google Doc](https://docs.google.com/document/d/1_X2CTiDXmxk2JozBNwQ2uP8FfV1rxx9ISE5puHu0yIk/edit)                             | [#otel-maintainers](https://cloud-native.slack.com/archives/C01NJ7V1KRC)                                                                                     |
| Collector                             | Every Wednesday at 09:00 PT plus monthly on first Wednesday at 00:00 PT and on third Wednesday at 16:00 PT | [Google Doc](https://docs.google.com/document/d/1r2JC5MB7GupCE7N32EwGEXs9V_YIsPgoFiLP4VWVMkE/edit?usp=sharing)            | [#otel-collector](https://cloud-native.slack.com/archives/C01N6P7KR6W)                                                                                       |
| C/C++: SDK                            | Every week alternating between Monday at 13:00 PT and Wednesday at 9:00 PT                                 | [Google Doc](https://docs.google.com/document/d/1i1E4-_y4uJ083lCutKGDhkpi3n4_e774SBLi9hPLocw/edit?usp=sharing)            | [#otel-cpp](https://cloud-native.slack.com/archives/C01N3AT62SJ)                                                                                             |
| .NET: Automatic Instrumentation       | Every Wednesday at 9:00 PT                                                                                 | [Google Doc](https://docs.google.com/document/d/1XedN2D8_PH4YLej-maT8sp4RKogfuhFpccRi3QpUcoI/edit?usp=sharing)            | [#otel-dotnet-auto-instr](https://cloud-native.slack.com/archives/C01NR1YLSE7)                                                                               |
| .NET: SDK                             | Every Tuesday alternating between 9:00 and 16:00 PT                                                        | [Google Doc](https://docs.google.com/document/d/1yjjD6aBcLxlRazYrawukDgrhZMObwHARJbB9glWdHj8/edit?usp=sharing)            | [#otel-dotnet](https://cloud-native.slack.com/archives/C01N3BC2W7Q)                                                                                          |
| Erlang/Elixir: SDK                    | Every other Thursday at 9:00 PT                                                                            | [Google Doc](https://docs.google.com/document/d/1EbBiRjBc_cBf0T_B5OtNRPhbD4jdBrVYJAy8euCDrUI/edit?usp=sharing)            | [#otel-erlang-elixir](https://cloud-native.slack.com/archives/C01N75YMZCN)                                                                                   |
| GoLang: SDK                           | Every Thursday alternating between 10:00 and 15:00 PDT                                                     | [Google Doc](https://docs.google.com/document/d/1E5e7Ld0NuU1iVvf-42tOBpu2VBBLYnh73GJuITGJTTU/edit)                        | [#otel-go](https://cloud-native.slack.com/archives/C01NPAXACKT)                                                                                              |
| GoLang: Automatic Instrumentation     | Every other week on Tuesday at 9:30 PT                                                                     | [Google Doc](https://docs.google.com/document/d/1P6am_r_cxCX1HcpDQlznrTrTOvwN2whshL0f58lXSWI/edit)                        | [#otel-go-instrumentation](https://cloud-native.slack.com/archives/C03S01YSAS0)                                                                              |
| Java: SDK + Automatic Instrumentation | Every Thursday at 09:00 PT                                                                                 | [Google Doc](https://docs.google.com/document/d/1WK9h4p55p8ZjPkxO75-ApI9m0wfea6ENZmMoFRvXSCw/)                            | [#otel-java](https://cloud-native.slack.com/archives/C014L2KCTE3)                                                                                            |
| JavaScript: SDK                       | Every Wednesday at 09:00 PT                                                                                | [Google Doc](https://docs.google.com/document/d/1tCyoQK49WVcE-x8oryZOTTToFm7sIeUhxFPm9g-qL1k)                             | [#otel-js](https://cloud-native.slack.com/archives/C01NL1GRPQR) and [GitHub Discussions](https://github.com/open-telemetry/opentelemetry-js/discussions)     |
| PHP: SDK                              | Every Wednesday at 10:30 PT                                                                                | [Google Doc](https://docs.google.com/document/d/1WLDZGLY24rk5fRudjdQAcx_u81ZQWCF3zxiNT-sz7DI/edit)                        | [#otel-php](https://cloud-native.slack.com/archives/C01NFPCV44V)                                                                                             |
| Python: SDK                           | Every Thursday at 09:00 PT                                                                                 | [Google Doc](https://docs.google.com/document/d/1CIMGoIOZ-c3-igzbd6_Pnxx1SjAkjwqoYSUWxPY8XIs/edit)                        | [#otel-python](https://cloud-native.slack.com/archives/C01PD4HUVBL)                                                                                          |
| Ruby: SDK                             | Every Tuesday at 09:00 PT                                                                                  | [Google Doc](https://docs.google.com/document/d/1D15bO8o340sQm2CVZiukEJuCO_XMMHKPuTznoEhyFqE/edit)                        | [#otel-ruby](https://cloud-native.slack.com/archives/C01NWKKMKMY) and [GitHub Discussions](https://github.com/open-telemetry/opentelemetry-ruby/discussions) |
| Rust: SDK                             | Every Tuesday at 09:00 PT                                                                                 | [Google Doc](https://docs.google.com/document/d/1tGKuCsSnyT2McDncVJrMgg74_z8V06riWZa0Sr79I_4)                             | [#otel-rust](https://cloud-native.slack.com/archives/C03GDP0H023) and [Gitter](https://gitter.im/open-telemetry/opentelemetry-rust)                          |
| Swift: SDK                            | Every Thursday at 09:00 PT                                                                                 | [Google Doc](https://docs.google.com/document/d/1LugL8r4bAkbTxZ1Gq_6j_8SDv1LuZaNeUdR-QLN4d48/edit)                        | [#otel-swift](https://cloud-native.slack.com/archives/C01NCHR19SB)                                                                                           |
| Communications (Website, [Documentation](https://opentelemetry.io/docs/) etc.)        | Every other week on Monday at 10:00 PT                                                                     | [Google Doc](https://docs.google.com/document/d/1wW0jLldwXN8Nptq2xmgETGbGn9eWP8fitvD5njM-xZY)                             | [#otel-comms](https://cloud-native.slack.com/archives/C02UN96HZH6)                                                                                           |
| End-User WG                           | Every other week on Thursday at 10:00 PT                                                                   | [Google Doc](https://docs.google.com/document/d/1e-UNZA3Tuno9b53RQbe--whUcO0VIXF3P81oXsrBK6g/edit#heading=h.ip90glf2wys2) | [#otel-user-research](https://cloud-native.slack.com/archives/C01RT3MSWGZ)                                                                                   |
| eBPF                                  | Every week on Tuesday at 09:00 PT                                                                          | [Google Doc](https://docs.google.com/document/d/13GK915hdDQ9sUYzUIWi4pOfJK68EE935ugutUgL3yOw)                             | [#otel-ebpf](https://cloud-native.slack.com/archives/C02AB15583A)                                                                                            |
| Agent Management WG                   | Every other week on Tuesday at 11:00 PT                                                                    | [Google Doc](https://docs.google.com/document/d/19WA5-ex8rNFIBIyVb5VqMXfWNmUQwppGhN8zBeNG0f4)                             | [#otel-agentmanwg](https://cloud-native.slack.com/archives/C02J58HR58R)                                                                                      |
| Prometheus Interoperability WG        | Every other week on Wednesday at 08:00 PT                                                                  | [Google Doc](https://docs.google.com/document/d/19bnXziPn2MZ9wO6684UoI4D-LCjGL5bTJkGhux29bx8/edit#)                       | [#otel-prometheus-wg](https://cloud-native.slack.com/archives/C01LSCJBXDZ)                                                                                   |
| Client Instrumentation                | Every Tuesday at 9:00 AM PT                                                                                | [Google Doc](https://docs.google.com/document/d/16Vsdh-DM72AfMg_FIt9yT9ExEWF4A_vRbQ3jRNBe09w/edit)                        | [#otel-client-side-telemetry](https://cloud-native.slack.com/archives/C0239SYARD2)                                                                           |
| Kubernetes Operator                   | Every other week on Thursday at 09:00 PT                                                                   | [Google Doc](https://docs.google.com/document/d/1Unbs2qp_j5kp8FfL_lRH-ld7i5EOQpsq0I4djkOOSL4)                             | [#otel-operator](https://cloud-native.slack.com/archives/C033BJ8BASU)                                                                                        |
| Community Demo Application            | Every Wednesday at 8:00 PT                                                                                    | [Google Doc](https://docs.google.com/document/d/16f-JOjKzLgWxULRxY8TmpM_FjlI1sthvKurnqFz9x98/edit)                        | [#otel-community-demo](https://cloud-native.slack.com/archives/C03B4CWV4DA)                                                                                  |
| Functions as a Service (FAAS)         | Every other Tuesday at 12:00 PM PT                                                                         | [Google Doc](https://docs.google.com/document/d/187XYoQcXQ9JxS_5v2wvZ0NEysaJ02xoOYNXj08pT0zc/edit#)                       | [#otel-faas](https://cloud-native.slack.com/archives/C04HVBETC9Z)                                                                                            |
| Profiling WG                          | Every other week on Thursday at 08:00 AM PT                                                                | [Google Doc](https://docs.google.com/document/d/19UqPPPlGE83N37MhS93uRlxsP1_wGxQ33Qv6CDHaEp0/edit?usp=sharing)            | [#otel-profiles](https://cloud-native.slack.com/archives/C03J794L0BV)                                                                                        |
| Security                              | Weekly on Wednesday at 08:30 AM PT                                                                         | [Google Doc](https://docs.google.com/document/d/1P2xejC7lEkOV_Z-8E0oZPXLK5HOnUPNuRqKP0ZQ5fpg/edit?usp=sharing)            | [#otel-sig-security](https://cloud-native.slack.com/archives/C05A85QC281)                                                                                    |
| OpenTelemetry on Mainframes           | Weekly on Tuesday at 10:00 AM PT                                                                         | [Google Doc](https://docs.google.com/document/d/14p-bpofozTL4n3jy6HZH_TKjoOXvog18G1HBRqq6liE/edit?usp=sharing)            | [#otel-mainframes](https://cloud-native.slack.com/archives/C05PXDFTCPJ)                                                                                      |

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
