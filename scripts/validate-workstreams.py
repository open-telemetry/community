#!/usr/bin/env python3
"""
Validates people.yml and workstreams.yml.

Usage:
    python scripts/validate-workstreams.py [--install]

Pass --install to auto-install dependencies (pyyaml, jsonschema) before running.
"""

import subprocess
import sys
from pathlib import Path

if (len(sys.argv) > 1) and (sys.argv[1] == "--install"):
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "jsonschema"])

import yaml
import jsonschema

REPO_ROOT    = Path(__file__).parent.parent
SCHEMAS_DIR  = REPO_ROOT / "schemas"

PEOPLE_FILE        = REPO_ROOT / "people.yml"
WORKSTREAMS_FILE   = REPO_ROOT / "workstreams.yml"
PEOPLE_SCHEMA      = SCHEMAS_DIR / "people.yaml"
WORKSTREAMS_SCHEMA = SCHEMAS_DIR / "workstreams.yaml"

TBD = "tbd"

KIND_REQUIRED_ROLES = {
    "sig":           {"gcLiaison", "tcSponsor"},
    "working-group": {"gcLiaison", "tcSponsor", "lead"},
    "enhancement":   {"lead"},
}

MEMBERSHIP_REQUIRED_ROLES = {"gcLiaison", "tcSponsor", "specSponsor"}


def load_schema(path: Path) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


def load_yaml(path: Path) -> object:
    with open(path) as f:
        return yaml.safe_load(f)


def validate_against_schema(data: object, schema: dict, label: str) -> list[str]:
    errors = []
    validator = jsonschema.Draft202012Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path)):
        path = " -> ".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"[{label}] {path}: {err.message}")
    return errors


def validate_people_semantics(people: dict) -> list[str]:
    return []


def validate_workstreams_semantics(workstreams: list[dict], people: dict) -> list[str]:
    errors: list[str] = []

    seen_ids: set[str] = set()
    for w in workstreams:
        wid = w.get("id", "")
        if wid in seen_ids:
            errors.append(f"[{wid}] Duplicate workstream id")
        seen_ids.add(wid)

    for w in workstreams:
        wid  = w.get("id", "(unknown)")
        kind = w.get("kind", "")

        person_roles = {pr.get("role") for pr in w.get("people", [])}
        for required_role in KIND_REQUIRED_ROLES.get(kind, set()):
            if required_role not in person_roles:
                errors.append(
                    f"[{wid}] kind '{kind}' requires at least one '{required_role}'"
                )

        for pr in w.get("people", []):
            if pr.get("role") == "tcSponsor" and "tcSponsorLevel" not in pr:
                errors.append(
                    f"[{wid}] tcSponsor '{pr.get('github')}' is missing 'tcSponsorLevel'"
                )

        for pr in w.get("people", []):
            role   = pr.get("role")
            handle = pr.get("github", "")

            if handle == TBD or role not in MEMBERSHIP_REQUIRED_ROLES:
                continue

            if handle not in people:
                errors.append(
                    f"[{wid}] '{handle}' is assigned {role} "
                    "but is not found in people.yml"
                )
                continue

            membership = set(people[handle].get("membership", []))

            if role == "gcLiaison" and "gc-member" not in membership:
                errors.append(
                    f"[{wid}] '{handle}' is assigned gcLiaison but is not a gc-member"
                )
            elif role == "tcSponsor" and "tc-member" not in membership:
                errors.append(
                    f"[{wid}] '{handle}' is assigned tcSponsor but is not a tc-member"
                )
            elif role == "specSponsor":
                if "spec-sponsor" not in membership and "tc-member" not in membership:
                    errors.append(
                        f"[{wid}] '{handle}' is assigned specSponsor "
                        "but is not a spec-sponsor or tc-member"
                    )

    return errors


def main() -> None:
    all_errors: list[str] = []

    people_schema      = load_schema(PEOPLE_SCHEMA)
    workstreams_schema = load_schema(WORKSTREAMS_SCHEMA)

    people_data      = load_yaml(PEOPLE_FILE)
    workstreams_data = load_yaml(WORKSTREAMS_FILE)

    all_errors += validate_against_schema(people_data, people_schema, "people.yml")
    all_errors += validate_against_schema(workstreams_data, workstreams_schema, "workstreams.yml")

    if not all_errors:
        all_errors += validate_people_semantics(people_data)
        all_errors += validate_workstreams_semantics(workstreams_data, people_data)

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        sys.exit(1)

    count = len(workstreams_data)
    print(f"OK — {count} workstream(s) and {len(people_data)} people validated.")


if __name__ == "__main__":
    main()
