# OpenTelemetry Governance Committee Charter

Last updated: November 2023

## Overview

This document describes the goals, the scope and the structure of the
OpenTelemetry Governance Committee (GC). It describes the election process for
the Governance Committee and how the committee operates.

## Goals

The initial role of the governance committee is to **instantiate the formal
process for OpenTelemetry governance**. In addition to defining the initial
governance process, the bootstrap committee strongly believes that **it is
important to provide a means for iterating** the processes defined by the
governance committee. We do not believe that we will get it right the first
time, or possibly ever, and won’t even complete the governance development in a
single shot. The role of the governance committee is to be a live, responsive
body that can refactor and reform as necessary to adapt to a changing project
and community.

## Scope

The Governance Committee has a set of rights and responsibilities including the
following:

- Charter for **Technical Committee**.
- Define, evolve, and defend a **Code of Conduct**, which must include a
  neutral, unbiased process for resolving conflicts.
- Define and evolve **project governance structures and policies**, including
  how contributors become committers/maintainers, approvers, reviewers, members,
  etc.
- Decide, for the purpose of elections, who can vote.
- Logo/landing page/marketing. 
- Maintain relationships with CNCF. For instance, creating [documents describing
  the project](https://github.com/cncf/toc/blob/main/proposals/sandbox/opentelemetry.adoc)
- Define, evolve, and defend the **vision, values, mission, and scope** of the
  project - to establish and maintain the soul of OpenTelemetry.
- Decide how and when **official releases** of OpenTelemetry artifacts are
  made and what they include.
- Establish processes regarding, and provide **a final escalation path** for any
  contested OpenTelemetry related decision.
- Establish processes regarding other **project resources/assets**, including
  artifact repositories, build and test infrastructure, web sites and their
  domains, blogs, social-media accounts, etc.
- **Request funds** and other support from the CNCF (e.g. marketing, press,
  etc.).
- **Delegate appropriate authority** to trusted individuals.

This work is to be handled by the Governance Committee or delegated to other
project groups like the [Technical Committee](./tech-committee-charter.md).

## Committee Structure

The **OpenTelemetry Governance Committee consists of 9 individual members** of
the community **elected for 2 year terms**.
The terms are **staggered with elections each year** (alternating 4 seats in even 
years and 5 seats in odd years).

## Elections

### Members of Standing

Standing in the OpenTelemetry community will be defined by the union of:

- Active members - those with 20 contributions (PRs, Issues, Comments etc.) in
  the prior rolling year.
- All approvers, and maintainers in the OpenTelemetry organization

Members who don’t meet the criteria above and are part of the following are
encouraged to help us evolve the definition of Member of Standing through the
Exception Process outline below.

- Maintainers for projects (vendors, OSS observability solutions, etc) with
  strong end-user adoption that have taken a hard dependency on OpenTelemetry
  APIs or data formats (one representative per project)
- Representatives from major organizations that have adopted OpenTelemetry as
  end-users (one representative per organization)

The Governance Committee explicitly believes that this heuristic will be
inaccurate and not represent the entire community. An exception form will be
provided for people who have contributed to the project but may not meet these
criteria. Exception eligibility applications will be approved by the Governance
Committee by a simple majority vote. The exception process will be used as data
points for refining the criteria for the future.

It is the responsibility of the Governance Committee to refine these criteria 
prior to each election, including adjusting the number of required contributions
, and adding any additional community memberships that include eligibility.

### Eligibility for candidacy

Anyone may nominate either themselves or someone else to be a candidate in the
election. To be ratified as a candidate, the nominee must accept the nomination
and three Members of Standing (including the nominator, if she/he has standing)
from three different employers, must endorse the nomination.

Nominators are free to nominate as many people as they wish to. Members of
Standing may endorse multiple nominees, but we expect endorsements to be in good
faith. If this turns out to be a problem, this will be reconsidered.

### Eligibility for voting

All Members of Standing are eligible to vote for the governance committee
members. 

### Election process

Elections will be held using time-limited approval voting on
[Helios](https://vote.heliosvoting.org/). The top vote getters will be elected
to the respective positions.

### Maximal representation

To encourage diversity there will be a maximum of one-third representation on
the Governance Committee from any one company at any time. If the outcomes of
an election result in greater than 1/3 representation (or maximum of two,
whichever is greater), the lowest vote getters from any particular company will
be removed until representation on the committee is less than one-third.

If percentages shift because of job changes, acquisitions, or other events,
sufficient members of the committee must resign until max one-third
representation is achieved. If it is impossible to find sufficient members to
resign, the entire company’s representation will be removed and new special
elections held. In the event of a question of company membership (for example
evaluating independence of corporate subsidiaries) a majority of all
non-involved Governance Committee members will decide. 

### Special Elections

In the event of a resignation or other loss of a governance committee member, a
special election for that position will be held as soon as possible. The same
group of people as described in "eligibility for voting" will vote in the
special election. A committee member elected in a special election will serve
out the remainder of the term for the person they are replacing, regardless of
the length of that remainder.

### Limiting Corporate Campaigning Support

To reduce the size of company advantages, candidates may not use their companies
internal or external brand to campaign. Their employers cannot solicit votes on
their behalf or sponsor candidates from partner organizations. Simply put,
elections highlight individuals outside of their corporate role and should be
treated as "brand free" activities.

## Refactoring or reforming the governance committee

At any time the governance committee may vote, via supermajority (greater than
two-thirds of votes), to rewrite or remove any part of this charter. Beyond
small tweaks, this should be used sparingly, if ever, and in the presence of
clear failures of the process. We explicitly do not allocate a role for the
broader community in reformulating governance, we believe that in such a case
the community will "vote with their feet" by either leaving or forking the
project.

## Emeritus Term

Members of the governance committee will graduate to becoming *Emeritus* members
of the governance committee.

## Governance Committee Meetings

Regular governance committee meetings will be held, at least once per month. The
entire governance committee is generally expected to attend every meeting, but
quorum is met with 2/3 attendance. If a member misses more than 50% of all
meetings held within a six month period then they will be removed from the
committee and a special election will be held. Recorded videos of the meetings
will be made publicly available in a timely manner.

Non-recorded, closed meetings are reserved for confidential matters (for
example, code of conduct issues) which are not appropriate to be shared with the
broader community. Governance committee meetings can be made closed by a simple
majority vote of the governance committee members, but closed meetings do not
count towards the required meeting frequency. The governance committee will
inform the community if a particular meeting is closed, as well as the general
reasons for this, prior to the meeting taking place.

## Community Manager Role

In order to facilitate end-user and contributor experience programs that cut
across multiple SIGs in the OpenTelemetry project, the governance committee
may appoint Community Managers (CMs) to act as liaisons, facilitators, and 
organizers for such programs. The goal of this role is to ensure the health of
the OpenTelemetry end-user and contributor community.

### Community Manager Responsibilities

- Act as stewards for the OpenTelemetry end-user and contributor community by
  organizing events and coordinating programs.
- Manage the OpenTelemetry social media and blog presence.
- Work with the CNCF and member organizations on cross-functional projects as
  needed.
- Track and report on OpenTelemetry end-user and contributor community health
  for the GC.
- Grow the OpenTelemetry end-user and contributor community by advocating for
  programs and initiatives that will attract new users or aid contributor
  experience.
  
### Community Manager Eligibility, Term, and Selection

CMs shall be nominated and approved by the GC for one-year terms on an as-needed 
basis, by simple majority vote. The GC shall re-confirm CMs on an annual basis, at
the first meeting following an annual GC election. A CM that wishes to step down 
from their role shall notify the GC at least 30 days before the next GC meeting.

The GC may appoint individuals who are not part of the OpenTelemetry project. 

The GC may dismiss a CM for violations of the project Code of Conduct or a 
failure to uphold the responsibilities of the role.

### Community Manager Rights and Permissions

A CM may act as an extension of the GC in pursuing their responsibilities. Pursuant
to this, the GC should hold CMs accountable for their actions if they reflect poorly
on the project, its contributors, or the CNCF. Thus, CMs should work in collaboration
with the GC, especially if their actions could be construed as controversial. They
will be the point of contact for the CNCF on events, swag, communications, and
other programs as needed. Thus, they will have access to Service Desk. Other
permissions (for example, repository creation and management) can be granted by
the GC on an as-needed basis.
