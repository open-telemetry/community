# Network Observability

## Background and description

This project aims to establish unified and comprehensive network semantic conventions for OpenTelemetry, enabling traditional network observability methods (like NetFlow, IPFIX, SNMP) to integrate natively into the ecosystem.

### Current challenges

Currently, OpenTelemetry's network semantic conventions are sparse and predominantly reflect an application's perspective of its own network activity. This creates a significant gap for network-centric observability, which relies heavily on L3 and L4 attributes for protocols like Netflow, SNMP, and SNMP Trap. Compounding this issue is a general lack of defined network-related metrics and traces, including standardized metrics and flow trace instrumentation within OpenTelemetry eBPF Instrumentation (OBI).

On the collection side, the existing OpenTelemetry collector contrib receivers for Netflow and SNMP lack the necessary functionality to be useful and do not adhere to standard network semantic conventions. Furthermore, there is currently no SNMP trap receiver available in the collector contrib.

### Goals, objectives, and requirements

This project makes OpenTelemetry viable for network-centric observability. We will expand core semantic conventions (`network`, `source`, `destination`, `dns`), define standards for traditional telemetry (Netflow, SNMP), and fix fragmented collector receivers. Acting now prevents the spread of non-standard L3/L4 implementations. This work establishes OpenTelemetry as a unified standard for network engineers and provides foundational network telemetry for other SIGs (like OBI and Entities).

- **Expand, clarify, and maintain core network-related semantic conventions**: This includes maintaining the `network`, `source`, `destination`, and `dns` areas. We will work closely with several SIGs, particularly the main Semantic Conventions SIG, as well as the Entities, System, and OBI SIGs.

- **Define deep network semantic conventions for traditional network telemetry methods**: This objective focuses on deep network concepts where we will take advantage of a federated semantic convention repository. Key deliverables include:
  - Defining Netflow metrics and trace spans
  - Defining traceroute / network-path telemetry conventions
  - Defining BGP telemetry conventions
  - Defining standard SNMP metrics
  - Defining standard SNMP trap logs

- **Provide support and contributions across the broader OpenTelemetry ecosystem**: Addressing the objectives above establishes the foundation needed to support and contribute across the broader OpenTelemetry ecosystem. Key examples of these separate but related efforts include:
  - Improving the usability of network-related `opentelemetry-collector-contrib` receiver components (e.g., `snmpreceiver` and `netflowreceiver`) and adding an `snmptrapreceiver`.
  - Supporting other SIGs (such as OBI) with their network-related telemetry functions.
  - Defining network-related entity definitions as a part of the Entities SIG.

## Deliverables

**Near-term:**

1. Review existing attributes within `network`, `source`, `destination`, and `dns` areas to clarify language and definitions.
2. Triage and resolve existing open issues related to labels: [area:network](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Anetwork), [area:source](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Asource), [area:destination](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Adestination), and [area:dns](https://github.com/open-telemetry/semantic-conventions/issues?q=state%3Aopen%20label%3Aarea%3Adns).
3. Document the [new pattern for source/destination attribute](https://github.com/open-telemetry/semantic-conventions/issues/3791).
4. Establish a guiding heuristic to dictate what belongs in the `system.network` vs. `network` namespace.

**Mid-term:**

1. Expand core network attributes (DNS, AS, CIDR, and VPC attribution; network interfaces).
2. Establish protocol-related metrics (e.g., [TCP/UDP proposal](https://github.com/open-telemetry/semantic-conventions/issues/3682), [ICMP issue](https://github.com/open-telemetry/semantic-conventions/issues/1368)).
3. Define semantic conventions for flow, path, and routing telemetry:
   - [Netflow metrics](https://github.com/open-telemetry/semantic-conventions/pull/3656) and [netflow trace spans](https://docs.mermin.dev/concepts/introduction-to-flow-traces)
   - Traceroute / network-path telemetry (hops, hop index, address/hostname/ASN, per-hop RTT, timeouts or unreachable outcomes)
   - BGP telemetry (ASN, advertised and withdrawn prefixes, route updates, and related metrics/log events)
4. Establish network-related entities (e.g., network interface, subnet, proc).
5. Define semantic conventions for common SNMP MIB objects and SNMP Trap events as OpenTelemetry logs.

**Long-term:**

1. Collaborate with the Collector SIG to provide official receivers for Netflow, SNMP, and SNMP Trap.
2. Collaborate with the OBI SIG to instrument the network, targeting the generation of flow traces and metrics via eBPF.
3. Define SNMP semantic conventions for less-common and vendor-specific MIBs.

## Staffing / Help Wanted

### SIG

Network

### Required staffing

#### Project Leads(s)

- Rob Cowart (@robcowart) (affiliation: entities)
- Sven Cowart (@svencowart)  (affiliation: semconv)
- Antonio Jimenez (@ajimenez1503)
- Braydon Kains (@braydonk) (affiliation: system)

#### Other Staffing

- Jake Smith (@jksmth)
- Giuseppe Ognibene (@pinoOgni) (affiliation: obi)
- Stephen Lang (@skl)
- Mario Macias (@mariomac) (affiliation: obi)
- Matthieu Noirbusson (@MatthieuNoirbusson)
- Henrik Rexed (@henrikrexed)
- Christian Adell (@chadell)

### Sponsorship

#### TC Sponsor

[TODO: Add TC Sponsor]

#### GC Liaison

Ted Young (@tedsuo)

## Expected Timeline

- **Months 1-2**: Complete near-term deliverables (review core attributes, triage issues, establish namespace heuristics).
- **Months 3-6**: Complete mid-term deliverables (expand attributes, establish protocol and flow metrics, define entities and SNMP standards).
- **Months 7-18**: Complete long-term deliverables (collaborate on collector receivers, eBPF instrumentation, and vendor-specific MIBs).

[TODO: After the project has started, please use GitHub project updates to set specific target start and completion dates (see [Project Lifecycle](project-management.md#project-lifecycle) for more information).]

## Labels

- `area:network`
- `area:source`
- `area:destination`
- `area:dns`

---

## Post-Approval Next-Steps

### GitHub Project (Post-Approval)

Once approved, a project should be managed using a [GitHub project](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects). This project should be pre-populated with issues that cover all known deliverables, organized by timeline milestones.

Any [member](./guides/contributor/membership.md) associated with the project can create the board.
Please use the existing [GitHub Project template](https://github.com/orgs/open-telemetry/projects/140) to create your project, replacing placeholders as appropriate.

Once created, the creator of the board should:

- Assign `Admin` privileges on the project to the relevant project members (using a new or existing GitHub team).
- Change the visibility of the project to `Public` in order to share project status and priorities outside the OpenTelemetry organization (default in template).
- Configure project workflows to automatically add issues and PRs to the board based on repositories and labels.

See [Project Lifecycle](project-management.md#project-lifecycle) for more information about sharing project updates and status.

Once created, please add a link to the project board here.

### SIG Meetings, Roadmap, and Other Info (Post-Approval)

Once a project is started, its corresponding SIG should meet regularly for discussion. These meeting times should be posted on the [OpenTelemetry public calendar](https://github.com/open-telemetry/community#calendar) and automatically recorded.

Any relevant information related to the SIG (e.g. sponsors, meeting times, Slack channels, meeting notes, etc.) must be publicly available in the [community](https://github.com/open-telemetry/community) SIG tables, which can be updated via the [workstreams.yml](./workstreams.yml) file and running `make generate`.
Please ensure that the GitHub project ID is added to [workstreams.yml](./workstreams.yml) as a `roadmapProject` resource entry under the corresponding SIG to include this project in the OpenTelemetry Roadmap (see [Roadmap Management](./roadmap-management.md) for more information).

See [How to create and configure meetings](./docs/how-to-handle-public-calendar.md) for updating the public calendar or open an issue in the community repository so it's taken care of.
