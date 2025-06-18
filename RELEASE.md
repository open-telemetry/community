# OpenTelemetry Release Processes Overview

## Common Release Practices
* **Semantic Versioning (SemVer)** is used in every repository (`vMAJOR.MINOR.PATCH`). See our [Versioning and Stability](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/versioning-and-stability.md) policy for more information.
* CHANGELOGs keep an **“Unreleased”** section that is promoted to a versioned section during a release.
* Releases are tagged from the default branch or a dedicated *release/x.y* branch; tags are always prefixed with **v**.
* GitHub Actions prepare release PRs, bump versions, draft release notes, publish artifacts, and create Git tags.
* Each release produces a GitHub Release plus language‑specific artifacts (Maven Central, NuGet, PyPI, NPM, RubyGems, crates.io, Packagist, Docker Hub, etc.).
* A designated **maintainer or release manager** triggers/approves the workflows and verifies the release checklist.

## Common Artifact & Versioning Practices

| Aspect | Approach |
| ------ | -------- |
| **Versioning after 1.0** | No breaking changes in the 1.x line; major bump required for breaking changes. |
| **Unreleased versions** | Suffixes like `-SNAPSHOT`, `.dev`, `beta.n` are kept on `main` and stripped for the release commit. |
| **Artifact registries** | Maven Central (Java), NuGet (.NET), PyPI (Python), npmjs.com (JS), RubyGems (Ruby), crates.io (Rust), Packagist (PHP), PECL (PHP), Docker Hub (Collector/Images). |
| **Version‑bump tooling** | Gradle scripts, MinVer, `cargo release`, `npm version`, Toys scripts, Makefiles, custom GH Actions. |---

## Release Process by SIG / Component

### Java (SIG Java)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-java | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java/blob/main/RELEASING.md) | Monthly | GitHub Actions (prepare + publish) | [@open-telemetry/java-maintainers](https://github.com/orgs/open-telemetry/teams/java-maintainers) |
| opentelemetry-java-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java-contrib/blob/main/RELEASING.md) | Monthly | GitHub Actions (prepare + publish) | [@open-telemetry/java-contrib-maintainers](https://github.com/orgs/open-telemetry/teams/java-contrib-maintainers) |
| opentelemetry-java-instrumentation | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-java-instrumentation/blob/main/RELEASING.md) | Monthly | GitHub Actions (prepare + publish) | [@open-telemetry/java-instrumentation-maintainers](https://github.com/orgs/open-telemetry/teams/java-instrumentation-maintainers) |

### .NET (SIG .NET)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-dotnet | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/build/RELEASING.md) | ~Every 4-6 weeks | GitHub Actions + slash-commands | [@open-telemetry/dotnet-maintainers](https://github.com/orgs/open-telemetry/teams/dotnet-maintainers) |
| opentelemetry-dotnet-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet-contrib/blob/main/build/RELEASING.md) | Monthly (aligned) | Partial automation | [@open-telemetry/dotnet-contrib-maintainers](https://github.com/orgs/open-telemetry/teams/dotnet-contrib-maintainers) |
| opentelemetry-dotnet-instrumentation | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/blob/main/docs/releasing.md) | Quarterly / ad-hoc | Partial | [@open-telemetry/dotnet-instrumentation-maintainers](https://github.com/orgs/open-telemetry/teams/dotnet-instrumentation-maintainers) |

### Go (SIG Go)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-go | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-go/blob/main/RELEASING.md) | ~Every 4-6 weeks | Make scripts (manual) | [@open-telemetry/go-maintainers](https://github.com/orgs/open-telemetry/teams/go-maintainers) |
| opentelemetry-go-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-go-contrib/blob/main/RELEASING.md) | Monthly (after core) | Partial | [@open-telemetry/go-contrib-maintainers](https://github.com/orgs/open-telemetry/teams/go-contrib-maintainers) |
| opentelemetry-go-instrumentation | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-go-instrumentation/blob/main/RELEASING.md) | ~Every 4-6 weeks | Make scripts (manual) | [@open-telemetry/go-instrumentation-maintainers](https://github.com/orgs/open-telemetry/teams/go-instrumentation-maintainers) |

### Python (SIG Python)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-python | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-python/blob/main/RELEASING.md) | Monthly | GitHub Actions (high) | [@open-telemetry/python-maintainers](https://github.com/orgs/open-telemetry/teams/python-maintainers) |
| opentelemetry-python-contrib | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-python-contrib/blob/main/RELEASING.md) | Monthly (aligned) | GitHub Actions (high) | [@open-telemetry/python-contrib-maintainers](https://github.com/orgs/open-telemetry/teams/python-contrib-maintainers) |

### JavaScript (SIG JS)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-js | [Releasing Guide](https://github.com/open-telemetry/opentelemetry-js/blob/main/doc/contributing/releasing.md) | ~bi-weekly, on-demand (after SemConv release) | Release PR + Publish workflow | [@open-telemetry/javascript-maintainers](https://github.com/orgs/open-telemetry/teams/javascript-maintainers) |
| opentelemetry-js-contrib | n/a | ~bi-weekly (after core), on-demand | GitHub Actions | [@open-telemetry/javascript-maintainers](https://github.com/orgs/open-telemetry/teams/javascript-maintainers) |

### Ruby (SIG Ruby)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-ruby | [CONTRIBUTING → Releases](https://github.com/open-telemetry/opentelemetry-ruby/blob/main/CONTRIBUTING.md#releases) | Monthly | Toys scripts + GitHub Actions | [@open-telemetry/ruby-maintainers](https://github.com/orgs/open-telemetry/teams/ruby-maintainers) |
| opentelemetry-ruby-contrib | Same as above | Monthly (aligned) | Automated with core | [@open-telemetry/ruby-maintainers](https://github.com/orgs/open-telemetry/teams/ruby-maintainers) |

### PHP (SIG PHP) ⚠️ Needs input from PHP SIG

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-php | n/a | Ad-hoc | GitHub Actions + [scripting](https://github.com/opentelemetry-php/dev-tools) + Packagist auto-sync | [@open-telemetry/php-maintainers](https://github.com/orgs/open-telemetry/teams/php-maintainers) |
| opentelemetry-php-contrib | Follows core | Ad-hoc | Follows core | [@open-telemetry/php-maintainers](https://github.com/orgs/open-telemetry/teams/php-maintainers) |
| opentelemetry-php-instrumentation | Follows core | Ad-hoc | GitHub Actions + scripting + PECL manual upload | [@open-telemetry/php-maintainers](https://github.com/orgs/open-telemetry/teams/php-maintainers) |

### C++ (SIG C++)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-cpp | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/RELEASING.md) | Quarterly | Scripts (manual) | [@open-telemetry/cpp-maintainers](https://github.com/orgs/open-telemetry/teams/cpp-maintainers) |

### Rust (SIG Rust)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-rust | n/a | 4-8 weeks | `cargo release` (tool-assisted) | [@open-telemetry/rust-maintainers](https://github.com/orgs/open-telemetry/teams/rust-maintainers) |

### Swift (SIG Swift)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-swift | n/a | Bi-monthly | Tag → SPM/CocoaPods | [@open-telemetry/swift-maintainers](https://github.com/orgs/open-telemetry/teams/swift-maintainers) |

### Collector (SIG Collector)

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-collector | [docs/release.md](https://github.com/open-telemetry/opentelemetry-collector/blob/main/docs/release.md) | Bi-weekly | Prepare PR + GitHub Actions | [@open-telemetry/collector-maintainers](https://github.com/orgs/open-telemetry/teams/collector-maintainers) |
| opentelemetry-collector-contrib | Same as core | Bi-weekly (after core) | Prepare PR + GitHub Actions | [@open-telemetry/collector-contrib-maintainers](https://github.com/orgs/open-telemetry/teams/collector-contrib-maintainers) |
| opentelemetry-collector-releases | Same as core | Bi-weekly (after contrib) | Prepare PR + GitHub Actions | [@open-telemetry/collector-maintainers](https://github.com/orgs/open-telemetry/teams/collector-maintainers) |

### Operator & Other Components

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-operator | [RELEASE.md](https://github.com/open-telemetry/opentelemetry-operator/blob/main/RELEASE.md) | ~Monthly | GitHub Actions (Docker + Helm) | [@open-telemetry/operator-maintainers](https://github.com/orgs/open-telemetry/teams/operator-maintainers) |
| opentelemetry-lambda | [RELEASE.md](https://github.com/open-telemetry/opentelemetry-lambda/blob/main/RELEASE.md) | Ad-hoc | Scripts + GitHub Actions | [@open-telemetry/lambda-maintainers](https://github.com/orgs/open-telemetry/teams/lambda-maintainers) |

### Specifications & Schemas

| Repository | Release Doc | Frequency | Automation | Release Maintainers |
| ---------- | ----------- | --------- | ---------- | ------------------- |
| opentelemetry-specification | [CHANGELOG](https://github.com/open-telemetry/opentelemetry-specification/blob/main/CHANGELOG.md) | Monthly | Manual (TC oversight) | [@open-telemetry/specification-maintainers](https://github.com/orgs/open-telemetry/teams/specification-maintainers) |
| semantic-conventions | [RELEASING.md](https://github.com/open-telemetry/semantic-conventions/blob/main/RELEASING.md) | On demand | GitHub Actions (prepare) | [@open-telemetry/specs-semconv-maintainers](https://github.com/orgs/open-telemetry/teams/specs-semconv-maintainers) |
| opentelemetry-proto | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-proto/blob/main/RELEASING.md) | On demand | Manual | [@open-telemetry/proto-maintainers](https://github.com/orgs/open-telemetry/teams/proto-maintainers) |
| opentelemetry-proto-go | [RELEASING.md](https://github.com/open-telemetry/opentelemetry-proto-go/blob/main/RELEASING.md) | On demand after proto | Make scripts (manual) | [@open-telemetry/proto-go-maintainers](https://github.com/orgs/open-telemetry/teams/proto-go-maintainers) |
| weaver | [CONTRIBUTING.md](https://github.com/open-telemetry/weaver/blob/main/CONTRIBUTING.md#creating-a-new-release-for-the-weaver-project) | ~ Every 4-6 weeks | [@open-telemetry/weaver-maintainers](https://github.com/orgs/open-telemetry/teams/weaver-maintainers) |

---

**Tip:** Most repositories expose their release automation under **.github/workflows/**. Reading those workflow files provides the authoritative sequence of release steps if the written docs fall behind.
