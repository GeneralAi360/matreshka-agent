# Changelog

All notable changes to Matreshka Agent are recorded here.

## 0.1.1 - 2026-07-16

### Added

- Nine optional Codex custom-prompt wrappers, including `/prompts:matreshka-orchestrate`.
- Offline validation that checks every wrapper emits the matching explicit skill invocation.

### Compatibility

- Claude Code, Cursor, and Antigravity keep their native skill-to-slash invocation paths; no duplicate command component is installed for them.

## 0.1.0 - 2026-07-16

### Added

- Nine portable skills for coding-agent development workflows.
- Native manifests for Codex, Claude Code, Cursor, and Antigravity CLI.
- Local marketplace catalogs for Claude Code and Cursor.
- Offline package validation and a read-only environment doctor.
- Package and per-skill eval schema validation.

### Security

- No hooks, MCP servers, apps, telemetry, network runtime, or dependency installation.
