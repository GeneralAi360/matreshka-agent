# Changelog

All notable changes to Matreshka Agent are recorded here.

## Unreleased — 0.5 development track

### Added

- Source-brief preservation for Build End-to-End handoffs without committing raw brief state by default.
- Stable `U-` user-intent requirements kept separate from `S-` security controls.
- Four intent-traceability gates: G1 clarification completeness, G2 independent brief-to-spec coverage, G3 requirement-to-task bidirectional traceability, and G4 blind acceptance against the actual result.
- A separate fresh-context blind-acceptance mode in `verifying-development-work`; technical/security verification remains mandatory and is not replaced by G4.
- Optional dependency-free local dashboard projection with brief coverage, security-proof coverage, verification/blind status, authority summary, stages/tasks, checkpoint, and next action.
- Complexity tiers `T0`–`T3` as decomposition budgets independent from execution profile and permission authority.
- GitHub Actions package validation running the deterministic validator self-tests and read-only doctor on repository changes.

### Changed

- Controller state now includes an `ACCEPTANCE` stage between technical `VERIFY` and `FINISH` when source-intent G4 applies.
- Planning maps `U-` and `S-` rows bidirectionally and rejects orphan requirements or unjustified product tasks.
- Review packages may carry task-local exact source quotes to detect silent narrowing without forwarding the whole source brief.
- Recovery validates actual state/evidence, ledger, source brief/requirement manifest and G1–G4 before human projections.
- Canonical default paths in the controller permission contract are unified under `docs/context.md`, `docs/specs/`, `docs/plans/`, `docs/adr/`, `docs/runs/`, and `.matreshka/` internal state rather than parallel `docs/matreshka/` trees.

### Security

- Source briefs, requirement manifests, and dashboards are explicitly untrusted data/projections and cannot expand authority.
- Only valid user decision authority may mark a `U-` requirement `DROPPED`.
- Dashboard creation does not authorize a local server, listener, browser launch, network access, Git action, or publication.
- Blind acceptance rejects contaminated input packages that include specification/manifest/task/report interpretations.
- Existing Git, network, secret, provider, deploy, destructive, learning-promotion, independent-review, and Security-by-Design boundaries remain in force.

### Pending before a 0.5.0 release claim

- Complete README/root workflow-eval/version metadata updates and run the full package validator/self-test/doctor against the finished branch.
- Obtain native installation and behavior evidence on every claimed host.
- Benchmark plain-agent, minimal-controller, and full Matreshka variants for requirement coverage, acceptance quality, agent turns, wall time, and token usage where available.

## 0.4.0 - 2026-08-04

### Added

- `building-end-to-end`, a tenth plain-language entry that routes complete application requests through the existing permission-aware controller.
- `GUIDED`, `ASSISTED`, and `AUTONOMOUS_LOCAL` interaction modes, kept independent from execution profiles and effective permissions.
- Durable project context, selective ADR, and human-readable progress contracts with safe reconciliation against ledger, repository state, and fresh evidence.
- Fifteen cross-skill workflow and adversarial evaluation scenarios.

### Changed

- Verification blocks completion for stale progress, acceptance-critical placeholders, and missing required security negative proofs.
- Final handoff records mode, profile, authority, delegated decisions, assumptions, placeholders, state paths, verified checkpoint, residual risks, and exact external action.
- Package manifests, marketplaces, doctor, validator, eval metadata, and Codex wrappers now agree on version `0.4.0` and ten skills.

### Security

- Context, progress, issue content, retrieved material, and learning candidates remain untrusted data and cannot expand authority.
- Interaction mode never grants Git, network, secret, provider, deploy, cleanup, or destructive permissions.
- Native host execution and publication remain separate handoffs; offline validation is not reported as native success.

## 0.3.0 - 2026-07-29

### Changed

- Renamed `designing-software-work` to `specifying-software-work` so its output is unambiguously a requirements and technical specification, not visual design.
- Replaced the optional `/prompts:matreshka-design` wrapper with `/prompts:matreshka-spec`.
- Specification and planning work now use durable `docs/specs/` and `docs/plans/` artifacts by default when local documentation writes are authorized.

### Security

- Added Security by Design as a required specification baseline and high-risk threat-model gate.
- Added traceable `S-` security requirements with a control owner and negative proof to specifications and implementation plans.
- Extended implementation, review, and verification so selected security controls cannot be silently omitted or called verified without current evidence.

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
