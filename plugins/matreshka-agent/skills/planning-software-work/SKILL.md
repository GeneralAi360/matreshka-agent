---
name: planning-software-work
description: >-
  Convert a confirmed software specification or bounded change into an implementation plan with requirement coverage, project-area/interface routing, design-contract routing when UI is affected, security controls, small ordered tasks, exact repository paths, focused RED/GREEN checks, review gates, and stop conditions. Use when the user asks for a coding plan or task breakdown but does not yet want the plan executed.
---

# Plan Software Work

Produce an executable plan, not implementation. Start only from a confirmed specification, authoritative requirement, or small change whose behavior/boundaries are already unambiguous.

Read [task-decomposition.md](references/task-decomposition.md) before splitting work or validating the final task map. Read [complexity-tiers.md](references/complexity-tiers.md) before deciding task boundaries. Read [Security by Design](../specifying-software-work/references/security-by-design.md) for selected/high-risk `S-` requirements. When the controller supplies Build End-to-End `U-` rows, read [brief traceability](../building-end-to-end/references/brief-traceability.md). When the controller supplies Project Intelligence, read [project-intelligence.md](../orchestrating-subagent-work/references/project-intelligence.md) and preserve the controller-supplied `RUNTIME_MAP` identity/status as the runtime source for planning. When the current task is UI/design relevant or controller supplies a design identity, read [Design Intelligence integration](../orchestrating-subagent-work/references/design-intelligence.md). Preserve current area/context/interface/runtime/design facts without treating them as authority. Use [implementation-plan-template.md](assets/implementation-plan-template.md).

## Validate planning input

1. Read confirmed specification, applicable repository instructions, selected `S-` requirements, controller-supplied `U-` rows, current Project Intelligence summary, and current Design Intelligence summary when provided.
2. Inspect current source, public interfaces, schemas/migrations, tests, package/workspace scripts, runtime seams, and nearby patterns in read-only mode.
3. Revalidate affected Project Topology areas and any durable interface/runtime docs needed by the change. For UI work, validate root `DESIGN.md` path/identity and the small set of token/component/layout/state sources needed to plan the change.
4. Repository evidence and valid design/user authority outrank stale profile/context/design prose; do not silently choose one source when the current accepted UI and `DESIGN.md` materially conflict.
5. Record exact baseline, constraints, non-goals, permission boundaries, affected areas, design relevance/identity, and remote/runtime handoffs.
6. Identify contradictions, unresolved architecture/design direction, missing acceptance outcomes, source-intent rows not represented in spec, security controls without negative proof, producer/consumer seams that can drift, and UI tasks that lack a stable design contract.
7. Return `NEEDS_CONTEXT` for one exact uninspectable fact, `BLOCKED` when specification/interface/design authority is missing, `CONTEXT_TOO_BROAD` when project context cannot remain bounded, or `DESIGN_CONTEXT_TOO_BROAD` when a UI task would require unrelated design surfaces/history to stay correct.

Do not invent file paths, symbols, commands, models, interfaces, topology areas, runtime ownership, design tokens, component libraries, viewports, or design identity. Discover safely. If discovery depends on a later environment, make the first gate bounded/read-only; do not use a fake placeholder as executable/design truth.

A source brief, `U-` manifest, project profile, topology map, area doc, `DESIGN.md`, prototype, or screenshot is provenance/context according to its contract, not permission. Return material conflicts to controller.

## Create documentation artifact

Use confirmed spec slug and write `docs/plans/YYYY-MM-DD-<safe-kebab-slug>-plan.md`, unless repository has a compatible convention. When docs writes are authorized, create only missing compatible directories; do not reorganize existing docs.

When docs writes are not authorized, return complete inline plan as `PLAN_READY_TO_SAVE`. Documentation/design-doc writes do not grant product-code, Git, browser/process, remote, deploy, migration, dependency-install, secret, or interface-implementation authority.

## Build requirement/security/design coverage first

Create coverage before Task 1:

```text
U-/functional requirement or S- control -> task -> verification evidence
```

For source-qualified work:

- include every live controller-supplied `U-` row;
- keep short source quote/reference where it protects against narrowing;
- map every `IN_SPEC` user requirement to task + proof;
- consume only controller-validated DROPPED status;
- keep DEFERRED/PLACEHOLDER visible with reason/owner;
- map each task back to `U-`, `S-`, or named enabling step.

For UI-bearing work also record the frozen design identity used for the task and the design evidence axis required for affected UI. Do not convert design preferences into new `U-` rows unless they actually came from user intent; design contract rules are a separate project/design source.

Include every selected `S-` control, negative proof, migration/rollback, compatibility, observability, design-review/visual-check obligation, and handoff requirement when applicable. Stop if matrix exposes unresolved design direction, orphan requirement, or unsourced product work.

## Apply Project Intelligence before task cutting

Use current topology to name only areas affected by this plan. A website does not automatically require separate frontend/backend tasks; split/route based on actual repository ownership and independently reviewable seams.

For each proposed task determine:

- primary area;
- adjacent areas required for correctness;
- minimal `AREA_CONTEXT_SET` and explicit exclusions;
- cross-area `IC-xx` contracts consumed/produced;
- runtime dependency/status/log observation needed for tests;
- specialist role archetype only when useful;
- Design Intelligence relevance/identity and `DESIGN_CONTEXT_SET` when UI is affected;
- potential durable design impact;
- potential durable documentation impact.

### Cross-area interface contracts

When a single outcome crosses independently owned producer/consumer areas and assumptions can drift, plan one controller-owned `IC-xx` contract before dependent writers start. Define source requirements, producer/consumer areas, input/output/errors, auth/data boundary, delivery semantics, compatibility, integration proof, and freeze order.

Do not let separate frontend/backend/data tasks invent different versions of the seam. A frozen material change later returns `INTERFACE_CHANGED` to controller reconciliation.

Do not create an interface artifact for a cohesive single-area helper seam without an independent consumer/version boundary.

### Project context routing

A task `AREA_CONTEXT_SET` includes only relevant `U-`/`S-`, primary-area facts, required neighboring interface contracts/invariants, focused commands/paths, and required security/data/runtime facts. Exclude unrelated area docs/history/reports/logs/full source brief/branch diff.

If correctness needs several independent boundaries, split or return `CONTEXT_TOO_BROAD`; never hide a dependency to make context smaller.

### Design context routing

For UI-affecting tasks derive a separate `DESIGN_CONTEXT_SET` from the frozen root `DESIGN.md` identity. Include only:

- product personality when it constrains the task;
- relevant app-shell/screen/layout pattern;
- relevant typography/spacing/color/radius/depth tokens;
- canonical component/primitive and state rules;
- responsive/touch/keyboard rules;
- accessibility rules;
- motion rules only if affected;
- approved design invariants;
- selected prototype/direction reference only when implementation depends on it.

Exclude unrelated screens, old design decisions, unselected prototypes, broad screenshot sets, and the whole design history. Backend-only tasks normally receive `DESIGN_NOT_APPLICABLE`.

If a correct UI task needs several unrelated design surfaces, split or return `DESIGN_CONTEXT_TOO_BROAD`; do not hide conflicting design dependencies.

### Design change vs design drift

A task plans against one frozen design identity.

- valid later material design decision -> `DESIGN_CHANGED` and controller reconciliation before dependent implementation continues;
- implementation invents a new style/pattern without design authority -> `DESIGN_DRIFT` and correction against current contract;
- verified valid design decision changes durable rules -> `DESIGN_UPDATE_REQUIRED` for root `DESIGN.md` before final identity/evidence is clean.

### Specialist routing

Select one role archetype only when it materially improves correctness/context/boundary ownership. Examples include general, frontend, backend, data/migration, UI, `DESIGN_ENGINEER`, `DESIGN_REVIEWER`, E2E, documentation/browser/operator roles.

Role archetypes reuse existing Matreshka skills. `DESIGN_ENGINEER` routes to source-qualified `designing-product-experience`; `DESIGN_REVIEWER` is a scoped read-only review role. Specialist labels do not add agent turns, tool authority, filesystem scope, Git/network/process/browser/secret/remote permission, or relax execution-profile/security requirements.

## Select complexity tier

Choose exactly one tier from `complexity-tiers.md` based on independently reviewable product/data/security/interface/design boundaries, not spec length/file count/desired speed:

- `T0` one direct reviewable task;
- `T1` normally 2–3 tasks;
- `T2` normally 4–8;
- `T3` normally 9–16;
- above safe T3 -> `SPLIT_REQUIRED` / `DECISION_MAP_REQUIRED`.

Counts are budgets, not quotas. `T0 + maximum quality` is valid. Multiple topology areas/design surfaces do not automatically mean multiple tasks or more agent budget. Parallel writers remain forbidden in one checkout.

A design-direction/prototype decision may precede coding tasks, but do not turn each design token/screen into a separate implementation task unless it is independently reviewable.

## Decompose into reviewable tasks

Each task should produce one independently reviewable result with:

- one primary area/subsystem/security boundary;
- one coherent allowlist and bounded area context set;
- frozen `IC-xx` identities when relevant;
- frozen design identity + bounded design context when UI-relevant;
- one focused RED/GREEN cycle;
- one task verification gate plus integration proof when needed;
- design review/visual check obligation when applicable;
- explicit non-goals, specialist boundary, design/docs-impact candidates, and stop conditions.

For security tasks include selected `S-`, exact auth/input/output/dependency boundary, negative test/review proof, required security-review tier.

For UI tasks identify required states rather than planning only the happy static screen: default + any affected hover/active/focus/disabled/loading/empty/error/success/responsive states.

Treat file count as risk signal. Prefer small changes, but split by independent outcomes/boundaries. Return `SPLIT_REQUIRED` when one task mixes migration/runtime, auth/UI, provider/persistence, separate security/experience designs, unrelated major screen patterns, or several acceptance results that can pass independently.

After draft, run mandatory merge pass: merge avoidable cold-start boundaries sharing one result/seam/design context when no independent review/rollback/evidence/security/ownership benefit exists. Re-check tier.

At T0 there is still exact task brief, design context if UI-relevant, review policy, verification, design/docs-impact decisions, and applicable G4.

## Order dependencies deliberately

Order design/interface/test seams before dependent consumers. Keep migrations, compatibility layers, runtime changes, remote application, and cleanup distinct when rollback/permission boundaries differ.

For each task state:

1. Goal + `U-`/functional and `S-` IDs.
2. Short source quote/reference when applicable.
3. Primary/adjacent areas and area context set.
4. Frozen `IC-xx` contracts and exact interfaces.
5. Design relevance, frozen design identity and bounded `DESIGN_CONTEXT_SET`.
6. Exact write allowlist/inspect-only scope.
7. Role archetype, owned responsibility, forbidden neighboring responsibility.
8. Non-goals/forbidden actions.
9. Focused RED and expected failure.
10. Minimal GREEN and command.
11. Nearest regressions, integration/interface proof, security evidence, targeted static/diff checks.
12. Design review + visual-state/viewport proof when applicable.
13. Runtime dependency/ownership observation if applicable.
14. Risk/capability tier, review policy/evidence.
15. Potential durable design impact and documentation impact.
16. Stop conditions/remote handoff.

Do not include full source brief, full topology/profile, full `DESIGN.md`/design history, all prototypes/screenshots, project history, unrelated specs, raw logs, or previous reports in task briefs.

## Propose bounded execution budgets

Recommend speed/balanced/quality from risk, leaving final selection to controller/user.

Per task/phase propose complexity/task budget, maximum unique roles/turns, one fixer wave, broad suite/build timing, high-judgment count, context limits, audit threshold, STOP_AND_RESCOPE.

Design review does not automatically create another role. Balanced may use combined reviewer with design responsibilities; maximum-quality/design-critical work may route design-specialist review only within the existing budget.

Never plan second fixer wave. Never plan parallel writers in one checkout. Specialist routing, number of areas and number of screens cannot inflate agent budget automatically. Independent read-only research/review are the only default parallel candidates.

## Validate G3 and complete plan

Before returning:

1. Trace every functional/`U-` through coverage matrix.
2. Confirm paths/commands/topology/runtime facts against repository or bounded discovery gate.
3. Check task dependencies/cycles/shared-file conflicts.
4. Check every selected `S-` owner/negative proof/review/verification.
5. Check G3 both directions: no live `U-` without task/proof; no product task without source/enabling justification.
6. Confirm each task has one primary area and bounded `AREA_CONTEXT_SET`.
7. Confirm every UI task has one design identity and bounded `DESIGN_CONTEXT_SET`, or explicit `DESIGN_NOT_APPLICABLE`.
8. Confirm every drift-prone cross-area seam has one shared `IC-xx` contract/freeze order and dependent tasks reference same identity.
9. Confirm runtime actions are not implied by runtime map; missing ownership/permission explicit.
10. Confirm design review/visual evidence is separated from technical E2E and G4; missing rendering capability is explicit.
11. Confirm specialist roles stay inside existing role/turn budget and permission envelope.
12. Re-run complexity merge pass; >16 trustworthy tasks -> split unless separately evidenced rescope.
13. Check focused tests fail intended reason and broad suites aren't repeated unnecessarily.
14. Check each task can stop without corrupting next task.
15. Identify design/docs impact candidates but do not update root `DESIGN.md` or other docs from an implementer task merely to make work pass.
16. Remove fake facts/duplicated requirements/implementation prose/options disguised as required.

Return:

- `PLAN_READY` with saved complete plan, coverage, topology/area routing, required interfaces, frozen design identity/design routing where applicable, tier, task budget;
- `PLAN_READY_TO_SAVE` inline + intended path;
- `NEEDS_CONTEXT` one exact question;
- `BLOCKED` architecture/traceability/interface/design/runtime contradiction or missing authority;
- `CONTEXT_TOO_BROAD` with required project split/context correction;
- `DESIGN_CONTEXT_TOO_BROAD` with exact UI/design split needed;
- `SPLIT_REQUIRED` with corrected task map.

Do not dispatch or edit product code. Hand `PLAN_READY` to controller only when execution requested/delegated.
