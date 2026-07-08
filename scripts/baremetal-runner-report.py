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
import os
import subprocess
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from typing import Iterable

BAREMETAL_LABEL_PREFIX = "oracle-bare-metal"


def gh_paginated(path: str, list_key: str) -> Iterable[dict]:
    proc = subprocess.run(
        ["gh", "api", "--paginate",
         "-H", "Accept: application/vnd.github+json",
         "--jq", f".{list_key}[]", path],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=120,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh api {path}: {proc.stderr}")
    for line in proc.stdout.splitlines():
        line = line.strip()
        if line:
            yield json.loads(line)


def discover_workflows(owner: str) -> list[tuple[str, str]]:
    proc = subprocess.run(
        [
            "gh", "search", "code",
            f"{BAREMETAL_LABEL_PREFIX} path:.github/workflows",
            "--owner", owner,
            "--json", "repository,path",
            "--limit", "1000",
        ],
        capture_output=True, text=True, encoding="utf-8", errors="replace",
        timeout=120,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gh search code: {proc.stderr}")
    workflows = set()
    for result in json.loads(proc.stdout or "[]"):
        repo = result.get("repository", {}).get("nameWithOwner")
        path = result.get("path")
        if not repo or not path:
            continue
        dirname, filename = os.path.split(path)
        if dirname != ".github/workflows" or not filename.endswith((".yml", ".yaml")):
            continue
        workflows.add((repo, filename))
    return sorted(workflows)


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


def workflow_url(repo: str, wf_file: str) -> str:
    return f"https://github.com/{repo}/blob/main/.github/workflows/{wf_file}"


def collect_run_jobs(repo: str, wf_file: str, run: dict) -> tuple[list[dict], str | None]:
    records: list[dict] = []
    run_id = run["id"]
    wf_name = run.get("name") or wf_file
    run_started_at = run.get("run_started_at") or run.get("created_at")
    try:
        jobs = list(gh_paginated(
            f"/repos/{repo}/actions/runs/{run_id}/jobs?per_page=100",
            "jobs",
        ))
    except Exception as e:
        return records, f"{repo} {wf_file} run {run_id}: {str(e).strip()}"
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
            started_dt = parse_iso(started)
            dur = (parse_iso(completed) - started_dt).total_seconds()
        except ValueError:
            continue
        if dur <= 0:
            continue
        qwait = 0.0
        if run_started_at:
            try:
                qwait = max(
                    0.0,
                    (started_dt - parse_iso(run_started_at)).total_seconds(),
                )
            except ValueError:
                qwait = 0.0
        records.append({
            "repo": repo,
            "wf_file": wf_file,
            "wf_name": wf_name,
            "run_id": run_id,
            "started": started_dt,
            "duration": dur,
            "qwait": qwait,
        })
    return records, None


def collect_jobs(
    workflows: list[tuple[str, str]], since: datetime, jobs_concurrency: int,
) -> tuple[list[dict], list[str]]:
    """Return per-job records for every bare-metal job since `since`."""
    since_q = since.strftime("%Y-%m-%dT%H:%M:%SZ")
    records: list[dict] = []
    errors: list[str] = []
    for repo, wf_file in workflows:
        print(f"  - {repo} :: {wf_file}", file=sys.stderr)
        runs_path = (
            f"/repos/{repo}/actions/workflows/{wf_file}/runs"
            f"?per_page=100&status=completed&created=%3E%3D{since_q}"
        )
        try:
            runs = list(gh_paginated(runs_path, "workflow_runs"))
        except Exception as e:
            msg = str(e).strip()
            errors.append(f"{repo} {wf_file}: {msg}")
            print(f"    ! {msg}", file=sys.stderr)
            continue
        print(f"    {len(runs)} workflow runs", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=jobs_concurrency) as executor:
            futures = [
                executor.submit(collect_run_jobs, repo, wf_file, run)
                for run in runs
            ]
            for index, future in enumerate(as_completed(futures), 1):
                run_records, error = future.result()
                records.extend(run_records)
                if error:
                    errors.append(error)
                    print(f"    ! {error}", file=sys.stderr)
                if index % 50 == 0 or index == len(futures):
                    print(f"    processed {index}/{len(futures)} runs", file=sys.stderr)
    return records, errors


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
        wf_link = workflow_url(repo, wf_file)
        out.append(
            f"| {repo_short} | [`{wf_file}`]({wf_link}) | "
            f"{n_runs} | {fmt_dur(v['total'])} | {fmt_dur(avg)} | "
            f"{fmt_dur(max_run)} | {fmt_dur(v['qwait_max'])} |"
        )
    return "\n".join(out)


def render_workflows(workflows: list[tuple[str, str]]) -> str:
    lines = ["## Discovered workflow files", ""]
    for repo, wf_file in workflows:
        repo_short = repo.split("/", 1)[1] if "/" in repo else repo
        lines.append(f"- {repo_short}: [`{wf_file}`]({workflow_url(repo, wf_file)})")
    return "\n".join(lines)


def render_collection_notes(errors: list[str]) -> str:
    if not errors:
        return "## Collection notes\n\nNo API collection errors."
    lines = ["## Collection notes", "", "The report skipped these API calls:"]
    for error in errors:
        lines.append(f"- {error}")
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument(
        "--windows", type=int, nargs="+", default=[7, 30],
        help="One or more day windows to emit tables for.",
    )
    p.add_argument(
        "--jobs-concurrency", type=int, default=12,
        help="Number of concurrent run job API calls.",
    )
    p.add_argument("--owner", default="open-telemetry")
    p.add_argument("--output", default="baremetal-runner-report.md")
    args = p.parse_args()
    if args.jobs_concurrency < 1:
        p.error("--jobs-concurrency must be at least 1")

    now = datetime.now(timezone.utc)
    max_days = max(args.windows)
    since_max = now - timedelta(days=max_days)

    workflows = discover_workflows(args.owner)
    print(f"Discovered {len(workflows)} bare-metal workflow files", file=sys.stderr)
    print(f"Fetching jobs since {since_max.isoformat()} "
          f"(max window {max_days} days)", file=sys.stderr)
    records, errors = collect_jobs(workflows, since_max, args.jobs_concurrency)
    print(f"Collected {len(records)} bare-metal job records", file=sys.stderr)

    sections: list[str] = [
        "# Bare-metal runner report",
        "",
        f"Generated: {now.isoformat()}",
        "",
        render_workflows(workflows),
        "",
        render_collection_notes(errors),
        "",
    ]
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
