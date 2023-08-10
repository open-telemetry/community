# OpenTelemetry Technical Committee (TC) Charter

## Guiding Principle

The OpenTelemetry project will operate transparently, collaboratively, ethically, and in alignment with the interests of OpenTelemetry technology end-users. Project proposals, timelines, and status must not merely be open, but also easily visible to and discoverable by outsiders.

## Evolution of OpenTelemetry Governance

Most large, complex open source communities have both a business and a technical governance model. Since its inception, the OpenTelemetry project strives to combine and align the OpenTracing and OpenCensus projects. OpenTelemetry has a project-level Governance Committee, a project-level Technical Committee, and is an incubating project in the Cloud Native Computing Foundation, working for interoperability and engagement across the industry in conjunction with the CNCF's Board of Directors and Technical Oversight Committee.

This OpenTelemetry Technical Committee Charter reflects the scope and expectations of the Technical Committee ("TC") with the maintainers, the consumers, and the ecosystem of the project. The charter will not be perfect, and so has a simple amendment process – a TC member proposes changes to be discussed and voted on by the full TC.

## Establishment of the Technical Committee

TC memberships are not time-limited. There is no maximum size of the TC. The size is expected to vary in order to ensure adequate coverage of important areas of expertise, balanced with the ability to make decisions efficiently. The TC must have at least four members and is recommended to have an odd number of members for tie-breaking purposes.

TC membership is developed through leadership in the project and was bootstrapped initially by selection of long-standing maintainers in the OpenTracing and OpenCensus projects. The TC may add additional members to the TC by the [election process](#election-of-tc-members) described below. The TC members are expected to be active leaders in the project. A TC member may be removed from the TC by voluntary resignation, by a super-majority TC vote similar to the [election process](#election-of-tc-members), or in accordance with the participation rules described below.

Changes to TC membership should be posted in the agenda document, and may be suggested as any other agenda item.

### No Over-Representation

No more than one-fourth (25%) of the TC members may be affiliated with the same employer (in the event of confusion or concern, the OpenTelemetry TC will defer to the CNCF definition of "same employer"). If removal or resignation of a TC member, or a change of employment by a TC member, creates a situation where more than one-fourth of the TC membership shares an employer, then the situation must be immediately remedied by the resignation or removal of one or more TC members affiliated with the over-represented employer(s).

### Participation

The TC may, at its discretion, invite any number of non-voting observers to participate in the public portion of TC discussions and meetings.

The TC shall meet regularly using tools that enable participation by the community The meeting shall be directed by the TC Chairperson. Responsibility for directing individual meetings may be delegated by the TC Chairperson to any other TC member. TC members are expected to regularly participate in TC activities.

In the case where an individual TC member -- within any six month period -- attends fewer than 25% of the regularly scheduled meetings, does not participate in TC discussions, and does not participate in TC votes, the member shall be automatically removed from the TC. The member may be invited to continue attending TC meetings as an observer.

## Responsibilities of the Technical Committee

The TC is responsible for all technical development within the OpenTelemetry project, including:

* Setting release dates
* Quality standards for releases
* Technical direction
* GitHub repository management, membership and hosting
* Development process and any coding standards
* Approving changes to any specifications
* Mediating technical discussions which have cross project impact
* Deciding on and communicating about proposed donations to OpenTelemetry

The TC recognizes that maintainers of specific languages or sub-projects have significant autonomy over their SIG and implementations.  The TC’s focus is on cross-project or disputed concerns with a primary goal of seeking consensus to develop an appropriate technical solution. The TC will define OpenTelemetry’s release vehicles and serve as the primary technical liaison body for the OpenTelemetry project with the CNCF's TOC, external open source projects, consortiums and groups.

## OpenTelemetry Project Operations

The TC will establish and maintain a development process for OpenTelemetry. The development process will establish guidelines for how the developers and community will operate.

The TC is additionally responsible for organizing the project structure, including possibly the creation and alignment of Special Interest Groups (SIGs), and/or sub-projects. Each SIG or sub-project must have a well-defined scope and must work within that scope.

The development process will include a process for the TC to oversee and approve changes in the lifecycle of a Project, which will include consideration of the following criteria:

* Cleanliness of code base
* Ample and diverse Members, Approvers and Maintainers to assure the vitality of the project
* Stability (e.g. presence of test suites, stable APIs and use of an appropriate source-code control system)
* Predictability of releases and standards of compatibility
* Alignment with OpenTelemetry’s goals and priorities

The TC and entire technical community will follow any processes as may be specified by the Cloud Native Computing Foundation relating to the intake and license compliance review of contributions, including the CNCF IP Policy.

### Code Donations

From time to time, organizations may wish to donate existing code to
OpenTelemetry. The basic process for donating code is described [in
CONTRIBUTING.md](CONTRIBUTING.md#donations).  Of note is the expectation that
the TC respond to donation proposals **within two weeks.**

## Elections

Leadership roles in OpenTelemetry project will be peer elected representatives of the community.

### Election of TC Members

New TC members can be nominated by any Member in Standing as defined in the [OpenTelemetry Governance Charter](https://github.com/open-telemetry/community/blob/master/governance-charter.md#members-of-standing), and must be sponsored by one of the existing TC members to bring it to a vote. A candidate can be elected to the TC by the super-majority vote (greater than two thirds) of the existing TC members. The voting by the TC members is anonymous. A multiple-candidate method, such as [Condorcet](https://en.wikipedia.org/wiki/Condorcet_method) or [Single Transferable Vote](https://en.wikipedia.org/wiki/Single_transferable_vote), may be used to conduct the vote, by phrasing the selections as:

* Vote for Nominee X
* Vote against Nominee X

The voting should remain open for a minimum of 5 business days.

### Election of TC Chair

The TC will elect from amongst voting TC members a TC Chairperson to work on building an agenda for TC meetings. The TC shall hold annual elections to select a TC Chairperson; there are no limits on the number of terms a TC Chairperson may serve.

For election of persons (such as the TC Chairperson) by a vote of the TC voting members, a multiple-candidate method should be used, such as:

* [Condorcet](https://en.wikipedia.org/wiki/Condorcet_method) or
* [Single Transferable Vote](https://en.wikipedia.org/wiki/Single_transferable_vote)

Multiple-candidate methods may be reduced to simple election by plurality when there are only two candidates for one position to be filled. No election is required if there is only one candidate and no objections to the candidates election. Elections shall be done within the Projects by the collaborators active in the Project.

## Voting on project issues

For internal project decisions, Maintainers shall operate under Lazy Consensus, a decision-making policy which assumes general consent if no responses are posted within a defined period. The TC shall establish appropriate guidelines for implementing Lazy Consensus (e.g. expected notification and review time periods) within the development process.

The TC follows a [Consensus Seeking](https://en.wikipedia.org/wiki/Consensus-seeking_decision-making) decision making model. When an agenda item has appeared to reach a consensus the moderator will ask "Does anyone object?" as a final call for dissent from the consensus.

If an agenda item cannot reach a consensus a TC member can call for either a closing vote or a vote to table the issue to the next meeting. The call for a vote must be seconded by a majority of the TC or else the discussion will continue.

For all votes, a simple majority of a quorum of TC members for, or against, the issue wins. A TC member may choose to participate in any vote through abstention. A quorum is defined as > 1/2 of TC members voting for or against or explicitly abstaining. TC votes may be done synchronously or asynchronously. Asynchronous votes remain open for a period of time agreed upon by the TC when the issue is put to a vote. Aggregated TC vote results are shared publicly but the vote selections of individual members are not shared. The TC decides whether vote selections by members are anonymous or shared among members when the issue is put to a vote.

### Requesting a TC decision

When a project issue fails to reach consensus, OpenTelemetry [community members](./community-membership.md#member) may request that the TC make a decision. If the issue falls under a project with assigned [approvers](./community-membership.md#approver) and / or [maintainers](./community-membership.md#maintainer), at least two of those members should agree to and coordinate requesting a TC decision.

The request for a TC decision must be made by a comment on a public issue. The comment must explicitly tag the TC team (@open-telemetry/technical-committee), and summarize the various options and their relative tradeoffs. A TC member should review the summary and may request additional details or other changes to more accurately frame the issue. The request will then be added to the TC agenda, and the TC will work towards a decision using the [TC voting process](#voting-on-project-issues).

## Project Roles

The OpenTelemetry project git repository is maintained by the TC and additional Maintainers who are added by the TC on an ongoing basis.

Individuals making significant and valuable contributions, can move through the project to leadership roles as outlined in the [Community Membership](./community-membership.md) document. Modifications of the contents of the git repository are made on a collaborative basis as defined in the development process.

Project Members may opt to elevate (via [mail list](./#tc-technical-committee)) significant or controversial modifications, or modifications that have not found consensus to the TC for discussion. The TC will serve as the final arbiter where required. The TC will additionally publish and maintain a development process guide for people looking to participate in the development effort.
