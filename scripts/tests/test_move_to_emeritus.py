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


if __name__ == "__main__":
    unittest.main()
