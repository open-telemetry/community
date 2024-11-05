## Description

Quite a few of our users are happy using a non-v1 Collector, as evidenced by talks delivered by eBay or VTEX. On the other hand, other companies have internal policies forbidding the usage of software that hasn’t reached v1.

Other companies, hearing the success stories of the “early adopters”, tried to use the Collector, but due to a lack of guidance, ended up using components that weren’t ready for prime time and were frustrated.

Our main goal with this project is to define what's the scope for Collector v1, defining which use-cases we want to satisfy first, followed by stabilizing the components that are required for that. Once we are there, we'll focus on documentation for those components and use cases.

We believe we are close to a v1 of the Collector, given that users are using it in production already. Therefore, we are confident we can deliver a v1 in 2024.

Teams involved in this:

* @open-telemetry/collector-approvers 
* @open-telemetry/collector-contrib-approvers 
* @open-telemetry/collector-maintainers 
* @open-telemetry/collector-contrib-maintainer 
* @open-telemetry/docs-maintainers
* @open-telemetry/docs-approvers
 
### Project Board

To be created.

### Deliverables

The current goal (subject to change) is to have deliverables covering our two current distributions: core and contrib. Deliverables should be linked from the main opentelemetry.io website. 

#### Must-haves
* Binaries for Windows, MacOS, and Linux for amd64 and x86
* Multi-arch container images

#### Nice to have
* OS-specific packages for Linux (deb, rpm, …) and Macos (homebrew)

### Staffing / Help Wanted

@jpkrohling is the GC sponsor for this and has the buy-in from other Collector leaders, including core and contrib approvers/maintainers (listed above).

### Meeting Times

For the public discussions, we are using the Collector SIG meeting slot.

### Timeline

To be defined, but this project should be completed in 2024.