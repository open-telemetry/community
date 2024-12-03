# OpenTelemetry managed assets

This file is intended to list all the assets controlled by OpenTelemetry.

<!-- Re-generate TOC with `make markdown-toc` -->

<!-- toc -->

- [Credential Storage](#credential-storage)
- [Community Resource Accounts](#community-resource-accounts)
  * [AWS account](#aws-account)
  * [Equinix bare metal](#equinix-bare-metal)
  * [Grafana organization for SIG Security](#grafana-organization-for-sig-security)
  * [Netlify](#netlify)
  * [Oracle Cloud account](#oracle-cloud-account)
- [Artifact repositories](#artifact-repositories)
  * [NuGet OpenTelemetry organization](#nuget-opentelemetry-organization)
  * [MyGet OpenTelemetryCNCF account](#myget-opentelemetrycncf-account)
  * [NPM OpenTelemetry Organization](#npm-opentelemetry-organization)
  * [Crates](#crates)
  * [Maven](#maven)
  * [PyPI](#pypi)
  * [PHP Extras](#PHP-Extras)
- [Communication channels](#communication-channels)
  * [opentelemetry-calendar-contributors Google Group](#opentelemetry-calendar-contributors-google-group)
  * [OpenTelemetry Calendar Invites Google Group](#opentelemetry-calendar-invites-google-group)
  * [Mailing list cncf-opentelemetry-net-maintainers@lists.cncf.io](#mailing-list-cncf-opentelemetry-net-maintainerslistscncfio)
  * [Mailing list cncf-opentelemetry-ruby@lists.cncf.io](#mailing-list-cncf-opentelemetry-rubylistscncfio)
  * [Mailing list cncf-opentelemetry-governance@lists.cncf.io](#mailing-list-cncf-opentelemetry-governancelistscncfio)
  * [YouTube channel OpenTelemetry](#youtube-channel-opentelemetry)
  * [Zoom accounts](#zoom-accounts)
  * [Zapier account](#zapier-account)
  * [Google Workspace accounts](#google-workspace-accounts)
  * [Google account for cncf-opentelemetry-governance@lists.cncf.io](#google-account-for-cncf-opentelemetry-governancelistscncfio)
- [Bot accounts](#bot-accounts)
  * [Easy CLA](#easy-cla)
  * [Docker Hub](#docker-hub)
  * [OpenTelemetry Bot](#opentelemetry-bot)
- [Security](#security)

<!-- tocstop -->

## Credential Storage

- [1Password Teams](https://1password.com/)
  - Team account: https://opentelemetry.1password.com/
  - https://github.com/1Password/1password-teams-open-source#opentelemetry
  - PR: https://github.com/1Password/1password-teams-open-source/pull/364
  - Admins: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)

## Community Resource Accounts

### AWS account

Link: http://cncf-aws-opentelemetry.signin.aws.amazon.com/

- Community account to published Lambda layers
- Admin: Alex Boten @codeboten & Anthony Mirabella @aneurysm9

### Equinix bare metal

Link: https://console.equinix.com/projects/6f1c9af6-0470-42da-8f22-59d0df245f6b

- Reserved bare metal machines for the community to run performance tests and
  other assets on
- Admin: Juraci Paixão Kröhling @jpkrohling and OTel TC via the mailing list address

### GitHub-hosted ARM64 runners

These Linux and Windows ARM64
[GitHub-hosted runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners)
are available to OpenTelemetry repositories:

- `otel-linux-arm64` (4-core)
- `otel-windows-arm64` (4-core)

At the time of writing, both of these runners have a concurrency limit of 20 jobs.

Individual repositories need to be granted access to the runners, so please open a community issue
if you would like to use them.

Note: these pay-as-you-go GitHub-hosted runners for ARM64 are available for free for CNCF projects.
CNCF and GitHub expect fair use of these provided resources.
Please ensure your workloads are optimized to avoid unnecessary usage.

### Google Cloud account

Link: https://cloud.google.com

- Community account to host https://go.opentelemetry.io
- Admin: [@austinlparker](https://github.com/austinlparker)
  (password is available in the OpenTelemetry Governance 1Password)

### Grafana organization for SIG Security

Link: https://grafana.com/orgs/otelsigsecurity

- Used to provide an overview of open security incidents in the org and
  historical data on how quickly we respond to incidents
- Users: SIG-Security Maintainers, Technical and Governance Committees
- Admins: Juraci Paixão Kröhling @jpkrohling & Armin Ruech @arminru

The GitHub organization `open-telemetry-private` also exists for this purpose.

### Netlify

Link: https://app.netlify.com/login

- Used to manage domain names under opentelemetry.io
- Used to publish https://opentelemetry.io
- Admins: [@austinlparker](https://github.com/austinlparker), [@svrnm](https://github.com/svrnm), [@chalin](https://github.com/chalin)

### Oracle Cloud account

Link: https://www.oracle.com/cloud/sign-in.html

- Community account to run [CLOWarden](https://github.com/cncf/clowarden)
- Admin: [@austinlparker](https://github.com/austinlparker)
  (password is available in the OpenTelemetry Governance 1Password)

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

### Crates

Link: https://crates.io/teams/github:open-telemetry:rust-publishers

Owners: [@open-telemetry/rust-publishers](https://github.com/orgs/open-telemetry/teams/rust-publishers)

### Maven

Link: https://repo1.maven.org/maven2/io/opentelemetry/

Maven doesn't have the concept of an "organization account",
but these individual OpenTelemetry members have been given rights to publish under `io.opentelemetry`:
* [@bogdandrutu](https://github.com/bogdandrutu)
* [@carlosalberto](https://github.com/carlosalberto)
* [@jack-berg](https://github.com/jack-berg)
* [@trask](https://github.com/trask)

### PyPI

Link: https://pypi.org/user/opentelemetry/

- Owner: [@codeboten](https://github.com/codeboten)
 
### PHP Extras

##### SIG Extra Repositories: https://github.com/opentelemetry-php

These read only repository clones are used in order to create split-repos, which are necessary for packagist php package publishing.

##### Packagist: https://packagist.org/packages/open-telemetry/

These are the published packages for opentelemetry-php (used by package managers like [composer](https://getcomposer.org))

Owners:

- [@bobstrecansky](https://github.com/bobstrecansky)
- [@brettmc](https://github.com/brettmc)

## Communication channels

### CNCF Community Group

Used by the End-User SIG to organize events (e.g. OTel Q&A, OTel in Practice, feedback sessions, etc.).

CNCF are the owners of the group, so certain requests (e.g. adding/removing organizers) need to be requested via on of these:

* CNCF Service Desk
* https://github.com/cncf/communitygroups/issues

Link: https://community.cncf.io/opentelemetry/

- Owners: CNCF
- Lead Organizers (i.e. admins):
  - [@open-telemetry/sig-end-user-approvers](https://github.com/orgs/open-telemetry/teams/sig-end-user-approvers): listed on group page, registered using their personal CNCF Community accounts.
  - [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee) who can request changes via CNCF Service Desk tickets.


### opentelemetry-calendar-contributors Google Group

Used to provide write access to public OpenTelemetry calendar. See [docs/how-to-handle-public-calendar.md](docs/how-to-handle-public-calendar.md).

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
- Admin: CNCF (via [CNCF Service Desk ticket](https://cncfservicedesk.atlassian.net/servicedesk/customer/portals)).

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
- Admins: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
- Note: while the account passwords are available in the Governance Committee 1Password, logging in from a new IP
  address will require being a member https://lists.cncf.io/g/cncf-otel-zoomadmins with at least moderator rights so you can see
  pending (unapproved) messages and retrieve the One-Time Password that is sent when you log in.
  To join https://lists.cncf.io/g/cncf-otel-zoomadmins, go to that URL and click "Apply For Membership In This Group".
  Then ask in the [#opentelemetry-gc](https://cloud-native.slack.com/archives/C01S673T1NE) for someone to approve your
  membership and then to give you owner rights.

### Zapier account

Link: https://zapier.com

- Used to automatically add links to Zoom meeting recordings to a
  [publicly viewable Google spreadsheet](https://docs.google.com/spreadsheets/d/1SYKfjYhZdm2Wh2Cl6KVQalKg_m4NhTPZqq-8SzEVO6s)
- Used to automatically add repo maintainers to new security incidents
- Admins: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
  (GitHub password is available in the OpenTelemetry Governance 1Password)

### Google Workspace accounts

- Accounts
  - admin@opentelemetry.io
- Admins: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
- Used to manage the OpenTelemetry community calendar
- Used to manage the [Google Custom Search](https://programmablesearchengine.google.com/) for [opentelemetry.io/search](https://opentelemetry.io/search/)

### Google account for cncf-opentelemetry-governance@lists.cncf.io

- Admins: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
- Used for community Google Docs
- Used to manage Zoom

## Bot accounts

Related: [Guidelines for adding new GitHub extensions](./docs/using-github-extensions.md).

### Easy CLA

This is not really an OpenTelemetry asset as we do not have any credentials or admin access for it.

For support:
* Check the [EasyCLA status page](https://status.linuxfoundation.org/)
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

- Admins: [@open-telemetry/technical-committee](https://github.com/orgs/open-telemetry/teams/technical-committee)
  (GitHub password and associated 2FA for the `@opentelemetrybot` account are available in the Technical Committee
  1Password)

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

### Slack

The slack user [`OpenTelemetry Admin`](https://cloud-native.slack.com/archives/D07EGBA9V6E) is community owned and can be
used for self-servicing slack (e.g. as Channel Manager to rename spaces).

- Owners: [@open-telemetry/governance-committee](https://github.com/orgs/open-telemetry/teams/governance-committee)
  (To login, go to <https://cloud-native.slack.com/>, click Sign In With Google and login as <admin@opentelemetry.io>.
  Click `Cancel` when you are asked to open slack in the app, and wait for the link `use Slack in your browser` to be
  available and use that.)

## Security

The SIG Security has access to the following tools, with GC and TC members welcome to request access to them as well.
Find more details under [`tools`](https://github.com/open-telemetry/sig-security/tree/main/tools/) on the [SIG Security
GitHub repository](https://github.com/open-telemetry/sig-security).

* Advisories Dashboard
* Snyk

