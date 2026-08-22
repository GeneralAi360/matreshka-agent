#!/usr/bin/env python3
"""Check that 0.5 cross-skill behavioral eval coverage exists and stays in CI.

Read-only/offline. This validates contract/eval coverage, not model behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

REQUIRED_CASES = {
    "skills/specifying-software-work/evals/evals.json": {
        "design-identity-preserved",
        "ui-direction-unresolved-before-spec",
    },
    "skills/designing-product-experience/evals/evals.json": {
        "ui-locale-unresolved-assisted-prototype",
        "anti-slop-generic-directions",
        "dropdown-open-state-quality",
        "prototype-write-requires-run-state",
    },
    "skills/implementing-with-tests/evals/evals.json": {
        "ui-task-preserves-area-interface-design",
        "implementation-detects-design-contract-change",
    },
    "skills/reviewing-agent-work/evals/evals.json": {
        "design-review-detects-screen-drift",
        "design-review-uncheckable-visual-feel",
    },
    "skills/verifying-development-work/evals/evals.json": {
        "visual-design-fails-while-e2e-passes",
        "visual-design-uncheckable-without-renderer",
        "g4-contaminated-by-design-artifacts",
    },
    "evals/security-hardening-evals.json": {
        "security-auth-hardening-spec",
        "security-auth-hardening-review",
        "security-file-execution-spec",
        "security-file-execution-verify",
        "security-atomic-effect-implementation",
        "security-atomic-effect-review",
        "security-atomic-effect-ordinary-crud-na",
        "security-baas-authz-spec",
        "security-baas-authz-verify",
        "security-paid-api-budget-spec",
        "security-paid-api-budget-verify",
    },
}

REQUIRED_PROFILE_MARKERS = (
    "design-critical/high-judgment experience signals",
    "DESIGN_REVIEWER",
    "two reviewer slots",
    "do not add a separate Design Reviewer on top of balanced budget",
    "Visual Design Check",
)

REQUIRED_CI_MARKERS = (
    "validate_dev_05.py",
    "check_dev_05.py",
    "check_dev_05_behavioral_contracts.py",
    "check_security_hardening.py",
    "sync_run_state.py --self-test",
    "check_context_budget.py",
    "evaluate_native_repeatability.py",
    "check_autopilot_regressions.py",
    "doctor_dev_05.py",
    "python-version: '3.11'",
)

STATIC_MARKERS = {
    "skills/designing-product-experience/references/anti-slop.md": (
        "Product UI language",
        "Dropdown / select / popover quality gate",
        "Content visible by default",
        "Prototype anti-slop pass",
        "product-specific signature",
    ),
    "skills/designing-product-experience/SKILL.md": (
        "anti-slop.md",
        "PRODUCT_UI_LOCALE",
        "product UI locale",
        "open/expanded state",
        "Do not freeze an unresolved draft",
    ),
    "skills/designing-product-experience/references/prototype-exploration.md": (
        "Resolve product UI locale first",
        "Run-state before prototype writes",
        "Layered/open control fidelity",
        "Anti-slop verification before user choice",
    ),
    "skills/designing-product-experience/assets/design-contract-template.md": (
        "Product UI locale",
        "Product language and localization",
        "Product-specific signature idea",
        "Open/expanded layered-control states",
        "Anti-slop review at selection",
    ),
    "skills/building-end-to-end/references/interaction-modes.md": (
        "CONVERSATION_LANGUAGE",
        "PRODUCT_UI_LOCALE",
        "Never infer `PRODUCT_UI_LOCALE`",
        "before comparison prototypes",
    ),
    "skills/reviewing-agent-work/references/review-checklist.md": (
        "Design, anti-slop, and interaction craft",
        "Select / dropdown / menu / popover open-state review",
        "Ordinary local CRUD/settings persistence is not automatically `S-ATOMIC-EFFECT`",
    ),
    "skills/verifying-development-work/references/browser-e2e.md": (
        "Layered-control open-state verification",
        "LAYERED_CONTROL_CHECK",
        "Product-locale visual evidence",
    ),
    "skills/specifying-software-work/references/security-by-design.md": (
        "Do **not** select this family merely because a product uses SQLite/Postgres",
        "create/edit/delete a calorie log entry",
        "do not infer `S-ATOMIC-EFFECT` from the mere presence of a database",
    ),
    "evals/context-budget.json": (
        "anti-slop.md",
    ),
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check Matreshka 0.5 cross-skill behavioral contract coverage."
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


def load_cases(path: Path) -> set[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("evals"), list):
        raise ValueError("expected object with evals array")
    return {
        str(case.get("id"))
        for case in payload["evals"]
        if isinstance(case, dict) and case.get("id") is not None
    }


def main() -> int:
    args = parse_args()
    plugin_root = Path(args.plugin_path).expanduser().resolve()
    marketplace_root = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root
        else infer_marketplace_root(plugin_root)
    )
    failures: list[str] = []

    for relative, required in REQUIRED_CASES.items():
        path = plugin_root / relative
        try:
            ids = load_cases(path)
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            failures.append(f"{relative}: unreadable eval suite: {exc}")
            continue
        missing = sorted(required - ids)
        if missing:
            failures.append(f"{relative}: missing cases {', '.join(missing)}")

    for relative, markers in STATIC_MARKERS.items():
        path = plugin_root / relative
        try:
            text = path.read_text(encoding="utf-8").casefold()
        except (OSError, UnicodeError) as exc:
            failures.append(f"{relative}: unreadable static contract: {exc}")
            continue
        for marker in markers:
            if marker.casefold() not in text:
                failures.append(f"{relative}: missing marker {marker!r}")

    profile_path = (
        plugin_root
        / "skills/orchestrating-subagent-work/references/profiles-and-budgets.md"
    )
    try:
        profile = profile_path.read_text(encoding="utf-8").casefold()
    except (OSError, UnicodeError) as exc:
        failures.append(f"profiles-and-budgets.md unreadable: {exc}")
        profile = ""
    for marker in REQUIRED_PROFILE_MARKERS:
        if marker.casefold() not in profile:
            failures.append(f"profiles-and-budgets.md missing {marker!r}")

    workflow_path = marketplace_root / ".github/workflows/package-validation.yml"
    try:
        workflow = workflow_path.read_text(encoding="utf-8").casefold()
    except (OSError, UnicodeError) as exc:
        failures.append(f"package-validation.yml unreadable: {exc}")
        workflow = ""
    for marker in REQUIRED_CI_MARKERS:
        if marker.casefold() not in workflow:
            failures.append(f"package-validation.yml missing CI step marker {marker!r}")

    if failures:
        print(
            "Matreshka 0.5 behavioral-contract coverage: "
            f"FAIL ({len(failures)} finding(s))"
        )
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Matreshka 0.5 behavioral-contract coverage: PASS")
    print("- specification preserves/blocks on design identity")
    print("- Design Intelligence separates product UI locale from conversation language")
    print("- prototype/design flow enforces anti-slop, open-state controls and pre-write run state")
    print("- implementation preserves area/IC/design context and stops on design identity change")
    print("- independent review detects design drift/slop/open-state defects and refuses fabricated visual confidence")
    print("- verification separates E2E, layered-control/open-state evidence, visual design, and G4 contamination")
    print("- five automatic security-hardening families include an ordinary-CRUD non-trigger regression case")
    print("- design reviewer fits existing balanced/maximum-quality budgets")
    print("- CI explicitly keeps package/component/behavior/security/state/context/repeatability/doctor gates")
    print("This confirms contract/eval coverage exists; native model behavior still needs acceptance execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
