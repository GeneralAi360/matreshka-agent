#!/usr/bin/env python3
"""Offline bootstrap contract regressions; temporary fixtures only, no runtimes."""
from __future__ import annotations

import copy
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True
CHECKER = Path(__file__).with_name("check_project_bootstrap.py")


class BootstrapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.assertTrue(CHECKER.is_file(), "bootstrap checker is not implemented")
        spec = importlib.util.spec_from_file_location("bootstrap_check", CHECKER)
        self.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.module)
        self.data = {
            "schema_version": 1,
            "profile": "split",
            "source": "docs/architecture.md",
            "documents": {"architecture": "docs/architecture.md", "testing": "docs/testing.md",
                          "local_development": "docs/local-development.md"},
            "decisions": {"frontend": "React", "backend": "Python API",
                          "database": "PostgreSQL", "hosting": "UNRESOLVED"},
            "areas": {"frontend": ["apps/frontend"], "backend": ["apps/backend"]},
            "migration_roots": ["apps/backend/db/migrations"],
            "files": ["AGENTS.md", "README.md", "docs/architecture.md",
                      "docs/local-development.md", "docs/testing.md"],
            "checks": [self.check("front", "frontend", "browser"),
                       self.check("logic", "backend", "unit"),
                       self.check("api", "backend", "integration")],
        }
        for name in self.data["files"]:
            self.write(name, "# Project\n")
        for name in ["apps/frontend", "apps/backend", "apps/backend/db/migrations"]:
            (self.root / name).mkdir(parents=True, exist_ok=True)

    @staticmethod
    def check(key, owner, layer):
        return {"id": key, "owner": owner, "layer": layer, "status": "PLANNED",
                "cwd": "apps/" + owner, "command": [], "command_source": None,
                "target": "isolated test environment pending", "prerequisites": "runtime pending",
                "scenario": "observable behavior required by spec", "reason": "runner not chosen"}

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def result(self):
        self.write("docs/bootstrap.json", json.dumps(self.data))
        return self.module.validate(self.root, "docs/bootstrap.json")

    def test_mixed_stack_provider_unknown_valid_but_runtime_unverified(self):
        r = self.result()
        self.assertEqual(r["errors"], [])
        self.assertEqual(r["runtime"], "NOT_VERIFIED")
        self.assertFalse((self.root / "supabase").exists())

    def test_required_backend_missing(self):
        del self.data["areas"]["backend"]
        self.assertIn("areas:backend", self.result()["errors"])

    def test_backend_tests_cannot_be_replaced_by_browser(self):
        self.data["checks"] = self.data["checks"][:1]
        self.assertIn("coverage:backend:integration", self.result()["errors"])

    def test_api_tests_do_not_satisfy_browser(self):
        self.data["checks"][0]["layer"] = "api"
        self.assertIn("coverage:frontend:browser", self.result()["errors"])

    def test_fullstack_maps_server_modules(self):
        self.data["profile"] = "fullstack"
        self.data["areas"] = {"frontend": ["apps/frontend"], "backend": ["apps/frontend"]}
        self.assertEqual(self.result()["errors"], [])

    def test_backend_only_needs_no_frontend(self):
        self.data["profile"] = "backend"
        del self.data["areas"]["frontend"]
        self.data["checks"] = self.data["checks"][1:]
        self.assertEqual(self.result()["errors"], [])

    def test_static_requires_no_manifests_database_or_backend(self):
        self.data["profile"] = "static"
        self.data["decisions"].update(backend="NONE", database="NONE")
        self.data["areas"] = {"frontend": ["apps/frontend"]}
        self.data["migration_roots"] = []
        self.data["checks"] = self.data["checks"][:1]
        self.assertEqual(self.result()["errors"], [])

    def test_managed_service_needs_backend_contract_tests(self):
        self.data["profile"] = "managed"
        self.data["areas"]["backend"] = ["docs/architecture.md"]
        self.assertEqual(self.result()["errors"], [])

    def test_missing_file_rejected(self):
        self.data["files"].append("docs/missing.md")
        self.assertTrue(any("missing" in x for x in self.result()["errors"]))

    def test_missing_command_source_rejected(self):
        self.data["checks"][1].update(command=["python", "-m", "unittest"],
                                     command_source="missing.md")
        self.assertTrue(self.result()["errors"])

    def test_npm_script_must_exist_and_is_never_executed(self):
        self.write("apps/frontend/package.json", json.dumps({"scripts": {"test": "exit 93"}}))
        row = self.data["checks"][0]
        row.update(command=["npm.cmd", "run", "missing"],
                   command_source="apps/frontend/package.json")
        self.assertIn("script:front", self.result()["errors"])
        row["command"][-1] = "test"
        self.assertEqual(self.result()["errors"], [])

    def test_traversal_absolute_and_sensitive_references_rejected(self):
        for name in ["../outside.md", "/etc/passwd", "C:/private.txt", ".env",
                     "apps/backend/.env.local", ".git/config", "private.pem"]:
            with self.subTest(name=name):
                self.data["files"] = [name]
                self.assertTrue(self.result()["errors"])

    def test_symlink_cannot_escape(self):
        with tempfile.TemporaryDirectory() as outside:
            external = Path(outside) / "outside.md"
            external.write_text("private", encoding="utf-8")
            try:
                (self.root / "escape.md").symlink_to(external)
            except OSError:
                self.skipTest("host cannot create a symlink; CI must exercise this case")
            self.data["files"].append("escape.md")
            self.assertTrue(self.result()["errors"])

    def test_zero_tests_and_skipped_only_cannot_be_pass(self):
        row = self.data["checks"][0]
        row.update(status="PASSED", command=["runner", "test"],
                   command_source="docs/testing.md", passed=0, failed=0, skipped=4,
                   exit=0, baseline="fixture-v1", evidence="docs/testing.md")
        self.assertIn("proof:front", self.result()["errors"])

    def test_complete_claim_is_still_not_runtime_verification(self):
        row = self.data["checks"][0]
        row.update(status="PASSED", command=["runner", "test"],
                   command_source="docs/testing.md", passed=1, failed=0, skipped=0,
                   exit=0, baseline="fixture-v1", evidence="docs/testing.md")
        r = self.result()
        self.assertEqual(r["errors"], [])
        self.assertEqual(r["runtime"], "NOT_VERIFIED")

    def test_duplicate_ids_and_migration_owners_rejected(self):
        self.data["checks"].append(copy.deepcopy(self.data["checks"][0]))
        self.data["migration_roots"].append("apps/backend/db/migrations")
        errors = self.result()["errors"]
        self.assertIn("duplicate:check-id", errors)
        self.assertIn("duplicate:migration-root", errors)

    def test_na_requires_reason(self):
        for reason in [None, False, {}, "", "  "]:
            with self.subTest(reason=reason):
                self.data["checks"][1].update(status="NOT_APPLICABLE", reason=reason)
                self.assertIn("reason:logic", self.result()["errors"])

    def test_required_documentation_cannot_be_omitted(self):
        self.data["files"].remove("docs/testing.md")
        (self.root / "docs/testing.md").unlink()
        self.assertTrue(self.result()["errors"])
        del self.data["documents"]["testing"]
        self.assertTrue(self.result()["errors"])

    def test_existing_equivalent_documentation_allowed(self):
        self.write("handbook/checks.md", "# Existing test instructions\n")
        self.data["documents"]["testing"] = "handbook/checks.md"
        self.data["files"].remove("docs/testing.md")
        self.data["files"].append("handbook/checks.md")
        self.assertEqual(self.result()["errors"], [])

    def test_malformed_input_is_clean_failure(self):
        for value in [[], {"schema_version": 1}, None, "bad"]:
            self.write("docs/bootstrap.json", json.dumps(value))
            r = self.module.validate(self.root, "docs/bootstrap.json")
            self.assertEqual(r["status"], "INVALID")

    def test_cli_exit_and_read_only_repeatability(self):
        self.result()
        before = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        for _ in range(2):
            p = subprocess.run([sys.executable, "-B", str(CHECKER), "--project", str(self.root)],
                               capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(p.returncode, 0, p.stdout + p.stderr)
            self.assertEqual(json.loads(p.stdout)["runtime"], "NOT_VERIFIED")
        after = {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main(verbosity=2)
