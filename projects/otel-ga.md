# OpenTelemetry GA: Completing our initial scope of work

This project file identifies the remaining workstreams needed to complete delivery of the
initial scope of work for OpenTelemetry: A telemetry system that delivers tracing,
metrics, and logs from the most common software libraries and cloud infrastructures.

NOTE: This is a meta-project. It describes a set of workstreams at a high level, so that we can
agree upon the overall scope of work needed for OpenTelemetry to be considered GA or "generally
available." For that reason, it is missing some sections that would normally be in a project
file. In the future we should develop better road-mapping tools, but this is what we have today.

## Background and description

As part of the [due diligence](https://github.com/cncf/toc/blob/main/projects/open-telemetry/otel-graduation-dd.md)
for OpenTelemetry's graduation, a scope of work was identified as required in order
for OpenTelemetry to be considered "stable" or "generally available."

The feedback on the initial proposal was that it was too open-ended, so this project attempts
to redefine workstreams to be more specific as to which SIG is indented to work on them, and
the concrete set of deliverables needed for OpenTelemetry to be considered GA.

## Current challenges

### De facto stable

Today, many components are "de facto" stable, meaning that they are versioned as 0.X and are
technically still in beta, but are recommended to be used in production. This is confusing, as
OpenTelemetry also has components marked 0.X that are genuinely experimental and should not be
used in production. Additionally, some end user organizations have rules that prohibit them
from deploying 0.X software to production.

As part of graduation, it was requested that we provide a mechanism for indicating to end
users which OpenTelemetry components are "production ready." Actually, we already have a
mechanism for indicating this – the version number of the component. Going forward, we need to
align "production readiness" with bumping a component to v1.0 or greater.

In practice, this means finalizing the v1.0 roadmap for every component necessary for
OpenTelemetry to be considered generally available.

### Deploying at scale

While there is a way to install every individual component in OpenTelemetry, we do not
currently have tools that can install and manage all of OpenTelemetry at scale. We have the
beginnings of these tools for Kubernetes and Linux, but they are not complete, and can only
manage a portion of the OpenTelemetry components needed for a complete deployment.

### Future-proofing

We've made it this far, but there are several aspects of the project that need to be improved
in order continue maintaining OpenTelemetry after GA. The specific areas that were identified
include security, project management, performance, and long term support.

## Workstreams

Based on the above challenges, there following workstreams need to be developed and managed as
a roadmap to GA that can be presented to the community.

### Stability: Collector v1.0

Managed by Collector SIG, the OpenTelemetry Collector needs to complete its roadmap for v1.0.

### Stability: SemConv Tooling for managing instrumentation

In order to lower the cost of manage instrumentation at scale, and to better support native
instrumentation efforts, we need tooling that improves correctness while reducing the cost of
maintaining instrumentation.  The SemConv Tooling SIG is in charge of this project.

* Weaver
* AI coding
* Test harnesses

### Stability: Instrumentation

The biggest barrier to general availability is unstable instrumentation.

* Move away from the “community contrib” model for critical instrumentation packages.
* Deploy the new SemConv tooling across all language ecosystems.
* Badges and other forms of recognition
* Native instrumentation push to move instrumentation out of OpenTelemetry.

### Deployment: OpAMP v1.0

In order to manage OpenTelemetry at scale, we need a control plane. Therefore, OpAMP needs
to be stable and feature complete for its core set of management tasks.

The OpAMP SIG is in charge of this project.

### Deployment: Packaging v1.0

The Packaging SIG is in charge of this project.

* Official packages for Debian and RHEL
* Cross language definitions for distributions and versioning
* Language distributions for SDKs, plugins, and instrumentation
* Declarative configuration for managing instrumentation and stability

### Deployment: Kubernetes Operator v1.0

The Kubernetes Operator needs several features in order to make OpenTelemetry generally
available on Kubernetes. Operator SIG is in charge of this project.

* The need for pod attribution and other manual configuration requirements that interfere
  with deploying OpenTelemetry at scale.
* All major languages supported.
* Works with the same distributions and configuration options as developed by the package
  management SIG, so that end users only need to learn a single set of configuration patterns.

### Security

While project-wide security protocols can always be improved. The following tasks have been
identified as high priority. The Security SIG is in charge of this project.

* Better staffing of the Security SIG.
* Triage that can keep up with AI-powered CVE reporting noise.
* Oversight to ensure that security response protocols are being followed.
* OTel scanning tools to counter noisy and inaccurate scanning tools used by end users.

### Roadmaps & Project Management

While OpenTelemetry has been making many incremental improvements to its project management
tools and workflows, we have identified a need for larger changes to our project structure.

OpenTelemetry always had a de-facto roadmap – first traces, then metrics, then logs. That
roadmap is now complete. Once we have delivered this final set of work needed to make the
original goals generally available, the roadmap is now unwritten. How will we write it as
a community?

The Governance Committee is in charge of this project, but everyone's input is needed.

* More agency and responsibility for the roadmap in the hands of the maintainers.
* Better ways to socialize the projects that need input.
* Better ways to visualize the long term roadmap.

## Out of scope

There is additional work that we see as necessary for the success of the project. However, in
order to stay focused as a community, we must limit the number of large projects that we take
on at any one time – we cannot ask maintainers to have five or six "number one priorities."

The following projects are seen as important for the long term success of OpenTelemetry, but
not actually necessary to deliver stable components that are deployable at scale.

### Performance / Benchmarking

OpenTelemetry maintainers are always encouraged to continue optimizing the performance
of the code that they are in charge of.

### Long term support

The primary goal of this initiative is to get all of the necessary components to v1.0.
OpenTelemetry does have compatibility and support requirements for various types of
components, such as APIs and plugin architectures. Once we have reached this milestone, we
can revisit our compatibility requirements and long term support guarantees.

### Better designs and architecture

The core specification for tracing, metrics, and logs have all been completed. However, we
are always learning. It's reasonable that we may want to revisit these designs, either to
incorporate new developments within the industry, or to address fundamental performance issues.

Let's finish shipping v1.0 first, before distracting ourselves with v2.0.
