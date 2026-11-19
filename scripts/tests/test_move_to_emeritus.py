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
                        "example", changes
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


if __name__ == "__main__":
    unittest.main()
