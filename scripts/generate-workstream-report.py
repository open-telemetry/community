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


def sig_category(ws):
    return ws.get("sigCategory")


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


# ─── Section 1: Mermaid chart ─────────────────────────────────────────────────

CAT_ABBREV = {
    "specification": "spec",
    "implementation": "impl",
    "cross-cutting": "cross",
}

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
    kind = ws.get("kind", "sig")

    if kind == "sig":
        kind_str = f"Kind: sig ({CAT_ABBREV[sig_category(ws)]})"
    else:
        kind_str = f"Kind: {kind}"

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
                tc_sponsors.append(f"{display_name} ({level})")

    lines = [name, kind_str]
    if gc_liaisons:
        lines.append("GC: " + ", ".join(gc_liaisons))
    if tc_sponsors:
        lines.append("TC: " + ", ".join(tc_sponsors))
    return "<br/>".join(lines)


def render_node(ws, indent=2):
    """Emit a node label then recurse into children, connecting via edges."""
    nid = node_id(ws["id"])
    label = build_label(ws)
    pad = " " * indent

    chart_lines.append(f'{pad}{nid}["{label}"]')
    node_classes[nid] = highest_tc_level(ws["id"])
    for child in children[ws["id"]]:
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

for ws in all_items:
    if is_top_level(ws):
        render_node(ws)
chart_lines.append("")

for nid, lvl in node_classes.items():
    chart_lines.append(f"  class {nid} tc_{lvl}")
chart_lines.append("")

chart_lines.append("```")
mermaid_section = "\n".join(chart_lines)


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

**Name suffix** — SIG category: `(spec)` Specification · `(impl)` Implementation · `(cross)` Cross-cutting

**Arrows** (`-->`) — parent workstream points to child workstream\
"""


# ─── Assemble output ──────────────────────────────────────────────────────────

output = f"""\
# Workstream Report

{LEGEND}

## Workstream Hierarchy

{mermaid_section}
"""

with open(OUTPUT_FILE, "w") as f:
    f.write(output)
print(f"Wrote {OUTPUT_FILE}.")
