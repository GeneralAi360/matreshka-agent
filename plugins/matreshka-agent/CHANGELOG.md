# Changelog

All notable changes to Matreshka Agent are recorded here.

## Unreleased — 0.5 development track

> Versioned plugin manifests intentionally remain `0.4.0` until native/release gates pass. The development branch already contains the 0.5 feature scope.

### Added

- Source-brief preservation for Build End-to-End without committing raw brief state by default.
- Stable `U-` user-intent requirements separated from `S-` Security-by-Design controls.
- G1 clarification completeness, G2 independent brief→spec coverage, G3 bidirectional requirement↔task/proof traceability, and G4 fresh blind acceptance against the actual result.
- Public modes `INTERVIEW`, `ASSISTED`, `FULL_AUTO` plus scenarios `NEW_PROJECT`, `CONTINUE_PROJECT`, `EXISTING_PROJECT`; internal controller autonomy remains separate.
- Complexity tiers `T0`–`T3` independent from execution profile and permission authority.
- Russian-first dependency-free local dashboard with responsive layout, overall progress, stages/tasks, tests, requirements/security, Project Intelligence, Browser/E2E, permissions, timing and truthful token telemetry.
- Exact/partial/unavailable timing and token semantics; unavailable counters are never estimated from text/time/message volume.
- Browser/E2E capability discovery with repository-native framework first, optional managed Chromium/CDP/host browser tooling, isolated-context requirements and console/network evidence where available.
- Separate technical Browser E2E and Browser G4 acceptance axes.
- Separate browser/process/port/dependency-install/test-data/destructive-E2E permission fields.
- Project Intelligence Layer:
  - P1 `PROJECT_TOPOLOGY` from current repository evidence;
  - P2 task-local `AREA_CONTEXT_SET`;
  - P3 frozen controller-owned `IC-xx` cross-area interface contracts;
  - P4 ownership-aware `RUNTIME_MAP`;
  - P5 `DOCUMENTATION_DRIFT_GATE`;
  - P6 specialist role archetypes over existing Matreshka skills without authority/budget inflation.
- Run-local Project Intelligence/interface templates and reusable validated profile summaries when authorized.
- Project Intelligence ledger/dashboard/recovery state.
- Fourteen Project Intelligence adversarial cases for topology, CLI no-fake-split, interface freeze/drift, context minimization, runtime ownership, docs drift, specialist boundaries, budget inflation, execution-only operators and stale recovery.
- GitHub Actions validation on `main`, `dev/**` and pull requests.
- `scripts/check_dev_05.py`, a read-only/offline integrity checker for required 0.5 components, cross-skill wiring and eval JSON.

### Changed

- Controller state includes `ACCEPTANCE` between technical `VERIFY` and `FINISH` when G4 applies.
- Planning maps U/S bidirectionally, rejects orphan requirements/unsourced product tasks, routes by current areas and freezes shared interfaces before dependent writer dispatch.
- Review packages can carry task-local source quotes and frozen `IC-xx` contracts to detect source-intent/interface narrowing.
- Project profiles cache only validated topology/context/runtime/interface locations and are revalidated before reuse.
- Task briefs/dispatches include primary area, bounded context, interfaces, specialist boundary, runtime dependency and documentation-impact candidate when relevant.
- Verification keeps technical/security evidence mandatory; Browser E2E can add technical evidence, while G4 remains a distinct restricted-input acceptance check.
- Clean finish requires applicable documentation drift to resolve honestly before `FINISHED_*`.
- Recovery revalidates source intent, topology, interfaces, runtime, browser state, timing/usage and projections against actual current evidence.
- Human-facing final handoff template is Russian-first while preserving stable machine enums/IDs.
- Repository and package READMEs now describe the development 0.5 architecture instead of stale 0.4 launch terminology.
- Codex Build wrapper/card preserve Russian `interview/assisted/full-auto/continue-project/existing-project` UX while remaining compatible with the current 0.4 validator's `[TASK]` wrapper hint and canonical `$building-end-to-end` token.

### Security

- Source briefs, manifests, topology/context/interface/runtime/profile/docs/dashboard/browser/report artifacts remain data/projections/claims and cannot expand authority.
- Only valid user authority may set `U-` to `DROPPED`.
- `FULL_AUTO` does not grant Git, dependency/network, browser download/launch, local service start, port bind, test-data/destructive setup, secrets, provider, deploy or remote actions.
- Existing repository E2E is preferred; missing E2E does not authorize framework installation.
- Personal/ambient browser profiles, cookies/session and unrelated tabs are invalid Browser G4 authority.
- Destructive E2E setup requires exact disposable/approved environment proof and explicit mutation/reset authority.
- Runtime observation is separate from start/stop/restart/kill; unknown port ownership cannot be solved by broad process killing.
- Specialist labels never add tools, filesystem scope, turns or permissions.
- Frozen interfaces cannot be materially redefined by a producer/consumer implementer without controller reconciliation.
- `DOCS_UPDATE_REQUIRED` is not documentation-write permission; docs maintainer remains docs-only.
- Execution-only remote/file-transfer operators cannot infer follow-up actions.
- G4 rejects contaminated inputs containing spec/manifest/plan/tasks/reports/projections.
- Existing one-writer, one-fixer-wave, independent-review, Security-by-Design, secret and remote boundaries remain in force.

### Hardening / validation

- CI now runs, in order: package validator negative self-tests → 0.5 development integrity → read-only doctor.
- Hardening found and fixed a real validator/UX mismatch in the Codex Build wrapper/card.
- `check_dev_05.py` verifies required source-intent, dashboard, Browser/E2E and Project Intelligence assets plus controller/planner/reviewer/verifier/finish wiring and key eval coverage.
- Core TaskLedger native acceptance on an earlier 0.5 snapshot correctly returned `PARTIALLY_VERIFIED / DEGRADED` instead of false `COMPLETE` when Python 3.11/native-verifier evidence was unavailable; persistence, G2, G3, review/re-review and G4 were exercised.
- Project Intelligence and Browser implementation plans are closed as `IMPLEMENTED_PENDING_NATIVE_VALIDATION`; remaining items are evidence gates, not missing P1–P6/B1–B7 components.

### Pending before an actual 0.5.0 release claim

- Observe final-development-HEAD CI success and latest-checkout validator/self-test + `check_dev_05.py` + doctor results.
- Run a disposable full-stack native acceptance covering Project Topology, Area Context, frozen IC contracts, Runtime Map, specialist routing, Browser E2E/G4, docs drift and the updated Russian dashboard.
- Record native evidence for every host actually claimed in release documentation.
- Only then bump manifests/marketplaces/validator/doctor/root eval metadata to `0.5.0`.
- Complete final publisher/security metadata required for public release.

## 0.4.0 - 2026-08-04

### Added

- `building-end-to-end`, a tenth plain-language entry that routes complete application requests through the existing permission-aware controller.
- `GUIDED`, `ASSISTED`, and `AUTONOMOUS_LOCAL` interaction modes for the 0.4 line.
- Durable project context, selective ADR, human-readable progress, quality gates and Security by Design.

### Changed

- Verification blocks completion for stale progress, acceptance-critical placeholders and missing security negative proofs.
- Final handoff records mode, profile, authority, decisions, assumptions, placeholders, state paths and fresh evidence.

### Security

- Context/progress/issues/retrieved material remain untrusted data and cannot expand authority.
- Interaction mode never grants Git, network, secret, provider, deploy, cleanup or destructive permissions.

## 0.3.0 - 2026-07-29

- Renamed `designing-software-work` to `specifying-software-work`.
- Specification/planning use durable `docs/specs/` and `docs/plans/` when authorized.
- Added Security by Design, high-risk threat-model gates and traceable `S-` negative proofs.

## 0.2.0 - 2026-07-18

- Added project-local profiles, skill-source mapping, compact quality gates, optional worktree guidance and directed-learning candidates.

## 0.1.4 - 2026-07-18

- Reordered visible skill labels to `Action · Matreshka Agent`.

## 0.1.3 - 2026-07-18

- Added Matreshka source identity to skill cards/labels.

## 0.1.2 - 2026-07-18

- Controller resolves bundled skills by verified Matreshka package identity and refuses similarly named external substitutes.

## 0.1.1 - 2026-07-16

- Added optional Codex prompt wrappers and offline wrapper validation.

## 0.1.0 - 2026-07-16

- Initial nine portable skills, manifests, marketplaces, offline validation and read-only doctor.
