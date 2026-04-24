#!/usr/bin/env python3
import subprocess
import sys

# in the Makefile we use a unmodified python container to run this script, so we need to install pyyaml if it's not already installed
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
    sys.argv = sys.argv[1:]

import yaml

# Do not safe the file but verify that it is different from the original one.
run_in_check_mode = (len(sys.argv) > 1) and (sys.argv[1] == "--check")

WORKSTREAMS_FILE = "workstreams.yml"
METADATA_FILE    = "people.yml"
markdown_file    = "README.md"

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


def sig_short_name(ws):
    for res in ws.get("resources", []):
        if "slack" in res:
            channel_name = res["slack"]["name"]
            return "sig-" + channel_name.replace("#otel-", "").replace("sig-", "")
    return None


def extract_row_data(ws):
    meeting_schedule = ""
    notes_link = ""
    chats = []
    calendar = ""

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
            chats.append(f"[{s['name']}](https://cloud-native.slack.com/archives/{s['id']})")
        elif "githubDiscussion" in res:
            chats.append(f"[GitHub Discussions]({res['githubDiscussion']})")

    chat_str = " and ".join(chats)

    gc_liaisons = []
    tc_sponsors = []

    for entry in ws.get("people", []):
        if "gcLiaison" in entry:
            link = person_link(entry["gcLiaison"])
            if link:
                gc_liaisons.append(link)
        elif "tcSponsor" in entry:
            link = person_link(entry["tcSponsor"]["username"])
            if link:
                tc_sponsors.append(link)
        elif "specSponsor" in entry:
            link = person_link(entry["specSponsor"])
            if link:
                tc_sponsors.append(link)

    gc_str = "<br/>".join(gc_liaisons)

    if ws.get("tcSponsorship") == "collective":
        sponsor_str = "[Technical Committee](./community-members.md#technical-committee)"
    else:
        sponsor_str = ",<br/>".join(tc_sponsors)

    return meeting_schedule, notes_link, chat_str, calendar, sponsor_str, gc_str


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


def render_group(group_name, sigs, show_sponsors):
    content = f"### {group_name}\n\n"
    if show_sponsors:
        content += "| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Sponsors](./project-management.md#project-proposal) | [Governance Committee](./community-members.md#governance-committee) Liaison |\n"
        content += "|------|--------------|---------------|---------------|-----------------|--------------------------------|--------------------------------|\n"
    else:
        content += "| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Governance Committee](./community-members.md#governance-committee) Liaison |\n"
        content += "|------|--------------|---------------|---------------|-----------------|--------------------------------|\n"

    for ws in sigs:
        name = ws["name"]
        short_name = sig_short_name(ws)
        meeting, notes, chats, calendar, sponsors, gc = extract_row_data(ws)

        if short_name:
            name_cell = f"{name}&nbsp;<a id=\"{short_name}\" href=\"#{short_name}\"><sup>🔗</sup></a>"
        else:
            name_cell = name

        if show_sponsors:
            content += f"| {name_cell} | {meeting} | {notes} | {chats} | {calendar} | {sponsors} | {gc} | \n"
        else:
            content += f"| {name_cell} | {meeting} | {notes} | {chats} | {calendar} | {gc} |\n"

    content += "\n"
    return content


with open(markdown_file, encoding="utf-8") as f:
    content = f.read()

top_part = content.split(start_marker, 1)[0]
bottom_part = content.split(end_marker, 1)[1]

markdown_content = start_marker + "\n"
markdown_content += render_group("Specification SIGs", spec_sigs, show_sponsors=True)
markdown_content += render_group("Implementation SIGs", impl_sigs, show_sponsors=False)
markdown_content += render_group("Cross-Cutting SIGs", cross_sigs, show_sponsors=False)
markdown_content += render_group("Localization Teams (part of SIG Communications)", localization_sigs, show_sponsors=False)
markdown_content += end_marker

result = top_part + markdown_content + bottom_part

if run_in_check_mode:
    with open(markdown_file, encoding="utf-8") as f:
        original = f.read()
    if original == result:
        sys.exit(0)
    else:
        sys.exit(1)
else:
    with open(markdown_file, "w", encoding="utf-8") as f:
        f.write(result)

# Inform the user that the markdown file has been updated
print("The markdown file has been updated with the new SIG tables.")
