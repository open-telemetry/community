# Writing a Good GitHub Issue

Most issues that sit without a response for weeks aren't controversial or
complex. They just don't have enough to go on.

All issue activity is governed by the
[OpenTelemetry Code of Conduct](../../code-of-conduct.md).

## Table of Contents

- [Before You Open an Issue](#before-you-open-an-issue)
- [Writing the Issue](#writing-the-issue)
  - [Title](#title)
  - [Description](#description)
  - [Linking Related Issues](#linking-related-issues)
- [Connecting Issues to Pull Requests](#connecting-issues-to-pull-requests)
- [Labels](#labels)
- [Signaling Intent to Work on an Issue](#signaling-intent-to-work-on-an-issue)

## Before You Open an Issue

Search first. Duplicate issues split the conversation and make it harder to
track what's already been decided. If an existing issue covers what you're
seeing, react to it to signal that it affects you and add any new details
as a comment, rather than opening a duplicate. OpenTelemetry uses issue
reactions to assess priority; see the
[issue participation guide](https://opentelemetry.io/community/end-user/issue-participation/)
for details.

For support questions and "is this expected behavior" checks, use
[Slack](https://cloud-native.slack.com/archives/CJFCJHG4Q). Issues are for
bugs and feature requests.

If you're reporting a security vulnerability, do not open a public issue.
Use the repository's security policy (the "Security" tab on the repo page)
to report it privately.

## Writing the Issue

If the repository uses issue templates and the template includes a footer, leave it in place.

### Title

Describe the problem, not your reaction to it. Be specific about what and
where:

- `Connection retries don't honor the configured backoff interval`
- `API docs don't mention the maximum allowed payload size`

Titles like "it's broken" or "docs are wrong" don't help triagers and make
the issue impossible to find later.

If the repo has a title convention (some use a `[component/name]` prefix,
others don't), follow it.

### Description

Say what you expected and what actually happened. These are often different
in ways that matter, and the gap is usually the bug.

Include steps to reproduce, written as if the reader has never seen your
setup. A minimal config that still triggers the issue beats a full
production config with everything redacted. Log output and stack traces go
in code blocks, not screenshots, because text is searchable and copyable.

When the environment might matter, include:

- the component or SDK version
- the runtime version (Go, Java, Python, etc.)
- the OS and architecture

For feature requests, lead with the problem you're trying to solve, not the
solution you have in mind. That leaves room for someone to suggest an
approach you hadn't considered.

### Linking Related Issues

If your issue is a follow-up to an existing issue or a Slack thread, say so
near the top of the description. GitHub renders `#NNN` as a link within the
same repository. For cross-repository references, use the full URL:

```
This is a follow-up to #1234.

Related: https://github.com/<org>/<other-repo>/issues/1234
```

This one habit saves a lot of time reconstructing context later.

## Connecting Issues to Pull Requests

If your pull request fixes an issue, use one of GitHub's
[closing keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
in the PR description:

```
Fixes #1234
```

When the PR merges into the default branch, GitHub closes the issue, and
anyone who finds the issue later gets a direct link to the fix.

If the PR is related to an issue but doesn't fully resolve it, use a plain
mention instead:

```
Part of #1234
```

That creates the cross-reference without triggering auto-close.

## Labels

You don't need to apply labels yourself. Triagers handle that. Knowing what
the common ones mean helps you find work.

| Label | What it means |
|---|---|
| `good first issue` | A good starting point for someone new to the codebase. Maintainers have agreed to help if you get stuck. Scope should be narrow and described clearly in the issue. |
| `help wanted` | Contributions welcome. Usually needs more context than a good first issue. |
| `bug` | Confirmed or suspected unintended behavior. |
| `enhancement` | New capability, or an improvement to existing behavior. |
| `question` | Needs clarification before anyone can act on it. |

If a `good first issue` turns out to be larger than it looked, say so in a
comment. Maintainers can re-label it and help adjust the scope.

## Signaling Intent to Work on an Issue

Issues can only be assigned to org members and repository collaborators,
because of how GitHub permissions work. If you want to take something on,
leave a comment:

> I'd like to work on this. I'll have a draft up by end of next week.

That's enough to claim it without blocking anyone. If you get stuck or can't
continue, drop a note in the thread so others know it's available again.
