---
name: TC Review Request
about: Request a Technical-Committee stability review (promotion to Stable/GA)
title: "TC Review Request: "
labels: "area/stability"
assignees: ""
---

<!--
Delete the guidance comments after filling in the form.
-->

# TC Review Request: <Component / Language> <Signal> (API / SDK / Collector-module)

## 1. Promotion scope
| Signal | Part of project | Current maturity | Target maturity |
| ------ | -------------- | ---------------- | --------------- |
| <Tracing \| Metrics \| Logs \| Profiles> | <API / SDK package / Other> | experimental / beta | **stable (GA)** |

## 2. Motivation
<Why are you requesting GA now? Adoption stats, user demand, risk mitigation, etc.>

## 3. Target version / tag
`<org>/<repo>@<tag>` – commit `<sha>`

## 4. Links for reviewers
* **Spec-compliance checklist:** <link>
* **Compatibility matrix (if any):** <link>
* **Public docs / getting-started sample:** <link>
* **CHANGELOG draft:** <link>
* **Open spec gaps referenced:**
  * open-telemetry/opentelemetry-specification#NNNN – <summary>

## 5. Self-checklist
- [ ] All **MUST / MUST_NOT** requirements implemented
- [ ] [Spec Compliance Matrix](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md) populated and up-to-date
- [ ] Public API surface frozen & annotated as **Stable**
- [ ] Docs & examples updated
- [ ] CI green on **main** and on the release tag above
- [ ] ≥ 1 beta/RC used in production for ≥ 4 weeks
- [ ] CHANGELOG & version bump prepared

## 6. Maintainer points-of-contact
- @<handle> – SIG lead / shepherd
- @<handle> – backup

## 7. Requested reviewer expertise
<e.g., “Metrics SDK spec”, “Collector pipeline”, “Logs data-model”>

/cc @open-telemetry/technical-committee
