# Optional worktree isolation

Use a worktree only to isolate a clearly bounded task from unrelated local state. It is not a reason to create parallel writers, bypass repository policy, or clean user-owned files.

## Entry gate

Before creating a worktree, require all of the following:

1. Git is available and the real project root is confirmed.
2. The permission envelope explicitly authorizes creating a Git workspace for this task.
3. The current branch, baseline, target paths, and task ownership are recorded.
4. The target does not overlap a nested repository, submodule, symlink escape, or host-managed worktree.
5. The controller can name a run-owned location and a single exact task that will use it.

If any condition is missing, continue in the approved checkout only when ownership is clear; otherwise return `HANDOFF_REQUIRED`. Do not improvise a branch name or remove a conflicting workspace.

## Operating rules

- The controller creates, records, and owns the run worktree; subagents never create or remove it.
- Permit only one writer in a worktree at a time. Matreshka's default remains sequential implementation even when multiple worktrees exist.
- Give every task brief the real worktree path, baseline identity, exact allowlist, and report path.
- Preserve pre-existing changes in the original checkout. Do not copy or absorb them into the worktree without a separate decision.
- Record creation evidence, branch/ref, path, ownership, task ID, and cleanup authority in the ledger.
- Treat a worktree as disposable only after work is preserved, verification is complete, and cleanup of that exact run-owned path is explicitly permitted.

Never remove a user-created or host-managed worktree. When cleanup authority is absent or ownership is uncertain, preserve it and hand off the exact path.
