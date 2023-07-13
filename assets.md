# OpenTelemetry managed assets

This file is intended to list all the assets controlled by OpenTelemetry.

## Credential Storage

- [1Password Teams](https://1password.com/)
  - Team account: https://opentelemetry.1password.com/
  - https://github.com/1Password/1password-teams-open-source#opentelemetry
  - PR: https://github.com/1Password/1password-teams-open-source/pull/364
  - Admin: Alex Boten @codeboten

## Artifact repositories

### NuGet OpenTelemetry organization

Link: https://www.nuget.org/organization/OpenTelemetry

- All .NET SIG maintainers are administrators of this organization.
- Organization e-mail (cncf-opentelemetry-net-maintainers@lists.cncf.io) is owned by CNCF.

### MyGet OpenTelemetryCNCF account

Link: https://www.myget.org/feed/Packages/opentelemetry

- registered under the service account (cncf-opentelemetry-net-maintainers@lists.cncf.io).
- Individual accounts of .NET SIG maintainers are administrators of the OpenTelemetry feed.
- Admin: [manage members](https://www.myget.org/feed/Security/opentelemetry).

### NPM OpenTelemetry Organization

Link: https://www.npmjs.com/settings/opentelemetry/packages

- Ask any of the following people if you need access
- Owner: Mayur Kale @mayurkale22
- Admin: Daniel Dyla @dyladan
- Member: Bogdan Drutu @bogdandrutu

### Maven

Link: https://repo1.maven.org/maven2/io/opentelemetry/

Maven doesn't have the concept of an "organization account",
but these individual OpenTelemetry members have been given rights to publish under `io.opentelemetry`:
* [@bogdandrutu](https://github.com/bogdandrutu)
* [@carlosalberto](https://github.com/carlosalberto)
* [@jack-berg](https://github.com/jack-berg)
* [@trask](https://github.com/trask)

## Communication channels

### opentelemetry-calendar-contributors Google Group

Used to provide write access to public OpenTelemertry calendar. See [docs/how-to-handle-public-calendar.md](docs/how-to-handle-public-calendar.md).

Link: https://groups.google.com/g/opentelemetry-calendar-contributors

- Owners: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
- Members: SIG maintainers and individuals appointed by maintainers

### OpenTelemetry Calendar Invites Google Group

Used to automatically invite members to all OpenTelemetry calendar events, so that time is blocked on their calendars.

Link: https://groups.google.com/g/opentelemetry-calendar

- Owners: @mtwo

### Mailing list cncf-opentelemetry-net-maintainers@lists.cncf.io

- Used to register service accounts and as a NuGet OpenTelemetry organization e-mail. All .NET SIG maintainers are part of this list. Owned by CNCF.
- Admin: [add member](https://lists.cncf.io/g/cncf-opentelemetry-net-maintainers/).

### Mailing list cncf-opentelemetry-ruby@lists.cncf.io

- Used as a service account e-mail for Ruby SIG. All Ruby SIG maintainers [@open-telemetry/ruby-maintainers](https://github.com/orgs/open-telemetry/teams/ruby-maintainers) are moderators of this list. Owned by CNCF.
- Moderators: [add member](https://lists.cncf.io/g/cncf-opentelemetry-ruby/members).

### Mailing list cncf-opentelemetry-governance@lists.cncf.io

- Private mailing list for OpenTelemetry Governance Committee.
- All GC members AND CNCF reps (Amye Scavarda Perrin, Chris Aniszczyk, Taylor Waggoner) are on the list and are list moderators.
- Admin: [add member](https://lists.cncf.io/g/cncf-opentelemetry-governance/members).

### YouTube channel OpenTelemetry

Link: https://www.youtube.com/channel/UCHZDBZTIfdy94xMjMKz-_MA/videos

- Ask any of the following people if you need to manage the feed:
  - Owners: Amye Scavarda Perrin (CNCF rep), Sergey Kanzhelev
  - Managers: Alolita Sharma, Alan West, Austin Parker, Ben Sigelman, Eddy Nakamura

### Zoom accounts

- Accounts
  - cncf-opentelemetry@cncf.io
  - cncf-opentelemetry-meeting-1@cncf.io
  - cncf-opentelemetry-meeting-2@cncf.io
  - cncf-opentelemetry-meeting-3@cncf.io
  - cncf-opentelemetry-meeting-4@cncf.io
- Owned by: Amye Scavarda Perrin (CNCF rep)
- Admins: [@austinlparker](https://github.com/austinlparker), [@eddynaka](https://github.com/eddynaka),
  and [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
- Note: while the account passwords are available in the Governance Committee 1Password, logging in from a new IP
  address will require being a member https://lists.cncf.io/g/cncf-otel-zoomadmins with admin rights so you can see
  pending (unapproved) messages and retrieve the One-Time Password that is sent when you log in.
  To join https://lists.cncf.io/g/cncf-otel-zoomadmins and get admin rights, open a
  [CNCF ServiceDesk](https://cncfservicedesk.atlassian.net/).

### Splain account

Link: https://splain.io/

- Used to upload Zoom meeting recordings to Youtube
- Owned by: Amye Scavarda Perrin (CNCF rep)

### Project Google account: cncf-opentelemetry-governance@lists.cncf.io

- Used to manage the OpenTelemetry community calendar and Zoom
- Owned by the governance committee

## Bot accounts

### Easy CLA

This is not really an OpenTelemetry asset as we do not have any credentials or admin access for it.

For support:
* Open an [OpenTelemetry community issue](https://github.com/open-telemetry/community/issues/new/choose)
* Ask in the [`#easycla`](https://cloud-native.slack.com/archives/CK8QVEXQB) Slack channel
* Open an [EasyCLA Jira ticket](https://jira.linuxfoundation.org/plugins/servlet/desk/portal/4/create/143)

### Docker Hub

- We publish images from CI to Docker hub using https://hub.docker.com/u/otelbot account. The bot is registered using cncf-opentelemetry-tc@lists.cncf.io email address and Technical Committee members are owners of this account. The Admin for bot security credentials for CI is @tigrannajaryan

### OpenTelemetry Bot

This is a community-owned bot account that you can use when automating common GitHub tasks
(e.g. release automation tasks).

Important: You do not need to (and should not) give this account any permissions to any OpenTelemetry repository.

Link: [@opentelemetrybot](https://github.com/opentelemetrybot)

- Admins: [@trask](https://github.com/trask) and
  [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
  (GitHub password and associated 2FA for the `@opentelemetrybot` account are available in the OpenTelemetry Governance
  1Password)
- Admins for the associated GitHub organization secret:
  [@open-telemetry/technical-committee](https://github.com/orgs/open-telemetry/teams/technical-committee)

The OpenTelemetry Bot addresses two common issues:

1. Since you can't push directly to `main` from workflows (due to branch protections), the next best thing is to
   generate a pull request from the automation and use an account which has signed the CLA as the commit author.

   The OpenTelemetry Bot account has signed the CNCF CLA, and you can assign it as the commit author in your automation:

   ```
   git config user.name opentelemetrybot
   git config user.email 107717825+opentelemetrybot@users.noreply.github.com
   ```

   It is recommended to push to branch names that start with `opentelemetrybot/`, and to add a branch protection
   rule for `opentelemetrybot/**/**` with the same setup as documented for
   [`dependabot/**/**`](https://github.com/open-telemetry/community/blob/main/docs/how-to-configure-new-repository.md#branch-protection-rule-dependabot). Note that branch protection rule ordering matters, so you will need to
   delete the `**/**` branch protection rule temporarily, then add the `opentelemetrybot/**/**` branch protection
   rule, then add back the `**/**` branch protection rule.

2. When you use the built-in `secrets.GITHUB_TOKEN` to generate a pull request from inside of a GitHub Action, workflows
   will not run on that new pull request without closing and re-opening it manually (this limitation is in place to
   prevent accidental recursive workflow runs).

   The OpenTelemetry GitHub organization has a GitHub Action secret named `OPENTELEMETRYBOT_GITHUB_TOKEN`, which is a
   [Personal Access Token][] for [@opentelemetrybot](https://github.com/opentelemetrybot) with `public_repo`
   scope for the OpenTelemetry Bot that you can use to bypass this limitation.

   The personal access token also has `workflow` scope which is needed when merging upstream changes of
   `.github/workflow` files into opentelemetrybot's forks (these forks are used for automatically opening PRs against
   external repos).

   Maintainers can open an issue in the community repository to have their repository granted access to this
   organization secret.

   [Personal Access Token]: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
