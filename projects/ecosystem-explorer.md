# OpenTelemetry Ecosystem Explorer

## Background and description

Related issues:

* [Java Instrumentation Metadata System](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13468)
  * [Associated Github Project](https://github.com/orgs/open-telemetry/projects/153?query=sort%3Aupdated-desc+is%3Aopen)
* [Java Instrumentation Documentation](https://github.com/open-telemetry/opentelemetry.io/issues/7740)

This project is initially primarily focused on Java instrumentation, but the concepts and tooling could be applied to
other languages (and the collector) as well, and we intend to explore that.

As a user, contributor, or maintainer of official [Java OpenTelemetry instrumentations](https://github.com/open-telemetry/opentelemetry-java-instrumentation),
I want documentation that can answer the following questions:

* What technologies and libraries are instrumented by the agent or have standalone instrumentation libraries I can use?
* Which versions of the various libraries or technologies are supported?
* How do I install and use the standalone instrumentation libraries?
* The library I use is supported, what kind of spans and metrics will be emitted when I use it?
* What attributes will the spans and metrics have?
* Are there any configurations I can enable to get additional or different attributes on my metrics or spans?
* Are there any configurations I can enable to get more/less metrics or spans for the libraries I use?
* I’m about to upgrade my Java agent from version x to version y, what telemetry or attributes changed?

A proof of concept "[Instrumentation Explorer](https://jaydeluca.github.io/instrumentation-explorer/)" website was 
created that can do all of this. It allows users to explore the different instrumentations and see the emitted telemetry.
It allows them to see how spans, metrics, and their associated attributes change when different configuration options are
changed, and it allows for comparing the telemetry across different versions of the Java agent.

This POC was created as part of an [effort](https://github.com/open-telemetry/opentelemetry-java-instrumentation/issues/13468)
by the Java SIG, which focused on analyzing the 250+ instrumentations in the Java agent, and created structured metadata
for each that could then be used to generate documentation.

We would like to rebuild and make this POC production-ready, and make it an official part of the OpenTelemetry 
documentation. We will create a standalone website that can be hosted on the OpenTelemetry domain, and integrate it into
the official OpenTelemetry documentation.

### Current challenges

The instrumentation projects are large code bases with many different components, often with behavior that changes 
depending on certain versions of the libraries in use in your code base, or if certain configuration options are enabled.

There are varying degrees of existing documentation for different instrumentation components, but it can be difficult to
find, and might not have all the information needed to understand the whole picture. Much of this documentation
exists on as github readmes, which are not indexed by google, and therefore are not easily discoverable.

Things can also change between different versions of the instrumentation artifacts themselves, and the resulting 
emitted telemetry can vary greatly. It can be frustrating for users to upgrade their OpenTelemetry instrumentation and
have their dashboards and alerts break because it’s not clear that signals or attributes were going to change.

In most cases, in order to understand what telemetry a user will get, they must first deploy their service using the 
instrumentation, find a way to execute all the different code paths, and then explore the resulting telemetry in a
backend. This is a lot of effort for someone who might be evaluating OpenTelemetry for the first time, and might deter
them from going through the exercise all together.

Maintainers of instrumentations also have the challenge of finding ways to keep the documentation up to date, and 
often have to make updates in several places. Most projects do a great job of keeping things up to date in the 
source code, but there isn't an existing process for ensuring that documentation is kept in sync.

The OpenTelemetry.io website has rich content related to SDKs, APIs, and concepts, but there is a gap when it comes to
instrumentation. The registry has some information, but it can be lacking important context and there are many 
instrumentations that are not listed there at all.

### Goals, objectives, and requirements

The aim of this project is to create an Ecosystem Explorer web application that provides a user interface to
explore instrumentation components across the OpenTelemetry ecosystem. The platform will be powered by structured
metadata and documentation extracted directly from instrumentation project source code, maintained through automated
processes.

**Primary Objectives:**

1. Address instrumentation documentation gaps by creating a centralized platform where users can:
    - Discover what technologies and libraries are instrumented
    - Understand what telemetry will be emitted (spans, metrics, attributes)
    - Compare telemetry across different versions and configurations
    - Access current documentation that addresses the scattered information problem identified in the challenges section

2. Establish a reusable documentation model that other language SIGs can adopt for their instrumentation projects,
  starting with Java and expanding to Javascript and Collector components

3. Integrate with the existing OpenTelemetry.io documentation ecosystem in a seamless manner

4. Implement automated maintenance workflows that keep documentation synchronized with source code changes

**Technical Requirements:**

- Production-ready web application rebuilt from the existing proof-of-concept
- Automated extraction of structured metadata from instrumentation source code
- Scalable data architecture to replace the current 2MB+ JSON file approach
- Extraction and availability of metadata for Javascript and Collector components to validate multi-language applicability

## Deliverables

**Production-Ready Ecosystem Explorer for Java**
* Refactored data pipeline and data architecture for managing the source metadata by agent version
* Rebuilt web application with professional UI/UX and responsive design
* Production and Staging deployment infrastructure with CI/CD
* Integration with OpenTelemetry.io documentation ecosystem

**Multi-Language Exploration**
* Research and prototype implementations to validate the approach for other languages and components
* Documentation and metadata models and templates that other language SIGs can adopt
* Assessment of Javascript instrumentation and Collector component applicability

## Staffing / Help Wanted

This project requires a blend of frontend development, tooling and automation, documentation expertise, and 
OpenTelemetry domain knowledge to transform the existing proof-of-concept into a production-ready platform.

### SIG

This project will be led by a cross-cutting effort coordinating with the Java SIG (primary implementation) and
Communications SIG (documentation integration). A new dedicated SIG or working group will be formed to help manage 
and move this project forward. 

### Required staffing

#### Project Leads(s)

* @jaydeluca (Grafana Labs)
* @svrnm (Causely)
* Looking for other leads with experience in OpenTelemetry instrumentation and/or web application development

#### TC Sponsor
TBD

#### GC Liaison
* @svrnm (Severin Neumann)

#### Other Staffing

**Frontend/UX Development (2+ contributors needed)**
- Frontend development skills for web application
- UI/UX design experience for data visualization and user experience
- Responsive design and accessibility expertise
- Experience with modern web frameworks and deployment pipelines

**Documentation and Integration (1+ contributors needed)**
- OpenTelemetry ecosystem knowledge for integration with OpenTelemetry.io
- Technical documentation and content strategy experience
- SEO and discoverability optimization
- Community engagement and adoption support

**Backend/Infrastructure (1+ contributors needed)**
- Data pipeline / Python scripting experience
- CI/CD and deployment automation


* TBD - Frontend Developer(s) with experience in React or similar frameworks

### Industry outreach (Optional)

Who (people, companies) in the industry should be aware of this effort? Was there an attempt to get them onboard? What did they say?

## Expected Timeline

This timeline assumes project approval and resource allocation as outlined in the staffing section. Until staffing is
confirmed and expected time commitments are known, this timeline is in flux.

**Phase 1: Foundation and Planning (Months 1-2)**
- Establish project infrastructure, GitHub project board, and team coordination
- Complete technical assessment of existing POC and data architecture requirements
- Finalize UI/UX design requirements and technical specifications
- Set up development, testing, and staging environments

**Phase 2: Core Platform Development (Months 3-8)**
- Refactor and rebuild data pipeline with scalable architecture
- Develop production-ready web application with professional UI/UX
- Implement automated metadata extraction from Java instrumentation repositories

**Phase 3: Integration and Multi-Language Research (Months 9-11)**
- Integration with OpenTelemetry.io documentation ecosystem
- Conduct JavaScript and Collector component research and prototyping
- Create documentation templates and adoption guidance for other language SIGs
- Beta testing with Java SIG and selected community members

**Phase 4: Production Launch (Month 12)**
- Production deployment and monitoring setup
- Community rollout and adoption support
- Documentation and maintenance procedure finalization
- Project handoff to ongoing maintenance team

The timeline may be adjusted based on contributor availability and community feedback during the development process.
Multi-language expansion beyond research phase will depend on interest and engagement from other language SIGs.

## Labels

`instrumentation-docs` for all PRs and issues related to this project.

## GitHub Project (Post-Approval)

TBD

## SIG Meetings, Roadmap, and Other Info (Post-Approval)

TBD