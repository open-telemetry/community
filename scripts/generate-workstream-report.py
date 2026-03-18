#!/usr/bin/env python3
"""Generate workstreams.md: Mermaid SIG hierarchy chart with legend.

Usage:
    python scripts/generate-workstream-report.py [--install]
"""

import re
import subprocess
import sys
from collections import defaultdict

# Support --install like other scripts in this repo
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
    sys.argv = sys.argv[1:]

import yaml


WORKSTREAMS_FILE = "workstreams.yml"
PEOPLE_FILE = "people.yml"
OUTPUT_FILE = "workstreams.md"

with open(WORKSTREAMS_FILE) as f:
    all_items = yaml.safe_load(f)
with open(PEOPLE_FILE) as f:
    _people_data = yaml.safe_load(f)

people_info = _people_data.get("people", {})   # login -> {name, company}
teams_data  = _people_data.get("teams", {})    # team-slug -> [logins]


def node_id(ws_id):
    """Convert workstream ID to Mermaid-safe identifier (alphanumeric + underscore)."""
    return ws_id.replace("-", "_")


def clean_label(name):
    """Strip markdown links and escape double-quotes for Mermaid node labels."""
    # [text](url) -> text
    name = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", name)
    return name.replace('"', "'")


# children: parent_id -> [child workstream, ...]
children = defaultdict(list)
for ws in all_items:
    parent = ws.get("parent", "none")
    if parent != "none":
        children[parent].append(ws)

# ws_tc_levels: ws_id -> {level -> count}  (only entries with a real username)
ws_tc_levels = defaultdict(lambda: defaultdict(int))
for ws in all_items:
    for entry in ws.get("people", []):
        if "tcSponsor" in entry:
            u = entry["tcSponsor"].get("username")
            level = entry["tcSponsor"].get("level") or "tbd"
            if u and u != "tbd":
                ws_tc_levels[ws["id"]][level] += 1

BUDGET_LEVELS = ["leading", "guiding", "escalating"]

_subtree_memo: dict = {}


def subtree_tc_levels(ws_id):
    """Recursively sum TC level counts for ws_id and all its descendants."""
    if ws_id in _subtree_memo:
        return _subtree_memo[ws_id]
    result: dict = dict(ws_tc_levels[ws_id])
    for child in children[ws_id]:
        for lvl, count in subtree_tc_levels(child["id"]).items():
            result[lvl] = result.get(lvl, 0) + count
    _subtree_memo[ws_id] = result
    return result


level_totals = {
    lvl: sum(ws_tc_levels[ws["id"]].get(lvl, 0) for ws in all_items)
    for lvl in BUDGET_LEVELS
}


# ─── Section 1: Mermaid chart ─────────────────────────────────────────────────

# Highest TC level wins for color; "none" = no assigned sponsors
TC_LEVEL_PRIORITY = ["leading", "guiding", "escalating", "tbd", "none"]
TC_LEVEL_STYLES = {
    "leading":    "fill:#c8e6c9,stroke:#388e3c,color:#1b5e20",
    "guiding":    "fill:#bbdefb,stroke:#1976d2,color:#0d47a1",
    "escalating": "fill:#e1bee7,stroke:#7b1fa2,color:#4a148c",
    "tbd":        "fill:#f5f5f5,stroke:#9e9e9e,color:#424242",
    "none":       "fill:#ffcdd2,stroke:#e53935,color:#b71c1c",
}

chart_lines = []
node_classes = {}  # nid -> level key, collected during render_node


def highest_tc_level(ws_id):
    level_counts = ws_tc_levels[ws_id]
    for lvl in TC_LEVEL_PRIORITY:
        if lvl == "none":
            return "none"
        if level_counts.get(lvl, 0) > 0:
            return lvl


def build_label(ws):
    """Build a multi-line Mermaid node label for a workstream."""
    name = clean_label(ws["name"])

    gc_liaisons = []
    tc_sponsors = []
    for entry in ws.get("people", []):
        if "gcLiaison" in entry:
            u = entry["gcLiaison"]
            if u and u != "tbd":
                gc_liaisons.append(people_info.get(u, {}).get("name", u))
        elif "tcSponsor" in entry:
            u = entry["tcSponsor"].get("username")
            level = entry["tcSponsor"].get("level") or "tbd"
            if u and u != "tbd":
                display_name = people_info.get(u, {}).get("name", u)
                level_abbrev = {"leading": "L", "guiding": "G", "escalating": "E"}.get(level, level)
                tc_sponsors.append(f"{display_name} ({level_abbrev})")

    lines = [name]
    if gc_liaisons:
        lines.append("GC: " + ", ".join(gc_liaisons))
    if tc_sponsors:
        chunks = [", ".join(tc_sponsors[i:i+3]) for i in range(0, len(tc_sponsors), 3)]
        tc_str = "<br/>".join(chunks)
    else:
        tc_str = "tbd"
    lines.append("TC: " + tc_str)

    own = ws_tc_levels[ws["id"]]
    sub = subtree_tc_levels(ws["id"])
    abbrevs = {"leading": "L", "guiding": "G", "escalating": "E"}
    parts = []
    for lvl in BUDGET_LEVELS:
        o = own.get(lvl, 0)
        s = sub.get(lvl, 0)
        denom = level_totals.get(lvl, 0)
        if o == 0 and s == 0 or denom == 0:
            continue
        o_pct = round(o / denom * 100)
        s_pct = round(s / denom * 100)
        if o == s:
            parts.append(f"{abbrevs[lvl]}:{o_pct}%")
        else:
            parts.append(f"{abbrevs[lvl]}:{o_pct}% ({s_pct}%)")
    lines.append("TC Coverage: " + (" · ".join(parts) if parts else "tbd"))

    return "<br/>".join(lines)


def child_sort_key(ws):
    """Sort key: more children first, alphabetical by name as tiebreaker."""
    return (-len(children[ws["id"]]), ws["name"])


def render_node(ws, indent=2):
    """Emit a node label then recurse into children, connecting via edges."""
    nid = node_id(ws["id"])
    label = build_label(ws)
    pad = " " * indent

    if ws.get("kind") == "working-group":
        chart_lines.append(f'{pad}{nid}(["{label}"])')
    else:
        chart_lines.append(f'{pad}{nid}["{label}"]')
    node_classes[nid] = highest_tc_level(ws["id"])
    for child in sorted(children[ws["id"]], key=child_sort_key):
        chart_lines.append(f'{pad}{nid} --> {node_id(child["id"])}')
        render_node(child, indent)


def is_top_level(ws):
    """True if the SIG has no parent."""
    return ws.get("parent", "none") == "none"


chart_lines.append("```mermaid")
chart_lines.append('%%{init: {"flowchart": {"nodeSpacing": 20, "rankSpacing": 40}}}%%')
chart_lines.append("graph LR")
chart_lines.append("")

for lvl, style in TC_LEVEL_STYLES.items():
    chart_lines.append(f"  classDef tc_{lvl} {style}")
chart_lines.append("")

for ws in sorted((ws for ws in all_items if is_top_level(ws)), key=child_sort_key):
    render_node(ws)
chart_lines.append("")

for nid, lvl in node_classes.items():
    chart_lines.append(f"  class {nid} tc_{lvl}")
chart_lines.append("")

chart_lines.append("```")
mermaid_section = "\n".join(chart_lines)


# ─── Section 2: TC sponsorship pivot table ────────────────────────────────────

TC_LEVELS = ["leading", "guiding", "escalating", "tbd"]

# pivot: login (lowercase) -> level -> count
tc_pivot = defaultdict(lambda: defaultdict(int))
for ws in all_items:
    for entry in ws.get("people", []):
        if "tcSponsor" in entry:
            u = entry["tcSponsor"].get("username", "")
            level = entry["tcSponsor"].get("level") or "tbd"
            if u and u != "tbd":
                tc_pivot[u.lower()][level] += 1


def tc_pivot_table():
    tc_members = sorted(
        teams_data.get("technical-committee", []),
        key=lambda u: people_info.get(u, {}).get("name", u).split()[-1].lower(),
    )

    header = "| Member | " + " | ".join(lvl.capitalize() for lvl in TC_LEVELS) + " | Total |"
    sep    = "|--------|" + "---------|" * len(TC_LEVELS) + "---------|"
    rows   = ["## TC Sponsorship Summary\n", header, sep]

    col_totals = defaultdict(int)
    for u in tc_members:
        name = people_info.get(u, {}).get("name", u)
        cells = []
        row_total = 0
        for lvl in TC_LEVELS:
            count = tc_pivot[u.lower()].get(lvl, 0)
            col_totals[lvl] += count
            row_total += count
            cells.append(str(count) if count else "")
        rows.append(f"| [{name}](https://github.com/{u}) | " + " | ".join(cells) + f" | {row_total} |")

    total_cells = " | ".join(str(col_totals[lvl]) for lvl in TC_LEVELS)
    rows.append(f"| **Total** | {total_cells} | {sum(col_totals.values())} |")
    return "\n".join(rows)


# ─── Legend ───────────────────────────────────────────────────────────────────

LEGEND = """\
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

**Arrows** (`-->`) — parent workstream points to child workstream

**TC Coverage line** — `TC Coverage: L:x% (y%) · G:x% (y%) · E:x% (y%)` — share of all Leading / Guiding / Escalating sponsorships assigned to this workstream. Figure in parentheses rolls up all child workstreams; parentheses omitted when the workstream has no children contributing at that level. `tbd` when no sponsor is assigned.\
"""


# ─── Assemble output ──────────────────────────────────────────────────────────

unsponsored_count = sum(1 for ws in all_items if highest_tc_level(ws["id"]) == "none")

output = f"""\
# Workstream Report

{LEGEND}

## Workstream Hierarchy

{mermaid_section}

{tc_pivot_table()}

{unsponsored_count} workstream(s) have no TC sponsor assigned.
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(output)
print(f"Wrote {OUTPUT_FILE}.")
