---
name: implementing-with-tests
description: Implement a bounded software feature or bug fix through a focused test-first cycle and produce evidence for review. Use when an approved task requires code or configuration changes, a regression test, focused RED/GREEN proof, and nearby regression checks. Do not use for design-only work, root-cause diagnosis without an authorized fix, independent review, verification-only requests, or branch finishing.
---

# Implement with focused tests

## Establish the task boundary

1. Read the current user request, applicable repository instructions, approved task brief, and permission envelope.
2. Resolve the project root and the real paths of every allowed file before writing. Stop if a symlink, nested repository, submodule, or changed root crosses the approved boundary.
3. Record the baseline, including pre-existing dirty files. Preserve work not owned by this task.
4. Confirm one observable goal, exact acceptance criteria, the file allowlist, non-goals, permitted commands, and stop conditions.
5. Return `SPLIT_REQUIRED` when the task contains independent outcomes or crosses multiple implementation or security boundaries.

Do not launch child agents. Do not stage, commit, push, open a pull request, deploy, access a remote system, install dependencies, or read secrets. Implementation owns only allowlisted product/test writes, approved local checks, and the one designated run-state report/evidence path. Return Git, dependency, secret, network, and remote actions to the controller; route an authorized finish through `finishing-development-work`.

## Select the smallest useful behavior

Choose one focused executable example that fails without the requested behavior and passes when it exists. Prefer a public interface or the nearest stable boundary over private implementation details.

Read [the focused test cycle](references/focused-test-cycle.md) when selecting a test seam, separating a valid RED from an infrastructure failure, or considering a test-first exception.

## Produce RED evidence

1. Add or adjust the smallest test that expresses the missing behavior.
2. Run only its focused command.
3. Confirm that it fails for the expected behavioral reason.
4. Record the command, exit code, pass/fail counts when available, and the decisive failure note.

Do not accept a syntax error, missing dependency, broken fixture, unrelated failure, or already-passing test as RED. Repair only task-owned test setup within the allowlist. Otherwise return `BLOCKED` with evidence.

Use a test-first exception only when the behavior is genuinely non-executable in the current environment, such as prose-only documentation, generated artifacts controlled elsewhere, or unavailable hardware. Record the reason before implementation and define the strongest permitted alternate check. Never use schedule pressure as an exception.

## Reach GREEN minimally

1. Change only what is necessary to satisfy the focused behavior.
2. Keep public contracts, error semantics, tenant boundaries, and compatibility constraints from the brief intact.
3. Re-run the same focused command until it passes or the bounded attempt budget is exhausted.
4. Stop to diagnose through `debugging-systematically` when the failure mechanism is unclear. Do not stack speculative fixes.

Record unrelated defects as adjacent findings. Do not fix them in the current task.

## Run the task gate

After focused GREEN, run only the checks required by the task and repository policy:

- the focused task suite;
- one to three nearest regression suites;
- targeted typecheck or lint for touched paths;
- a diff/whitespace check when available;
- a build only when the changed path or policy requires it;
- a targeted security or secret scan only for relevant boundaries.

After a reviewer-directed fix, run the covering test and nearest regression rather than the full suite unless the fix changes the planned verification tier.

Check the final scoped diff and file list. Stop with `STOP_AND_RESCOPE` when the allowed scope, security boundary, or one-fixer-wave budget has been exceeded.

## Report without claiming more than proved

Use [the implementation report template](assets/implementation-report-template.md). Include:

- status and completed scope;
- changed files and untouched dirty files;
- valid RED and fresh GREEN evidence;
- task-gate evidence;
- test-first exceptions or skipped checks;
- assumptions, adjacent findings, and pre-existing failures;
- permissions still required;
- exact next action for the controller.

Return `PARTIALLY_VERIFIED` rather than `COMPLETE` when a required check could not run. Treat the report as a handoff claim; allow the controller and reviewer to inspect the diff and reproduce critical evidence.
