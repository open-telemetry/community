# How to use saved replies on GitHub

Saved replies let maintainers and approvers respond to common situations
(policy violations, contribution guidance, closing stale PRs, etc.) without
retyping the same message every time. This document explains how to set them
up on GitHub and links to the prepared reply templates the OpenTelemetry
community maintains.

## Setting up saved replies

Saved replies live on your **personal GitHub account**; they are not tied to
an organization or repository. Any saved reply you create is available to you
across every repo you comment on.

1. Go to [github.com/settings/replies](https://github.com/settings/replies).
2. Click **Add a saved reply**.
3. Give it a short, descriptive **title** (this is what you will search for
   later — e.g. `genai-policy-violation`).
4. Paste the reply body from one of the templates in [replies/](./replies/).
5. Click **Add saved reply**.

Repeat for each template you want available.

## Using a saved reply

When commenting on an issue or pull request:

1. Click the reply comment box.
2. Click the arrow icon in the toolbar above the text area (**Insert a reply**),
   or press <kbd>Ctrl</kbd>+<kbd>.</kbd> (Windows/Linux) or <kbd>⌘</kbd>+<kbd>.</kbd>
   (macOS).
3. Search for the reply by title and select it.
4. Adjust the text as needed for the specific situation if necessary.
5. Post the comment.

## Guidelines for using prepared replies

- **Read the contribution first.** A saved reply is a time-saver, not a
  substitute for reviewing what the contributor submitted.
- **Be respectful.** These replies exist to keep responses consistent and
  fair. Follow the
  [Code of Conduct](https://github.com/cncf/foundation/blob/main/code-of-conduct.md).

## Available templates

Prepared reply templates live in [replies/](./replies/). Each file contains
the body of one saved reply plus a short note on when to use it.

- [code-of-conduct-violation.md](./replies/code-of-conduct-violation.md) —
  Comment or behavior violates the [Code of Conduct](../code-of-conduct.md).
- [genai-policy-violation.md](./replies/genai-policy-violation.md) — PR
  appears to violate the [Generative AI Contribution Policy](../policies/genai.md)
  and will be closed.
- [needs-repro.md](./replies/needs-repro.md) — Issue lacks actionable detail;
  ask the reporter for a minimal reproducible example.

## Adding a new template

If you find yourself writing the same response repeatedly, add a new file
under [replies/](./replies/) and open a PR. Keep the template short, link to
the relevant policy, and include a short note at the top of the file
describing when to use it.
