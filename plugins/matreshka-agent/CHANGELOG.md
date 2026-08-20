# Changelog

All notable changes to Matreshka Agent are recorded here.

## Unreleased — 0.5 development track

### Added

- Source-brief preservation for Build End-to-End handoffs without committing raw brief state by default.
- Stable `U-` user-intent requirements kept separate from `S-` security controls.
- Four intent-traceability gates: G1 clarification completeness, G2 independent brief-to-spec coverage, G3 requirement-to-task bidirectional traceability, and G4 blind acceptance against the actual result.
- A separate fresh-context blind-acceptance mode in `verifying-development-work`; technical/security verification remains mandatory and is not replaced by G4.
- Optional dependency-free Russian-first local dashboard projection with brief coverage, security proof coverage, project intelligence, verification/blind status, authority summary, stages/tasks, timing/usage, checkpoint, and next action.
- Complexity tiers `T0`–`T3` as decomposition budgets independent from execution profile and permission authority.
- Simple public Build End-to-End modes `INTERVIEW`, `ASSISTED`, and `FULL_AUTO`, plus project scenarios `NEW_PROJECT`, `CONTINUE_PROJECT`, and `EXISTING_PROJECT`.
- Browser/E2E capability preflight that detects existing repository E2E, managed browser, optional Chrome CDP, host browser tooling, isolation, console/network inspection, runtime needs, and missing permissions.
- Browser verification contract that prefers existing Playwright/Cypress/Selenium/WebdriverIO infrastructure and recommends Playwright managed Chromium only for a separately authorized new setup.
- Browser G4 blind acceptance for user-visible web outcomes, with isolated browser observation, minimal screenshots/traces, and decisive console/network evidence where supported.
- Separate permission fields for browser interaction, local process/runtime, port binding, browser/dependency installation, test-data mutation, and destructive E2E setup.
- Browser verification summaries in the ledger and live dashboard projection.
- Project Intelligence Layer P1–P6: repository-derived Project Topology, task-local Area Context routing, controller-owned cross-area `IC-xx` interface contracts, safe Runtime Map, post-verification Documentation Drift Gate, and bounded Specialist Role Routing.
- Run-local Project Intelligence and interface-contract templates under `.matreshka/runs/<run-id>/`, plus reusable validated project-profile topology/runtime/context summaries when authorized.
- Project Intelligence dashboard/ledger fields for area count/current area, interface freeze state, runtime status, documentation drift, specialist archetype, and context guarantee.
- Focused adversarial Project Intelligence scenarios covering fake frontend/backend decomposition, interface drift, oversized context, unknown process ownership, stale documentation, specialist budget inflation, operator overreach, and stale recovery caches.
- GitHub Actions package validation running the deterministic validator self-tests and read-only doctor on repository changes.

### Changed

- Controller state now includes an `ACCEPTANCE` stage between technical `VERIFY` and `FINISH` when source-intent G4 applies.
- Planning maps `U-` and `S-` rows bidirectionally, rejects orphan requirements/unjustified product tasks, routes tasks by current project areas, and freezes shared cross-area interfaces before dependent writer dispatch.
- Review packages may carry task-local exact source quotes and frozen `IC-xx` contracts to detect silent requirement/interface narrowing without forwarding the whole source brief or project history.
- Project profiles now cache only validated project topology, area context index, runtime map, command sources, and durable interface-document locations; stale subsets are revalidated against current repository evidence before reuse.
- Task briefs and dispatches now include one primary area, minimal `AREA_CONTEXT_SET`, explicit exclusions, interface identities, specialist boundary, runtime dependency, and documentation-impact candidate when applicable.
- Recovery validates actual state/evidence, ledger, source brief/manifest, topology, active interfaces, runtime ownership, context routing, documentation drift, browser evidence, and G1–G4 before human projections.
- Public interaction names are kept separate from internal controller autonomy: `FULL_AUTO` never means `EXTENDED_AUTONOMOUS` and legacy `AUTONOMOUS_LOCAL` is compatibility/internal terminology only.
- Existing browser E2E is preferred over installing a second framework; automated E2E and browser G4 are separate evidence axes.
- A clean finish now requires a resolved documentation-drift state when verified work changes an authoritative durable repository contract.
- Canonical default paths are unified under `docs/context.md`, `docs/specs/`, `docs/plans/`, `docs/adr/`, `docs/runs/`, and `.matreshka/` internal state rather than parallel `docs/matreshka/` trees.

### Security

- Source briefs, requirement manifests, Project Intelligence/profile/context/interface/runtime artifacts, dashboards, browser screenshots/traces, console/network summaries, documentation, and other run evidence are explicitly data/projections/claims and cannot expand authority.
- Only valid user decision authority may mark a `U-` requirement `DROPPED`.
- Dashboard creation does not authorize a local server, listener, browser launch, process start, network access, Git action, documentation write, or publication.
- `FULL_AUTO` does not authorize dependency installation, browser download/launch, local service start, port binding, test-data mutation, destructive E2E setup, secrets, documentation writes, Git, provider, or remote actions.
- Project Topology never forces a frontend/backend split; specialist role labels never add agents, turns, tools, filesystem scope, or permissions by themselves.
- A frozen `IC-xx` interface cannot be materially redefined by a producer/consumer implementer; material drift returns to controller reconciliation before dependent work continues.
- Runtime Map observation does not authorize process mutation. Unknown process ownership cannot be resolved by broad kill-by-port/process-name cleanup.
- `DOCS_UPDATE_REQUIRED` is not documentation-write permission; the documentation maintainer receives only an exact docs allowlist after verified behavior.
- Execution-only remote/file-transfer operator roles cannot infer or execute follow-up actions beyond the exact authorized target/action.
- CDP/host browser acceptance cannot use a personal browser profile, ambient authenticated session, unrelated tabs/cookies, or uncontrolled personal data as test authority.
- E2E/global setup that resets, seeds, truncates, recreates, or migrates data requires exact disposable/approved environment proof and explicit mutation authority; `localhost` or a `test:e2e` command name is not sufficient.
- Blind acceptance rejects contaminated input packages that include specification/manifest/task/Project-Intelligence/interface/report interpretations.
- Existing Git, network, secret, provider, deploy, destructive, learning-promotion, independent-review, and Security-by-Design boundaries remain in force.

### Pending before a 0.5.0 release claim

- Complete README/root workflow-eval/version metadata updates and run the full package validator/self-test/doctor against the finished branch.
- Obtain native installation and behavior evidence on every claimed host.
- Run a disposable web acceptance fixture covering Project Topology/Area Context/Interface Contract/Runtime/Docs/Specialist behavior together with existing Playwright/Cypress reuse, missing install authority, CDP isolation, destructive-test firewall, and the case where automated E2E passes but browser G4 correctly fails.
- Benchmark plain-agent, minimal-controller, and full Matreshka variants for requirement coverage, context size, interface rework, acceptance quality, agent turns, wall time, and token usage where available.

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
