# Contributing

Welcome to OpenTelemetry community repository!

Before you start - see OpenTelemetry general [contributing](guides/contributor/README.md)
requirements and recommendations.

## Updating SIG information

The SIG summary tables on the [README.md](README.md) page, the detailed SIG information on the [`sigs.md`](sigs.md) page, and the sponsorship load tables on the [`sig-sponsorship-ledger.md`](sig-sponsorship-ledger.md) page are generated from [`workstreams.yml`](workstreams.yml) and [`people.yml`](people.yml).
The [`community-members.md`](community-members.md) page is also generated from [`people.yml`](people.yml).

To regenerate after updating any `workstreams.yml` or `people.yml` content, run:

```bash
make generate
```
