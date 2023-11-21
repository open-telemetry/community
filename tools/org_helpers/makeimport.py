import json

def generate_terraform_commands(json_file):
    # Read and parse the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Extract members and owners
    members = data.get('members', [])
    owners = data.get('owners', [])

    # Generate Terraform import commands
    commands = []

    for member in members:
        command = f"tofu import 'module.memberships[\"{member}\"].github_membership.member' open-telemetry:{member}"
        commands.append(command)

    for owner in owners:
        command = f"tofu import 'module.owners[\"{owner}\"].github_membership.member' open-telemetry:{owner}"
        commands.append(command)

    # Return the commands
    return commands

# Usage
json_file = 'output.json'
commands = generate_terraform_commands(json_file)
for command in commands:
    print(command)
