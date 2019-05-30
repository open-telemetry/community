# OpenTelemetry: A Roadmap to Convergence

This document covers the intial milestones for each SIG developing an implementation of the OpenTelemetry Specification. For each new language, we want to quickly achieve parity with existing OpenTracing and OpenCensus implementations.

[Merging OpenTracing and OpenCensus: A Roadmap to Convergence](https://medium.com/opentracing/a-roadmap-to-convergence-b074e5815289) defines the goals and timelines for OpenTelemetry.

If you are interested in starting a new SIG, please do the following:
* [create an issue](github.com/open-telemetry/community/issues) proposing the new SIG.
* [Configure the new repository](docs/how-to-configure-new-repository.md).
* Add the milestones listed below to the backlog.

## Initial Milestones
For languages which have both an OpenTracing and OpenCensus implementation, we would like to achieve parity in OpenTelemetry by **September, 2019**, and sunset the existing OpenTracing and OpenCensus SIGs by **November, 2019**. 

Parity can be defined as the following milestones:
* A set of interfaces which define the OpenTelemetry Specification in a given programming language.
* An SDK which can propagate context and record data in common formats.
* Backwards compatibility with OpenTracing and OpenCensus.
* Metadata helpers for recording common operations defined in the OpenTelemetry data model.
* Tests which provide evidence of interoperability.
* Benchmarks which provide evidence of expected resource utilization.

### SPEC: Define OpenTelemetry Interfaces
* Metrics
* Trace
* Tags
* Resources

### SDK: Propagate Common Trace Contexts
* Propagate context in Trace-Context format
* Propagate context in custom formats

### SDK: Export Common Data Formats
* Export data in OpenTelemetry format
* Export data in custom format

### SDK: Record Common Operations
* A data structure representing each operation type
* Utilities to record 

### SDK: OpenTracing Bridge
* the OpenTelemtry SDK implements the latest version of the OpenTracing interface.
* register as GlobalTracer.

### SDK: OpenCensus Bridge
* implement a version of OpenCensus which bridges to OpenTelemetry.

### TEST: Verify Interoperability
* Integration tests which verify SIG is interoperable with the rest of OpenTelemetry.
* CI integration to alert for incorrect context propagation.
* CI integration to alert for variations in data output.

### TEST: Verify Resource Utilization
* Integration tests which verify expected resource overhead. 
* CI integration to monitor code changes, and alert on unexpected resource usage.

### SUNSET: Migrate Ecosystems
* Ensure that popular OpenTracing and OpenCensus instrumentation has an OpenTelemetry equivalent.

### SUNSET: Code Freeze OpenTracing
* Update documentation to point to OpenTelemetry.
* No further code changes of any kind.

### SUNSET: Code Freeze OpenCensus
* Update documentation to point to OpenTelemetry.
* No further code changes of any kind.
