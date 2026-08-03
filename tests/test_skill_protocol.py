"""Verify the Requirements Workshop interaction contract.

This intentionally uses only the Python standard library so anyone cloning the
plugin can confirm that the documented discussion protocol remains intact.
"""

from __future__ import annotations

import json
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).parents[1]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "requirements-workshop"
SKILL_PATH = PLUGIN_ROOT / "skills" / "requirements-workshop" / "SKILL.md"
MANIFEST_PATH = PLUGIN_ROOT / ".codex-plugin" / "plugin.json"
MARKETPLACE_PATH = REPO_ROOT / ".agents" / "plugins" / "marketplace.json"
README_PATH = REPO_ROOT / "README.md"


class RequirementsWorkshopProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.skill = SKILL_PATH.read_text(encoding="utf-8")

    def test_requires_numbered_rounds_and_compact_replies(self) -> None:
        self.assertIn("第 x 轮/共 y 轮", self.skill)
        self.assertIn("1B, 2D", self.skill)
        self.assertIn("1E: <custom answer>", self.skill)

    def test_requires_option_and_confirmation_protocol(self) -> None:
        self.assertIn("其他（请说明）", self.skill)
        self.assertIn("Confirmed so far", self.skill)
        self.assertIn("基本需求已确认完毕。请确认是否还有需要补充的需求？", self.skill)

    def test_prevents_implementation_before_confirmation(self) -> None:
        self.assertIn("Do not begin implementation until", self.skill)

    def test_returns_to_the_authorized_task_without_a_prd(self) -> None:
        self.assertIn("start the originally requested planning or implementation output", self.skill)
        self.assertIn("Generate a PRD only when the user explicitly requests one", self.skill)
        self.assertIn("PRD-[product-name].md", self.skill)


class RepositoryStructureTests(unittest.TestCase):
    def test_plugin_manifest_has_release_metadata(self) -> None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

        self.assertRegex(manifest["version"], r"^\d+\.\d+\.\d+$")
        self.assertEqual(manifest["author"]["name"], "Cherys")
        self.assertNotEqual(manifest["interface"]["developerName"], "Local developer")
        self.assertEqual(manifest["license"], "MIT")
        self.assertEqual(manifest["repository"], "https://github.com/ChrysFu-FndVent/requirements-workshop")
        self.assertIn("requirements-engineering", manifest["keywords"])

    def test_marketplace_entry_resolves_to_plugin(self) -> None:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
        entry = next(item for item in marketplace["plugins"] if item["name"] == "requirements-workshop")
        relative_path = entry["source"]["path"].removeprefix("./")

        self.assertEqual(entry["policy"]["installation"], "AVAILABLE")
        self.assertEqual(entry["policy"]["authentication"], "ON_INSTALL")
        self.assertEqual((REPO_ROOT / relative_path).resolve(), PLUGIN_ROOT.resolve())
        self.assertTrue(MANIFEST_PATH.is_file())

    def test_repository_has_license_and_ci(self) -> None:
        self.assertTrue((REPO_ROOT / "LICENSE").is_file())
        self.assertTrue((REPO_ROOT / ".github" / "workflows" / "ci.yml").is_file())

    def test_readme_installation_is_portable(self) -> None:
        readme = README_PATH.read_text(encoding="utf-8")

        self.assertIn('codex plugin marketplace add "$PWD"', readme)
        self.assertIn(
            "codex plugin add requirements-workshop@requirements-workshop-marketplace",
            readme,
        )
        self.assertNotIn("/Users/", readme)

    def test_repository_does_not_name_an_external_prd_skill(self) -> None:
        text_files = (
            README_PATH,
            SKILL_PATH,
            *sorted((REPO_ROOT / "docs").glob("*.md")),
            *sorted((REPO_ROOT / "examples").glob("*.md")),
        )

        for path in text_files:
            with self.subTest(path=path.relative_to(REPO_ROOT)):
                self.assertNotIn("create-prd", path.read_text(encoding="utf-8"))

    def test_examples_and_evidence_docs_exist(self) -> None:
        for relative_path in (
            "examples/new-app.md",
            "examples/existing-feature.md",
            "examples/external-integration.md",
            "docs/direct-coding-vs-workshop.md",
            "docs/text-to-app-agent-workflow.md",
            "docs/metrics.md",
        ):
            with self.subTest(relative_path=relative_path):
                self.assertTrue((REPO_ROOT / relative_path).is_file())


if __name__ == "__main__":
    unittest.main()
