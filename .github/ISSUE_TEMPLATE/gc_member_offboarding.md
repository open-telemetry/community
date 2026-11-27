---
name: GC Member Offboarding
about: Offboard a departing member of the Governance Committee
title: 'GC OFFBOARDING: <GH_USERNAME>'
labels: area/gc-election
assignees: ''
---

<!-- Please remember to change the title of this issue by replacing
<GH_USERNAME> with the actual GitHub username of the GC member to be
offboarded. -->

This issue should be assigned to both an existing member and the departing
member. It reverses the steps of the
[GC Member Onboarding](https://github.com/open-telemetry/community/blob/main/.github/ISSUE_TEMPLATE/gc_member_onboarding.md)
template. Membership in the `open-telemetry` organization and any roles outside
the GC are not affected.

The issue should be `Closed as completed` after all steps have been completed.

## Community

The existing member must:

- [ ] Invite the departing member to [opentelemetry-gc-alum](https://cloud-native.slack.com/archives/C02KBUGC685)
  on CNCF Slack.
- [ ] Remove the departing member from the `governance-committee` team in
  [open-telemetry/community/people.yml](https://github.com/open-telemetry/community/blob/main/people.yml)
  and from [CODEOWNERS](https://github.com/open-telemetry/community/blob/main/CODEOWNERS),
  and add them to the Governance Committee Emeritus list in
  [community-members.md](https://github.com/open-telemetry/community/blob/main/community-members.md).
- [ ] Reassign the SIGs where the departing member is `gcLiaison` in
  [workstreams.yml](https://github.com/open-telemetry/community/blob/main/workstreams.yml),
  or set them to `tbd` until a new liaison is found. `make validate-sigs` fails
  if a liaison is not in the `governance-committee` team. Run `make generate`
  afterwards.
- [ ] Transfer ownership of any asset in
  [assets.md](https://github.com/open-telemetry/community/blob/main/assets.md)
  owned by the departing member.

## Access Revocation

The existing member must:

- [ ] Remove the departing member from the `Owners` group in
  [OpenTelemetry 1Password](https://opentelemetry.1password.com).
- [ ] Remove the departing member from the following private Slack channels:
  - [opentelemetry-gc](https://cloud-native.slack.com/archives/C01S673T1NE)
  - [opentelemetry-gc-tc](https://cloud-native.slack.com/archives/C02KF2PPUV9)
  - [opentelemetry-gc-end-user](https://cloud-native.slack.com/archives/C065JSPJN15)
- [ ] Send an email to cncf-maintainer-changes@cncf.io to request removal from:
  - https://lists.cncf.io/g/cncf-opentelemetry-governance
  - https://lists.cncf.io/g/cncf-opentelemetry-announce (moderator)
  - the [FOSSA OpenTelemetry Team](https://app.fossa.com/account/settings/organization/teams/78675)
- [ ] Open a ticket with [LF support](https://support.linuxfoundation.org/)
  requesting removal of the departing member's role on the OpenTelemetry project
  in the [LFX Project Control Center](https://projectadmin.lfx.linuxfoundation.org).
  Roles cannot be removed self-serve (see
  [user permissions](https://docs.linuxfoundation.org/lfx/project-control-center/v2-latest-version/operations/user-permissions)).
  Afterwards, validate they are no longer listed under Operations > User
  permissions.
- [ ] Remove the departing member from https://lists.cncf.io/g/cncf-otel-zoomadmins
  if they are still a member. The list is only used for the
  [deprecated Zoom accounts](https://github.com/open-telemetry/community/blob/main/assets.md#deprecated-zoom-accounts).
- [ ] Ask TC to remove the departing member from the
  [open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
  team.
- [ ] Merge the bot PRs that sync the `open-telemetry/governance-committee` team
  to CNCF's maintainer records. They are created daily, first in
  [open-telemetry/opentelemetry.io](https://github.com/open-telemetry/opentelemetry.io/pulls?q=is%3Apr+%22Update+community+members%22)
  and then in [open-telemetry/.project](https://github.com/open-telemetry/.project/pulls).
  Validate the departing member is no longer listed in the `servicedesk` team of
  [maintainers.yaml](https://github.com/open-telemetry/.project/blob/main/maintainers.yaml).
  This removes their Service Desk access and, unless they are still a
  maintainer elsewhere in OpenTelemetry, their access to
  https://lists.cncf.io/g/cncf-opentelemetry-maintainers.
- [ ] Remove the departing member from the `governance-committee@opentelemetry.io`
  Google group. This also removes their access to the GC meeting notes.
- [ ] Remove the departing member from the Governance Committee Meeting and the
  Governance/Technical Committee Joint Meeting invites.

## Departing Member

The departing member must:

- [ ] Confirm they no longer receive GC mailing list emails or OpenTelemetry
  CNCF Service Desk requests.
