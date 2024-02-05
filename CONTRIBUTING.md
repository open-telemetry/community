# OpenTelemetry Contributor Guide

Welcome to OpenTelemetry! This document is the single source of truth for how to
contribute to the code base. Feel free to browse the [open
issues](https://github.com/open-telemetry/community/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%2Fcontributor-guide)
and file new ones, all feedback welcome!

# Before you get started

## Sign the CLA

Before you can contribute, you will need to sign the [Contributor License
Agreement](https://docs.linuxfoundation.org/lfx/easycla/contributors).

## Code attribution

[License information](README.md#License) should be included in all source files where applicable.
Either full or short version of the header should be used as described at [apache.org](https://www.apache.org/foundation/license-faq.html#Apply-My-Software).
It is OK to exclude the year from the copyright notice. For the details on how to apply the copyright,
see the next section.

## Copyright Notices

OpenTelemetry follows [CNCF recommendations](https://github.com/cncf/foundation/blob/master/copyright-notices.md)
for copyright notices. We use "Copyright The OpenTelemetry Authors" notice form.

According to CNCF recommendations if you are contributing third-party code
you will need to [retain the original copyright notice](https://github.com/cncf/foundation/blob/master/copyright-notices.md#dont-change-someone-elses-notice-without-their-permission).

Any contributed third-party code must originally be Apache 2.0-Licensed or must
carry a permissive software license that is compatible when combining with
Apache 2.0 License. At this moment, BSD and MIT are the only
[OSI-approved licenses](https://opensource.org/licenses/alphabetical) known to be compatible.

If you make substantial changes to the third-party code, _prepend_ the contributed
third party file with OpenTelemetry's copyright notice.

If the contributed code is not third-party code and you are the author we
strongly encourage to avoid including your name in the notice and use the
generic "Copyright The OpenTelemetry Authors" notice. See rationale for this
recommendation [here](https://github.com/cncf/foundation/blob/master/copyright-notices.md#why-not-list-every-copyright-holder).

## Code of Conduct

Please make sure to read and observe our [Code of
Conduct](https://github.com/open-telemetry/community/blob/master/code-of-conduct.md).

## Community Expectations and Roles

OpenTelemetry is a community project. Consequently, it is wholly dependent on
its community to provide a productive, friendly, and collaborative environment.

- See [Community
  Membership](https://github.com/open-telemetry/community/blob/master/community-membership.md)
  for a list the various responsibilities of contributor roles. You are
  encouraged to move up this contributor ladder as you gain experience.

# Your First Contribution

Would you like to help make robust, modern telemetry a built-in feature of
modern software? We will help you understand the organization of the project and
direct you to the best places to get started. You'll be able to pick up issues,
write code to fix them, and get your work reviewed and merged.

Please be aware that, due to the number of issues our triage team deals with, we
cannot offer technical support in GitHub issues. If you have questions about the
development process, feel free to jump into our [Slack
Channel](https://cloud-native.slack.com/archives/CJFCJHG4Q) ([Get an invite to join CNCF](https://slack.cncf.io/)). You can also ask
questions on [Stack
Overflow](https://stackoverflow.com/questions/tagged/open-telemetry).

## Find something to work on

Help is always welcome! For example, documentation (like the text you are
reading now) can always use improvement. There's always code that can be
clarified and variables or functions that can be renamed or commented. There's
always a need for more test coverage. You get the idea: if you ever see
something you think should be fixed, you should own it.

You can also find issues crafted for contributions using the tag
**opentelemetry** at
[up-for-grabs.net](https://up-for-grabs.net/#/filters?tags=opentelemetry).

Those interested in contributing without writing code may help documenting,
evangelizing or helping answer questions about OpenTelemetry on various forums.

### Find a good first topic

There are multiple repositories within the OpenTelemetry organization. Each
repository has beginner-friendly issues that provide a good stepping stone to
larger contributions. For example, [Java
SDK](https://github.com/open-telemetry/opentelemetry-java/) has [help
wanted](https://github.com/open-telemetry/opentelemetry-java/labels/help%20wanted)
and [good first
issue](https://github.com/open-telemetry/opentelemetry-java/labels/good%20first%20issue)
labels for issues that should not need deep knowledge of the system. The good
first issue label indicates that members have committed to providing extra
assistance for new contributors.

#### Issue Assignment in Github

Often, new contributors ask to be assigned an issue they are willing to take on.
Unfortunately, due to GitHub limitations we can only assign issues to org
members or repo collaborators. Instead, please state in a comment that you
intend to work on this issue and it will be assumed to be yours.

### Learn about SIGs

#### SIG structure

You may have noticed that some repositories in the OpenTelemetry Organization
are owned by Special Interest Groups, or SIGs. We organize the community into
SIGs in order to improve our workflow and more easily manage a community
project. The developers within each SIG have autonomy and ownership over that
SIG's part of OpenTelemetry.

A SIG is an open, community effort. Anybody is welcome to jump into a SIG and
begin fixing issues, critiquing design proposals and reviewing code. SIGs have
regular [video
meetings](https://github.com/open-telemetry/community#special-interest-groups)
which everyone is welcome to attend.

### SIG-specific contributing guidelines

Some SIGs have their own CONTRIBUTING.md files, which may contain extra
information or guidelines in addition to these general ones. These are located
in the SIG-specific GitHub repositories.

### File an Issue

Not ready to contribute code, but see something that needs work? While the
community encourages everyone to contribute code, it is also appreciated when
someone reports an issue (aka problem). Issues should be filed under the
appropriate OpenTelemetry subrepository.

Make sure to adhere to the repository specific policies or issue templates to
provide detailed information that will help prompt answer and resolution of an
issue.

### Contributing

OpenTelemetry is open source, but many of the people working on it do so as
their day job. In order to avoid forcing people to be "at work" effectively
24/7, we want to establish some semi-formal protocols around development.
Hopefully, these rules make things go more smoothly. If you find that this is
not the case, please complain loudly.

As a potential contributor, your changes and ideas are welcome at any hour of
the day or night, weekdays, weekends, and holidays. Please do not ever hesitate
to ask a question or send a pull request.

### Communication

It is best to contact your
[SIG](https://github.com/open-telemetry/community#Special-Interest-Groups) for
issues related to the SIG's topic. Your SIG will be able to help you much more
quickly than a general question would.

For general questions and troubleshooting, use the [standard lines of
communication](https://github.com/open-telemetry/community#Communication).

## GitHub workflow

To check out code to work on, please refer to [the GitHub Workflow
Guide](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)
from Kubernetes. OpenTelemetry uses the same workflow. One of the main
highlights - all the work should happen on forks, to minimize the number of
branches on a given repository.

## Open a Pull Request

Pull requests are often called simply "PR". OpenTelemetry follows the standard
[github pull request](https://help.github.com/articles/about-pull-requests/)
process.

Common new contributor PR issues are:

- not having correctly signed the CLA ahead of your first PR (please [Sign the
  CLA](https://identity.linuxfoundation.org/projects/cncf))
- following any SIG or repository specific contributing guidelines (see
  CONTRIBUTING.md of the corresponding repository)
- dealing with test cases which fail on your PR, unrelated to the changes you
  introduce
- Introducing change that should be first be approved by TC, for instance, the
  introduction of new terminology

## Code Review

There are two aspects of code review: giving and receiving.

To make it easier for your PR to receive reviews, consider the reviewers will
need you to:

- follow the project and repository coding conventions
- write [good commit messages](https://chris.beams.io/posts/git-commit/)
- break large changes into a logical series of smaller patches which
  individually make easily understandable changes, and in aggregate solve a
  broader issue
- label PRs with appropriate SIGs and reviewers: to do this read the messages
  the bot sends you to guide you through the PR process

Reviewers, the people giving the review, are highly encouraged to revisit the
[Code of
Conduct](https://github.com/open-telemetry/community/blob/master/code-of-conduct.md)
and must go above and beyond to promote a collaborative, respectful community.

When reviewing PRs from others [The Gentle Art of Patch
Review](https://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)
suggests an iterative series of focuses which is designed to lead new
contributors to positive collaboration without inundating them initially with
nuances:

- Is the idea behind the contribution sound?
- Is the contribution architected correctly?
- Is the contribution polished?

Note: if your pull request isn't getting enough attention, you can explicitly
mention approvers or maintainers of this repository.

# Community

If you haven't noticed by now, we have a large, lively, and friendly open-source
community. We depend on new people becoming members and regular code
contributors, so we would like you to come join us! The [Community Membership
Document](https://github.com/open-telemetry/community/blob/master/community-membership.md)
covers membership processes and roles.

## Donations

Donations of preexisting code fall into two broad categories:
* **Small donations:** Some donations only amount to a single PR and should
  usually just be contributed as such
* **Large or complex donations:** Other donations are much larger, require
  ongoing maintenance of their own, and/or introduce nuanced licensing issues

Large donations – or small donations that turn up complex issues during PR
review – should be referred to the Technical Committee (TC) by filing an issue
in this `community` repository and tagging
`@open-telemetry/technical-committee`. The TC will respond to donation
proposals **within two weeks** (that is, after having time to meet and discuss
live). If the TC has not responded to the donation request within that
interval, the donating party can and should point to this document and request
guidance at the TC's earliest convenience.

All donated code requires a license compatible with the Apache Software License
2.0, and donated code will require a change of copyright to reflect the
OpenTelemetry Authors. The Governance Committee will also ask to review any
trademarks (like the names of components) the donation can carry and make a
decision to either remove those trademarks or transfer them to the CNCF.

### Donation process

Broadly, these are the steps the OpenTelemetry Governance and Technical
Committees follow to handle a prospective donation.

1. Per the above, the donating organization creates a GitHub issue using
   the "Donation Proposal" form in the `community` repository.
2. The Governance Committee (GC) will evaluate the proposal to ensure that
   the donation is aligned with the overall OpenTelemetry project vision
   and roadmap and has a balanced set of interested contributors and maintainers.
   The GC is also responsible for driving awareness in the community about
   the contribution and making sure all interested parties have a chance to
   object and/or contribute. The GC should work with any appropriate Special Interest
   Groups or Working Groups to evaluate the donation proposal, consider alternatives,
   and ensure OTel has the resources required to support the donation. When
   considering alternatives, the GC should consider at least the CNCF ecosystem,
   and may also consider other well-known open source projects or alternatives proposed
   by the community.
3. If a donation proposal passes the initial GC screening, the Technical Committee (TC)
   will conduct due diligence to determine if the proposed donation can be effectively
   integrated into the OpenTelemetry project in a way that meets the quality, security,
   and privacy standards of the project without violating stable specification or OTEPs.
   The TC will summarize their findings, and make a recommendation to either,
   conditionally or unconditionally, accept or reject the proposal, in a report which will
   be attached to the donation proposal issue. Writing the report may require meeting
   and discussing alternative technologies with different vendors in the community and
   can be a lengthy process. The TC member driving the report will post updates and time
   estimates to the issue.
4. The GC will consider the report and make a final decision about the donation,
   and document that decision on the donation proposal issue.
5. If accepted, the contributing organization – particularly if it's a
   commercial entity – must formally acknowledge via the GitHub issue that its
   respective sales and marketing departments have received, understood, and
   accepted the terms of the [OpenTelemetry marketing guidelines](https://github.com/open-telemetry/community/blob/main/marketing-guidelines.md).
6. Given all of the above, the GitHub issue is closed and the donation moves
   forward as agreed to by the TC and GC.

## Communication

- [General
  Information](https://github.com/open-telemetry/community#Communication)

## Events

OpenTelemetry participates in KubeCon + CloudNativeCon, held three times per
year in China, Europe and in North America. Information about these and other
community events is available on the CNCF [events](https://www.cncf.io/events/)
pages.
