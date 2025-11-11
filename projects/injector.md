# The OpenTelemetry Injector Project

Installing an OpenTelemetry client can be a difficult process. An OpenTelemetry
client consists of a language-specific OpenTelemetry SDK plus a set of
instrumentation packages that matches the set of libraries used by the target
application. The correct set of SDK plugins also need to be installed and
configured to match the correct settings for their deployment environment.

System operators are end users who have access to deployment and management tools
for their organization's services, but do not have access to the source code or
command line invocations for those services.

Currently, system operators have very limited choices for installing OpenTelemetry clients.
There are several language-specific installation efforts supported by the
OpenTelemetry Operator, providing coverage for a limited number of use cases. Using
LD_PRELOAD, we can extend this set of use cases to six languages, and remove the
requirement that the users be running Kubernetes. Running Linux will still be a
requirement.

Note: This SIG is concerned with the OpenTelemetry Injector mechanism itself. We
will provide a proof of concept of how the injector can be delivered via system
packages. We do not believe that this SIG should maintain any system packages beyond
the scope needed for demonstrating the utility of the Injector. For the actual
packaging of OpenTelemetry, best practices should be established based on community
feedback. For example, we believe that deciding how to use the OpenTelemetry
Injector with Kubernetes should be discussed as part of the OpenTelemetry Operator
SIG.

## Background and description

LD_PRELOAD-based injection of instrumentation into application runtimes is a
technique that has been widely in use in the APM industry. It requires no elevated
security privileges (LD_PRELOAD shared objects run with the same privileges of their
host process) and is known to work in a variety of runtimes: Java, Node.js, .NET,
Python, Ruby, Elixir and PHP. LD_PRELOAD-based injection is generally not applicable
to compiled languages, like C, C++, Rust or Go (although for Go there is precedent
in commercial vendors to add instrumentations by redirecting local symbols);
however, this is a limitation of SDKs and auto-instrumentations, not of LD_PRELOAD
itself.

### Current challenges

Adopting OpenTelemetry can be a difficult task for most users without expertise in
Observability. Modifying applications to add and maintain SDKs and their setup is a
chore that most developers would rather avoid. Many practitioners – even experienced
ones – are perfectly fine starting their observability journey by using
auto-instrumentation, especially for those languages with good instrumentation
coverage and mature SDKs.

As mentioned in the overview, system operators are an important group of end users –
they have wide access to modifying service deployments in ways that would allow them
to deploy end-to-end observability faster and more completely than anyone else in
their organization. They are often the same group of people tasked with managing
many of the security concerns that can relate to telemetry.

### Goals, objectives, and requirements

The OpenTelemetry Injector can provide an easy installation experience for users
that run services on Linux-based (virtual) hosts. An “apt install opentelemetry“
experience that results in OpenTelemetry installed in every service on the box is
going to allow operators to quickly add observability using a workflow that they are
familiar with.

For kubernetes, the OpenTelemetry Operator provides an auto-instrumentation
experience. We foresee a collaboration with the OpenTelemetry Operator SIG to
deliver the injector through the operator and, in so doing, streamline the
auto-instrumentation experience. (As a matter of fact, the Injector SIG actually
started with an engagement in the OpenTelemetry Operator, which then was spun into
this dedicated SIG.)

For docker and other containerized applications, a layered-based image approach can
easily mix in the same opentelemetry packages. However, solving all of the different
approaches to packaging is not a focus for this project.

#### Goals

Create a uniform mechanism for operators as well as application developers to
install SDKs and library auto-instrumentation applicable to all applications on a
Linux host just by means of adding system packages, and support as many languages as
possible while doing so. We know from industry experience that this significantly
improves installation success at scale, especially in situations when application
developers are not readily available or willing to devote the effort to maintain
observability setups inside their applications.

In pursuit of this vision, we will provide an LD-PRELOAD object that enables
out-of-the-box, system-wide auto-instrumentation experience on Linux hosts and
containers.

We will also create a proof of concept for the structure of system packages. The
package structure should not to be monolithic, but rather separate the common
injecting concerns from the language-specific SDKs and instrumentation packages. The
packages should be arranged so that custom distributions can be provided for
specific runtimes. The Injector SIG will pick one common packaging environment and
use it to provide a reference solution to these problems.

#### Why now?

As part of "crossing the chasm" to the mainstream, OpenTelemetry needs to provide
mainstream organizations with an installation experience that either matches or
improves upon what they have come to expect from existing APM tools.

This is especially critical for organizations in which operators are in charge of
maintaining observability setups, without the ability to modify application source
code or command line invocations. Today, these users are blocked from deploying
OpenTelemetry.

This has become one of the primary limiting factors for many organizations
interested in adopting OpenTelemetry. Organizations adopt the Collector because
operators are allowed to have control over it, but they cannot deploy OpenTelemetry
SDKs and thus miss out on distributed tracing plus all of our library-level
instrumentation.

## Deliverables

We intend to deliver:
A ready-made, LD_PRELOAD injector of production quality that will work regardless of
the GNU LibC flavor used in the linked application, and be inert when the linked
application does not contain a LibC. This is already available in the
opentelemetry-injector, with one last major feature-functionality drop to be donated
by Dash0 (support for dynamically-linked binaries that do not link a LibC).

A proof of concept of system packaging for Java and Node.js OTel SDKs and
auto-instrumentations for Debian-based Linux distributions that provides the `apt
install opentelemetry` experience. We want to set up packages not to be monolithic,
but rather separate the injector concern from language-specific SDKs, and in so
doing, provide a baseline for observability vendors to build upon with their own
OpenTelemetry distributions.

A document outlining a draft of the packaging architecture outline describing how to
structure modular .deb system packages so that end users can opt into
vendor-provided distributions.

## Staffing / Help Wanted

### Industry outreach (Optional)

We (Michele) tried to reach out to Canonical for help with .deb packaging, but while
generally interested, they cannot pitch in on a short-enough notice to make the
Kubecon timeline.

### SIG

[Github Repo](https://github.com/open-telemetry/opentelemetry-injector)

[SIG Meeting](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-injector)

### Staffing

Engineering is done by the [Injector Approvers and Maintainers](https://github.com/orgs/open-telemetry/teams/injector-approvers)

### Sponsorship

#### TC Sponsor

@jack-berg (Grafana Labs)

#### Delegated TC Sponsor (Optional)

N/A

#### GC Liaison

@tedsuo (Grafana Labs)

## Expected Timeline

Our first deadline is November 10th, 2025, Observability Day co-located with
KubeCon + CloudNativeCon North America 2025.

We want to:

* Cut the first release of the OpenTelemetry injector.
* Demo a proof of concept of an `apt install opentelemetry` experience that works
  for Java and Node.js.
* Propose a first draft of the packaging architecture outline describing how to
  structure modular .deb system packages so that end users can opt into
  vendor-provided distributions.

## GitHub Project (Post-Approval)

<https://github.com/open-telemetry/opentelemetry-injector>

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

[SIG Meeting:](https://github.com/open-telemetry/community?tab=readme-ov-file#sig-injector)
