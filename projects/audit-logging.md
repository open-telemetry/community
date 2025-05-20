# Audit Logging

## Background and description

Audit logging describes the capability of capturing audit-trail relevant events of a system to meet compliance requirements. Such events may originate from the infrastructure (e.g. a Kubernetes cluster) up to the application-level. It is a capability that is particularly relevant for providers of enterprise software.

Unlike regular application logs, audit logs are usually subject to long retention periods and software providers must guarantee their completeness (i.e. guarantee of delivery).

Examples of audit logs include: (see [Appendix B: Examples of Audit Log Events])
- failed login attempts
- permission changes (e.g. of a service account or application user)
- accessing sensitive information
- modification of data

We intend to tackle this in phases:
- In Phase 1 (_in progress_), we are **building an end-to-end prototype** to refine the challenges and requirements for audit logging in OTel and to showcase potential solutions. This is time-boxed until end of September 2025. We are set up to run this without a formal OTel project sign-off.
- In Phase 2, we intend to **contribute functional extensions upstream** back to OTel. We will work towards signing off this project proposal and either join existing SIGs or form a separate one. The results from Phase 1 should help us in the discussions with the maintainers to make our proposed extensions/changes more tangible.
- In Phase 3, we plan to **work on semantic conventions** for audit logging.

### Current challenges

OpenTelemetry does not have a good solution for audit logging

- no semantic conventions for audit logs in OTel
- lack of delivery guarantees in OTel, e.g.:
    - OTel APIs/SDKs do not provide feedback to the application level whether data (in particular logs) have been successfully delivered to a remote endpoint. To guarantee delivery, either the SDK has to give those guarantees, or provide feedback to the application so that it can take care of guaranteed delivery itself.
    - OTel Collector instances may lose audit logs in transit (i.e. no guarantee of delivery)

See [Appendix A: Guarantee of Delivery] for more details

### Goals, objectives, and requirements

The goal of this project is to make OTel fit for audit logging purposes that meet compliance requirements of enterprise software providers, in particular: (_to be refined by Phase 1_)

- REQ-01: Semantic conventions for application-level audit logs are defined
- REQ-02: Semantic conventions for infrastructure-level audit logs are defined
- REQ-03: Guaranteed delivery of audit logs exported via OpenTelemetry SDK
- REQ-04: OTel Collector instances must provide guaranteed delivery of audit logs, including when its process is interrupted

See [Appendix A: Guarantee of Delivery] for more details

## Deliverables

Phase 1 (_in progress_, see repo [audit-log-poc-for-otel](https://github.com/apeirora/audit-log-poc-for-otel)):
- end-to-end prototype of a setup that produces audit logs uses OTel to deliver them to a sink.
- list of gaps in OTel with regard to delivering audit logs
- prototype implementations to close selected gaps

Phase 2:
- extend OTel APIs/SDKs for audit logging purposes (in collaboration with the respective SIG)
- extend OTel Collector for audit logging purposes (in collaboration with the respective SIG)

Phase 3:
- semantic convention for audit logs

## Staffing / Help Wanted

The following vendors are interested in improving this area:
- SAP (@mlenkeit, @FWinkler79)
- Microsoft (@reyang)

Other vendors are invited to join the discussion.

### Required staffing

* Project lead: @hilmarf
* Sponsors:
  - @reyang
  - tbd
* GC liaison: @svrnm
* Engineers contributing to the SIG:
  - @hilmarf
  - ...
* Maintainers/approvers: tbd

## Timeline

- Phase 1: until end of September 2025 (approx.)
- Phase 2: tbd
- Phase 3: tbd

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

The implications of guarantee of delivery can be illustrated with an example consisting of a workload, an OTel Collector instance, and a durable storage. The workload acts as the source and produces audit logs via the OTel API/SDK. It writes the data via OTLP to the collector. The collector is configured to export audit logs to a durable storage that acts as the destination such as an S3 bucket.

The following implications would apply:

- workload produces an audit-relevant event:

  The workload emits the event via the OTel API/SDK. It may wait for acknowledgement of receipt from the collector before proceeding. If the event is rejected or receipt is not acknowledged in time, the workload or SDK may act accordingly, e.g. retry, rollback a database transaction, inform the user, etc.

- OTel Collector receives the event:

  To ensure that the event is not lost even if the collector process is terminated or crashes, the collector may need to persist the event before acknowledging receipt to the workload or SDK. If the event cannot be persisted, receipt must be rejected.

- OTel Collector exports the event:

  Once the event is exported and the target (i.e. S3) acknowledges receipt, the event can dropped from the collector's persistence.

- the target (i.e. S3) receives the event:

  Acknowledges receipt after persisting the event.

  Note that this is outside the scope of the OTel. More general, when using OTel for audit logging purposes, it's the users (e.g. Ops) responsibility to configure a suitable export target.

Note that this example may contain implementation details for illustration purposes. The actual implementation may differ as long as the requirements are met.

The example is kept simple for illustration purposes. Many edge cases need to be discussed by the SIG, such as batch-sending of signals or handling of multiple export targets.

It may turn out that all OTel receivers, processors, or exporters can be made compatible with guarantee of delivery for audit logging purposes.

### Appendix B: Examples of Audit Log Events

The following list contains sample audit log events in a YAML format for better readability and intentionally do not follow any OTel-related schema.

An event consists of the event name, event-specific data, and general metadata. The individual properties of these events would ideally be reflected in common or audit log-specific semantic conventions.

- failed login attempts

  ```yaml
  event: UserLoginFailure
  data:
    loginMethod: oidc
    failureReason: userLocked
  metadata:
    id: 50b925b5-0ba9-42f3-b476-8a6795000046
    timestamp: 1732193414483
    ip: 10.11.12.13
    initiator: john-doe
    application: payroll
    tenant: fab54af9-f978-463e-9c02-f92db1afc2b4
  ```

- permission changes (e.g. of a service account or application user)

  ```yaml
  event: AuthnRoleToUserAdd
  data:
    user: jane-doe
    role: editor
  metadata:
    id: 50b925b5-0ba9-42f3-b476-8a6795000046
    timestamp: 1732193414483
    ip: 10.11.12.13
    initiator: john-doe
    application: payroll
    tenant: fab54af9-f978-463e-9c02-f92db1afc2b4
  ```

- accessing sensitive information

  ```yaml
  event: DppDataAccess
  data:
    channelType: web
    channelId: https://payroll.example.com/user/jane-doe/compensation
    dataSubjectType: employeeID
    dataSubjectId: jane-doe
    objectType: compensation
    objectId: 1196f42b-8f12-4df0-9b1f-01c98d2c7291
    attribute: salary
    value: 50000
  metadata:
    id: 50b925b5-0ba9-42f3-b476-8a6795000046
    timestamp: 1732193414483
    ip: 10.11.12.13
    initiator: john-doe
    application: payroll
    tenant: fab54af9-f978-463e-9c02-f92db1afc2b4
  ```


- modification of data

  ```yaml
  event: DataModification
  data:
    objectType: CronJob
    objectId: my-sample-cronjob
    attribute: schedule
    oldValue: 0 0 1 * * # monthly
    newValue: 0 0 1 1 * # annually
  metadata:
    id: 50b925b5-0ba9-42f3-b476-8a6795000046
    timestamp: 1732193414483
    ip: 10.11.12.13
    initiator: john-doe
    k8sCluster: my-sample-cluster
  ```

<!-- links -->
[Appendix A: Guarantee of Delivery]: #appendix-a-guarantee-of-delivery
[Appendix B: Examples of Audit Log Events]: #appendix-b-examples-of-audit-log-events
