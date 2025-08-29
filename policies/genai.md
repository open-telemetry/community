# Generative AI Contribution Policy

This policy provides general guidance for contributors and maintainers relating
to the use of Generative AI in OpenTelemetry projects. This guidance supersedes
and extends the policy defined in the [Linux Foundation Generative AI
Policy](https://www.linuxfoundation.org/legal/generative-ai).

## The Short Version

While we welcome contributions from anyone, maintainers of individual
projects may -- at their discretion -- hide or close issues, pull requests, or
other contributions that are made totally or in part through generative AI
tooling.

The human driving any contribution is responsible for ensuring that LLM-generated
content aligns with project guidelines and policies, especially this Generative AI
document and the aforementioned Linux Foundation Generative AI Policy.

## The Long Version

### General Guidelines for Generative AI Usage

Increasingly, we have observed a trend of contributors who are utilizing LLMs
and other generative tools to participate in issues and create pull requests.
Regurgitating the output of an LLM is unlikely to be particularly helpful, or
valuable, to other contributors, maintainers, and end-users for a couple of reasons.

First, time is a very scarce resource for maintainers and approvers. Thoughtful,
high-quality code reviews both essential to the success of OpenTelemetry, and
require a significant time commitment. There is not enough time to give proper
responses to low-effort pull requests without compromising our responsiveness to
high-effort pull requests. Second, OpenTelemetry is a complex, fast-moving
project -- LLMs will often have stale data in their training sets, and are prone
to offering output that is not relevant to the current state of the project.
While LLMs can be incredibly powerful coding assistants they are not a
substitute for human judgement and knowledge.

With proper usage, Generative AI can be a valuable tool for writing code,
documentation, tests, and more. This level of usage requires enough
understanding of the project to evaluate the LLM output, and to know when to
accept or reject it. Therefore, we ask that contributors do not rely on LLM
output as the sole basis for their contributions.

Examples of this include:

- Copying and pasting LLM output into issues or pull requests without any
  additional context or explanation.
- Reviewing existing pull requests solely via
  LLMs, or using LLMs to respond to issues without any additional context or
  explanation.

### Human Responsibility and Control

The human driving any contribution — whether as an author, reviewer, or maintainer — must
remain in control of the process and bear full responsibility for the final output.
This means actively reviewing, understanding, and validating any LLM-generated content
before submission. You cannot delegate your responsibility to an AI tool, nor can you
claim that an AI made an error as a defense for problematic contributions. The human
contributor is accountable for ensuring that all content, regardless of its origin,
meets project standards, follows established policies, and contributes meaningfully
to the OpenTelemetry project.

## Frequently Asked Questions - Contributors

_Q: Can I use LLMs to help me write code, documentation, or tests?_

Yes, this policy does not prohibit the use of LLMs to assist in writing code,
documentation, or tests. However, we ask that you do not rely on LLM output as
the sole basis for your contributions.

_Q: Can I use LLMs to help me review pull requests, issues, or understand the code base?_

Yes, this is also allowed -- and a good idea! You should use LLMs as a tool to
assist in your understanding, but not as a replacement for your own judgement
and ability.

_Q: How do I know the difference between allowed and disallowed usages of LLMs?_

"If you have to ask, you already know the answer." This policy is not a broad
ban of LLMs, it is a request that you -- as an individual -- use them in a way
that adds value to the project and respects the time of other contributors and
maintainers. If you are using LLMs to help you write code, that is fine; You
should be clear about this in pull requests and reviews. If you are using LLMs
to understand code so that you can participate in issues or reviews, that is
also fine -- but you should be clear about this as well. What is not fine is
copying and pasting a GitHub issue into an LLM prompt and asking it to write the
PR for you, then blindly submitting that response. You must be an active and
willing participant in the process of contributing to OpenTelemetry.

## Frequently Asked Questions - Maintainers

_Q: Can I close or hide issues or pull requests that are made through LLMs?_

Yes, as your discretion you may close or hide issues or pull requests that are
made through LLMs. We ask that you provide a clear explanation for why you are
doing so, and -- if possible -- provide guidance on how the contributor can
improve their contribution.

_Q: How do I address contributors who are making consistent, low-effort contributions via LLMs?_

If an individual contributor continues to engage in low-effort PRs or issues,
_and_ you have exhausted other avenues of communication, please escalate the
situation to the OpenTelemetry Governance Committee. Per the [Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md),
contributors are expected to help maintain a positive environment, which would
include following guidance and published policy.

_Q: Can I use LLM or Generative AI tooling to assist in my own work as a maintainer?_

In general, you should evaluate the output of LLMs -- regardless of how you use
them -- in the same way you'd evaluate the output of a human contributor or
non-AI tool. For example, tools like [Dosu](https://dosu.dev/) are being used in
certain repositories to aid in code review and issue management. Remember that
these tools can make mistakes, and use your best judgement when evaluating their
output.
