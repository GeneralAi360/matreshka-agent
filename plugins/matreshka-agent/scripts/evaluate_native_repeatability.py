#!/usr/bin/env python3
"""Validate Matreshka 0.5 native repeatability plans/results.

CI uses ``--validate-plan`` only; that proves the repeatability contract exists.
A release or host-validation run passes a result JSON without ``--validate-plan``.
Every blocking scenario must have all required repetitions and all must PASS.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ALLOWED_RESULTS = {"PASS", "FAIL", "BLOCKED", "UNCHECKABLE"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate Matreshka native repeatability evidence.")
    parser.add_argument(
        "--plan",
        default=str(Path(__file__).resolve().parent.parent / "evals" / "native-repeatability.json"),
    )
    parser.add_argument("--validate-plan", action="store_true")
    parser.add_argument("--results", help="Native result JSON matching the plan result_schema")
    return parser.parse_args()


def load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON must be an object")
    return payload


def validate_plan(plan: dict[str, Any]) -> tuple[list[str], dict[str, int]]:
    failures: list[str] = []
    scenarios = plan.get("scenarios")
    if not isinstance(scenarios, list) or not scenarios:
        return ["scenarios must be a non-empty list"], {}
    required: dict[str, int] = {}
    for index, scenario in enumerate(scenarios):
        if not isinstance(scenario, dict):
            failures.append(f"scenarios[{index}] is not an object")
            continue
        sid = scenario.get("id")
        reps = scenario.get("repetitions", plan.get("default_repetitions", 5))
        if not isinstance(sid, str) or not sid:
            failures.append(f"scenarios[{index}] has no id")
            continue
        if sid in required:
            failures.append(f"duplicate scenario id: {sid}")
            continue
        if not isinstance(reps, int) or reps < 2:
            failures.append(f"{sid}: repetitions must be >= 2")
            continue
        if not isinstance(scenario.get("property"), str) or not scenario.get("property", "").strip():
            failures.append(f"{sid}: missing property")
        if scenario.get("blocking") is not True:
            failures.append(f"{sid}: current release matrix requires blocking=true")
        required[sid] = reps
    must = {
        "repeat-red-before-code",
        "repeat-interface-freeze",
        "repeat-design-freeze",
        "repeat-permission-boundary",
        "repeat-g4-isolation",
        "repeat-design-review-drift",
    }
    missing = sorted(must - set(required))
    if missing:
        failures.append("missing critical scenarios: " + ", ".join(missing))
    return failures, required


def evaluate_results(plan: dict[str, Any], results: dict[str, Any]) -> list[str]:
    failures, required = validate_plan(plan)
    if failures:
        return failures
    host = results.get("host")
    snapshot = results.get("snapshot")
    runs = results.get("runs")
    if not isinstance(host, str) or not host.strip():
        failures.append("results.host is required")
    if not isinstance(snapshot, str) or len(snapshot.strip()) < 7:
        failures.append("results.snapshot commit identity is required")
    if not isinstance(runs, list):
        failures.append("results.runs must be a list")
        return failures

    seen: dict[str, dict[int, str]] = defaultdict(dict)
    for index, run in enumerate(runs):
        if not isinstance(run, dict):
            failures.append(f"runs[{index}] is not an object")
            continue
        sid = run.get("scenario")
        rep = run.get("repetition")
        result = run.get("result")
        evidence = run.get("evidence")
        if sid not in required:
            failures.append(f"runs[{index}]: unknown scenario {sid!r}")
            continue
        if not isinstance(rep, int) or rep < 1 or rep > required[sid]:
            failures.append(f"runs[{index}]: invalid repetition for {sid}")
            continue
        if rep in seen[sid]:
            failures.append(f"duplicate result for {sid} repetition {rep}")
            continue
        if result not in ALLOWED_RESULTS:
            failures.append(f"runs[{index}]: invalid result {result!r}")
            continue
        if not isinstance(evidence, str) or not evidence.strip():
            failures.append(f"runs[{index}]: evidence is required")
        seen[sid][rep] = result

    for sid, reps in required.items():
        missing = [rep for rep in range(1, reps + 1) if rep not in seen[sid]]
        if missing:
            failures.append(f"{sid}: missing repetitions {missing}")
            continue
        bad = {rep: seen[sid][rep] for rep in range(1, reps + 1) if seen[sid][rep] != "PASS"}
        if bad:
            detail = ", ".join(f"{rep}={result}" for rep, result in bad.items())
            failures.append(f"{sid}: repeatability failed ({detail})")
    return failures


def main() -> int:
    args = parse_args()
    try:
        plan = load_json(Path(args.plan).expanduser().resolve())
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Native repeatability: FAIL — cannot read plan: {exc}", file=sys.stderr)
        return 1

    if args.validate_plan:
        failures, required = validate_plan(plan)
        if failures:
            print(f"Native repeatability plan: FAIL ({len(failures)})")
            for failure in failures:
                print(f"- {failure}")
            return 1
        print("Native repeatability plan: PASS")
        print(f"- scenarios: {len(required)}")
        print(f"- required executions: {sum(required.values())}")
        print("- this validates the matrix only; native behavior is not claimed")
        return 0

    if not args.results:
        print("--results is required unless --validate-plan is used", file=sys.stderr)
        return 2
    try:
        results = load_json(Path(args.results).expanduser().resolve())
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"Native repeatability: FAIL — cannot read results: {exc}", file=sys.stderr)
        return 1

    failures = evaluate_results(plan, results)
    if failures:
        print(f"Native repeatability: FAIL ({len(failures)})")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("Native repeatability: PASS")
    print(f"- host: {results.get('host')}")
    print(f"- snapshot: {results.get('snapshot')}")
    print("- every blocking invariant passed every required repetition")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
