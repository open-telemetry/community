# Contributing

Welcome to OpenTelemetry community repository!

Before you start - see OpenTelemetry general [contributing](guides/contributor/README.md)
requirements and recommendations.

## Updating SIG information on the README.md

The SIG tables on the [README.md](README.md) page are generated from [`workstreams.yml`](workstreams.yml) and [`people.yml`](people.yml).

To regenerate those tables after updating any `workstreams.yml` content, run:

```bash
make table-generation
```
