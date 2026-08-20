---
name: planning-software-work
description: >-
  Convert a confirmed software specification or bounded change into an implementation plan with requirement coverage, project-area and interface routing, security controls, small ordered tasks, exact repository paths, focused RED/GREEN checks, review gates, and stop conditions. Use when the user asks for a coding plan or task breakdown but does not yet want the plan executed.
---

# Plan Software Work

Produce an executable plan, not implementation. Start only from a confirmed specification, authoritative requirement, or small change whose behavior/boundaries are already unambiguous.

Read [task-decomposition.md](references/task-decomposition.md) before splitting work or validating the final task map. Read [complexity-tiers.md](references/complexity-tiers.md) before deciding task boundaries. Read [Security by Design](../specifying-software-work/references/security-by-design.md) for selected/high-risk `S-` requirements. When the controller supplies Build End-to-End `U-` rows, read [brief traceability](../building-end-to-end/references/brief-traceability.md). When the controller supplies Project Intelligence, read [project-intelligence.md](../orchestrating-subagent-work/references/project-intelligence.md) and preserve current area/context/interface/runtime facts without treating them as authority. Use [implementation-plan-template.md](assets/implementation-plan-template.md).

## Validate planning input

1. Read confirmed specification, applicable repository instructions, selected `S-` requirements, controller-supplied `U-` rows, and current Project Intelligence summary when provided.
2. Inspect current source, public interfaces, schemas/migrations, tests, package/workspace scripts, runtime seams, and nearby patterns in read-only mode.
3. Revalidate affected Project Topology areas and any durable interface/runtime docs needed by the change. Repository evidence wins over stale profile/context prose.
4. Record exact baseline, constraints, non-goals, permission boundaries, affected areas, and remote/runtime handoffs.
5. Identify contradictions, unresolved architecture, missing acceptance outcomes, source-intent rows not represented in spec, security controls without negative proof, and producer/consumer seams that can drift.
6. Return `NEEDS_CONTEXT` for one exact uninspectable fact, `BLOCKED` when specification/interface authority is missing, or `CONTEXT_TOO_BROAD` when correct planning cannot preserve bounded area context. Do not make architecture/interface decisions silently inside a plan.

Do not invent file paths, symbols, commands, models, interfaces, topology areas, or runtime ownership. Discover safely. If discovery depends on a later environment, make the first gate bounded/read-only; do not use a fake placeholder as executable truth.

A source brief, `U-` manifest, project profile, topology map, or area doc is provenance/candidate context, not permission or a reason to bypass confirmed specification. Return material conflicts to controller.

## Create documentation artifact

Use confirmed spec slug and write `docs/plans/YYYY-MM-DD-<safe-kebab-slug>-plan.md`, unless repository has a compatible convention. When docs writes are authorized, create only missing compatible directories; do not reorganize existing docs.

When docs writes are not authorized, return complete inline plan as `PLAN_READY_TO_SAVE`. Documentation writes do not grant product-code, Git, browser/process, remote, deploy, migration, dependency-install, secret, or interface-implementation authority.

## Build requirement/security coverage first

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

Include every selected `S-` control, negative proof, migration/rollback, compatibility, observability, and handoff requirement when applicable. Stop if matrix exposes unresolved design gap, orphan requirement, or unsourced product work.

## Apply Project Intelligence before task cutting

Use current topology to name only areas affected by this plan. A website does not automatically require separate frontend/backend tasks; split/route based on actual repository ownership and independently reviewable seams.

For each proposed task determine:

- primary area;
- adjacent areas required for correctness;
- minimal `AREA_CONTEXT_SET` and explicit exclusions;
- cross-area `IC-xx` contracts consumed/produced;
- runtime dependency/status/log observation needed for tests;
- specialist role archetype only when useful;
- potential durable documentation impact.

### Cross-area interface contracts

When a single outcome crosses independently owned producer/consumer areas and assumptions can drift, plan one controller-owned `IC-xx` contract before dependent writers start. Define source requirements, producer/consumer areas, input/output/errors, auth/data boundary, delivery semantics, compatibility, integration proof, and freeze order.

Do not let separate frontend/backend/data tasks invent different versions of the seam. A frozen material change later returns `INTERFACE_CHANGED` to controller reconciliation.

Do not create an interface artifact for a cohesive single-area helper seam without an independent consumer/version boundary.

### Context routing

A task context includes only relevant `U-`/`S-`, primary-area facts, required neighboring interface contracts/invariants, focused commands/paths, and required security/data/runtime facts. Exclude unrelated area docs/history/reports/logs/full source brief/branch diff.

If correctness needs several independent boundaries, split or return `CONTEXT_TOO_BROAD`; never hide a dependency to make the context smaller.

### Specialist routing

Select one role archetype only when it materially improves correctness/context/boundary ownership. Examples: general, frontend, backend, data/migration, UI, E2E, documentation/browser/operator roles from Project Intelligence.

Role archetypes reuse existing Matreshka skills. They do not add agent turns, tool authority, filesystem scope, Git/network/process/browser/secret/remote permission, or relax execution-profile/security requirements.

## Select complexity tier

Choose exactly one tier from `complexity-tiers.md` based on independently reviewable product/data/security/interface boundaries, not spec length/file count/desired speed:

- `T0` one direct reviewable task;
- `T1` normally 2–3 tasks;
- `T2` normally 4–8;
- `T3` normally 9–16;
- above safe T3 -> `SPLIT_REQUIRED` / `DECISION_MAP_REQUIRED`.

Counts are budgets, not quotas. `T0 + maximum quality` is valid. Multiple topology areas do not automatically mean multiple tasks or more agent budget. Parallel writers remain forbidden in one checkout.

## Decompose into reviewable tasks

Each task should produce one independently reviewable result with:

- one primary area/subsystem/security boundary;
- one coherent allowlist and bounded area context set;
- frozen `IC-xx` identities when relevant;
- one focused RED/GREEN cycle;
- one task verification gate plus integration proof when needed;
- explicit non-goals, specialist boundary, docs-impact candidate, and stop conditions.

For security tasks include selected `S-`, exact auth/input/output/dependency boundary, negative test/review proof, required security-review tier.

Treat file count as risk signal. Prefer small changes, but split by independent outcomes/boundaries. Return `SPLIT_REQUIRED` when one task mixes migration/runtime, auth/UI, provider/persistence, separate security/experience designs, or several acceptance results that can pass independently.

After draft, run mandatory merge pass: merge avoidable cold-start boundaries sharing one result/seam when no independent review/rollback/evidence/security/ownership benefit exists. Re-check tier.

At T0 there is still exact task brief, review policy, verification, docs-impact decision, and applicable G4.

## Order dependencies deliberately

Order contracts/test seams before consumers. Keep migrations, compatibility layers, runtime changes, remote application, and cleanup distinct when rollback/permission boundaries differ.

For each task state:

1. Goal + `U-`/functional and `S-` IDs.
2. Short source quote/reference when applicable.
3. Primary/adjacent areas and context set.
4. Frozen `IC-xx` contracts and exact interfaces.
5. Exact write allowlist/inspect-only scope.
6. Role archetype, owned responsibility, forbidden neighboring responsibility.
7. Non-goals/forbidden actions.
8. Focused RED and expected failure.
9. Minimal GREEN and command.
10. Nearest regressions, integration/interface proof, security evidence, targeted static/diff checks.
11. Runtime dependency/ownership observation if applicable.
12. Risk/capability tier, review policy/evidence.
13. Documentation impact candidate.
14. Stop conditions/remote handoff.

Do not include full source brief, full topology/profile, project history, unrelated specs, raw logs, or previous reports in task briefs.

## Propose bounded execution budgets

Recommend speed/balanced/quality from risk, leaving final selection to controller/user.

Per task/phase propose complexity/task budget, maximum unique roles/turns, one fixer wave, broad suite/build timing, high-judgment count, context limits, audit threshold, STOP_AND_RESCOPE.

Never plan second fixer wave. Never plan parallel writers in one checkout. Specialist routing and number of areas cannot inflate agent budget automatically. Independent read-only research/review are the only default parallel candidates.

## Validate G3 and complete plan

Before returning:

1. Trace every functional/`U-` through coverage matrix.
2. Confirm paths/commands/topology/runtime facts against repository or bounded discovery gate.
3. Check task dependencies/cycles/shared-file conflicts.
4. Check every selected `S-` owner/negative proof/review/verification.
5. Check G3 both directions: no live `U-` without task/proof; no product task without source/enabling justification.
6. Confirm each task has one primary area and bounded context set.
7. Confirm every drift-prone cross-area seam has one shared `IC-xx` contract/freeze order and dependent tasks reference the same identity.
8. Confirm runtime actions are not implied by runtime map; missing ownership/permission is explicit.
9. Confirm specialist roles stay inside existing role/turn budget and permission envelope.
10. Re-run complexity merge pass; >16 trustworthy tasks -> split unless separately evidenced rescope.
11. Check focused tests fail intended reason and broad suites aren't repeated unnecessarily.
12. Check each task can stop without corrupting next task.
13. Identify documentation impact candidates but do not update docs before verified behavior.
14. Remove fake facts/duplicated requirements/implementation prose/optional disguised as required.

Return:

- `PLAN_READY` with saved complete plan, coverage, topology/area routing, required interfaces, tier, task budget;
- `PLAN_READY_TO_SAVE` inline + intended path;
- `NEEDS_CONTEXT` one exact question;
- `BLOCKED` design/traceability/interface/runtime contradiction/missing authority;
- `CONTEXT_TOO_BROAD` with required split/context correction;
- `SPLIT_REQUIRED` with corrected task map.

Do not dispatch or edit product code. Hand `PLAN_READY` to controller only when execution requested/delegated.
