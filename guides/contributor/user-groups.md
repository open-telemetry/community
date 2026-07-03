# OpenTelemetry User Groups

OpenTelemetry is used across an enormous range of industries, domains, and
environments — far more than the project's official structures can or should
track directly.

Making something *official* in OpenTelemetry, like forming a
[SIG](https://github.com/open-telemetry/community/blob/main/community-members.md),
starting a new project, or donating code under the
[project management](https://github.com/open-telemetry/community/blob/main/project-management.md)
and [donation](https://github.com/open-telemetry/community/blob/main/guides/contributor/donations.md)
guidelines, is deliberately a heavy process with real requirements. That
weight is necessary: once something is official, the project has to treat it as
such and maintain it, and everyone on the outside will treat it as canonical
OpenTelemetry work.

**OpenTelemetry User Groups** (OUGs) are the low-friction alternative. They let people who share an
interest in a particular slice of the OpenTelemetry world find each other and
self-organize as part of the **ecosystem**, without becoming part of the
**core**. There's no application and nothing to get approved. We want these
groups to exist, and this page explains how to start one and what help is
available from the project.

## What is a User Group?

An OUG is an informal, self-organized community of people interested
in a specific theme within the OpenTelemetry ecosystem: a place where interest
can gather, people can compare notes, and ideas can grow.

Good examples of themes for a User Group:

- An **industry or vertical** — e.g. OpenTelemetry in healthcare, finance,
  telco, or automotive, where adopters share domain-specific practices and
  constraints.
- A **class of technology or environment** — e.g. OpenTelemetry for databases,
  or on embedded and resource-constrained devices, where a distinct set of
  problems brings people together.

If people are curious about a topic and want to explore it together, that's
enough. There are no size or seriousness thresholds.

User Groups are **not**:

- **A replacement for existing project work.** Areas the project already
  organizes around already have a home, i.e. the language implementations (.NET, Java, Go, …), the
  Collector, semantic conventions, and so on. Use the
  existing SIG instead of starting a parallel group.
- **An official body.** User Groups don't speak for the OpenTelemetry project,
  don't hold formal decision-making power, and aren't governed by the
  [governance committee](https://github.com/open-telemetry/community/blob/main/governance-charter.md).
  They're communities the project is happy to support and point to.

If you're not sure whether your idea overlaps with existing project work, ask in
the [OpenTelemetry Slack channel](#spaces-the-project-can-offer). Folks are
glad to help you figure out where you fit.

## How to start one

There's no gatekeeping here. A rough recipe:

1. **Gauge interest.** Mention the idea in a relevant existing Slack channel, on
   social media, or at a meeting. You don't need a crowd, a handful of
   interested people is a fine start.
2. **Pick a name.** See [Naming & branding](#naming--branding) below.
3. **Find one or two organizers.** Someone to keep the channel alive, schedule
   the occasional meeting, and welcome newcomers. It doesn't have to be you
   alone.
4. **Request a space to talk** (see below).
5. **Tell people it exists.** You're welcome to have your group listed as an
   unofficial-but-welcomed community (see
   [Getting your group listed](#getting-your-group-listed)).

### Spaces the project can offer

OpenTelemetry lives in the **CNCF Slack**. If you're not there yet, sign up at
[slack.cncf.io](https://slack.cncf.io/) and join the `#opentelemetry` channel —
that's the project's main channel and the best place to start a conversation.

For a User Group, the project can offer:

- **A dedicated Slack channel** named `#otel-<name>` (e.g. `#otel-healthcare`),
  with the OpenTelemetry Admin user as a channel manager. Ask in `#opentelemetry` and
  an admin can create it.
- **Access to the OpenTelemetry Zoom** for regular meetings, if your group wants
  to meet synchronously.

### Requirements when using official spaces

The recommendations on this page are just that — recommendations. But the moment
your group uses **official OpenTelemetry or CNCF spaces** (Slack, Zoom, etc.), a few things are **mandatory**:

- Everyone must follow the
  [CNCF / OpenTelemetry Code of Conduct](https://github.com/open-telemetry/community/blob/main/code-of-conduct.md).
  This is non-negotiable and applies to all participants.
- Group communications and any promotion must respect the OpenTelemetry
  **marketing, naming, and social media guidelines** and other applicable
  [project and CNCF policies](https://github.com/open-telemetry/community/tree/main/policies).

If your group operates entirely in spaces you run yourselves, these are still
good practice — but only the spaces the project provides come with hard
requirements attached.

## Naming & branding

"OpenTelemetry" is a trademark, and its use is governed by the
[Linux Foundation Trademark Usage Guidelines](https://www.linuxfoundation.org/legal/trademark-usage).
Please read them before naming your group. In short, you may use the mark to
describe what your group is about, but you may not use it in a way that implies
your group is an official OpenTelemetry product or that the project endorses it.

- **Group name:** name your group as a *User Group for* your topic rather than
  folding the mark into a new product-like name. For example, prefer
  **"OpenTelemetry User Group for Industrial Applications"** over "OpenTelemetry
  Industrial". The "User Group for …" construction makes clear that this is a
  community using OpenTelemetry, which is exactly what it is. If you're unsure
  whether a name is acceptable, ask the project, or reach out to
  [trademarks@linuxfoundation.org](mailto:trademarks@linuxfoundation.org).
- **Slack channel:** `#otel-<name>` (e.g. `#otel-telco`). Do not name it `#opentelemetry-<name>`
- **GitHub:** if your group wants a place for code or documents, use a **personal
  repository** — there's no need for (and we'd rather you not
  create) a separate GitHub organization. You may prefix the repository name with
  `otel-` (e.g. `otel-telco-examples`) to make it discoverable.
- **Licensing:** license any code or content you publish under **Apache-2.0**.
  Beyond being permissive and well-understood, it keeps the door open for a clean
  donation to the OpenTelemetry project later, should your group's work ever grow
  into something the project wants to adopt.

When in doubt about a name or logo usage, ask — it's much easier to adjust early
than after a group has momentum.

## Getting your group listed

Once your group is up and running, you're welcome to have it listed as an
**unofficial but welcomed** community — for example on the OpenTelemetry website
or in the community README. Open a pull request or issue against the
[community repository](https://github.com/open-telemetry/community/), or ask in
the community Slack channel, and someone will help get it added.

Listing helps people find your group. It does **not** confer official status.

## Where a group might go

Most User Groups will simply be communities — good ones can run for years
sharing knowledge and never need to become anything more official, and that is a
complete success. Graduating into official project work is **not** the goal, and
it isn't a ladder every group is expected to climb.

That said, groups have a way of surfacing good ideas, and sometimes an idea
wants a more official home. When that happens, a User Group can be fertile ground
for it, and the usual project paths are open:

- A group might put forward a **project proposal**, often in collaboration with
  an existing SIG. See the
  [project management guidelines](https://github.com/open-telemetry/community/blob/main/project-management.md).
- A group might turn out to be **adjacent to an existing SIG** — for instance the
  [End-User SIG](https://github.com/open-telemetry/community/blob/main/community-members.md) —
  and the natural move is to bring the work there.

None of this is an obvious or expected path — just a possible one. Groups that
reach that point tend to find their way, and the project is happy to help when
asked.

## Questions?

Join `#opentelemetry` in the [CNCF Slack](https://slack.cncf.io/), or open an
issue in the [community repository](https://github.com/open-telemetry/community/).
We're glad you're here.

## Appendix: Disclaimer

To make your group's unofficial status clear, please add a disclaimer to your
group's spaces (e.g. Slack channel topic, repository README, or event
descriptions). You're welcome to copy the following:

```md
> [!NOTE]
>
> This is an [OpenTelemetry User Group](https://github.com/open-telemetry/community/blob/main/guides/contributor/user-groups.md).
> It is not an official body within the OpenTelemetry project. It is subject to
> the [CNCF Code of Conduct](https://github.com/open-telemetry/community/blob/main/code-of-conduct.md).
```
