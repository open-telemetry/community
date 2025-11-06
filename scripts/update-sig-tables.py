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

# Define the YAML input file and the markdown file to be updated
yaml_input = "sigs.yml"
markdown_file = "README.md"

# Define the markers
start_marker = "<!-- sigs -->"
end_marker = "<!-- endsigs -->"

def format_chat(chat):
    if chat['type'] == 'slack':
        return f"[{chat['name']}](https://cloud-native.slack.com/archives/{chat['id']})"
    elif chat['type'] == 'other':
        return f"[{chat['name']}]({chat['link']})"
    else:
        return ""

# Read the YAML file
with open(yaml_input, 'r') as file:
    data = yaml.safe_load(file)

# Extract the top and bottom parts of the existing markdown file
with open(markdown_file, 'r') as file:
    content = file.read()
    top_part, bottom_part = content.split(start_marker, 1)[0], content.split(end_marker, 1)[1]

# Generate the markdown content for each SIG group
markdown_content = start_marker + '\n'
for group in data:
    # Group heading
    group_name = group['name']
    markdown_content += f"### {group_name}\n\n"

    # Table headers
    if group_name == "Specification SIGs":
        markdown_content += "| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Sponsors](./project-management.md#project-proposal) | [Governance Committee](./community-members.md#governance-committee) Liaison |\n"
        markdown_content += "|------|--------------|---------------|---------------|-----------------|--------------------------------|--------------------------------|\n"
    else:
        markdown_content += "| Name | Meeting Time | Meeting Notes | Slack Channel | Meeting Invites Group | [Governance Committee](./community-members.md#governance-committee) Liaison |\n"
        markdown_content += "|------|--------------|---------------|---------------|-----------------|--------------------------------|\n"

    # Table rows for SIGs
    for sig in group['sigs']:
        name = sig['name']
        meeting = sig.get('meeting', '')
        notes_type = sig['notes'].get('type', '')
        notes_value = sig['notes'].get('value', '')

        chats = " and ".join(
            [format_chat(chat) 
            for chat in sig.get('chat', [])
            if chat.get('name') and chat.get('type')]
        )

        short_name = None
        for chat in sig.get('chat', []):
            if chat.get('type') == 'slack':
                short_name = 'sig-' + chat.get('name').replace('#otel-', '').replace('sig-', '')
                break

        invites = sig.get('invites', 'none')
        tc_sponsors = ",<br/>".join(
            [f"[{sponsor['name']}](https://github.com/{sponsor['github']})"
            for sponsor in sig.get('sponsors', [])
            if sponsor.get('name') and sponsor.get('github')]
        )

        gc_liaison = "<br/>".join(
            [f"[{liaison['name']}](https://github.com/{liaison['github']})"
            for liaison in sig.get('gcLiaison', [])
            if liaison.get('name') and liaison.get('github')]
        )

        # Construct notes and calendar entries based on type
        if notes_type == "gDoc":
            notes = f"[Google Doc](https://docs.google.com/document/d/{notes_value})"
        else:
            notes = notes_value
        
        if invites == "none":
            calendar = ""
        else:
            calendar = f"[{invites}](https://groups.google.com/a/opentelemetry.io/g/{invites})"
        
        if group_name == "Specification SIGs":
            markdown_content += f"| {name}&nbsp;<a id=\"{short_name}\" href=\"#{short_name}\"><sup>🔗</sup></a> | {meeting} | {notes} | {chats} | {calendar} | {tc_sponsors} | {gc_liaison} | \n"
        else:
            markdown_content += f"| {name}&nbsp;<a id=\"{short_name}\" href=\"#{short_name}\"><sup>🔗</sup></a> | {meeting} | {notes} | {chats} | {calendar} | {gc_liaison} |\n"

    # Add a newline for spacing after the table
    markdown_content += "\n"

markdown_content += end_marker

result = top_part + markdown_content + bottom_part

if run_in_check_mode:
    with open(markdown_file, 'r') as file:
        original = file.read()
    if original == result:
        sys.exit(0)
    else:
        sys.exit(1)
else:
    # Write the updated markdown content to file
    with open(markdown_file, 'w') as file:
        file.write(top_part)
        file.write(markdown_content)
        file.write(bottom_part)

# Inform the user that the markdown file has been updated
print("The markdown file has been updated with the new SIG tables.")
