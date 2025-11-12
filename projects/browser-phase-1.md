# Browser Instrumentation (Phase 1) Proposal

## Background and Description

OpenTelemetry is rebooting telemetry for the Browser as a sequence of small, highly focused projects. The first project will focus on creating instrumentation for the browser runtime and a small set of browser libraries, plus the prerequisite API and data modeling work needed to create this instrumentation.

## Current Challenges

OpenTelemetry currently has a NodeJS-focused javascript implementation that is also capable of running in the browser. However, the requirements for a successful browser observability solution differ enough from NodeJS that a specialized solution is required.

* Loading and unloading in the browser are specialized tasks that are very different from booting and shutting down a NodeJS application. Unloading in particular is under strict time and resource constraints.
* Memory, cpu, and networking resources are severely constrained, especially on mobile devices.
* A lack of compression and gRPC in browsers
* Package and dependency sizes
* All activity occurring in the program relates to a single user instead of many independent transactions. So far this has led to a number of spec developments, such as the need for mutable resources for session management, a better logging model for recording events, and may lead to more browser specific design requirements.
* Sessions in particular are a very important lifecycle for clients which are not present as a concept in server-side programs.
* Sessions persist across multiple page loads, another difficult problem to design a solution for that is browser specific.
* NodeJS has built in facilities for tracking context across async boundaries, but browsers do not have an equivalent concept.

## Goals, Objectives, and Requirements

OpenTelemetry needs a javascript implementation optimized for the browser. Sharing code with NodeJS is helpful when possible. But going forward, we want to prioritize running well in the browser over code reuse with the NodeJS project. If there are places where code reuse with NodeJS is a hard requirement, those places should be identified explicitly.

We also have a goal of taking an incremental approach, focused on obtaining the highest initial value for the least amount of work. Among participating companies with the OpenTelemetry community, there are already multiple solutions for browser observability. And the current OTel JS SDK does run in the browser.

Rather than start from scratch with a new SDK, we would like to focus our browser work on instrumentation.  OTel instrumentation has only one dependency, the OTel instrumentation API. There is no need to do SDK work in order to stabilize the instrumentation packages we want to provide for our community.

We propose that the various existing browser clients bind to the new OTel Browser API, and we delay work on providing an optimized SDK solution until after we have stabilized a key set of instrumentation packages. This will allow the community to begin receiving value from our OTel browser work much faster than if we were to start by optimizing the SDK.

## Deliverables

### Step 1: Browser Fundamentals

Review the current Tracing, Metrics, and Logs API packages. Identify what, if anything, would need to be changed to make these packages optimal for the browser. Discuss the pros and cons of implementing these changes by sharing the existing packages with NodeJS, or forking them to have a separate set of API packages just for the Browser. Please note that the goal of this review is not to deviate from the OpenTelemetry API specification, but to evaluate the practical limitations that the current API packages may place on browser instrumentation.

OpenTelemetry API review:
* Package size
* Dependencies
* Other browser requirements that differ from NodeJS

Data Modelling:
* Sessions
* Resources / Entities
* Navigation
* Anonymous user ids (Manager)

The SIG will also evaluate how best to maintain browser-specific packages, in terms of teams, repos, and other GitHub code management policies.

### Support

We will also decide our compatibility story.
* Which Browser features and APIs do we require to be present?
* Based on those features, which browser versions will we support?
* Will we aim support electron at this time?
* Do any considerations need to be made for web assembly?

### Step 2: Core Instrumentation

Once we are clear on what API packages we plan on using, we plan to implement an initial set of instrumentation packages for high priority browser libraries. The goal of this step is to provide enough of an initial ecosystem that end users and vendors can validate the decisions made in Step 1, along with the Semantic Conventions, so that we can stabilize these decisions based on real world feedback.

During this phase, the SIG will not be focused on implementing a browser-optimized SDK. Instead, we will continue to use the existing OTel JS SDK as our reference implementation. Third party SDKs may also choose to bind to the OTel Browser API at this time.

In some cases, browser instrumentation already exists but may be different from the new instrumentation we want to provide. This instrumentation should be treated as "de facto stable" and should not experience breaking changes until we are ready to issue a stable v1.0. New unstable versions of this instrumentation should be managed in a way that allow the SIG to move quickly without destabilizing any instrumentation currently in production.

Instrumentation for the browser runtime:
* Page load/unload
* User events (clicks, etc)
* Resource timing
* Errors
* Web vitals
* Long tasks

Example list of library instrumentation:
* Fetch / XHR Requests
* Websockets
* React
* Next
* Svelte
* Angular
* Vue.js

### Next Steps

Once we are satisfied that we have achieved the above goals, this SIG will review the remaining work and available resources and choose a new project for the SIG to work on. 

Options include:
* Continue implementing instrumentation packages.
* Implement a browser-specific SDK.
* Implement a more efficient client protocol.
* Implement a public gateway for client protocols.
* Support for web assembly.
* TBD

## Staffing / Help Wanted

### Industry Outreach

There are a number of existing RUM/Client observability implementations. Representatives from a wide selection of companies that have experience with browser observability are present in the SIG. This includes Microsoft, New Relic, DynaTrace, HoneyComb, Grafana Labs, and Cisco, among others. We plan for further outreach among end users once we have working code for them to review.

### Required Staffing

**Project Lead:** @tedsuo (Grafana Labs)

**GC Liaison:** @tedsuo (New Relic)

**Sponsors:**
* @tedsuo - Spec Maintainer Sponsor (Grafana Labs)
* @dyladan  - Spec Maintainer Sponsor (Dynatrace)
* @carlosalberto – TC Escalating Sponsor

**Implementation Engineers:**
* @martinkuba (ServiceNow)
* @pkanal (Honeycomb)
* @Karlie-777 (Microsoft)
* @krimple (Honeycomb)
* @overbalance (Embrace)
* @joaquin-diaz (Embrace)
* @Abinet18 (Cisco)

	
**NodeJS Maintainers and Approvers:**

When bootstrapping our browser work, we want to make sure that the existing OpenTelemetry Javascript community is involved. Existing OTel JS maintainers and approvers should participate in this project to help ensure that it is successful.
* @@martinkuba (ServiceNow)
* @pkanal (Honeycomb)
* @hectorhdzg (Microsoft)
* @david-luna (Elastic)

### Additional SIG Members

**Design review:**
* @ramthi (Microsoft)
* @scheler (Cisco / Splunk)
* @codecapitano (Grafana Labs)
* metal-messiah (New Relic)

## Timeline

### Step 1 Deliverables

Expected due dates for step 1 proposals:
* OpenTelemetry API review and changes proposal: TBD
* Browser Compatibility and Support proposal: TBD
* Data modeling and additional features proposal: TBD

Expected due dates for code changes based on the above proposals:
* API changes: TBD
* Data Modelling changes: TBD

### Step 2 Deliverables

Expected due dates for step 2 proposals:
* Browser runtime instrumentation proposal: TBD
* Initial library instrumentation proposal: TBD

Expected due dates for code changes based on the above proposals:
* Browser runtime instrumentation: TBD
* Library instrumentation: TBD

## Labels

`spec-browser` for all PRs and Issues related to this project.

## Project Board

https://github.com/orgs/open-telemetry/projects/146/views/1

## SIG Meetings and Other Info

**SIG Meeting time:**  
Proposing a weekly 30 min meeting, Thursdays 8:30am Pacific (please confirm if this works for you)

Once the Browser Instrumentation SIG begins, the current Client SIG will be retired.
