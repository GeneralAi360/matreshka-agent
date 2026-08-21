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
    "doctor_dev_05.py",
    "python-version: '3.11'",
)


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
    print("- implementation preserves area/IC/design context and stops on design identity change")
    print("- independent review detects design drift and refuses fabricated visual confidence")
    print("- verification separates E2E, visual design, and G4 contamination")
    print("- design reviewer fits existing balanced/maximum-quality budgets")
    print("- CI explicitly runs package, component, behavioral-contract and doctor checks")
    print("This confirms contract/eval coverage exists; native model behavior still needs acceptance execution.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
