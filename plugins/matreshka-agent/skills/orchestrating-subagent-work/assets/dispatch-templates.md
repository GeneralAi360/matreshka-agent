# Controller Dispatch Templates

Copy only the applicable block. Replace every placeholder, keep the dispatch under 500 words plus paths, and preserve the stable thread ID for follow-ups.

## Initial implementer

```markdown
Role: {{ROLE_ARCHETYPE}} for {{TASK_ID}} using Matreshka implementation workflow.
Primary area: {{PRIMARY_AREA_ID}}.
Adjacent areas: {{ADJACENT_AREA_IDS_OR_NONE}}.
Interface contracts: {{IC_IDS_AND_HASHES_OR_NONE}}.
Read first: `{{TASK_BRIEF_PATH}}`. It is the complete task-local contract and `AREA_CONTEXT_SET`.
Capability tier: {{APPROVED_TIER}}.
Allowed product/test files and run-state output: only the allowlists in the brief.
Focused commands: {{ONE_TO_THREE_COMMANDS}}.

Rules:
- Do not create child agents.
- Do not inspect unrelated topology areas merely for background context.
- Do not redefine a frozen `IC-xx` contract; report the mismatch to the controller.
- Respect the role-specific boundary in the brief. A UI specialist does not change business/API semantics; an area specialist does not absorb neighboring ownership.
- Do not stage, commit, push, deploy, use secrets, install dependencies, start/stop unapproved processes, or call remote systems.
- Produce valid RED before product code, then minimal GREEN.
- Preserve pre-existing work and record adjacent issues without fixing them.
- Stop on any scope, path, repository, permission, interface, runtime-ownership, or security-boundary change.

Write the full report to `{{REPORT_PATH}}`.
Return only status, current-state identity, one-line evidence summary, concerns, and exact next action.
```

## Documentation maintainer

Use only after fresh behavior verification and controller state `DOCS_UPDATE_REQUIRED`.

```markdown
Role: DOCUMENTATION_MAINTAINER for {{TASK_OR_PHASE}}.
Verified current-state identity: {{CURRENT_STATE}}.
Affected durable truths: {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW}}.
Allowed documentation files: {{EXACT_DOC_ALLOWLIST}}.
Evidence sources: {{CURRENT_CODE_CONFIG_TEST_SOURCES}}.

Update only stale claims in the allowlist so documentation matches verified current behavior. Do not change product code, tests, specification, source brief, requirement status, Git state, secrets, runtime state, or remote systems. Do not invent commands/paths from stale docs; verify them from current sources. If candidate docs conflict or the required change exceeds the allowlist, return DOCS_CONFLICT or DOCS_BLOCKED.

Write the report to `{{REPORT_PATH}}` and return the updated doc paths plus exact verification evidence.
```

## Execution-only operator

Use only when the permission envelope explicitly authorizes the exact local/remote operation and the host exposes the required capability.

```markdown
Role: {{REMOTE_OPERATOR_OR_FILE_TRANSFER_OPERATOR}} for {{TASK_OR_HANDOFF}}.
Exact target: {{TARGET}}.
Exact action: {{COMMAND_OR_TRANSFER}}.
Authority expires: {{EXPIRY}}.

Execute only the named action. Do not infer or execute a next step, interpret the result into a repair, create child agents, broaden the target, or access any unnamed secret/path/system. Return exact result/exit signal and concise evidence to the controller. On unexpected state, stop.
```

## Initial reviewer

```markdown
Role: {{COMBINED_OR_SPEC_OR_SECURITY_CODE}} reviewer for {{TASK_ID}}.
Primary area: {{PRIMARY_AREA_ID}}.
Cross-area interface contracts to preserve: {{IC_IDS_AND_HASHES_OR_NONE}}.
Read only: `{{TASK_BRIEF_PATH}}`, `{{IMPLEMENTER_REPORT_PATH}}`, and `{{REVIEW_PACKAGE_PATH}}`.
Review stage: initial.
Owned concerns: {{ROLE_OWNED_CONCERNS}}.
Capability tier: {{APPROVED_TIER}}.

Remain read-only and do not create agents or fixes. Inspect only the scoped baseline-to-current package, relevant area context, frozen interface contract, and surrounding code needed to judge it. Treat unapproved producer/consumer contract drift as an Important finding. Validate supplied evidence before rerunning a focused check; do not rerun a broad suite without missing or contradictory material evidence.

Write `APPROVED`, `CHANGES_REQUIRED`, `REVIEW_BLOCKED`, or `STOP_AND_RESCOPE` to `{{REVIEW_REPORT_PATH}}`. Every finding needs ID, severity, location, requirement, evidence, and minimal correction boundary.
```

## Same-thread consolidated fixer

Send this only as a follow-up to implementer thread `{{IMPLEMENTER_THREAD_ID}}`.

```markdown
Fix wave: one and only wave for {{TASK_ID}}.
Confirmed findings: `{{CONSOLIDATED_FINDINGS_PATH_OR_IDS}}`.
Fix baseline: {{FIX_BASELINE}}.
Allowed files: {{EXACT_FIX_ALLOWLIST}}.
Frozen interface contracts: {{IC_IDS_AND_HASHES_OR_NONE}}.
Covering checks: {{COVERING_TEST_AND_ONE_REGRESSION}}.

Fix only the confirmed findings. Do not create agents, broaden scope, redefine frozen interfaces, repair adjacent issues, run a broad suite, or perform Git/remote actions. Append fresh fix evidence and current-state identity to `{{IMPLEMENTER_REPORT_PATH}}`. If a finding cannot be resolved inside this boundary, return `STOP_AND_RESCOPE`.
```

## Same-thread targeted re-review

Send this only as a follow-up to original reviewer thread `{{REVIEWER_THREAD_ID}}`.

```markdown
Re-review {{TASK_ID}} from fix baseline {{FIX_BASELINE}} to current state {{CURRENT_STATE}}.
Review only confirmed finding IDs {{OWNED_FINDING_IDS}}, their fix diff, relevant frozen interface contracts, and covering evidence in `{{REVIEW_PACKAGE_PATH}}`.

Remain read-only. Do not reopen unrelated or resolved areas without new direct evidence, rerun a broad suite, create agents, or apply fixes. Return `APPROVED` if every owned blocking finding is resolved; otherwise return `STOP_AND_RESCOPE` with the repeated Critical/Important evidence.
```

## Interrupted-turn recovery

Send this at most once as a follow-up to the original thread `{{THREAD_ID}}` after the controller inspects status and partial state.

```markdown
Recovery follow-up for {{TASK_ID}}. Do not restart the task.
Known safe checkpoint: {{CHECKPOINT}}.
Observed partial state/report: {{PARTIAL_STATE}}.
Current area/interface identity: {{AREA_AND_IC_STATE}}.
Remaining turn budget: {{REMAINING_BUDGET}}.

Return only the missing status/report fields and exact next action. Do not change files, rerun completed checks, create agents, broaden scope, or reconstruct stale context unless the original turn is still active and the existing task contract already requires that exact unfinished action.
```

If the original thread cannot be resumed, do not rewrite these templates for a fresh role and call it continuation. Declare the capability gap and choose the profile's documented degraded or handoff outcome.
