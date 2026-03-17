#!/usr/bin/env python3
"""
One-time migration script: converts sigs.yml to workstreams.yml format.

Writes the result to workstreams.yml, preserving any existing non-sig
workstreams (working-group, enhancement) from the current file.

Usage:
    python scripts/migrate-sigs.py [--dry-run]
"""

import re
import sys
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent

# ---------------------------------------------------------------------------
# Slug overrides: sigs.yml name -> workstream id
# ---------------------------------------------------------------------------
SLUG_OVERRIDES = {
    "Specification: General + OTel Maintainers Sync":             "spec-general",
    "Specification: Sampling":                                     "sampling",
    "Specification: Logs":                                         "spec-logs",
    "Specification: Entities":                                     "spec-entities",
    "Semantic Conventions: General":                               "semconv-general",
    "Semantic Conventions: System Metrics":                        "semconv-system-metrics",
    "Semantic Conventions: K8s":                                   "semconv-k8s",
    "Semantic Conventions and Instrumentation: GenAI":             "gen-ai",
    "Semantic Conventions: CI/CD":                                 "semconv-cicd",
    "Semantic Conventions: RPC":                                   "semconv-rpc",
    "Semantic Conventions: Security":                              "semconv-security",
    "Semantic Conventions: Service and Deployment":                "semconv-service-deployment",
    "Semantic Conventions: Tooling":                               "semconv-tooling",
    "Functions as a Service (FAAS)":                               "faas",
    "OpenTelemetry on Mainframes":                                 "mainframes",
    "Client Instrumentation":                                      "client-instrumentation",
    "Prometheus Interoperability":                                 "prometheus-interop",
    "GoLang: SDK":                                                 "go",
    "GoLang: Automatic Instrumentation":                           "go-auto-instr",
    "GoLang: Compile-Time Instrumentation":                        "go-compile-instr",
    "C++: SDK":                                                    "cpp",
    ".NET: Automatic Instrumentation":                             "dotnet-auto-instr",
    ".NET: SDK":                                                   "dotnet",
    "Erlang/Elixir: SDK":                                          "erlang-elixir",
    "Android: SDK + Automatic Instrumentation":                    "android",
    "Kubernetes Operator":                                         "k8s-operator",
    "Kubernetes Helm Charts":                                      "k8s-helm-charts",
    "Community Demo Application":                                  "community-demo",
    "eBPF Instrumentation":                                        "ebpf-instrumentation",
    "Communications (Website, [Documentation](https://opentelemetry.io/docs/), etc.)": "communications",
    "End-User SIG":                                                "end-user",
    "Project Infrastructure":                                      "project-infra",
    "Contributor Experience":                                      "contributor-experience",
    "Developer Experience":                                        "developer-experience",
    "Bengali (bn)":                                                "localization-bn",
    "Chinese (zh-CN)":                                             "localization-zh-cn",
    "French (fr-FR)":                                              "localization-fr",
    "Japanese (ja-JA)":                                            "localization-ja",
    "Portuguese (pt-BR)":                                          "localization-pt-br",
    "Spanish (es-ES)":                                             "localization-es",
    "Ukrainian (uk-UA)":                                           "localization-uk",
    "Romanian (ro-RO)":                                            "localization-ro",
}

# ---------------------------------------------------------------------------
# Parent relationships: workstream id -> parent id
# ---------------------------------------------------------------------------
GROUP_CATEGORY = {
    "Specification SIGs":                          None,           # omit — specification is the default
    "Implementation SIGs":                         "implementation",
    "Cross-Cutting SIGs":                          "cross-cutting",
    "Localization Teams (part of SIG Communications)": "cross-cutting",
}

PARENT_MAP = {
    "sampling":                   "spec-general",
    "spec-logs":                  "spec-general",
    "spec-entities":              "spec-general",
    "semconv-general":            "spec-general",
    "semconv-system-metrics":     "semconv-general",
    "semconv-k8s":                "semconv-general",
    "gen-ai":                     "semconv-general",
    "semconv-cicd":               "semconv-general",
    "semconv-rpc":                "semconv-general",
    "semconv-security":           "semconv-general",
    "semconv-service-deployment": "semconv-general",
    "semconv-tooling":            "semconv-general",
    "localization-bn":            "communications",
    "localization-zh-cn":         "communications",
    "localization-fr":            "communications",
    "localization-ja":            "communications",
    "localization-pt-br":         "communications",
    "localization-es":            "communications",
    "localization-uk":            "communications",
    "localization-ro":            "communications",
}


def slugify(name: str) -> str:
    slug = name.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return slug.strip("-")


def extract_repo_slug(url: str) -> str | None:
    m = re.search(r"github\.com/(.+)", url)
    return m.group(1).rstrip("/") if m else None


def convert_sig(sig: dict, tc_members: set[str], group_name: str = "") -> dict:
    name = sig["name"]
    wid  = SLUG_OVERRIDES.get(name) or slugify(name)

    ws: dict = {"id": wid, "kind": "sig"}
    if category := GROUP_CATEGORY.get(group_name):
        ws["sigCategory"] = category
    ws["name"] = name

    parent = PARENT_MAP.get(wid)
    if parent:
        ws["parent"] = parent

    # --- people ---
    people = []

    gc_liaisons = sig.get("gcLiaison") or []
    people.append({"gcLiaison": gc_liaisons[0]["github"] if gc_liaisons else "tbd"})

    sponsors     = sig.get("sponsors") or []
    tc_sponsors  = [s for s in sponsors if s["github"] in tc_members]
    if tc_sponsors:
        for s in tc_sponsors:
            people.append({"tcSponsor": {"username": s["github"], "level": "tbd"}})
    else:
        people.append({"tcSponsor": {"username": "tbd", "level": "tbd"}})

    ws["people"] = people

    # --- resources ---
    resources = []

    schedule = sig.get("meeting", "")
    if schedule:
        meeting: dict = {"schedule": schedule}
        if invites := sig.get("invites"):
            meeting["calendarInviteGroup"] = invites
        notes = sig.get("notes") or {}
        if notes.get("type") == "gDoc" and notes.get("value"):
            meeting["gDocNotes"] = notes["value"]
        resources.append({"meeting": meeting})

    for chat in sig.get("chat") or []:
        if chat["type"] == "slack":
            resources.append({"slack": {"name": chat["name"], "id": chat["id"]}})
        elif "GitHub Discussions" in chat.get("name", ""):
            resources.append({"githubDiscussion": chat["link"]})

    for repo_url in sig.get("repositories") or []:
        slug = extract_repo_slug(repo_url)
        if slug:
            resources.append({"repository": slug})

    for project_id in sig.get("roadmapProjectIDs") or []:
        resources.append({"roadmapProject": project_id})

    if resources:
        ws["resources"] = resources

    return ws


def main() -> None:
    dry_run = "--dry-run" in sys.argv

    sigs_data       = yaml.safe_load((REPO_ROOT / "sigs.yml").read_text())
    people_data     = yaml.safe_load((REPO_ROOT / "people.yml").read_text())
    workstreams_path = REPO_ROOT / "workstreams.yml"
    workstreams_raw  = yaml.safe_load(workstreams_path.read_text()) if workstreams_path.exists() else []

    tc_members = {
        handle
        for handle, info in people_data.items()
        if "tc-member" in info.get("membership", [])
    }

    # Convert all SIGs from sigs.yml
    sigs_by_id: dict[str, dict] = {}
    for group in sigs_data:
        for sig in group.get("sigs", []):
            ws = convert_sig(sig, tc_members, group["name"])
            sigs_by_id[ws["id"]] = ws

    # Preserve existing non-sig workstreams (working-group, enhancement).
    # If a preserved entry has the same id as a generated SIG, the preserved
    # entry wins (it may carry richer data, e.g. leads and split meetings).
    preserved = [w for w in workstreams_raw if w.get("kind") != "sig"]
    preserved_ids = {w["id"] for w in preserved}
    sigs = [w for w in sigs_by_id.values() if w["id"] not in preserved_ids]

    output = sigs + preserved

    result = yaml.dump(
        output,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=120,
    )

    if dry_run:
        print(result)
    else:
        (REPO_ROOT / "workstreams.yml").write_text(result)
        print(f"Wrote {len(output)} workstreams ({len(sigs_by_id)} SIGs + {len(preserved)} preserved).")


if __name__ == "__main__":
    main()
