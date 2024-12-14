# Otel/STEF

## Background and description

Otel/STEF (Sequential Tabular Encoding Format) is a new data format and network 
protocol for OpenTelemetry data.

On the tested datasets Otel/STEF payloads are several times more compact than OTLP, with 
comparable serialization speed. Otel/STEF payloads are also smaller and serialization is 
faster than Otel Arrow Phase 1.

Otel/STEF targets a narrower niche than OTLP or Otel Arrow and is more efficient
for that niche. Otel/STEF is optimized for payload size and fast serialization
and is primarily intended to be used in the last communication leg from Otel Collector
to observability backend where large volumes of data make network cost
savings significant.

Otel/STEF supports options that allow trading speed for size. At the highest 
speed setting it can be faster than OTLP (_including_ conversion to/from pdata), while 
producing significantly smaller payloads.

A draft specification and a prototype implementation of Otel/STEF is attached to thi
proposal.

### Goals, objectives, and requirements

The project goals are the following:

- Implement missing capabilities in the [prototype implementation](#prototypes-and-draft-specs).
- Extend benchmarking and test suite to cover more variety of datasets.
- Turn the prototype into a production grade implementation.
- Add support for traces and logs (the prototype implements metrics only).
- Add Otel/STEF exporter and Otel/STEF receiver to Otel Collector.
- Publish benchmark-justified guidelines on applicability of Otel/STEF vs OTLP vs Otel
  Arrow.
- Refine and stabilize Otel/STEF specification and encourage its implementation
  inside or outside Otel.

Project non-goals:

- We do not plan to offer Otel/STEF as a general-purpose replacement for OTLP or for Otel
  Arrow.

Unlike
[OTLP](https://github.com/open-telemetry/opentelemetry-proto/blob/main/docs/design-goals.md),
for Otel/STEF it is not a goal to be a universal protocol useful for all
node types. We do not plan it to be used by instrumented applications 
and thus don't need Otel/STEF to be implemented in all language SDKs. This 
significantly reduces the total engineering cost of this project since we
only need the Go implementation for the Otel Collector.

Otel/STEF design takes into account learnings from Otel Arrow and borrows some of the
technics (e.g. dictionary encoding and gRPC streams).

## Benchmarks

A fairly full-featured, non-production grade prototype Otel/STEF implementation for 
metric data exists in Go. It demonstrates wire-size and performance improvements over 
OTLP and Otel Arrow.

A small subset of existing benchmarks is reproduced in this section. For more detailed 
speed and size tests and comparison to other protocols see
[benchmarks](https://github.com/tigrannajaryan/stef/tree/main/benchmarks).

The benchmarks are run on the highest compression / slowest speed option.

### Wire Size

The following benchmarks show zstd-compressed wire sizes of OTLP vs Otel/STEF vs Otel 
Arrow. Benchmarks are run using
[Otel Arrow bench](https://github.com/open-telemetry/otel-arrow), with Otel/STEF
prototype implementation added for comparison.

Dataset `hipstershop_metrics.pb`:

| BATCH SIZE         | OTLP                    | Otel/STEF                       | OTEL ARROW                      |
|--------------------|-------------------------|---------------------------------|---------------------------------|
| Compressed (bytes) |                         |                                 |                                 |
| batch_size: 128    | 4579  (total: 1.6 MB)   | 947 (x  4.83) (total: 323 kB)   | 2067 (x  2.22) (total: 705 kB)  |
| batch_size: 1024   | 24764  (total: 1.1 MB)  | 5622 (x  4.40) (total: 242 kB)  | 10773 (x  2.30) (total: 463 kB) |
| batch_size: 2048   | 39325  (total: 865 kB)  | 9209 (x  4.27) (total: 203 kB)  | 17808 (x  2.21) (total: 392 kB) |
| batch_size: 4096   | 64824  (total: 713 kB)  | 15501 (x  4.18) (total: 170 kB) | 29421 (x  2.20) (total: 324 kB) |
| batch_size: 16384  | 196877  (total: 591 kB) | 38376 (x  5.13) (total: 115 kB) | 86299 (x  2.28) (total: 259 kB) |

Dataset `multivariate-metrics.pb`:

| BATCH SIZE         | OTLP                     | Otel/STEF                      | OTEL ARROW                       |
|--------------------|--------------------------|--------------------------------|----------------------------------|
| Compressed (bytes) |                          |                                |                                  |
| batch_size: 128    | 20355  (total: 1.6 MB)   | 1453 (x 14.00) (total: 115 kB) | 4114 (x  4.95) (total: 325 kB)   |
| batch_size: 1024   | 157995  (total: 1.6 MB)  | 9828 (x 16.07) (total: 98 kB)  | 25103 (x  6.29) (total: 251 kB)  |
| batch_size: 2048   | 315777  (total: 1.6 MB)  | 19205 (x 16.44) (total: 96 kB) | 46502 (x  6.79) (total: 232 kB)  |
| batch_size: 4096   | 526047  (total: 1.6 MB)  | 30948 (x 17.00) (total: 93 kB) | 73267 (x  7.18) (total: 220 kB)  |
| batch_size: 16384  | 1573005  (total: 1.6 MB) | 89450 (x 17.59) (total: 90 kB) | 193842 (x  8.11) (total: 194 kB) |

To summarize, on these datasets Otel/STEF is smaller than OTLP about 4-15 times, and 
is approximately 1.5-2 times smaller than Otel Arrow.

### Speed

The following benchmarks show serialization/deserialization/conversion speed of OTLP vs 
Otel/STEF vs Otel Arrow Phase 1.

Dataset `hipstershop_metrics.pb`:

| BATCH SIZE               | OTLP           | Otel/STEF              | OTEL ARROW              |
|--------------------------|----------------|------------------------|-------------------------|
| Exporter steps           |                |                        |                         |
| OTLP -> OTel Arrow conv. |                |                        |                         |
| batch_size: 128          | Not Applicable | 0.690ms/msg (x  0.00)  | 0.930ms/msg (x  0.00)   |
| batch_size: 1024         | Not Applicable | 5.703ms/msg (x  0.00)  | 6.477ms/msg (x  0.00)   |
| batch_size: 2048         | Not Applicable | 8.833ms/msg (x  0.00)  | 12.956ms/msg (x  0.00)  |
| batch_size: 4096         | Not Applicable | 13.567ms/msg (x  0.00) | 28.200ms/msg (x  0.00)  |
| batch_size: 16384        | Not Applicable | 41.819ms/msg (x  0.00) | 144.682ms/msg (x  0.00) |
| Protobuf serialization   |                |                        |                         |
| batch_size: 128          | 0.083ms/msg    | 0.247ms/msg (x  0.34)  | 0.004ms/msg (x 20.73)   |
| batch_size: 1024         | 0.632ms/msg    | 1.840ms/msg (x  0.34)  | 0.012ms/msg (x 54.57)   |
| batch_size: 2048         | 1.263ms/msg    | 3.094ms/msg (x  0.41)  | 0.024ms/msg (x 52.77)   |
| batch_size: 4096         | 2.515ms/msg    | 2.929ms/msg (x  0.86)  | 0.026ms/msg (x 95.18)   |
| batch_size: 16384        | 9.353ms/msg    | 4.611ms/msg (x  2.03)  | 0.119ms/msg (x 78.37)   |
| Compression              |                |                        |                         |
| batch_size: 128          | 0.193ms/msg    | 0.013ms/msg (x 14.39)  | 0.102ms/msg (x  1.90)   |
| batch_size: 1024         | 1.097ms/msg    | 0.028ms/msg (x 39.79)  | 0.802ms/msg (x  1.37)   |
| batch_size: 2048         | 1.508ms/msg    | 0.074ms/msg (x 20.40)  | 0.727ms/msg (x  2.07)   |
| batch_size: 4096         | 2.746ms/msg    | 0.047ms/msg (x 58.74)  | 1.091ms/msg (x  2.52)   |
| batch_size: 16384        | 9.026ms/msg    | 0.044ms/msg (x207.36)  | 3.256ms/msg (x  2.77)   |
| Sub total                |                |                        |                         |
| batch_size: 128          | 0.276ms/msg    | 0.951ms/msg (x  0.29)  | 1.036ms/msg (x  0.27)   |
| batch_size: 1024         | 1.729ms/msg    | 7.571ms/msg (x  0.23)  | 7.291ms/msg (x  0.24)   |
| batch_size: 2048         | 2.771ms/msg    | 12.001ms/msg (x  0.23) | 13.707ms/msg (x  0.20)  |
| batch_size: 4096         | 5.262ms/msg    | 16.543ms/msg (x  0.32) | 29.318ms/msg (x  0.18)  |
| batch_size: 16384        | 18.379ms/msg   | 46.474ms/msg (x  0.40) | 148.057ms/msg (x  0.12) |
| Receiver steps           |                |                        |                         |
| Decompression            |                |                        |                         |
| batch_size: 128          | 0.063ms/msg    | 0.001ms/msg (x 43.02)  | 0.050ms/msg (x  1.24)   |
| batch_size: 1024         | 0.376ms/msg    | 0.003ms/msg (x109.00)  | 0.247ms/msg (x  1.52)   |
| batch_size: 2048         | 0.608ms/msg    | 0.007ms/msg (x 81.33)  | 0.460ms/msg (x  1.32)   |
| batch_size: 4096         | 1.047ms/msg    | 0.007ms/msg (x150.92)  | 0.842ms/msg (x  1.24)   |
| batch_size: 16384        | 3.233ms/msg    | 0.009ms/msg (x357.56)  | 2.665ms/msg (x  1.21)   |
| Protobuf deserialization |                |                        |                         |
| batch_size: 128          | 0.247ms/msg    | 0.224ms/msg (x  1.10)  | 0.005ms/msg (x 48.27)   |
| batch_size: 1024         | 1.875ms/msg    | 1.697ms/msg (x  1.11)  | 0.021ms/msg (x 91.37)   |
| batch_size: 2048         | 3.325ms/msg    | 2.665ms/msg (x  1.25)  | 0.032ms/msg (x103.28)   |
| batch_size: 4096         | 6.900ms/msg    | 4.106ms/msg (x  1.68)  | 0.044ms/msg (x156.26)   |
| batch_size: 16384        | 24.714ms/msg   | 11.596ms/msg (x  2.13) | 0.166ms/msg (x148.68)   |
| OTel Arrow -> OTLP conv. |                |                        |                         |
| batch_size: 128          | 0.000ms/msg    | 0.000ms/msg (x  0.73)  | 0.471ms/msg (x  0.00)   |
| batch_size: 1024         | 0.000ms/msg    | 0.000ms/msg (x  0.60)  | 3.328ms/msg (x  0.00)   |
| batch_size: 2048         | 0.000ms/msg    | 0.000ms/msg (x  0.66)  | 6.260ms/msg (x  0.00)   |
| batch_size: 4096         | 0.000ms/msg    | 0.000ms/msg (x  0.40)  | 11.690ms/msg (x  0.00)  |
| batch_size: 16384        | 0.000ms/msg    | 0.000ms/msg (x  0.94)  | 44.226ms/msg (x  0.00)  |
| Sub total                |                |                        |                         |
| batch_size: 128          | 0.310ms/msg    | 0.226ms/msg (x  1.37)  | 0.526ms/msg (x  0.59)   |
| batch_size: 1024         | 2.251ms/msg    | 1.700ms/msg (x  1.32)  | 3.596ms/msg (x  0.63)   |
| batch_size: 2048         | 3.933ms/msg    | 2.672ms/msg (x  1.47)  | 6.752ms/msg (x  0.58)   |
| batch_size: 4096         | 7.947ms/msg    | 4.113ms/msg (x  1.93)  | 12.576ms/msg (x  0.63)  |
| batch_size: 16384        | 27.947ms/msg   | 11.606ms/msg (x  2.41) | 47.057ms/msg (x  0.59)  |
| ======================== |                |                        |                         |
| End-to-end               |                |                        |                         |
| Total                    |                |                        |                         |
| batch_size: 128          | 0.586ms/msg    | 1.177ms/msg (x  0.50)  | 1.562ms/msg (x  0.38)   |
| batch_size: 1024         | 3.980ms/msg    | 9.272ms/msg (x  0.43)  | 10.888ms/msg (x  0.37)  |
| batch_size: 2048         | 6.704ms/msg    | 14.674ms/msg (x  0.46) | 20.459ms/msg (x  0.33)  |
| batch_size: 4096         | 13.209ms/msg   | 20.656ms/msg (x  0.64) | 41.894ms/msg (x  0.32)  |
| batch_size: 16384        | 46.327ms/msg   | 58.080ms/msg (x  0.80) | 195.115ms/msg (x  0.24) |

Dataset `multivariate-metrics.pb`:

| BATCH SIZE               | OTLP           | Otel/STEF               | OTEL ARROW               |
|--------------------------|----------------|-------------------------|--------------------------|
| Exporter steps           |                |                         |                          |
| OTLP -> OTel Arrow conv. |                |                         |                          |
| batch_size: 128          | Not Applicable | 1.923ms/msg (x  0.00)   | 6.309ms/msg (x  0.00)    |
| batch_size: 1024         | Not Applicable | 11.709ms/msg (x  0.00)  | 51.335ms/msg (x  0.00)   |
| batch_size: 2048         | Not Applicable | 22.592ms/msg (x  0.00)  | 128.277ms/msg (x  0.00)  |
| batch_size: 4096         | Not Applicable | 38.261ms/msg (x  0.00)  | 313.769ms/msg (x  0.00)  |
| batch_size: 16384        | Not Applicable | 108.851ms/msg (x  0.00) | 1963.445ms/msg (x  0.00) |
| Protobuf serialization   |                |                         |                          |
| batch_size: 128          | 0.622ms/msg    | 0.289ms/msg (x  2.15)   | 0.013ms/msg (x 48.64)    |
| batch_size: 1024         | 4.741ms/msg    | 1.027ms/msg (x  4.61)   | 0.043ms/msg (x109.74)    |
| batch_size: 2048         | 9.056ms/msg    | 1.996ms/msg (x  4.54)   | 0.176ms/msg (x 51.52)    |
| batch_size: 4096         | 15.519ms/msg   | 3.241ms/msg (x  4.79)   | 0.274ms/msg (x 56.58)    |
| batch_size: 16384        | 47.248ms/msg   | 9.422ms/msg (x  5.01)   | 0.855ms/msg (x 55.25)    |
| Compression              |                |                         |                          |
| batch_size: 128          | 0.772ms/msg    | 0.015ms/msg (x 50.15)   | 0.218ms/msg (x  3.54)    |
| batch_size: 1024         | 5.205ms/msg    | 0.033ms/msg (x159.55)   | 1.717ms/msg (x  3.03)    |
| batch_size: 2048         | 9.382ms/msg    | 0.033ms/msg (x285.89)   | 2.153ms/msg (x  4.36)    |
| batch_size: 4096         | 15.868ms/msg   | 0.045ms/msg (x355.14)   | 3.904ms/msg (x  4.06)    |
| batch_size: 16384        | 55.229ms/msg   | 0.085ms/msg (x649.12)   | 9.948ms/msg (x  5.55)    |
| Sub total                |                |                         |                          |
| batch_size: 128          | 1.394ms/msg    | 2.228ms/msg (x  0.63)   | 6.540ms/msg (x  0.21)    |
| batch_size: 1024         | 9.946ms/msg    | 12.769ms/msg (x  0.78)  | 53.095ms/msg (x  0.19)   |
| batch_size: 2048         | 18.438ms/msg   | 24.620ms/msg (x  0.75)  | 130.606ms/msg (x  0.14)  |
| batch_size: 4096         | 31.387ms/msg   | 41.547ms/msg (x  0.76)  | 317.947ms/msg (x  0.10)  |
| batch_size: 16384        | 102.478ms/msg  | 118.358ms/msg (x  0.87) | 1974.248ms/msg (x  0.05) |
| Receiver steps           |                |                         |                          |
| Decompression            |                |                         |                          |
| batch_size: 128          | 0.340ms/msg    | 0.002ms/msg (x226.20)   | 0.174ms/msg (x  1.95)    |
| batch_size: 1024         | 2.425ms/msg    | 0.005ms/msg (x531.95)   | 1.127ms/msg (x  2.15)    |
| batch_size: 2048         | 4.511ms/msg    | 0.006ms/msg (x700.24)   | 2.041ms/msg (x  2.21)    |
| batch_size: 4096         | 7.391ms/msg    | 0.010ms/msg (x737.08)   | 3.081ms/msg (x  2.40)    |
| batch_size: 16384        | 22.998ms/msg   | 0.016ms/msg (x1460.22)  | 9.069ms/msg (x  2.54)    |
| Protobuf deserialization |                |                         |                          |
| batch_size: 128          | 1.570ms/msg    | 0.731ms/msg (x  2.15)   | 0.015ms/msg (x104.49)    |
| batch_size: 1024         | 12.099ms/msg   | 4.838ms/msg (x  2.50)   | 0.066ms/msg (x183.76)    |
| batch_size: 2048         | 23.459ms/msg   | 9.521ms/msg (x  2.46)   | 0.204ms/msg (x115.15)    |
| batch_size: 4096         | 37.510ms/msg   | 16.177ms/msg (x  2.32)  | 0.484ms/msg (x 77.56)    |
| batch_size: 16384        | 114.350ms/msg  | 46.924ms/msg (x  2.44)  | 0.624ms/msg (x183.30)    |
| OTel Arrow -> OTLP conv. |                |                         |                          |
| batch_size: 128          | 0.000ms/msg    | 0.000ms/msg (x  0.99)   | 2.640ms/msg (x  0.00)    |
| batch_size: 1024         | 0.000ms/msg    | 0.000ms/msg (x  0.27)   | 20.898ms/msg (x  0.00)   |
| batch_size: 2048         | 0.000ms/msg    | 0.000ms/msg (x  0.94)   | 43.580ms/msg (x  0.00)   |
| batch_size: 4096         | 0.000ms/msg    | 0.000ms/msg (x  3.14)   | 76.346ms/msg (x  0.00)   |
| batch_size: 16384        | 0.000ms/msg    | 0.001ms/msg (x  0.38)   | 307.095ms/msg (x  0.00)  |
| Sub total                |                |                         |                          |
| batch_size: 128          | 1.910ms/msg    | 0.733ms/msg (x  2.61)   | 2.829ms/msg (x  0.68)    |
| batch_size: 1024         | 14.524ms/msg   | 4.843ms/msg (x  3.00)   | 22.091ms/msg (x  0.66)   |
| batch_size: 2048         | 27.970ms/msg   | 9.528ms/msg (x  2.94)   | 45.824ms/msg (x  0.61)   |
| batch_size: 4096         | 44.902ms/msg   | 16.188ms/msg (x  2.77)  | 79.911ms/msg (x  0.56)   |
| batch_size: 16384        | 137.348ms/msg  | 46.941ms/msg (x  2.93)  | 316.788ms/msg (x  0.43)  |
| ======================== |                |                         |                          |
| End-to-end               |                |                         |                          |
| Total                    |                |                         |                          |
| batch_size: 128          | 3.305ms/msg    | 2.961ms/msg (x  1.12)   | 9.369ms/msg (x  0.35)    |
| batch_size: 1024         | 24.470ms/msg   | 17.612ms/msg (x  1.39)  | 75.186ms/msg (x  0.33)   |
| batch_size: 2048         | 46.408ms/msg   | 34.148ms/msg (x  1.36)  | 176.430ms/msg (x  0.26)  |
| batch_size: 4096         | 76.289ms/msg   | 57.735ms/msg (x  1.32)  | 397.859ms/msg (x  0.19)  |
| batch_size: 16384        | 239.826ms/msg  | 165.299ms/msg (x  1.45) | 2291.036ms/msg (x  0.10) |

To summarize, on these datasets Otel/STEF is the fastest when receiving and is the second 
fastest when exporting.

## Deliverables

- stef-go: STEF supporting libraries for Go.
- stef-gogrpc: STEF/gRPC protocol implementation in Go.
- stef-pdata: Collector pdata <-> Otel/STEF converters.
- Otel/STEF exporter and receiver, in
  [open-telemetry/opentelemetry-collector-contrib](https://github.com/open-telemetry/opentelemetry-collector-contrib)
  repository.
- stef-spec:  Otel/STEF format and protocol specification repository, with publication on
  [https://opentelemetry.io/docs/](https://opentelemetry.io/docs/).

## Staffing / Help Wanted

The project already has all necessary staffing, see the next section. Additional 
participants are welcome.

### Required staffing

- Project Lead, TC Sponsor, Go implementation engineer:
[Tigran Najaryan](https://github.com/tigrannajaryan)
- Second TC Sponsor: [Josh Suereth](https://github.com/jsuereth)
- GC liaison: [Morgan McLean](https://github.com/mtwo)
- Collector Maintainer: [Dmitrii Anoshin](https://github.com/dmitryax)

## Timeline

- 2025 Q2: Otel/STEF production grade implementation in Go, Otel Collector exporter and 
  receiver in Development. Publish STEF specification in Development.
- 2025 Q2: Add support for traces and logs.
- 2025 Q3: Stabilization and improvements period.
- 2025 Q4: Beta specification and implementation.
- 2026 Q1+: Stable specification and implementation.

## Project Board

Project board link to be added here.

## SIG Meetings and Other Info

SIG meeting to be scheduled once the project is approved.

## FAQ

Q. What's Otel/STEF data model?<br/>
A. Otel/STEF uses OpenTelemetry data model.

Q. Is Otel/STEF based on Protobuf or some other well-known encoding?<br/>
A. No, the format is a custom design. STEF/gRPC uses a basic Protobuf envelope that 
carries STEF-formatted bytes.

Q. Why is STEF not targeted as an OTLP or Otel Arrow replacement?<br/>
A. STEF is a custom format that is harder to implement and maintain than 
OTLP or Otel Arrow. Implementing it in all Otel-supported languages would have a 
high engineering cost that is unlikely to be justified. We only plan to implement and 
maintain Otel/STEF in Go to keep engineering costs under control.

Q. Are there any Otel/STEF implementations?<br/>
A. Yes, the following prototype implementations exist: Go serializer/deserializer, 
STEF/gRPC protocol implementation, Otel Collector exporter, STEF/gRPC test server.

Q. What signals are supported?<br/>
A. The current prototype supports metrics only. We plan to add support for traces and 
logs.

Q. How does Otel/STEF achieve high compression levels?<br/>
A. It is a combination of several methods:
- Dictionary encoding of primitive values (e.g. attribute keys) and complex objects
  (e.g. Resources).
- Delta encoding of primitive values (e.g. Int64 numeric measurements) and complex 
  objects (e.g. attribute lists).
- Sorting of input data to improve locality and aid delta encoding.
- XOR encoding for floating point values (e.g. numeric measurements and histogram
  boundaries) and delta-of-delta encoding of integer values (e.g. timestamps) as 
  described in [this paper](https://www.vldb.org/pvldb/vol8/p1816-teller.pdf).
- Columnar encoding, resulting in better compressibility by general-purpose compressors.
- Compact variable-length encoding for numeric values.
- Tight bit packing.
- Keeping the state of the dictionaries and of zstd compressors/decompressor between
  the gRPC messages.

For detailed data format and network protocol description see
[the spec](https://github.com/tigrannajaryan/stef/tree/main/stef-spec).

Q. Why not use Parquet, Arrow, (insert your preferred format) instead?<br/>
A. Otel/STEF is specifically optimized for OpenTelemetry data. Benchmarks demonstrate
Otel/STEF outperforms existing formats on speed while matching or outperforming on size.

## Prototypes and Draft Specs

- [benchmarks](https://github.com/tigrannajaryan/stef/tree/main/benchmarks): Benchmarks, tests, comparisons to other formats.
- [otelcol](https://github.com/tigrannajaryan/stef/tree/main/otelcol): Otel/STEF protocol Collector exporter implementation.
- [stef-go](https://github.com/tigrannajaryan/stef/tree/main/stef-go): STEF supporting libraries for Go.
- [stef-gogrpc](https://github.com/tigrannajaryan/stef/tree/main/stef-gogrpc): STEF/gRPC protocol implementation in Go.
- [stef-otel](https://github.com/tigrannajaryan/stef/tree/main/stef-otel): Otel/STEF protocol schema and generated code in Go.
- [stef-pdata](https://github.com/tigrannajaryan/stef/tree/main/stef-pdata): Collector 
  pdata <-> Otel/STEF converters.
- [stef-spec](https://github.com/tigrannajaryan/stef/tree/main/stef-spec): STEF Specification and Protobuf definitions.
- [stefgen](https://github.com/tigrannajaryan/stef/tree/main/stefgen): Generates serializers from STEF schema.
