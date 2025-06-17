# OpenTelemetry Release Processes Overview

## Common Release Practices
  * **Semantic Versioning (SemVer)** is used in every repository (`vMAJOR.MINOR.PATCH`). See our [Versioning and Stability](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/versioning-and-stability.md) policy for more information.
  * CHANGELOGs keep an **“Unreleased”** section that is promoted to a versioned section during a release.
  * Releases are tagged from the default branch or a dedicated *release/x.y* branch; tags are always prefixed with **v**.
  * GitHub Actions prepare release PRs, bump versions, draft release notes, publish artifacts, and create Git tags.
  * Each release produces a GitHub Release plus language‑specific artifacts (Maven Central, NuGet, PyPI, NPM, RubyGems, crates.io, Packagist, Docker Hub, etc.).
  * A designated **maintainer or release manager** triggers/approves the workflows and verifies the release checklist.

## Common Artifact & Versioning Practices

| Aspect | Approach |
| ------ | -------- |
| **Versioning after 1.0** | No breaking changes in the 1.x line; major bump required for breaking changes. |
| **Unreleased versions** | Suffixes like `-SNAPSHOT`, `.dev`, `beta.n` are kept on `main` and stripped for the release commit. |
| **Artifact registries** | Maven Central (Java), NuGet (.NET), PyPI (Python), npmjs.com (JS), RubyGems (Ruby), crates.io (Rust), Packagist (PHP), Docker Hub (Collector/Images). |
| **Version‑bump tooling** | Gradle scripts, MinVer, `cargo release`, `npm version`, Toys scripts, Makefiles, custom GH Actions. |

---

## Release Process by SIG / Component

### Java (SIG Java)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-java | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java/blob/main/RELEASING.md) | Monthly | GitHub Actions (prepare + publish) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-java/blob/main/.github/CODEOWNERS) |
| opentelemetry-java-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/RELEASING.md) | Monthly (aligned) | GitHub Actions (partial) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/.github/CODEOWNERS) |
| opentelemetry-java-instrumentation | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/RELEASING.md) | Monthly | Gradle scripts + GH Actions | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/.github/CODEOWNERS) |

### .NET (SIG . NET)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-dotnet | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/build/RELEASING.md) | ~Every 4‑6 weeks | GH Actions + slash‑commands | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/.github/CODEOWNERS) |
| opentelemetry-dotnet-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/blob/main/build/RELEASING.md) | Monthly (aligned) | Partial automation | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/blob/main/CODEOWNERS) |
| opentelemetry-dotnet-instrumentation | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/docs/releasing.md) | Quarterly / ad‑hoc | Partial | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/.github/CODEOWNERS) |

### Go (SIG Go)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-go | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-go/blob/main/RELEASING.md) | ~Every 4‑6 weeks | Make scripts (manual) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-go/blob/main/CODEOWNERS) |
| opentelemetry-go-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/RELEASING.md) | Monthly (after core) | Partial | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/CODEOWNERS) |

### Python (SIG Python)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-python | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-python/blob/main/RELEASING.md) | Monthly | GH Actions (high) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-python/blob/main/.github/CODEOWNERS) |
| opentelemetry-python-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/RELEASING.md) | Monthly (aligned) | GH Actions (high) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/.github/CODEOWNERS) |

### JavaScript (SIG JS)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-js | [Releasing Guide](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/contributing/releasing.md) | ~Every 4‑6 weeks | Release PR + Publish workflow | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-js/blob/main/.github/CODEOWNERS) |
| opentelemetry-js-contrib | n/a | Monthly (aligned) | Partial | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-js-contrib/blob/main/.github/CODEOWNERS) |

### Ruby (SIG Ruby)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-ruby | [CONTRIBUTING → Releases](https://github.com/open-telemetry/opentelemetry-ruby/blob/main/CONTRIBUTING.md#releases) | Monthly | Toys scripts + GH Actions | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-ruby/blob/main/CODEOWNERS) |
| opentelemetry-ruby-contrib | Same as above | Monthly (aligned) | Automated with core | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-ruby/blob/main/CODEOWNERS) |

### PHP (SIG PHP)

⚠️ Needs input from PHP SIG

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-php | n/a | Monthly | GH Actions + Packagist auto‑sync | n/a |
| opentelemetry-php-contrib | Follows core | Ad‑hoc | Manual tagging | n/a |

### C++ (SIG C++)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-cpp | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/RELEASING.md) | Quarterly | Scripts (manual) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/.github/CODEOWNERS) |

### Rust (SIG Rust)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-rust | n/a | 4‑8 weeks | `cargo release` (tool‑assisted) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-rust/blob/main/.github/CODEOWNERS) |

### Swift (SIG Swift)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-swift | n/a | Bi‑monthly | Tag → SPM/CocoaPods | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-swift/blob/main/CODEOWNERS) |

### Collector (SIG Collector)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-collector | [docs/release.md](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/release.md) | Bi‑weekly | Prepare PR + GH Actions | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-collector/blob/main/.github/CODEOWNERS) |
| opentelemetry-collector-contrib | Same as core | Bi‑weekly (after core) | Prepare PR + GH Actions | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/.github/CODEOWNERS) |

### Operator & Other Components

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-operator | [RELEASE.md](https://github.com/open-telemetry/opentelemetry-operator/blob/main/RELEASE.md) | ~Monthly | GH Actions (Docker + Helm) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-operator/blob/main/.github/CODEOWNERS) |
| opentelemetry-lambda | [RELEASE.md](https://github.com/open-telemetry/opentelemetry-lambda/blob/main/RELEASE.md) | Ad‑hoc | Scripts + GH Actions | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-lambda/blob/main/.github/CODEOWNERS) |

### Specifications & Schemas

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ---------- | --------- | ---------- | ------------------- |
| opentelemetry-specification | [CHANGELOG](https://github.com/open-telemetry/opentelemetry-specification/blob/main/CHANGELOG.md) | Monthly | Manual (TC oversight) | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-specification/blob/main/.github/CODEOWNERS) |
| semantic-conventions | [RELEASING.md](https://github.com/open-telemetry/semantic-conventions/blob/main/RELEASING.md) | On demand | GH Actions (prepare) | [CODEOWNERS](https://github.com/open-telemetry/semantic-conventions/blob/main/.github/CODEOWNERS) |
| opentelemetry-proto | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-proto/blob/main/RELEASING.md) | Few times / year | Manual | [CODEOWNERS](https://github.com/open-telemetry/opentelemetry-proto/blob/main/.github/CODEOWNERS) |

---

**Tip:** Most repositories expose their release automation under **.github/workflows/**. Reading those workflow files provides the authoritative sequence of release steps if the written docs fall behind.
