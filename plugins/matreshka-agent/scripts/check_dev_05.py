#!/usr/bin/env python3
"""Deterministic integrity check for the unreleased Matreshka Agent 0.5 track.

Read-only and offline. This proves that intended development contracts/assets
exist and that major controller seams are wired through planning, dispatch,
review, verification, finish, recovery and observability. It does not claim
native host behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True


PLUGIN_REQUIRED_FILES = (
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
    "skills/orchestrating-subagent-work/assets/task-brief-template.md",
    "skills/orchestrating-subagent-work/assets/dispatch-templates.md",
    "skills/orchestrating-subagent-work/assets/agent-report-template.md",
    "skills/orchestrating-subagent-work/assets/ledger-template.md",
    "skills/orchestrating-subagent-work/assets/project-profile-template.md",
    "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json",
    "skills/finishing-development-work/assets/finish-handoff-template.md",
)

PLUGIN_MARKERS = {
    "skills/building-end-to-end/SKILL.md": (
        "INTERVIEW", "ASSISTED", "FULL_AUTO", "CONTINUE_PROJECT", "EXISTING_PROJECT",
        "SOURCE_BRIEF", "matreshka-agent:orchestrating-subagent-work",
    ),
    "skills/orchestrating-subagent-work/SKILL.md": (
        "PROJECT_TOPOLOGY", "AREA_CONTEXT_SET", "IC-", "RUNTIME_MAP",
        "documentation drift", "specialist", "G4",
    ),
    "skills/orchestrating-subagent-work/references/controller-contract.md": (
        "Project Topology gate", "AREA_CONTEXT_SET", "INTERFACE_CHANGED",
        "DOCS_UPDATE_REQUIRED", "Browser/E2E capability gate", "G4",
    ),
    "skills/orchestrating-subagent-work/references/permission-handoff-ledger.md": (
        "Documentation writes", "Browser interaction", "Local process/runtime",
        "Destructive E2E setup", "Project Intelligence",
    ),
    "skills/orchestrating-subagent-work/references/project-profile.md": (
        "PROJECT_TOPOLOGY", "RUNTIME_MAP", "AREA_CONTEXT_SET", ".matreshka/project-profile.md",
    ),
    "skills/planning-software-work/SKILL.md": (
        "Project Topology", "AREA_CONTEXT_SET", "IC-", "RUNTIME_MAP",
        "documentation impact", "Specialist routing",
    ),
    "skills/reviewing-agent-work/SKILL.md": (
        "frozen cross-area", "IC-", "source-intent narrowing", "specialist",
    ),
    "skills/verifying-development-work/SKILL.md": (
        "browser", "Blind user-intent acceptance", "technical/security", "G4",
    ),
    "skills/finishing-development-work/SKILL.md": (
        "documentation drift", "Project Intelligence", "DOCS_NOT_REQUIRED", "DOCS_CURRENT",
    ),
    "skills/orchestrating-subagent-work/assets/task-brief-template.md": (
        "Project Intelligence routing", "AREA_CONTEXT_SET", "INTERFACE_CHANGED",
        "Role-specific boundary", "Documentation impact",
    ),
    "skills/orchestrating-subagent-work/assets/dispatch-templates.md": (
        "Documentation maintainer", "Execution-only operator", "AREA_CONTEXT_SET",
        "IC-xx", "Role:",
    ),
    "skills/orchestrating-subagent-work/assets/agent-report-template.md": (
        "Role archetype", "Primary area", "Cross-area contracts",
        "Documentation impact candidate", "Runtime ownership/status issue",
    ),
    "skills/orchestrating-subagent-work/assets/project-intelligence-template.md": (
        "Project topology", "Area context index", "Cross-area interfaces",
        "Runtime map", "Specialist routing", "Documentation drift",
    ),
    "skills/orchestrating-subagent-work/assets/interface-contract-template.md": (
        "Producer area", "Consumer areas", "Contract identity/hash",
        "Failure semantics", "Delivery semantics", "Integration/contract proof",
    ),
    "skills/orchestrating-subagent-work/assets/ledger-template.md": (
        "## Project Intelligence", "Documentation drift state", "Current specialist archetype",
        "Token usage status", "Browser / E2E verification", "Interface-contract mismatch",
    ),
    "skills/finishing-development-work/assets/finish-handoff-template.md": (
        "Итоговый статус", "Project Intelligence", "Documentation drift gate",
        "Общее время", "Токены",
    ),
    "skills/building-end-to-end/assets/dashboard-template.html": (
        "Общий прогресс", "Общее время", "Токены", "Карта проекта",
        "Техническая проверка", "Независимая приёмка G4", "s.intelligence",
    ),
    "skills/building-end-to-end/assets/dashboard-state-template.js": (
        '"timing"', '"usage"', '"intelligence"', '"tests"', '"browser"',
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

MARKETPLACE_REQUIRED_FILES = (
    "README.md",
    ".github/workflows/package-validation.yml",
    "docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md",
    "docs/plans/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-plan.md",
    "docs/specs/2026-08-20-matreshka-agent-0.5-browser-e2e-spec.md",
    "docs/plans/2026-08-20-matreshka-agent-0.5-browser-e2e-plan.md",
    "docs/specs/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-spec.md",
    "docs/plans/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-plan.md",
)

MARKETPLACE_MARKERS = {
    "README.md": (
        "0.5 development track", "FULL_AUTO", "Project Intelligence Layer",
        "Browser E2E + Browser G4", "check_dev_05.py",
    ),
    ".github/workflows/package-validation.yml": (
        "validate_package.py", "check_dev_05.py", "doctor.py", "python-version: '3.11'",
    ),
    "docs/plans/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-plan.md": (
        "IMPLEMENTED_PENDING_NATIVE_RELEASE_VALIDATION", "T5", "STATIC_HARDENING_IMPLEMENTED",
    ),
    "docs/plans/2026-08-20-matreshka-agent-0.5-browser-e2e-plan.md": (
        "IMPLEMENTED_PENDING_NATIVE_VALIDATION", "B1", "B7", "B8", "PENDING_NATIVE",
    ),
    "docs/plans/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-plan.md": (
        "IMPLEMENTED_PENDING_NATIVE_VALIDATION", "P1", "P6", "P7", "P8",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Matreshka Agent 0.5 development-track integrity.")
    parser.add_argument(
        "plugin_path", nargs="?", default=str(Path(__file__).resolve().parent.parent),
        help="Plugin root; defaults to the parent of this scripts directory.",
    )
    parser.add_argument(
        "--marketplace-root",
        help="Repository root; inferred from plugins/<name> when omitted.",
    )
    return parser.parse_args()


def infer_marketplace_root(plugin_root: Path) -> Path:
    if plugin_root.parent.name == "plugins":
        return plugin_root.parent.parent.resolve()
    return plugin_root.resolve()


def read(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.append(f"READ {path}: {exc}")
        return ""


def require_files(root: Path, files: tuple[str, ...], prefix: str, failures: list[str]) -> None:
    for relative in files:
        if not (root / relative).is_file():
            failures.append(f"MISSING {prefix}{relative}")


def require_markers(root: Path, mapping: dict[str, tuple[str, ...]], prefix: str, failures: list[str]) -> None:
    for relative, markers in mapping.items():
        text = read(root / relative, failures)
        for marker in markers:
            if marker.casefold() not in text.casefold():
                failures.append(f"MARKER {prefix}{relative}: missing {marker!r}")


def main() -> int:
    args = parse_args()
    plugin_root = Path(args.plugin_path).expanduser().resolve()
    marketplace_root = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root else infer_marketplace_root(plugin_root)
    )
    failures: list[str] = []

    require_files(plugin_root, PLUGIN_REQUIRED_FILES, "plugin/", failures)
    require_markers(plugin_root, PLUGIN_MARKERS, "plugin/", failures)
    require_files(marketplace_root, MARKETPLACE_REQUIRED_FILES, "repo/", failures)
    require_markers(marketplace_root, MARKETPLACE_MARKERS, "repo/", failures)

    for relative in JSON_FILES:
        text = read(plugin_root / relative, failures)
        if not text:
            continue
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(f"JSON plugin/{relative}: line {exc.lineno}, column {exc.colno}: {exc.msg}")

    build_prompt = read(plugin_root / "codex-prompts/matreshka-build.md", failures)
    if 'argument-hint: "[TASK]"' not in build_prompt:
        failures.append("CODEX build wrapper must keep validator-compatible [TASK] argument hint")
    if "$$matreshka-agent:building-end-to-end" not in build_prompt:
        failures.append("CODEX build wrapper must route to namespaced Matreshka Build End-to-End")

    openai_yaml = read(plugin_root / "skills/building-end-to-end/agents/openai.yaml", failures)
    if "$building-end-to-end" not in openai_yaml:
        failures.append("Codex skill card must preserve the canonical skill token")
    if "$matreshka-agent:building-end-to-end" not in openai_yaml:
        failures.append("Codex skill card must show the namespaced Matreshka invocation")
    for public_word in ("interview", "assisted", "full-auto", "continue-project", "existing-project"):
        if public_word not in openai_yaml:
            failures.append(f"Codex skill card is missing public launch hint {public_word!r}")

    pi_evals_path = plugin_root / "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json"
    try:
        pi_payload = json.loads(pi_evals_path.read_text(encoding="utf-8"))
        cases = pi_payload.get("evals", []) if isinstance(pi_payload, dict) else []
        if len(cases) < 14:
            failures.append("Project Intelligence adversarial suite must contain at least 14 cases")
        ids = {str(case.get("id")) for case in cases if isinstance(case, dict)}
        required_ids = {
            "pi-topology-fullstack", "pi-topology-cli-no-fake-split", "pi-interface-freeze",
            "pi-interface-change-mid-run", "pi-context-router", "pi-runtime-unknown-port-owner",
            "pi-runtime-observe-not-start", "pi-docs-public-contract-drift", "pi-docs-private-refactor",
            "pi-ui-specialist-boundary", "pi-specialists-no-budget-inflation", "pi-operator-execute-only",
            "pi-recovery-stale-cache", "pi-docs-conflict-no-authority",
        }
        missing_ids = sorted(required_ids - ids)
        if missing_ids:
            failures.append(f"Project Intelligence eval coverage missing: {', '.join(missing_ids)}")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"Project Intelligence eval suite unreadable: {exc}")

    state_text = read(plugin_root / "skills/building-end-to-end/assets/dashboard-state-template.js", failures)
    html_text = read(plugin_root / "skills/building-end-to-end/assets/dashboard-template.html", failures)
    dashboard_contract = {
        "intelligence": "s.intelligence",
        "timing": "s.timing",
        "usage": "s.usage",
        "tests": "s.tests",
        "browser": "s.browser",
        "authority": "s.authority",
    }
    for state_key, html_marker in dashboard_contract.items():
        if f'"{state_key}"' not in state_text or html_marker not in html_text:
            failures.append(f"DASHBOARD contract mismatch for {state_key}: state/html are not both wired")

    if failures:
        print(f"Matreshka 0.5 development integrity: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Matreshka 0.5 development integrity: PASS")
    print("- launch modes/scenarios: present and Codex-routed")
    print("- source brief + U/S + G1-G4: present")
    print("- Russian dashboard + state/timing/tokens: wired")
    print("- Browser/E2E: wired through controller/verifier/dashboard")
    print("- Project Intelligence P1-P6: wired through controller/planner/task/review/finish/recovery")
    print("- task/dispatch/report/handoff templates: wired")
    print("- Project Intelligence adversarial coverage: 14 required cases present")
    print("- plans/README/CI development-track markers: present")
    print("Native host behavior is intentionally outside this static check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
