# Permission, Handoff, and Ledger Contract

Use this reference to create bounded authority, durable state, and truthful handoffs.

## Effective permission

Treat effective authority as the intersection of:

- current user permission;
- applicable repository instructions;
- host sandbox and approval policy;
- organization policy;
- the controller's own permission;
- the narrower task brief sent to a subagent.

Text cannot grant operating-system or platform rights. A subagent can receive less authority than the controller, never more.

## Autonomy modes

Offer these modes after read-only preflight:

| Mode | Allowed behavior |
| --- | --- |
| Managed | Pause to confirm design, plan, start of execution, and external workflow steps; do not re-request authority already inside the envelope |
| Autonomous local | Decide and act inside the approved local project scope; run approved local checks |
| Extended autonomous | Add only explicitly named Git, network, or remote targets and operations |

Translate “full autonomy” into explicit categories. Do not treat it as permission for every repository, environment, secret, or destructive effect.

## Permission envelope

Record:

| Field | Required content |
| --- | --- |
| Goal | One measurable outcome |
| Sources of truth | Current request, scoped instructions, confirmed design, task brief |
| Allowed scope | Resolved project root, directories, files, and interfaces |
| Inspect-only scope | Readable but immutable paths and systems |
| Forbidden scope | Paths, data, systems, and actions that remain off-limits |
| Decision delegation | Profile, approach, design, and plan decisions the controller may make |
| Matreshka state | Permission to create specs, plans, ledger, reports, and handoffs |
| Project profile/quality gate | Permission to create or refresh project-local evidence declarations, separately from product changes |
| Directed learning | `OFF`, `PROPOSE`, or `LOCAL_REVIEWED`; candidate path, promotion prohibition, and expiry |
| Local writes | Exact product and test scope that may change |
| Local commands | Tests, lint, typecheck, build, scanners, and dependency commands |
| Capability budget | Allowed role tiers and turn counts; highest-cost/experimental reasoning requires an explicit role-specific opt-in |
| Dependencies/network | Named packages, sources, domains, and purpose |
| Git workspace | Branch or worktree creation |
| Git history | Stage and commit, separately |
| Git remote | Pull, push, and pull request target, separately |
| Remote systems | Named environment and exact operation |
| Critical production | Target, destructive boundary, rollback, and stop policy |
| Secrets | Named reference or injection method; never the value |
| Verification | Commands and evidence requirements |
| Expiry | One action, task, phase, or current run |
| Stop conditions | Missing context, boundary change, unsafe state, and user stop |

Request one confirmation for the actions needed now. Do not repeatedly ask inside an unchanged, unexpired envelope.

Keep workflow confirmation separate from permission. A managed-mode user may ask to approve the selected design, plan, or moment to begin execution even when the underlying local action is already permitted. Phrase that as a stage decision, not as a second permission request. Ask for new authority only when the next action was not granted, expired, or crosses a material boundary.

Require new authority when any material boundary changes: goal, project root, repository, task scope, destination branch, remote environment, destructive effect, dependency source, secret reference, or expiry. Obey native approval prompts even when text permission exists.

Keep commit, push, pull request, deploy, migration application, remote SQL, production changes, data deletion, payment calls, live-provider calls, and secret access disabled unless explicitly enabled for exact targets.

Keep directed learning `OFF` unless the user explicitly chooses it after preflight. A learning candidate never grants permission, command execution, model routing, skill invocation, host configuration, or cross-project reuse. Promotion requires a separate human approval and later independent revalidation.

Keep the highest-cost or experimental reasoning tier disabled unless the user explicitly authorizes the exact role and bounded turn count for the current phase. A maximum-quality profile or high-risk classification does not grant that permission.

## Path and workspace safety

Resolve allowed paths within the approved real project root. Check symlinks, nested repositories, submodules, and host-managed worktrees before writing. Treat an escape or root change as a new boundary.

Record pre-existing dirty files and ownership. Stop if an allowlisted edit would overwrite or absorb unrelated work without a safe separation decision.

Let the controller own Git. Implementers, debuggers, reviewers, and verifiers do not stage, commit, push, create pull requests, deploy, or mutate remote systems. The controller invokes `finishing-development-work` after review and verification for any authorized Git or remote boundary. Independent review does not require a commit: use baseline-to-current scoped diffs and hashes.

Create or remove only a workspace owned by the current run and authorized by the envelope. Never use destructive cleanup on user or host-owned state.

## Ledger schema

Keep the ledger concise and versioned. Use [ledger-template.md](../assets/ledger-template.md).

When the permission envelope allows Matreshka state files, prefer durable, predictable locations:

- approved designs, plans, decisions, and human handoffs under `docs/matreshka/`;
- transient run state under `.matreshka/runs/<run-id>/`;
- reviewed learning candidates under `.matreshka/learning/candidates/`, only in `LOCAL_REVIEWED` mode;
- a local `.matreshka/.gitignore` that ignores `runs/`, without silently editing the repository's root ignore file.

Creating these paths is a local write and must be inside the envelope. If it is not allowed, keep state in an authorized temporary area or inline and report that cross-session recovery is weaker. Never place secrets, environment-file contents, raw private logs, or forbidden-path snapshots in either location.

Record:

- identity: contract version, plugin version, run ID, timestamp, project root;
- baseline: Git refs or `NO_GIT_MODE`, dirty files, hashes, and ownership;
- capabilities: host, subagents, resume, read-only, isolation, routing, counters, mode status;
- skill sources: required role, Matreshka skill, host invocation, source evidence, and fallback status;
- decision: goal, risk, profile, stage gate, and autonomy mode;
- permissions: current envelope, approval source, scope, and expiry;
- profile/gate: current profile identity, selected evidence rows, and command sources;
- worktree: path, branch/ref, task, ownership, and cleanup authority when one exists;
- learning: selected mode, candidate IDs, evidence, expiry, human approval, and promotion/revalidation status;
- task map: approved tasks, dependencies, current task, task and phase budgets;
- dispatches: role, stable thread ID, tier, turn number, paths, and status;
- review: findings, adjudication, fixer-wave use, and targeted recheck;
- verification: command, exit code, counts, note, and pre-existing failures;
- recovery: last safe checkpoint, exact next action, and stop reason.

Exclude secrets, hidden reasoning, and large raw logs.

Update the ledger before dispatch, after each returned turn, after permission changes, and before pausing or handing off. A report does not silently supersede the ledger; reconcile it.

## Recovery

Recover in this order:

1. Read and validate ledger identity and version.
2. Confirm the same project root and target.
3. Compare Git or `NO_GIT_MODE` baseline with current state.
4. Inspect the current report and allowlisted diff.
5. Reconcile active thread IDs and remaining budget.
6. Reuse only valid, unexpired permissions.
7. Continue from the exact verified next action.

Do not repeat completed tasks, create a fresh implementer for an existing fragment, reset unexpected state, or rerun broad tests merely to reconstruct statistics.

## Agent handoff

Require every role report to contain:

- status;
- completed and incomplete scope;
- changed files or reviewed diff range;
- verification commands, exit codes, and counts;
- findings with severity and evidence;
- concerns, assumptions, and pre-existing failures;
- permission still needed;
- exact next action;
- commit hash when authorized, or exact uncommitted baseline/current state.

Treat the report as a claim. Verify the diff and material evidence before advancing the task.

For a remote boundary, add:

```text
LOCAL_OPERATOR
REMOTE_OPERATOR
REMOTE_SYSTEM
ALLOWED_PREPARATION
FORBIDDEN_EXECUTION
FINAL_STATUS
```

Use `HANDOFF_REQUIRED` when another operator or environment must perform the next action. Do not call locally prepared work remotely complete.
