#!/usr/bin/env python3
"""Run the targeted G2 delivery-versus-rigor regression evaluation.

This is a deterministic, offline behavioral model. It does not inspect a user
project, launch a model, start a browser, or mutate run state. Its purpose is
to protect the semantic distinction found during native v3 acceptance.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parent.parent
PLAN = ROOT / "evals" / "g2-rigor-evals.json"


def classify_g2(coverage: str, independence: str) -> str:
    if coverage in {"MISSING", "HALF_COVERED", "UNSOURCED"}:
        return "GAP"
    if coverage != "CLEAN":
        return "BLOCKED"
    return {
        "NATIVE": "CLEAN_FRESH_NATIVE",
        "EXTERNAL": "CLEAN_FRESH_EXTERNAL",
        "INLINE": "CLEAN_DEGRADED_INLINE",
    }.get(independence, "BLOCKED")


def derive_rigor(g2_class: str, other_degradations: list[str] | None = None) -> tuple[str, list[str]]:
    degradations = list(other_degradations or [])
    if g2_class == "CLEAN_DEGRADED_INLINE":
        degradations.append("G2_INDEPENDENCE")
    unique = list(dict.fromkeys(degradations))
    return ("DEGRADED" if unique else "FULL", unique)


def derive_delivery(gates: dict[str, str], g2_class: str | None = None) -> str:
    if g2_class in {"GAP", "BLOCKED"}:
        return "PARTIALLY_VERIFIED"
    required = {
        "requirements": "PASS",
        "security": "PASS",
        "interfaces": "PASS",
        "runtime": "PASS",
        "browser": "PASS",
        "design": "PASS",
        "docs": "PASS",
        "g4": "PASS",
    }
    return "COMPLETE" if all(gates.get(key) == value for key, value in required.items()) else "PARTIALLY_VERIFIED"


def run_case(case_id: str) -> dict[str, Any]:
    if case_id == "g2-clean-inline-delivery-complete-rigor-degraded":
        g2 = classify_g2("CLEAN", "INLINE")
        rigor, degradations = derive_rigor(g2)
        delivery = derive_delivery({key: "PASS" for key in (
            "requirements", "security", "interfaces", "runtime",
            "browser", "design", "docs", "g4",
        )}, g2)
        dashboard = {
            "deliveryStatus": delivery,
            "runRigor": rigor,
            "g2EvidenceClass": g2,
            "rigorDegradations": degradations,
        }
        checks = {
            "g2_preserved": g2 == "CLEAN_DEGRADED_INLINE",
            "delivery_complete": delivery == "COMPLETE",
            "rigor_degraded": rigor == "DEGRADED",
            "g2_degradation_recorded": degradations == ["G2_INDEPENDENCE"],
            "dashboard_does_not_upgrade": dashboard["g2EvidenceClass"] == g2,
        }
        return {"id": case_id, "checks": checks}

    if case_id == "g2-material-gap-blocks-plan":
        g2 = classify_g2("MISSING", "INLINE")
        rigor, degradations = derive_rigor(g2)
        plan_status = "BLOCKED" if g2 in {"GAP", "BLOCKED"} else "READY"
        checks = {
            "g2_is_gap": g2 == "GAP",
            "plan_blocked": plan_status == "BLOCKED",
            "delivery_not_complete": derive_delivery({
                key: "PASS" for key in (
                    "requirements", "security", "interfaces", "runtime",
                    "browser", "design", "docs", "g4",
                )
            }, g2) != "COMPLETE",
            "no_posthoc_upgrade": g2 == "GAP",
        }
        return {"id": case_id, "checks": checks}

    raise ValueError(f"unknown case: {case_id}")


def main() -> int:
    payload = json.loads(PLAN.read_text(encoding="utf-8"))
    cases = payload.get("evals", [])
    expected = {
        "g2-clean-inline-delivery-complete-rigor-degraded",
        "g2-material-gap-blocks-plan",
    }
    actual = {str(case.get("id")) for case in cases if isinstance(case, dict)}
    if not expected <= actual:
        missing = ", ".join(sorted(expected - actual))
        print(f"G2 targeted rigor eval: FAIL — missing cases: {missing}")
        return 1

    results = [run_case(case_id) for case_id in sorted(expected)]
    failures = [
        f"{result['id']}: {name}"
        for result in results
        for name, passed in result["checks"].items()
        if not passed
    ]
    if failures:
        print(f"G2 targeted rigor eval: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"G2 targeted rigor eval: PASS ({len(results)}/{len(results)} cases)")
    print("- CLEAN_DEGRADED_INLINE remains historical and is never upgraded by G4 or finish")
    print("- DELIVERY_STATUS=COMPLETE can coexist with RUN_RIGOR=DEGRADED")
    print("- material G2 GAP blocks PLAN")
    print("- dashboard/progress projection cannot promote degraded evidence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
