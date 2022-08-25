# OpenTelemetry Governance Committee Charter

Last updated: August 2022

## Overview

This document describes the bootstrapping process for the OpenTelemetry
Governance Committee. It describes the formation of the initial governance
committee and its core responsibilities. This includes its governance processes
and processes to reform itself as necessary.

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
  the project](https://github.com/cncf/toc/blob/master/proposals/opentelemetry.adoc)
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

### Establishment of a governance committee

To bootstrap the process of OpenTelemetry governance, 5 individuals (Ben
Sigelman, Bogdan Drutu, Sergey Kanzhelev, Sarah Novotny, and Yuri Shkuro) were
identified to be the *Bootstrap Committee*, to provide the initial process that
can bootstrap the remainder of the process.

The Bootstrap Committee will be replaced by the elected OpenTelemetry Governance
Committee. Ultimately, the **OpenTelemetry Governance Committee will consist
of 9 individual members** of the community **elected for 2 year terms**. The
terms will be **staggered with 1 year elections** (alternating 4 seats and 5
seats).

To provide a level of continuity as this process is established, the initial
committee will include continuity members, expanding the size to 9 members.
Note that from the 2020 election to the 2021 election, the committee will
include 11 members.

In 2019 as this approval is enacted, the committee consists of the
members of the bootstrap committee (Ben Sigelman, Bogdan Drutu, Sarah Novotny,
Sergey Kanzhelev, Yuri Shkuro) plus 4 positions to be elected from the
community. Of the 4 members that are elected, 2 will have a two year term and 2
will have one year term. 

One year later (in 2020) there will be an election to fill the two seats
opening up, each with a two year term. The continuity members of the original
bootstrap committee will continue to serve.

One year after that (2021), there will be an election to fill the 5 open
seats on the governance committee. The previous continuity members are
eligible to run for these seats.

The committee will continue to iterate with alternating elections of four and
five members each year. 

For clarity, a table describing this process is given below:

| *Year* | *Continuity* | *Election Cohort #1*    | *Election Cohort #2*    | GC size post-election |
| ------ | ------------ | ----------------------- | ----------------------- | --------------------- |
| 2019   | 5 people     | **2 people** (2yr term) | **2 people** (1yr term) | 9 people (+4)         |
| 2020   | -            | -                       | **4 people** (2yr term) | 11 people (-2, +4)    |
| 2021   | 0 people     | **5 people** (2yr term) | -                       | 9 people (-7, +5)     |
| 2022   | -            | -                       | **4 people** (2yr term) | 9 people (-4, +4)     |
| 2023   | -            | **5 people** (2yr term) | -                       | 9 people (-5, +5)     |

## Elections

*Special note*: The bootstrap committee pledges to recuse itself from any direct
election activities while they serve as continuity members. Members of the
bootstrap committee will refrain from endorsing or otherwise advocating for any
candidate (with the exception that the members of the bootstrap committee may
vote in the elections, and may choose to run in the 2021 election).

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

The bootstrap committee explicitly believes that this heuristic will be
inaccurate and not represent the entire community. An exception form will be
provided for people who have contributed to the project but may not meet these
criteria. Exception eligibility applications will be approved by the bootstrap
committee by a simple majority vote. The exception process will be used as data
points for refining the criteria for the future.

Within its first year, the Governance Committee will redefine these criteria
around a more robust idea of community membership.

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

### Initial Election

Because of the need to bootstrap a staggered election cycle, some of the initial
committee members will only serve a single year term. These two people will be
selected from the "lowest vote getters" from the four non-continuity committee
members in the initial election.

The bootstrap committee will operate the election and circulate a timeline for
nominations, and the vote.

### Special Elections

In the event of a resignation or other loss of a governance committee member, a
special election for that position will be held as soon as possible. The same
group of people as described in "eligibility for voting" will vote in the
special election. A committee member elected in a special election will serve
out the remainder of the term for the person they are replacing, regardless of
the length of that remainder. If a continuity member resigns or otherwise is
lost from the Committee, that position will not be filled.

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
