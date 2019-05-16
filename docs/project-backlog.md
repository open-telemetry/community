# Backlog Structure for OpenTelemetry

It's an important community goal for OpenTelemetry that our members find the backlogs to be responsive, and easy to take part in. Having a shared methodology for processing issues helps new members understand the current state of each project.

## Roles
* **Triager**: Person who is triaging the issue by determining its workability. This person is responsible for getting the ticket to one of two stages - 1) ready-for-work 2) wontfix. They are responsible for triaging  by working with the OP to get additional information as needed and analyzing the issue and adding relevant details/information/guidance that would be helpful to the resolution of the issue.

* **OP**: Original Poster. This is the person who has opened or posted the issue.

* **Contributor**: Person(s) that are actually doing the work related to the ticket. Once work is done, they work with the Reviewer and the Contributing Reviewers to get feedback implemented and complete the work. They are responsible for making sure issue status label is up to date.

* **Reviewer**: Person(s) whose Approval is needed to merge the PR.

* **Contributing Reviewer**: Person who provides feedback on an PR but whose Approval is not necessarily needed to merge the PR.

## SLAs
We value having a responsive backlog, and have response SLAs for each role. If an issue exceeds an SLA, it is put into the `stale` state.

* **Triager**: Daily (Business Days) review of new issues with initial feedback to OP or issue processed within 3 days of last activity.
* **Reviewer / Contributing Reviewer**: Provide feedback within 3 days of the last activity on a PR
* **Contributor**: 3 day updates as comments on the PR to indicate activity

## Issue States

### New
label: `new`

New issues are the domain of the backlog Triagers. Every new issue should be responded to quickly, with a greeting and any needed clarifying questions. If assessing the issue requires more information, the Triager collaborates with the OP until workability is determined.

The most common next steps for new tickets:
* `available` for actionable work items.
* `needs-discussion` for issues which cannot be triaged quickly, but raise important points.
* `no-further-action` for issues which can be quickly resolved.

### Available
label: `available`

For new work requests Once it has been classified, a ticket is up for grabs to be picked up to be worked on by a contributor.

All work is labeled with a priority:
* `P0` = Critical (Drop everything and work on it.)
* `P1` = Important (Work on it if no P0 are present. Use judgment to prioritize items within a list of P1s)
* `P2` = Low (Work on it when no P1 are left or some one from community wants to contribute)

Work can also be classified into a number of categories, to make available issues easier to find. Common examples of work categories are:
* `feature-request`
* `enhancement`
* `bug`
* `docs`

Available work can be assigned in the following ways:
* A contributor assigns the ticket to themselves.
* A maintainer assigns the ticket to a contributor.

All tickets transition to `wip` once they have been assigned.

### WIP
label: `wip`

Any ticket which has been assigned a lead contributor is considered work in progress. 

* If a PR is merged which resolves the issue, the ticket can be closed as `completed`.
* If work is blocked on review, the ticket transitions to `needs-review`.
* If work is abandoned, or the ocntributors otherwise change their minds, the ticket can be closed as `no-further-action`.

### Needs Review
label: `needs-review`

Implementation work related to the ticket has been completed. Work related to a Review and/or any changes requested as part of the review  is in progress.  Issues with a PR associated with it will be considered as in ‘In Review’.

* Move the issue back to `in-progess` if significant changes are needed.
* Close the issue with the `completed` label.
* Close the issue with the `no-action` label.

### Needs Discussion
label: `needs-discussion`

Some issues are not directly related to a particular code change. This can often arise with tickets describing unclear edge cases, and situations where applying OpeTelemetry is proving to be difficult.  If a ticket is worth considering in the issue backlog, but not scoped clearly enough to move to `wip`, then it `needs-discussion`.

* When possible, move the discussion forwards by using code examples.
* Mark the ticket as `agreed` if a resolution is found. 
* Close the ticket as `no-action` if discussion ends without a solution.
* Note: If the ticket is a help request with an existing answer, please link to the answer before closing the ticket.

### Agreed
label: `agreed`

An agreement has been reached. Once a course of action is determined, discussion is (hopefully) over.

* Clearly list any resulting action items which need to be adressed.
* Close the ticket once all action items are completed.

### Stale
label: `stale`

When a ticket has violated an SLA, it becomes stale.

Action items for stale tickets:
* record the SLA details as comment on the ticket.
* @mention the person(s) who can resolve the SLA.

### Blocked
label: `blocked`

An Issue is blocked due to an external reason or extenuating circumstances. Genereally, issues should be closed as `no-further-action`, rather than be left in a `blocked` state.

### No Futher Action
label: `no-further-action`

Not every discussion or feature request results in action. Issues which cannot be adressed at the present moment, or have no futher discussion, should be closed. This helps keep the open backlog focused on active discussions.

Possible reasons:
* a prior discussion decided the issue for now.
* a discussion is off topic.
* a feature request is not implementable.

In these cases, close the ticket as `no-further-action`. Please include a description explaining why the ticket was closed, including links to prior tickets if available. Please describe how the ticket can be reopened if needed.

### Completed
label: `completed`

Any issues which are resolved via a merged pull request can be closed with the `completed`. This extra label can be helpful when searching closed issues.
