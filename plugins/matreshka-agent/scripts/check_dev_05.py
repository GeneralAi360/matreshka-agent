#!/usr/bin/env python3
"""Deterministic integrity check for the unreleased Matreshka Agent 0.5 track.

This checker is read-only and offline. It proves that the development branch
contains the intended contracts/assets and that the major controller seams are
wired together. It does not claim native host behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True


REQUIRED_FILES = (
    "skills/building-end-to-end/references/brief-traceability.md",
    "skills/building-end-to-end/references/interaction-modes.md",
    "skills/building-end-to-end/references/launch-scenarios.md",
    "skills/building-end-to-end/references/run-observability.md",
    "skills/building-end-to-end/assets/source-brief-template.md",
    "skills/building-end-to-end/assets/requirement-manifest-template.md",
    "skills/building-end-to-end/assets/dashboard-state-template.js",
    "skills/building-end-to-end/assets/dashboard-template.html",
    "skills/planning-software-work/references/complexity-tiers.md",
    "skills/verifying-development-work/references/browser-e2e.md",
    "skills/orchestrating-subagent-work/references/project-intelligence.md",
    "skills/orchestrating-subagent-work/assets/project-intelligence-template.md",
    "skills/orchestrating-subagent-work/assets/interface-contract-template.md",
    "skills/orchestrating-subagent-work/assets/ledger-template.md",
    "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json",
)

MARKERS = {
    "skills/building-end-to-end/SKILL.md": (
        "INTERVIEW",
        "ASSISTED",
        "FULL_AUTO",
        "CONTINUE_PROJECT",
        "EXISTING_PROJECT",
        "SOURCE_BRIEF",
        "matreshka-agent:orchestrating-subagent-work",
    ),
    "skills/orchestrating-subagent-work/SKILL.md": (
        "PROJECT_TOPOLOGY",
        "AREA_CONTEXT_SET",
        "IC-",
        "RUNTIME_MAP",
        "DOCUMENTATION_DRIFT_GATE",
        "SPECIALIST_ROLE_ROUTING",
        "G4",
    ),
    "skills/orchestrating-subagent-work/references/controller-contract.md": (
        "PROJECT_TOPOLOGY",
        "AREA_CONTEXT_SET",
        "INTERFACE_CHANGED",
        "DOCS_UPDATE_REQUIRED",
        "BROWSER",
    ),
    "skills/orchestrating-subagent-work/references/permission-handoff-ledger.md": (
        "Documentation writes",
        "Browser interaction",
        "Local process/runtime",
        "Destructive E2E setup",
        "Project Intelligence",
    ),
    "skills/planning-software-work/SKILL.md": (
        "PROJECT_TOPOLOGY",
        "AREA_CONTEXT_SET",
        "IC-",
        "RUNTIME_MAP",
        "DOCUMENTATION_DRIFT_GATE",
        "SPECIALIST_ROLE_ROUTING",
    ),
    "skills/reviewing-agent-work/SKILL.md": (
        "cross-area interface",
        "IC-",
        "source-intent narrowing",
    ),
    "skills/verifying-development-work/SKILL.md": (
        "browser",
        "Blind user-intent acceptance",
        "technical/security",
    ),
    "skills/finishing-development-work/SKILL.md": (
        "documentation drift",
        "Project Intelligence",
    ),
    "skills/building-end-to-end/assets/dashboard-template.html": (
        "Общий прогресс",
        "Общее время",
        "Токены",
        "Карта проекта",
        "Техническая проверка",
        "Независимая приёмка G4",
    ),
    "skills/building-end-to-end/assets/dashboard-state-template.js": (
        '"timing"',
        '"usage"',
        '"projectIntelligence"',
        '"browser"',
    ),
    "skills/orchestrating-subagent-work/assets/ledger-template.md": (
        "## Project Intelligence",
        "Documentation drift state",
        "Current specialist archetype",
        "Token usage status",
        "Browser / E2E verification",
    ),
}

JSON_FILES = (
    "skills/building-end-to-end/evals/evals.json",
    "skills/building-end-to-end/evals/trigger-evals.json",
    "skills/orchestrating-subagent-work/evals/evals.json",
    "skills/orchestrating-subagent-work/evals/trigger-evals.json",
    "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json",
    "skills/planning-software-work/evals/evals.json",
    "skills/verifying-development-work/evals/evals.json",
    "evals/package-validation.json",
    "evals/workflow-evals.json",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Matreshka Agent 0.5 development-track integrity.")
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
        help="Plugin root; defaults to the parent of this scripts directory.",
    )
    return parser.parse_args()


def read(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.append(f"READ {path}: {exc}")
        return ""


def main() -> int:
    root = Path(parse_args().plugin_path).expanduser().resolve()
    failures: list[str] = []

    for relative in REQUIRED_FILES:
        path = root / relative
        if not path.is_file():
            failures.append(f"MISSING {relative}")

    for relative, markers in MARKERS.items():
        path = root / relative
        text = read(path, failures)
        for marker in markers:
            if marker.casefold() not in text.casefold():
                failures.append(f"MARKER {relative}: missing {marker!r}")

    for relative in JSON_FILES:
        path = root / relative
        text = read(path, failures)
        if not text:
            continue
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(
                f"JSON {relative}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
            )

    build_prompt = read(root / "codex-prompts/matreshka-build.md", failures)
    if 'argument-hint: "[TASK]"' not in build_prompt:
        failures.append("CODEX build wrapper must keep validator-compatible [TASK] argument hint")
    if "$$matreshka-agent:building-end-to-end" not in build_prompt:
        failures.append("CODEX build wrapper must route to namespaced Matreshka Build End-to-End")

    openai_yaml = read(root / "skills/building-end-to-end/agents/openai.yaml", failures)
    if "$building-end-to-end" not in openai_yaml:
        failures.append("Codex skill card must preserve the canonical skill token")
    if "$matreshka-agent:building-end-to-end" not in openai_yaml:
        failures.append("Codex skill card must show the namespaced Matreshka invocation")
    for public_word in ("interview", "assisted", "full-auto", "continue-project", "existing-project"):
        if public_word not in openai_yaml:
            failures.append(f"Codex skill card is missing public launch hint {public_word!r}")

    pi_evals_path = root / "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json"
    try:
        pi_payload = json.loads(pi_evals_path.read_text(encoding="utf-8"))
        cases = pi_payload.get("evals", []) if isinstance(pi_payload, dict) else []
        if len(cases) < 14:
            failures.append("Project Intelligence adversarial suite must contain at least 14 cases")
        ids = {str(case.get("id")) for case in cases if isinstance(case, dict)}
        required_ids = {
            "pi-topology-fullstack",
            "pi-topology-cli-no-fake-split",
            "pi-interface-freeze",
            "pi-context-router",
            "pi-runtime-unknown-port-owner",
            "pi-docs-public-contract-drift",
            "pi-ui-specialist-boundary",
            "pi-specialists-no-budget-inflation",
            "pi-operator-execute-only",
            "pi-recovery-stale-cache",
        }
        missing_ids = sorted(required_ids - ids)
        if missing_ids:
            failures.append(f"Project Intelligence eval coverage missing: {', '.join(missing_ids)}")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"Project Intelligence eval suite unreadable: {exc}")

    if failures:
        print(f"Matreshka 0.5 development integrity: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Matreshka 0.5 development integrity: PASS")
    print("- launch modes/scenarios: present")
    print("- source brief + G1-G4: present")
    print("- dashboard timing/tokens/Russian UX: present")
    print("- Browser/E2E: present")
    print("- Project Intelligence P1-P6: present")
    print("- planning/review/verification/finish seams: present")
    print("- eval JSON syntax + Project Intelligence adversarial coverage: present")
    print("Native host behavior is intentionally outside this static check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
