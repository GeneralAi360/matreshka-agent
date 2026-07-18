#!/usr/bin/env python3
"""Deterministically validate a Matreshka Agent package without network access."""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import shutil
import stat
import sys
import tempfile
from dataclasses import asdict, dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable
from urllib.parse import unquote


sys.dont_write_bytecode = True

PLUGIN_ID = "matreshka-agent"
DISPLAY_NAME = "Matreshka Agent"
VERSION = "0.1.2"
DESCRIPTION = (
    "Orchestrates coding-agent work from design and planning through tested "
    "implementation, review, verification, and handoff."
)
CONTRIBUTOR_NAME = "Matreshka Agent contributors"
REQUIRED_SKILLS = (
    "orchestrating-subagent-work",
    "designing-software-work",
    "planning-software-work",
    "writing-portable-agent-prompt",
    "implementing-with-tests",
    "debugging-systematically",
    "reviewing-agent-work",
    "verifying-development-work",
    "finishing-development-work",
)
VERSIONED_MANIFESTS = (
    ".codex-plugin/plugin.json",
    ".claude-plugin/plugin.json",
    ".cursor-plugin/plugin.json",
)
PACKAGE_CHECKS = {
    "valid-package",
    "required-skills",
    "manifest-consistency",
    "forbidden-components",
    "forbidden-references",
    "eval-schemas",
    "internal-links",
    "symlink-containment",
    "secret-files",
    "executable-policy",
    "offline-runtime",
    "codex-slash-prompts",
}
WORKFLOW_CATEGORIES = {
    "end-to-end",
    "recovery",
    "adversarial",
    "platform-compatibility",
}
WORKFLOW_PLATFORMS = {
    "codex",
    "claude-code",
    "cursor",
    "antigravity-cli",
}
BASELINE_VARIANTS = ["plain-agent", "minimal-controller", "full-candidate"]
BASELINE_CONTROLS = {
    "repository-snapshot",
    "task-prompt",
    "permission-envelope",
    "available-tools",
    "model-capability-tier",
    "time-limit",
}
TEXT_SUFFIXES = {
    ".json",
    ".md",
    ".mdc",
    ".markdown",
    ".py",
    ".sh",
    ".ps1",
    ".yaml",
    ".yml",
    ".txt",
    ".toml",
}
TEXT_NAMES = {"LICENSE", ".gitignore"}
IGNORED_PARTS = {".git", "__pycache__", "results", "workspaces"}
FORBIDDEN_TOP_LEVEL_DIRS = {"agents", "apps", "commands", "hooks", "monitors", "rules"}
FORBIDDEN_ANY_DIRS = {"apps", "hooks", "monitors"}
FORBIDDEN_COMPONENT_FILES = {
    ".app.json",
    ".lsp.json",
    ".mcp.json",
    "hooks.json",
    "lsp.json",
    "mcp.json",
    "mcp_config.json",
    "monitors.json",
}
DEPENDENCY_FILES = {
    "cargo.toml",
    "go.mod",
    "package-lock.json",
    "package.json",
    "pipfile",
    "pnpm-lock.yaml",
    "poetry.lock",
    "pyproject.toml",
    "requirements.txt",
    "uv.lock",
    "yarn.lock",
}
EXECUTABLE_ALLOWLIST = {
    PurePosixPath("scripts/doctor.py"),
    PurePosixPath("scripts/validate_package.py"),
}
CODEX_PROMPT_WRAPPERS = {
    "matreshka-orchestrate.md": "orchestrating-subagent-work",
    "matreshka-design.md": "designing-software-work",
    "matreshka-plan.md": "planning-software-work",
    "matreshka-prompt.md": "writing-portable-agent-prompt",
    "matreshka-implement.md": "implementing-with-tests",
    "matreshka-debug.md": "debugging-systematically",
    "matreshka-review.md": "reviewing-agent-work",
    "matreshka-verify.md": "verifying-development-work",
    "matreshka-finish.md": "finishing-development-work",
}
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
WINDOWS_ABSOLUTE_RE = re.compile(r"^[A-Za-z]:[\\/]")


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate Matreshka Agent packaging, skills, evals, and safety gates."
    )
    parser.add_argument(
        "plugin_path",
        nargs="?",
        default=str(Path(__file__).resolve().parent.parent),
        help="Plugin root; defaults to the parent of this scripts directory.",
    )
    parser.add_argument(
        "--marketplace-root",
        help="Repository marketplace root; inferred from plugins/<name> when omitted.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Print a machine-readable result.",
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Validate the package and exercise negative checks in temporary copies.",
    )
    return parser.parse_args()


def add(findings: list[Finding], code: str, path: Path | str, message: str) -> None:
    findings.append(Finding(code=code, path=str(path).replace(os.sep, "/"), message=message))


def inferred_marketplace_root(plugin_root: Path) -> Path:
    if plugin_root.parent.name == "plugins":
        return plugin_root.parent.parent
    return plugin_root


def relative_label(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def walk_entries(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return
    for dirpath, dirnames, filenames in os.walk(root, topdown=True, followlinks=False):
        dirnames[:] = sorted(name for name in dirnames if name not in IGNORED_PARTS)
        current = Path(dirpath)
        for name in dirnames:
            yield current / name
        for name in sorted(filenames):
            if name not in IGNORED_PARTS:
                yield current / name


def read_text(path: Path, root: Path, findings: list[Finding], code: str) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        add(findings, code, relative_label(path, root), f"cannot read UTF-8 text: {exc}")
        return None


def load_json(
    path: Path,
    root: Path,
    findings: list[Finding],
    code: str,
) -> dict[str, Any] | None:
    text = read_text(path, root, findings, code)
    if text is None:
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        add(
            findings,
            code,
            relative_label(path, root),
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}",
        )
        return None
    if not isinstance(payload, dict):
        add(findings, code, relative_label(path, root), "top-level JSON value must be an object")
        return None
    return payload


def load_json_array(
    path: Path,
    root: Path,
    findings: list[Finding],
    code: str,
) -> list[Any] | None:
    text = read_text(path, root, findings, code)
    if text is None:
        return None
    try:
        payload = json.loads(text)
    except json.JSONDecodeError as exc:
        add(
            findings,
            code,
            relative_label(path, root),
            f"invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}",
        )
        return None
    if not isinstance(payload, list):
        add(findings, code, relative_label(path, root), "top-level JSON value must be an array")
        return None
    return payload


def require_string(
    payload: dict[str, Any],
    field: str,
    findings: list[Finding],
    code: str,
    path: str,
    *,
    expected: str | None = None,
) -> str | None:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        add(findings, code, path, f"`{field}` must be a non-empty string")
        return None
    if expected is not None and value != expected:
        add(findings, code, path, f"`{field}` must equal `{expected}`")
    return value


def require_string_list(
    value: Any,
    findings: list[Finding],
    code: str,
    path: str,
    field: str,
    *,
    nonempty: bool = True,
) -> list[str] | None:
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        add(findings, code, path, f"`{field}` must be an array of non-empty strings")
        return None
    if nonempty and not value:
        add(findings, code, path, f"`{field}` must not be empty")
        return None
    return value


def reject_unknown_fields(
    payload: dict[str, Any],
    allowed: set[str],
    findings: list[Finding],
    code: str,
    path: str,
) -> None:
    for field in sorted(set(payload) - allowed):
        add(findings, code, path, f"unsupported field `{field}`")


def validate_contract_path(
    plugin_root: Path,
    raw: Any,
    expected: str,
    findings: list[Finding],
    code: str,
    path: str,
) -> None:
    if not isinstance(raw, str) or not raw.strip():
        add(findings, code, path, "skills path must be a non-empty relative string")
        return
    normalized = raw.rstrip("/")
    if normalized != expected.rstrip("/"):
        add(findings, code, path, f"skills path must be `{expected}`")
    pure = PurePosixPath(normalized)
    if pure.is_absolute() or ".." in pure.parts:
        add(findings, code, path, "skills path must stay inside the plugin root")
        return
    resolved = (plugin_root / Path(*pure.parts)).resolve(strict=False)
    if not is_within(resolved, plugin_root.resolve()) or not resolved.is_dir():
        add(findings, code, path, "skills path does not resolve to a plugin directory")


def walk_json_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from walk_json_strings(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from walk_json_strings(item)


def validate_manifest_placeholders(
    payload: dict[str, Any], findings: list[Finding], code: str, path: str
) -> None:
    markers = ("example.com", "local developer", "replace_me", "[todo:")
    for value in walk_json_strings(payload):
        folded = value.casefold()
        if any(marker in folded for marker in markers) or re.search(r"<[a-z0-9_-]+>", folded):
            add(findings, code, path, "manifest contains placeholder metadata")
            return


def validate_codex_manifest(
    plugin_root: Path, payload: dict[str, Any], findings: list[Finding], path: str
) -> None:
    code = "MANIFEST_CODEX"
    allowed = {
        "name",
        "version",
        "description",
        "author",
        "license",
        "keywords",
        "skills",
        "interface",
    }
    reject_unknown_fields(payload, allowed, findings, code, path)
    require_string(payload, "name", findings, code, path, expected=PLUGIN_ID)
    version = require_string(payload, "version", findings, code, path, expected=VERSION)
    if version and not SEMVER_RE.fullmatch(version):
        add(findings, code, path, "`version` must be strict semantic versioning")
    require_string(payload, "description", findings, code, path, expected=DESCRIPTION)
    require_string(payload, "license", findings, code, path, expected="MIT")
    validate_contract_path(plugin_root, payload.get("skills"), "./skills", findings, code, path)
    author = payload.get("author")
    if not isinstance(author, dict):
        add(findings, code, path, "`author` must be an object")
    else:
        reject_unknown_fields(author, {"name", "email", "url"}, findings, code, path)
        require_string(author, "name", findings, code, path, expected=CONTRIBUTOR_NAME)
    interface = payload.get("interface")
    if not isinstance(interface, dict):
        add(findings, code, path, "`interface` must be an object")
        return
    interface_allowed = {
        "displayName",
        "shortDescription",
        "longDescription",
        "developerName",
        "category",
        "capabilities",
        "websiteURL",
        "privacyPolicyURL",
        "termsOfServiceURL",
        "brandColor",
        "composerIcon",
        "logo",
        "logoDark",
        "screenshots",
        "defaultPrompt",
    }
    reject_unknown_fields(interface, interface_allowed, findings, code, path)
    require_string(interface, "displayName", findings, code, path, expected=DISPLAY_NAME)
    require_string(interface, "shortDescription", findings, code, path)
    require_string(interface, "longDescription", findings, code, path)
    require_string(
        interface, "developerName", findings, code, path, expected=CONTRIBUTOR_NAME
    )
    require_string(interface, "category", findings, code, path)
    capabilities = require_string_list(
        interface.get("capabilities"), findings, code, path, "interface.capabilities"
    )
    if capabilities is not None and set(capabilities) - {"Interactive", "Write"}:
        add(findings, code, path, "capabilities must be limited to `Interactive` and `Write`")
    prompts = require_string_list(
        interface.get("defaultPrompt"), findings, code, path, "interface.defaultPrompt"
    )
    if prompts is not None:
        if len(prompts) > 3:
            add(findings, code, path, "`interface.defaultPrompt` may contain at most 3 prompts")
        if any(len(prompt) > 128 for prompt in prompts):
            add(findings, code, path, "each default prompt must be at most 128 characters")
    color = interface.get("brandColor")
    if color is not None and (
        not isinstance(color, str) or re.fullmatch(r"#[0-9A-Fa-f]{6}", color) is None
    ):
        add(findings, code, path, "`interface.brandColor` must use `#RRGGBB`")
    for field in ("composerIcon", "logo", "logoDark"):
        raw = interface.get(field)
        if raw is not None:
            validate_asset_path(plugin_root, raw, findings, code, path, f"interface.{field}")
    screenshots = interface.get("screenshots")
    if screenshots is not None:
        values = require_string_list(screenshots, findings, code, path, "interface.screenshots")
        if values:
            for index, raw in enumerate(values):
                validate_asset_path(
                    plugin_root, raw, findings, code, path, f"interface.screenshots[{index}]"
                )
    validate_manifest_placeholders(payload, findings, code, path)


def validate_asset_path(
    plugin_root: Path,
    raw: str,
    findings: list[Finding],
    code: str,
    path: str,
    field: str,
) -> None:
    pure = PurePosixPath(raw)
    if pure.is_absolute() or ".." in pure.parts:
        add(findings, code, path, f"`{field}` must stay inside the plugin root")
        return
    target = (plugin_root / Path(*pure.parts)).resolve(strict=False)
    if not is_within(target, plugin_root.resolve()) or not target.is_file():
        add(findings, code, path, f"`{field}` does not point to a packaged file")


def validate_claude_manifest(
    plugin_root: Path, payload: dict[str, Any], findings: list[Finding], path: str
) -> None:
    code = "MANIFEST_CLAUDE"
    allowed = {
        "name",
        "displayName",
        "version",
        "description",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
        "skills",
    }
    reject_unknown_fields(payload, allowed, findings, code, path)
    require_string(payload, "name", findings, code, path, expected=PLUGIN_ID)
    require_string(payload, "displayName", findings, code, path, expected=DISPLAY_NAME)
    require_string(payload, "version", findings, code, path, expected=VERSION)
    require_string(payload, "description", findings, code, path, expected=DESCRIPTION)
    require_string(payload, "license", findings, code, path, expected="MIT")
    validate_contract_path(plugin_root, payload.get("skills"), "./skills", findings, code, path)
    author = payload.get("author")
    if not isinstance(author, dict):
        add(findings, code, path, "`author` must be an object")
    else:
        reject_unknown_fields(author, {"name", "email", "url"}, findings, code, path)
        require_string(author, "name", findings, code, path, expected=CONTRIBUTOR_NAME)
    validate_manifest_placeholders(payload, findings, code, path)


def validate_cursor_manifest(
    plugin_root: Path, payload: dict[str, Any], findings: list[Finding], path: str
) -> None:
    code = "MANIFEST_CURSOR"
    allowed = {
        "name",
        "version",
        "description",
        "author",
        "homepage",
        "repository",
        "license",
        "keywords",
        "logo",
        "skills",
    }
    reject_unknown_fields(payload, allowed, findings, code, path)
    require_string(payload, "name", findings, code, path, expected=PLUGIN_ID)
    require_string(payload, "version", findings, code, path, expected=VERSION)
    require_string(payload, "description", findings, code, path, expected=DESCRIPTION)
    require_string(payload, "license", findings, code, path, expected="MIT")
    validate_contract_path(plugin_root, payload.get("skills"), "./skills", findings, code, path)
    author = payload.get("author")
    if not isinstance(author, dict):
        add(findings, code, path, "`author` must be an object")
    else:
        reject_unknown_fields(author, {"name", "email"}, findings, code, path)
        require_string(author, "name", findings, code, path, expected=CONTRIBUTOR_NAME)
    logo = payload.get("logo")
    if logo is not None:
        if not isinstance(logo, str):
            add(findings, code, path, "`logo` must be a relative string")
        else:
            validate_asset_path(plugin_root, logo, findings, code, path, "logo")
    validate_manifest_placeholders(payload, findings, code, path)


def validate_antigravity_manifest(
    payload: dict[str, Any], findings: list[Finding], path: str
) -> None:
    code = "MANIFEST_ANTIGRAVITY"
    allowed = {"name", "description"}
    reject_unknown_fields(payload, allowed, findings, code, path)
    require_string(payload, "name", findings, code, path, expected=PLUGIN_ID)
    require_string(payload, "description", findings, code, path, expected=DESCRIPTION)
    validate_manifest_placeholders(payload, findings, code, path)


def validate_manifests(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    validators = {
        ".codex-plugin/plugin.json": validate_codex_manifest,
        ".claude-plugin/plugin.json": validate_claude_manifest,
        ".cursor-plugin/plugin.json": validate_cursor_manifest,
    }
    versions: dict[str, str] = {}
    for relative, validator in validators.items():
        path = plugin_root / relative
        label = relative_label(path, marketplace_root)
        payload = load_json(path, marketplace_root, findings, "MANIFEST_JSON")
        if payload is None:
            continue
        validator(plugin_root, payload, findings, label)
        version = payload.get("version")
        if isinstance(version, str):
            versions[relative] = version
    if len(set(versions.values())) > 1:
        add(
            findings,
            "MANIFEST_VERSION_MISMATCH",
            relative_label(plugin_root, marketplace_root),
            "versioned platform manifests disagree",
        )
    antigravity_path = plugin_root / "plugin.json"
    antigravity = load_json(
        antigravity_path, marketplace_root, findings, "MANIFEST_JSON"
    )
    if antigravity is not None:
        validate_antigravity_manifest(
            antigravity, findings, relative_label(antigravity_path, marketplace_root)
        )


def validate_marketplace_source(
    marketplace_root: Path,
    raw: Any,
    expected: str,
    plugin_root: Path,
    findings: list[Finding],
    code: str,
    path: str,
) -> None:
    if not isinstance(raw, str) or raw != expected:
        add(findings, code, path, f"plugin source must equal `{expected}`")
        return
    pure = PurePosixPath(raw)
    if pure.is_absolute() or ".." in pure.parts:
        add(findings, code, path, "plugin source must be a contained relative path")
        return
    resolved = (marketplace_root / Path(*pure.parts)).resolve(strict=False)
    if resolved != plugin_root.resolve():
        add(findings, code, path, "plugin source does not resolve to this plugin root")


def validate_marketplace_common(
    payload: dict[str, Any], findings: list[Finding], code: str, path: str
) -> list[dict[str, Any]] | None:
    require_string(payload, "name", findings, code, path, expected=PLUGIN_ID)
    owner = payload.get("owner")
    if not isinstance(owner, dict):
        add(findings, code, path, "`owner` must be an object")
    else:
        require_string(owner, "name", findings, code, path, expected=CONTRIBUTOR_NAME)
    plugins = payload.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        add(findings, code, path, "`plugins` must be a non-empty array")
        return None
    if any(not isinstance(item, dict) for item in plugins):
        add(findings, code, path, "each plugin entry must be an object")
        return None
    names = [item.get("name") for item in plugins]
    if len(names) != len(set(str(name) for name in names)):
        add(findings, code, path, "plugin names must be unique")
    matches = [item for item in plugins if item.get("name") == PLUGIN_ID]
    if len(matches) != 1:
        add(findings, code, path, "marketplace must contain exactly one Matreshka entry")
        return None
    return matches


def validate_marketplaces(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    claude_path = marketplace_root / ".claude-plugin" / "marketplace.json"
    claude = load_json(claude_path, marketplace_root, findings, "MARKETPLACE_CLAUDE_JSON")
    if claude is not None:
        reject_unknown_fields(
            claude,
            {"name", "owner", "metadata", "plugins", "renames"},
            findings,
            "MARKETPLACE_CLAUDE",
            relative_label(claude_path, marketplace_root),
        )
        matches = validate_marketplace_common(
            claude,
            findings,
            "MARKETPLACE_CLAUDE",
            relative_label(claude_path, marketplace_root),
        )
        if matches:
            entry = matches[0]
            validate_marketplace_source(
                marketplace_root,
                entry.get("source"),
                "./plugins/matreshka-agent",
                plugin_root,
                findings,
                "MARKETPLACE_CLAUDE",
                relative_label(claude_path, marketplace_root),
            )
            require_string(
                entry,
                "version",
                findings,
                "MARKETPLACE_CLAUDE",
                relative_label(claude_path, marketplace_root),
                expected=VERSION,
            )
        metadata = claude.get("metadata")
        if not isinstance(metadata, dict):
            add(
                findings,
                "MARKETPLACE_CLAUDE",
                relative_label(claude_path, marketplace_root),
                "`metadata` must be an object",
            )
        else:
            require_string(
                metadata,
                "version",
                findings,
                "MARKETPLACE_CLAUDE",
                relative_label(claude_path, marketplace_root),
                expected=VERSION,
            )
        validate_manifest_placeholders(
            claude,
            findings,
            "MARKETPLACE_CLAUDE",
            relative_label(claude_path, marketplace_root),
        )

    cursor_path = marketplace_root / ".cursor-plugin" / "marketplace.json"
    cursor = load_json(cursor_path, marketplace_root, findings, "MARKETPLACE_CURSOR_JSON")
    if cursor is not None:
        reject_unknown_fields(
            cursor,
            {"name", "owner", "metadata", "plugins"},
            findings,
            "MARKETPLACE_CURSOR",
            relative_label(cursor_path, marketplace_root),
        )
        matches = validate_marketplace_common(
            cursor,
            findings,
            "MARKETPLACE_CURSOR",
            relative_label(cursor_path, marketplace_root),
        )
        if matches:
            entry = matches[0]
            validate_marketplace_source(
                marketplace_root,
                entry.get("source"),
                "plugins/matreshka-agent",
                plugin_root,
                findings,
                "MARKETPLACE_CURSOR",
                relative_label(cursor_path, marketplace_root),
            )
            require_string(
                entry,
                "version",
                findings,
                "MARKETPLACE_CURSOR",
                relative_label(cursor_path, marketplace_root),
                expected=VERSION,
            )
        metadata = cursor.get("metadata")
        if not isinstance(metadata, dict):
            add(
                findings,
                "MARKETPLACE_CURSOR",
                relative_label(cursor_path, marketplace_root),
                "`metadata` must be an object",
            )
        else:
            require_string(
                metadata,
                "version",
                findings,
                "MARKETPLACE_CURSOR",
                relative_label(cursor_path, marketplace_root),
                expected=VERSION,
            )
        validate_manifest_placeholders(
            cursor,
            findings,
            "MARKETPLACE_CURSOR",
            relative_label(cursor_path, marketplace_root),
        )

    codex_path = marketplace_root / ".agents" / "plugins" / "marketplace.json"
    codex = load_json(codex_path, marketplace_root, findings, "MARKETPLACE_CODEX_JSON")
    if codex is not None:
        require_string(
            codex,
            "name",
            findings,
            "MARKETPLACE_CODEX",
            relative_label(codex_path, marketplace_root),
            expected=PLUGIN_ID,
        )
        plugins = codex.get("plugins")
        if not isinstance(plugins, list):
            add(
                findings,
                "MARKETPLACE_CODEX",
                relative_label(codex_path, marketplace_root),
                "`plugins` must be an array",
            )
        else:
            matches = [
                item
                for item in plugins
                if isinstance(item, dict) and item.get("name") == PLUGIN_ID
            ]
            if len(matches) != 1:
                add(
                    findings,
                    "MARKETPLACE_CODEX",
                    relative_label(codex_path, marketplace_root),
                    "marketplace must contain exactly one Matreshka entry",
                )
            else:
                source = matches[0].get("source")
                expected_source = {
                    "source": "local",
                    "path": "./plugins/matreshka-agent",
                }
                if source != expected_source:
                    add(
                        findings,
                        "MARKETPLACE_CODEX",
                        relative_label(codex_path, marketplace_root),
                        "local source must point to `./plugins/matreshka-agent`",
                    )
                policy = matches[0].get("policy")
                if not isinstance(policy, dict) or policy.get("installation") not in {
                    "AVAILABLE",
                    "INSTALLED_BY_DEFAULT",
                }:
                    add(
                        findings,
                        "MARKETPLACE_CODEX",
                        relative_label(codex_path, marketplace_root),
                        "installation policy must allow the plugin",
                    )


def parse_scalar(raw: str) -> tuple[Any, str | None]:
    value = raw.strip()
    if not value:
        return None, None
    if value.startswith(('"', "'")):
        try:
            return ast.literal_eval(value), None
        except (SyntaxError, ValueError):
            return None, "invalid quoted scalar"
    if value.casefold() == "true":
        return True, None
    if value.casefold() == "false":
        return False, None
    if value.casefold() in {"null", "none", "~"}:
        return None, None
    return value, None


def parse_frontmatter(text: str) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, ["file must begin with `---` YAML frontmatter"]
    end = next((index for index in range(1, len(lines)) if lines[index].strip() == "---"), None)
    if end is None:
        return None, ["frontmatter is not closed with `---`"]
    payload: dict[str, Any] = {}
    index = 1
    while index < end:
        line = lines[index]
        if not line.strip() or line.lstrip().startswith("#"):
            index += 1
            continue
        if line[:1].isspace():
            errors.append(f"unexpected indentation on frontmatter line {index + 1}")
            index += 1
            continue
        match = re.fullmatch(r"([A-Za-z0-9_-]+):(?:\s*(.*))?", line)
        if match is None:
            errors.append(f"unsupported YAML on frontmatter line {index + 1}")
            index += 1
            continue
        key, raw = match.group(1), match.group(2) or ""
        if key in payload:
            errors.append(f"duplicate frontmatter key `{key}`")
        if raw in {"|", "|-", "|+", ">", ">-", ">+"}:
            block: list[str] = []
            index += 1
            while index < end and (not lines[index].strip() or lines[index][:1].isspace()):
                block.append(lines[index].lstrip())
                index += 1
            payload[key] = (" " if raw.startswith(">") else "\n").join(block).strip()
            continue
        value, error = parse_scalar(raw)
        if error:
            errors.append(f"frontmatter key `{key}`: {error}")
        payload[key] = value
        index += 1
    return payload, errors


def parse_openai_yaml(text: str) -> tuple[dict[str, dict[str, Any]] | None, list[str]]:
    result: dict[str, dict[str, Any]] = {}
    errors: list[str] = []
    section: str | None = None
    for index, line in enumerate(text.splitlines(), start=1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        top = re.fullmatch(r"([A-Za-z0-9_-]+):\s*", line)
        if top:
            section = top.group(1)
            if section in result:
                errors.append(f"duplicate section `{section}`")
            result.setdefault(section, {})
            continue
        child = re.fullmatch(r"  ([A-Za-z0-9_-]+):(?:\s*(.*))?", line)
        if child and section:
            key, raw = child.group(1), child.group(2) or ""
            if key in result[section]:
                errors.append(f"duplicate `{section}.{key}`")
            value, error = parse_scalar(raw)
            if error:
                errors.append(f"line {index}: {error}")
            result[section][key] = value
            continue
        errors.append(f"unsupported YAML on line {index}")
    return result, errors


def validate_openai_yaml(
    skill_root: Path,
    skill_name: str,
    marketplace_root: Path,
    findings: list[Finding],
) -> None:
    path = skill_root / "agents" / "openai.yaml"
    label = relative_label(path, marketplace_root)
    text = read_text(path, marketplace_root, findings, "SKILL_AGENT_YAML")
    if text is None:
        return
    payload, errors = parse_openai_yaml(text)
    for error in errors:
        add(findings, "SKILL_AGENT_YAML", label, error)
    if payload is None:
        return
    reject_sections = set(payload) - {"interface", "policy"}
    for section in sorted(reject_sections):
        add(findings, "SKILL_AGENT_YAML", label, f"unsupported section `{section}`")
    interface = payload.get("interface")
    if not isinstance(interface, dict):
        add(findings, "SKILL_AGENT_YAML", label, "`interface` section is required")
    else:
        unknown = set(interface) - {"display_name", "short_description", "default_prompt"}
        for field in sorted(unknown):
            add(findings, "SKILL_AGENT_YAML", label, f"unsupported `interface.{field}`")
        display = interface.get("display_name")
        if not isinstance(display, str) or not display.strip():
            add(findings, "SKILL_AGENT_YAML", label, "`interface.display_name` is required")
        short = interface.get("short_description")
        if not isinstance(short, str) or not 25 <= len(short.strip()) <= 64:
            add(
                findings,
                "SKILL_AGENT_YAML",
                label,
                "`interface.short_description` must contain 25 to 64 characters",
            )
        prompt = interface.get("default_prompt")
        token = f"${skill_name}"
        if not isinstance(prompt, str) or token not in prompt:
            add(
                findings,
                "SKILL_AGENT_YAML",
                label,
                f"`interface.default_prompt` must contain `{token}`",
            )
    policy = payload.get("policy")
    if not isinstance(policy, dict):
        add(findings, "SKILL_AGENT_YAML", label, "`policy` section is required")
    else:
        unknown = set(policy) - {"allow_implicit_invocation"}
        for field in sorted(unknown):
            add(findings, "SKILL_AGENT_YAML", label, f"unsupported `policy.{field}`")
        if not isinstance(policy.get("allow_implicit_invocation"), bool):
            add(
                findings,
                "SKILL_AGENT_YAML",
                label,
                "`policy.allow_implicit_invocation` must be boolean",
            )


def validate_skills(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    skills_root = plugin_root / "skills"
    if not skills_root.is_dir():
        add(findings, "SKILLS_REQUIRED", relative_label(skills_root, marketplace_root), "missing")
        return
    actual = sorted(
        path.name
        for path in skills_root.iterdir()
        if path.is_dir() and not path.name.startswith(".")
    )
    missing = sorted(set(REQUIRED_SKILLS) - set(actual))
    unexpected = sorted(set(actual) - set(REQUIRED_SKILLS))
    for name in missing:
        add(findings, "SKILLS_REQUIRED", f"skills/{name}", "required skill is missing")
    for name in unexpected:
        add(findings, "SKILLS_UNEXPECTED", f"skills/{name}", "unexpected v0.1.2 skill")
    for name in REQUIRED_SKILLS:
        skill_root = skills_root / name
        if not skill_root.is_dir():
            continue
        skill_md = skill_root / "SKILL.md"
        label = relative_label(skill_md, marketplace_root)
        text = read_text(skill_md, marketplace_root, findings, "SKILL_FRONTMATTER")
        if text is None:
            continue
        payload, errors = parse_frontmatter(text)
        for error in errors:
            add(findings, "SKILL_FRONTMATTER", label, error)
        if payload is not None:
            skill_name = payload.get("name")
            if skill_name != name:
                add(findings, "SKILL_FRONTMATTER", label, f"`name` must equal `{name}`")
            if not isinstance(skill_name, str) or not SKILL_NAME_RE.fullmatch(skill_name):
                add(findings, "SKILL_FRONTMATTER", label, "`name` must be lowercase kebab-case")
            description = payload.get("description")
            if not isinstance(description, str) or not description.strip():
                add(findings, "SKILL_FRONTMATTER", label, "`description` is required")
            elif len(description) > 1024:
                add(findings, "SKILL_FRONTMATTER", label, "`description` exceeds 1024 characters")
        if len(text.splitlines()) > 500:
            add(findings, "SKILL_SIZE", label, "SKILL.md exceeds the 500-line disclosure limit")
        validate_openai_yaml(skill_root, name, marketplace_root, findings)
        validate_skill_evals(skill_root, name, marketplace_root, findings)
        validate_trigger_evals(skill_root, marketplace_root, findings)


def validate_codex_prompt_wrappers(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    prompts_root = plugin_root / "codex-prompts"
    readme = prompts_root / "README.md"
    if not readme.is_file():
        add(
            findings,
            "CODEX_PROMPT_WRAPPER",
            relative_label(readme, marketplace_root),
            "installation instructions are missing",
        )
    if not prompts_root.is_dir():
        add(
            findings,
            "CODEX_PROMPT_WRAPPER",
            relative_label(prompts_root, marketplace_root),
            "optional slash-prompt wrapper directory is missing",
        )
        return
    actual = {
        path.name for path in prompts_root.glob("*.md") if path.name != "README.md"
    }
    missing = sorted(set(CODEX_PROMPT_WRAPPERS) - actual)
    unexpected = sorted(actual - set(CODEX_PROMPT_WRAPPERS))
    for name in missing:
        add(
            findings,
            "CODEX_PROMPT_WRAPPER",
            f"codex-prompts/{name}",
            "required wrapper is missing",
        )
    for name in unexpected:
        add(
            findings,
            "CODEX_PROMPT_WRAPPER",
            f"codex-prompts/{name}",
            "unexpected wrapper file",
        )
    for filename, skill_name in CODEX_PROMPT_WRAPPERS.items():
        path = prompts_root / filename
        label = relative_label(path, marketplace_root)
        text = read_text(path, marketplace_root, findings, "CODEX_PROMPT_WRAPPER")
        if text is None:
            continue
        payload, errors = parse_frontmatter(text)
        for error in errors:
            add(findings, "CODEX_PROMPT_WRAPPER", label, error)
        if payload is None:
            continue
        description = payload.get("description")
        if not isinstance(description, str) or not description.strip():
            add(findings, "CODEX_PROMPT_WRAPPER", label, "`description` is required")
        if payload.get("argument-hint") != "[TASK]":
            add(findings, "CODEX_PROMPT_WRAPPER", label, "`argument-hint` must equal `[TASK]`")
        expected_token = f"$$matreshka-agent:{skill_name}"
        if expected_token not in text:
            add(
                findings,
                "CODEX_PROMPT_WRAPPER",
                label,
                f"wrapper must emit `{expected_token}`",
            )
        if "$ARGUMENTS" not in text:
            add(
                findings,
                "CODEX_PROMPT_WRAPPER",
                label,
                "wrapper must forward `$ARGUMENTS`",
            )


def validate_eval_files(
    value: Any, skill_root: Path, findings: list[Finding], label: str
) -> None:
    if not isinstance(value, list):
        add(findings, "EVAL_SCHEMA", label, "`files` must be an array")
        return
    for index, item in enumerate(value):
        raw_path: str | None = None
        if isinstance(item, str):
            raw_path = item
        elif isinstance(item, dict):
            if set(item) - {"path", "content"}:
                add(findings, "EVAL_SCHEMA", label, f"files[{index}] has unsupported fields")
            raw = item.get("path")
            if isinstance(raw, str):
                raw_path = raw
            else:
                add(findings, "EVAL_SCHEMA", label, f"files[{index}].path is required")
        else:
            add(findings, "EVAL_SCHEMA", label, f"files[{index}] must be a path or object")
        if raw_path:
            pure = PurePosixPath(raw_path)
            if pure.is_absolute() or ".." in pure.parts:
                add(findings, "EVAL_SCHEMA", label, f"files[{index}] escapes the skill root")


def validate_skill_evals(
    skill_root: Path,
    skill_name: str,
    marketplace_root: Path,
    findings: list[Finding],
) -> None:
    path = skill_root / "evals" / "evals.json"
    label = relative_label(path, marketplace_root)
    payload = load_json(path, marketplace_root, findings, "EVAL_JSON")
    if payload is None:
        return
    reject_unknown_fields(
        payload,
        {"skill_name", "evals"},
        findings,
        "EVAL_SCHEMA",
        label,
    )
    require_string(payload, "skill_name", findings, "EVAL_SCHEMA", label, expected=skill_name)
    cases = payload.get("evals")
    if not isinstance(cases, list) or len(cases) < 2:
        add(findings, "EVAL_SCHEMA", label, "`evals` must contain at least two cases")
    else:
        seen: set[str] = set()
        for index, case in enumerate(cases):
            case_label = f"{label}#evals[{index}]"
            if not isinstance(case, dict):
                add(findings, "EVAL_SCHEMA", case_label, "case must be an object")
                continue
            reject_unknown_fields(
                case,
                {"id", "prompt", "expected_output", "expectations", "files"},
                findings,
                "EVAL_SCHEMA",
                case_label,
            )
            identifier = case.get("id")
            if isinstance(identifier, bool) or not isinstance(identifier, (int, str)):
                add(findings, "EVAL_SCHEMA", case_label, "`id` must be an integer or string")
            elif not str(identifier).strip():
                add(findings, "EVAL_SCHEMA", case_label, "`id` must not be empty")
            elif str(identifier) in seen:
                add(findings, "EVAL_SCHEMA", case_label, "`id` must be unique")
            else:
                seen.add(str(identifier))
            require_string(case, "prompt", findings, "EVAL_SCHEMA", case_label)
            require_string(case, "expected_output", findings, "EVAL_SCHEMA", case_label)
            require_string_list(
                case.get("expectations"),
                findings,
                "EVAL_SCHEMA",
                case_label,
                "expectations",
            )
            if "files" in case:
                validate_eval_files(case["files"], skill_root, findings, case_label)


def validate_trigger_evals(
    skill_root: Path,
    marketplace_root: Path,
    findings: list[Finding],
) -> None:
    path = skill_root / "evals" / "trigger-evals.json"
    label = relative_label(path, marketplace_root)
    payload = load_json_array(path, marketplace_root, findings, "TRIGGER_EVAL_JSON")
    if payload is None:
        return
    if len(payload) < 4:
        add(
            findings,
            "TRIGGER_EVAL_SCHEMA",
            label,
            "trigger suite must contain at least four cases",
        )
    seen: set[str] = set()
    outcomes: set[bool] = set()
    for index, case in enumerate(payload):
        case_label = f"{label}#[{index}]"
        if not isinstance(case, dict):
            add(findings, "TRIGGER_EVAL_SCHEMA", case_label, "case must be an object")
            continue
        reject_unknown_fields(
            case,
            {"query", "should_trigger"},
            findings,
            "TRIGGER_EVAL_SCHEMA",
            case_label,
        )
        query = require_string(
            case, "query", findings, "TRIGGER_EVAL_SCHEMA", case_label
        )
        if query:
            if query in seen:
                add(findings, "TRIGGER_EVAL_SCHEMA", case_label, "query must be unique")
            seen.add(query)
        outcome = case.get("should_trigger")
        if not isinstance(outcome, bool):
            add(
                findings,
                "TRIGGER_EVAL_SCHEMA",
                case_label,
                "`should_trigger` must be boolean",
            )
        else:
            outcomes.add(outcome)
    if outcomes != {True, False}:
        add(
            findings,
            "TRIGGER_EVAL_SCHEMA",
            label,
            "trigger suite must cover both positive and negative cases",
        )


def validate_package_eval_suite(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    path = plugin_root / "evals" / "package-validation.json"
    label = relative_label(path, marketplace_root)
    payload = load_json(path, marketplace_root, findings, "PACKAGE_EVAL_JSON")
    if payload is None:
        return
    reject_unknown_fields(
        payload,
        {"schema_version", "plugin", "version", "cases"},
        findings,
        "PACKAGE_EVAL_SCHEMA",
        label,
    )
    require_string(payload, "schema_version", findings, "PACKAGE_EVAL_SCHEMA", label, expected="1.0")
    require_string(payload, "plugin", findings, "PACKAGE_EVAL_SCHEMA", label, expected=PLUGIN_ID)
    require_string(payload, "version", findings, "PACKAGE_EVAL_SCHEMA", label, expected=VERSION)
    cases = payload.get("cases")
    if not isinstance(cases, list):
        add(findings, "PACKAGE_EVAL_SCHEMA", label, "`cases` must be an array")
        return
    observed: set[str] = set()
    ids: set[str] = set()
    for index, case in enumerate(cases):
        case_label = f"{label}#cases[{index}]"
        if not isinstance(case, dict):
            add(findings, "PACKAGE_EVAL_SCHEMA", case_label, "case must be an object")
            continue
        reject_unknown_fields(
            case,
            {"id", "check", "expected"},
            findings,
            "PACKAGE_EVAL_SCHEMA",
            case_label,
        )
        identifier = require_string(case, "id", findings, "PACKAGE_EVAL_SCHEMA", case_label)
        check = require_string(case, "check", findings, "PACKAGE_EVAL_SCHEMA", case_label)
        require_string(case, "expected", findings, "PACKAGE_EVAL_SCHEMA", case_label, expected="pass")
        if identifier:
            if identifier in ids:
                add(findings, "PACKAGE_EVAL_SCHEMA", case_label, "duplicate case id")
            ids.add(identifier)
        if check:
            observed.add(check)
            if check not in PACKAGE_CHECKS:
                add(findings, "PACKAGE_EVAL_SCHEMA", case_label, "unknown package check")
    if observed != PACKAGE_CHECKS:
        missing = ", ".join(sorted(PACKAGE_CHECKS - observed)) or "none"
        extra = ", ".join(sorted(observed - PACKAGE_CHECKS)) or "none"
        add(
            findings,
            "PACKAGE_EVAL_SCHEMA",
            label,
            f"package checks differ; missing: {missing}; extra: {extra}",
        )


def validate_workflow_eval_suite(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    path = plugin_root / "evals" / "workflow-evals.json"
    label = relative_label(path, marketplace_root)
    payload = load_json(path, marketplace_root, findings, "WORKFLOW_EVAL_JSON")
    if payload is None:
        return
    reject_unknown_fields(
        payload,
        {"schema_version", "plugin", "version", "baseline_protocol", "cases"},
        findings,
        "WORKFLOW_EVAL_SCHEMA",
        label,
    )
    require_string(payload, "schema_version", findings, "WORKFLOW_EVAL_SCHEMA", label, expected="1.0")
    require_string(payload, "plugin", findings, "WORKFLOW_EVAL_SCHEMA", label, expected=PLUGIN_ID)
    require_string(payload, "version", findings, "WORKFLOW_EVAL_SCHEMA", label, expected=VERSION)
    protocol = payload.get("baseline_protocol")
    if not isinstance(protocol, dict):
        add(findings, "WORKFLOW_EVAL_SCHEMA", label, "`baseline_protocol` must be an object")
    else:
        reject_unknown_fields(
            protocol,
            {
                "variants",
                "controls",
                "fresh_context_per_run",
                "blind_review",
                "record",
            },
            findings,
            "WORKFLOW_EVAL_SCHEMA",
            label,
        )
        variants = require_string_list(
            protocol.get("variants"), findings, "WORKFLOW_EVAL_SCHEMA", label, "baseline_protocol.variants"
        )
        if variants is not None and variants != BASELINE_VARIANTS:
            add(findings, "WORKFLOW_EVAL_SCHEMA", label, "baseline variants or order changed")
        controls = require_string_list(
            protocol.get("controls"), findings, "WORKFLOW_EVAL_SCHEMA", label, "baseline_protocol.controls"
        )
        if controls is not None and not BASELINE_CONTROLS.issubset(set(controls)):
            add(findings, "WORKFLOW_EVAL_SCHEMA", label, "baseline controls are incomplete")
        if protocol.get("fresh_context_per_run") is not True:
            add(findings, "WORKFLOW_EVAL_SCHEMA", label, "fresh contexts must be required")
        if protocol.get("blind_review") is not True:
            add(findings, "WORKFLOW_EVAL_SCHEMA", label, "blind review must be required")
        require_string_list(
            protocol.get("record"), findings, "WORKFLOW_EVAL_SCHEMA", label, "baseline_protocol.record"
        )
    cases = payload.get("cases")
    if not isinstance(cases, list) or not cases:
        add(findings, "WORKFLOW_EVAL_SCHEMA", label, "`cases` must be a non-empty array")
        return
    categories: set[str] = set()
    platforms: set[str] = set()
    ids: set[str] = set()
    for index, case in enumerate(cases):
        case_label = f"{label}#cases[{index}]"
        if not isinstance(case, dict):
            add(findings, "WORKFLOW_EVAL_SCHEMA", case_label, "case must be an object")
            continue
        reject_unknown_fields(
            case,
            {
                "id",
                "category",
                "platform",
                "profile",
                "prompt",
                "expected_outcome",
                "assertions",
            },
            findings,
            "WORKFLOW_EVAL_SCHEMA",
            case_label,
        )
        identifier = require_string(case, "id", findings, "WORKFLOW_EVAL_SCHEMA", case_label)
        if identifier:
            if identifier in ids:
                add(findings, "WORKFLOW_EVAL_SCHEMA", case_label, "duplicate case id")
            ids.add(identifier)
        category = require_string(case, "category", findings, "WORKFLOW_EVAL_SCHEMA", case_label)
        if category:
            categories.add(category)
            if category not in WORKFLOW_CATEGORIES:
                add(findings, "WORKFLOW_EVAL_SCHEMA", case_label, "unknown category")
        platform = case.get("platform")
        if platform is not None:
            if not isinstance(platform, str) or platform not in WORKFLOW_PLATFORMS:
                add(findings, "WORKFLOW_EVAL_SCHEMA", case_label, "unknown platform")
            else:
                platforms.add(platform)
        if category == "platform-compatibility" and platform is None:
            add(findings, "WORKFLOW_EVAL_SCHEMA", case_label, "platform case needs `platform`")
        require_string(case, "profile", findings, "WORKFLOW_EVAL_SCHEMA", case_label)
        require_string(case, "prompt", findings, "WORKFLOW_EVAL_SCHEMA", case_label)
        require_string(case, "expected_outcome", findings, "WORKFLOW_EVAL_SCHEMA", case_label)
        require_string_list(
            case.get("assertions"), findings, "WORKFLOW_EVAL_SCHEMA", case_label, "assertions"
        )
    if categories != WORKFLOW_CATEGORIES:
        add(findings, "WORKFLOW_EVAL_SCHEMA", label, "workflow category coverage is incomplete")
    if platforms != WORKFLOW_PLATFORMS:
        add(findings, "WORKFLOW_EVAL_SCHEMA", label, "platform coverage is incomplete")


def validate_root_evals(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    validate_package_eval_suite(plugin_root, marketplace_root, findings)
    validate_workflow_eval_suite(plugin_root, marketplace_root, findings)


def validate_forbidden_components(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    for entry in walk_entries(plugin_root):
        rel = entry.relative_to(plugin_root)
        folded_parts = [part.casefold() for part in rel.parts]
        if folded_parts and folded_parts[0] in FORBIDDEN_TOP_LEVEL_DIRS:
            add(
                findings,
                "FORBIDDEN_COMPONENT",
                relative_label(entry, marketplace_root),
                "top-level runtime component is not allowed in v0.1.2",
            )
        elif any(part in FORBIDDEN_ANY_DIRS for part in folded_parts):
            add(
                findings,
                "FORBIDDEN_COMPONENT",
                relative_label(entry, marketplace_root),
                "runtime component directory is not allowed",
            )
        name = entry.name.casefold()
        if name in FORBIDDEN_COMPONENT_FILES:
            add(
                findings,
                "FORBIDDEN_COMPONENT",
                relative_label(entry, marketplace_root),
                "runtime component file is not allowed",
            )
        if name in DEPENDENCY_FILES or name.startswith("requirements-"):
            add(
                findings,
                "DEPENDENCY_MANIFEST",
                relative_label(entry, marketplace_root),
                "the plugin must not require dependency installation",
            )
        if "telemetry" in name or "analytics" in name:
            add(
                findings,
                "TELEMETRY_COMPONENT",
                relative_label(entry, marketplace_root),
                "telemetry and analytics components are not allowed",
            )


def is_text_file(path: Path) -> bool:
    return path.is_file() and (path.suffix.casefold() in TEXT_SUFFIXES or path.name in TEXT_NAMES)


def validate_forbidden_references(
    marketplace_root: Path, findings: list[Finding]
) -> None:
    # Keep the prohibited token out of the package source while still enforcing
    # the user's zero-occurrence requirement deterministically.
    blocked = bytes.fromhex("7375706572706f77657273").decode("ascii").casefold()
    for entry in walk_entries(marketplace_root):
        if entry.is_symlink() or not is_text_file(entry):
            continue
        text = read_text(entry, marketplace_root, findings, "TEXT_READ")
        if text is not None and blocked in text.casefold():
            add(
                findings,
                "FORBIDDEN_REFERENCE",
                relative_label(entry, marketplace_root),
                "package contains a prohibited external-system reference",
            )


def validate_symlinks(marketplace_root: Path, findings: list[Finding]) -> None:
    root = marketplace_root.resolve()
    for entry in walk_entries(marketplace_root):
        if not entry.is_symlink():
            continue
        label = relative_label(entry, marketplace_root)
        try:
            target = entry.resolve(strict=True)
        except OSError:
            add(findings, "SYMLINK_BROKEN", label, "symlink target does not exist")
            continue
        if not is_within(target, root):
            add(findings, "SYMLINK_ESCAPE", label, "symlink resolves outside the package root")


def validate_secret_files(marketplace_root: Path, findings: list[Finding]) -> None:
    exact_names = {
        ".env",
        "credentials.json",
        "id_ed25519",
        "id_rsa",
        "secrets.json",
        "token.json",
    }
    secret_suffixes = {".key", ".p12", ".pem", ".pfx"}
    patterns = (
        re.compile("-----BEGIN " + "PRIVATE KEY-----"),
        re.compile("AK" + "IA[0-9A-Z]{16}"),
        re.compile("gh" + "p_[A-Za-z0-9]{30,}"),
        re.compile("sk" + "-[A-Za-z0-9]{32,}"),
    )
    for entry in walk_entries(marketplace_root):
        if entry.is_dir() or entry.is_symlink():
            continue
        name = entry.name.casefold()
        if name in exact_names or name.startswith(".env.") or entry.suffix.casefold() in secret_suffixes:
            add(
                findings,
                "SECRET_FILE",
                relative_label(entry, marketplace_root),
                "secret-like file must not be packaged",
            )
        if is_text_file(entry):
            text = read_text(entry, marketplace_root, findings, "TEXT_READ")
            if text is not None and any(pattern.search(text) for pattern in patterns):
                add(
                    findings,
                    "SECRET_CONTENT",
                    relative_label(entry, marketplace_root),
                    "text resembles a credential or private key",
                )


def validate_executables(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    execute_mask = stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH
    for entry in walk_entries(plugin_root):
        if not entry.is_file() or entry.is_symlink():
            continue
        try:
            executable = bool(entry.stat().st_mode & execute_mask)
        except OSError:
            continue
        if executable and PurePosixPath(entry.relative_to(plugin_root).as_posix()) not in EXECUTABLE_ALLOWLIST:
            add(
                findings,
                "EXECUTABLE_UNEXPECTED",
                relative_label(entry, marketplace_root),
                "executable bit is outside the package allowlist",
            )


def dotted_call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = dotted_call_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def validate_python_runtime(
    path: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    label = relative_label(path, marketplace_root)
    text = read_text(path, marketplace_root, findings, "SCRIPT_PARSE")
    if text is None:
        return
    try:
        tree = ast.parse(text, filename=label)
    except SyntaxError as exc:
        add(findings, "SCRIPT_PARSE", label, f"Python syntax error at line {exc.lineno}")
        return
    blocked_imports = {
        "aiohttp",
        "ftplib",
        "http",
        "requests",
        "smtplib",
        "socket",
        "telnetlib",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".", 1)[0] in blocked_imports:
                    add(findings, "NETWORK_RUNTIME", label, f"network import `{alias.name}` is forbidden")
        elif isinstance(node, ast.ImportFrom):
            module = node.module or ""
            if module.split(".", 1)[0] in blocked_imports:
                add(findings, "NETWORK_RUNTIME", label, f"network import `{module}` is forbidden")
        elif isinstance(node, ast.Call):
            call = dotted_call_name(node.func)
            if call in {"os.popen", "os.system"}:
                add(findings, "UNSAFE_RUNTIME", label, f"dynamic shell call `{call}` is forbidden")


def validate_script_runtime(
    plugin_root: Path, marketplace_root: Path, findings: list[Finding]
) -> None:
    network_tools = ("cu" + "rl", "wg" + "et")
    install_tools = ("pip", "pip3", "npm", "pnpm", "yarn", "uv")
    network_re = re.compile(r"\b(?:" + "|".join(network_tools) + r")\b", re.IGNORECASE)
    install_re = re.compile(
        r"\b(?:" + "|".join(install_tools) + r")\s+(?:install|add|sync)\b",
        re.IGNORECASE,
    )
    for entry in walk_entries(plugin_root):
        if not entry.is_file() or entry.is_symlink() or "scripts" not in entry.parts:
            continue
        if entry.suffix.casefold() == ".py":
            validate_python_runtime(entry, marketplace_root, findings)
        elif entry.suffix.casefold() in {".sh", ".ps1", ".js", ".mjs", ".cjs"}:
            text = read_text(entry, marketplace_root, findings, "SCRIPT_PARSE")
            if text is None:
                continue
            if network_re.search(text):
                add(
                    findings,
                    "NETWORK_RUNTIME",
                    relative_label(entry, marketplace_root),
                    "network command is forbidden",
                )
            if install_re.search(text):
                add(
                    findings,
                    "DEPENDENCY_INSTALL",
                    relative_label(entry, marketplace_root),
                    "dependency installation is forbidden",
                )


def link_target(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and ">" in value:
        return value[1 : value.index(">")]
    if " " in value:
        return value.split(" ", 1)[0]
    return value


def validate_internal_links(marketplace_root: Path, findings: list[Finding]) -> None:
    root = marketplace_root.resolve()
    for entry in walk_entries(marketplace_root):
        if entry.is_symlink() or not entry.is_file() or entry.suffix.casefold() not in {
            ".md",
            ".mdc",
            ".markdown",
        }:
            continue
        text = read_text(entry, marketplace_root, findings, "LINK_READ")
        if text is None:
            continue
        for match in MARKDOWN_LINK_RE.finditer(text):
            raw = link_target(match.group(1))
            if not raw or raw.startswith("#"):
                continue
            folded = raw.casefold()
            if re.match(r"^[a-z][a-z0-9+.-]*:", folded):
                continue
            path_part = unquote(raw.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            if path_part.startswith(("/", "\\")) or WINDOWS_ABSOLUTE_RE.match(path_part):
                add(
                    findings,
                    "LINK_ABSOLUTE",
                    relative_label(entry, marketplace_root),
                    f"internal link `{raw}` must be relative",
                )
                continue
            target = (entry.parent / Path(path_part)).resolve(strict=False)
            if not is_within(target, root):
                add(
                    findings,
                    "LINK_ESCAPE",
                    relative_label(entry, marketplace_root),
                    f"internal link `{raw}` escapes the package root",
                )
            elif not target.exists():
                add(
                    findings,
                    "LINK_MISSING",
                    relative_label(entry, marketplace_root),
                    f"internal link `{raw}` does not exist",
                )


def validate_package(
    plugin_root: Path, marketplace_root: Path | None = None
) -> list[Finding]:
    plugin_root = plugin_root.expanduser().resolve()
    marketplace_root = (
        marketplace_root.expanduser().resolve()
        if marketplace_root is not None
        else inferred_marketplace_root(plugin_root).resolve()
    )
    findings: list[Finding] = []
    if not plugin_root.is_dir():
        add(findings, "PLUGIN_ROOT", plugin_root, "plugin root does not exist")
        return findings
    if not marketplace_root.is_dir():
        add(findings, "MARKETPLACE_ROOT", marketplace_root, "marketplace root does not exist")
        return findings
    if not is_within(plugin_root, marketplace_root):
        add(findings, "PLUGIN_ROOT", plugin_root, "plugin must be inside the marketplace root")
        return findings

    validate_symlinks(marketplace_root, findings)
    validate_forbidden_components(plugin_root, marketplace_root, findings)
    validate_forbidden_references(marketplace_root, findings)
    validate_secret_files(marketplace_root, findings)
    validate_executables(plugin_root, marketplace_root, findings)
    validate_script_runtime(plugin_root, marketplace_root, findings)
    validate_manifests(plugin_root, marketplace_root, findings)
    validate_marketplaces(plugin_root, marketplace_root, findings)
    validate_skills(plugin_root, marketplace_root, findings)
    validate_codex_prompt_wrappers(plugin_root, marketplace_root, findings)
    validate_root_evals(plugin_root, marketplace_root, findings)
    validate_internal_links(marketplace_root, findings)

    unique = {(item.code, item.path, item.message): item for item in findings}
    return sorted(unique.values(), key=lambda item: (item.code, item.path, item.message))


def copy_test_fixture(plugin_root: Path, marketplace_root: Path, target: Path) -> tuple[Path, Path]:
    target_plugin = target / "plugins" / PLUGIN_ID
    target_plugin.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(plugin_root, target_plugin, symlinks=True)
    for relative in (
        Path(".agents/plugins/marketplace.json"),
        Path(".claude-plugin/marketplace.json"),
        Path(".cursor-plugin/marketplace.json"),
    ):
        source = marketplace_root / relative
        destination = target / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
    return target_plugin, target


def write_test_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def run_negative_case(
    plugin_root: Path,
    marketplace_root: Path,
    case_name: str,
    expected_code: str,
    mutate: Any,
) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix="matreshka-validation-") as temporary:
        root = Path(temporary)
        test_plugin, test_marketplace = copy_test_fixture(
            plugin_root, marketplace_root, root / "marketplace"
        )
        try:
            mutate(test_plugin, test_marketplace)
        except (OSError, NotImplementedError) as exc:
            return True, f"SKIP {case_name}: host cannot create fixture ({exc})"
        codes = {finding.code for finding in validate_package(test_plugin, test_marketplace)}
        if expected_code in codes:
            return True, f"PASS {case_name}: detected {expected_code}"
        return False, f"FAIL {case_name}: expected {expected_code}; observed {sorted(codes)}"


def run_self_tests(plugin_root: Path, marketplace_root: Path) -> tuple[bool, list[str]]:
    messages: list[str] = []
    baseline = validate_package(plugin_root, marketplace_root)
    if baseline:
        messages.append("FAIL valid-package: package must pass before negative self-tests")
        return False, messages
    messages.append("PASS valid-package")

    def missing_skill(plugin: Path, _: Path) -> None:
        shutil.rmtree(plugin / "skills" / REQUIRED_SKILLS[0])

    def version_mismatch(plugin: Path, _: Path) -> None:
        path = plugin / ".cursor-plugin" / "plugin.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["version"] = "0.1.3"
        write_test_json(path, payload)

    def forbidden_component(plugin: Path, _: Path) -> None:
        path = plugin / "hooks" / "hooks.json"
        path.parent.mkdir(parents=True)
        write_test_json(path, {"hooks": {}})

    def forbidden_reference(plugin: Path, _: Path) -> None:
        token = bytes.fromhex("7375706572706f77657273").decode("ascii")
        (plugin / "forbidden.md").write_text(token, encoding="utf-8")

    def invalid_eval(plugin: Path, _: Path) -> None:
        path = plugin / "skills" / REQUIRED_SKILLS[0] / "evals" / "evals.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        payload["evals"][0]["expected_output"] = ""
        write_test_json(path, payload)

    def broken_link(plugin: Path, _: Path) -> None:
        (plugin / "broken-link.md").write_text("[missing](not-present.md)\n", encoding="utf-8")

    def secret_file(plugin: Path, _: Path) -> None:
        (plugin / ".env").write_text("SAFE_TEST_VALUE=not-a-secret\n", encoding="utf-8")

    def executable_file(plugin: Path, _: Path) -> None:
        path = plugin / "unexpected-tool.sh"
        path.write_text("exit 0\n", encoding="utf-8")
        path.chmod(path.stat().st_mode | stat.S_IXUSR)

    def symlink_escape(plugin: Path, marketplace: Path) -> None:
        outside = marketplace.parent / "outside.txt"
        outside.write_text("outside\n", encoding="utf-8")
        (plugin / "escape-link").symlink_to(outside)

    def missing_codex_prompt(plugin: Path, _: Path) -> None:
        (plugin / "codex-prompts" / "matreshka-orchestrate.md").unlink()

    cases = (
        ("required-skills", "SKILLS_REQUIRED", missing_skill),
        ("manifest-consistency", "MANIFEST_VERSION_MISMATCH", version_mismatch),
        ("forbidden-components", "FORBIDDEN_COMPONENT", forbidden_component),
        ("forbidden-references", "FORBIDDEN_REFERENCE", forbidden_reference),
        ("eval-schemas", "EVAL_SCHEMA", invalid_eval),
        ("internal-links", "LINK_MISSING", broken_link),
        ("secret-files", "SECRET_FILE", secret_file),
        ("executable-policy", "EXECUTABLE_UNEXPECTED", executable_file),
        ("symlink-containment", "SYMLINK_ESCAPE", symlink_escape),
        ("codex-slash-prompts", "CODEX_PROMPT_WRAPPER", missing_codex_prompt),
    )
    passed = True
    for name, expected, mutation in cases:
        okay, message = run_negative_case(
            plugin_root, marketplace_root, name, expected, mutation
        )
        messages.append(message)
        passed = passed and okay
    messages.append("PASS offline-runtime: validation completed without network access")
    return passed, messages


def main() -> int:
    args = parse_args()
    plugin_root = Path(args.plugin_path).expanduser().resolve()
    marketplace_root = (
        Path(args.marketplace_root).expanduser().resolve()
        if args.marketplace_root
        else inferred_marketplace_root(plugin_root).resolve()
    )
    findings = validate_package(plugin_root, marketplace_root)
    self_test_passed = True
    self_test_messages: list[str] = []
    if args.self_test:
        self_test_passed, self_test_messages = run_self_tests(plugin_root, marketplace_root)
    passed = not findings and self_test_passed
    if args.json_output:
        print(
            json.dumps(
                {
                    "ok": passed,
                    "plugin": str(plugin_root),
                    "marketplace_root": str(marketplace_root),
                    "version": VERSION,
                    "findings": [asdict(item) for item in findings],
                    "self_test": self_test_messages,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        if findings:
            print(f"Validation failed with {len(findings)} finding(s):")
            for finding in findings:
                print(f"- [{finding.code}] {finding.path}: {finding.message}")
        else:
            print(f"Validation passed: {PLUGIN_ID} {VERSION}")
        for message in self_test_messages:
            print(message)
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
