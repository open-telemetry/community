# Issue Management for OpenTelemetry

It's an important community goal for OpenTelemetry that our members find the backlogs to be responsive, and easy to take part in. Having a shared methodology for processing issues helps new members understand the current state of each project.

SIGs are encouraged to experiment with labels and backlog management procedures. This document only covers the bare bones of issue management which should work the same across all SIGs, to help maintain a responsive backlog and allow us to track work across all projects in a similar manner.

## New Issues

Flow:
* An issue is filed by a community member.
* A maintainer responds and asks clarifying questions.
* The maintainer processes the issue as a Code Change, a Discussion, or resolves it quickly.

Every new issue should be responded to quickly by a Maintainer, with a greeting and any needed clarifying questions. If assessing the issue requires more information, the Triager collaborates with the OP until workability is determined. If the ticket is a help request with an existing answer, please link to the answer before closing the ticket.

## Code Changes

Flow:
* A new issue is filed, proposing a code change.
* Maintainer labels the issue as `up-for-grabs`; reviewers are assigned.
* `up-for-grabs` becomes `wip` once a Collaborator is assigned.
* Closed once all PRs are accepted.

A ticket becomes `up-for-grabs` once a maintainer deems it is processed sufficiently that work can begin. Issues should be well scoped and have clear goals.

A ticket labeled `up-for-grabs` can be picked up by anyone in the community. Available work can be assigned in the following ways:
* A contributor assigns the ticket to themselves.
* A maintainer assigns the ticket to a contributor.

All tickets transition to `wip` once they have been assigned. If a PR is merged which resolves the issue, the issue can be closed. If work is abandoned, or the contributors otherwise change their minds, the ticket should be closed as `no-further-action`.

## Discussions

Flow:
* A new issue is filed, raising an important question.
* Maintainer labels the issue as `needs-discussion`.
* `needs-discussion` becomes `agreed` when a decision is reached.
* Issue is closed once all action items are complete.

Some issues are not directly related to a particular code change. If a ticket is worth considering in the issue backlog, but not scoped clearly enough for work to begin, then it `needs-discussion`.

* When possible, move the discussion forwards by using tests and code examples.
* If discussion happens elsewhere, record relevant meeting notes into the issue.
* When an agreement is made, clearly summarize the decision, and list any resulting action items which need to be addressed.

## When Issues get Stuck

Flow:
* An existing issue gets stuck due to a lack of response.
* The `stale` label is applied, and the appropriate members contacted.
* If an issue is stuck for an external reason – other than a lack of response – the `blocked` label is applied instead.

We value a responsive backlog, and would like to have SLAs which cover response times for every role in issue processing. When a ticket has violated an SLA, it becomes `stale`.

Common SLAs:
* **Triager**: Daily (Business Days) review of new issues with initial feedback to OP or issue processed within 3 days of last activity.
* **Reviewer**: Provide feedback within 3 days of the last activity on a PR
* **Contributor**: 3 day updates as comments on the PR to indicate activity.

Action items for stale tickets:
* record the SLA details as comment on the ticket.
* @mention the person(s) who can resolve the SLA.

Sometimes, an issue cannot move forwards is due to an external reason or extenuating circumstances. For example, waiting on work to be finished in another project. In these cases, the `blocked` label is used instead. Preferably, issues should be closed, rather than be left for long periods in a `blocked` state.

## Closing an Issue
Any issues which are resolved via a merged pull request can simply be closed.

### `no-further-action`

Not every discussion or feature request results in action. Issues which cannot be addressed at the present moment, or have no further discussion, should be closed. This helps keep the open backlog focused on active discussions.

Possible reasons:
* a prior discussion decided the issue for now.
* a discussion is off topic.
* a feature request is not implementable.

In these cases, close the ticket as `no-further-action`. Please include a description explaining why the ticket was closed, including links to prior tickets if available. Please describe how the ticket can be reopened if needed.

