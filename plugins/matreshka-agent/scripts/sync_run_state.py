#!/usr/bin/env python3
"""Validate and atomically synchronize a Matreshka dashboard projection.

This helper is intentionally narrower than a runtime/dashboard server:

- it never opens a browser;
- it never starts/stops/kills a process;
- it never binds a port or uses the network;
- it never changes the ledger, product code, DESIGN.md, Git, or remote state.

It validates ``dashboard-state.js``, enforces deterministic projection
invariants, atomically rewrites the normalized state, and embeds the same
last-known-good snapshot into ``dashboard.html``.  If validation fails, neither
file is changed, so a bad state update cannot destroy the last usable dashboard.

Usage from a resolved Matreshka package path::

    python3 -B <plugin-root>/scripts/sync_run_state.py \
      .matreshka/runs/<run-id>

The command itself still requires the run-state write/local-command authority
already granted to the controller.  It grants no authority of its own.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True

STATE_FILE = "dashboard-state.js"
HTML_FILE = "dashboard.html"
SNAPSHOT_START = "/*MATRESHKA_SNAPSHOT_START*/"
SNAPSHOT_END = "/*MATRESHKA_SNAPSHOT_END*/"
ASSIGNMENT = "window.MATRESHKA_RUN_STATE"
SNAPSHOT_ASSIGNMENT = "window.MATRESHKA_RUN_STATE_SNAPSHOT"

DEFAULT_STAGE_ORDER = [
    "source",
    "g1",
    "spec",
    "g2",
    "plan",
    "implementation",
    "review",
    "technical",
    "g4",
    "finish",
]

ACTIVE = {"ACTIVE", "IN_PROGRESS"}
PENDING = {"PENDING", "NOT_STARTED"}
TERMINAL = {
    "PASS",
    "COMPLETE",
    "VERIFIED",
    "APPROVED",
    "PARTIAL",
    "PARTIALLY_VERIFIED",
    "FAILED",
    "FAIL",
    "BLOCKED",
    "HANDOFF_REQUIRED",
    "NOT_RUN",
    "NOT_APPLICABLE",
    "SKIPPED",
}
KNOWN = ACTIVE | PENDING | TERMINAL


class StateError(ValueError):
    pass


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def parse_iso(value: Any) -> datetime | None:
    if not isinstance(value, str) or not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = path.stat().st_mode if path.exists() else None
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=path.parent)
    tmp = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        if mode is not None:
            os.chmod(tmp, mode)
        os.replace(tmp, path)
    finally:
        try:
            tmp.unlink()
        except FileNotFoundError:
            pass


def load_state(path: Path) -> tuple[str, dict[str, Any]]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise StateError(f"cannot read {path}: {exc}") from exc

    marker = re.search(r"window\.MATRESHKA_RUN_STATE\s*=", text)
    if not marker:
        raise StateError(f"{path}: missing {ASSIGNMENT} assignment")
    prefix = text[: marker.start()]
    body = text[marker.end() :].strip()
    if body.endswith(";"):
        body = body[:-1].rstrip()
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise StateError(
            f"{path}: invalid state JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(payload, dict):
        raise StateError(f"{path}: state must be a JSON object")
    return prefix, payload


def allowed_pairs(state: dict[str, Any]) -> set[frozenset[str]]:
    integrity = state.get("stateIntegrity")
    raw = integrity.get("allowedConcurrentStagePairs", []) if isinstance(integrity, dict) else []
    pairs: set[frozenset[str]] = set()
    if not isinstance(raw, list):
        raise StateError("stateIntegrity.allowedConcurrentStagePairs must be a list")
    for item in raw:
        if not isinstance(item, list) or len(item) != 2 or not all(isinstance(v, str) for v in item):
            raise StateError("every allowedConcurrentStagePairs entry must be [stageA, stageB]")
        pairs.add(frozenset(item))
    return pairs


def nearest_later_started(
    stage_id: str,
    stages_by_id: dict[str, dict[str, Any]],
    order: list[str],
) -> str | None:
    try:
        start = order.index(stage_id)
    except ValueError:
        return None
    candidates: list[tuple[datetime, str]] = []
    for later_id in order[start + 1 :]:
        later = stages_by_id.get(later_id)
        if not later:
            continue
        value = later.get("startedAt")
        parsed = parse_iso(value)
        if parsed:
            candidates.append((parsed, value))
    candidates.sort(key=lambda item: item[0])
    return candidates[0][1] if candidates else None


def normalize_and_validate(state: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Return normalized projection or raise without mutating caller state.

    The helper may derive only *mechanical* facts.  It can fill a missing
    ``finishedAt`` for a stage that is already semantically terminal, using the
    next stage's exact ``startedAt`` (or the run's exact finished timestamp).
    It never upgrades ACTIVE/PARTIAL/BLOCKED/etc. to PASS.
    """

    data = json.loads(json.dumps(state))
    warnings: list[str] = []

    order = data.get("stageOrder", DEFAULT_STAGE_ORDER)
    if not isinstance(order, list) or not order or not all(isinstance(v, str) and v for v in order):
        raise StateError("stageOrder must be a non-empty list of stage IDs")
    if len(order) != len(set(order)):
        raise StateError("stageOrder contains duplicate stage IDs")

    stages = data.get("stages", [])
    if not isinstance(stages, list):
        raise StateError("stages must be a list")

    by_id: dict[str, dict[str, Any]] = {}
    for index, stage in enumerate(stages):
        if not isinstance(stage, dict):
            raise StateError(f"stages[{index}] must be an object")
        stage_id = stage.get("id")
        if not isinstance(stage_id, str) or not stage_id:
            raise StateError(f"stages[{index}] is missing a string id")
        if stage_id in by_id:
            raise StateError(f"duplicate stage id: {stage_id}")
        by_id[stage_id] = stage
        status = str(stage.get("status", "PENDING")).upper()
        if status not in KNOWN:
            raise StateError(f"stage {stage_id}: unknown status {status!r}")
        stage["status"] = status
        if stage_id not in order:
            warnings.append(f"stage {stage_id} is not declared in stageOrder")

    concurrency = allowed_pairs(data)
    active = [stage for stage in stages if stage.get("status") in ACTIVE]
    if len(active) > 1:
        active_ids = [str(stage["id"]) for stage in active]
        for i, left in enumerate(active_ids):
            for right in active_ids[i + 1 :]:
                if frozenset((left, right)) not in concurrency:
                    raise StateError(
                        "concurrent active stages are not allowed: " + ", ".join(active_ids)
                    )

    rank = {stage_id: index for index, stage_id in enumerate(order)}
    progressed = {
        stage_id
        for stage_id, stage in by_id.items()
        if stage.get("status") not in PENDING or stage.get("startedAt")
    }
    for stage in active:
        stage_id = str(stage["id"])
        if not parse_iso(stage.get("startedAt")):
            raise StateError(f"active stage {stage_id} has no valid startedAt")
        if stage_id not in rank:
            continue
        later = [sid for sid in progressed if sid in rank and rank[sid] > rank[stage_id]]
        for later_id in later:
            if frozenset((stage_id, later_id)) not in concurrency:
                raise StateError(
                    f"stage invariant violated: {stage_id} is still active after {later_id} started"
                )

    run_finished = None
    timing = data.get("timing")
    if isinstance(timing, dict):
        run_finished = timing.get("finishedAt")

    for stage_id in order:
        stage = by_id.get(stage_id)
        if not stage or stage.get("status") not in TERMINAL:
            continue
        started = parse_iso(stage.get("startedAt"))
        finished_value = stage.get("finishedAt")
        finished = parse_iso(finished_value)
        if finished_value and not finished:
            raise StateError(f"stage {stage_id}: invalid finishedAt")
        if not finished:
            inferred = nearest_later_started(stage_id, by_id, order) or run_finished
            if inferred and parse_iso(inferred):
                stage["finishedAt"] = inferred
                finished = parse_iso(inferred)
                warnings.append(f"filled {stage_id}.finishedAt from exact later transition")
        if started and finished and finished < started:
            raise StateError(f"stage {stage_id}: finishedAt precedes startedAt")

    integrity = data.get("stateIntegrity")
    if not isinstance(integrity, dict):
        integrity = {}
        data["stateIntegrity"] = integrity
    integrity.setdefault("allowedConcurrentStagePairs", [])
    stamp = now_iso()
    integrity["status"] = "PARTIAL" if warnings else "PASS"
    integrity["findingsCount"] = len(warnings)
    integrity["lastSyncedAt"] = stamp
    integrity["snapshotUpdatedAt"] = stamp
    integrity["normalizations"] = warnings[:8]
    integrity["source"] = "sync_run_state.py"
    return data, warnings


def render_state(prefix: str, state: dict[str, Any]) -> str:
    clean_prefix = prefix.rstrip() + "\n" if prefix.strip() else ""
    return clean_prefix + f"{ASSIGNMENT} = " + json.dumps(
        state, ensure_ascii=False, indent=2, sort_keys=False
    ) + ";\n"


def embed_snapshot(html: str, state: dict[str, Any]) -> str:
    start = html.find(SNAPSHOT_START)
    end = html.find(SNAPSHOT_END)
    if start < 0 or end < 0 or end <= start:
        raise StateError(
            f"{HTML_FILE}: missing ordered {SNAPSHOT_START}/{SNAPSHOT_END} markers"
        )
    payload = json.dumps(state, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    replacement = (
        SNAPSHOT_START
        + "\n"
        + f"{SNAPSHOT_ASSIGNMENT}={payload};\n"
        + SNAPSHOT_END
    )
    return html[:start] + replacement + html[end + len(SNAPSHOT_END) :]


def sync(run_dir: Path) -> tuple[list[str], dict[str, Any]]:
    state_path = run_dir / STATE_FILE
    html_path = run_dir / HTML_FILE
    prefix, original = load_state(state_path)
    normalized, warnings = normalize_and_validate(original)
    try:
        html = html_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise StateError(f"cannot read {html_path}: {exc}") from exc
    next_html = embed_snapshot(html, normalized)

    # Both prospective contents are built before either replace. Validation
    # failure therefore leaves the previous pair untouched.
    atomic_write(state_path, render_state(prefix, normalized))
    atomic_write(html_path, next_html)
    return warnings, normalized


def self_test() -> int:
    from tempfile import TemporaryDirectory

    def base_state() -> dict[str, Any]:
        return {
            "runId": "self-test",
            "stageOrder": ["source", "spec", "plan"],
            "stateIntegrity": {"allowedConcurrentStagePairs": []},
            "timing": {"finishedAt": None},
            "stages": [
                {
                    "id": "source",
                    "status": "PASS",
                    "startedAt": "2026-08-21T10:00:00Z",
                    "finishedAt": None,
                },
                {
                    "id": "spec",
                    "status": "ACTIVE",
                    "startedAt": "2026-08-21T10:01:00Z",
                    "finishedAt": None,
                },
                {"id": "plan", "status": "PENDING", "startedAt": None, "finishedAt": None},
            ],
        }

    html_template = (
        "<html><script>\n"
        + SNAPSHOT_START
        + "\nwindow.MATRESHKA_RUN_STATE_SNAPSHOT=null;\n"
        + SNAPSHOT_END
        + "\n</script></html>"
    )

    checks: list[tuple[str, bool]] = []
    with TemporaryDirectory() as tmp:
        run = Path(tmp)
        state_path = run / STATE_FILE
        html_path = run / HTML_FILE
        state_path.write_text(
            f"{ASSIGNMENT} = " + json.dumps(base_state(), ensure_ascii=False) + ";\n",
            encoding="utf-8",
        )
        html_path.write_text(html_template, encoding="utf-8")
        warnings, normalized = sync(run)
        checks.append(("terminal timestamp normalized", normalized["stages"][0]["finishedAt"] == "2026-08-21T10:01:00Z"))
        checks.append(("integrity recorded", normalized["stateIntegrity"]["status"] == "PARTIAL"))
        checks.append(("snapshot embedded", "self-test" in html_path.read_text(encoding="utf-8")))
        _, reparsed = load_state(state_path)
        checks.append(("state remains parseable", reparsed["runId"] == "self-test"))
        checks.append(("normalization warning present", bool(warnings)))

        broken = base_state()
        broken["stages"][2] = {
            "id": "plan",
            "status": "ACTIVE",
            "startedAt": "2026-08-21T10:02:00Z",
            "finishedAt": None,
        }
        state_path.write_text(
            f"{ASSIGNMENT} = " + json.dumps(broken) + ";\n", encoding="utf-8"
        )
        before_html = html_path.read_text(encoding="utf-8")
        failed = False
        try:
            sync(run)
        except StateError:
            failed = True
        checks.append(("conflicting active stages rejected", failed))
        checks.append(("bad sync preserves last dashboard", html_path.read_text(encoding="utf-8") == before_html))

    failed_checks = [name for name, ok in checks if not ok]
    if failed_checks:
        print(f"sync_run_state self-test: FAIL ({len(failed_checks)})")
        for name in failed_checks:
            print(f"- {name}")
        return 1
    print(f"sync_run_state self-test: PASS ({len(checks)} checks)")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Synchronize Matreshka local dashboard state safely.")
    parser.add_argument("run_dir", nargs="?", help=".matreshka/runs/<run-id> directory")
    parser.add_argument("--self-test", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.self_test:
        return self_test()
    if not args.run_dir:
        print("run_dir is required unless --self-test is used", file=sys.stderr)
        return 2
    run_dir = Path(args.run_dir).expanduser().resolve()
    try:
        warnings, state = sync(run_dir)
    except StateError as exc:
        print(f"Matreshka run-state sync: BLOCKED — {exc}", file=sys.stderr)
        return 1
    status = state.get("stateIntegrity", {}).get("status", "PASS")
    print(f"Matreshka run-state sync: {status}")
    print(f"- run: {state.get('runId', run_dir.name)}")
    print(f"- snapshot: embedded in {run_dir / HTML_FILE}")
    if warnings:
        for warning in warnings:
            print(f"- note: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
