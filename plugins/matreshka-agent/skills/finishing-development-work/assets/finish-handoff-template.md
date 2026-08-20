# Finish and handoff — <task, phase, or branch>

## Final status

- Result: `<FINISHED_LOCAL | FINISHED_COMMITTED | FINISHED_REMOTE | HANDOFF_REQUIRED | PARTIALLY_VERIFIED | BLOCKED>`
- Project root: `<resolved root or NO_GIT_MODE>`
- Baseline/current state: `<refs, commit, or hashes>`
- Verified state matches current: `<yes/no and evidence>`
- Permission envelope used: `<scope and expiry>`
- Public interaction mode: `<INTERVIEW | ASSISTED | FULL_AUTO | NOT_APPLICABLE>`
- Execution profile: `<selected profile and source>`
- Effective authority: `<exact local / Git / remote / secret / destructive capabilities>`
- Last verified checkpoint: `<report path, state identity, and time if available>`
- Progress / ledger identity: `<paths and matching state identifiers>`

## Project Intelligence

- Topology state / affected areas: `<CURRENT/PARTIAL/STALE + AREA IDs>`
- Active interface contracts: `<IC IDs + hashes/status, or none>`
- Runtime map / caveats: `<service ownership/status/log facts or not applicable>`
- Documentation drift state: `<DOCS_NOT_REQUIRED | DOCS_CURRENT | DOCS_UPDATE_REQUIRED | DOCS_BLOCKED | DOCS_CONFLICT>`
- Documentation updated: `<exact paths or none>`
- Last task specialist/context: `<role archetype + primary area + NARROW/DEGRADED>`

A clean finished result requires the documentation drift state required by the controller to be resolved. Project Intelligence is context/state, not permission or verification evidence by itself.

## Delivered scope

- Completed: `<acceptance results>`
- Not completed: `<remaining results>`
- Task-owned files: `<exact paths>`
- Pre-existing dirty files preserved: `<paths or none>`
- Generated/unknown files left untouched: `<paths or none>`
- Context / ADR / progress paths: `<exact paths or not created>`
- Project profile / Project Intelligence paths: `<exact paths or inline/not created>`
- Delegated decisions: `<decision, rationale, reversibility, or none>`
- Assumptions made: `<assumption, source/status, or none>`
- Unresolved placeholders: `<item, acceptance impact/severity, resolution owner, or none>`
- Residual risks: `<risk, evidence, owner, or none>`

## Quality evidence

- Review decision: `<decision and blocking findings>`
- Verification verdict: `<verdict>`
- Cross-area integration/interface proof: `<evidence or not applicable>`
- Key fresh commands/interactions: `<command / exit / counts / note>`
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
