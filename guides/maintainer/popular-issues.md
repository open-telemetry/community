# Managing Expectations on Popular GitHub Issues

Within OpenTelemetry, we encourage end-users and community members to leave 👍
reactions on GitHub issues, as indicated in our
[website](https://opentelemetry.io/community).

This unified approach makes it easier for end-users to highlight important
issues without requiring them to join SIG meetings or Slack channels. By
showcasing the impact of highly-voted issues, the End-User SIG can later
demonstrate how user input shapes OpenTelemetry, boosting engagement and
strengthening the feedback loop.

GitHub issue reactions help maintainers to:

- Get a high-level signal that measures the interest from the community in
  particular issues, in a way that can be evaluated and compared across one or
  many repositories.
- Avoid redundant, unproductive comments like "I have this issue too", which
  are difficult to compare across issues, and provide no context for triage.

## Popularity Does Not Imply Priority

OpenTelemetry SIGs have the autonomy to organize their work and manage roadmaps
independently, balancing their priorities while remaining aligned with the
general direction of the project.

While maintainers may use these reactions to prioritize issues, they’re **not
expected to solely base their issue prioritization on popularity**. Other
matters (e.g. security, spec compliance) may take precedence over individual
popular issues.

In addition, particular issues may be blocked by ongoing or future work, and
cannot be actioned until those are completed.

## Communicating Priorities

Triagers should keep the most voted issues up-to-date on a best-effort basis,
and communicate SIG priorities back to users if other work is taking precedence
before a given issue is prioritized. This avoids frustration for end-users and
gives them a way to see progress towards the issues they find the most
important.

How this communication is carried out within the most voted issues, or how many
issues are considered, is decided by SIG maintainers and triagers. This may 
involve pointing users to a project board where issues are prioritized, meeting
notes, or simply updating popular issues regularly.

## Finding the Most Popular Issues

The most popular issues for a given SIG can be found:

- For a particular repo: see
  [this sample filter](https://github.com/open-telemetry/community/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc)
  for the `community` repo.
- Across multiple repos: see
  [this sample filter](https://github.com/search?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+repo%3Aopen-telemetry%2Fopentelemetry.io+repo%3Aopen-telemetry%2Fcommunity+&type=issues)
  for the `community` and `opentelemetry.io` repos.

## Recommended Footnote on Issue Templates

We recommend using the following footnote on issue templates to ensure users
have direct access to guidance on how OpenTelemetry uses issue reactions.

```markdown
<sub>**Tip**: React with 👍 to help prioritize this issue. Add more useful info in comments to help maintainers triage it. Learn more [here](https://opentelemetry.io/community/).</sub>
```

Which renders as:

<sub>**Tip**: React with 👍 to help prioritize this issue. Add more useful info in comments to help maintainers triage it. Learn more [here](https://opentelemetry.io/community/).</sub>