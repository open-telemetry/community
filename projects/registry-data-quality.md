# OpenTelemetry Registry Data Quality Improvements

## Background and description

The [OpenTelemetry registry](https://opentelemetry.io/ecosystem/registry/) has been a part of the OpenTelemetry project from the start:
inherited from the [OpenTracing registry](https://opentracing.io/registry/) it provides an entry point for end users to find all the
building blocks they need for observability.

The registry is a part of the [OpenTelemetry website](https://opentelemetry.io/) and currently maintained by SIG Communications as part
of that.

Although hidden under `Ecosystem > Registry` in the navigation, the registry is among the top 10 pages YTD
([based on Google Analytics Data](https://lookerstudio.google.com/s/qhPHQtyfRbU)).

In the last months SIG Comms implemented a set of changes to the registry, to make it more user-friendly and easier to find:

- [A semi-automatic semi-complete scanner](https://github.com/open-telemetry/opentelemetry.io/pull/1920)
- [Rework of the design](https://github.com/open-telemetry/opentelemetry.io/pull/3730), including a new search engine, badges, quick installation instructions
- [A daily run workflow that keeps package versions up-to-date](https://github.com/open-telemetry/opentelemetry.io/pull/3840)
- [A JSON schema definition to verify registry entry format](https://github.com/open-telemetry/opentelemetry.io/pull/4805)
- [Included the registry in many pages, including the sidebar navigation for all languages and the collector](https://github.com/open-telemetry/opentelemetry.io/pull/3932)

Overall, the registry is in a good shape and is slowly turning into a place that people use for it's original intend.

### Current challenges

While being reworks in incremental steps in the last few months, the registry is still facing a set of challenges, that require a bigger
review and eventually a collaboration across many SIGs to be addressed:

1. Besides the update of package versions, the maintenance is a manual process:
   1. Packages from different project repositories are either detected by a semi-automatic scanner, that needs to be run
      manually, or by SIGs reporting new entries themselves.
   2. After a package has been added to the registry, it is a manual process to verify if the package is still available and
      if the meta-data is still correct.
2. Packages lack a lot of information, and the information available is sometimes of bad quality. Metadata that might be available
   for packages is not in a human readable format, or in the case of the collector (`mdatagen`-data) not consumed by the registry.
3. [Vendors](https://opentelemetry.io/ecosystem/vendors/), [Integrations](https://opentelemetry.io/ecosystem/integrations/), [Adopters](https://opentelemetry.io/ecosystem/adopters/) and [Distributions](https://opentelemetry.io/ecosystem/distributions/) are separated out into their own pages, and entries on these pages are also hard to maintain and verify.
4. Adding an entry to the registry requires the addition of a YAML file, in a pre-defined format, that until recently has not been enforced consistently.

All these issues are mostly related to the quality of the data, i.e. what is available, what is outdated, how detailed is the data
and how useable is that data. If we address those issues end users will see the registry as a valuable place and will use
it to find the building blocks they need, and by reaching that state, we can use the registry to accomplish other goals, like

- making end users aware of non-otel-community created components they can use. Combined with a system to label "good quality"
  packages, we can go from building everything as a community to endorsing good work.
- having a complete overview ourselves of the components that exist within the project and outside in the wider ecosystem
- having a single place that allows end users not only to learn what is available, but also what they get from using a
  certain component (stability levels, supported signals, exported trace/metric/log names)
- having a central place with all the names and versions, that can be used in different places of the registry.
- communicating certain preferences of our project, i.e. by tagging instrumentations as "native" or "first party" we can
  indicate that native instrumentations are best, vs having instrumentation libraries.

### Goals, objectives, and requirements

The goal of this project is to improve the quality of the data in the registry in a way, that it is

- complete for project-owned components (collector, instrumentation libraries, exporters, resource detectors, loggers)
- always up-to-date for all components (versions, deprecation, deletions)
- fine-grained, meaningful and of consistent quality (not only some basic names and description, but meta data like stability, signals, etc.)
- labelled in a way that we can communicate certain preferences (native, "by first party", etc.)
- kept up-to-date by automatic workflows

The goal of this particular project is _only_ about the data quality and tooling that helps to build and keep the data up-to-date.
Changing the software of the registry is out of scope, except it will be helpful to accomplish any of the objectives mentioned above.

To accomplish this goal, this project requires support from all SIGs delivering software artifacts, consumed by end users, this includes
especially the [Implementation SIGs](https://github.com/open-telemetry/community/?tab=readme-ov-file#implementation-sigs), since this
project will create some standards to make data readable, that might need to be implemented across the project

## Deliverables

To accomplish the goals mentioned above this project, will create the following deliverables

- A machine-readable meta-data format and schema, that contains all the potential details of a registry entry. This may build on top of `mdatagen`,
  but as part of the project other existing formats will be reviewed for consideration.
- Tooling to read that data from different sources (pull or push, tbd) to keep the registry up-to-date
- A tagging and labelling system to highlight components that fit into certain criteria

## Staffing / Help Wanted

GC/TC sponsors:

- `<tbd>`
- `<tbd>`

Contributors:

- `<tbd>`

**Note**: there is no goal to create a new SIG for this. This is a (hopefully) mid-term living group of people collaborating to accomplish this goal,
or this may be part of an existing SIG (Comms, Project Infra, ...), but with some dedicated resources.

## Timeline

`<tbd>`

## Project Board

`<tbd>`

## SIG Meetings and Other Info

`<tbd>`
