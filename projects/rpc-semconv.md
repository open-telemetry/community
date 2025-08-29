# RPC Semantic Convention Stability

## Goals, objectives, and requirements

- Define the scope of what is an RPC system? Graph QL, WebSockets, SSE over HTTP, MCP, SignalR, WCF, etc?
  Are logical operations like AWS SDK calls (REST over HTTP) RPC calls?
- Update non-streaming RPC semantic conventions to be consistent with the naming conventions that
  have been established through HTTP and Database semantic convention stabilization.
- Alignment with the gRPC team and clear guidance for users who are currently confused
  because of differences between OpenTelemetry semantic conventions
  [gRPC semantic conventions](https://github.com/grpc/proposal/blob/master/A66-otel-stats.md).
- Stabilize the non-streaming RPC semantic conventions.
- Stretch goal: Stabilize streaming RPC semantic conventions.

## Deliverables

Stable RPC semantic conventions.

## Staffing / Help Wanted

* @trask project lead / GC sponsor
* @lmolkova project lead / TC sponsor
* @mconnew domain expert from [CoreWCF](https://github.com/CoreWCF/CoreWCF)
* @albumenj domain expert from [Apache Dubbo](https://github.com/apache/dubbo)
* @SteveRao lead for [Apache Dubbo Java instrumentation](https://github.com/open-telemetry/opentelemetry-java-instrumentation/tree/main/instrumentation/apache-dubbo-2.7)
* @matt-hensley .NET instrumentation contributor

### Industry outreach

- @JamesNK from .NET gRPC library - open to us reaching out as needed

### Required staffing

Projects cannot be started until the following participants have been identified:
* Every project needs a project lead, who is willing to bottom line the project and address any issues which are not handled by other project members.
* At least two sponsoring [TC](../community-members.md#technical-committee) or [GC](../community-members.md#governance-committee) members (or [semantic convention maintainers](https://github.com/orgs/open-telemetry/teams/specs-semconv-maintainers) in the case of semantic convention SIGs), or community members delegated by them. Sponsors are dedicated to attending meetings, reviewing proposals, and in general being aware of the state of the project and its technical details. Sponsors guide the project through the spec process, keep the tracking issue up to date, and help to ensure that relevant community members provide input at the appropriate times.
* A GC liaison to facilitate this SIG's health and ensure project scope remains true to the project description. If a GC member is also a sponsor for this project, they are by default the GC liaison (see [GC check-ins](../gc-check-ins.md)).
* Engineers willing to write prototypes in at least two languages (if relevant to project). Languages should be fairly different from each other (for example: Java and Python).
* Maintainers or approvers from those languages committed to reviewing the prototypes.

## Timeline

Starting in early September. Targeting completion by KubeCon Europe 2026.

## Labels

[`area:rpc`](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3A%22area%3Arpc%22)
in the semantic-conventions repository.

## Project Board

Once approved, a project should be managed using a GitHub project board (see [open projects](https://github.com/orgs/open-telemetry/projects?query=is%3Aopen)). This project board should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

Any [member](../guides/contributor/membership.md) associated with the project can create the board. Once created, the creator of the board should:

- Assign `Admin` privileges on the project to the relevant project members (using a new or existing GitHub team).
- Change the visibility of the project to `Public` in order to share project status and priorities outside of the OpenTelemetry organization.
- Configure project workflows to automatically add issues and PRs to the board based on repositories and labels.

Once created, please add a link to the project board here.

## SIG Meetings and Other Info

Once a project is started, its corresponding SIG should meet regularly for discussion. These meeting times should be posted on the [OpenTelemetry public calendar](https://github.com/open-telemetry/community#calendar) and automatically recorded.

Any relevant information related to the SIG (e.g. sponsors, meeting times, Slack channels, meeting notes, etc.) must be publicly available in the [community](https://github.com/open-telemetry/community) SIG tables, which can be updated via the [sigs.yml](../sigs.yml) file and running `make table-generation`.

See [How to create and configure meetings](../docs/how-to-handle-public-calendar.md) for updating the public calendar or open an issue in the community repository so it's taken care of.
