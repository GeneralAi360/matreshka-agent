#!/usr/bin/env python3
"""Deterministic context-surface budget check for Matreshka 0.5.

This intentionally measures exact UTF-8 bytes, not estimated model tokens.
Runtime token telemetry keeps the stricter host-reported EXACT/PARTIAL/UNAVAILABLE
contract.  The goal here is regression control: prevent hot-path instruction
surfaces from silently growing without an explicit budget change/review.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.dont_write_bytecode = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Matreshka context-load byte budgets.")
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
    )
    parser.add_argument(
        "--config",
        default="evals/context-budget.json",
        help="Path relative to plugin root unless absolute.",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.plugin_path).expanduser().resolve()
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = root / config_path
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Context budget: FAIL — cannot read config: {exc}", file=sys.stderr)
        return 1

    failures: list[str] = []
    report: list[dict[str, Any]] = []
    single_max = int(config.get("single_file_max_bytes", 0) or 0)
    seen: set[str] = set()

    surfaces = config.get("surfaces")
    if not isinstance(surfaces, list) or not surfaces:
        print("Context budget: FAIL — surfaces must be a non-empty list", file=sys.stderr)
        return 1

    for surface in surfaces:
        if not isinstance(surface, dict):
            failures.append("surface entry is not an object")
            continue
        sid = str(surface.get("id", "<missing>"))
        max_bytes = int(surface.get("max_bytes", 0) or 0)
        files = surface.get("files")
        if not isinstance(files, list) or not files or max_bytes <= 0:
            failures.append(f"{sid}: invalid files/max_bytes")
            continue
        total = 0
        file_rows: list[dict[str, Any]] = []
        for relative in files:
            if not isinstance(relative, str) or not relative:
                failures.append(f"{sid}: invalid file path")
                continue
            path = root / relative
            if not path.is_file():
                failures.append(f"{sid}: missing {relative}")
                continue
            size = len(path.read_bytes())
            total += size
            file_rows.append({"path": relative, "bytes": size})
            seen.add(relative)
            if single_max and size > single_max:
                failures.append(
                    f"single-file budget exceeded: {relative} = {size} > {single_max} bytes"
                )
        if total > max_bytes:
            failures.append(f"surface {sid} = {total} > {max_bytes} bytes")
        report.append(
            {
                "id": sid,
                "bytes": total,
                "max_bytes": max_bytes,
                "headroom_bytes": max_bytes - total,
                "files": file_rows,
            }
        )

    if args.json_output:
        print(
            json.dumps(
                {
                    "ok": not failures,
                    "measurement": "utf8_bytes",
                    "surfaces": report,
                    "failures": failures,
                    "note": config.get("note"),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        print("Matreshka 0.5 context budget")
        for row in report:
            state = "PASS" if row["headroom_bytes"] >= 0 else "FAIL"
            print(
                f"- {row['id']}: {state} — {row['bytes']} / {row['max_bytes']} bytes "
                f"(headroom {row['headroom_bytes']})"
            )
        print("- runtime token counts: not estimated here; host telemetry only")
        if failures:
            print(f"Context budget: FAIL ({len(failures)} finding(s))")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print("Context budget: PASS")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
