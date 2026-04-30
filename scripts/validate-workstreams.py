#!/usr/bin/env python3
"""
Validates workstreams.yml.

Usage:
    python scripts/validate-workstreams.py [--install]

Pass --install to auto-install dependencies (pyyaml, jsonschema) before running.

People validation (gcLiaison/tcSponsor/specSponsor membership checks) requires
people.yml, which is checked into the repository. Validation fails if it is missing.
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

WORKSTREAMS_FILE   = REPO_ROOT / "workstreams.yml"
WORKSTREAMS_SCHEMA = SCRIPTS_DIR / "schema" / "workstreams.schema.yml"
PEOPLE_FILE        = REPO_ROOT / "people.yml"

TBD  = "tbd"
NONE = "none"

KIND_REQUIRED_ROLES = {
    "sig":           {"gcLiaison", "tcSponsor"},
    "working-group": {"gcLiaison", "tcSponsor", "lead"},
}

VALID_PARENT_KINDS = {
    "sig":           {"sig"},
    "working-group": {"sig"},
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


def _entry_role_and_username(entry: dict) -> tuple[str, str]:
    """Return (role, username) from a single-key people entry."""
    role = next(iter(entry))
    val  = entry[role]
    if role == "tcSponsor":
        username = val.get("username", "") if isinstance(val, dict) else ""
    else:
        username = val if isinstance(val, str) else ""
    return role, username


def validate_workstreams_semantics(workstreams: list[dict], people_data: dict) -> list[str]:
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

        if parent_id is None or parent_id == NONE:
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
        while current is not None and current != NONE:
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

        teams = people_data.get("teams", {})
        gc_members    = {u.lower() for u in teams.get("governance-committee", [])}
        tc_members    = {u.lower() for u in teams.get("technical-committee", [])}
        spec_sponsors = {u.lower() for u in teams.get("spec-sponsors", [])} | tc_members

        for pr in w.get("people", []):
            role, username = _entry_role_and_username(pr)

            if username == TBD or role not in MEMBERSHIP_REQUIRED_ROLES:
                continue

            if role == "gcLiaison" and username.lower() not in gc_members:
                errors.append(
                    f"[{wid}] '{username}' is assigned gcLiaison "
                    "but is not in the governance-committee team"
                )
            elif role == "tcSponsor" and username.lower() not in tc_members:
                errors.append(
                    f"[{wid}] '{username}' is assigned tcSponsor "
                    "but is not in the technical-committee team"
                )
            elif role == "specSponsor" and username.lower() not in spec_sponsors:
                errors.append(
                    f"[{wid}] '{username}' is assigned specSponsor "
                    "but is not in the spec-sponsors or technical-committee team"
                )

    return errors


def main() -> None:
    all_errors: list[str] = []

    workstreams_schema = load_schema(WORKSTREAMS_SCHEMA)
    workstreams_data   = load_yaml(WORKSTREAMS_FILE)

    all_errors += validate_against_schema(workstreams_data, workstreams_schema, "workstreams.yml")

    if not PEOPLE_FILE.exists():
        print(f"Error: {PEOPLE_FILE.name} not found.", file=sys.stderr)
        sys.exit(1)

    with open(PEOPLE_FILE) as f:
        people_data = yaml.safe_load(f)

    if not all_errors:
        all_errors += validate_workstreams_semantics(workstreams_data, people_data)

    if all_errors:
        for err in all_errors:
            print(err, file=sys.stderr)
        sys.exit(1)

    count = len(workstreams_data)
    print(f"OK — {count} workstream(s) validated (membership checks enabled).")


if __name__ == "__main__":
    main()
