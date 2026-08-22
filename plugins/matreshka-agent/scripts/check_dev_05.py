#!/usr/bin/env python3
"""Deterministic integrity check for the unreleased Matreshka Agent 0.5 track.

Read-only and offline. This proves that intended development contracts/assets
exist and that the major source-intent, Project Intelligence, Design
Intelligence, Browser/E2E, specification, planning, implementation, review,
verification, finish, recovery and observability seams remain statically
connected.

It deliberately does NOT claim native host behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

EXPECTED_SKILLS = {
    "building-end-to-end",
    "orchestrating-subagent-work",
    "designing-product-experience",
    "specifying-software-work",
    "planning-software-work",
    "writing-portable-agent-prompt",
    "implementing-with-tests",
    "debugging-systematically",
    "reviewing-agent-work",
    "verifying-development-work",
    "finishing-development-work",
}

EXPECTED_CODEX_WRAPPERS = {
    "matreshka-build.md",
    "matreshka-orchestrate.md",
    "matreshka-design.md",
    "matreshka-spec.md",
    "matreshka-plan.md",
    "matreshka-prompt.md",
    "matreshka-implement.md",
    "matreshka-debug.md",
    "matreshka-review.md",
    "matreshka-verify.md",
    "matreshka-finish.md",
}

PLUGIN_REQUIRED_FILES = (
    "README.md",
    "CHANGELOG.md",
    ".codex-plugin/plugin.json",
    "skills/building-end-to-end/SKILL.md",
    "skills/building-end-to-end/references/brief-traceability.md",
    "skills/building-end-to-end/references/interaction-modes.md",
    "skills/building-end-to-end/references/launch-scenarios.md",
    "skills/building-end-to-end/references/run-observability.md",
    "skills/building-end-to-end/assets/source-brief-template.md",
    "skills/building-end-to-end/assets/requirement-manifest-template.md",
    "skills/building-end-to-end/assets/dashboard-state-template.js",
    "skills/building-end-to-end/assets/dashboard-template.html",
    "skills/designing-product-experience/SKILL.md",
    "skills/designing-product-experience/agents/openai.yaml",
    "skills/designing-product-experience/references/design-core.md",
    "skills/designing-product-experience/references/design-intelligence.md",
    "skills/designing-product-experience/references/prototype-exploration.md",
    "skills/designing-product-experience/references/anti-slop.md",
    "skills/designing-product-experience/assets/design-contract-template.md",
    "skills/designing-product-experience/evals/evals.json",
    "skills/designing-product-experience/evals/trigger-evals.json",
    "skills/specifying-software-work/SKILL.md",
    "skills/specifying-software-work/assets/specification-template.md",
    "skills/planning-software-work/SKILL.md",
    "skills/planning-software-work/assets/implementation-plan-template.md",
    "skills/planning-software-work/references/complexity-tiers.md",
    "skills/implementing-with-tests/SKILL.md",
    "skills/implementing-with-tests/assets/implementation-report-template.md",
    "skills/reviewing-agent-work/SKILL.md",
    "skills/reviewing-agent-work/assets/review-report-template.md",
    "skills/verifying-development-work/SKILL.md",
    "skills/verifying-development-work/assets/verification-report-template.md",
    "skills/verifying-development-work/references/browser-e2e.md",
    "skills/finishing-development-work/SKILL.md",
    "skills/finishing-development-work/assets/finish-handoff-template.md",
    "skills/orchestrating-subagent-work/SKILL.md",
    "skills/orchestrating-subagent-work/references/controller-contract.md",
    "skills/orchestrating-subagent-work/references/permission-handoff-ledger.md",
    "skills/orchestrating-subagent-work/references/project-intelligence.md",
    "skills/orchestrating-subagent-work/references/design-intelligence.md",
    "skills/orchestrating-subagent-work/references/project-profile.md",
    "skills/orchestrating-subagent-work/assets/project-intelligence-template.md",
    "skills/orchestrating-subagent-work/assets/interface-contract-template.md",
    "skills/orchestrating-subagent-work/assets/task-brief-template.md",
    "skills/orchestrating-subagent-work/assets/dispatch-templates.md",
    "skills/orchestrating-subagent-work/assets/agent-report-template.md",
    "skills/orchestrating-subagent-work/assets/review-package-template.md",
    "skills/orchestrating-subagent-work/assets/ledger-template.md",
    "skills/orchestrating-subagent-work/assets/project-profile-template.md",
    "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json",
    "codex-prompts/matreshka-design.md",
    "scripts/validate_dev_05.py",
    "scripts/doctor_dev_05.py",
)

# NOTE: this map intentionally contains stable semantic marker strings instead of
# line numbers, so small wording/layout changes do not disable the contract gate.
PLUGIN_MARKERS = {
    "README.md": (
        "Design Intelligence Layer",
        "Одиннадцать bundled skills",
        "Apple-inspired design core",
        "DESIGN.md",
        "VISUAL DESIGN CHECK",
        "validate_dev_05.py",
        "doctor_dev_05.py",
    ),
    "CHANGELOG.md": (
        "Design Intelligence Layer",
        "designing-product-experience",
        "Apple-inspired Design Core",
        "DESIGN_DRIFT_GATE",
        "18 Design Intelligence adversarial evals",
        "IMPLEMENTED_PENDING_NATIVE_VALIDATION",
    ),
    ".codex-plugin/plugin.json": (
        "eleven portable skills",
        "durable UX/UI design contracts",
        "Design a coherent product experience",
    ),
    "skills/building-end-to-end/SKILL.md": (
        "INTERVIEW",
        "ASSISTED",
        "FULL_AUTO",
        "CONTINUE_PROJECT",
        "EXISTING_PROJECT",
        "SOURCE_BRIEF",
        "matreshka-agent:orchestrating-subagent-work",
        "DESIGN_RELEVANCE_SIGNAL",
        "designing-product-experience",
        "DESIGN.md",
    ),
    "skills/designing-product-experience/SKILL.md": (
        "DESIGN_CURRENT",
        "DESIGN_RECON_REQUIRED",
        "DESIGN_DIRECTION_REQUIRED",
        "DESIGN_READY_TO_SAVE",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "DESIGN_CONTEXT_SET",
        "PRODUCT_UI_LOCALE",
        "anti-slop",
        "open/expanded state",
        "DESIGN.md",
        "Apple-inspired",
    ),
    "skills/designing-product-experience/references/design-core.md": (
        "Purpose",
        "Agency",
        "Responsibility",
        "Familiarity",
        "Flexibility",
        "Simplicity",
        "Craft",
        "Delight",
        "Wayfinding",
        "Reduced motion",
    ),
    "skills/designing-product-experience/references/design-intelligence.md": (
        "DESIGN_RELEVANCE",
        "DESIGN_RECON",
        "DESIGN_CONTEXT_SET",
        "DESIGN_REVIEW",
        "VISUAL_DESIGN_CHECK",
        "DESIGN_DRIFT_GATE",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
    ),
    "skills/designing-product-experience/references/prototype-exploration.md": (
        "Default to **3** directions",
        "Real divergence",
        "Prototype isolation",
        "PRODUCT_UI_LOCALE",
        "anti-slop",
        "Layered/open control fidelity",
        "run ledger/state",
        "Picker behavior",
        "Promotion",
    ),
    "skills/designing-product-experience/references/anti-slop.md": (
        "Product-specific point of view",
        "Product UI language",
        "Dropdown / select / popover quality gate",
        "Content visible by default",
        "Prototype anti-slop pass",
        "Final review",
    ),
    "skills/designing-product-experience/assets/design-contract-template.md": (
        "# Product Design Contract",
        "Product UI locale",
        "Product personality and signature",
        "Product language and localization",
        "Select/Menu/Popover",
        "Open/expanded layered-control states",
        "Product copy follows the resolved `PRODUCT_UI_LOCALE`",
        "Anti-slop reminder",
        "Apple-inspired core reminder",
    ),
    "skills/specifying-software-work/SKILL.md": (
        "Design Intelligence",
        "frozen design identity",
        "DESIGN_READY_TO_SAVE",
        "DESIGN_CHANGED",
        "DESIGN_CONTEXT_SET",
        "DESIGN.md",
        "Security by Design",
    ),
    "skills/specifying-software-work/assets/specification-template.md": (
        "Design Intelligence reference",
        "Design identity/hash",
        "User-experience outcomes",
        "Design-critical constraints",
        "Visual Design Check",
        "DESIGN_CONTEXT_SET",
    ),
    "skills/orchestrating-subagent-work/SKILL.md": (
        "Project Intelligence",
        "Design Intelligence",
        "designing-product-experience",
        "DESIGN_CONTEXT_SET",
        "DESIGN.md",
        "VISUAL_DESIGN_CHECK",
        "DESIGN_DRIFT_GATE",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "G4",
        "DOCUMENTATION_DRIFT_GATE",
    ),
    "skills/orchestrating-subagent-work/references/controller-contract.md": (
        "Project Intelligence gates",
        "Design Intelligence gates",
        "DESIGN_CONTEXT_SET",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "Apple-inspired design-core gate",
        "Visual Design Verification gate",
        "Browser/E2E capability gate",
        "G4",
        "DOCS_UPDATE_REQUIRED",
    ),
    "skills/orchestrating-subagent-work/references/permission-handoff-ledger.md": (
        "Design contract writes",
        "Prototype writes",
        "Design visual evidence",
        "DESIGN_READY_TO_SAVE",
        "DESIGN_DRIFT",
        "Documentation writes",
        "Browser interaction",
        "Local process/runtime",
        "Destructive E2E setup",
        "Project Intelligence safety",
        "Design Intelligence safety",
    ),
    "skills/orchestrating-subagent-work/references/design-intelligence.md": (
        "PREFLIGHT",
        "SPECIFICATION",
        "PLAN",
        "REVIEW",
        "VERIFY",
        "FINISH",
        "RECOVERY",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "G4 isolation",
    ),
    "skills/orchestrating-subagent-work/references/project-intelligence.md": (
        "PROJECT_TOPOLOGY",
        "AREA_CONTEXT_SET",
        "RUNTIME_MAP",
        "DESIGN_CONTEXT_SET",
        "DESIGN_ENGINEER",
        "DESIGN_REVIEWER",
        "DESIGN.md",
        "Documentation drift",
    ),
    "skills/orchestrating-subagent-work/references/project-profile.md": (
        "PROJECT_TOPOLOGY",
        "RUNTIME_MAP",
        "AREA_CONTEXT_SET",
        ".matreshka/project-profile.md",
        "DESIGN.md",
        "DESIGN_CONTEXT_SET",
        "designing-product-experience",
    ),
    "skills/planning-software-work/SKILL.md": (
        "Project Topology",
        "AREA_CONTEXT_SET",
        "IC-",
        "RUNTIME_MAP",
        "documentation impact",
        "Specialist routing",
        "DESIGN_CONTEXT_SET",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "designing-product-experience",
    ),
    "skills/planning-software-work/assets/implementation-plan-template.md": (
        "Design Intelligence snapshot",
        "Design Intelligence routing",
        "Design identity",
        "Visual design check",
        "Design impact candidates",
        "DESIGN_CONTEXT_SET",
    ),
    "skills/implementing-with-tests/SKILL.md": (
        "AREA_CONTEXT_SET",
        "IC-xx",
        "DESIGN_CONTEXT_SET",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "DESIGN.md",
        "existing design system/components/primitives first",
    ),
    "skills/implementing-with-tests/assets/implementation-report-template.md": (
        "Project Intelligence boundary",
        "Design Intelligence boundary",
        "Design identity/hash used",
        "DESIGN_CONTEXT_SET",
        "Interface mismatch",
        "Design / documentation impact candidates",
        "Independent Design Review / Visual Design Check",
    ),
    "skills/orchestrating-subagent-work/assets/review-package-template.md": (
        "Project Intelligence boundary",
        "Design Intelligence boundary",
        "DESIGN_CONTEXT_SET",
        "DESIGN_REVIEWER",
        "Apple-inspired core",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
    ),
    "skills/reviewing-agent-work/SKILL.md": (
        "frozen cross-area",
        "IC-",
        "source-intent narrowing",
        "Design Intelligence",
        "Apple-inspired",
        "DESIGN.md",
        "UNCHECKABLE",
    ),
    "skills/reviewing-agent-work/assets/review-report-template.md": (
        "Project Intelligence reviewed",
        "Design Intelligence reviewed",
        "Frozen design identity/hash",
        "Design consistency verdict",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "Apple-inspired core principles",
        "UNCHECKABLE",
    ),
    "skills/verifying-development-work/SKILL.md": (
        "Blind user-intent acceptance",
        "technical/security",
        "Visual design verification",
        "VISUAL_DESIGN_CHECK",
        "DESIGN_VERIFICATION",
        "DESIGN.md",
        "G4 must not",
        "browser",
    ),
    "skills/verifying-development-work/assets/verification-report-template.md": (
        "Technical/security status",
        "Project Intelligence evidence",
        "Automated Browser E2E",
        "Visual Design Check",
        "DESIGN_VERIFICATION",
        "Blind G4 handoff boundary",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
    ),
    "skills/finishing-development-work/SKILL.md": (
        "Design Intelligence",
        "DESIGN_DRIFT",
        "DESIGN_CURRENT",
        "DESIGN.md",
        "documentation drift",
        "DOCS_NOT_REQUIRED",
        "DOCS_CURRENT",
    ),
    "skills/orchestrating-subagent-work/assets/task-brief-template.md": (
        "Project Intelligence routing",
        "AREA_CONTEXT_SET",
        "INTERFACE_CHANGED",
        "Design Intelligence routing",
        "DESIGN_CONTEXT_SET",
        "DESIGN_CHANGED",
        "DESIGN_DRIFT",
        "Role-specific boundary",
        "Documentation impact",
    ),
    "skills/orchestrating-subagent-work/assets/dispatch-templates.md": (
        "Design engineer",
        "Design reviewer",
        "Documentation maintainer",
        "Execution-only operator",
        "AREA_CONTEXT_SET",
        "DESIGN_CONTEXT_SET",
        "IC-xx",
    ),
    "skills/orchestrating-subagent-work/assets/agent-report-template.md": (
        "Role archetype",
        "Primary area",
        "Cross-area contracts",
        "Design observations",
        "Design impact candidate",
        "Documentation impact candidate",
        "Runtime ownership/status issue",
    ),
    "skills/orchestrating-subagent-work/assets/project-intelligence-template.md": (
        "Project topology",
        "Area context index",
        "Cross-area interfaces",
        "Runtime map",
        "Specialist routing",
        "Documentation drift",
    ),
    "skills/orchestrating-subagent-work/assets/interface-contract-template.md": (
        "Producer area",
        "Consumer areas",
        "Contract identity/hash",
        "Failure semantics",
        "Delivery semantics",
        "Integration/contract proof",
    ),
    "skills/orchestrating-subagent-work/assets/ledger-template.md": (
        "## Project Intelligence",
        "## Design Intelligence",
        "Root design contract path",
        "Design review status",
        "Visual design check status",
        "Design drift gate",
        "Documentation drift state",
        "Token usage status",
        "Browser / E2E verification",
    ),
    "skills/finishing-development-work/assets/finish-handoff-template.md": (
        "Итоговый статус",
        "Project Intelligence",
        "Design Intelligence",
        "Root `DESIGN.md`",
        "Design Drift Gate",
        "Visual design check",
        "Documentation drift gate",
        "Общее время",
        "Токены",
    ),
    "skills/building-end-to-end/assets/dashboard-template.html": (
        "Общий прогресс",
        "Общее время",
        "Токены",
        "Карта проекта",
        "Дизайн и UX",
        "Design Drift Gate",
        "DESIGN.md",
        "Техническая проверка",
        "Независимая приёмка G4",
        "s.intelligence",
        "s.design",
    ),
    "skills/building-end-to-end/assets/dashboard-state-template.js": (
        '"intelligence"',
        '"design"',
        '"designDocWrite"',
        '"prototypeWrite"',
        '"browser"',
    ),
}

MARKETPLACE_REQUIRED_FILES = (
    "README.md",
    ".github/workflows/package-validation.yml",
    "docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md",
    "docs/plans/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-plan.md",
    "docs/specs/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-spec.md",
    "docs/plans/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-plan.md",
    "docs/specs/2026-08-20-matreshka-agent-0.5-browser-e2e-spec.md",
    "docs/plans/2026-08-20-matreshka-agent-0.5-browser-e2e-plan.md",
    "docs/specs/2026-08-20-matreshka-agent-0.5-design-intelligence-spec.md",
    "docs/plans/2026-08-20-matreshka-agent-0.5-design-intelligence-plan.md",
)

MARKETPLACE_MARKERS = {
    "README.md": (
        "0.5 development track",
        "Source Intent Traceability",
        "Project Intelligence Layer",
        "Design Intelligence Layer",
        "Apple-inspired design core",
        "DESIGN.md",
        "Browser E2E",
        "Visual Design Check",
        "Одиннадцать bundled skills",
        "validate_dev_05.py",
        "check_dev_05.py",
        "doctor_dev_05.py",
    ),
    ".github/workflows/package-validation.yml": (
        "validate_dev_05.py",
        "check_dev_05.py",
        "check_dev_05_behavioral_contracts.py",
        "doctor_dev_05.py",
        "python-version: '3.11'",
    ),
    "docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md": (
        "SOURCE_BRIEF",
        "U-",
        "G2",
        "G3",
        "G4",
    ),
    "docs/plans/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-plan.md": (
        "Task 1",
        "Task 8",
        "G4",
    ),
    "docs/specs/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-spec.md": (
        "PROJECT_TOPOLOGY",
        "AREA_CONTEXT_SET",
        "CROSS_AREA_INTERFACE_CONTRACT",
        "RUNTIME_MAP",
        "DOCUMENTATION_DRIFT_GATE",
        "SPECIALIST_ROLE_ROUTING",
    ),
    "docs/plans/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-plan.md": (
        "P1",
        "P2",
        "P3",
        "P4",
        "P5",
        "P6",
    ),
    "docs/specs/2026-08-20-matreshka-agent-0.5-browser-e2e-spec.md": (
        "PLAYWRIGHT_MANAGED",
        "CHROME_CDP",
        "HOST_BROWSER_TOOL",
        "Browser G4",
        "Destructive",
    ),
    "docs/plans/2026-08-20-matreshka-agent-0.5-browser-e2e-plan.md": (
        "B1",
        "B2",
        "B3",
        "B4",
        "B5",
    ),
    "docs/specs/2026-08-20-matreshka-agent-0.5-design-intelligence-spec.md": (
        "DESIGN.md",
        "Apple-inspired",
        "DESIGN_CONTEXT_SET",
        "VISUAL_DESIGN_CHECK",
        "DESIGN_DRIFT",
    ),
    "docs/plans/2026-08-20-matreshka-agent-0.5-design-intelligence-plan.md": (
        "D1",
        "D5",
        "D9",
        "D10",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check Matreshka Agent 0.5 development wiring."
    )
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
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


def require_files(root: Path, relatives: tuple[str, ...], label: str, failures: list[str]) -> None:
    for relative in relatives:
        path = root / relative
        if not path.is_file():
            failures.append(f"MISSING {label}{relative}")


def require_markers(root: Path, mapping: dict[str, tuple[str, ...]], label: str, failures: list[str]) -> None:
    for relative, markers in mapping.items():
        text = read(root / relative, failures)
        if not text:
            continue
        folded = text.casefold()
        for marker in markers:
            if marker.casefold() not in folded:
                failures.append(f"MARKER {label}{relative}: missing {marker!r}")


def check_inventory(plugin_root: Path, failures: list[str]) -> None:
    skills_root = plugin_root / "skills"
    actual_skills = {p.name for p in skills_root.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    if actual_skills != EXPECTED_SKILLS:
        missing = sorted(EXPECTED_SKILLS - actual_skills)
        extra = sorted(actual_skills - EXPECTED_SKILLS)
        failures.append(f"SKILL inventory mismatch: missing={missing}, extra={extra}")

    wrapper_root = plugin_root / "codex-prompts"
    actual_wrappers = {p.name for p in wrapper_root.glob("matreshka-*.md") if p.is_file()}
    if actual_wrappers != EXPECTED_CODEX_WRAPPERS:
        missing = sorted(EXPECTED_CODEX_WRAPPERS - actual_wrappers)
        extra = sorted(actual_wrappers - EXPECTED_CODEX_WRAPPERS)
        failures.append(f"CODEX wrapper inventory mismatch: missing={missing}, extra={extra}")


def check_json_files(plugin_root: Path, failures: list[str]) -> None:
    for path in plugin_root.rglob("*.json"):
        text = read(path, failures)
        if not text:
            continue
        try:
            json.loads(text)
        except json.JSONDecodeError as exc:
            failures.append(
                f"JSON plugin/{path.relative_to(plugin_root)}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
            )


def check_codex_routing(plugin_root: Path, failures: list[str]) -> None:
    build_prompt = read(plugin_root / "codex-prompts/matreshka-build.md", failures)
    if 'argument-hint: "[TASK]"' not in build_prompt:
        failures.append("CODEX build wrapper must keep [TASK] argument hint")
    if "$$matreshka-agent:building-end-to-end" not in build_prompt:
        failures.append("CODEX build wrapper must route to namespaced Matreshka Build")

    design_prompt = read(plugin_root / "codex-prompts/matreshka-design.md", failures)
    if 'argument-hint: "[TASK]"' not in design_prompt:
        failures.append("CODEX design wrapper must keep [TASK] argument hint")
    if "$$matreshka-agent:designing-product-experience" not in design_prompt:
        failures.append("CODEX design wrapper must route to namespaced design skill")

    build_yaml = read(
        plugin_root / "skills/building-end-to-end/agents/openai.yaml", failures
    )
    if "$building-end-to-end" not in build_yaml:
        failures.append("Codex Build skill card must preserve canonical skill token")
    if "$matreshka-agent:building-end-to-end" not in build_yaml:
        failures.append("Codex Build skill card must show namespaced invocation")
    for word in (
        "interview",
        "assisted",
        "full-auto",
        "continue-project",
        "existing-project",
    ):
        if word not in build_yaml:
            failures.append(f"Codex Build skill card missing launch hint {word!r}")

    design_yaml = read(
        plugin_root / "skills/designing-product-experience/agents/openai.yaml", failures
    )
    if "$designing-product-experience" not in design_yaml:
        failures.append("Codex design skill card must preserve canonical design token")


def check_project_intelligence_evals(plugin_root: Path, failures: list[str]) -> None:
    path = plugin_root / "skills/orchestrating-subagent-work/evals/project-intelligence-evals.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        cases = payload.get("evals", []) if isinstance(payload, dict) else []
        if len(cases) < 14:
            failures.append("Project Intelligence suite must contain at least 14 cases")
        ids = {str(case.get("id")) for case in cases if isinstance(case, dict)}
        required = {
            "pi-topology-fullstack",
            "pi-topology-cli-no-fake-split",
            "pi-interface-freeze",
            "pi-interface-change-mid-run",
            "pi-context-router",
            "pi-runtime-unknown-port-owner",
            "pi-runtime-observe-not-start",
            "pi-docs-public-contract-drift",
            "pi-docs-private-refactor",
            "pi-ui-specialist-boundary",
            "pi-specialists-no-budget-inflation",
            "pi-operator-execute-only",
            "pi-recovery-stale-cache",
            "pi-docs-conflict-no-authority",
        }
        missing = sorted(required - ids)
        if missing:
            failures.append(
                "Project Intelligence eval coverage missing: " + ", ".join(missing)
            )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"Project Intelligence eval suite unreadable: {exc}")


def check_design_intelligence_evals(plugin_root: Path, failures: list[str]) -> None:
    path = plugin_root / "skills/designing-product-experience/evals/evals.json"
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
        cases = payload.get("evals", []) if isinstance(payload, dict) else []
        if len(cases) < 22:
            failures.append("Design Intelligence suite must contain at least 22 cases")
        ids = {str(case.get("id")) for case in cases if isinstance(case, dict)}
        required = {
            "ui-project-missing-design-md",
            "no-design-write-authority",
            "existing-product-reconstruct-before-change",
            "user-does-not-know-style",
            "fake-prototype-divergence",
            "full-auto-does-not-invent-brand",
            "design-drift-random-tokens",
            "valid-design-change-reconciles",
            "narrow-design-context",
            "backend-no-design-payload",
            "existing-primitive-first",
            "library-install-not-authorized",
            "high-frequency-over-animation",
            "accessibility-design-blocker",
            "e2e-g4-pass-design-fail",
            "visual-capability-unavailable",
            "stale-design-contract-conflict",
            "recovery-design-identity-changed",
            "ui-locale-unresolved-assisted-prototype",
            "anti-slop-generic-directions",
            "dropdown-open-state-quality",
            "prototype-write-requires-run-state",
        }
        missing = sorted(required - ids)
        if missing:
            failures.append(
                "Design Intelligence eval coverage missing: " + ", ".join(missing)
            )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"Design Intelligence eval suite unreadable: {exc}")


def check_dashboard_contract(plugin_root: Path, failures: list[str]) -> None:
    state_text = read(
        plugin_root / "skills/building-end-to-end/assets/dashboard-state-template.js",
        failures,
    )
    html_text = read(
        plugin_root / "skills/building-end-to-end/assets/dashboard-template.html",
        failures,
    )
    contract = {
        "intelligence": "s.intelligence",
        "design": "s.design",
        "timing": "s.timing",
        "usage": "s.usage",
        "tests": "s.tests",
        "browser": "s.browser",
        "authority": "s.authority",
    }
    for state_key, html_marker in contract.items():
        if f'"{state_key}"' not in state_text or html_marker not in html_text:
            failures.append(
                f"DASHBOARD contract mismatch for {state_key}: state/html not both wired"
            )

    for authority_key in (
        "designDocWrite",
        "prototypeWrite",
        "browserInteraction",
        "localProcess",
        "dependencyInstall",
    ):
        if f'"{authority_key}"' not in state_text:
            failures.append(f"DASHBOARD authority state missing {authority_key}")


def main() -> int:
    args = parse_args()
    plugin_root = Path(args.plugin_path).expanduser().resolve()
    marketplace_root = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root
        else infer_marketplace_root(plugin_root)
    )
    failures: list[str] = []

    require_files(plugin_root, PLUGIN_REQUIRED_FILES, "plugin/", failures)
    require_markers(plugin_root, PLUGIN_MARKERS, "plugin/", failures)
    require_files(marketplace_root, MARKETPLACE_REQUIRED_FILES, "repo/", failures)
    require_markers(marketplace_root, MARKETPLACE_MARKERS, "repo/", failures)

    check_inventory(plugin_root, failures)
    check_json_files(plugin_root, failures)
    check_codex_routing(plugin_root, failures)
    check_project_intelligence_evals(plugin_root, failures)
    check_design_intelligence_evals(plugin_root, failures)
    check_dashboard_contract(plugin_root, failures)

    if failures:
        print(f"Matreshka 0.5 development integrity: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Matreshka 0.5 development integrity: PASS")
    print("- exact 11-skill development inventory + 11 Codex wrappers: present")
    print("- Build→Controller→Source/U/S/G1-G4: wired")
    print("- Project Intelligence P1-P6: controller→spec/plan→task→implement→review→verify→finish→recovery wired")
    print("- Design Intelligence D1-D9: controller→design→spec→plan→task→implement→review→visual verify→drift→finish/recovery wired")
    print("- Apple-inspired design core + anti-slop + product-locale + layered-control open-state contracts are required UX-quality gates")
    print("- Browser E2E, Visual Design Check and G4 remain independent evidence axes")
    print("- permission contract separates design-doc/prototype/visual authority")
    print("- implementation/review/verification reports carry interface/design identities and evidence boundaries")
    print("- Russian dashboard state↔HTML includes Project + Design Intelligence, timing/tokens and authority")
    print("- Project Intelligence adversarial coverage: 14 required cases present")
    print("- Design Intelligence adversarial coverage: 22 required cases present")
    print("- plans/READMEs/CHANGELOG/CI development-track markers: synchronized")
    print("Native host behavior is intentionally outside this static check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
