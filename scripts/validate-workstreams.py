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
SCRIPTS_DIR  = REPO_ROOT / "scripts"

PEOPLE_FILE        = REPO_ROOT / "people.yml"
WORKSTREAMS_FILE   = REPO_ROOT / "workstreams.yml"
PEOPLE_SCHEMA      = SCRIPTS_DIR / "schema" / "people.schema.yml"
WORKSTREAMS_SCHEMA = SCRIPTS_DIR / "schema" / "workstreams.schema.yml"

TBD = "tbd"

KIND_REQUIRED_ROLES = {
    "sig":           {"gcLiaison", "tcSponsor"},
    "working-group": {"gcLiaison", "tcSponsor", "lead"},
    "enhancement":   {"lead"},
}

VALID_PARENT_KINDS = {
    "sig":           {"sig"},
    "working-group": {"sig"},
    "enhancement":   {"sig", "working-group"},
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


def _entry_role_and_username(entry: dict) -> tuple[str, str | None]:
    """Return (role, username) from a single-key people entry.
    Returns (role, None) for team entries (maintainers) that have no username."""
    role = next(iter(entry))
    val  = entry[role]
    if role == "tcSponsor":
        username = val.get("username", "") if isinstance(val, dict) else ""
    elif role == "maintainers":
        username = None
    else:
        username = val if isinstance(val, str) else ""
    return role, username


def validate_workstreams_semantics(workstreams: list[dict], people: dict) -> list[str]:
    errors: list[str] = []

    seen_ids: set[str] = set()
    for w in workstreams:
        wid = w.get("id", "")
        if wid in seen_ids:
            errors.append(f"[{wid}] Duplicate workstream id")
        seen_ids.add(wid)

    id_to_workstream = {w["id"]: w for w in workstreams if "id" in w}

    for w in workstreams:
        wid       = w.get("id", "(unknown)")
        kind      = w.get("kind", "")
        parent_id = w.get("parent")

        if parent_id is None:
            continue

        if parent_id == wid:
            errors.append(f"[{wid}] parent references itself")
            continue

        if parent_id not in id_to_workstream:
            errors.append(f"[{wid}] parent '{parent_id}' does not exist")
            continue

        parent_kind = id_to_workstream[parent_id].get("kind", "")
        if parent_kind not in VALID_PARENT_KINDS.get(kind, set()):
            errors.append(
                f"[{wid}] kind '{kind}' cannot have a parent of kind '{parent_kind}'"
            )

    for w in workstreams:
        wid     = w.get("id", "(unknown)")
        visited = set()
        current = wid
        while current is not None:
            if current in visited:
                errors.append(f"[{wid}] parent chain contains a cycle")
                break
            visited.add(current)
            current = id_to_workstream.get(current, {}).get("parent")

    for w in workstreams:
        wid  = w.get("id", "(unknown)")
        kind = w.get("kind", "")

        if "sigCategory" in w and kind != "sig":
            errors.append(
                f"[{wid}] sigCategory is only valid on kind 'sig'"
            )

        person_roles = {next(iter(pr)) for pr in w.get("people", [])}
        for required_role in KIND_REQUIRED_ROLES.get(kind, set()):
            if required_role not in person_roles:
                errors.append(
                    f"[{wid}] kind '{kind}' requires at least one '{required_role}'"
                )

        for pr in w.get("people", []):
            role, username = _entry_role_and_username(pr)

            if username is None or username == TBD or role not in MEMBERSHIP_REQUIRED_ROLES:
                continue

            if username not in people:
                errors.append(
                    f"[{wid}] '{username}' is assigned {role} "
                    "but is not found in people.yml"
                )
                continue

            membership = set(people[username].get("membership", []))

            if role == "gcLiaison" and "gc-member" not in membership:
                errors.append(
                    f"[{wid}] '{username}' is assigned gcLiaison but is not a gc-member"
                )
            elif role == "tcSponsor" and "tc-member" not in membership:
                errors.append(
                    f"[{wid}] '{username}' is assigned tcSponsor but is not a tc-member"
                )
            elif role == "specSponsor":
                if "spec-sponsor" not in membership and "tc-member" not in membership:
                    errors.append(
                        f"[{wid}] '{username}' is assigned specSponsor "
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
