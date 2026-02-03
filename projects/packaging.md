# OpenTelemetry System Packaging

The goal of the Packaging SIG is to provide a product-like, idiomatic experience to provide a seamless experience of monitoring applications running on (virtual) hosts through a combination of the [OpenTelemetry Injector](https://github.com/open-telemetry/opentelemetry-injector) injecting SDKs and autoinstrumentation packages, [OpenTelemetry eBPF Instrumentation (OBI)](https://github.com/open-telemetry/opentelemetry-ebpf-instrumentation), and the OpenTelemetry Collector.

This SIG takes over and continues work about system packaging started in the Injector SIG (see [project](https://github.com/open-telemetry/community/pull/3097)), joining forces with the OBI SIG to provide a cohesive experience and better coverage for the various application runtimes.
The ultimate goal is to provide an excellent experience via:

```shell
{apt|yum} install opentelemetry
```

**Note:** Due to the predominance of adoption of Linux as the “Cloud computing” OS, and specifically Debian and Red Hat distributions, the SIG focuses on system packages for the DEB and RPM ecosystem. Windows is an OS that we acknowledge also needs a simple OpenTelemetry experience, but it is out of the initial scope for reasons of priorities, bandwidth and lack of expertise in the founding members of the SIG.

**Note:** The deliverables of the Profiler SIG would likely also benefit from being packaged. This is out of scope for the foreseeable future for reasons of priorities and bandwidth in the founding members of the SIG.

## Background and description

### Current challenges

Adopting OpenTelemetry can be a difficult task for most users without significant expertise in observability. Modifying applications to add and maintain SDKs and their setup is a chore that most developers would rather avoid. A lot of practitioners, and especially those without expert-level skills in observability (which is the overwhelming majority of people out there needing observability) are perfectly fine starting their observability journey by using auto-instrumentations, especially for those languages with good instrumentation coverage and mature SDKs.

Packaging OBI, the OpenTelemetry Injector and autoinstrumentations in system packages, modular and well integrated with the existing OpenTelemetry Collector system packages, will provide an easy, satisfactory experience for users needing to monitor applications running on Linux-based (virtual) hosts. An {apt|yum} install opentelemetry experience that results in non-containerized applications monitored out of the box is going to allow ops personas to gain observability with a workflow they are familiar with, and to be able to “deploy OpenTelemetry at scale” with tools they already use in their workflows.

### Goals, objectives, and requirements

#### Goals

* Create the infrastructure to publish APT and RPM repositories for OpenTelemetry system packages.
  * We would love to explore publishing the packages in universe (Debian, Ubuntu) and EPEL (RHEL) repositories, as opposed to creating separate repositories; but we acknowledge that, as long as the packaging and associated policies are mature, we will likely need to host OpenTelemetry-specific package repositories.
* Publish modular, well-integrated system packages for:
  * OBI
  * OpenTelemetry Injector
  * SDK+autoinstrumentation for Java, .NET, Node.js and Python (with potentially Python and Ruby if bandwidth allows)
* Make the existing OpenTelemetry Collector system packages from the [Releases repository](https://github.com/open-telemetry/opentelemetry-collector-releases) in the APT and RPM repositories.
* Define versioning policies and how they align with the packaging versioning policies of Debian, Ubuntu and Red Hat.
* Extensible to vendor packages: It should be possible for vendor system packages to provide alternatives to upstream system packages, especially for collector and autoinstrumentation system packages.
* Make [declarative configuration](https://github.com/open-telemetry/opentelemetry-configuration) a first-class citizen of the system packages.

#### Why now?

We feel OpenTelemetry needs to provide a more product-like, batteries-included experience to newcomers, especially operators used to the ease of adoption of some proprietary vendors. This is especially critical for organizations in which operators are in charge of maintaining observability setups, without the ability of modifying single applications. We want to make the experience of getting library-level telemetry from autoinstrumentations straightforward and seamless.

#### Requirements

* **Enterprise-ready:** The OpenTelemetry package repositories must be easy to add a trusted package repository to the Linux system.
* **Easy mode is easy:** `{apt|yum} install opentelemetry` and some lightweight configurations in `/etc` should be all the user needs to do to set up autoinstrumentation of the applications running on the system.
**Note:** There is much more we could do to configure the collector, e.g., automatically set up syslog / journald receivers, host resource detectors, and more. But that is outside the current scope.
* **Cohesive:** OBI and the Injector need to “play nice together,” to avoid double instrumentation of processes that both support. Whether OBI or the Injector have precedence over one another, or whether they are “alternatives” (as in: packages that cannot be installed at the same time, but fulfill the requirement set out by the same meta-package) is TBD.
* **Extensible to vendor packages:** It should be possible for vendor system packages to provide alternatives to upstream system packages, especially for collector and autoinstrumentation system packages.
* **Declarative configuration:** OBI and the SDKs injected by the OpenTelemetry Injector should default to using declarative configuration.
* **Packaging best practices:** The system packages must adhere to the best practices set out by the ecosystem in terms of modularity, uninstall, interdependencies, licensing metadata, etc.
* **Filesystem Hierarchy Standard (FHS):** The system packages need to respect the best practices set out by the FHS, both in terms of executable files and configurations.
* **Collector:** The system packages for OBI and the Injector should be aware whether a Collector system package is also installed, and preferentially route telemetry through it.
* **Stretch goals:**
  * Ruby support via the Injector
  * PHP support via the Injector
  * Useful MAN pages

#### Benefits

Idiomatic, dead-simple process to set up the monitoring of applications running in Linux virtual hosts with the same tooling used to deploy (most of) the software to monitor.
The Injector and AutoInstrumentation packages would likely also be reusable while building container images, but that is not a primary goal at this time.

## Deliverables

TODO

## Staffing / Help Wanted

[`@mmanciop`](https://github.com/mmanciop) (Dash0): DEB system packages, injector

TODO

### Industry outreach (Optional)

[`@mmanciop`](https://github.com/mmanciop) tried to reach out to Canonical for help with DEB packaging, but while generally interested, they have not committed to helping.

Need more expertise in packaging RPM, right now the expertise in the SIG is mostly with DEB

### SIG

otel-packaging

### Staffing

TODO

### Sponsorship

See [Project Sponsorship](/project-management.md#project-sponsorship)

#### TC Sponsor

Name of TC sponsor

#### Delegated TC Sponsor (Optional)

Name of delegated TC sponsor

#### GC Liaison

Ted Young

## Expected Timeline

TODO

## Labels (Optional)

*Issues should be properly labeled to indicate what parts of the specification it is focused on. List here the labels applicable to this project, and consider adding them to corresponding GitHub Project automation to include them automatically into the project backlog.*

## GitHub Project (Post-Approval)

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

Repo: TODO

SIG Meeting

