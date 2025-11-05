---
name: GC Member Onboarding
about: Onboard a new member of the Governance Committee
title: 'GC ONBOARDING: <GH_USERNAME>'
labels: area/onboarding
assignees: ''
---

<!-- Please remember to change the title of this issue by replacing
<GH_USERNAME> with the actual GitHub username of the GC member to be
onboarded. -->

This issue should be assigned to both an existing member and a newly elected
member, and the actions should be performed by both in collaboration. This
ensures fluid communication and a successful onboarding into the
OpenTelemetry Governance Committee.

The issue should be `Closed as completed` by the new member after all steps
have been completed.

## Assumptions
These assumptions ensure that the rest of the guide can be followed
successfully.

The existing member must:

1. Have the necessary privileges to perform the actions listed below.

The new member must:

1. Be familiar with basic OpenTelemetry concepts
   1. [Mission, Vision and Values](https://opentelemetry.io/community/mission/)
   2. [Concepts](https://opentelemetry.io/docs/concepts/)
   3. [Specification](https://opentelemetry.io/docs/specs/otel/)
2. Have read and agreed to comply with the
   [OpenTelemetry Governance Committee Charter](../../governance-charter.md)
   as per requirements to stand for election.
3. Have an email address, Google account, and GitHub account and is willing
   to share those details with other GC members.
   1. **Note**: Google account is mainly needed for Google Docs, but one may
      prefer to use work email or personal email for calendar invites.


## Access Grants
This section ensures that the new member has access to all systems and has the
necessary privileges to perform their role as a member of the GC.

### 1Password
1Password contains credentials for accounts managed by the GC as a group (i.e.
not personal items).

The existing member must:

- [ ] Invite new member to [OpenTelemetry 1Password](https://opentelemetry.1password.com)
      via email.
- [ ] After invite is accepted, add them to the `Owners` group as a `Manager`.

The new member must:

- [ ] Accept invitation and create new account on [OpenTelemetry 1Password](https://opentelemetry.1password.com).
- [ ] Validate they have `Manager` access to `Owners` group, and that the group
      contains only current GC members.
- [ ] Validate they have `Full Access` to the `OpenTelemetry Governance` vault.
      This should be given automatically via the `Owners` group.

### CNCF Slack
The main async medium for GC and TC members to communicate is a set of private
channels on Slack.

The existing member must:

- [ ] Add new member to the following private channels:
  - [opentelemetry-gc](https://cloud-native.slack.com/archives/C01S673T1NE)
  - [opentelemetry-gc-tc](https://cloud-native.slack.com/archives/C02KF2PPUV9)
  - [opentelemetry-gc-alum](https://cloud-native.slack.com/archives/C02KBUGC685)
  - [opentelemetry-gc-end-user](https://cloud-native.slack.com/archives/C065JSPJN15)

The new member must:

- [ ] Create a [CNCF Slack](https://slack.cncf.io/) account if they do not
  already have one.

### CNCF Service Desk and Mailing Lists
Interactions between the OpenTelemetry GC and CNCF are mostly driven via Service
Desk tickets. Members can create tickets to discuss access to systems, licensing,
funds, marketing, press, etc.

The existing member must:

- [ ] Send an email to cncf-maintainer-changes@cncf.io to request invitations to the Service Desk
      and mailing lists for the new member
      - https://lists.cncf.io/g/cncf-opentelemetry-governance (moderator)
      - https://lists.cncf.io/g/cncf-opentelemetry-announce (moderator)
      - https://lists.cncf.io/g/cncf-opentelemetry-maintainers (member)

The new member must:

- [ ] Accept invitation to CNCF Service Desk and create an account.
- [ ] Validate they have access to the [CNCF Service Desk](https://cncfservicedesk.atlassian.net/servicedesk/customer/portals)
  (see more information about Service Desk in the [docs](https://github.com/cncf/servicedesk#readme)).
- [ ] Validate they have access to [OpenTelemetry Requests](https://cncfservicedesk.atlassian.net/servicedesk/customer/user/requests?page=1&reporter=org-31).
- [ ] Accept invitations to mailing lists above, creating an account on https://lists.cncf.io
  if necessary, using their preferred email address.

### Additional Mailing List

The existing member must:

- [ ] Invite new member as `Moderator`, ensuring that they have the same
  privileges as existing members, to the following mailing list:
  - https://lists.cncf.io/g/cncf-otel-zoomadmins

The new member must:
- [ ] Accept invitations to mailing list above, creating an account on https://lists.cncf.io
  if necessary, using their preferred email address.

### GitHub
Most of the management, enablement, support and documentation work done by GC
members happens on GitHub.

The existing member must:

- [ ] Ask TC to add new member as `Member` to the [open-telemetry](https://github.com/open-telemetry/)
  organization.
- [ ] Ask TC to add new member as `Member` to the [open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
  team.
- [ ] Add new member as code owner in [open-telemetry/community](https://github.com/open-telemetry/community/blob/main/CODEOWNERS)
- [ ] Add new member to the list of GC members in [open-telemetry/community/community-members.md](https://github.com/open-telemetry/community/blob/main/community-members.md).
- [ ] Add new member in the `OpenTelemetry (Governance Committee)` section of [cncf/foundation/project-maintainers.csv](https://github.com/cncf/foundation/blob/main/project-maintainers.csv)

### Google Drive
OpenTelemetry handles minutes and other ad-hoc documents in Google Drive.

The existing member must:

- [ ] Give new member write access to:
  - [OpenTelemetry Governance Committee meeting notes](https://docs.google.com/document/d/1-23Sf7-xZK3OL5Ogv2pK0NP9YotlSa0PKU9bvvtQwp8)
- [ ] Add email from the new member to the `governance-committee@opentelemetry.io` Google group.

The new member must:

- [ ] Validate they have write access to the documents listed above.

_Note: Confidential documents shared only between GC members are stored under the admin google account and never shared with private accounts. To see/edit them, you must login into the admin google account._

### Zapier
Zapier is used to sync meeting recordings from Zoom to a publicly viewable
Google spreadsheet (see https://github.com/open-telemetry/community/blob/main/docs/how-meeting-recordings-upload-works.md
for more details).

The new member must:
- [ ] Validate they can log in to https://zapier.com with the credentials in 1Password.

### FOSSA
The CNCF FOSSA Service is a static code checker that codifies and monitors the project's compliance with the [CNCF's 3rd Party License policy](https://github.com/cncf/foundation/blob/main/policies-guidance/allowed-third-party-license-policy.md#cncf-allowlist-license-policy).

The existing member must:

- [ ] Send an email to cncf-maintainer-changes@cncf.io to request invitation of the new member to [FOSSA](https://app.fossa.com/)
- [ ] After invite is accepted, add them to the [OpenTelemetry Team](https://app.fossa.com/account/settings/organization/teams/78675).

The new member must:

- [ ] Accept invitation and create account.
- [ ] Validate they are in the [OpenTelemetry Team](https://app.fossa.com/account/settings/organization/teams/78675).

## Meetings and Ceremonies
As per GC charter, all members are expected to attend the following meetings:

- Governance Committee Meeting (every [Wednesday 8:00 Pacific Time](https://dateful.com/convert/pst-pdt-pacific-time?t=0800)).
- Governance/Technical Committee Joint Meeting (every second Wednesday of the month,
  coinciding with the Governance Committee Meeting).

The dates and times of these meetings may be discussed and updated after every
election cycle to accommodate time zones and scheduling requirements of attendees.

The existing member must:
- [ ] Invite the new member to the meetings using the new members' preferred
  email address.

## Further Reading
The following is a list of documents and other media that new members must
familiarize themselves with. The new member must go through these media and ask
any relevant questions that will aid them in understanding their role as a GC
member. The existing member must assist the new member, to the best of their
capacity, in finding answers to these questions.

- [ ] [OpenTelemetry Code of Conduct](https://github.com/open-telemetry/community/blob/main/code-of-conduct.md):
  all GC members define, evolve, and defend the Code of Conduct.
- [ ] [OpenTelemetry Governance Committee meeting notes](https://docs.google.com/document/d/1-23Sf7-xZK3OL5Ogv2pK0NP9YotlSa0PKU9bvvtQwp8):
  to identify items currently in progress. [Meeting Recordings](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s)
  can help get more details if needed.
- [ ] [Project Management](https://github.com/open-telemetry/community/blob/main/project-management.md):
  to understand the fundamentals of how projects are managed by the GC and TC.
- [ ] [Active Projects](https://github.com/open-telemetry/community/tree/main/projects):
  to understand current project deliverables and the challenges they aim to
  solve.
- [ ] [Projects](https://github.com/open-telemetry/community/projects?query=is%3Aopen):
  understand the current state of the projects listed in the previous item.
- [ ] [Community repo docs](https://github.com/open-telemetry/community/tree/main/docs):
  for instructions on how to work with calendars, configuring repositories,
  uploading recordings, etc. As a GC member, it is useful to know that these 
  docs are there when needed.
- [ ] [Inclusive Open Source Community Orientation (LFC102)](https://training.linuxfoundation.org/training/inclusive-open-source-community-orientation-lfc102/):
  this free orientation course is designed to provide you with essential
  background knowledge and practical skills to create an inclusive culture
  in the open source community. Members of the GC may take this course in
  support of our community values.
