# Contributor Experience

## Background and description

Over the last few years the OpenTelemetry project has seen massive growth, not
only in adoption and lines of code, but also in the number of individuals who
contribute to this project in different ways.

While in the beginning of the project contributors knew each other well and
could share implicit in-group knowledge effortlessly, the project has outgrown that
phase a while ago and we see different kinds of problems, that make it hard
for long-term contributors to maintain the project sustainably and for new-comers
to enter the project effortlessly.

In this project proposal we suggest to form a cross-cutting special interest group
that takes responsibility for driving contributor experience projects and that
closely collaborates with all other SIGs and governing bodies to increase contributor
sustainability, velocity and happiness.

### Current challenges

Among others the challenges the OpenTelemetry project is facing in regards of
contributor experience are:

* No consistent way of moving contributors "up the ladder", e.g. from member to
  approver, from approver to maintainer etc, which makes those changes invisible
  to the larger project and opaque to project leadership on who is doing
  what.
* No clear onboarding path for new contributors, or contributors taking on new
  responsibilities within the project (triagers, approvers, maintainers, committee
  members), which leads to friction in understanding of the overall project goals,
  to misalignment in implementations and the feeling of contributors being remote
  to other parts of the project.
* No explicit contributor guidebook that helps contributors to answer common
  questions no matter where they are on the contributors' ladder.
* No mentorship available for new contributors or contributors stepping up into new roles to
  make them part of the project and aware of expectations.  
* Only implicit and unstructured recognition for contributors, instead of explicit
   recognition which would help contributors to feel seen and recognized.
* No structured collaboration across SIGs, especially in the case of cross-cutting
  concerns (Security, Docs, End-User, ...), leading to information silos and misalignment.
* SIGs are short of contributors and require some help to advertise their need
  (blog post, social posts, etc) and to lower the barrier of entry into their
  sub-project.
* Implicit bias towards US (and EU) working hours, rituals and modes of operation. Majority of SIG meetings occurring from early PST onward.

Note that there are individuals within the project who try to tackle some of those
aspects as individuals and not in a team effort, notable:

* [Add skeleton for maintainer and contributor guidebooks](https://github.com/open-telemetry/community/pull/2051)
* Mentorship efforts, e.g. [Outreachy](https://cloud-native.slack.com/archives/C060GFUL0P6)
* Surveys by the End User SIG that aim towards contributor experience
* _add more_

Also related to this initiative is the [Check-In process of the Governance Committee](../gc-check-ins.md)

### Goals, objectives, and requirements

The goal of this project is to establish a cross-cutting "SIG Contributor Experience",
which is "responsible for improving the experience of those who upstream contribute to
the OpenTelemetry project. [They] do this by creating, and maintaining programs and processes that promote community health and reduce project friction, while retiring those programs and processes that don't. Being conscientious of our contributor base is critical to scaling the project, growing the ecosystem, and helping the project succeed". (via [K8s Contributor Experience Special Interest Group Charter](https://github.com/kubernetes/community/blob/master/sig-contributor-experience/charter.md))

While this is "yet another SIG" initiative, we believe that **not** establishing
such a SIG is not an option: the problems outlined above will get bigger not
smaller and while the final ownership of the health of the project is with the GC
this requires a coordinated effort and more hands across the project to be addressed
successfully.

Note that similar to other cross-cutting SIGs (Docs, Security, End-User) this SIG will not exclusively own
the domain of contributor experience, but they take responsibility to drive efforts in close collaboration
with SIGs and Committees.

## Deliverables

After foundation the SIG will collaborate with contributors of existing efforts
(see above) and work towards establishing programs and initiatives around contributor
experience, including

* Onboarding rituals for members, approvers, maintainers
* A contributor guidebook
* Mentorship opportunities
* Contributor recognition programs (e.g. via [Credly](https://credly.com) or with blog posts on the style of "here's what's happening under the hood"
* Blog posts and social media posts to highlight areas where help is needed
* Events targeting the Contributor Community
* Consume SIG Check-In reports from the GC and use this data to improve contributor experience
* Support the community of contributors to maintain the Code of Conduct (Note: this is a support function, the responsibility for the CoC and especially enforcing it lays with the Governance Committee)
* Implement or suggest measures to support contributor diversity
* Help SIGs to establish practices to improve contributor experience, e.g. having multiple meeting times to serve more timezones
* Maintain a relationship with other Contributor Experience SIGs (e.g. from K8s) and TAG Contributor Strategy, to consult them for best practices and resources where that makes sense, as well as upstream our governance resources into their repos for other projects when that makes sense.

## Staffing / Help Wanted

GC/TC sponsors:

* [@jpkrohling](https://github.com/jpkrohling)
* [@svrnm](https://github.com/svrnm)
  
Maintainers, approvers, and contributors:

* [@JamieDanielson](https://github.com/JamieDanielson)
* [@jpkrohling](https://github.com/jpkrohling)
* [@maryliag](https://github.com/maryliag)
* [@musingvirtual](https://github.com/musingvirtual)
* [@mx-psi](https://github.com/mx-psi)
* [@svrnm](https://github.com/svrnm)
* [@theletterf](https://github.com/theletterf)

## Meeting Times

The SIG will meeting time will be discussed and finalized when this proposal has been merged. There will be a weekly meeting, if necessary to cater as many time zones as possible there will be bi-weekly meetings at alternating times.

## Timeline

* Month 1: Establish the SIG with all required resources (repository, meeting notes, calendar, GH groups, etc)
* Month 2-6:
  * Create a charter based on the [K8s SIG Contributors Experience Charter](https://github.com/kubernetes/community/blob/master/sig-contributor-experience/charter.md)
  * Tackle existing projects (contributor guide book, mentorship)
  * Identify high stake initiatives
* Month 6: Report to GC & TC about the establishment of the SIG
* Beyond that the SIG is established and will operate similar to existing SIGS.
