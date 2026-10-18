"""Cross-skill entry contracts: these assertions must fail on the old run-only system."""
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class EntryContractTests(unittest.TestCase):
    def test_build_report_is_mandatory(self):
        text = (ROOT / 'skills/building-end-to-end/SKILL.md').read_text(encoding='utf-8')
        self.assertNotIn('Dashboard is controller-owned and optional', text)
        self.assertIn('project-reporting.md', text)

    def test_direct_skill_entrypoints_share_project_lifecycle(self):
        for path in sorted((ROOT / 'skills').glob('*/SKILL.md')):
            with self.subTest(skill=path.parent.name):
                text = path.read_text(encoding='utf-8')
                self.assertIn('project-reporting.md', text)
                self.assertIn('read-only', text)

if __name__ == '__main__':
    unittest.main()
