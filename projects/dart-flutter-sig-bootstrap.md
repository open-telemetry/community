# Bootstrap Dart and Flutter SIG

## Background and description

[Dart](https://dart.dev/) is a top-15 programming language and the language
of [Flutter](https://flutter.dev/), one of the most popular multi-platform
application frameworks. Dart runs on servers, desktop, mobile, and web —
yet it is the last top-15 language without an officially maintained
OpenTelemetry SDK. Prior community efforts, most notably
[Workiva/opentelemetry-dart](https://github.com/Workiva/opentelemetry-dart),
are no longer maintained.

An actively developed implementation of the OpenTelemetry specification for
Dart exists today:

- [dartastic_opentelemetry](https://github.com/MindfulSoftwareLLC/dartastic_opentelemetry) —
  a full SDK implementing the specification's MUST and SHOULD requirements
  for traces and metrics, with logs implemented and maturing, and OTLP/gRPC
  and OTLP/HTTP exporters.
- [dartastic_opentelemetry_api](https://github.com/MindfulSoftwareLLC/dartastic_opentelemetry_api) —
  the standalone API package providing the specification-mandated no-op
  behavior when no SDK is installed.

Both are Apache 2.0, published on pub.dev, and proposed for donation to
OpenTelemetry in
[open-telemetry/community#2718](https://github.com/open-telemetry/community/issues/2718).
The API is stable and extensively unit-tested, downloads are approaching
10,000 per week and climbing, and only a handful of field issues have been
reported to date.
The initial design was reviewed with César Muñoz
([@likethesalad](https://github.com/likethesalad)) of the Android SIG, and
members of Google's Dart and Flutter teams have engaged with and
contributed to the project.

This project bootstraps a **Dart and Flutter SIG** to take ownership of an
official Dart implementation, complete the donation due diligence, and
chart the path to a Flutter (client) SDK in coordination with the Client
SIG and mobile SIGs (Android, Swift, Kotlin).

### Current challenges

**No Official OpenTelemetry Support for Dart and Flutter:**

- Dart and Flutter developers have no officially supported OpenTelemetry
  SDK; the registry's only Dart entry is unmaintained.
- Flutter is a major client platform with no path to the consistency work
  happening in the Client SIG and mobile SIGs.

**Fragmented Community Efforts:**

Multiple abandoned Dart OTel libraries on pub.dev fragment the ecosystem,
duplicate effort, and erode user trust.

**Governance, Not Maturity, Blocks Adoption:**

Without OpenTelemetry governance, a single-vendor implementation cannot
offer the long-term sustainability, security processes, and spec-evolution
guarantees users need. This is observable in practice: several large
enterprises — and Google's own Dart and Flutter teams, who report customer
demand for OpenTelemetry-compliant Dart observability — have evaluated the
SDK but defer production adoption until it is under neutral OpenTelemetry
governance. Technical maturity has not been the blocker; governance has.

### Goals, objectives, and requirements

The primary goal of this project is to bootstrap a Dart and Flutter SIG
that maintains an official, spec-compliant OpenTelemetry API and SDK for
Dart.

**Specific Objectives**

1. **Form the SIG**: meetings, Slack channel, governance per OpenTelemetry
   norms.
2. **Complete due diligence** and acceptance of the donation proposed in
   open-telemetry/community#2718, including repository transfer to the
   open-telemetry organization (donation acceptance remains a separate
   process tracked on that issue).
3. **Document spec compliance** — bring the implementation to a documented
   position on the
   [spec compliance matrix](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md).
4. **Stabilize logs**; drive toward a 1.0 stable release of API and SDK.
5. **Grow a contributor base** beyond the initial maintainers (a Call for
   Contributors blog post is scheduled with SIG Communications).
6. **Define the roadmap for Flutter** client instrumentation in
   coordination with the Client SIG, as a subsequent contribution.

**Motivation for Starting Now**

- Maintainer commitments from four sponsoring organizations plus an
  independent maintainer are in place.
- Google's Dart and Flutter teams are engaged and report customer demand
  for OpenTelemetry-compliant Dart observability.
- Large enterprises that have evaluated the SDK are waiting on
  OpenTelemetry governance to deploy — the donation unblocks adoption.

**Benefits to OpenTelemetry**

- Closes the last top-15 language gap in OpenTelemetry SDK coverage.
- Extends OpenTelemetry's reach into the large Flutter developer community.
- Adds a client-platform perspective to ongoing client/mobile consistency
  work.

## Deliverables

1. **SIG formation** — recurring meeting on the community calendar, Slack
   channel, CONTRIBUTING and governance docs, GitHub project board.
2. **Donation due diligence** (with TC) for the two repositories proposed in
   #2718, followed by transfer to the open-telemetry org upon acceptance.
3. **Spec compliance matrix entries** for Dart (traces, metrics, logs,
   baggage, context, propagators).
4. **Stable 1.0 release** of the Dart API and SDK packages on pub.dev under
   OpenTelemetry governance.
5. **Documentation** — opentelemetry.io language landing page for Dart,
   getting-started guide, and examples.
6. **Flutter SDK roadmap** — a written proposal for Flutter client
   instrumentation, reviewed with the Client SIG (implementation is a
   future project, not part of this bootstrap).

## Expected responsibilities

Once formed, the future work of the SIG will be to adhere to the practices
existing for other supported languages, including:

- build, release, and distribution infrastructure (pub.dev publishing under
  OpenTelemetry governance)
- develop and stabilize a Semantic Conventions library for Dart
- develop the remaining exporters and propagators standard in other
  languages — notably a Zipkin exporter and the B3 and Jaeger propagators
  (OTLP/gRPC, OTLP/HTTP, Prometheus, and console exporters already exist)
- publish API documentation (dartdoc, generated from code)
- produce user guides covering installation, basic usage, and configuration
  on opentelemetry.io
- provide example applications (Dart HTTP server, CLI tool, Flutter app)
- performance benchmarks
- security audits of the implementation
- maintain a versioning and compatibility policy
- track specification releases and semantic-conventions changes as they land

## Staffing / Help Wanted

- A Call for Contributors blog post is approved and scheduled with SIG
  Communications ([opentelemetry.io#9902](https://github.com/open-telemetry/opentelemetry.io/issues/9902)).
- Coordination with the Client SIG and the Android, Swift, and Kotlin SIGs
  for client/mobile consistency.

### Industry outreach

Dartastic.io, Grafana, Embrace, and Ello are sponsoring maintainers (see
below). Outreach and promotion will be conducted through:

- **Developer relations funded by Dartastic.io** — Dartastic.io will
  conduct ongoing devrel for the project: content, demos, and community
  support.
- **Google's Dart and Flutter teams** — Kevin Moore
  ([@kevmoo](https://github.com/kevmoo)) has contributed to the API
  packages, and joint promotion of server-side Dart observability is in
  discussion with Abdallah Shaban
  ([@abdallahshaban557](https://github.com/abdallahshaban557 )) and the Flutter/Dart Outbound Product Management team.
- **Conference talks** — Michael Bushe will present on OpenTelemetry at
  Dart/Flutter conferences.
- **Social platforms** — sustained promotion on social channels.
- **Call for Contributors blog post** — approved and scheduled with SIG
  Communications
  ([opentelemetry.io#9902](https://github.com/open-telemetry/opentelemetry.io/issues/9902)).
- **Cross-SIG coordination** — with the Client SIG and the Android, Swift, Kotlin 
  and Browser SIGs for client/mobile consistency.

### SIG

This project requires the creation of a new SIG: **Dart and Flutter SIG**.

### Required staffing

#### Project Lead(s)

- Michael Bushe ([@michaelbushe](https://github.com/michaelbushe)) —
  Mindful Software, LLC d.b.a. Dartastic.io — author of the donated
  implementation; OpenTelemetry Client SIG participant.

#### Other Staffing

Committed maintainers, across four sponsoring organizations and one
independent:
- Yusuf Rosman ([@yuzurihaaa](https://github.com/yuzurihaaa)) — independent —
  contributed the Logs API; contributor to both the Workiva and Dartastic
  implementations.
- Robert Magnusson ([@robert-northmind](https://github.com/robert-northmind)) —
  Grafana — leads a Flutter app; OpenTelemetry contributor.
- Dane Bratz ([@danexello](https://github.com/danexello)) — Ello —
  contributed the BaggageSpanProcessor; runs a consumer app using the SDK.
- Tamir Hasain ([@tamirh](https://github.com/tamirh)) —
  Ello — Flutter lead.
- Ben Bennett ([@benjaben](https://github.com/benjaben)) — Embrace — Embrace
  uses the Dartastic API in its products.

- https://github.com/open-telemetry/community/issues/2718#issuecomment-4914074892


Additional contributors sought via the Call for Contributors: Dart and
Flutter engineers, documentation writers, and users willing to give
feedback ahead of 1.0.
----
Update: The following contributors showed interest following up on 
the Call for Contributors.  Their replies expressing interest is copied 
here from the [The Donation Proposal](https://github.com/open-telemetry/community/issues/2718) (the Call linked there instead of here):

- Harshit Kushwaha [(@harshitt13)](https://github.com/harshitt13)), OTel backend + Flutter engineer, [donation reply link](https://github.com/open-telemetry/community/issues/2718#issuecomment-4914074892), commits to 3-4 hours a week - he's already put in overtime
- Muhammad Kamel [(@muhammadkamel)](https://github.com/muhammadkamel), Flutter framework contributor, [donation reply link]
- Rohit Joshi [(@rohit482)](https://github.com/rohit482), longtime OTel user and Dartastic follower, [donation reply link](https://github.com/open-telemetry/community/issues/2718#issuecomment-4846499500) commits to 3-4 hrs weekly
- [(@cnbleu)](https://github.com/cnbleu), extensive experience in Flutter, mobile iOS and Android, and RUM, [donation reply link](https://github.com/open-telemetry/community/issues/2718#issuecomment-4843210477), commits to 2-4 hours per week

The `#otel-dart` channel on the [CNCF Slack](https://slack.cncf.io/) will be used for project communication.
All contributors should join including the above four and ([@yuzurihaaa](https://github.com/yuzurihaaa)), ([@robert-northmind](https://github.com/robert-northmind)), ([@danexello](https://github.com/danexello)), ([@tamirh](https://github.com/tamirh)), ([@tamirh](https://github.com/tamirh)), ([@benjaben](https://github.com/benjaben)).
The Slack channel is also included in the API and SDK's CONTRIBUTING.md document.
----

This project implements the existing OpenTelemetry specification; no OTEPs
or specification changes are anticipated, so the cross-language prototype
staffing requirement does not apply. Should a specification change become
necessary, maintainers or approvers from at least two other language SIGs
will be recruited as reviewers per the project staffing requirements.

### Sponsorship

#### TC Sponsor

Requested — see pull request description.

#### GC Liaison

Severin Neumann ([@svrnm](https://github.com/svrnm))

## Expected Timeline

- **Months 1–2:** SIG bootstrapped — meetings scheduled, Slack channel,
  project board; donation due-diligence started with the TC.
- **Months 2–6:** Repository transfer upon donation acceptance; CI, CLA,
  and release automation aligned with org standards.
- **Months 6–9:** Spec compliance matrix submitted; logs stabilization.
- **Months 9–12:** 1.0 stable release of API and SDK; Flutter SDK roadmap
  proposal reviewed with the Client SIG; project completion review — SIG
  transitions to permanent operation.

This timeline is deliberately paced around adoption, not implementation:
the SDK is already built, stable, and tested. Large organizations that have
evaluated it are waiting on OpenTelemetry governance before deploying to
production. The months between donation acceptance and the 1.0 release are
sized to convert those evaluations into production deployments and to fold
feedback from real workloads at scale into the API before 1.0
can be considered production ready.

Deliverables requiring public review — donation due diligence, the spec
compliance matrix, and 1.0 API stabilization — will be announced ahead of
their review windows so reviewers can plan availability. After approval,
specific target dates will be set on the GitHub project, and status will be
shared via GitHub project updates at least quarterly (using the standard
Inactive / On Track / At Risk / Off Track / Completed statuses). Timelines
will be revised in this document if they prove unrealistic.

## Labels (Optional)

`area:sdk`, `lang:dart`

## GitHub Project (Post-Approval)

To be created from the OpenTelemetry project template after approval; link
will be added here.

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

Meeting cadence, calendar entry, and `workstreams.yml` updates will be made
after approval, following the community contributing guide.
