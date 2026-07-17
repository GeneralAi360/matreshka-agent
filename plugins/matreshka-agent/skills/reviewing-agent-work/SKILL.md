---
name: reviewing-agent-work
description: Independently review an agent-produced scoped diff and its evidence for specification compliance, correctness, security, isolation, leakage, maintainability, and test sufficiency. Use after implementation or a reviewer-directed fix, or when asked for a code/security review. Keep the review read-only and consolidated; do not use this skill to implement fixes, perform final fresh verification, or finish a branch.
---

# Review agent work independently

## Establish an immutable review boundary

1. Read the current request, applicable repository instructions, task brief, acceptance criteria, implementer report, permission envelope, and scoped review package.
2. Require a precise baseline and current state, changed-file list, scoped diff, allowlisted untracked files, and compact test evidence.
3. Return `REVIEW_BLOCKED` or `NEEDS_CONTEXT` when the package cannot identify what belongs to the task.
4. Restrict inspection to the task diff and only the surrounding code or contracts needed to judge it. Do not silently review the whole branch.

Remain read-only for product code, tests, configuration, Git state, and remote systems. Write only the designated review report when that output path is explicitly permitted; otherwise return the report inline. If technical read-only enforcement is unavailable, use the supplied immutable package or compare scoped hashes/status before and after. Any unexplained mutation invalidates the review.

Do not launch child agents, stage, commit, push, open a pull request, deploy, apply fixes, access secrets, or broaden scope.

## Review evidence before rerunning checks

Inspect command provenance, state/ref, exit codes, counts, and relevant notes. Do not rerun a full suite merely to recreate complete and consistent evidence. Run a focused read-only check only when evidence is missing, stale, contradictory, or insufficient for a material acceptance or security claim and the command is permitted.

Treat the implementer report as a claim, not proof. Inspect the actual scoped diff and critical interfaces.

## Perform one consolidated pass

Read [the review checklist and severity guide](references/review-checklist.md). Check only applicable dimensions:

- acceptance and explicit non-goals;
- behavioral correctness and failure semantics;
- public contract and compatibility;
- authorization, tenant or organization isolation, and data leakage;
- input validation, secret handling, and unsafe side effects;
- concurrency, retries, idempotency, persistence, and migrations when touched;
- test quality, valid RED/GREEN evidence, and regression coverage;
- maintainability and repository conventions;
- user experience and accessibility only for affected UI behavior.

Seek counterevidence before raising a finding. Do not convert style preference or speculative future work into a blocker.

Mark each listed review dimension either checked or `N/A` with a short reason. Do not silently omit security, isolation, leakage, tests, or UX when the task makes them relevant.

## Write actionable findings

Give every finding:

- a stable ID and severity;
- exact file/location or contract boundary;
- evidence from the diff or behavior;
- concrete impact and affected acceptance criterion;
- the smallest required condition for resolution;
- confidence or counterevidence when material.

Use `Critical` for an exploitable or destructive safety, security, isolation, or data-integrity failure that must stop progression. Use `Important` for an acceptance, correctness, regression, or material maintainability failure that blocks the task. Use `Minor` for a real non-blocking improvement that does not violate acceptance criteria.

Mark an unrelated real issue `RECORD_FOR_FUTURE_TASK`. Do not require its repair in the current change unit.

## Return one decision

Use [the review report template](assets/review-report-template.md) and return exactly one primary decision:

- `APPROVED` when no Critical or Important finding remains;
- `CHANGES_REQUIRED` with one consolidated finding list;
- `REVIEW_BLOCKED` when the package or read-only guarantee is inadequate;
- `STOP_AND_RESCOPE` when the task boundary is incoherent or a repeated Critical/Important finding remains after the single fixer-wave.

Do not dispatch or direct multiple fixers. Let the controller adjudicate disputed or conflicting findings and create one consolidated fix package.

On re-review, inspect only confirmed findings, the fix diff, and covering evidence. Reuse the original review identity/thread when the platform supports it. Do not reopen resolved or unrelated areas without new evidence. Report a repeated blocking finding to the controller; never start a second fixer-wave yourself.
