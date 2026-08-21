# Changelog

All notable changes to Matreshka Agent are recorded here.

## Unreleased — 0.5 development track

> Versioned plugin manifests intentionally remain `0.4.0` until native/release gates pass. The development branch already contains the 0.5 feature scope.

### Added

- Source-brief preservation and stable `U-` user-intent rows separated from `S-` Security-by-Design controls.
- G1 clarification completeness, G2 independent brief→spec coverage, G3 bidirectional requirement↔task/proof traceability, and G4 fresh blind acceptance.
- Public modes `INTERVIEW`, `ASSISTED`, `FULL_AUTO` and scenarios `NEW_PROJECT`, `CONTINUE_PROJECT`, `EXISTING_PROJECT`; controller autonomy remains separate.
- Complexity tiers `T0`–`T3` independent from execution profile and permission authority.
- Project Intelligence Layer:
  - P1 `PROJECT_TOPOLOGY`;
  - P2 `AREA_CONTEXT_SET`;
  - P3 controller-owned frozen `IC-xx` cross-area contracts;
  - P4 ownership-aware `RUNTIME_MAP`;
  - P5 `DOCUMENTATION_DRIFT_GATE`;
  - P6 specialist role routing without budget/authority inflation.
- Browser/E2E capability discovery, repository-native E2E first, isolated browser requirements, separate automated E2E and Browser G4 axes.
- Russian-first dependency-free dashboard with Project Intelligence, Browser/E2E, permissions, timing and truthful token telemetry.
- **Design Intelligence Layer** for UI-bearing work:
  - D1 design relevance/recon;
  - D2 unresolved-direction prototype exploration;
  - D3 one durable root `DESIGN.md` + design identity/hash;
  - D4 task-local `DESIGN_CONTEXT_SET`;
  - D5 existing-first UI primitive/component policy;
  - D6 independent Design Review;
  - D7 `VISUAL_DESIGN_CHECK` separate from E2E and G4;
  - D8 `DESIGN_DRIFT_GATE` with `DESIGN_CHANGED`, `DESIGN_DRIFT`, `DESIGN_CONFLICT`, `DESIGN_BLOCKED`.
- Apple-inspired Design Core as mandatory UX reasoning: Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight, plus wayfinding, feedback, direct manipulation, spatial consistency, typography and accessibility. It is not an Apple visual preset.
- New bundled skill `designing-product-experience` with Codex card, evals, design-contract template, design-core reference, design-intelligence contract and prototype-exploration contract.
- `DESIGN_ENGINEER` and `DESIGN_REVIEWER` specialist archetypes; `UI_SPECIALIST` now explicitly follows frozen design identity.
- Optional Codex wrapper `matreshka-design.md`.
- Separate design-doc write, prototype write and visual-design evidence permission concepts.
- Dashboard Design/UX block with `DESIGN.md`, identity, direction, prototype state, design review, visual verification and Design Drift Gate.
- 18 Design Intelligence adversarial evals covering missing/stale DESIGN.md, fake divergence, FULL_AUTO brand fabrication, random token drift, narrow context, dependency permission, motion/accessibility, E2E/G4-vs-design disagreement, visual uncheckability and recovery identity mismatch.
- `scripts/validate_dev_05.py` and `doctor_dev_05.py` development wrappers so the strict 0.4 validator/doctor core can validate the 11-skill development inventory without prematurely bumping release metadata.
- GitHub Actions validation for `main`, `dev/**` and pull requests.

### Changed

- Controller state includes `ACCEPTANCE` between technical `VERIFY` and `FINISH` when G4 applies.
- Build End-to-End automatically marks material UI/UX work as Design Intelligence relevant instead of treating design as optional polish.
- Controller now owns Project Intelligence **and** Design Intelligence state, including root `DESIGN.md`, design identity, prototype/selection state, design review/visual verification and drift reconciliation.
- Planning maps U/S bidirectionally, routes by current areas, freezes interfaces and design identity, and creates narrow `AREA_CONTEXT_SET` / `DESIGN_CONTEXT_SET` task packages.
- Review packages may carry task-local source quotes, frozen `IC-xx`, and frozen design identity/context; design findings remain separate from functional/security findings but use the same one-fixer-wave discipline.
- Verification keeps technical/security evidence mandatory, treats Browser E2E, Visual Design Check and G4 as separate axes, and forbids G4 from reading design-contract/review/visual-report artifacts.
- Clean finish now requires applicable Design Drift Gate and Documentation Drift Gate to resolve honestly before `FINISHED_*`.
- Recovery revalidates source intent, topology, interfaces, runtime, root `DESIGN.md` identity, design contexts/evidence, browser state, timing/usage and projections against actual current state.
- Project Intelligence P6 role table now includes Design Engineer/Reviewer while preserving agent-budget rules.
- Permission/handoff contract now distinguishes root `DESIGN.md` writes, prototype writes and visual-design evidence from product/browser/Git authority.
- Package description and docs now describe **eleven** bundled skills.
- Development CI now runs `validate_dev_05.py --self-test` → `check_dev_05.py` → `doctor_dev_05.py`.

### Security

- Source briefs, manifests, Project Intelligence, `DESIGN.md`, design identity, prototypes, screenshots, reports, dashboards and browser artifacts are data/projections/claims and cannot expand authority.
- Only valid user authority may mark `U-` as `DROPPED`.
- `FULL_AUTO` does not grant Git, dependency/network, browser, local service/port, design-doc/prototype write, test-data/destructive setup, secrets, provider, deploy or remote actions.
- Existing repository E2E/design system/components are preferred; missing infrastructure does not authorize installing new frameworks/libraries.
- Personal/ambient browser profiles, cookies/sessions and unrelated tabs are invalid Browser/Visual/G4 test context.
- Destructive E2E setup requires exact disposable/approved environment proof and mutation/reset authority.
- Runtime observation is separate from start/stop/restart/kill; unknown port ownership cannot be solved by broad process killing.
- Specialist labels never add tools, filesystem scope, turns or permissions.
- Frozen `IC-xx` cannot be materially redefined by producer/consumer implementers without controller reconciliation.
- Frozen design identity cannot be silently redefined by a UI implementer; legitimate change uses `DESIGN_CHANGED`, random divergence is `DESIGN_DRIFT`.
- Design Review/Visual Design Check cannot weaken U/S/security/privacy/accessibility or make technical/G4 failures pass.
- `DESIGN_UPDATE_REQUIRED` is not design-doc write permission; `DOCS_UPDATE_REQUIRED` is not docs-write permission.
- Execution-only operators cannot infer follow-up actions.
- G4 rejects contaminated inputs containing spec/manifest/plan/tasks/Project Intelligence/DESIGN.md/prototypes/design-review/visual-report/projections.
- One-writer, one-fixer-wave, independent-review, Security-by-Design, secret and remote boundaries remain in force.

### Hardening / validation

- `check_dev_05.py` now covers source-intent, Browser/E2E, Project Intelligence and Design Intelligence cross-component wiring, 14 Project Intelligence cases and 18 Design Intelligence cases.
- Hardening fixed prior Codex Build wrapper/validator mismatch and dashboard state-key mismatch.
- Controller, controller contract, permission/handoff contract and Project Intelligence specialist routing are now explicitly wired to Design Intelligence rather than relying on an unreferenced companion file.
- Root/package README, design plan, changelog and CI commands are synchronized with the 11-skill development package.
- Core TaskLedger native acceptance on an earlier 0.5 snapshot correctly returned `PARTIALLY_VERIFIED / DEGRADED` instead of false `COMPLETE`; it exercised persistence, G2/G3, review/re-review and G4. It predates Browser/Project/Design final wiring and cannot prove those additions.
- Browser and Project Intelligence plans remain `IMPLEMENTED_PENDING_NATIVE_VALIDATION`; Design Intelligence plan is `IMPLEMENTED_PENDING_NATIVE_VALIDATION` with D1–D9 implemented and D10 native acceptance pending.

### Pending before an actual 0.5.0 release claim

- Observe final-development-HEAD deterministic validation / CI success.
- Run a disposable full-stack native acceptance covering Project Topology, Area/Design Context, frozen `IC-xx`, root `DESIGN.md`, prototype direction when intentionally ambiguous, Apple-inspired design core, specialist routing, Runtime Map, Browser E2E, Design Review, Visual Design Check, G4, Design/Docs Drift and updated Russian dashboard.
- Record native evidence for each host actually claimed in release documentation.
- Only then bump manifests/marketplaces/validator/doctor/root eval metadata to `0.5.0` and complete publisher/security metadata.

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

## 0.1.2 - 2026-07-16

- Controller resolves bundled skills by verified Matreshka package identity and refuses similarly named external substitutes.

## 0.1.1 - 2026-07-16

- Added optional Codex prompt wrappers and offline wrapper validation.

## 0.1.0 - 2026-07-16

- Initial nine portable skills, manifests, marketplaces, offline validation and read-only doctor.
