# WIP OpenTelemetry Release Process

State: draft

## Versioning

* Used by opentelemetry-specification for the API version number
* Used by the language SIGs that implement the spec and they have their own versioning that can be different from the spec.
* MAJOR version when you make incompatible API changes
* MINOR version when you add functionality in a backwards compatible manner
* PATCH version when you make backwards compatible bug fixes

## Prioritization

* Option 1: priority/p0, priority/p1, priority/p2
  * E.g. priority/p0 means MUST be released in the next release
* Option 2: Just a release-blocker label: https://github.com/golang/go/labels/release-blocker
* Option 3: Priority group label without numbers: https://github.com/kubernetes/kubernetes/labels?q=priority
  * priority/critical-urgent
  * priority/important-soon
  * priority/important-longterm
  * priority/backlog
  * priority/awaiting-more-evidence

## Tracking work for future releases

* When to triage?
  * Triage as responsibility of maintainer
  * Option 1: Triage summary as part of sig mtg (may cause meeting to go overtime)
  * Option 2: Triage as set once per week
* Github Project to track the next release with a due date that is kept up-to-date.
* Optional to have a github project for patch releases; skip if emergency or small oopsie patch release (roll forward, no rollback)

## Non-core codebase

* Explanation of responsibilities of release for external community plugins.
* Explanation of which code goes into contrib versus the core repository.

## Integration and testing requirements

* Stating supported environments
  * Operating System
  * Performance requirements
  * Automated regression tests
  * Unit test coverage
  * Tests for adherence to the opentelemetry-specification release
* Maturity matrix - when to update

## Misc

These items need to be sorted.

* What role can perform the release (keeping deployment secrets accessible); suggestion for now: maintainers
* What is the release procedure and how to fix it if something goes wrong.
* Patching process (should be fastest and able to perform within 24 hrs for CVE)
* open-telemetry security contact list
* Release notes: categorization of description of what goes into the release:
  * Built from the github project if there was one representing the release.
  * At least 2 categories: bug fix, enhancement
  * Specify the opentelemetry-specification version that the release adheres to.
  * Can have more categories if not confusing e.g. https://github.com/open-telemetry/opentelemetry-js/releases
* Where to get the artifacts that each SIG should describe; and from there, pointers to system requirements, how to install, etc.
