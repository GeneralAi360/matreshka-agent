---
name: finishing-development-work
description: Safely finish verified development work by preserving state, selecting and executing only authorized Git or handoff actions, and producing an exact continuation record. Use after review and fresh verification when the user wants to keep local work, create a commit, prepare or open a pull request, push to an approved target, merge through an approved workflow, or hand work to another operator. Never infer push, deploy, merge, cleanup, or destructive permission from “finish” or “ship it.”
---

# Finish verified work safely

## Confirm readiness and authority

1. Read the current request, applicable repository instructions, ledger, permission envelope, task or phase plan, review decision, fresh verification report, and current repository state.
2. Require an exact project root and target change unit. Detect nested repositories, submodules, symlinks, and host-managed worktrees before any Git action.
3. Confirm that required acceptance criteria are verified and no unresolved Critical or Important finding remains.
4. Reconcile the current state with the verified state. Re-verify affected claims when files changed after verification.
5. Separate task-owned files, pre-existing dirty files, and generated artifacts.

Do not launch child agents. Do not treat “finish,” “ship it,” an old plan, a branch name, or a commit message as permission for remote or destructive actions. Effective authority remains the intersection of current user consent, repository instructions, organization policy, sandbox controls, and the platform's native approvals.

## Select the finish path

Read [the finish decision guide](references/finish-decisions.md). Choose the most complete path already allowed by the permission envelope:

- preserve and hand off the uncommitted state;
- create an allowlisted local commit;
- push an exact branch to an exact repository;
- open or update a pull request with an exact base and head;
- invoke an explicitly approved merge or deployment workflow;
- prepare a remote-system handoff without executing the remote action.

When autonomous authority already covers the exact action, proceed without asking again. Pause for approval only when the action, repository, branch destination, remote environment, destructive scope, secret access, or permission expiry falls outside the envelope.

If the user has not chosen among materially different safe outcomes, present concise options and recommend one. Always keep handoff-only available.

## Preserve state before Git actions

Record status, baseline/current refs, task-owned paths, untracked task files, existing staged files, and user-owned dirty files.

For an authorized commit:

1. Stage only explicit task-owned paths. Never use broad staging that can capture unrelated work.
2. Inspect the staged file list and staged diff.
3. Exclude secrets, local environment files, raw logs, and unrelated generated output.
4. Create a commit only when the staged set matches the verified change unit.
5. Record the resulting commit identity and remaining working-tree state.

Do not amend, rebase, force-push, rewrite history, discard files, reset, clean, or delete a branch/worktree unless that exact operation is separately authorized and safe. This skill does not need destructive cleanup to finish successfully.

## Execute remote actions narrowly

Before an authorized push, pull request, merge, deploy, migration, or provider action, confirm:

- exact repository and remote;
- exact source and destination branch or environment;
- current verified commit/state;
- authentication method without exposing secret values;
- required status checks and rollback/stop policy;
- whether the native platform will request an additional approval.

Perform only the named action. Do not broaden a staging deployment into production, a push into a merge, or a prepared migration into remote SQL execution.

If a different operator owns the remote boundary, return `HANDOFF_REQUIRED` and prepare exact safe steps without claiming the remote result.

## Clean up only owned disposable state

Clean up only a branch, worktree, temporary artifact, or local state created by this run, after its work is preserved and cleanup is explicitly permitted. Never remove host-managed worktrees or user-created branches. Leave uncertain ownership untouched and document it.

## Produce the final handoff

Use [the finish and handoff template](assets/finish-handoff-template.md). Record:

- final status and verified state;
- completed and uncompleted scope;
- files and commit identity, or exact uncommitted baseline/current hashes;
- review and verification evidence summary;
- Git and remote actions actually performed;
- preserved dirty or generated files;
- unresolved Minor and adjacent findings;
- required permissions or external operator steps;
- exact next action and rollback/stop notes.

Use `FINISHED_LOCAL`, `FINISHED_COMMITTED`, `FINISHED_REMOTE`, `HANDOFF_REQUIRED`, `PARTIALLY_VERIFIED`, or `BLOCKED` accurately. Never report push, merge, deploy, migration, or cleanup success without direct evidence from the exact target.
