#!/usr/bin/env python3
"""Read-only structural check of a project's declared bootstrap map.

No commands, providers, environment variables or recursive project scans.
Exit 0 means structural consistency only, NEVER runtime verification.
"""
from __future__ import annotations

import argparse
import json
import stat
import sys
from pathlib import Path, PurePosixPath

sys.dont_write_bytecode = True
PROFILES = {"split", "fullstack", "managed", "backend", "static"}
STATUSES = {"PLANNED", "NOT_RUN", "BLOCKED", "PASSED", "FAILED", "NOT_APPLICABLE"}
LAYERS = {"unit", "component", "api", "integration", "access", "browser", "visual", "build"}


def safe_path(root: Path, value: str) -> Path:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("path")
    normal = value.replace("\\", "/")
    parts = PurePosixPath(normal).parts
    if normal.startswith("/") or ":" in normal or ".." in parts:
        raise ValueError("path")
    for part in parts:
        name = part.lower()
        if ((name.startswith(".env") and name != ".env.example")
                or name in {".git", ".ssh", ".aws", "credentials", "id_rsa", "id_ed25519"}
                or name.endswith((".pem", ".key", ".p12", ".pfx"))):
            raise ValueError("sensitive-path")
    path = root
    for part in parts:
        path = path / part
        if path.is_symlink():
            raise ValueError("link")
        if path.exists() and getattr(path.lstat(), "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
            raise ValueError("reparse-point")
    if not path.resolve().is_relative_to(root):
        raise ValueError("outside-root")
    return path


def read_json(path: Path):
    if path.stat().st_size > 1_000_000:
        raise ValueError("oversized-json")
    return json.loads(path.read_text(encoding="utf-8-sig"))


def validate(project: Path, manifest: str = "docs/bootstrap.json") -> dict:
    errors = []
    root = project.resolve()
    result = {"status": "INVALID", "runtime": "NOT_VERIFIED", "errors": errors}

    def exists(value, label, directory=False):
        try:
            p = safe_path(root, value)
            if not (p.is_dir() if directory else p.is_file()):
                errors.append("missing:" + label)
            return p
        except (ValueError, OSError):
            errors.append("unsafe:" + label)
            return None

    try:
        if not root.is_dir():
            raise ValueError("project")
        path = safe_path(root, manifest)
        if path.suffix.lower() != ".json":
            raise ValueError("manifest-extension")
        data = read_json(path)
        if not isinstance(data, dict) or data.get("schema_version") != 1:
            raise ValueError("schema_version")
        profile = data.get("profile")
        if not isinstance(profile, str) or profile not in PROFILES:
            raise ValueError("profile")
        decisions = data.get("decisions")
        documents = data.get("documents")
        areas = data.get("areas")
        files = data.get("files")
        migrations = data.get("migration_roots")
        checks = data.get("checks")
        if not all(isinstance(x, dict) for x in (decisions, documents, areas)):
            raise ValueError("decisions/documents/areas")
        if not all(isinstance(x, list) for x in (files, migrations, checks)):
            raise ValueError("files/migration_roots/checks")
        for key in ("frontend", "backend", "database", "hosting"):
            if not isinstance(decisions.get(key), str) or not decisions[key].strip():
                errors.append("decision:" + key)
        exists(data.get("source"), "source")
        for role in ("architecture", "testing", "local_development"):
            exists(documents.get(role), "document:" + role)
        if data.get("source") != documents.get("architecture"):
            errors.append("source:architecture")
        mandatory = {"AGENTS.md", "README.md"}
        if not all(isinstance(f, str) for f in files):
            raise ValueError("files")
        if not mandatory.issubset(files):
            errors.append("files:entrypoints")
        for i, name in enumerate(files):
            exists(name, "file-" + str(i))
        required = {"backend"} if profile == "backend" else {"frontend"}
        if profile in {"split", "fullstack", "managed"}:
            required.add("backend")
        for kind in required:
            if not areas.get(kind):
                errors.append("areas:" + kind)
        for kind, paths in areas.items():
            if kind not in {"frontend", "backend", "data"} or not isinstance(paths, list) or not paths:
                raise ValueError("area")
            for i, name in enumerate(paths):
                p = exists(name, kind + str(i), directory=False) if profile == "managed" and kind == "backend" else None
                # Managed boundaries can be an existing directory OR a documented service contract.
                if profile == "managed" and kind == "backend":
                    if p and p.is_dir():
                        errors.remove("missing:" + kind + str(i))
                else:
                    exists(name, kind + str(i), directory=True)
        normalized_migrations = []
        for i, name in enumerate(migrations):
            p = exists(name, "migration-" + str(i), directory=True)
            if p:
                normalized_migrations.append(str(p.resolve()))
        if len(normalized_migrations) != len(set(normalized_migrations)):
            errors.append("duplicate:migration-root")
        # A row is one test family, never an authorization to execute its command.
        ids, coverage = [], set()
        for row in checks:
            if not isinstance(row, dict):
                raise ValueError("check")
            key, owner, layer, status = (row.get(k) for k in ("id", "owner", "layer", "status"))
            if not all(isinstance(x, str) for x in (key, owner, layer, status)) or not key:
                raise ValueError("check-fields")
            ids.append(key)
            if owner not in areas or layer not in LAYERS or status not in STATUSES:
                errors.append("check:" + key)
            coverage.add((owner, layer))
            exists(row.get("cwd"), "cwd:" + key, directory=True)
            for field in ("scenario", "target", "prerequisites"):
                if not isinstance(row.get(field), str) or not row[field].strip():
                    errors.append(field + ":" + key)
            cmd = row.get("command")
            if not isinstance(cmd, list) or not all(isinstance(x, str) and x for x in cmd):
                raise ValueError("command")
            if status != "PASSED" and (not isinstance(row.get("reason"), str) or not row["reason"].strip()):
                errors.append("reason:" + key)
            if cmd:
                source = exists(row.get("command_source"), "command-source:" + key)
                if cmd[0] in {"npm", "npm.cmd"} and len(cmd) >= 3 and cmd[1] == "run":
                    expected = safe_path(root, row["cwd"]) / "package.json"
                    if not source or source != expected or source.name != "package.json":
                        errors.append("script-source:" + key)
                    elif source.is_file():
                        package = read_json(source)
                        scripts = package.get("scripts", {}) if isinstance(package, dict) else {}
                        if not isinstance(scripts, dict) or not isinstance(scripts.get(cmd[2]), str) or not scripts[cmd[2]].strip():
                            errors.append("script:" + key)
            elif status in {"PASSED", "FAILED"}:
                errors.append("command:" + key)
            if status == "PASSED":
                passed, failed, skipped = (row.get(k) for k in ("passed", "failed", "skipped"))
                if (type(passed) is not int or passed <= 0 or type(failed) is not int or failed != 0
                        or type(skipped) is not int or skipped < 0 or type(row.get("exit")) is not int
                        or row["exit"] != 0 or not isinstance(row.get("baseline"), str) or not row["baseline"]):
                    errors.append("proof:" + key)
                exists(row.get("evidence"), "evidence:" + key)
        if len(ids) != len(set(ids)):
            errors.append("duplicate:check-id")
        for owner in required:
            layers = ("browser",) if owner == "frontend" else ("unit", "integration")
            for layer in layers:
                if (owner, layer) not in coverage:
                    errors.append("coverage:" + owner + ":" + layer)
        if not errors:
            result["status"] = "STRUCTURE_VALID"
    except (OSError, ValueError, TypeError, KeyError, UnicodeError, RecursionError):
        errors.append("invalid-manifest")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--manifest", default="docs/bootstrap.json")
    args = parser.parse_args()
    result = validate(args.project, args.manifest)
    print(json.dumps(result, ensure_ascii=True))
    return 0 if result["status"] == "STRUCTURE_VALID" else 1


if __name__ == "__main__":
    raise SystemExit(main())
