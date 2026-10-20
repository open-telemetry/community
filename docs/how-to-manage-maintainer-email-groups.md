# How to manage maintainer email groups

Maintainer email groups provide shared `*-maintainers@opentelemetry.io` contact
addresses for security reports and external services. They accept email from
non-members while keeping conversations and membership details private to members.

## Requesting a group

Open an [issue in the community repository](https://github.com/open-telemetry/community/issues/new/choose)
with the requested address, its purpose, and the corresponding GitHub maintainer
team. Confirm recipients' preferred email addresses privately, for example by
Slack direct message. Do not post recipient lists in public issues.

## Creating and configuring a group

Use the [Google Workspace admin account](../assets.md#google-workspace-accounts)
to create the group in [Google Groups](https://groups.google.com/), selecting the
`opentelemetry.io` domain.

Keep `admin@opentelemetry.io` as an **Owner**, but set its subscription to
**No email** so it does not receive routine group messages. Add maintainers or
their designated contacts as **Managers**, subscribed to **Each email**, so they
can receive messages and manage membership without using the shared admin account.

Use the following recommended configuration for new maintainer groups.
Existing groups may have different settings.

| Setting | Value |
| --- | --- |
| Who can see group | Organization members |
| Who can join group | Invited users only |
| Allow external members | On |
| Who can modify group details | Group owners and managers |
| Who can view conversations | Group members |
| Who can post | Anyone on the web |
| Who can view members | Group members |
| Who can manage members | Group owners and managers |
| Who can modify custom roles | Group owners and managers |
| Who can view member email addresses | Group members |
| Allow Email Posting | On |
| Allow web posting | On |
| Conversation history | On |
| Message moderation | No moderation |
| New member restrictions | No posting restriction for new members |
| Spam message handling | Moderate and notify content moderators |
| Enable additional Google Groups features | No additional features |

In this table, **Group members** includes owners and managers.
The group is discoverable within the Workspace organization, but non-members
cannot read conversations or view membership details.

External posting and external membership are separate settings. Allowing anyone
to post lets researchers and external services email the group without joining.
Allowing external members lets maintainers receive those messages at addresses
outside `opentelemetry.io`.

Save changes and reopen the settings and member list to confirm the permissions,
roles, and subscriptions. Before relying on the address, send a test message from
an external address and confirm that maintainers receive it.

## Maintaining membership

Group owners and managers can add and remove recipients through the group's
**Members** page. New recipients should normally be subscribed to **Each email**.
Give the **Manager** role to people responsible for maintaining the recipient list.

Keep membership aligned with the corresponding GitHub maintainer team. Do not
assume that changes to a GitHub team automatically update Google Group membership.
Review the recipient list when maintainers join or leave.
