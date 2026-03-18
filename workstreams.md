# Workstream Report

## Legend

**Node color** — TC sponsorship level:

| Color | Level | Meaning |
|-------|-------|---------|
| Green | Leading | TC sponsor actively driving the workstream |
| Blue | Guiding | TC sponsor providing guidance |
| Purple | Escalating | TC sponsor available for escalation |
| Gray | TBD | Sponsor assigned, level not yet determined |
| Red | None | No TC sponsor assigned |

**Node shape** — workstream kind: rectangle = SIG · pill = Working Group

**Name suffix** — SIG category: `(spec)` Specification · `(impl)` Implementation · `(cross)` Cross-cutting

**Arrows** (`-->`) — parent workstream points to child workstream

## Workstream Hierarchy

```mermaid
%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 40}}}%%
graph LR

  classDef tc_leading fill:#c8e6c9,stroke:#388e3c,color:#1b5e20
  classDef tc_guiding fill:#bbdefb,stroke:#1976d2,color:#0d47a1
  classDef tc_escalating fill:#e1bee7,stroke:#7b1fa2,color:#4a148c
  classDef tc_tbd fill:#f5f5f5,stroke:#9e9e9e,color:#424242
  classDef tc_none fill:#ffcdd2,stroke:#e53935,color:#b71c1c

  communications["Communications (Website, Documentation, etc.)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: Jack Berg (escalating)"]
  communications --> localization_bn
  localization_bn["Bengali (bn)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> localization_zh_cn
  localization_zh_cn["Chinese (zh-CN)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: Reiley Yang (tbd)"]
  communications --> localization_fr
  localization_fr["French (fr-FR)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> localization_ja
  localization_ja["Japanese (ja-JA)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> getting_started_docs
  getting_started_docs(["New Getting Started Documentation and Reference Application<br/>Kind: working-group<br/>GC: Severin Neumann<br/>TC: Jack Berg (tbd)"])
  communications --> ecosystem_explorer
  ecosystem_explorer(["OpenTelemetry Ecosystem Explorer<br/>Kind: working-group<br/>GC: Severin Neumann<br/>TC: Jack Berg (escalating)"])
  communications --> localization_pt_br
  localization_pt_br["Portuguese (pt-BR)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> localization_ro
  localization_ro["Romanian (ro-RO)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> localization_es
  localization_es["Spanish (es-ES)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  communications --> localization_uk
  localization_uk["Ukrainian (uk-UA)<br/>Kind: sig (cross)<br/>GC: Severin Neumann<br/>TC: unsponsored"]
  spec_general["Specification: General + OTel Maintainers Sync<br/>Kind: sig (spec)<br/>TC: unsponsored"]
  spec_general --> semconv_general
  semconv_general["Semantic Conventions: General<br/>Kind: sig (spec)<br/>GC: Trask Stalnaker<br/>TC: Armin Ruech (leading), Josh Suereth (leading), Liudmila Molkova (leading)"]
  semconv_general --> semconv_cicd
  semconv_cicd["Semantic Conventions: CI/CD<br/>Kind: sig (spec)<br/>GC: Marylia Gutierrez<br/>TC: Carlos Alberto Cortez (escalating)"]
  semconv_cicd --> cicd_phase_2
  cicd_phase_2(["CI/CD Observability SIG Phase 2<br/>Kind: working-group<br/>GC: Marylia Gutierrez<br/>TC: Carlos Alberto Cortez (tbd)"])
  semconv_general --> gen_ai
  gen_ai["Semantic Conventions and Instrumentation: GenAI<br/>Kind: sig (spec)<br/>GC: Ted Young<br/>TC: Liudmila Molkova (leading)"]
  semconv_general --> semconv_k8s
  semconv_k8s["Semantic Conventions: K8s<br/>Kind: sig (spec)<br/>GC: Alolita Sharma<br/>TC: David Ashpole (leading)"]
  semconv_general --> semconv_rpc
  semconv_rpc["Semantic Conventions: RPC<br/>Kind: sig (spec)<br/>GC: Trask Stalnaker<br/>TC: Liudmila Molkova (guiding)"]
  semconv_general --> semconv_security
  semconv_security["Semantic Conventions: Security<br/>Kind: sig (spec)<br/>GC: Trask Stalnaker<br/>TC: Josh Suereth (escalating)"]
  semconv_general --> semconv_service_deployment
  semconv_service_deployment["Semantic Conventions: Service and Deployment<br/>Kind: sig (spec)<br/>GC: Trask Stalnaker<br/>TC: Josh Suereth (escalating)"]
  semconv_general --> semconv_system_metrics
  semconv_system_metrics["Semantic Conventions: System Metrics<br/>Kind: sig (spec)<br/>GC: Pablo Baeyens<br/>TC: Josh Suereth (escalating)"]
  semconv_general --> semconv_tooling
  semconv_tooling["Semantic Conventions: Tooling<br/>Kind: sig (impl)<br/>GC: Juraci Paixão Kröhling<br/>TC: Josh Suereth (leading), Liudmila Molkova (leading)"]
  spec_general --> spec_entities
  spec_entities["Specification: Entities<br/>Kind: sig (spec)<br/>GC: Severin Neumann<br/>TC: Josh Suereth (leading), Tigran Najaryan (leading)"]
  spec_general --> spec_logs
  spec_logs["Specification: Logs<br/>Kind: sig (spec)<br/>GC: Trask Stalnaker<br/>TC: Liudmila Molkova (guiding)"]
  spec_general --> sampling
  sampling["Specification: Sampling<br/>Kind: sig (spec)<br/>GC: Juraci Paixão Kröhling<br/>TC: Joshua MacDonald (guiding)"]
  collector["Collector<br/>Kind: sig (impl)<br/>GC: Pablo Baeyens<br/>TC: BogdanDrutu (guiding), Joshua MacDonald (guiding)"]
  collector --> collector_v1
  collector_v1(["Collector v1<br/>Kind: working-group<br/>GC: Juraci Paixão Kröhling<br/>TC: unsponsored"])
  collector --> agentic_workflow
  agentic_workflow(["OpenTelemetry Collector Agentic Workflows<br/>Kind: working-group<br/>GC: Pablo Baeyens<br/>TC: unsponsored"])
  end_user["End-User SIG<br/>Kind: sig (cross)<br/>GC: Marylia Gutierrez<br/>TC: Jack Berg (escalating)"]
  end_user --> otel_blueprints
  otel_blueprints(["OTel Blueprints<br/>Kind: working-group<br/>GC: Marylia Gutierrez<br/>TC: Reiley Yang (escalating)"])
  dotnet_auto_instr[".NET: Automatic Instrumentation<br/>Kind: sig (impl)<br/>GC: Morgan McLean<br/>TC: Reiley Yang (escalating)"]
  dotnet[".NET: SDK<br/>Kind: sig (impl)<br/>GC: Morgan McLean<br/>TC: Reiley Yang (escalating)"]
  android["Android: SDK + Automatic Instrumentation<br/>Kind: sig (impl)<br/>GC: Ted Young<br/>TC: Jack Berg (escalating)"]
  arrow["Arrow<br/>Kind: sig (impl)<br/>GC: Trask Stalnaker<br/>TC: Joshua MacDonald (leading)"]
  zig_sig_bootstrap(["Bootstrap Zig Special Interest Group<br/>Kind: working-group<br/>GC: Alolita Sharma<br/>TC: Joshua MacDonald (tbd)"])
  browser["Browser<br/>Kind: sig (impl)<br/>GC: Ted Young<br/>TC: Carlos Alberto Cortez (escalating)"]
  cpp["C++: SDK<br/>Kind: sig (impl)<br/>GC: Severin Neumann<br/>TC: Reiley Yang (escalating)"]
  client_instrumentation["Client Instrumentation<br/>Kind: sig (spec)<br/>GC: Ted Young<br/>TC: Carlos Alberto Cortez (escalating)"]
  community_demo["Community Demo Application<br/>Kind: sig (impl)<br/>GC: Austin Parker<br/>TC: Reiley Yang (escalating)"]
  contributor_experience["Contributor Experience<br/>Kind: sig (cross)<br/>GC: Marylia Gutierrez<br/>TC: Liudmila Molkova (escalating)"]
  developer_experience["Developer Experience<br/>Kind: sig (cross)<br/>GC: Austin Parker<br/>TC: Liudmila Molkova (escalating)"]
  erlang_elixir["Erlang/Elixir: SDK<br/>Kind: sig (impl)<br/>GC: Austin Parker<br/>TC: Josh Suereth (escalating)"]
  faas["Functions as a Service (FAAS)<br/>Kind: sig (spec)<br/>GC: Austin Parker<br/>TC: unsponsored"]
  go_auto_instr["GoLang: Automatic Instrumentation<br/>Kind: sig (impl)<br/>GC: Juraci Paixão Kröhling<br/>TC: David Ashpole (escalating)"]
  go_compile_instr["GoLang: Compile-Time Instrumentation<br/>Kind: sig (impl)<br/>GC: Juraci Paixão Kröhling<br/>TC: David Ashpole (escalating)"]
  go["GoLang: SDK<br/>Kind: sig (impl)<br/>GC: Marylia Gutierrez<br/>TC: David Ashpole (leading)"]
  injector["Injector<br/>Kind: sig (impl)<br/>GC: Morgan McLean<br/>TC: Jack Berg (guiding)"]
  java_sdk_instrumentation["Java: SDK + Instrumentation<br/>Kind: sig (impl)<br/>GC: Trask Stalnaker<br/>TC: Jack Berg (leading)"]
  javascript_sdk["JavaScript: SDK<br/>Kind: sig (impl)<br/>GC: Marylia Gutierrez<br/>TC: Carlos Alberto Cortez (escalating)"]
  k8s_helm_charts["Kubernetes Helm Charts<br/>Kind: sig (impl)<br/>GC: Pablo Baeyens<br/>TC: unsponsored"]
  k8s_operator["Kubernetes Operator<br/>Kind: sig (impl)<br/>GC: Juraci Paixão Kröhling<br/>TC: David Ashpole (escalating)"]
  network["Network<br/>Kind: sig (impl)<br/>GC: Ted Young<br/>TC: David Ashpole (escalating)"]
  opamp["OpAMP<br/>Kind: sig (spec)<br/>GC: Ted Young<br/>TC: Tigran Najaryan (leading)"]
  mainframes["OpenTelemetry on Mainframes<br/>Kind: sig (spec)<br/>GC: Morgan McLean<br/>TC: unsponsored"]
  php_sdk["PHP: SDK<br/>Kind: sig (impl)<br/>GC: Severin Neumann<br/>TC: Jack Berg (escalating)"]
  profiling["Profiling<br/>Kind: sig (spec)<br/>GC: Morgan McLean<br/>TC: Josh Suereth (guiding), Tigran Najaryan (guiding)"]
  project_infra["Project Infrastructure<br/>Kind: sig (cross)<br/>GC: Austin Parker<br/>TC: Armin Ruech (escalating)"]
  prometheus_interop["Prometheus Interoperability<br/>Kind: sig (spec)<br/>GC: Pablo Baeyens<br/>TC: David Ashpole (leading)"]
  python_sdk["Python: SDK<br/>Kind: sig (impl)<br/>GC: Marylia Gutierrez<br/>TC: Reiley Yang (escalating)"]
  ruby_sdk["Ruby: SDK<br/>Kind: sig (impl)<br/>GC: Ted Young<br/>TC: Armin Ruech (escalating)"]
  rust_sdk["Rust: SDK<br/>Kind: sig (impl)<br/>GC: Ted Young<br/>TC: Reiley Yang (escalating)"]
  security["Security<br/>Kind: sig (cross)<br/>GC: Trask Stalnaker<br/>TC: Reiley Yang (leading)"]
  swift_sdk["Swift: SDK<br/>Kind: sig (impl)<br/>GC: Alolita Sharma<br/>TC: Reiley Yang (escalating)"]
  ebpf_instrumentation["eBPF Instrumentation<br/>Kind: sig (impl)<br/>GC: Severin Neumann<br/>TC: David Ashpole (escalating)"]

  class communications tc_escalating
  class localization_bn tc_none
  class localization_zh_cn tc_tbd
  class localization_fr tc_none
  class localization_ja tc_none
  class getting_started_docs tc_tbd
  class ecosystem_explorer tc_escalating
  class localization_pt_br tc_none
  class localization_ro tc_none
  class localization_es tc_none
  class localization_uk tc_none
  class spec_general tc_none
  class semconv_general tc_leading
  class semconv_cicd tc_escalating
  class cicd_phase_2 tc_tbd
  class gen_ai tc_leading
  class semconv_k8s tc_leading
  class semconv_rpc tc_guiding
  class semconv_security tc_escalating
  class semconv_service_deployment tc_escalating
  class semconv_system_metrics tc_escalating
  class semconv_tooling tc_leading
  class spec_entities tc_leading
  class spec_logs tc_guiding
  class sampling tc_guiding
  class collector tc_guiding
  class collector_v1 tc_none
  class agentic_workflow tc_none
  class end_user tc_escalating
  class otel_blueprints tc_escalating
  class dotnet_auto_instr tc_escalating
  class dotnet tc_escalating
  class android tc_escalating
  class arrow tc_leading
  class zig_sig_bootstrap tc_tbd
  class browser tc_escalating
  class cpp tc_escalating
  class client_instrumentation tc_escalating
  class community_demo tc_escalating
  class contributor_experience tc_escalating
  class developer_experience tc_escalating
  class erlang_elixir tc_escalating
  class faas tc_none
  class go_auto_instr tc_escalating
  class go_compile_instr tc_escalating
  class go tc_leading
  class injector tc_guiding
  class java_sdk_instrumentation tc_leading
  class javascript_sdk tc_escalating
  class k8s_helm_charts tc_none
  class k8s_operator tc_escalating
  class network tc_escalating
  class opamp tc_leading
  class mainframes tc_none
  class php_sdk tc_escalating
  class profiling tc_guiding
  class project_infra tc_escalating
  class prometheus_interop tc_leading
  class python_sdk tc_escalating
  class ruby_sdk tc_escalating
  class rust_sdk tc_escalating
  class security tc_leading
  class swift_sdk tc_escalating
  class ebpf_instrumentation tc_escalating

```

## TC Sponsorship Summary

| Member | Leading | Guiding | Escalating | Tbd | Total |
|--------|---------|---------|---------|---------|---------|
| [David Ashpole](https://github.com/dashpole) | 3 |  | 5 |  | 8 |
| [Jack Berg](https://github.com/jack-berg) | 1 | 1 | 5 | 1 | 8 |
| [Carlos Alberto Cortez](https://github.com/carlosalberto) |  |  | 4 | 1 | 5 |
| [Bogdan Drutu](https://github.com/bogdandrutu) |  | 1 |  |  | 1 |
| [Joshua MacDonald](https://github.com/jmacd) | 1 | 2 |  | 1 | 4 |
| [Liudmila Molkova](https://github.com/lmolkova) | 3 | 2 | 2 |  | 7 |
| [Tigran Najaryan](https://github.com/tigrannajaryan) | 2 | 1 |  |  | 3 |
| [Armin Ruech](https://github.com/arminru) | 1 |  | 2 |  | 3 |
| [Josh Suereth](https://github.com/jsuereth) | 3 | 1 | 4 |  | 8 |
| [Reiley Yang](https://github.com/reyang) | 1 |  | 8 | 1 | 10 |
| **Total** | 15 | 8 | 30 | 4 | 57 |

13 workstream(s) have no TC sponsor assigned.
