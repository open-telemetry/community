# Using GitHub Apps, Extensions, and bots

In OpenTelemetry it is critically important to preserve code integrity, including copyright.

Extensions, apps, or bots that can **arbitrarily modify code are NOT allowed**. Read-only code access, opening pull requests from another fork, or bug triage bots can be considered to be installed.

## Requesting installing of Apps, Extensions, or bots

- The default answer for installing third party tools in the org is "NO". Justification needs to be provided and supported by multiple org members.
- Open an issue at https://github.com/open-telemetry/community/issues
  - Include reasoning and SIG(s) requesting this
  - List permissions required by this extension, app, or bot.
  - If possible: point to other uses of this extensions in OSS.
  - Requests from maintainers typically carry higher weight; please make sure to discuss in the SIG you participate.
  - If a third-party tool is requested for a specific repository, it is recommended to tag that repository's maintainers and ask them to +1 the request, such that there is a consensus among the majority of maintainers on adding the tool.
- GC member needs to approve with no other GC members raising concerns. It is recommended to discuss each extension, app, or bot that is about to be installed at GC meeting for awareness.
- Once GC approval received, TC member will install the extension.

## Writing your GitHub Action workflows

Many GitHub Action workflows do not require a dedicated GitHub account. Good examples are auto-assign workflows for issues and PRs such as [the one used in specifications repo](https://github.com/open-telemetry/opentelemetry-specification/blob/main/.github/workflows/auto-assign-issue.yml).

If your workflow does require a dedicated GitHub account, you should use [@opentelemetrybot](https://github.com/opentelemetrybot).
See [OpenTelemetry Bot documentation](../assets.md#opentelemetry-bot) for more details.

## Creating your own GitHub extensions for OpenTelemetry

We didn't encounter these requests yet. The policy will be created once it will become a problem.
