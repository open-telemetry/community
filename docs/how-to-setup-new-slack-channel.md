# How we setup new Slack channels

## Naming

Most channels have a name pattern like `#otel-*`. We recommend that pattern
for consistency.

## Channel Settings

The following channel settings help users to understand what a channel is
for and how to quickly access common resources.

### Topic

Describe in a few words what the purpose of this channel is. Assume that end users might not be aware that
`#otel-foo` is the channel of the OpenTelemetry Foo SIG, or what this SIG is doing. A few examples:

- `Discussion of the Java implementation of OpenTelemetry, including the javaagent and instrumentation`
- `Discussion of the OpenTelemetry specification`
- `OpenTelemetry semantic conventions in the security domain`
- `OpenTelemetry Contributor Experience SIG: Improving the experience for those who contribute to OpenTelemetry`

### Description

If the topic field does not provide enough space to write out what your channel is about, you can provide
a more detailed description, otherwise leave it empty.

### Channel Manager

Make sure that all maintainers of your SIG are set as [Channel Managers](https://slack.com/help/articles/8328303095443-Understand-Channel-Managers-in-Slack).
The person who creates the channel, will be a Channel Manager by default and can invite the maintainers.

Do also make the [`OpenTelemetry Admin`](https://cloud-native.slack.com/archives/D07EGBA9V6E) user a Channel Manager.
[The Governance Committee manages this shared account](../assets.md#slack).

### Bookmarks

If the channel is for a specific SIG add bookmarks for the following resources:

- Meeting Notes (Google Docs, `https://docs.google.com/document/d/<id>`)
- Project Board (GitHub, `https://github.com/orgs/open-telemetry/projects/<id>`)
- Get Meeting Invites (Google group for calendar invites, `https://groups.google.com/a/opentelemetry.io/g/calendar-<name>`)
- Issue Tracker (GitHub, `https://github.com/open-telemetry/<reponame>/issues`)

Feel free to add any other link you think is helpful for users to interact with
your SIG, or links that help your triagers, approvers and maintainers for quick access.

### Workflows

You can add workflows to your channel, e.g.

- A reminder for an upcoming SIG meeting
- A welcome message to new users
