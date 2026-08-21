#!/usr/bin/env python3
"""Check Matreshka 0.5 automatic Security-by-Design hardening coverage.

Read-only/offline. This proves that the five hardening families are present,
recorded in specifications, reviewed, carried by existing S- requirement
mechanics, covered by eval cases, and wired into CI. It does not prove a native
model run or that any particular application is secure.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True

FAMILIES = (
    "S-AUTH-HARDENING",
    "S-FILE-EXECUTION",
    "S-ATOMIC-EFFECT",
    "S-BAAS-AUTHZ",
    "S-PAID-API-BUDGET",
)

REQUIRED_EVAL_IDS = {
    "security-auth-hardening-spec",
    "security-auth-hardening-review",
    "security-file-execution-spec",
    "security-file-execution-verify",
    "security-atomic-effect-implementation",
    "security-atomic-effect-review",
    "security-baas-authz-spec",
    "security-baas-authz-verify",
    "security-paid-api-budget-spec",
    "security-paid-api-budget-verify",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Matreshka security hardening wiring.")
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
    )
    parser.add_argument("--marketplace-root")
    return parser.parse_args()


def infer_marketplace_root(plugin_root: Path) -> Path:
    if plugin_root.parent.name == "plugins":
        return plugin_root.parent.parent.resolve()
    return plugin_root.resolve()


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
        else infer_marketplace_root(root)
    )
    failures: list[str] = []

    security = read(
        root / "skills/specifying-software-work/references/security-by-design.md",
        failures,
    )
    spec_template = read(
        root / "skills/specifying-software-work/assets/specification-template.md",
        failures,
    )
    implementer = read(root / "skills/implementing-with-tests/SKILL.md", failures)
    reviewer = read(root / "skills/reviewing-agent-work/SKILL.md", failures)
    review_checklist = read(
        root / "skills/reviewing-agent-work/references/review-checklist.md",
        failures,
    )
    verifier = read(root / "skills/verifying-development-work/SKILL.md", failures)
    workflow = read(repo / ".github/workflows/package-validation.yml", failures)

    for family in FAMILIES:
        require(security, family, "security baseline", failures)
        require(spec_template, family, "specification template", failures)
        require(review_checklist, family, "review checklist", failures)

    baseline_markers = (
        "Automatic hardening-family selection",
        "both source/network dimension **and** account/identity dimension",
        "at least 12 characters",
        "MFA for privileged/admin accounts",
        "generate an opaque server-side storage name/key",
        "outside executable application/code roots",
        "concurrent/replayed requests",
        "browser-accessible tables",
        "RLS",
        "wrong-user/wrong-tenant",
        "global emergency usage/spend ceiling",
        "concurrency-safe reservation/accounting",
        "REQUIRED | N/A(reason) | HANDOFF",
    )
    for marker in baseline_markers:
        require(security, marker, "security baseline", failures)

    template_markers = (
        "Automatic hardening-family selection",
        "Every `REQUIRED` hardening family materializes as one or more `S-xx` rows",
        "Race-sensitive effects include concurrent/replay proof",
        "BaaS policy inventory/RLS/rules evidence",
        "Paid-provider quota/circuit-breaker model",
    )
    for marker in template_markers:
        require(spec_template, marker, "specification template", failures)

    review_markers = (
        "Five automatic hardening families",
        "frontend-only disabled button/countdown is not rate limiting",
        "Sequential-only tests are insufficient",
        "public/anon provider key may be intentionally public",
        "Provider billing alerts alone are not an application abuse boundary",
    )
    for marker in review_markers:
        require(review_checklist, marker, "review checklist", failures)

    # Existing cross-skill S- mechanics must remain the delivery path. We do not
    # duplicate five special implementations in every skill.
    for marker in (
        "selected S",
        "negative security proof",
        "Design decisions never weaken security/privacy/accessibility safeguards",
    ):
        require(implementer, marker, "implementation S-requirement wiring", failures)
    for marker in (
        "Read Security by Design",
        "Review each selected control and negative proof",
        "Critical",
    ):
        require(reviewer, marker, "review S-requirement wiring", failures)
    for marker in (
        "selected `S-`",
        "Required negative security proofs are explicit matrix rows",
        "Do not use technical `VERIFIED` while selected `S-` lacks current evidence",
    ):
        require(verifier, marker, "verification S-requirement wiring", failures)

    eval_path = root / "evals/security-hardening-evals.json"
    try:
        payload = json.loads(eval_path.read_text(encoding="utf-8"))
        cases = payload.get("evals", []) if isinstance(payload, dict) else []
        ids = {
            str(case.get("id"))
            for case in cases
            if isinstance(case, dict) and case.get("id") is not None
        }
        missing = sorted(REQUIRED_EVAL_IDS - ids)
        if missing:
            failures.append("security hardening eval coverage missing: " + ", ".join(missing))
        if len(cases) < len(REQUIRED_EVAL_IDS):
            failures.append("security hardening eval suite is smaller than required matrix")
        targets = {str(case.get("target_skill")) for case in cases if isinstance(case, dict)}
        for required_target in (
            "specifying-software-work",
            "implementing-with-tests",
            "reviewing-agent-work",
            "verifying-development-work",
        ):
            if required_target not in targets:
                failures.append(f"security hardening eval suite missing target {required_target}")
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        failures.append(f"security hardening eval suite unreadable: {exc}")

    require(workflow, "check_security_hardening.py", "CI security hardening wiring", failures)

    if failures:
        print(f"Matreshka security hardening: FAIL ({len(failures)} finding(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Matreshka security hardening: PASS")
    print("- S-AUTH-HARDENING: auto-selected for password/privileged auth")
    print("- S-FILE-EXECUTION: upload storage cannot become executable code")
    print("- S-ATOMIC-EFFECT: concurrent/replay value effects require atomic proof")
    print("- S-BAAS-AUTHZ: client-addressable BaaS requires provider-side policies")
    print("- S-PAID-API-BUDGET: metered APIs require per-caller + global guardrails")
    print("- all selected families flow through normal S- implementation/review/verification")
    print("- behavioral eval matrix and CI linkage are present")
    print("This is contract coverage, not a claim that any application is invulnerable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
