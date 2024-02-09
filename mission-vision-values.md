<!--- Hugo front matter used to generate the website version of this page:
linkTitle: Mission, vision, and values
aliases: [/mission]
github_repo: &repo https://github.com/open-telemetry/community
path_base_for_github_subdir: tmp/community
github_project_repo: *repo
weight: -10
--->

# OpenTelemetry mission, vision, and values

## Mission

> Our overall north star as a community

OpenTelemetry's Mission: **to enable effective observability by making
high-quality, portable telemetry ubiquitous.**

## Vision

> The world we imagine for OTel end-users

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

## Engineering values

> The principles that guide our contributions

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

## Community values

> The principles that guide our interactions

The OpenTelemetry project aims to be a welcoming place where new and existing
members feel safe to respectfully share their opinions and disagreements. We
want to attract a diverse group of people to collaborate with us, which means
acknowledging that people come from different backgrounds and cultures.

There might be situations where community members act in a dubious manner. If
you have seen or experienced unacceptable behavior or anything that would make
our community less welcoming, please speak up! See
[our code of conduct](https://github.com/open-telemetry/community/blob/main/code-of-conduct.md)
for more information on how to report unacceptable behavior.

While we want to encourage everyone to express themselves in their own way,
there are some behaviors that we encourage you to adopt while interacting with
other community members.

### Act on behalf of the project

It’s no secret that a good number of maintainers of the project are employed by
companies with commercial interests in OpenTelemetry, especially vendors in the
observability space. That said, we expect community members to act in the best
interests of the project. Each member’s priorities can (and should!) align with
those of their employers so that the relationship is beneficial to all parties,
but when acting as a maintainer or contributor to the project, community members
are expected to wear the project’s hat.

### Disclose potential conflicts of interest

Even within the project, people might have different hats: a Collector
maintainer might be part of the Governance Committee, a JavaScript maintainer
might be part of the Technical Committee, and so on. When the context of your
message can be ambiguous, make it clear which hat you are using. For instance,
during a GC call, a person who is also a maintainer of the Collector might say:
“as a Collector maintainer, I believe that…, while as a GC member, I believe …”

### Assume positive intent

We all have different priorities in our daily jobs, and while some of us are
employed to work full time on OpenTelemetry, some of us are paid to improve
specific parts of the project according to the commercial interests of our
employers. When reviewing proposals, documents, or code, take the different
perspectives into consideration, but more importantly, assume positive intent:
while the proposal might seem skewed towards a specific perspective at first,
it’s very likely that the author is open to improving it if different
perspectives are provided.

### Respectfully disagree

Many decisions are made every day as part of our project. Despite giving our
best, not all decisions are the right ones. We encourage ideas and solutions to
be proposed and debated until an agreement is reached or until the “disagree and
commit” stage is reached. What we cannot tolerate is turning attacks against
ideas into attacks against people: in the heat of the moment, it might be
tempting to make an ad hominem attack but it’s always wrong. If you have reasons
to believe the person you are debating with is not acting in the interest of the
project, seek mediation instead of engaging further. While the technical merits
of the matter should be resolved within the SIG by the maintainers or, in
ultimate cases, by the Technical Committee (TC), non-technical matters should be
brought up to the Governance Committee.

### Be nice

As evidenced in [The Cultural Map](https://erinmeyer.com/books/the-culture-map/)
by Erin Meyer, people from different cultural backgrounds have different ways of
communicating. While we don’t expect you to be an expert in capturing unspoken
nuances, we expect that you be nice to other folks and that your communication
is clear without requiring the other parties to infer what’s not explicitly
written there. This includes being minimally polite while transmitting your
thoughts and keeping snarky or inappropriate comments to yourself.
