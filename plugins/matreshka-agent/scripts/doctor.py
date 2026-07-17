#!/usr/bin/env python3
"""Read-only, beginner-friendly diagnostics for a Matreshka Agent package."""

from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys
from dataclasses import asdict
from pathlib import Path
from types import ModuleType
from typing import Any


sys.dont_write_bytecode = True

PLUGIN_ID = "matreshka-agent"
VERSION = "0.1.1"
HOST_COMMANDS = {
    "Codex": "codex",
    "Claude Code": "claude",
    "Cursor": "cursor",
    "Antigravity CLI": "agy",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Read-only Matreshka Agent diagnostics. This command does not install, "
            "update, delete, or send anything."
        )
    )
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
        help="Plugin root; defaults to the parent of this scripts directory.",
    )
    parser.add_argument(
        "--marketplace-root",
        help="Marketplace repository root; inferred from plugins/<name> when omitted.",
    )
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument(
        "--strict-release",
        action="store_true",
        help="Return exit code 2 when public-release metadata is unfinished.",
    )
    return parser.parse_args()


def inferred_marketplace_root(plugin_root: Path) -> Path:
    if plugin_root.parent.name == "plugins":
        return plugin_root.parent.parent
    return plugin_root


def load_validator(plugin_root: Path) -> ModuleType:
    validator_path = plugin_root / "scripts" / "validate_package.py"
    spec = importlib.util.spec_from_file_location("matreshka_package_validator", validator_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load scripts/validate_package.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def load_json(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return {}
    return payload if isinstance(payload, dict) else {}


def publication_warnings(plugin_root: Path, marketplace_root: Path) -> list[str]:
    warnings: list[str] = []
    manifests = [
        load_json(plugin_root / ".codex-plugin" / "plugin.json"),
        load_json(plugin_root / ".claude-plugin" / "plugin.json"),
        load_json(plugin_root / ".cursor-plugin" / "plugin.json"),
    ]
    if not any(manifest.get("repository") for manifest in manifests):
        warnings.append("Choose the final source repository and add its verified URL before publication.")
    if not any(manifest.get("homepage") for manifest in manifests):
        warnings.append("Choose the final documentation homepage before publication.")
    author_names = {
        author.get("name")
        for manifest in manifests
        if isinstance((author := manifest.get("author")), dict)
    }
    if not author_names or author_names == {"Matreshka Agent contributors"}:
        warnings.append("Replace the neutral contributor label with the final publisher identity.")
    security_text = ""
    try:
        security_text = (plugin_root / "SECURITY.md").read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        pass
    if "private security contact" in security_text.casefold() and "not been selected" in security_text.casefold():
        warnings.append("Select a verified private security-reporting channel.")
    asset_root = plugin_root / "assets"
    icons = []
    if asset_root.is_dir():
        icons = [
            path
            for path in asset_root.iterdir()
            if path.is_file() and path.suffix.casefold() in {".png", ".svg"}
        ]
    if not icons:
        warnings.append("Add and visually verify the final package icon.")
    if not (marketplace_root / "README.md").is_file():
        warnings.append("Add beginner installation and usage documentation.")
    return warnings


def git_status(marketplace_root: Path) -> dict[str, Any]:
    git = shutil.which("git")
    if git is None:
        return {"available": False, "repository": False, "status": "Git is not on PATH."}
    if not (marketplace_root / ".git").exists():
        return {
            "available": True,
            "repository": False,
            "status": "The marketplace root is not a Git checkout; local validation still works.",
        }
    try:
        completed = subprocess.run(
            [git, "-C", str(marketplace_root), "status", "--short", "--untracked-files=all"],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        return {
            "available": True,
            "repository": True,
            "status": f"Git status could not be read: {exc}",
        }
    if completed.returncode != 0:
        detail = completed.stderr.strip() or f"exit {completed.returncode}"
        return {
            "available": True,
            "repository": True,
            "status": f"Git status failed: {detail}",
        }
    lines = [line for line in completed.stdout.splitlines() if line.strip()]
    untracked = len([line for line in lines if line.startswith("??")])
    changed = len(lines) - untracked
    if changed == 0 and untracked == 0:
        status = "Working tree is clean."
    else:
        status = f"{changed} tracked change(s), {untracked} untracked path(s); review them before release."
    return {
        "available": True,
        "repository": True,
        "changed_tracked_paths": changed,
        "untracked_paths": untracked,
        "status": status,
    }


def host_status() -> list[dict[str, Any]]:
    return [
        {
            "host": label,
            "command": command,
            "available": shutil.which(command) is not None,
        }
        for label, command in HOST_COMMANDS.items()
    ]


def main() -> int:
    args = parse_args()
    plugin_root = Path(args.plugin_path).expanduser().resolve()
    marketplace_root = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root
        else inferred_marketplace_root(plugin_root).resolve()
    )
    load_error: str | None = None
    findings: list[Any] = []
    try:
        validator = load_validator(plugin_root)
        findings = validator.validate_package(plugin_root, marketplace_root)
    except (OSError, RuntimeError, ImportError, SyntaxError) as exc:
        load_error = str(exc)
    release_warnings = publication_warnings(plugin_root, marketplace_root)
    hosts = host_status()
    git = git_status(marketplace_root)
    package_ok = load_error is None and not findings
    payload = {
        "ok": package_ok,
        "plugin": str(plugin_root),
        "marketplace_root": str(marketplace_root),
        "version": VERSION,
        "read_only": True,
        "network_used": False,
        "python": {
            "version": ".".join(str(part) for part in sys.version_info[:3]),
            "supported": sys.version_info >= (3, 10),
        },
        "hosts": hosts,
        "git": git,
        "findings": [asdict(item) for item in findings],
        "validator_load_error": load_error,
        "release_warnings": release_warnings,
    }
    if args.json_output:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(f"Matreshka Agent doctor — {VERSION} (read-only, offline)")
        print(f"Package: {'PASS' if package_ok else 'FAIL'}")
        if load_error:
            print(f"  Validator could not start: {load_error}")
        for finding in findings:
            print(f"  [{finding.code}] {finding.path}: {finding.message}")
        print("Host commands (only presence was checked):")
        for item in hosts:
            state = "found" if item["available"] else "not found"
            print(f"  - {item['host']}: {state} (`{item['command']}`)")
        print(f"Git: {git['status']}")
        if release_warnings:
            print("Public-release checklist still needs:")
            for warning in release_warnings:
                print(f"  - {warning}")
        else:
            print("Public-release metadata: complete")
        if package_ok:
            print("Local package checks passed. Missing host commands do not block other platforms.")
        print("No files were changed and no network request was made.")
    if not package_ok:
        return 1
    if args.strict_release and release_warnings:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
