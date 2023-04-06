<!--- Hugo front matter used to generate the website version of this page:
linkTitle: Mission, vision, and values
aliases: [/mission]
github_repo: &repo https://github.com/open-telemetry/community
github_subdir: ''
path_base_for_github_subdir:
  from: content/en/community/mission\.md
  to: mission-vision-values.md
github_project_repo: *repo
weight: -10
--->

# OpenTelemetry mission, vision, and values

## Mission &mdash; our overall north star as a community

OpenTelemetry's Mission: **to enable effective observability by making
high-quality, portable telemetry ubiquitous.**

## Vision &mdash; the world we imagine for OTel end-users

Effective observability is powerful because it enables developers to innovate
faster while maintaining high reliability. But effective observability
absolutely requires high-quality telemetry – and the performant, consistent
instrumentation that makes it possible.

Telemetry in this context is the firehose of raw observational data streaming
out of software applications, and while “high-quality telemetry” may be a
requirement for excellent observability, it’s still unreasonable and unrealistic
to expect developers of application software to add or maintain the necessary
instrumentation on their own. That is a massive undertaking, and in practice
it’s not “just code” – there is also necessary alignment around protocols and
semantic conventions for tags, attributes, and other metadata to consider.

So how do we get high-quality, turnkey telemetry without a massive,
unsustainable engineering effort? This is where OpenTelemetry comes in. To
achieve our vision, OpenTelemetry sees five key opportunities, listed here:

### Telemetry should be easy

With OpenTelemetry we want high-quality telemetry to be easy, especially for
end-users. That means that OpenTelemetry should have fast time-to-value, set
reasonable defaults yet allow for customization, and pair with excellent
documentation and a top-tier overall developer experience.

### Telemetry should be universal

Telemetry protocols and conventions should be unified across languages and
signal types (tracing, metrics, logging, etc), not divergent or siloed. This
means that OpenTelemetry aspires to find technical solutions that work
consistently, both locally and globally.

### Telemetry should be vendor-neutral

For decades, proprietary drop-in agents from monitoring and observability
vendors have been the primary source for useful telemetry from across the
application stack. Unfortunately, the lack of common standards or APIs across
these agents has led to vendor lock-in for customers, and inhibited innovation
by tightly coupling telemetry collection with telemetry storage and analysis.
With OpenTelemetry, we strive to provide a level playing field for all
observability providers, avoid lock-in to any vendor, and interoperate with
other OSS projects in the telemetry and observability ecosystem.

### Telemetry should be loosely coupled

OpenTelemetry end-users should be able to pick and choose from the pieces they
want without bringing in the rest of the project. To enable this,
OpenTelemetry’s software architecture is decoupled wherever possible. As a
corollary, this also means that OpenTelemetry does not want to “pick winners”
when it comes to particular projects or technologies: where possible, we prefer
to give our end-users a choice.

### Telemetry should be built-in

Historically, telemetry was something developers integrated manually or via
post-compilation agents. OpenTelemetry believes that high-quality telemetry can
be built in to the entire software stack – just like comments are today.

While the structure and technical details of OpenTelemetry may change over time,
these five key opportunities will remain outstanding until we achieve our
mission, and as a project we refer to them to orient – and reorient – as we
chart our path.

## Engineering values &mdash; the principles that guide our contributions

OpenTelemetry’s mission and vision describe where we want to go. OpenTelemetry’s
engineering values describe how we want to get there.

OpenTelemetry’s core engineering values are _compatibility_, _stability_,
_resiliency_, and _performance_.

### We value _compatibility_

Given the number of stakeholders and supported platforms, following
specifications and enabling interoperability is very important. OpenTelemetry
strives to be standards-compliant, vendor-neutral, and consistent across
languages and components.

### We value _stability_

As many libraries take dependencies on OpenTelemetry APIs, API stability and
backwards compatibility is vital for our end-users. As a corollary, we do not
introduce new concepts unless we’re confident they’re needed by a broad subset
of OpenTelemetry’s end-users.

### We value _resilience_

In OpenTelemetry we value technical resiliency: the ability to adapt and to
continue operating even in the face of resource scarcity or other environmental
challenges. OpenTelemetry is designed to work and keep collecting telemetry
signals when an application is misbehaving, and OpenTelemetry code is designed
to degrade gracefully as needed.

### We value _performance_

OpenTelemetry users should not have to choose between high-quality telemetry and
a performant application. High performance is a requirement for OpenTelemetry,
and unexpected interference effects in the host application are unacceptable.
