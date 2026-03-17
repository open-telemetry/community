#!/usr/bin/env python3
"""Generate workstreams.md: Mermaid SIG hierarchy + community member coverage tables."""

import re
import subprocess
import sys
from collections import defaultdict

# Support --install like other scripts in this repo
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml"])
    sys.argv = sys.argv[1:]

import yaml

run_in_check_mode = (len(sys.argv) > 1) and (sys.argv[1] == "--check")

WORKSTREAMS_FILE = "workstreams.yml"
PEOPLE_FILE = "people.yml"
OUTPUT_FILE = "workstreams.md"

with open(WORKSTREAMS_FILE) as f:
    all_items = yaml.safe_load(f)
with open(PEOPLE_FILE) as f:
    people = yaml.safe_load(f)

# Only SIGs (not working-groups)
sigs = [ws for ws in all_items if ws.get("kind") == "sig"]
id_to_sig = {ws["id"]: ws for ws in sigs}


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
                gc_liaisons.append(people.get(u, {}).get("name", u))
        elif "tcSponsor" in entry:
            u = entry["tcSponsor"].get("username")
            level = entry["tcSponsor"].get("level") or "tbd"
            if u and u != "tbd":
                display_name = people.get(u, {}).get("name", u)
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


# ─── Section 2: People tables ─────────────────────────────────────────────────

# Build person -> role -> [workstream_names]
# For tcSponsor: role key is the level (e.g. "leading", "guiding", "escalating", "tbd")
person_roles = defaultdict(lambda: defaultdict(list))

for ws in sigs:
    ws_name = clean_label(ws["name"])  # strip any markdown links from the name
    for entry in ws.get("people", []):
        if "gcLiaison" in entry:
            u = entry["gcLiaison"]
            if u and u != "tbd":
                person_roles[u]["gcLiaison"].append(ws_name)
        elif "tcSponsor" in entry:
            u = entry["tcSponsor"].get("username")
            if u and u != "tbd":
                level = entry["tcSponsor"].get("level") or "tbd"
                person_roles[u][level].append(ws_name)
        elif "specSponsor" in entry:
            u = entry["specSponsor"]
            if u and u != "tbd":
                person_roles[u]["specSponsor"].append(ws_name)

TC_LEVELS = ["leading", "guiding", "escalating", "tbd"]


def sort_by_last_name(usernames):
    def key(u):
        name = people.get(u, {}).get("name", u)
        parts = name.split()
        return parts[-1].lower() if parts else name.lower()
    return sorted(usernames, key=key)


def fmt_ws(names):
    """Comma-separated workstream names sorted alphabetically."""
    return ", ".join(sorted(names)) if names else ""


def person_link(u):
    name = people.get(u, {}).get("name", u)
    return f"[{name}](https://github.com/{u})"


tc_members = sort_by_last_name(
    [u for u, p in people.items() if "tc-member" in p.get("membership", [])]
)
gc_members = sort_by_last_name(
    [u for u, p in people.items() if "gc-member" in p.get("membership", [])]
)
spec_sponsors = sort_by_last_name(
    [u for u, p in people.items() if "spec-sponsor" in p.get("membership", [])]
)


def tc_table():
    sep = "|--------|" + "-----------|" * len(TC_LEVELS)
    header = "| Member | " + " | ".join(f"TC: {lvl}" for lvl in TC_LEVELS) + " |"
    rows = ["### Technical Committee\n", header, sep]
    totals = {lvl: 0 for lvl in TC_LEVELS}
    for u in tc_members:
        cells = []
        for lvl in TC_LEVELS:
            ws = person_roles[u].get(lvl, [])
            totals[lvl] += len(ws)
            cells.append(fmt_ws(ws))
        rows.append(f"| {person_link(u)} | " + " | ".join(cells) + " |")
    total_cells = " | ".join(str(totals[lvl]) for lvl in TC_LEVELS)
    rows.append(f"| **Total** | {total_cells} |")
    return "\n".join(rows)


def gc_table():
    rows = [
        "### Governance Committee\n",
        "| Member | GC Liaison |",
        "|--------|-----------|",
    ]
    for u in gc_members:
        gc_cell = fmt_ws(person_roles[u].get("gcLiaison", []))
        rows.append(f"| {person_link(u)} | {gc_cell} |")
    return "\n".join(rows)


def sponsorship_gaps_table():
    id_to_ws = {ws["id"]: ws for ws in all_items}

    rows = [
        "## Sponsorship Gaps\n",
        "Workstreams with no assigned TC sponsor (**Unsponsored**) or with a sponsor "
        "whose level has not yet been determined (**Level TBD**).\n",
        "| Workstream | Kind | Category | TC Status |",
        "|------------|------|----------|-----------|",
    ]

    def category_cell(ws):
        if ws.get("kind") == "sig":
            return CAT_ABBREV[sig_category(ws)]
        parent_ws = id_to_ws.get(ws.get("parent", "none"))
        if parent_ws:
            return f"(child of {clean_label(parent_ws['name'])})"
        return ""

    gaps = []
    for ws in all_items:
        lvl = highest_tc_level(ws["id"])
        if lvl == "none":
            status = "Unsponsored"
        elif lvl == "tbd":
            status = "Level TBD"
        else:
            continue
        gaps.append((status, ws["name"], ws, category_cell(ws)))

    # Sort: Unsponsored first, then Level TBD; alphabetically within each group
    gaps.sort(key=lambda x: (x[0] != "Unsponsored", x[1]))

    for status, name, ws, cat in gaps:
        kind = ws.get("kind", "sig")
        rows.append(f"| {clean_label(name)} | {kind} | {cat} | {status} |")

    rows.append(f"\n_{len([g for g in gaps if g[0] == 'Unsponsored'])} unsponsored, "
                f"{len([g for g in gaps if g[0] == 'Level TBD'])} level TBD_")
    return "\n".join(rows)


def spec_sponsors_table():
    rows = [
        "### Specification Sponsors\n",
        "| Sponsor | Spec Sponsor |",
        "|---------|-------------|",
    ]
    for u in spec_sponsors:
        spec_cell = fmt_ws(person_roles[u].get("specSponsor", []))
        rows.append(f"| {person_link(u)} | {spec_cell} |")
    return "\n".join(rows)


# ─── Assemble output ──────────────────────────────────────────────────────────

output = f"""\
# Workstream Report

## Workstream Hierarchy

{mermaid_section}

{sponsorship_gaps_table()}

## Community Member Coverage

{tc_table()}

{gc_table()}

{spec_sponsors_table()}
"""

if run_in_check_mode:
    try:
        with open(OUTPUT_FILE) as f:
            existing = f.read()
    except FileNotFoundError:
        print(f"{OUTPUT_FILE} not found.", file=sys.stderr)
        sys.exit(1)
    if existing == output:
        print(f"{OUTPUT_FILE} is up to date.")
        sys.exit(0)
    else:
        print(f"{OUTPUT_FILE} is out of date.", file=sys.stderr)
        sys.exit(1)
else:
    with open(OUTPUT_FILE, "w") as f:
        f.write(output)
    print(f"Wrote {OUTPUT_FILE}.")
