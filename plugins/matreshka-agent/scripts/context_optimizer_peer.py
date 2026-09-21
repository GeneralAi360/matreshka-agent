#!/usr/bin/env python3
"""Resolve and optionally invoke the peer Context Optimizer skill.

No network, package installation, Git mutation or implicit download is performed.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

SKILL_NAME = "context-optimizer"
ENV_HOME = "MATRESHKA_CONTEXT_OPTIMIZER_HOME"
COMMANDS = {"start", "adopt", "resume", "check", "status", "optimize"}


def _candidate_roots(project: Path) -> list[tuple[str, Path]]:
    home = Path.home()
    candidates: list[tuple[str, Path]] = []

    env = os.environ.get(ENV_HOME)
    if env:
        candidates.append(("ENV", Path(env).expanduser()))

    for base, source in (
        (project / ".agents" / "skills" / SKILL_NAME, "PROJECT_CODEX"),
        (project / ".claude" / "skills" / SKILL_NAME, "PROJECT_CLAUDE"),
        (project / ".gemini" / "skills" / SKILL_NAME, "PROJECT_GEMINI"),
        (project / "skills" / SKILL_NAME, "PROJECT_PACKAGE"),
        (home / ".agents" / "skills" / SKILL_NAME, "USER_CODEX"),
        (home / ".claude" / "skills" / SKILL_NAME, "USER_CLAUDE"),
        (home / ".gemini" / "skills" / SKILL_NAME, "USER_GEMINI"),
    ):
        candidates.append((source, base))

    # Development checkout convenience. It is read-only discovery, not install.
    for name in ("Matreshk-context-optimizer", "Matreshka-context-optimizer"):
        candidates.append(("SIBLING_REPOSITORY", project.parent / name / "skills" / SKILL_NAME))

    return candidates


def _normalize_candidate(path: Path) -> Path | None:
    path = path.expanduser().resolve()
    direct = path / "SKILL.md"
    runner = path / "scripts" / "context_optimizer.py"
    if direct.is_file() and runner.is_file():
        return path

    nested = path / "skills" / SKILL_NAME
    if (nested / "SKILL.md").is_file() and (nested / "scripts" / "context_optimizer.py").is_file():
        return nested
    return None


def resolve(project: Path) -> dict[str, Any]:
    seen: set[str] = set()
    for source, candidate in _candidate_roots(project):
        normalized = _normalize_candidate(candidate)
        if normalized is None:
            continue
        key = str(normalized)
        if key in seen:
            continue
        seen.add(key)
        return {
            "status": "READY",
            "skill": SKILL_NAME,
            "source": source,
            "skill_root": key,
            "runner": str(normalized / "scripts" / "context_optimizer.py"),
        }
    return {
        "status": "UNAVAILABLE",
        "skill": SKILL_NAME,
        "source": None,
        "skill_root": None,
        "runner": None,
        "message_ru": (
            "Оптимизатор контекста не найден. Matreshka продолжит работу без "
            "выдуманных измерений. Автоматическая установка не выполняется."
        ),
    }


def invoke(
    project: Path,
    command: str,
    *,
    execute: bool,
    provider: str,
    trigger_mode: str,
    trigger_reason: str | None,
    automatic: bool,
) -> dict[str, Any]:
    state = resolve(project)
    if state["status"] != "READY":
        return state

    argv = [
        sys.executable,
        str(state["runner"]),
        "--project",
        str(project.resolve()),
        "--provider",
        provider,
        "--trigger-mode",
        trigger_mode,
    ]
    if trigger_reason:
        argv.extend(["--trigger-reason", trigger_reason])
    if automatic:
        argv.append("--automatic")
    argv.append(command)

    if not execute:
        return {
            **state,
            "status": "READY_TO_RUN",
            "command": command,
            "argv": argv,
            "message_ru": (
                "Оптимизатор контекста найден. Для запуска требуется разрешение "
                "на локальный процесс либо нативный вызов peer skill со стороны host."
            ),
        }

    proc = subprocess.run(
        argv,
        cwd=str(project.resolve()),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=180,
    )
    if proc.returncode != 0:
        return {
            **state,
            "status": "ERROR",
            "command": command,
            "exit_code": proc.returncode,
            "message_ru": "Проверка контекста завершилась ошибкой.",
            "stderr": proc.stderr[-4000:],
        }

    try:
        payload = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            **state,
            "status": "ERROR",
            "command": command,
            "message_ru": "Оптимизатор вернул некорректный JSON.",
        }
    return {
        **state,
        "status": "COMPLETED",
        "command": command,
        "result": payload,
        "message_ru": str(payload.get("message_ru") or "Проверка контекста выполнена."),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Matreshka → Context Optimizer peer bridge")
    parser.add_argument("--project", default=".")
    parser.add_argument("--provider", default="auto", choices=["auto", "codex", "claude", "antigravity", "none"])
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--trigger-mode", default="MANUAL")
    parser.add_argument("--trigger-reason")
    parser.add_argument("--automatic", action="store_true")
    parser.add_argument("command", nargs="?", choices=sorted(COMMANDS))
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    if not project.exists() or not project.is_dir():
        print(json.dumps({"status": "ERROR", "message_ru": f"Проект не найден: {project}"}, ensure_ascii=False, indent=2))
        return 2

    if args.command is None:
        result = resolve(project)
    else:
        result = invoke(
            project,
            args.command,
            execute=args.execute,
            provider=args.provider,
            trigger_mode=args.trigger_mode,
            trigger_reason=args.trigger_reason,
            automatic=args.automatic,
        )

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("status") not in {"ERROR"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
