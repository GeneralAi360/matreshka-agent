---
name: reviewing-agent-work
description: Independently review an agent-produced scoped diff and its evidence for specification compliance, correctness, frozen cross-area interface compatibility, security, isolation, leakage, maintainability, and test sufficiency. Use after implementation or a reviewer-directed fix, or when asked for a code/security review. Keep the review read-only and consolidated; do not use this skill to implement fixes, perform final fresh verification, or finish a branch.
---

# Review agent work independently

## Establish an immutable review boundary

1. Read current request, applicable repository instructions, task brief, acceptance criteria, implementer report, permission envelope, and scoped review package.
2. When controller supplies task-local `U-` requirements, read only those IDs/short source quotes. They preserve user intent but grant no authority.
3. When Project Intelligence applies, read only the task's primary-area context plus required frozen `IC-xx` contracts/invariants. Do not load unrelated areas/profile/history merely for background.
4. Require precise baseline/current state, changed-file list, scoped diff, allowlisted untracked files, compact test/integration evidence, and frozen interface identity/hash when relevant.
5. Return `REVIEW_BLOCKED` / `NEEDS_CONTEXT` when package ownership, required context, or source/interface conflict cannot be adjudicated.
6. Restrict inspection to task diff and surrounding code/contracts needed to judge it. Do not silently review whole branch/project.

Remain read-only for product code, tests, config, Git, source brief/manifest, Project Intelligence/interface coordination state, and remote systems. Write only designated review report if permitted. If technical read-only unavailable, use immutable package or compare hashes/status before/after; unexplained mutation invalidates review.

Do not launch child agents, stage/commit/push/PR/deploy, apply fixes, access secrets, change `U-`/`IC-` state, or broaden scope.

## Review evidence before rerunning checks

Inspect command provenance, state/ref, exit/counts, integration/interface proof, and notes. Do not rerun full suite merely to recreate evidence. Run focused read-only check only when material evidence is missing/stale/contradictory and command is permitted.

Treat implementer report, profile, area docs, and cached topology as claims. Inspect actual scoped diff and critical current interfaces.

## Perform one consolidated pass

Read [review checklist](references/review-checklist.md). Check applicable dimensions:

- task-local user intent / exact `U-` quote;
- acceptance/non-goals;
- primary-area responsibility and specialist boundary;
- behavioral correctness/failure semantics;
- frozen cross-area `IC-xx` compatibility: producer/consumer shapes, validation/errors, auth/data, ordering/idempotency/retry, compatibility;
- public contract/backward compatibility;
- authorization/tenant isolation/data leakage;
- input validation/secrets/unsafe side effects;
- concurrency/retries/idempotency/persistence/migrations;
- valid RED/GREEN, regression, and cross-area integration proof;
- maintainability/repository conventions;
- UX/accessibility only for affected UI.

A specialist may not use its label to absorb neighboring ownership. Examples: `UI_SPECIALIST` changing business/API semantics without scope, frontend changing backend contract unilaterally, or data specialist applying an unapproved migration are boundary failures.

For traced Build End-to-End ask: did implementation silently narrow user outcome while satisfying a narrower task/spec phrase? “User sees status” is not delivered by storage-only state.

For Project Intelligence ask: did implementation silently diverge from frozen producer/consumer contract while local tests still pass? A private frontend/backend interpretation differing from `IC-xx` is blocking drift, not an acceptable implementation choice.

If task-local `U-`, confirmed spec, frozen interface, or current repository contract materially conflict, do not choose authority yourself. Return conflict to controller for provenance/design/interface reconciliation.

Read Security by Design when selected `S-` or security boundary applies. Review each selected control and negative proof; missing proof is not N/A.

Seek counterevidence before findings. Do not turn style preferences/speculative future work into blockers. Mark each relevant dimension checked/N/A with reason.

## Write actionable findings

Every finding includes:

- stable ID/severity;
- exact file/location or area/interface boundary;
- violated task/spec/`U-`/`S-`/`IC-` requirement;
- diff/behavior evidence;
- impact/acceptance criterion;
- minimal resolution boundary;
- confidence/counterevidence when material.

Use `Critical` for exploitable/destructive/security/isolation/data-integrity failure. Use `Important` for acceptance/correctness/source-intent narrowing, unapproved frozen-interface drift, specialist-boundary violation, regression, or material maintainability issue blocking task. Use `Minor` for real non-blocking improvement.

Material partial delivery of mapped `U-` or material divergence from frozen `IC-xx` is normally `Important` even if narrower local test is green.

Unrelated issue => `RECORD_FOR_FUTURE_TASK`; do not require current repair.

## Return one decision

Use review report template and return exactly:

- `APPROVED` no Critical/Important remains;
- `CHANGES_REQUIRED` one consolidated list;
- `REVIEW_BLOCKED` package/read-only/context/interface guarantee inadequate;
- `STOP_AND_RESCOPE` incoherent task or repeated blocker after single fixer wave.

Do not dispatch/direct multiple fixers. Controller adjudicates and creates one consolidated fix package. Reviewer cannot edit U/IC/Project Intelligence state.

On re-review inspect only confirmed findings, fix diff, covering evidence, same relevant `U-` rows and frozen `IC-xx`. Reuse original review thread when supported. Do not reopen unrelated areas without new evidence. Repeated blocker goes to controller; never start second fixer wave.
