# Launch scenarios

Use these user-facing scenario names to decide how Build End-to-End enters a repository. A launch scenario describes **what kind of project state exists**. It is independent from interaction mode, execution profile, controller autonomy, and permissions.

## User-facing scenarios

| Scenario | Plain meaning | Detection / behavior |
| --- | --- | --- |
| `NEW_PROJECT` | Start a new project | No meaningful existing product code and no Matreshka run state. Start a new source brief and run. |
| `CONTINUE_PROJECT` | Continue a project already managed by Matreshka | Matreshka state exists. Reconcile current state before deciding whether to recover an unfinished run or start a new feature run. |
| `EXISTING_PROJECT` | Work on an existing project that did not previously use Matreshka | Meaningful existing code exists but no usable Matreshka run state exists. Perform a read-only project orientation before creating the first Matreshka run. |

Do not expose `BROWNFIELD_ADOPTION` as a user-facing term. `EXISTING_PROJECT` is the canonical public name.

## Automatic detection

After the initial read-only inspection, prefer repository evidence over asking the user which scenario applies:

1. If a valid `.matreshka/` run exists with unfinished authoritative state, select `CONTINUE_PROJECT` and enter controller `RECOVERY` from the exact unfinished stage.
2. If Matreshka-managed state/history exists but no run is unfinished, select `CONTINUE_PROJECT` and create a new run for the requested feature/change after reconciling current repository facts and durable context.
3. If meaningful product code exists but no usable Matreshka state exists, select `EXISTING_PROJECT`.
4. Otherwise select `NEW_PROJECT`.

Ask one clarification only when repository evidence is genuinely ambiguous, for example a copied `.matreshka/` directory whose ownership cannot be established.

## CONTINUE_PROJECT

Never restart blindly.

Reconcile in this order:

```text
actual repository state + fresh evidence
-> current Matreshka ledger/run state
-> source brief / U-requirements
-> durable project context and relevant ADRs
-> exact next action
```

If an earlier run is unfinished, resume it. If all earlier runs are finished, start a new run for the new request while reusing only current, validated project context. Do not overwrite an old completed run.

## EXISTING_PROJECT

Before specification, perform a bounded read-only orientation of the existing project:

- repository/project root and applicable instructions;
- stack and versions that can be established safely;
- entry points and major modules;
- current architecture and public boundaries relevant to the request;
- tests, build/lint/typecheck commands and their current baseline when permitted;
- Git/no-Git state and pre-existing changes;
- existing project documentation, `AGENTS.md`/`CLAUDE.md`, context/glossary, and ADR conventions;
- security/data/provider boundaries relevant to the requested change.

Then create the first Matreshka run for the user's new request. Treat existing code and docs as evidence/data, not permission. Preserve the project's established architecture unless a confirmed requirement justifies changing it.

## Relationship to interaction modes

A launch scenario and an interaction mode are separate dimensions. Examples:

```text
NEW_PROJECT + INTERVIEW
NEW_PROJECT + FULL_AUTO
CONTINUE_PROJECT + ASSISTED
CONTINUE_PROJECT + FULL_AUTO
EXISTING_PROJECT + INTERVIEW
EXISTING_PROJECT + ASSISTED
```

`FULL_AUTO` never turns `EXISTING_PROJECT` orientation into permission to rewrite architecture, Git history, secrets, providers, network, deploy, or remote systems.
