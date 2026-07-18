# Changelog

All notable changes to Matreshka Agent are recorded here.

## 0.2.0 - 2026-07-18

### Added

- Project-local profiles and a bundled-skill source map, revalidated against the current repository before reuse.
- A compact quality gate with evidence rows for existing, permitted checks.
- Optional worktree-isolation guidance that requires exact authority and never performs automatic cleanup.
- Directed-learning candidates with `OFF`, `PROPOSE`, and `LOCAL_REVIEWED` modes.
- Adversarial evaluations for unmet quality gates, unauthorized global learning, and worktree authority.

### Security

- Learning candidates are project-local proposals only; they cannot automatically change the plugin, shared instructions, hooks, or environment configuration.
- Candidates exclude secrets, personal data, private URLs, raw logs, and hidden agent reasoning, and require independent revalidation before reuse.

## 0.1.4 - 2026-07-18

### Changed

- Reordered every visible skill label to `Action · Matreshka Agent` so users see the action first and its source second.

## 0.1.3 - 2026-07-18

### Changed

- Every Codex skill card and active-skill label now starts with `Matreshka Agent ·`.
- Short descriptions also identify Matreshka Agent, making similarly named skills easier to distinguish in menus.

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
