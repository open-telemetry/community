# Audit Logging

## Background and description

Audit logging describes the capability of capturing audit-trail relevant events of a system to meet compliance requirements. Such events may originate from the infrastructure (e.g. a Kubernetes cluster) up to the application-level. It is a capability that is particularly relevant for providers of enterprise software.

Unlike regular application logs, audit logs are usually subject to long retention periods and software providers must guarantee their completeness (i.e. guarantee of delivery).

Examples of audit logs include:
- permission changes (e.g. of a service account or application user)
- modification of data
- accessing sensitive information
- failed login attempts

### Current challenges

Audit Logging is currently not within the scope of OpenTelemetry

- no semantic conventions for audit logs in OTel
- OTel APIs/SDKs do not provide feedback to the application level whether data (in particular logs) have been successfully delivered to a remote endpoint. To guarantee delivery, either the SDK has to give those guarantees, or provide feedback to the application so that it can take care of guaranteed delivery itself.
- OTel collectors may lose audit logs in transit (i.e. no guarantee of delivery)

### Goals, objectives, and requirements

The goal of this project is to make OTel fit for audit logging purposes that meet compliance requirements of enterprise software providers, in particular:

- REQ-CONV-01: Semantic conventions for application-level audit logs are defined
- REQ-CONV-02: Semantic conventions for infrastructure-level audit logs are defined
- REQ-APPL-01: Guaranteed delivery of audit logs exported via OpenTelemetry SDK
- REQ-PIPE-01: OTel collector must provide guaranteed delivery of audit logs, including when its process is interrupted

## Deliverables

- semantic convention for audit logs
- extend OTel APIs/SDKs for audit logging purposes (in collaboration with the respective SIG)
- extend OTel collector for audit logging purposes (in collaboration with the respective SIG)

## Staffing / Help Wanted

The following vendors are interested in improving this area:
- SAP (@mlenkeit, @FWinkler79)
- Microsoft (@reyang)

Other vendors are invited to join the discussion.

### Required staffing

* Project lead: SAP (name tbd)
* Sponsors:
  - Reiley Yang (@reyang)
  - tbd
* GC liaison: tbd
* Engineers:
  * SAP will provide a prototype in two languages (tbd; likely two of Java, JavaScript, Go)
* Maintainers/approvers: tbd

## Timeline

TBD based on community involvement.

## Labels

- audit-logging (tbc)

## Project Board

TODO: add link

## SIG Meetings and Other Info

TODO: add information

## Appendix

### Appendix A: Guarantee of Delivery

In the context of this document, guarantee of delivery describes the ability of delivering audit logs from source to destination through OTel means while ensuring that all such signals arrive at the destination and/or providing the source with a means to handle failed delivery.

Messaging protocols that support different levels of delivery guarantees may refer to this behavior as _at least once_ or _exactly once_, as opposed to _at most once_.

We assume that every component that is involved in the delivery of audit logs from source to destination must support guarantee of delivery individually, rather than assuming that this ability can be provided by e.g. only the collector or SDK.

The implications of guarantee of delivery can be illustrated with an example consisting of a workload, an OTel collector, and a durable storage. The workload acts as the source and produces audit logs via the OTel SDK/API. It writes the data via OTLP to the OTel collector. The OTel collector is configured to export audit logs to a durable storage that acts as the destination such as an S3 bucket.

The following implications would apply:

- workload produces an audit-relevant event:

  The workload emits the event via the OTel SDK/API. It may wait for acknowledgement of receipt from the collector before proceeding. If the event is rejected or receipt is not acknowledged in time, the workload or SDK may act accordingly, e.g. retry, rollback a database transaction, inform the user, etc.

- OTel collector receives the event:

  To ensure that the event is not lost even if the collector process is terminated or crashes, the collector may need to persist the event before acknowledging receipt to the workload or SDK. If the event cannot be persisted, receipt must be rejected.

- OTel collector exports the event:

  Once the event is exported and the target (i.e. S3) acknowledges receipt, the event can dropped from the collector's persistence.

- S3 receives the event:

  Acknowledges receipt after persisting the event.

  Note that this is outside the scope of the OTel. More general, when using OTel for audit logging purposes, it's the users (e.g. Ops) responsibility to configure a suitable export target.

Note that this example may contain implementation details for illustration purposes. The actual implementation may differ as long as the requirements are met.

The example is kept simple for illustration purposes. Many edge cases need to be discussed by the SIG, such as batch-sending of signals or handling of multiple export targets.

It may turn out that all OTel receivers, processors, or exporters can be made compatible with guarantee of delivery for audit logging purposes.