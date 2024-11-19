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
- REQ-APPL-01: Guaranteed delivery of audit logs exported via OpenTelemetry SDK.
- REQ-PIPE-01: OTel collector must provide guaranteed delivery of audit logs, including when its process is interrupted

## Deliverables

- semantic convention for audit logs
- extend OTel APIs/SDKs for audit logging purposes (in collaboration with the respective SIG)
- extend OTel collector for audit logging purposes (in collaboration with the respective SIG)

## Staffing / Help Wanted

The following vendors are interested in improving this area:
- SAP

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