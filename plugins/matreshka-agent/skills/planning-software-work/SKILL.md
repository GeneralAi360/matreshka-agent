---
name: planning-software-work
description: >-
  Convert a confirmed software specification or bounded change into an implementation plan with requirement coverage, security controls, small ordered tasks, exact repository paths, focused RED/GREEN checks, review gates, and stop conditions. Use when the user asks for a coding plan or task breakdown but does not yet want the plan executed.
---

# Plan Software Work

Produce an executable plan, not implementation. Start only from a confirmed specification, an authoritative requirement, or a small change whose behavior and boundaries are already unambiguous.

Read [task-decomposition.md](references/task-decomposition.md) before splitting work or validating the final task map. Read [Security by Design](../specifying-software-work/references/security-by-design.md) when the specification has `S-` requirements or the task touches a security boundary. Use [implementation-plan-template.md](assets/implementation-plan-template.md) when producing the plan artifact.

## Validate the planning input

1. Read the confirmed specification, applicable repository instructions, and any `S-` requirements.
2. Inspect current source, public interfaces, schemas, migrations, tests, package scripts, and nearby patterns in read-only mode.
3. Record the exact baseline, constraints, non-goals, permission boundaries, and remote handoffs.
4. Identify contradictions, unresolved architectural decisions, missing acceptance outcomes, and security controls without a negative proof.
5. Return `NEEDS_CONTEXT` for one exact uninspectable fact, or `BLOCKED` when specification authority is missing. Do not make architectural decisions silently inside a plan.

Do not invent file paths, symbols, commands, models, or interfaces. Discover them safely. If discovery depends on a later environment, make the first gate a bounded read-only discovery with a required output; do not use a fake placeholder as though it were executable.

## Create the documentation artifact

Use the confirmed specification slug and write the plan to `docs/plans/YYYY-MM-DD-<safe-kebab-slug>-plan.md`, unless the inspected repository has a clear compatible convention. When local documentation writes are authorized, create only missing `docs/`, `docs/specs/`, and `docs/plans/` directories; do not replace or reorganize existing documentation.

When documentation writes are not authorized, produce the complete plan inline and return `PLAN_READY_TO_SAVE` with the exact intended path. Do not claim that the plan is saved. Documentation writes do not grant product-code, Git, remote, deploy, migration, dependency-install, or secret authority.

## Build requirement and security coverage first

Create a coverage matrix before Task 1:

```text
requirement or security control -> task -> verification evidence
```

Include every selected `S-` control, its negative security behavior, migration/rollback, compatibility, observability, and handoff requirements when applicable. Every confirmed requirement must map to at least one task and one proof. Every task must map back to a requirement or an explicitly justified enabling step.

Stop if the matrix exposes an unresolved design gap.

## Decompose into reviewable tasks

Make each task produce one independently reviewable result with:

- one primary subsystem or security boundary;
- one coherent allowlist;
- one focused RED/GREEN cycle;
- one task verification gate;
- explicit non-goals and stop conditions.

For each security-relevant task, add the selected `S-` IDs, exact authorization/input/output/dependency boundary, at least one negative test or review proof, and a required security-review tier. Never put a security control into a generic final checklist without a task owner.

Treat file counts as risk signals. Prefer one to three production files and one to two test files, but split by independent outcomes and boundaries rather than arbitrary numbers.

Return `SPLIT_REQUIRED` when one task combines migration with runtime, auth with UI, provider execution with persistence, execution with report assembly, separate security and experience designs, or several acceptance results that can pass independently.

## Order dependencies deliberately

Order tasks so that contracts and test seams precede consumers. Keep migrations, compatibility layers, runtime changes, remote application, and cleanup as distinct stages when they have different rollback or permission boundaries.

For each task, state:

1. Goal and requirement IDs.
2. Inputs and exact existing interfaces.
3. Produced interface or behavior.
4. Exact write allowlist and inspect-only scope.
5. Non-goals and forbidden actions.
6. Focused RED check and expected failure reason.
7. Minimal GREEN behavior and focused command.
8. Nearest regressions, selected security evidence, and targeted static/diff checks.
9. Risk and required capability tier.
10. Review policy and evidence.
11. Stop conditions and remote handoff.

Do not include full project history, unrelated specifications, raw logs, or previous reports in a task brief.

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

## Validate the complete plan

Before returning the plan:

1. Trace every requirement through the coverage matrix.
2. Confirm every path and command against the repository or label the bounded discovery gate truthfully.
3. Check task dependencies for cycles and hidden shared-file conflicts.
4. Check that every selected `S-` requirement has an explicit task owner, negative proof, and review/verification owner.
5. Check that focused tests fail for the intended reason and task gates do not repeat broad suites unnecessarily.
6. Check that each task can stop without corrupting the next task.
7. Remove placeholders, duplicated requirements, implementation prose, and optional work disguised as required scope.

Return one of:

- `PLAN_READY` with the saved complete plan and coverage matrix;
- `PLAN_READY_TO_SAVE` with the complete inline plan and exact intended path;
- `NEEDS_CONTEXT` with one exact question;
- `BLOCKED` with the design contradiction or missing authority;
- `SPLIT_REQUIRED` with a corrected task map.

Do not dispatch or edit product code. Hand `PLAN_READY` to `orchestrating-subagent-work` only when execution is requested or already delegated.
