#!/usr/bin/env python3
import subprocess
import sys

# in the Makefile we use a unmodified python container to run this script, so we need to install pyyaml if it's not already installed
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])
    sys.argv = sys.argv[1:]

import yaml

# Do not save the file but verify that it is different from the original one.
run_in_check_mode = (len(sys.argv) > 1) and (sys.argv[1] == "--check")

METADATA_FILE = "people.yml"
MARKDOWN_FILE = "community-members.md"

with open(METADATA_FILE, encoding="utf-8") as f:
    metadata = yaml.safe_load(f)

people = metadata.get("people", {})
teams = metadata.get("teams", {})


def display_name(username):
    return people.get(username, {}).get("name", username)


def company(username):
    return people.get(username, {}).get("company", "")


def term_end(username):
    return people.get(username, {}).get("termEnd", "")


def render_gc():
    usernames = sorted(teams.get("governance-committee", []), key=display_name)
    return "\n".join(
        f"- [{display_name(u)}](https://github.com/{u}), {company(u)}, until {term_end(u)}"
        for u in usernames
    )


def render_tc():
    usernames = sorted(teams.get("technical-committee", []), key=display_name)
    return "\n".join(
        f"- [{display_name(u)}](https://github.com/{u}), {company(u)}"
        for u in usernames
    )


def splice(content, start_marker, end_marker, body):
    before, _, rest = content.partition(start_marker)
    _, _, after = rest.partition(end_marker)
    return f"{before}{start_marker}\n{body}\n{end_marker}{after}"


with open(MARKDOWN_FILE, encoding="utf-8") as f:
    original = f.read()

result = splice(original, "<!-- gc -->", "<!-- endgc -->", render_gc())
result = splice(result, "<!-- tc -->", "<!-- endtc -->", render_tc())

if run_in_check_mode:
    if original == result:
        sys.exit(0)
    else:
        sys.exit(1)
else:
    with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
        f.write(result)

print("The markdown file has been updated with the new GC and TC lists.")
