# OpenTelemetry Contributor Guide

Welcome to OpenTelemetry! This document is the single source of truth for how to
contribute to the code base. Feel free to browse the [open
issues](https://github.com/open-telemetry/community/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%2Fcontributor-guide)
and file new ones, all feedback welcome!

# Before you get started

## Sign the CLA

Before you can contribute, you will need to sign the [Contributor License
Agreement](https://docs.linuxfoundation.org/docs/communitybridge/communitybridge-easycla/contributors).

## Copyright Notices

OpenTelemetry follows [CNCF recommendations](https://github.com/cncf/foundation/blob/master/copyright-notices.md)
for copyright notices. We use "Copyright The OpenTelemetry Authors" notice form.

According to CNCF recommendations if you are contributing a third-party code
you will need to [retain the original copyright notice](https://github.com/cncf/foundation/blob/master/copyright-notices.md#dont-change-someone-elses-notice-without-their-permission).

Any contributed third-party code must originally be Apache 2.0-Licensed or must
carry a permisive software license that is compatible when combining with
Apache 2.0 License (e.g. BSD or MIT license). 

If you make substantial changes to the third-party code _prepend_ the contributed
third party file with OpenTelemetry's copyright notice.

If contributed code is not a third-party code and you are the author we
stroungly encourage to avoid including your name in the notice and use the
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
development process, feel free to jump into our [Gitter
Channel](https://gitter.im/open-telemetry/community) . You can also ask
questions on [Stack
Overflow](https://stackoverflow.com/questions/tagged/opentelemetry).

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
- Introducing change that should be first be approved by TSC, for instance, the
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
Review](http://sage.thesharps.us/2014/09/01/the-gentle-art-of-patch-review/)
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

## Communication

- [General
  Information](https://github.com/open-telemetry/community#Communication)

## Events

OpenTelemetry participates in KubeCon + CloudNativeCon, held three times per
year in China, Europe and in North America. Information about these and other
community events is available on the CNCF [events](https://www.cncf.io/events/)
pages.
