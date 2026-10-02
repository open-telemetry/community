#!/usr/bin/env python3
import subprocess
import sys
from collections import defaultdict

# in the Makefile we use an unmodified python container to run this script, so we need to install pyyaml if it's not already installed
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
    sys.argv = sys.argv[1:]

import yaml

# Do not save the file but verify that it is different from the original one.
run_in_check_mode = (len(sys.argv) > 1) and (sys.argv[1] == "--check")

WORKSTREAMS_FILE = "workstreams.yml"
METADATA_FILE = "people.yml"
LEDGER_FILE = "sig-sponsorship-ledger.md"

LEVELS = ["leading", "guiding", "escalating", "tbd"]
LEVEL_LABEL = {
    "leading": "Leading",
    "guiding": "Guiding",
    "escalating": "Escalating",
    "tbd": "No level set",
}

CATEGORY_LABEL = {
    "specification": "Specification",
    "implementation": "Implementation",
    "cross-cutting": "Cross-cutting",
}
CATEGORY_ORDER = ["specification", "implementation", "cross-cutting"]

with open(WORKSTREAMS_FILE, encoding="utf-8") as f:
    workstreams = yaml.safe_load(f)

try:
    with open(METADATA_FILE, encoding="utf-8") as f:
        _metadata = yaml.safe_load(f)
    _people = _metadata.get("people", {})
except FileNotFoundError:
    print(
        f"Warning: {METADATA_FILE} not found — display names will fall back to GitHub handles.",
        file=sys.stderr,
    )
    _people = {}


def person_link(username):
    if not username or username == "tbd":
        return "tbd"
    name = _people.get(username, {}).get("name", username)
    return f"[{name}](https://github.com/{username})"


by_id = {w["id"]: w for w in workstreams}


def parent_name(ws):
    parent = ws.get("parent", "none")
    if not parent or parent == "none":
        return None
    parent_ws = by_id.get(parent)
    return parent_ws["name"] if parent_ws else parent


rows_by_category = defaultdict(list)
gc_load = defaultdict(list)
tc_load_by_level = defaultdict(lambda: defaultdict(list))

for ws in workstreams:
    category = ws.get("sigCategory", "other")
    collective = ws.get("tcSponsorship") == "collective"

    gc_liaisons = [e["gcLiaison"] for e in ws.get("people", []) if "gcLiaison" in e]
    tc_sponsors = [e["tcSponsor"] for e in ws.get("people", []) if "tcSponsor" in e]

    for gc in gc_liaisons:
        if gc and gc != "tbd":
            gc_load[gc].append(ws["name"])

    if not collective:
        seen = set()
        for sponsor in tc_sponsors:
            username = sponsor.get("username")
            if not username or username == "tbd" or username in seen:
                continue
            seen.add(username)
            level = sponsor.get("level") or "tbd"
            if level not in LEVELS:
                level = "tbd"
            tc_load_by_level[username][level].append(ws["name"])

    gc_cell = ", ".join(person_link(g) for g in gc_liaisons) if gc_liaisons else "tbd"
    if collective:
        tc_cell = "[Technical Committee](./community-members.md#technical-committee)"
    elif tc_sponsors:
        parts = []
        for sponsor in tc_sponsors:
            link = person_link(sponsor.get("username"))
            level = sponsor.get("level")
            if level and level != "tbd":
                link += f" ({level})"
            parts.append(link)
        tc_cell = ", ".join(parts)
    else:
        tc_cell = "tbd"

    name_cell = ws["name"]
    parent = parent_name(ws)
    if parent:
        name_cell += f"<br><sub>under {parent}</sub>"

    rows_by_category[category].append((name_cell, gc_cell, tc_cell))


def rank_gc(load):
    items = list(load.items())
    items.sort(key=lambda kv: (-len(kv[1]), kv[0]))
    return items


def rank_tc(load_by_level):
    items = []
    for username, by_level in load_by_level.items():
        total = sum(len(v) for v in by_level.values())
        all_sigs = sorted({name for sigs in by_level.values() for name in sigs})
        items.append((username, by_level, total, all_sigs))
    items.sort(key=lambda row: (-row[2], row[0]))
    return items


gc_ranked = rank_gc(gc_load)
tc_ranked = rank_tc(tc_load_by_level)

missing_gc = sum(
    1
    for ws in workstreams
    if not any(e.get("gcLiaison") not in (None, "tbd") for e in ws.get("people", []) if "gcLiaison" in e)
)
missing_tc = 0
for ws in workstreams:
    if ws.get("tcSponsorship") == "collective":
        continue
    sponsors = [e["tcSponsor"] for e in ws.get("people", []) if "tcSponsor" in e]
    if not sponsors or all(s.get("username") == "tbd" for s in sponsors):
        missing_tc += 1


def plural(n, noun="SIG"):
    return f"{n} {noun}" if n == 1 else f"{n} {noun}s"


lines = []
lines.append("# SIG Sponsorship Ledger")
lines.append("")
lines.append("<!-- This file is auto-generated. To make changes, see CONTRIBUTING.md#updating-sig-information. -->")
lines.append("")
lines.append(
    "Every OpenTelemetry SIG with its Governance Committee (GC) liaison and Technical "
    "Committee (TC) sponsor(s), followed by how many SIGs each GC and TC member is "
    "currently responsible for. For full per-SIG details (meetings, Slack, repos), see [sigs.md](./sigs.md)."
)
lines.append("")
lines.append(
    f"**{plural(len(workstreams))}** · **{plural(len(gc_ranked), 'GC member')}** with at least one liaison "
    f"assignment · **{plural(len(tc_ranked), 'TC member')}** with at least one sponsor assignment · "
    f"**{plural(missing_gc)}** missing a GC liaison · **{plural(missing_tc)}** missing a TC sponsor"
)
lines.append("")

lines.append("## GC liaison load")
lines.append("")
lines.append("| GC member | SIGs | List |")
lines.append("| --- | --- | --- |")
for who, sigs in gc_ranked:
    lines.append(f"| {person_link(who)} | {len(sigs)} | {', '.join(sigs)} |")
lines.append("")

lines.append("## TC sponsor load")
lines.append("")
header = ["TC member"] + [LEVEL_LABEL[lvl] for lvl in LEVELS] + ["Total"]
lines.append("| " + " | ".join(header) + " |")
lines.append("| " + " | ".join(["---"] * len(header)) + " |")
for username, by_level, total, _all_sigs in tc_ranked:
    level_counts = [str(len(by_level.get(lvl, []))) for lvl in LEVELS]
    lines.append(f"| {person_link(username)} | " + " | ".join(level_counts) + f" | {total} |")
lines.append("")
lines.append("<details>")
lines.append("<summary>SIGs sponsored, per TC member</summary>")
lines.append("")
for username, by_level, total, all_sigs in tc_ranked:
    lines.append(f"- **{person_link(username)}** ({plural(total)}): {', '.join(all_sigs)}")
lines.append("")
lines.append("</details>")
lines.append("")
lines.append(
    '_Sponsorship of "Specification: General + OTel Maintainers Sync" is collective '
    "across the whole Technical Committee and is not counted toward individual totals above._"
)
lines.append("")

lines.append("## SIG directory")
lines.append("")
for category in CATEGORY_ORDER:
    rows = rows_by_category.get(category, [])
    if not rows:
        continue
    lines.append(f"### {CATEGORY_LABEL[category]} ({len(rows)})")
    lines.append("")
    lines.append("| SIG | GC liaison | TC sponsor(s) |")
    lines.append("| --- | --- | --- |")
    for name_cell, gc_cell, tc_cell in rows:
        lines.append(f"| {name_cell} | {gc_cell} | {tc_cell} |")
    lines.append("")

ledger_result = "\n".join(lines).rstrip() + "\n"


def file_matches(path, expected):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read() == expected
    except FileNotFoundError:
        return False


if run_in_check_mode:
    if file_matches(LEDGER_FILE, ledger_result):
        sys.exit(0)
    else:
        print(f"{LEDGER_FILE} is out of date. Run 'make generate' to update it.", file=sys.stderr)
        sys.exit(1)
else:
    with open(LEDGER_FILE, "w", encoding="utf-8") as f:
        f.write(ledger_result)
    print(f"{LEDGER_FILE} has been updated.")
