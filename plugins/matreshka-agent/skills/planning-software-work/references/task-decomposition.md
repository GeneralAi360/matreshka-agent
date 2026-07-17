# Task Decomposition Guide

Use this guide to turn a confirmed design into bounded, independently reviewable work.

## Planning invariants

Require:

```text
one task
= one measurable result
= one primary subsystem or security boundary
= one focused RED/GREEN cycle
= one task verification gate
= one independently reviewable diff
```

A commit may capture that unit only when Git history actions are authorized. A task remains reviewable without a commit when its baseline, current hashes, untracked allowlisted files, and scoped diff are exact.

## Strong split signals

Split when any signal creates independently testable or reversible work:

- migration plus runtime behavior;
- schema rollout plus data backfill;
- authentication or authorization plus interface wiring;
- provider adapter plus retry/fallback policy;
- provider execution plus persistence;
- persistence plus report assembly;
- API contract plus unrelated user experience redesign;
- local preparation plus remote application;
- feature delivery plus later cleanup;
- separate security and experience designs;
- several acceptance criteria that can pass or roll back independently.

Do not split purely by file. Several tightly coupled files can form one result; one file can contain multiple security boundaries that must be separated.

## File-count warning

Prefer tasks near:

- one to three production files;
- one to two focused test files;
- one public contract or one internal seam;
- one primary reviewer concern.

Exceed these values only with a written cohesion reason. If a task is likely to need more than one consolidated fixer wave, split before execution.

## Coverage matrix

Create stable requirement IDs. Map every row:

| Requirement | Source | Task | Verification | Negative/rollback evidence |
| --- | --- | --- | --- | --- |

Use separate rows for:

- user-visible behavior;
- input validation and failure shape;
- authorization and isolation;
- compatibility;
- migration and rollback;
- observability and redaction;
- performance constraints only when explicitly required;
- local-to-remote handoff.

Reject orphan requirements and tasks without requirement coverage.

## Task ordering heuristics

Prefer this dependency order when applicable:

1. Test seam or provider-neutral contract.
2. Pure domain behavior.
3. Boundary adapter.
4. Persistence or schema compatibility.
5. Orchestration/wiring.
6. User-facing integration.
7. Reporting/observability.
8. Remote handoff, rollout, and cleanup.

Change the order when the design requires a different safe migration sequence. Explain why.

## Exactness requirements

Resolve before dispatch:

- real project root and applicable instructions;
- exact files or tightly resolved globs;
- symbols and public interface names;
- current test runner and focused command;
- nearest regression commands;
- build/type/lint checks relevant to changed paths;
- baseline and pre-existing failures;
- remote operator boundary.

When an exact fact cannot be known in the current environment, define a read-only discovery gate with:

- a narrow question;
- allowed inspection scope;
- forbidden mutations;
- expected evidence;
- stop outcome if unresolved.

Do not write `TBD`, guess a filename, or leave a command that will silently run the whole suite.

## RED/GREEN design

For each task, choose one focused check that proves the missing behavior. State the expected RED reason so an unrelated failure does not count.

Define GREEN as the smallest behavior satisfying the task, not as all future refinements. Add one to three nearest regressions and targeted static/diff checks at the task gate.

Plan build, security scan, migration validation, or broad suite only when the changed path or phase warrants it. Run broad checks once at an integration or final boundary.

## Review policy in the plan

For low-risk work, permit controller verification or one combined reviewer according to profile.

For balanced work, plan:

```text
implementer -> combined reviewer -> same implementer fix -> same reviewer targeted recheck
```

For high-risk work, plan one spec reviewer and one security/code reviewer, followed by one consolidated fix and one targeted recheck by each original reviewer.

Never plan overlapping reviewers without distinct ownership. Never allow reviewers to dispatch fixes. Never plan more than one fixer wave.

## Execution profile budgets

Use the same numeric ceilings as the controller contract:

| Profile | Roles per task | Agent turns | Review and correction |
| --- | ---: | ---: | --- |
| Maximum speed | One implementer and at most one reviewer | At most four | Reviewer is optional; one same-implementer fix; no re-review for Minor-only changes when controller evidence is enough |
| Balanced | At most two: implementer and combined reviewer | At most four | Same implementer fixes once; same reviewer performs one targeted recheck |
| Maximum quality | At most three: implementer, spec reviewer, security/code reviewer | At most six | One consolidated same-implementer fix; each original reviewer rechecks only owned findings |

Prohibit maximum speed for authentication, authorization, tenant isolation, row-level security, destructive or data-transforming migrations, payments, secrets, provider credentials, persistence guarantees, production configuration, and irreversible remote actions.

The host's highest-cost or experimental reasoning tier is not part of any profile by default. Plan it only when the permission envelope names the exact role and bounded turn count and explains why ordinary high-judgment capability is insufficient.

## Context package

Keep a task brief under 2,000 words. Include only:

- task-local goal and inputs;
- exact allowlist and relevant interfaces;
- focused commands;
- inherited permission restrictions;
- output/report path;
- stop conditions.

Exclude the whole plan, conversation, unrelated task reports, branch-wide diff, and raw logs. The controller can link to a concise confirmed design section when the exact contract is needed.

## Dependency and overlap check

Before finalizing:

- build a file-to-task map;
- identify tasks that write the same path;
- sequence those tasks or redesign their seam;
- forbid parallel writers in the same checkout;
- mark read-only tasks that can safely run in parallel;
- ensure later tasks consume stable outputs rather than transient implementation details.

## Stop conditions

Include task-local triggers:

- `NEEDS_CONTEXT` for one uninspectable fact;
- `BLOCKED` for missing dependency or authority;
- `SPLIT_REQUIRED` for a newly discovered independent result;
- `CONTEXT_TOO_BROAD` for a non-local brief or review package;
- `RECORD_FOR_FUTURE_TASK` for an adjacent issue;
- `STOP_AND_RESCOPE` after the single fixer wave or when task cohesion fails;
- `HANDOFF_REQUIRED` for an unauthorized external boundary.

Do not use “ask if unsure” as a substitute for concrete stop conditions.

## Final plan audit

Confirm:

- the design remains unchanged;
- all requirements and negative cases have evidence;
- tasks are cohesive and ordered;
- no path, symbol, or command is fabricated;
- permission and remote boundaries are explicit;
- agent and test budgets are bounded;
- no parallel writer conflict exists;
- every task has a report destination and exact next action;
- the final phase has one truthful completion gate.
