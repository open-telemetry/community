#!/usr/bin/env python3
"""
Bare-metal benchmark runner usage report.

Emits a single Markdown table grouped by (repository, workflow) showing
on-runner time and queue-wait stats for jobs that target the
`oracle-bare-metal-*` runner labels.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from typing import Iterable

BAREMETAL_LABEL_PREFIX = "oracle-bare-metal"

# (repo, workflow file path) — discovered via:
#   gh search code 'oracle-bare-metal path:.github/workflows' --owner open-telemetry
WORKFLOWS = [
    ("open-telemetry/opentelemetry-go", "benchmark.yml"),
    ("open-telemetry/opentelemetry-java", "benchmark-tags.yml"),
    ("open-telemetry/opentelemetry-java", "benchmark.yml"),
    ("open-telemetry/opentelemetry-python", "benchmarks.yml"),
    ("open-telemetry/opentelemetry-rust", "benchmark.yml"),
    ("open-telemetry/opentelemetry-js", "benchmark.yml"),
    ("open-telemetry/opentelemetry-collector-contrib", "load-tests.yml"),
    ("open-telemetry/otel-arrow", "pipeline-perf-on-label.yaml"),
    ("open-telemetry/otel-arrow", "pipeline-perf-test-manual-pr.yaml"),
    ("open-telemetry/otel-arrow", "pipeline-perf-test-continuous.yml"),
    ("open-telemetry/otel-arrow", "pipeline-perf-test-nightly.yml"),
]


def gh_paginated(path: str, list_key: str) -> Iterable[dict]:
    proc = subprocess.run(
        ["gh", "api", "--paginate",
         "-H", "Accept: application/vnd.github+json",
         "--jq", f".{list_key}[]", path],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh api {path}: {proc.stderr}")
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line:
            yield json.loads(line)


def parse_iso(ts: str) -> datetime:
    return datetime.fromisoformat(ts.replace("Z", "+00:00"))


def fmt_dur(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h:
        return f"{h}h {m}m"
    if m:
        return f"{m}m {s}s"
    return f"{s}s"


def collect_jobs(since: datetime) -> list[dict]:
    """Return per-job records for every bare-metal job since `since`."""
    since_q = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    records: list[dict] = []
    for repo, wf_file in WORKFLOWS:
        print(f"  - {repo} :: {wf_file}", file=sys.stderr)
        runs_path = (
            f"/repos/{repo}/actions/workflows/{wf_file}/runs"
            f"?per_page=100&status=completed&created=%3E%3D{since_q}"
        )
        try:
            runs = list(gh_paginated(runs_path, "workflow_runs"))
        except RuntimeError as e:
            print(f"    ! {e}", file=sys.stderr)
            continue
        for run in runs:
            run_id = run["id"]
            wf_name = run.get("name") or wf_file
            run_started_at = run.get("run_started_at") or run.get("created_at")
            try:
                jobs = list(gh_paginated(
                    f"/repos/{repo}/actions/runs/{run_id}/jobs?per_page=100",
                    "jobs",
                ))
            except RuntimeError as e:
                print(f"    ! run {run_id}: {e}", file=sys.stderr)
                continue
            for job in jobs:
                labels = job.get("labels") or []
                if not any(
                    isinstance(lbl, str) and lbl.startswith(BAREMETAL_LABEL_PREFIX)
                    for lbl in labels
                ):
                    continue
                if job.get("conclusion") in ("skipped", "neutral"):
                    continue
                if not (job.get("runner_name") and job.get("runner_group_id")):
                    continue
                started, completed = job.get("started_at"), job.get("completed_at")
                if not started or not completed:
                    continue
                try:
                    dur = (parse_iso(completed) - parse_iso(started)).total_seconds()
                except ValueError:
                    continue
                if dur <= 0:
                    continue
                qwait = 0.0
                if run_started_at:
                    try:
                        qwait = max(
                            0.0,
                            (parse_iso(started) - parse_iso(run_started_at))
                            .total_seconds(),
                        )
                    except ValueError:
                        qwait = 0.0
                records.append({
                    "repo": repo,
                    "wf_file": wf_file,
                    "wf_name": wf_name,
                    "run_id": run_id,
                    "started": parse_iso(started),
                    "duration": dur,
                    "qwait": qwait,
                })
    return records


def render_table(records: list[dict], since: datetime) -> str:
    agg: dict[tuple[str, str, str], dict] = defaultdict(
        lambda: {"runs": set(), "total": 0.0,
                 "qwait_max": 0.0,
                 "run_totals": defaultdict(float)}
    )
    for r in records:
        if r["started"] < since:
            continue
        key = (r["repo"], r["wf_file"], r["wf_name"])
        a = agg[key]
        a["runs"].add(r["run_id"])
        a["total"] += r["duration"]
        a["run_totals"][r["run_id"]] += r["duration"]
        if r["qwait"] > a["qwait_max"]:
            a["qwait_max"] = r["qwait"]

    rows = sorted(agg.items(), key=lambda kv: -kv[1]["total"])
    out: list[str] = []
    out.append(
        "| Repository | Workflow | Runs | Total | Avg/run | "
        "Max run | Max queue wait |"
    )
    out.append("|---|---|---:|---:|---:|---:|---:|")
    for (repo, wf_file, wf_name), v in rows:
        n_runs = len(v["runs"])
        avg = v["total"] / n_runs if n_runs else 0
        max_run = max(v["run_totals"].values(), default=0.0)
        repo_short = repo.split("/", 1)[1] if "/" in repo else repo
        wf_link = (
            f"https://github.com/{repo}/blob/main/.github/workflows/{wf_file}"
        )
        out.append(
            f"| {repo_short} | [`{wf_file}`]({wf_link}) | "
            f"{n_runs} | {fmt_dur(v['total'])} | {fmt_dur(avg)} | "
            f"{fmt_dur(max_run)} | {fmt_dur(v['qwait_max'])} |"
        )
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--windows", type=int, nargs="+", default=[7, 30],
        help="One or more day windows to emit tables for.",
    )
    p.add_argument("--output", default="baremetal-runner-report.md")
    args = p.parse_args()

    now = datetime.now(timezone.utc)
    max_days = max(args.windows)
    since_max = now - timedelta(days=max_days)

    print(f"Fetching jobs since {since_max.isoformat()} "
          f"(max window {max_days} days)", file=sys.stderr)
    records = collect_jobs(since_max)
    print(f"Collected {len(records)} bare-metal job records", file=sys.stderr)

    sections: list[str] = []
    for days in sorted(args.windows):
        since = now - timedelta(days=days)
        sections.append(f"## Last {days} days")
        sections.append("")
        sections.append(render_table(records, since))
        sections.append("")

    text = "\n".join(sections).rstrip() + "\n"
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
