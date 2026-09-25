#!/usr/bin/env python3
import re
import subprocess
import sys

# in the Makefile we use a unmodified python container to run this script, so we need to install pyyaml if it's not already installed
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
    sys.argv = sys.argv[1:]

import yaml

# Do not save the file but verify that it is different from the original one.
run_in_check_mode = (len(sys.argv) > 1) and (sys.argv[1] == "--check")

WORKSTREAMS_FILE = "workstreams.yml"
METADATA_FILE    = "people.yml"
readme_file      = "README.md"
sigs_file        = "sigs.md"

start_marker = "<!-- sigs -->"
end_marker = "<!-- endsigs -->"

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
        return ""
    name = _people.get(username, {}).get("name", username)
    return f"[{name}](https://github.com/{username})"


def heading_anchor(text):
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = re.sub(r"[^a-z0-9\s-]", "", text.lower())
    return text.strip().replace(" ", "-")


def repository_link(repository):
    return f"[{repository}](https://github.com/{repository})"


def roadmap_project_link(project_id, name):
    return f"[{name} roadmap](https://github.com/orgs/open-telemetry/projects/{project_id})"


def extract_row_data(ws):
    meeting_schedule = ""
    notes_link = ""
    slack_channels = []
    discussions = []
    calendar = ""
    repositories = []
    roadmap_projects = []

    for res in ws.get("resources", []):
        if "meeting" in res:
            m = res["meeting"]
            meeting_schedule = m.get("schedule", "")
            if gdoc := m.get("gDocNotes"):
                notes_link = f"[Google Doc](https://docs.google.com/document/d/{gdoc})"
            if cal := m.get("calendarInviteGroup"):
                calendar = f"[{cal}](https://groups.google.com/a/opentelemetry.io/g/{cal})"
        elif "slack" in res:
            s = res["slack"]
            slack_channels.append(f"[{s['name']}](https://cloud-native.slack.com/archives/{s['id']})")
        elif "githubDiscussion" in res:
            discussions.append(f"[GitHub Discussions]({res['githubDiscussion']})")
        elif "repository" in res:
            repositories.append(repository_link(res["repository"]))
        elif "roadmapProject" in res:
            roadmap_projects.append(roadmap_project_link(res["roadmapProject"], ws["name"]))

    gc_liaisons = []
    tc_sponsors = []
    spec_sponsors = []

    for entry in ws.get("people", []):
        if "gcLiaison" in entry:
            gc_liaisons.append(person_link(entry["gcLiaison"]) or entry["gcLiaison"])
        elif "tcSponsor" in entry:
            sponsor = entry["tcSponsor"]
            link = person_link(sponsor["username"]) or sponsor["username"]
            level = sponsor.get("level")
            if level and level != "tbd":
                link = f"{link} ({level})"
            tc_sponsors.append(link)
        elif "specSponsor" in entry:
            spec_sponsors.append(person_link(entry["specSponsor"]) or entry["specSponsor"])

    if ws.get("tcSponsorship") == "collective":
        tc_sponsors = ["[Technical Committee](./community-members.md#technical-committee)"]

    return {
        "meeting_schedule": meeting_schedule,
        "notes_link": notes_link,
        "slack_channels": slack_channels,
        "discussions": discussions,
        "calendar": calendar,
        "repositories": repositories,
        "roadmap_projects": roadmap_projects,
        "gc_liaisons": gc_liaisons,
        "tc_sponsors": tc_sponsors,
        "spec_sponsors": spec_sponsors,
    }


# Categorize SIGs into groups, preserving workstreams.yml order within each group.
spec_sigs = []
impl_sigs = []
cross_sigs = []
localization_sigs = []

for ws in workstreams:
    if ws.get("kind") != "sig":
        continue
    category = ws.get("sigCategory")
    parent = ws.get("parent", "none")

    if category == "implementation":
        impl_sigs.append(ws)
    elif category == "cross-cutting":
        if parent == "communications":
            localization_sigs.append(ws)
        else:
            cross_sigs.append(ws)
    else:
        # specification (sigCategory absent or explicit)
        spec_sigs.append(ws)


def join_details(values):
    return ", ".join(value for value in values if value)


def render_group(group_name, sigs):
    content = f"### {group_name}\n\n"
    content += "| Name | Meeting Time | Meeting Invites Group | Slack Channel | Details |\n"
    content += "|------|--------------|-----------------------|---------------|---------|\n"

    for ws in sigs:
        name = ws["name"]
        data = extract_row_data(ws)
        details = f"[Details](./{sigs_file}#{heading_anchor(name)})"
        content += f"| {name} | {data['meeting_schedule']} | {data['calendar']} | {join_details(data['slack_channels'])} | {details} |\n"

    content += "\n"
    return content


def render_sig_details(ws):
    data = extract_row_data(ws)
    details = [
        ("Meeting time", data["meeting_schedule"]),
        ("Meeting notes", data["notes_link"]),
        ("Meeting invites group", data["calendar"]),
        ("Slack channel", join_details(data["slack_channels"])),
        ("GitHub Discussions", join_details(data["discussions"])),
        ("Repositories", join_details(data["repositories"])),
        ("Roadmap projects", join_details(data["roadmap_projects"])),
        ("Technical Committee sponsors", join_details(data["tc_sponsors"])),
        ("Spec sponsors", join_details(data["spec_sponsors"])),
        ("Governance Committee liaison", join_details(data["gc_liaisons"])),
    ]

    bullets = "".join(f"- **{label}:** {value}\n" for label, value in details if value)
    return f"### {ws['name']}\n\n{bullets}\n"


def render_sig_details_group(group_name, sigs):
    content = f"## {group_name}\n\n"
    for ws in sigs:
        content += render_sig_details(ws)
    return content


def render_sigs_markdown():
    content = "# OpenTelemetry Special Interest Groups\n\n"
    content += "<!-- This file is auto-generated. To make changes, see CONTRIBUTING.md#updating-sig-information. -->\n\n"
    content += "This page contains detailed information for all OpenTelemetry Special Interest Groups (SIGs).\n\n"
    content += render_sig_details_group("Specification SIGs", spec_sigs)
    content += render_sig_details_group("Implementation SIGs", impl_sigs)
    content += render_sig_details_group("Cross-Cutting SIGs", cross_sigs)
    content += render_sig_details_group("Localization Teams (part of SIG Communications)", localization_sigs)
    return content.rstrip() + "\n"


with open(readme_file, encoding="utf-8") as f:
    content = f.read()

top_part = content.split(start_marker, 1)[0]
bottom_part = content.split(end_marker, 1)[1]

markdown_content = start_marker + "\n"
markdown_content += render_group("Specification SIGs", spec_sigs)
markdown_content += render_group("Implementation SIGs", impl_sigs)
markdown_content += render_group("Cross-Cutting SIGs", cross_sigs)
markdown_content += render_group("Localization Teams (part of SIG Communications)", localization_sigs)
markdown_content += end_marker

readme_result = top_part + markdown_content + bottom_part
sigs_result = render_sigs_markdown()


def file_matches(path, expected):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read() == expected
    except FileNotFoundError:
        return False

if run_in_check_mode:
    if file_matches(readme_file, readme_result) and file_matches(sigs_file, sigs_result):
        sys.exit(0)
    else:
        print(f"{readme_file} or {sigs_file} is out of date. Run 'make generate' to update it.", file=sys.stderr)
        sys.exit(1)
else:
    with open(readme_file, "w", encoding="utf-8") as f:
        f.write(readme_result)
    with open(sigs_file, "w", encoding="utf-8") as f:
        f.write(sigs_result)

# Inform the user that the markdown file has been updated
print("The markdown files have been updated with the new SIG tables.")
