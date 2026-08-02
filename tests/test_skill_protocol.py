"""Verify the Requirements Workshop interaction contract.

This intentionally uses only the Python standard library so anyone cloning the
plugin can confirm that the documented discussion protocol remains intact.
"""

from __future__ import annotations

from pathlib import Path
import unittest


SKILL_PATH = Path(__file__).parents[1] / "skills" / "requirements-workshop" / "SKILL.md"


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

    def test_hands_confirmed_product_requirements_to_create_prd(self) -> None:
        self.assertIn("invoke `create-prd` after confirmation", self.skill)
        self.assertIn("do not repeat discovery questions", self.skill)
        self.assertIn("PRD-[product-name].md", self.skill)
        self.assertIn("as `TBD` rather than inventing them", self.skill)

    def test_uses_prd_first_and_workshop_record_for_details(self) -> None:
        self.assertIn("treat it as the primary requirements source", self.skill)
        self.assertIn("review the complete `requirements-workshop` discussion", self.skill)
        self.assertIn("a later explicit user instruction overrides the PRD", self.skill)
        self.assertIn("do not infer missing details from the PRD", self.skill)


if __name__ == "__main__":
    unittest.main()
