import json
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CORE = {
    "code-essence",
    "architecture-essence",
    "decision-essence",
    "validation-essence",
}
BUNDLES = {
    "core": CORE,
    "sre": {"incident-essence", "root-cause-essence", "security-essence"},
    "product": {
        "user-need-essence",
        "metrics-essence",
        "risk-essence",
        "roi-essence",
    },
}
EXTRAS = {"stock-essence", "game-design-essence"}


class EssenceDataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_payload = False
        self.payload = []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if (
            tag == "script"
            and attributes.get("type") == "application/json"
            and attributes.get("id") == "essence-data"
        ):
            self.in_payload = True

    def handle_endtag(self, tag):
        if tag == "script" and self.in_payload:
            self.in_payload = False

    def handle_data(self, data):
        if self.in_payload:
            self.payload.append(data)


def validate_output(output, schema):
    assert set(output) == set(schema["required"])
    assert output["skill"] in schema["properties"]["skill"]["enum"]
    assert isinstance(output["summary"], str) and output["summary"].strip()
    assert isinstance(output["open_questions"], list)
    for item in output["verified_facts"]:
        assert set(item) == {"category", "statement", "evidence"}
        assert item["statement"].strip() and item["evidence"]
        for evidence in item["evidence"]:
            assert set(evidence) == {"source", "location", "quote"}
            assert evidence["source"] and evidence["location"]
    for item in output["unverified_assumptions"]:
        assert set(item) == {"statement", "why_unverified"}
        assert item["statement"] and item["why_unverified"]
    for item in output["residual_risks"]:
        assert set(item) == {"statement", "severity", "evidence"}
        assert item["statement"] and item["evidence"]
        assert item["severity"] in {"low", "medium", "high", "unknown"}
    for item in output["recommended_actions"]:
        assert set(item) == {"action", "status", "owner"}
        assert item["action"]
        assert item["status"] in {
            "proposed",
            "in_progress",
            "completed",
            "unknown",
        }


def cited_lines(location, raw_lines):
    line_numbers = []
    for first, last in re.findall(r"(\d+)(?:-(\d+))?", location):
        start = int(first)
        end = int(last) if last else start
        line_numbers.extend(range(start, end + 1))
    assert line_numbers
    assert all(1 <= line <= len(raw_lines) for line in line_numbers)
    return "\n".join(raw_lines[line - 1] for line in line_numbers)


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema = json.loads(
            (ROOT / "schemas" / "essence-output.schema.json").read_text(
                encoding="utf-8"
            )
        )

    def test_sample_output_matches_contract_and_quotes_source(self):
        output = json.loads(
            (ROOT / "samples" / "incident-output.json").read_text(encoding="utf-8")
        )
        raw_lines = (
            ROOT / "samples" / "incident-raw.log"
        ).read_text(encoding="utf-8").splitlines()
        validate_output(output, self.schema)
        self.assertEqual(len(raw_lines), 50)
        self.assertEqual(output["skill"], "incident-essence")
        for fact in output["verified_facts"]:
            for evidence in fact["evidence"]:
                self.assertIn(
                    evidence["quote"], cited_lines(evidence["location"], raw_lines)
                )

    def test_html_report_contains_the_same_machine_payload(self):
        output = json.loads(
            (ROOT / "samples" / "incident-output.json").read_text(encoding="utf-8")
        )
        report = (ROOT / "samples" / "incident-report.html").read_text(
            encoding="utf-8"
        )
        parser = EssenceDataParser()
        parser.feed(report)
        self.assertEqual(json.loads("".join(parser.payload)), output)
        self.assertIn("<svg", report)
        self.assertIn("three.module.js", report)
        for heading in (
            "Verified facts",
            "Unverified assumptions",
            "Residual risks",
            "Recommended actions",
            "Open questions",
        ):
            self.assertIn(heading, report)

    def test_all_skills_declare_the_shared_contract(self):
        skills = list((ROOT / ".claude" / "skills").glob("*/SKILL.md"))
        skills += list((ROOT / "extras" / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 20)
        for path in skills:
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding="utf-8")
                self.assertIn("verified_facts", text)
                self.assertIn("residual_risks", text)
                self.assertIn("HTML5 report", text)
                self.assertIn("application/json", text)
                self.assertIn("Three.js", text)

    def test_repo_skills_require_line_citations_and_native_tools(self):
        for skill in ("code-essence", "architecture-essence"):
            text = (
                ROOT / ".claude" / "skills" / skill / "SKILL.md"
            ).read_text(encoding="utf-8")
            for required in ("Read", "Grep", "Glob", "line number"):
                self.assertIn(required, text)

    def test_bundle_membership_and_extras_layout(self):
        all_bundled = set().union(*BUNDLES.values())
        self.assertEqual(len(all_bundled), 11)
        self.assertEqual(len(all_bundled & CORE), 4)
        installer = (ROOT / "scripts" / "install.mjs").read_text(encoding="utf-8")
        for bundle in BUNDLES.values():
            for skill in bundle:
                self.assertIn(f'"{skill}"', installer)
        for skill in EXTRAS:
            self.assertTrue(
                (ROOT / "extras" / "skills" / skill / "SKILL.md").is_file()
            )
            self.assertIn(f'"{skill}"', installer)

    def test_incident_golden_keeps_unsupported_claims_out(self):
        cases = json.loads(
            (ROOT / "tests" / "eval-cases.json").read_text(encoding="utf-8")
        )
        incident_case = next(
            case for case in cases if case["id"] == "route-incident-evidence"
        )
        output = (
            ROOT / "samples" / "incident-output.json"
        ).read_text(encoding="utf-8").lower()
        for unsupported_claim in incident_case["must_not_claim"]:
            self.assertNotIn(unsupported_claim.lower(), output)
        self.assertIn('"severity": "unknown"', output)
        self.assertIn('"why_unverified"', output)

    def test_route_eval_cases_target_existing_skills(self):
        cases = json.loads(
            (ROOT / "tests" / "eval-cases.json").read_text(encoding="utf-8")
        )
        master = (
            ROOT / ".claude" / "skills" / "master-essence" / "SKILL.md"
        ).read_text(encoding="utf-8")
        self.assertGreaterEqual(len(cases), 4)
        for case in cases:
            with self.subTest(case=case["id"]):
                skill = case["expected_skill"]
                self.assertRegex(master, re.escape(skill))
                self.assertTrue(case["must_not_claim"])
                self.assertIn(skill, self.schema["properties"]["skill"]["enum"])


if __name__ == "__main__":
    unittest.main()
