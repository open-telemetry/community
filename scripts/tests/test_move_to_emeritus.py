# Copyright The OpenTelemetry Authors
# SPDX-License-Identifier: Apache-2.0

import importlib.util
import os
import unittest
from pathlib import Path
from unittest import mock


os.environ.setdefault("GITHUB_TOKEN", "test-token")
SCRIPT = Path(__file__).parents[1] / "move-to-emeritus.py"
SPEC = importlib.util.spec_from_file_location("move_to_emeritus", SCRIPT)
emeritus = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(emeritus)


class EmeritusDocumentTest(unittest.TestCase):
    def setUp(self):
        self.user_info = {
            "alice": {
                "role": "Maintainer",
                "roles": {"Maintainer"},
                "teams": ["example-maintainers"],
            }
        }

    def test_detects_active_member_in_contributing(self):
        readme = "# Example\n\n## License\n"
        contributing = (
            "# Contributing\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice), Example Corp\n"
        )

        self.assertFalse(emeritus._has_active_member(readme, self.user_info))
        self.assertTrue(
            emeritus._has_active_member(contributing, self.user_info)
        )

    @mock.patch.object(emeritus, "fetch_repo_file")
    @mock.patch.object(emeritus, "fetch_readme")
    def test_falls_back_to_contributing(self, fetch_readme, fetch_repo_file):
        readme = ("# Example\n\n## License\n", "readme-sha", "README.md")
        contributing = (
            "# Contributing\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice), Example Corp\n",
            "contributing-sha",
            "CONTRIBUTING.md",
        )
        fetch_readme.return_value = readme
        fetch_repo_file.return_value = contributing

        result = emeritus._find_membership_document("example", self.user_info)

        self.assertEqual(contributing, result)
        fetch_repo_file.assert_called_once_with("example", "CONTRIBUTING.md")

    @mock.patch.object(emeritus, "fetch_repo_file")
    @mock.patch.object(emeritus, "fetch_readme")
    def test_falls_back_to_contributing_without_readme(
        self, fetch_readme, fetch_repo_file
    ):
        contributing = (
            "# Contributing\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice), Example Corp\n",
            "contributing-sha",
            "CONTRIBUTING.md",
        )
        fetch_readme.return_value = None
        fetch_repo_file.return_value = contributing

        result = emeritus._find_membership_document("example", self.user_info)

        self.assertEqual(contributing, result)

    @mock.patch.object(emeritus, "fetch_repo_file")
    @mock.patch.object(emeritus, "fetch_readme")
    def test_keeps_contributing_for_emeritus_follow_up(
        self, fetch_readme, fetch_repo_file
    ):
        readme = ("# Example\n\n## License\n", "readme-sha", "README.md")
        contributing = (
            "# Contributing\n\n## Emeritus\n\n"
            "- [Alice Example](https://github.com/alice), Maintainer\n",
            "contributing-sha",
            "CONTRIBUTING.md",
        )
        fetch_readme.return_value = readme
        fetch_repo_file.return_value = contributing

        result = emeritus._find_membership_document("example", self.user_info)

        self.assertEqual(contributing, result)

    @mock.patch.object(emeritus, "fetch_repo_file")
    @mock.patch.object(emeritus, "fetch_readme")
    def test_keeps_readme_when_it_has_active_members(
        self, fetch_readme, fetch_repo_file
    ):
        readme = (
            "# Example\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice), Example Corp\n",
            "readme-sha",
            "README.md",
        )
        fetch_readme.return_value = readme

        result = emeritus._find_membership_document("example", self.user_info)

        self.assertEqual(readme, result)
        fetch_repo_file.assert_not_called()

    def test_moves_active_member_and_preserves_display_name(self):
        document = (
            "# Contributing\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice), Example Corp\n\n"
            "## Emeritus\n\n"
            "- [Bob Example](https://github.com/bob), Approver\n"
        )

        result, changes, missing = emeritus._apply_emeritus_changes(
            document, self.user_info
        )

        self.assertNotIn("Example Corp", result)
        self.assertIn(
            "- [Alice Example](https://github.com/alice), Maintainer", result
        )
        self.assertEqual(
            [("alice", "Maintainer", ["example-maintainers"])], changes
        )
        self.assertEqual([], missing)

    @mock.patch.object(emeritus, "_get_display_name")
    def test_preserves_name_with_unusual_trailing_text(self, get_display_name):
        document = (
            "# Example\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice) — team lead\n"
        )

        self.assertTrue(emeritus._has_active_member(document, self.user_info))
        result, changes, missing = emeritus._apply_emeritus_changes(
            document, self.user_info
        )

        self.assertIn(
            "- [Alice Example](https://github.com/alice), Maintainer", result
        )
        self.assertEqual(1, result.count("https://github.com/alice"))
        self.assertEqual(1, len(changes))
        self.assertEqual([], missing)
        get_display_name.assert_not_called()

    @mock.patch.object(emeritus, "_get_display_name")
    def test_preserves_name_with_mixed_case_profile_url(self, get_display_name):
        document = (
            "# Example\n\n## Maintainers\n\n"
            "- [Alice Example](HTTPS://GitHub.com/Alice), Example Corp\n"
        )

        self.assertTrue(emeritus._has_active_member(document, self.user_info))
        result, changes, missing = emeritus._apply_emeritus_changes(
            document, self.user_info
        )

        self.assertNotIn("Example Corp", result)
        self.assertIn(
            "- [Alice Example](https://github.com/alice), Maintainer", result
        )
        self.assertEqual(
            [("alice", "Maintainer", ["example-maintainers"])], changes
        )
        self.assertEqual([], missing)
        get_display_name.assert_not_called()

    def test_keeps_existing_follow_up_issue_behavior(self):
        document = (
            "# Example\n\n## Emeritus\n\n"
            "- [Alice Example](https://github.com/alice), Maintainer\n"
        )

        result, changes, missing = emeritus._apply_emeritus_changes(
            document, self.user_info
        )

        self.assertEqual(document, result)
        self.assertEqual(
            [("alice", "Maintainer", ["example-maintainers"])], changes
        )
        self.assertEqual([], missing)

    def test_does_not_add_member_missing_from_active_roles(self):
        document = "# Example\n\n## License\n"

        result, changes, missing = emeritus._apply_emeritus_changes(
            document, self.user_info
        )

        self.assertEqual(document, result)
        self.assertEqual([], changes)
        self.assertEqual(["alice"], missing)

    @mock.patch.object(emeritus, "_create_followup_issue")
    @mock.patch.object(emeritus, "fetch_repo_file")
    @mock.patch.object(emeritus, "fetch_readme")
    def test_creates_follow_up_for_emeritus_formatting_variants(
        self, fetch_readme, fetch_repo_file, create_followup_issue
    ):
        entries = (
            "- [Alice Example](https://github.com/alice/), Maintainer",
            "| [Alice Example](https://github.com/alice) | Maintainer |",
            "| [Alice Example](HTTPS://GitHub.com/Alice/) | Maintainer |",
        )
        report = {"example": [("alice", "example-maintainers", "Maintainer")]}
        for entry in entries:
            for path in ("README.md", "CONTRIBUTING.md"):
                with self.subTest(entry=entry, path=path):
                    document = "# Example\n\n## Emeritus\n\n" + entry + "\n"
                    membership = (document, "sha", path)
                    other = ("# Example\n", "other-sha", "README.md")
                    fetch_readme.return_value = (
                        membership if path == "README.md" else other
                    )
                    fetch_repo_file.return_value = (
                        membership if path == "CONTRIBUTING.md" else None
                    )
                    create_followup_issue.reset_mock()

                    result, changes, missing = emeritus._apply_emeritus_changes(
                        document, self.user_info
                    )
                    self.assertEqual(document, result)
                    self.assertEqual([], missing)

                    with mock.patch("builtins.print"):
                        emeritus.create_emeritus_prs(report, {}, "2026-01-01")

                    create_followup_issue.assert_called_once_with(
                        "example", changes, security_notes=None
                    )
                    self.assertEqual(
                        [("alice", "Maintainer", ["example-maintainers"])], changes
                    )

    def test_emeritus_check_matches_only_target_profile_in_section(self):
        document = (
            "# Example\n\n## Maintainers\n\n"
            "- [Alice Example](https://github.com/alice)\n\n"
            "## Emeritus\n\n"
            "| [Other Alice](https://github.com/alice-other/) | Maintainer |\n"
        )

        self.assertFalse(emeritus._has_emeritus_member(document, self.user_info))


class SecurityInsightsTest(unittest.TestCase):
    SI_V2 = (
        "header:\n"
        "  schema-version: 2.0.0\n"
        "project:\n"
        "  administrators:\n"
        "    - name: Alice Example\n"
        "      affiliation: Example Corp\n"
        "      social: https://github.com/alice\n"
        "      primary: true\n"
        "    - name: Bob Example\n"
        "      affiliation: Example Corp\n"
        "      social: https://github.com/bob\n"
        "      primary: false\n"
        "repository:\n"
        "  core-team:\n"
        "    - name: Alice Example\n"
        "      affiliation: Example Corp\n"
        "      social: https://github.com/alice\n"
        "      primary: true\n"
        "    - name: Carol Example\n"
        "      affiliation: Example Corp\n"
        "      social: https://github.com/carol\n"
        "      primary: false\n"
    )

    SI_V1 = (
        "header:\n"
        '  schema-version: "1.0.0"\n'
        "project-lifecycle:\n"
        "  status: active\n"
        "  core-maintainers:\n"
        "    - https://github.com/alice\n"
        "    - https://github.com/bob\n"
        "    - https://github.com/carol\n"
    )

    def test_remove_v2_drops_all_matching_entries(self):
        result, _ = emeritus._remove_security_insights_entry_v2(self.SI_V2, "alice")

        self.assertNotIn("github.com/alice\n", result)
        # Alice appeared in both administrators and core-team — both gone.
        self.assertEqual(0, result.count("github.com/alice"))
        # Other entries untouched.
        self.assertIn("github.com/bob", result)
        self.assertIn("github.com/carol", result)
        # Surrounding YAML structure preserved.
        self.assertIn("administrators:", result)
        self.assertIn("core-team:", result)

    def test_remove_v2_case_insensitive_url(self):
        doc = self.SI_V2.replace(
            "social: https://github.com/alice",
            "social: HTTPS://GitHub.com/Alice",
        )
        result, _ = emeritus._remove_security_insights_entry_v2(doc, "alice")

        self.assertNotIn("Alice", result.split("administrators:")[-1].split("repository:")[0])

    def test_remove_v2_missing_user_is_noop(self):
        result, changed = emeritus._remove_security_insights_entry_v2(
            self.SI_V2, "mallory"
        )

        self.assertEqual(self.SI_V2, result)
        self.assertFalse(changed)

    def test_remove_v1_drops_flat_url_entry(self):
        result, changed = emeritus._remove_security_insights_entry_v1(
            self.SI_V1, "bob"
        )

        self.assertNotIn("github.com/bob", result)
        self.assertIn("github.com/alice", result)
        self.assertIn("github.com/carol", result)
        self.assertTrue(changed)

    def test_remove_v1_case_insensitive(self):
        doc = self.SI_V1.replace(
            "- https://github.com/bob", "- HTTPS://GitHub.com/Bob"
        )
        result, changed = emeritus._remove_security_insights_entry_v1(doc, "bob")

        self.assertNotIn("Bob", result)
        self.assertTrue(changed)

    def test_update_reports_unresolved_users(self):
        # `dave` is nowhere in the file → removal is a no-op → unresolved stays empty.
        new_content, unresolved = emeritus._update_security_insights(
            self.SI_V2, ["dave"], schema_major=2
        )
        self.assertEqual(self.SI_V2, new_content)
        self.assertEqual([], unresolved)

    def test_update_flags_user_still_present_after_removal(self):
        # If the user URL appears in a format our regex doesn't recognise (e.g. a
        # free-text comment), we should flag them as unresolved.
        doc = (
            "header:\n"
            "  schema-version: 2.0.0\n"
            "project:\n"
            "  comment: see https://github.com/alice for history\n"
        )
        _, unresolved = emeritus._update_security_insights(
            doc, ["alice"], schema_major=2
        )
        self.assertEqual(["alice"], unresolved)

    @mock.patch.object(emeritus, "fetch_repo_file")
    def test_fetch_requires_schema_version_header(self, fetch_repo_file):
        # A file at the same path without a schema-version header is skipped so
        # we never mutate an unrelated file sitting there.
        fetch_repo_file.return_value = ("# just a readme\n", "sha", ".github/security-insights.yml")

        self.assertIsNone(emeritus._fetch_security_insights("example"))

    @mock.patch.object(emeritus, "fetch_repo_file")
    def test_fetch_detects_schema_version(self, fetch_repo_file):
        fetch_repo_file.side_effect = [
            (self.SI_V2, "sha", ".github/security-insights.yml"),
        ]

        result = emeritus._fetch_security_insights("example")
        self.assertIsNotNone(result)
        content, sha, path, schema_major = result
        self.assertEqual(sha, "sha")
        self.assertEqual(path, ".github/security-insights.yml")
        self.assertEqual(2, schema_major)

    @mock.patch.object(emeritus, "fetch_repo_file")
    def test_fetch_falls_back_to_root_path(self, fetch_repo_file):
        fetch_repo_file.side_effect = [
            None,
            (self.SI_V1, "sha", "SECURITY-INSIGHTS.yml"),
        ]

        result = emeritus._fetch_security_insights("example")
        self.assertIsNotNone(result)
        _, _, path, schema_major = result
        self.assertEqual(path, "SECURITY-INSIGHTS.yml")
        self.assertEqual(1, schema_major)


if __name__ == "__main__":
    unittest.main()
