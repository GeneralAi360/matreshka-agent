# Finish and handoff — <task, phase, or branch>

## Final status

- Result: `<FINISHED_LOCAL | FINISHED_COMMITTED | FINISHED_REMOTE | HANDOFF_REQUIRED | PARTIALLY_VERIFIED | BLOCKED>`
- Project root: `<resolved root or NO_GIT_MODE>`
- Baseline/current state: `<refs, commit, or hashes>`
- Verified state matches current: `<yes/no and evidence>`
- Permission envelope used: `<scope and expiry>`
- Interaction mode: `<ASSISTED | AUTONOMOUS_LOCAL | NOT_APPLICABLE>`
- Execution profile: `<selected profile and source>`
- Effective authority: `<exact local / Git / remote / secret / destructive capabilities>`
- Last verified checkpoint: `<report path, state identity, and time if available>`
- Progress / ledger identity: `<paths and matching state identifiers>`

## Delivered scope

- Completed: `<acceptance results>`
- Not completed: `<remaining results>`
- Task-owned files: `<exact paths>`
- Pre-existing dirty files preserved: `<paths or none>`
- Generated/unknown files left untouched: `<paths or none>`
- Context / ADR / progress paths: `<exact paths or not created>`
- Delegated decisions: `<decision, rationale, reversibility, or none>`
- Assumptions made: `<assumption, source/status, or none>`
- Unresolved placeholders: `<item, acceptance impact/severity, resolution owner, or none>`
- Residual risks: `<risk, evidence, owner, or none>`

## Quality evidence

- Review decision: `<decision and blocking findings>`
- Verification verdict: `<verdict>`
- Key fresh commands: `<command / exit / counts / note>`
- Unverified criteria: `<list or none>`

## Actions performed

| Action | Exact target | Evidence |
| --- | --- | --- |
| `<stage/commit/push/PR/merge/deploy/none>` | `<paths/repository/branch/environment>` | `<result/ref/URL/status>` |

## External handoff, if required

- Local operator: `<operator>`
- Remote operator: `<operator>`
- Remote system: `<system and exact environment>`
- Allowed preparation: `<artifacts and commands prepared>`
- Forbidden execution: `<actions not performed>`
- Verification steps: `<exact steps and expected result>`
- Rollback or stop policy: `<policy>`

## Continuation

- Minor findings: `<list or none>`
- Adjacent future tasks: `<list or none>`
- Assumptions and concerns: `<list or none>`
- Pre-existing failures: `<list or none>`
- Permissions still required: `<list or none>`
- Cleanup performed: `<owned targets and evidence, or none>`
- Exact next action: `<single next step or none>`
