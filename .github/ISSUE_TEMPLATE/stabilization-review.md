---
name: TC Review Request
about: Request a Technical Committee stability review (promotion to Stable)
title: "TC Review Request: "
labels: "area/stability"
assignees: ""
---

<!--
Delete the guidance comments after filling in the form.
-->

# TC Review Request: <Component / Language> <Signal> (API / SDK / Collector-module)

## 1. Review scope
| Signal | Part of project | Current maturity | Target maturity |
| ------ | --------------- | ---------------- | --------------- |
| <Tracing \| Metrics \| Logs \| Profiles> | <API / SDK package / Other> | experimental / beta | **stable** |

## 2. Motivation
<Why are you requesting stability now? Adoption stats, user demand, risk mitigation, etc.>

## 3. Target version / tag
`<org>/<repo>@<tag>` – commit `<sha>`

## 4. Links for reviewers
* **Spec compliance matrix:** <link to documentation of how your implementation meets each spec requirement>
  <!--
  Example compliance matrix format:

  ### Spec compliance matrix (Metrics SDK, spec @ 87c4a7f)

  | § | Requirement (paraphrased) | Status | Notes / Links |
  |---|---------------------------|--------|---------------|
  | 6.1.1 | MeterProvider **MUST** be safe for concurrent use | ✅ | Covered by mutex in meter_provider.go#L45 |
  | 6.1.2 | MeterProvider **MUST** return same Meter for identical name | ✅ | unit test `TestSameMeter` |
  | 6.3.1 | SDK **MUST** implement PeriodicReader | ✅ | pkg/metric/reader/periodic_reader.go |
  | 6.3.2 | SDK **SHOULD** implement ManualReader | ❌ | Tracked in #1234; planned before GA |
  | 6.12 | **MUST_NOT** drop data on forced shutdown | ✅ | integration test `TestForceFlush` |
  | … | … | … | … |
  -->
* **Public docs / getting-started sample:** <link>
* **CHANGELOG draft:** <link>

<!--
Notes on the self-checklist:

It is ideal to perform a stabilization review before a release candidate is generated.
-->

## 5. Self-checklist
- [ ] All **MUST / MUST NOT** requirements implemented
- [ ] [Spec compliance matrix](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md) populated and up-to-date
- [ ] Docs & examples updated
- [ ] Test suites passing
- [ ] CHANGELOG prepared

## 6. Maintainer points-of-contact
- @<handle> – SIG lead / primary contact
- @<handle> – backup

## 7. Requested reviewer expertise
<e.g., "Metrics SDK spec", "Collector pipeline", "Logs data-model">

/cc @open-telemetry/technical-committee
