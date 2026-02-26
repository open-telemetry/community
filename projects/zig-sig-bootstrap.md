# Bootstrap Zig Special Interest Group

## Background and description

Zig is a general-purpose programming language designed for performance, robustness, and clarity.
One of Zig's key features is its seamless interoperability with C, making it a compelling choice for systems programming. 
Zig code can compile to C and eBPF natively, and it speaks the C ABI without the need for bindings or FFI layers.
Zig is already used in OpenTelemetry in the [opentelemetry-injector](https://github.com/open-telemetry/opentelemetry-injector) project.

This project is the continuation of what proposed in #2514.
Over the past year, a handful of people have dedicated time to develop a working SDK and this proposal aims at making Zig an officially supported language in OpenTelemetry.
By doing so, we would enable two distinct developer communities:

1. **Zig developers**: A growing community building systems software, web services, games and low-latency applications
2. **C developers**: Who can leverage the Zig OpenTelemetry implementation directly through C ABI compatibility

The aforementioned work-in-progress SDK implementations exist at [zig-o11y/opentelemetry-sdk](https://github.com/zig-o11y/opentelemetry-sdk), demonstrating community interest and initial technical feasibility.
A complementary Semantic Convention library is developed at [zig-o11y/opentelemetry-semconv](https://github.com/zig-o11y/opentelemetry-semconv).
However, these efforts are fragmented and lack official OpenTelemetry support, governance, and long-term maintenance commitments.

### Current challenges

**Lack of Official OpenTelemetry Support for Zig and C:**
- Zig developers currently have no official OpenTelemetry SDK, forcing them to use wrappers around the C++ implementation, use foreign language bindings or forgo observability altogether
- C developers lack a modern, actively maintained OpenTelemetry implementation that follows current specification versions
- Existing unofficial implementations are fragmented and not coordinated under OpenTelemetry governance

**Fragmented Community Efforts:**
Multiple independent implementations lead to duplicated effort and inconsistent quality.
Without official SIG coordination, these efforts may diverge from OpenTelemetry specifications and there is no clear path for Zig/C developers to contribute to or adopt OpenTelemetry.

### Goals, objectives, and requirements

The primary goal of this project is to bootstrap a Zig SIG that will create and maintain an official OpenTelemetry implementation for the Zig programming language, with initial deliverables focused on establishing a compliant, production-ready SDK.

**Specific Objectives**

1. **Create OpenTelemetry API for Zig** covering stable signals: baggage, traces, metrics, and logs
2. **Implement OpenTelemetry SDK** providing the official implementation for signal collection, processing, and export
3. **Provide continued support to Semantic Conventions library** enabling consistent instrumentation across Zig applications
4. **Establish C ABI compatibility layer** allowing C developers to use the Zig implementation seamlessly
5. **Create comprehensive documentation** including API references, usage guides, and examples for both Zig and C developers
6. **Build test infrastructure** ensuring specification compliance and compatibility across Zig versions

**Requirements**

- Compliance with OpenTelemetry specification v1.48 (precise version is TBD based on timeline)
- Support for current stable Zig version (0.15.2 at time of writing) with commitment to track language releases
- Cross-platform support (Linux, macOS, Windows)
- Zero-dependency core implementation where possible, with minimal dependencies for exporters
- C ABI compatibility verified through examples and tests
- Documentation with code examples

_Note_: some of the above are already implemented in the un-official SDK.

**Motivation for Starting Now**

- Zig adoption is growing, particularly in systems programming and infrastructure domains where observability is critical
- Possibility to onboard C developers with an OpenTelemetry solution

**Benefits to OpenTelemetry**

- Extends OpenTelemetry reach to Zig and C developer communities
- Demonstrates OpenTelemetry's versatility across diverse programming language paradigms
- Creates potential for novel integration patterns through Zig's C/eBPF compilation capabilities
- Establishes a foundation for future work in eBPF-based auto-instrumentation using Zig

## Deliverables

This project will deliver the following components, organized by priority:

**1. Formation of a SIG**
- Scout for additional community member interested in supporting the language
- Create documents and recurring meetings

**2. OpenTelemetry API for Zig**
- Trace API implementing the specification
- Logs API implementing the specification
- Metrics API implementing the specification
- Context propagation and baggage APIs
- C header exports for all APIs

**3. Core SDK Implementation**
- Tracer Provider and Span Processor implementations
- Meter Provider and aggregation implementations
- Logger Provider implementation
- Resource detection and configuration
- OTLP exporter (HTTP and gRPC)

## Expected responsibilities

Once formed, the future work of the SIG will be to adhere to the practice existing for other supported language, including:

- build and distribution infrastructure
- stabilize the Semantic Conventions library
- develop exporters supported in other languages
- publish API documentation (generated from code)
- produce user guide covering installation, basic usage, and configuration
- provide example applications for Zig (HTTP server, CLI tool)
- provide example C applications demonstrating C ABI usage
- performance benchmarks
- security audit of implementation
- create a production deployment guide
- maintain versioning and compatibility policy
- create the first stable release (v1.0.0)

## Staffing / Help Wanted

### Industry outreach

The following communities and companies should be made aware of this effort:

**Communities:**
- Zig Software Foundation and core Zig community
- Systems programming communities using C who could benefit from OpenTelemetry observability
- eBPF Foundation members working on observability tooling
- OpenTelemetry language SIG maintainers for cross-SIG collaboration

**Companies Known to Use Zig:**
- Tigerbeetle (distributed financial transactions database)
- Bun (JavaScript runtime, acquired by Anthropic)
- ZML (Machine Learning platform)
- LightPanda (AI agent browser)
- Various infrastructure and systems programming companies in the Zig community

Outreach will be conducted through:
- Announcement in Zig Discord and community forums
- Blog post on OpenTelemetry website upon project approval
- Presentation at CNCF TAG Observability or related events
- Engagement with companies in the Zig ecosystem through direct contact

### SIG

#### Project Lead(s)

The following individuals have expressed interest and commitment to leading this project:

- **@inge4pres** (Francesco, Elastic) - Project initiator, maintainer
- **@kmos** - (Giovanni, Read Hat) Maintainer
- **@hendriknielaender** (Hendrik, Taxdoo Gmbh) Maintainer
- **@kakkoyun** (Kemal, DataDog) - Supporting lead
- **@jaronoff97** (Jacob, Tero) - Supporting lead

These individuals will become SIG maintainers upon project approval.

#### Contributors

We haven't had continued external contributions that haven't turned into maintainer roles.
We hope that by making Zig support official, more contributors will step in.

**Additional Contributors Sought:**
- Engineers with Zig experience willing to contribute to SDK implementation
- C developers who can test and validate C ABI compatibility
- Documentation writers for user guides and examples
- Developers with eBPF experience for future auto-instrumentation work

**Cross-SIG Review (for future OTEPs if needed):**
- If specification changes are proposed, maintainers from at least two other language SIGs will be recruited for prototype review
- Initial implementation will follow existing specifications, minimizing this requirement

### Sponsorship

#### TC Sponsor

**[TO BE DETERMINED]**

This project requires a TC sponsors who can provide at minimum "Guiding" level sponsorship to help align the SIG's efforts with OpenTelemetry's technical goals.
We're actively looking for a sponsor.

#### GC Liaison

**[TO BE DETERMINED]**

This project requires a GC liaison to facilitate SIG health and ensure the project scope remains aligned with the proposal.

Desired liaison characteristics:
- Familiarity with SIG formation and governance processes
- Ability to participate in quarterly check-ins
- Interest in growing the OpenTelemetry ecosystem

_Note_: @svrnm has already engaged in issue #2514, may be a potential liaison

### Zig Version Compatibility Strategy

Given that Zig is pre-1.0 and breaking changes occur between releases, the SIG will:
- Target the latest stable Zig release at time of development
- Commit to updating for new Zig releases within 4 weeks of release
- Maintain compatibility with at minimum the current and previous Zig version
- Document Zig version compatibility clearly in README and releases
- Use CI to test against multiple Zig versions
- After Zig 1.0 is released, adopt a more stable compatibility policy

This maintenance burden is acknowledged and accepted by the project leads as part of the commitment to this SIG.

## References

- Issue #2514: [Zig SIG: current level of interest?](https://github.com/open-telemetry/community/issues/2514)
- Zig Programming Language: https://ziglang.org
- Existing implementations:
  - https://github.com/zig-o11y/opentelemetry-sdk
  - https://github.com/zig-o11y/opentelemetry-semconv
  - https://github.com/zig-o11y/opentelemetry-proto

## License and copyright

The existing implementations mentioned above have a MIT license and the copyright holders are willing to donate them to CNCF.
