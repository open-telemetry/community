# <img src="https://opentelemetry.io/img/logos/opentelemetry-logo-nav.png" alt="OpenTelemetry Icon" width="45" height=""> June 2022 End User Interview
## Who: 
- An engineer on a technology development platform centralized observability team *and* OpenTelemetry project SDK maintainer.

## Stack/What they’re trying to Observe: 
- C
- C#
- C++
- Go
- Java
- JavaScript (TypeScript, Node.JS)
- .NET Core
- Python
- Ruby
- Rust

They also want to observe Kafka (subscriber model)

The company heavily uses logs and Statsd.

They want to instrument their Hosted SaaS & On Prem offerings.


## Their end vision for OTel:
They are focused for the moment in Tracing. They want to report traces that increase the efficiency of production tasks. 
Instrumentation goals deal with operational matters, does not include business intelligence use cases.

## Why OTel:
Create a better experience for engineers, support staff and customers.
Want to enable their customers to have a “bring your own telemetry offering.” The company wants to rely on OTel to give the choice to their own customers on where they want to export the telemetry from their platform. 

## Challenges:
1. Getting engineers on other teams bootstrapped to use OpenTelemetry
  - Their team has created some install guides and opinionated setups, but this takes time and is not complete. 
     - The ergonomics for adding span attributes are a challenge in some languages and not generally consistent
     - Specific Ask: There are reasonable configuration defaults, but not every language does it the same way. 
    - The centralized observability team commonly reviews PRs from other teams so they can provide feedback before merge which help enforce rules and control costs
- Documentation is confusing and overwhelming
  - Specific Ask: Create a consistent voice in the documentation. 
  - The company contributes upstream to project documentation
2. Maturity of auto-instrumentation
  - Things don’t work ‘magically’ for other team developers; this is a different experience than most developers have had with commercial solutions.  
3. Maturity of semantic conventions is hindering enthusiasm and wide internal adoption
They’re defining internal semantic conventions 

## Positive notes:
A recent expansion which includes node.js and rust components has recently gone to production and:  “so far so great”

## Notes of Interest: 
- Their usage of the collector is minimal, running a PoC now.  They would like to get recommendations on the right sizing for the collector. Requires managing the authentication layer with their proxy to make it work.  
- They have an internal distribution of Ruby OTel.
- Their company is very logs focused; tracing is not widely adopted. A logs focus has affected how they adopt the project considering the emerging maturity of logs. 
