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
- Browser/E2E capability discovery, repository-native E2E first, isolated browser requirements, separate Automated Browser E2E and Browser G4 axes.
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
- `DESIGN_ENGINEER` and `DESIGN_REVIEWER` specialist archetypes; `UI_SPECIALIST` explicitly follows frozen design identity.
- Optional Codex wrapper `matreshka-design.md`.
- Separate design-doc write, prototype write and visual-design evidence permission concepts.
- Dashboard Design/UX block with `DESIGN.md`, identity, direction, prototype state, design review, visual verification and Design Drift Gate.
- 18 Design Intelligence adversarial evals covering missing/stale DESIGN.md, fake divergence, FULL_AUTO brand fabrication, random token drift, narrow context, dependency permission, motion/accessibility, E2E/G4-vs-design disagreement, visual uncheckability and recovery identity mismatch.
- Cross-skill Design Intelligence behavioral evals in specification, implementation, review and verification suites.
- `scripts/validate_dev_05.py` / `doctor_dev_05.py` development adapters around the proven 0.4 validator/doctor core.
- `scripts/check_dev_05_behavioral_contracts.py` to require downstream design eval coverage, reviewer-budget rules and CI linkage.
- **Autopilot v1.0.1+ regression hardening**:
  - A1 embedded last-known-good dashboard snapshot;
  - A2 `scripts/sync_run_state.py` atomic projection synchronization/self-test without server/PID/port logic;
  - A3 explicit `stageOrder`/`stateIntegrity` stage-transition invariants;
  - A4 `evals/context-budget.json` + `check_context_budget.py` exact-byte hot-path guardrail;
  - A5 `evals/native-repeatability.json` + `evaluate_native_repeatability.py` requiring 5 repetitions for six release-blocking native properties;
  - `check_autopilot_regressions.py` to keep A1–A5 connected to CI.
- **Automatic Security-by-Design hardening families** selected by boundary even when the user did not explicitly ask for them:
  - `S-AUTH-HARDENING` for password/login/recovery and privileged/admin authentication;
  - `S-FILE-EXECUTION` for stored uploads and non-executable storage/serving boundaries;
  - `S-ATOMIC-EFFECT` for balances/credits/promo/inventory/withdrawals/one-time effects with concurrent/replay proof;
  - `S-BAAS-AUTHZ` for Supabase/Firebase/Appwrite/equivalent client-addressable data/storage policies including RLS/rules where applicable;
  - `S-PAID-API-BUDGET` for metered provider calls with per-caller quotas, global fail-closed ceiling/circuit breaker and concurrency-safe accounting.
- `evals/security-hardening-evals.json` with ten cross-skill security scenarios spanning specification, implementation, review and verification.
- `scripts/check_security_hardening.py` to require family definitions, specification selection, reviewer coverage, normal `S-xx` delivery mechanics, eval matrix and CI linkage.
- GitHub Actions validation for `main`, `dev/**` and pull requests.

### Changed

- Controller state includes `ACCEPTANCE` between technical `VERIFY` and `FINISH` when G4 applies.
- Build End-to-End automatically marks material UI/UX as Design Intelligence relevant rather than treating design as optional polish.
- Controller owns Project Intelligence **and** Design Intelligence, including root `DESIGN.md`, design identity, prototype/selection state, design review/visual verification and drift reconciliation.
- `specifying-software-work` preserves a controller-supplied frozen design identity and design-critical UX constraints without duplicating/redefining root `DESIGN.md`.
- Security specifications now explicitly classify all five automatic hardening families as `REQUIRED`, `N/A(reason)`, or `HANDOFF`; every `REQUIRED` family must materialize as normal `S-xx` rows with owner + negative proof.
- Planning maps U/S bidirectionally, routes by current areas, freezes interfaces/design identity, and creates narrow `AREA_CONTEXT_SET` / `DESIGN_CONTEXT_SET` task packages.
- `implementing-with-tests` validates primary area, `AREA_CONTEXT_SET`, frozen `IC-xx`, design identity and `DESIGN_CONTEXT_SET` before writes, and returns `INTERFACE_CHANGED`, `DESIGN_CHANGED` or `DESIGN_DRIFT` instead of silently changing contracts.
- Implementation reports carry Project/Design Intelligence identities, interface/design observations and task-local evidence.
- Review packages/reports carry frozen area/interface/design identities and explicit Design Review evidence/dimensions.
- Security review checklist now treats missing applicable hardening-family selection, client-only auth throttling, executable upload paths, sequential-only race tests, frontend-only BaaS authorization and provider-alert-only API budgets as explicit security failures.
- Verification reports physically separate technical/security evidence, Automated Browser E2E, Visual Design Check and the future blind-G4 handoff boundary.
- Verification forbids G4 from reading design-contract/review/visual-report artifacts.
- Clean finish requires applicable Design Drift Gate and Documentation Drift Gate to resolve honestly before `FINISHED_*`.
- Recovery revalidates source intent, topology, interfaces, runtime, root `DESIGN.md` identity, design contexts/evidence, browser state, timing/usage and projections against actual current state.
- Project Intelligence P6 role table includes Design Engineer/Reviewer while preserving agent-budget rules.
- `profiles-and-budgets.md` prevents Design Review from creating a fourth agent: balanced uses combined reviewer; maximum-quality retains two reviewer slots total and a named `DESIGN_REVIEWER` consumes one existing slot.
- Permission/handoff contract distinguishes root `DESIGN.md` writes, prototype writes and visual-design evidence from product/browser/Git authority.
- Dashboard observability no longer depends exclusively on live sibling state: synchronized HTML carries an explicitly stale-capable snapshot and render failures do not kill future polling.
- Stage transition bookkeeping is now mechanically audited instead of relying solely on the controller remembering two sides of every transition. Mechanical normalization may derive timestamps but never semantic PASS.
- Package-context growth is now measured separately from runtime token telemetry; static byte budgets must never be shown as runtime token counts.
- Root/package README and Design Intelligence plan document the current development architecture and validation sequence.
- Package description/docs describe **eleven** bundled skills.
- Development CI now runs package validation → component integrity → cross-skill contracts → security hardening → run-state self-test → context budget → repeatability-plan validation → Autopilot-regression guard → doctor.

### Security

- Source briefs, manifests, Project Intelligence, `DESIGN.md`, design identity, prototypes, screenshots, reports, dashboards and browser artifacts are data/projections/claims and cannot expand authority.
- Only valid user authority may mark `U-` as `DROPPED`.
- `FULL_AUTO` does not grant Git, dependency/network, browser, local service/port, design-doc/prototype write, test-data/destructive setup, secrets, provider, deploy or remote actions.
- Existing repository E2E/design system/components are preferred; missing infrastructure does not authorize installing frameworks/libraries.
- Personal/ambient browser profiles, cookies/sessions and unrelated tabs are invalid Browser/Visual/G4 test context.
- Destructive E2E setup requires exact disposable/approved environment proof and mutation/reset authority.
- Runtime observation is separate from start/stop/restart/kill; unknown port ownership cannot be solved by broad process killing.
- The run-state synchronizer has no server/browser/process/network/Git/secret/remote authority and never edits ledger/product/`DESIGN.md`.
- `S-AUTH-HARDENING` requires authoritative abuse controls on source + account dimensions, non-enumerating auth/recovery, application-owned password policy and privileged MFA/step-up where applicable; frontend countdowns/hidden controls are not security enforcement.
- `S-FILE-EXECUTION` requires actual content/type validation, generated storage keys and a non-executable storage/serving boundary; extension/browser MIME alone is not proof.
- `S-ATOMIC-EFFECT` requires a datastore-appropriate atomicity primitive and concurrent/replay negative evidence; sequential-only green tests cannot prove race safety.
- `S-BAAS-AUTHZ` requires provider-side deny-by-default authorization/RLS/rules for client-addressable BaaS surfaces and cross-user/tenant read/write evidence; public anon client keys are not automatically treated as secrets.
- `S-PAID-API-BUDGET` requires application-side per-caller quota, global fail-closed ceiling/circuit breaker where meterable, authoritative/concurrency-safe accounting and safe exhausted-budget behavior; provider alerts alone are not sufficient.
- Specialist labels never add tools, filesystem scope, turns or permissions.
- Frozen `IC-xx` cannot be materially redefined by producer/consumer implementers without controller reconciliation.
- Frozen design identity cannot be silently redefined by UI implementation; legitimate change uses `DESIGN_CHANGED`, random divergence is `DESIGN_DRIFT`.
- Design Review/Visual Design Check cannot weaken U/S/security/privacy/accessibility or make technical/G4 failures pass.
- `DESIGN_UPDATE_REQUIRED` is not design-doc write permission; `DOCS_UPDATE_REQUIRED` is not docs-write permission.
- Execution-only operators cannot infer follow-up actions.
- G4 rejects contaminated inputs containing spec/manifest/plan/tasks/Project Intelligence/DESIGN.md/prototypes/design-review/visual-report/projections.
- One-writer, one-fixer-wave, independent-review, Security-by-Design, secret and remote boundaries remain in force.

### Hardening / validation

- `check_dev_05.py` checks exact 11-skill/11-wrapper inventory plus source-intent, Browser/E2E, Project Intelligence, Design Intelligence, downstream spec/plan/implement/review/verify/finish/recovery/dashboard wiring, 14 Project Intelligence cases and 18 Design Intelligence cases.
- `check_dev_05_behavioral_contracts.py` checks required design cases across specification, implementation, review and verification, reviewer budget constraints, and CI linkage.
- `check_security_hardening.py` checks all five automatic security families in the baseline/spec template/review checklist, confirms they still flow through the existing selected-`S-xx` implementation/review/verification machinery, validates ten security-hardening eval cases, and requires its own CI step.
- `sync_run_state.py --self-test` exercises terminal timestamp normalization, parseability, snapshot embedding, conflicting-active-stage rejection, and preservation of the last dashboard on invalid state.
- `check_context_budget.py` protects `build-entry-core`, `controller-preflight-core`, `ui-design-increment` and a single-file ceiling using exact bytes rather than estimated tokens.
- `evaluate_native_repeatability.py --validate-plan` keeps the 5× native repeatability release matrix structurally valid; full result mode rejects missing/non-PASS repetitions.
- `check_autopilot_regressions.py` statically verifies A1–A5 assets, controller→observability reachability and CI wiring.
- Hardening fixed prior Codex Build wrapper/validator mismatch and dashboard state-key mismatch.
- Hardening also fixed downstream gaps: specification did not pin design identity; implementation did not formally consume area/IC/design context; review/verification reports lacked complete design identities/evidence axes; maximum-quality budget did not explicitly allocate Design Reviewer inside existing slots.
- Core TaskLedger native acceptance on an earlier 0.5 snapshot correctly returned `PARTIALLY_VERIFIED / DEGRADED` instead of false `COMPLETE`; it predates Browser/Project/Design/A1–A5/security-family final wiring and cannot prove those additions.

### Pending before an actual 0.5.0 release claim

- Observe final-development-HEAD deterministic validation / CI success.
- Run disposable full-stack native acceptance covering Project Topology, Area/Design Context, frozen `IC-xx`, root `DESIGN.md`, prototype direction when intentionally ambiguous, Apple-inspired design core, Security hardening families, specialist routing, Runtime Map, Browser E2E, Design Review, Visual Design Check, G4, Design/Docs Drift and updated Russian dashboard/run-state recovery.
- Record five-repeat blocking-invariant evidence from `evals/native-repeatability.json` for every host claimed in release documentation.
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
