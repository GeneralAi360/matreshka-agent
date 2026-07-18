# Changelog

All notable changes to Matreshka Agent are recorded here.

## 0.1.2 - 2026-07-18

### Fixed

- The controller now resolves chained skills by verified Matreshka package identity rather than a matching title or description.
- On namespaced hosts, root-cause diagnosis explicitly routes to `matreshka-agent:debugging-systematically`.
- If a bundled skill cannot be identified, the controller uses only its documented inline read-only fallback or returns `HANDOFF_REQUIRED`; it does not select an external substitute.

### Tested

- Added a controller evaluation for a host that presents two similarly named debugging skills.

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
