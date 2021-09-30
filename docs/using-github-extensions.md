# Using GitHub Apps, Extensions, and bots

In OpenTelemetry it is critically important to preserve code integrity, including copyright.

Extensions, apps, or bots that can **arbitrarily modify code are NOT allowed**. Read-only code access, opening pull requests from another fork, or bug triage bots can be considered to be installed.

## Requesting installing of Apps, Extensions, or bots

- The default answer for installing third party tools in the org is "NO". Justification needs to be provided and supported by multiple org members.
- Open an issue at https://github.com/open-telemetry/community/issues
  - Include reasoning and SIG(s) requesting this
  - Requests from maintainers typically carry higher weight; please make sure to discuss in the SIG you participate.
  - List permissions required by this extension, app, or bot.
  - If possible: point to other uses of this extensions in OSS.
- GC member needs to approve with no other GC members raising concerns. It is recommended to discuss each extension, app, or bot that is about to be installed at GC meeting for awareness.
- Once GC approval received, TC member will install the extension.

## Writing your GitHub Actions pipelines

Many GitHub Action workflows do not require a dedicated GitHub account. Good examples are auto-assign workflows for issues and PRs such as [the one used in specifications repo](https://github.com/open-telemetry/opentelemetry-specification/blob/main/.github/workflows/auto-assign-issue.yml).

There are cases when a dedicated account is needed to perform some higher privilege operations. In this cases the recommendation for maintainers is to use their accounts. See [example](https://github.com/open-telemetry/opentelemetry-specification/blob/main/.github/workflows/publish-schemas.yml).

Bot accounts are not recommended, as they require special work to pass CLA checks. If pushing automatically-generated, non-copyrightable code using a bot account is required, an explanation should be sent to the Governance Committee for review and forwarding to the EasyCLA team to exempt the bot's commits from the CLA requirement.

OpenTelemetry does not provide org-level access bot accounts. See discussion here: [open-telemetry/community#551](https://github.com/open-telemetry/community/issues/551).

## Creating your own GitHub extensions for OpenTelemetry

We didn't encounter these requests yet. The policy will be created once it will become a problem.
