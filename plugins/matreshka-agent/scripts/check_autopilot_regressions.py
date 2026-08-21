#!/usr/bin/env python3
"""Guard Matreshka against regression classes learned from Autopilot v1.0.1+.

This is a static/offline contract check. It does not claim native behavior.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Autopilot-derived hardening invariants.")
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
    )
    parser.add_argument("--marketplace-root")
    return parser.parse_args()


def read(path: Path, failures: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        failures.append(f"cannot read {path}: {exc}")
        return ""


def require(text: str, marker: str, label: str, failures: list[str]) -> None:
    if marker.casefold() not in text.casefold():
        failures.append(f"{label}: missing {marker!r}")


def main() -> int:
    args = parse_args()
    root = Path(args.plugin_path).expanduser().resolve()
    repo = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root
        else (root.parent.parent.resolve() if root.parent.name == "plugins" else root)
    )
    failures: list[str] = []

    html = read(root / "skills/building-end-to-end/assets/dashboard-template.html", failures)
    state = read(root / "skills/building-end-to-end/assets/dashboard-state-template.js", failures)
    obs = read(root / "skills/building-end-to-end/references/run-observability.md", failures)
    controller = read(root / "skills/orchestrating-subagent-work/SKILL.md", failures)
    sync = read(root / "scripts/sync_run_state.py", failures)
    workflow = read(repo / ".github/workflows/package-validation.yml", failures)

    # A1 — dashboard must carry an embedded fallback snapshot and keep polling.
    for marker in (
        "/*MATRESHKA_SNAPSHOT_START*/",
        "window.MATRESHKA_RUN_STATE_SNAPSHOT",
        'safeRender(lastGood,"SNAPSHOT")',
        "setTimeout(poll,10000)",
        "Последний корректный снимок сохранён",
    ):
        require(html, marker, "A1 dashboard snapshot", failures)

    # A2/A3 — deterministic synchronizer + explicit stage order/integrity.
    for marker in (
        "sync_run_state.py",
        "atomic_write",
        "normalize_and_validate",
        "allowedConcurrentStagePairs",
        "stage invariant violated",
        "--self-test",
    ):
        require(sync, marker, "A2/A3 synchronizer", failures)
    for marker in (
        '"stageOrder"',
        '"stateIntegrity"',
        '"allowedConcurrentStagePairs"',
    ):
        require(state, marker, "A3 dashboard state", failures)
    for marker in (
        "A1 — embedded last-known-good snapshot",
        "A2 — atomic run-state synchronizer",
        "A3 — stage transition invariants",
        "semantic success may not",
    ):
        require(obs, marker, "A1-A3 observability contract", failures)
    require(controller, "run-observability.md", "controller→observability wiring", failures)

    # A4 — package context growth has a deterministic byte budget, not fake token math.
    budget_path = root / "evals/context-budget.json"
    try:
        budget = json.loads(budget_path.read_text(encoding="utf-8"))
        ids = {row.get("id") for row in budget.get("surfaces", []) if isinstance(row, dict)}
        for required in {"build-entry-core", "controller-preflight-core", "ui-design-increment"}:
            if required not in ids:
                failures.append(f"A4 context budget: missing surface {required}")
        if budget.get("measurement") != "utf8_bytes":
            failures.append("A4 context budget: measurement must stay utf8_bytes")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"A4 context budget unreadable: {exc}")
    budget_checker = read(root / "scripts/check_context_budget.py", failures)
    for marker in ("utf8_bytes", "runtime token counts", "headroom"):
        require(budget_checker, marker, "A4 context budget checker", failures)

    # A5 — repeatability is an explicit release evidence contract.
    repeat_path = root / "evals/native-repeatability.json"
    try:
        repeat = json.loads(repeat_path.read_text(encoding="utf-8"))
        scenarios = repeat.get("scenarios", [])
        if len(scenarios) < 6:
            failures.append("A5 repeatability: expected at least 6 blocking scenarios")
        for scenario in scenarios:
            if not isinstance(scenario, dict):
                failures.append("A5 repeatability: invalid scenario object")
                continue
            if scenario.get("blocking") is not True:
                failures.append(f"A5 repeatability: {scenario.get('id')} must be blocking")
            if int(scenario.get("repetitions", 0) or 0) < 5:
                failures.append(f"A5 repeatability: {scenario.get('id')} requires fewer than 5 reps")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        failures.append(f"A5 repeatability plan unreadable: {exc}")
    evaluator = read(root / "scripts/evaluate_native_repeatability.py", failures)
    for marker in ("--validate-plan", "every blocking invariant", "missing repetitions"):
        require(evaluator, marker, "A5 repeatability evaluator", failures)

    # The CI must actually exercise the deterministic parts; otherwise files can rot silently.
    for marker in (
        "sync_run_state.py --self-test",
        "check_context_budget.py",
        "evaluate_native_repeatability.py",
        "--validate-plan",
        "check_autopilot_regressions.py",
    ):
        require(workflow, marker, "CI hardening wiring", failures)

    if failures:
        print(f"Autopilot-regression hardening: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Autopilot-regression hardening: PASS")
    print("- A1 embedded last-known-good dashboard snapshot")
    print("- A2 atomic state validation/synchronization")
    print("- A3 mechanically checked stage invariants")
    print("- A4 deterministic context byte budgets")
    print("- A5 five-run native repeatability evidence contract")
    print("Native repeatability results are intentionally outside this static check.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
