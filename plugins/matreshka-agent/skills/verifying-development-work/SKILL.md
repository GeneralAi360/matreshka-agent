---
name: verifying-development-work
description: Verify development claims against current repository state and acceptance criteria using fresh, proportionate command evidence. Use after implementation or fixes, before declaring a task, phase, branch, or handoff complete, or when asked to prove that existing work functions. Do not use to implement fixes, perform an independent code review, investigate an unknown root cause, or publish the result.
---

# Verify claims with fresh evidence

## Define what must be proved

1. Read the current request, applicable repository instructions, approved design or task brief, acceptance criteria, permission envelope, implementation report, review decision, and current state.
2. Resolve the project root and baseline/current identity. Record pre-existing dirty files and avoid attributing them to the task.
3. Read [the quality-gate rules](references/quality-gate.md) when the controller supplies a gate or a reusable project profile suggests checks.
4. Translate every completion claim into an observable criterion and a permitted verification method.
5. Build a compact matrix from claim to command, inspection, or external handoff. Preserve the source and status of every selected quality-gate row.

Do not launch child agents. Do not edit product code or tests, repair failures, stage, commit, push, open a pull request, deploy, mutate a remote system, install dependencies, or read secrets. Write only an authorized verification report or run-owned evidence artifact. Return fixes, Git publication, dependency changes, and remote actions to the controller. Verification must preserve the state it is judging.

## Choose the right verification tier

Read [the verification tiers and evidence rules](references/verification-tiers.md).

Use the smallest tier that proves the requested status:

- **Focused:** reproduce the changed behavior after a small fix or during task work.
- **Task gate:** run the task suite, one to three nearest regressions, targeted static checks, and diff checks required by the plan.
- **Phase/final gate:** run integration checks, build, or a broader suite once when the phase, branch, or release claim requires them.

Run a build only when the changed path, repository policy, or final acceptance contract requires it. Run security, secret, migration, or compatibility checks only when the affected boundary or policy requires them. Do not substitute a large suite for a missing targeted acceptance check.

Use [the quality-gate template](assets/quality-gate-template.md) when a repeated or phase-level verification needs a durable evidence declaration. The template does not grant a command, dependency install, network action, hook, or repair. Mark unavailable required rows `NOT_RUN` or `BLOCKED`; never silently omit them.

## Produce fresh evidence

Run critical permitted commands against the exact current state. Previous agent reports and screenshots may guide selection but do not prove the current result.

For externally produced evidence such as immutable CI, accept it only when its commit/ref, configuration, freshness, and relevant job scope match the state being verified. Otherwise rerun locally or mark the claim unverified.

For each check, record:

- exact safe command or interaction;
- state/ref or relevant hashes;
- exit code;
- pass, fail, and skip counts when available;
- one decisive note;
- any output limitation or environmental caveat.

Avoid copying huge logs. Preserve a safe reference when the report needs traceability. Never include credentials, tokens, private payloads, or environment-file contents.

## Protect the working state

Record scoped status or hashes before checks that may generate files. Inspect the state afterward. Do not silently keep generated tracked changes, snapshots, lockfile edits, formatter output, or modified fixtures. Report any unexpected mutation and invalidate affected evidence until the controller decides how to handle it.

Do not reset, clean, discard, or overwrite user-owned changes.

## Distinguish new, pre-existing, and unowned failures

When a required check fails, reproduce it on the recorded baseline only when safe and practical through an existing isolated state. Do not alter the current checkout to obtain that comparison.

Classify the result as:

- task-owned regression, when evidence proves the current change introduced it;
- pre-existing failure, when matching baseline evidence proves it already existed;
- unresolved attribution, when ownership cannot be established;
- environment or infrastructure blocker, when the intended behavior never executes.

Never turn “probably pre-existing” into a pass.

## Set an honest status

Use [the verification report template](assets/verification-report-template.md). Choose one status:

- `VERIFIED` when every required criterion is supported by fresh, current evidence and no blocking review finding remains;
- `PARTIALLY_VERIFIED` when proved criteria are useful but at least one required criterion could not be checked;
- `FAILED` when current evidence contradicts an acceptance claim;
- `BLOCKED` when environment, permissions, or missing inputs prevent meaningful checks;
- `HANDOFF_REQUIRED` when a named external operator must complete an allowed remote verification.

Do not use `VERIFIED` because code looks correct, an agent said tests passed, one unrelated suite passed, or no failure was observed. List unverified claims explicitly. Return failed implementation to the controller; do not fix it inside verification.

Do not extract or promote learning in this role. The controller may use the final report as evidence for an explicitly enabled, human-reviewed learning proposal.
