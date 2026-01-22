# Donations

Donations of preexisting code fall into two broad categories:

* **Small donations:** Some donations only amount to a single PR and should
  usually just be contributed as such
* **Large or complex donations:** Other donations are much larger, require
  ongoing maintenance of their own, and/or introduce nuanced licensing issues

Large donations – or small donations that turn up complex issues during PR
review – should follow the [donation process](#donation-process).

All donated code requires a license compatible with the Apache Software License
2.0, and donated code will require a change of copyright to reflect the
OpenTelemetry Authors. The Governance Committee (GC) will also ask to review any
trademarks (like the names of components) the donation can carry and make a
decision to either remove those trademarks or transfer them to the CNCF.

## Donation process

Broadly, these are the steps the OpenTelemetry Governance and Technical
Committees follow to handle a prospective donation.

1. The donating organization creates a GitHub issue using the "Donation
   Proposal" form in the `community` repository. Various steps in this process
   involve back and forth communication with the donating organization,
   which is expected to be engaged and responsive.
2. The GC will evaluate the proposal to ensure that
   the donation is aligned with the overall OpenTelemetry project vision
   and roadmap and has a balanced set of interested contributors and maintainers.
   The GC is also responsible for driving awareness in the community about
   the contribution and making sure all interested parties have a chance to
   object and/or contribute. The GC should work with any appropriate Special Interest
   Groups to evaluate the donation proposal, consider alternatives,
   and ensure OpenTelemetry has the resources required to support the donation. When
   considering alternatives, the GC should consider at least the CNCF ecosystem,
   and may also consider other well-known open source projects or alternatives proposed
   by the community.
3. If a donation proposal passes the initial GC screening, the TC
   will conduct due diligence to determine if the proposed donation can be effectively
   integrated into the OpenTelemetry project in a way that meets the quality, security,
   and privacy standards of the project without violating stable specification or OpenTelemetry Enhancement Proposals (OTEPs).
   The TC will summarize their findings, and make a recommendation to either
   accept or reject the proposal, conditionally or unconditionally, in a report
   which will be attached to the donation proposal issue. Writing the report may
   require meeting and discussing alternative technologies with different
   vendors. The amount of time for the TC member to produce the report varies based
   on the complexity of the donation, existing competing priorities, and other
   factors. However, generally TC members should aim to produce the initial
   report within a month or begin providing regular status updates on the issue.
4. The GC will consider the report and make a final decision about the donation,
   and document that decision on the donation proposal issue.
5. If accepted, the contributing organization – particularly if it's a
   commercial entity – must formally acknowledge via the GitHub issue that its
   respective sales and marketing departments have received, understood, and
   accepted the terms of the [OpenTelemetry marketing guidelines](../../marketing-guidelines.md).
6. Given all of the above, the GitHub issue is closed and the donation moves
   forward as agreed to by the TC and GC.