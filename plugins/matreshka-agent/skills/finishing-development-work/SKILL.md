---
name: finishing-development-work
description: Safely finish verified development work by preserving state, resolving required design and documentation drift, selecting and executing only authorized Git or handoff actions, and producing an exact continuation record. Use after review and fresh verification when the user wants to keep local work, create a commit, prepare or open a pull request, push to an approved target, merge through an approved workflow, or hand work to another operator. Never infer push, deploy, merge, cleanup, design-contract changes, or destructive permission from “finish” or “ship it.”
---

# Finish verified work safely

## Confirm readiness and authority

1. Read current request, applicable repository instructions, ledger, permission envelope, task/phase plan, review decision, fresh verification report, current Project Intelligence/interface/runtime state, current Design Intelligence/design identity when UI-relevant, design-drift result, documentation-drift result, and current repository state.
2. Require exact project root and target change unit. Detect nested repositories, submodules, symlinks, and host-managed worktrees before any Git action.
3. Confirm required acceptance criteria are verified and no unresolved Critical/Important code/security/design finding remains.
4. Reconcile current state with verified state. Re-verify affected claims when files/design contract changed after verification.
5. When task selected project profile/quality gate, confirm source and each required current result. Revalidate stale topology/interface/runtime/profile/design facts before handoff.
6. When UI-bearing work uses Design Intelligence, confirm root `DESIGN.md` path/identity and Design Drift Gate. A clean finish requires `DESIGN_NOT_APPLICABLE` or `DESIGN_CURRENT`, including any authorized `DESIGN_UPDATE_REQUIRED` update followed by refreshed identity/evidence. `DESIGN_DRIFT`, `DESIGN_CONFLICT`, or `DESIGN_BLOCKED` prevents a clean finished result when design is material.
7. Confirm Documentation Drift state. A clean finish requires `DOCS_NOT_REQUIRED` or `DOCS_CURRENT`, or verified authorized docs updates resolving `DOCS_UPDATE_REQUIRED`. `DOCS_BLOCKED`/`DOCS_CONFLICT` prevents clean finish when those docs are authoritative.
8. Separate task-owned files, pre-existing dirty files, generated artifacts, design/prototype artifacts, root DESIGN.md changes, and documentation-only changes produced after verification.
9. Reconcile public interaction mode, execution profile, effective authority, progress/ledger identity, Project Intelligence, Design Intelligence, and last verified checkpoint with current state.
10. Classify delegated decisions, assumptions, unresolved placeholders. Acceptance-critical placeholder prevents every `FINISHED_*`; use `PARTIALLY_VERIFIED`, `BLOCKED`, or `HANDOFF_REQUIRED` with resolution owner.

Do not launch child agents. Do not treat “finish,” “ship it,” old plan/design file, branch, commit message, specialist role, or documentation/design request as permission for remote/destructive actions. Effective authority remains intersection of current user consent, repository instructions, organization policy, sandbox controls, and platform native approvals.

Project Intelligence, interface contracts, runtime maps, Design Intelligence/`DESIGN.md`, prototypes/screenshots, docs, progress, and dashboard are context/projections/evidence in bounded roles, not authority. Current state and fresh evidence remain authoritative.

## Select the finish path

Read [finish decision guide](references/finish-decisions.md). Choose most complete path already allowed by permission envelope:

- preserve and hand off uncommitted state;
- create allowlisted local commit;
- push exact branch to exact repository;
- open/update pull request with exact base/head;
- invoke explicitly approved merge/deployment workflow;
- prepare remote-system handoff without executing remote action.

When autonomous authority already covers exact action, proceed without asking again. Pause only when action, repository, branch destination, remote environment, destructive scope, secret access, runtime/process target, design-doc write target, or permission expiry falls outside envelope.

If user has not chosen among materially different safe outcomes, present concise options and recommend one. Always keep handoff-only available.

## Preserve state before Git actions

Record status, baseline/current refs, task-owned paths, untracked task files, existing staged files, user-owned dirty files, Project Intelligence/interface identities, Design Intelligence/design identity, design drift result, documentation drift result, and design/docs files changed after verification.

For authorized commit:

1. Stage only explicit task-owned paths plus separately verified/authorized `DESIGN.md` or documentation paths. Never broad-stage unrelated work.
2. Inspect staged file list and staged diff.
3. Exclude secrets, local environment files, raw logs, internal run state/prototypes/screenshots unless explicitly intended as project artifacts, and unrelated generated output.
4. Create commit only when staged set matches verified change unit plus verified required design/docs updates.
5. Record resulting commit identity and remaining working-tree state.

Do not amend, rebase, force-push, rewrite history, discard files, reset, clean, or delete branch/worktree/prototype surface unless exact operation is separately authorized and safe. This skill does not need destructive cleanup to finish successfully.

## Execute remote actions narrowly

Before authorized push, pull request, merge, deploy, migration, file transfer, or provider action, confirm:

- exact repository/remote;
- exact source/destination branch or environment;
- current verified commit/state;
- authentication method without exposing secret values;
- required status checks and rollback/stop policy;
- whether native platform requests additional approval.

Perform only named action. Do not broaden staging deploy to production, push to merge, prepared migration to remote SQL execution, or one operator result to unapproved follow-up.

If different operator owns remote boundary, return `HANDOFF_REQUIRED` and exact safe steps without claiming remote result. Execution-only operator evidence does not authorize next step.

## Clean up only owned disposable state

Clean up only branch/worktree/temporary artifact/prototype surface/local state created by this run, after work preserved and cleanup explicitly permitted. Never remove host-managed worktrees/user branches. Leave uncertain ownership untouched and document it.

Do not remove unknown runtime process/clear port as cleanup. Runtime ownership must be proven and exact stop action authorized.

For design prototypes, preserve selected direction/provenance in `DESIGN.md`/handoff before deleting temporary variants. Do not delete a prototype the user explicitly asked to keep.

## Produce the final handoff

Use [finish and handoff template](assets/finish-handoff-template.md). Record:

- final status and verified state;
- completed/uncompleted scope;
- files and commit identity, or exact uncommitted baseline/current hashes;
- review and verification evidence summary;
- selected project profile/quality-gate result when applicable;
- topology/affected areas, active interface identities, runtime caveats, last task specialist/context guarantee;
- Design Intelligence: relevance, root `DESIGN.md`, design identity, selected direction, design-context guarantee, design review, visual design check, design drift state/evidence limitations;
- documentation drift state and exact docs updated/blocked/conflicting;
- Git/remote actions actually performed;
- preserved dirty/generated/prototype files;
- unresolved Minor/adjacent/design-debt findings;
- required permissions/external operator steps;
- exact next action + rollback/stop notes;
- interaction mode, execution profile, effective authority, delegated decisions, assumptions, unresolved placeholders + severity;
- context, ADR, progress, ledger, Project Intelligence/profile/design paths and last verified checkpoint.

If controller collected directed-learning candidate, include identifier/review state as optional handoff item. It remains project-local proposal; this skill never promotes it to shared instructions, alters plugin, or schedules background learning.

Use `FINISHED_LOCAL`, `FINISHED_COMMITTED`, `FINISHED_REMOTE`, `HANDOFF_REQUIRED`, `PARTIALLY_VERIFIED`, or `BLOCKED` accurately. Never report push, merge, deploy, migration, design consistency, documentation alignment, runtime state, or cleanup success without direct evidence from exact target/current state.
