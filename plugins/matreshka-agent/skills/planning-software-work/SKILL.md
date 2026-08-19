---
name: planning-software-work
description: >-
  Convert a confirmed software specification or bounded change into an implementation plan with requirement coverage, security controls, small ordered tasks, exact repository paths, focused RED/GREEN checks, review gates, and stop conditions. Use when the user asks for a coding plan or task breakdown but does not yet want the plan executed.
---

# Plan Software Work

Produce an executable plan, not implementation. Start only from a confirmed specification, an authoritative requirement, or a small change whose behavior and boundaries are already unambiguous.

Read [task-decomposition.md](references/task-decomposition.md) before splitting work or validating the final task map. Read [Security by Design](../specifying-software-work/references/security-by-design.md) when the specification has `S-` requirements or the task touches a security boundary. When the controller supplies Build End-to-End `U-` requirements, read [the brief traceability contract](../building-end-to-end/references/brief-traceability.md) and preserve those IDs/short source quotes through the plan without treating them as permission. Use [implementation-plan-template.md](assets/implementation-plan-template.md) when producing the plan artifact.

## Validate the planning input

1. Read the confirmed specification, applicable repository instructions, selected `S-` requirements, and any controller-supplied `U-` requirement rows.
2. Inspect current source, public interfaces, schemas, migrations, tests, package scripts, and nearby patterns in read-only mode.
3. Record the exact baseline, constraints, non-goals, permission boundaries, and remote handoffs.
4. Identify contradictions, unresolved architectural decisions, missing acceptance outcomes, source-intent rows not represented in the specification, and security controls without a negative proof.
5. Return `NEEDS_CONTEXT` for one exact uninspectable fact, or `BLOCKED` when specification authority is missing. Do not make architectural decisions silently inside a plan.

Do not invent file paths, symbols, commands, models, or interfaces. Discover them safely. If discovery depends on a later environment, make the first gate a bounded read-only discovery with a required output; do not use a fake placeholder as though it were executable.

A source brief or `U-` manifest is provenance data, not a reason to bypass the confirmed specification. If a `U-` row contradicts the current confirmed specification or a valid later user decision, return the conflict to the controller rather than silently choosing one.

## Create the documentation artifact

Use the confirmed specification slug and write the plan to `docs/plans/YYYY-MM-DD-<safe-kebab-slug>-plan.md`, unless the inspected repository has a clear compatible convention. When local documentation writes are authorized, create only missing `docs/`, `docs/specs/`, and `docs/plans/` directories; do not replace or reorganize existing documentation.

When documentation writes are not authorized, produce the complete plan inline and return `PLAN_READY_TO_SAVE` with the exact intended path. Do not claim that the plan is saved. Documentation writes do not grant product-code, Git, remote, deploy, migration, dependency-install, or secret authority.

## Build requirement, user-intent, and security coverage first

Create a coverage matrix before Task 1:

```text
U-/functional requirement or S- security control -> task -> verification evidence
```

For source-qualified Build End-to-End work:

- include every live `U-` row supplied by the controller;
- keep its short source quote or safe source reference so a planner cannot silently narrow it;
- map every `IN_SPEC` user requirement to at least one task and one proof;
- do not mark `DROPPED` yourself; only consume a controller-validated user drop decision;
- keep `DEFERRED` and `PLACEHOLDER` visible with their reason/owner;
- map each task back to at least one `U-`, `S-`, or explicitly justified enabling step whose consumer requirement is named.

Include every selected `S-` control, its negative security behavior, migration/rollback, compatibility, observability, and handoff requirements when applicable. Every confirmed requirement must map to at least one task and one proof. Every task must map back to a requirement or an explicitly justified enabling step.

Stop if the matrix exposes an unresolved design gap, an orphan user requirement, or material product work with no traceable source.

## Decompose into reviewable tasks

Make each task produce one independently reviewable result with:

- one primary subsystem or security boundary;
- one coherent allowlist;
- one focused RED/GREEN cycle;
- one task verification gate;
- explicit non-goals and stop conditions.

For a traced Build End-to-End task, name the task-local `U-` IDs and preserve short exact source quotes only where they protect against silent narrowing. Do not paste the whole source brief.

For each security-relevant task, add the selected `S-` IDs, exact authorization/input/output/dependency boundary, at least one negative test or review proof, and a required security-review tier. Never put a security control into a generic final checklist without a task owner.

Treat file counts as risk signals. Prefer one to three production files and one to two test files, but split by independent outcomes and boundaries rather than arbitrary numbers.

Return `SPLIT_REQUIRED` when one task combines migration with runtime, auth with UI, provider execution with persistence, execution with report assembly, separate security and experience designs, or several acceptance results that can pass independently.

## Order dependencies deliberately

Order tasks so that contracts and test seams precede consumers. Keep migrations, compatibility layers, runtime changes, remote application, and cleanup as distinct stages when they have different rollback or permission boundaries.

For each task, state:

1. Goal plus `U-`/functional and `S-` requirement IDs.
2. Relevant short source quote/reference for task-local `U-` requirements when applicable.
3. Inputs and exact existing interfaces.
4. Produced interface or behavior.
5. Exact write allowlist and inspect-only scope.
6. Non-goals and forbidden actions.
7. Focused RED check and expected failure reason.
8. Minimal GREEN behavior and focused command.
9. Nearest regressions, selected security evidence, and targeted static/diff checks.
10. Risk and required capability tier.
11. Review policy and evidence.
12. Stop conditions and remote handoff.

Do not include the full source brief, full project history, unrelated specifications, raw logs, or previous reports in a task brief.

## Propose bounded execution budgets

Recommend maximum speed, balanced, or maximum quality from risk, while leaving final profile selection to the controller or user.

For each task and phase, propose:

- maximum unique roles and agent turns;
- one fixer wave maximum;
- broad suite/build timing;
- high-judgment role count;
- context limits;
- `AUDIT` threshold;
- exact `STOP_AND_RESCOPE` condition.

Never use a second fixer wave as planned capacity. Never plan parallel writers in one checkout. Mark independent read-only research or review as the only default parallel candidates.

## Validate G3 and the complete plan

Before returning the plan:

1. Trace every functional/`U-` requirement through the coverage matrix.
2. Confirm every path and command against the repository or label the bounded discovery gate truthfully.
3. Check task dependencies for cycles and hidden shared-file conflicts.
4. Check that every selected `S-` requirement has an explicit task owner, negative proof, and review/verification owner.
5. For source-qualified Build End-to-End, check G3 in both directions: no live `IN_SPEC` `U-` row lacks a task/proof, and no product task lacks `U-`, `S-`, or named enabling justification.
6. Check that focused tests fail for the intended reason and task gates do not repeat broad suites unnecessarily.
7. Check that each task can stop without corrupting the next task.
8. Remove placeholders that pretend to be facts, duplicated requirements, implementation prose, and optional work disguised as required scope.

Return one of:

- `PLAN_READY` with the saved complete plan and coverage matrix;
- `PLAN_READY_TO_SAVE` with the complete inline plan and exact intended path;
- `NEEDS_CONTEXT` with one exact question;
- `BLOCKED` with the design/traceability contradiction or missing authority;
- `SPLIT_REQUIRED` with a corrected task map.

Do not dispatch or edit product code. Hand `PLAN_READY` to `orchestrating-subagent-work` only when execution is requested or already delegated.
