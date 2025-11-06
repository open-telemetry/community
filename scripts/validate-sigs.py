#!/usr/bin/env python3
import subprocess
import sys
import re

# in the Makefile we use a unmodified python container to run this script, so we need to install pyyaml if it's not already installed
if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyyaml'])

import yaml

def validate_yaml(filename):
    with open(filename, 'r') as file:
        content = yaml.safe_load(file)

    invalid_items = []

    for item_index, item in enumerate(content):
        item_prefix = f"{item.get('name', 'Unnamed')}"

        # Validate SIGs if they exist
        if 'sigs' in item:
            for sig_index, sig in enumerate(item['sigs']):
                sig_prefix = f"{item_prefix} - {sig.get('name', 'Unnamed')}:"

                # Check name and meeting are set for SIG
                if 'name' not in sig:
                    invalid_items.append(f"{sig_prefix} Missing 'name' field.")
                if 'meeting' not in sig:
                    invalid_items.append(f"{sig_prefix} Missing 'meeting' field.")

                # Check notes validation for SIG
                notes = sig.get('notes', {})
                if notes.get('type') not in ('none', 'gDoc'):
                    invalid_items.append(f"{sig_prefix} Notes type must be 'none' or 'gDoc'.")
                elif notes.get('type') == 'gDoc':
                    if not re.match(r'^[\w-]+$', notes.get('value', '')):
                        invalid_items.append(f"{sig_prefix} Invalid gDoc value.")

                # Check chat validation for SIG
                chats = sig.get('chat', [])
                slack_chats = [chat for chat in chats if chat.get('type') == 'slack']
                if len(slack_chats) == 0:
                    invalid_items.append(f"{sig_prefix} There must be at least one Slack chat.")
                else:
                    for chat in slack_chats:
                        if not chat.get('name', '').startswith('#otel-'):
                            invalid_items.append(f"{sig_prefix} Chat name must start with '#otel-'.")
                        if not re.match(r'^[A-Z0-9]{9,11}$', chat.get('id', '')):
                            invalid_items.append(f"{sig_prefix} Invalid Slack channel ID.")

                # Check invites is set for SIG
                if 'invites' not in sig:
                    invalid_items.append(f"{sig_prefix} Missing 'invites' field.")

                # Check sponsors for SIG
                tc_sponsors = sig.get('sponsors', [])
                if tc_sponsors:
                    for sponsor in tc_sponsors:
                        if 'name' not in sponsor or 'github' not in sponsor:
                            invalid_items.append(f"{sig_prefix} Each tcSponsor must have a 'name' and 'github'.")

                # Check GC Liaison validation for SIG
                gc_liaisons = sig.get('gcLiaison', [])
                if not gc_liaisons:
                    invalid_items.append(f"{sig_prefix} 'gcLiaison' list is missing or empty.")
                else:
                    for gc_liaison in gc_liaisons:
                        if 'name' not in gc_liaison or 'github' not in gc_liaison:
                            invalid_items.append(f"{sig_prefix} Each GC Liaison must have a 'name' and 'github'.")

    return invalid_items

# Replace 'your_file.yaml' with the path to your actual YAML file
invalid_items = validate_yaml('sigs.yml')
for invalid_item in invalid_items:
    print(invalid_item)
