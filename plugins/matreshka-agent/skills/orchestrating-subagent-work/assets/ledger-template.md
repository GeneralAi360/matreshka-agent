# Matreshka Run Ledger

## Identity

- Contract version: `{{CONTRACT_VERSION}}`
- Plugin version: `{{PLUGIN_VERSION}}`
- Run ID: `{{RUN_ID}}`
- Updated at: `{{TIMESTAMP}}`
- Project real root: `{{PROJECT_ROOT}}`

## Baseline

- Mode: `{{GIT_OR_NO_GIT_MODE}}`
- Branch/HEAD or timestamp: `{{BASELINE_ID}}`
- Pre-existing dirty files: {{DIRTY_FILES_OR_NONE}}
- Baseline hashes/snapshot: `{{BASELINE_RECORD}}`
- Change ownership notes: {{OWNERSHIP}}

## Capabilities

| Capability | Available | Guarantee/evidence |
| --- | --- | --- |
| Subagents | {{YES_NO}} | {{DETAIL}} |
| Fresh context | {{YES_NO}} | {{DETAIL}} |
| Same-thread resume | {{YES_NO}} | {{DETAIL}} |
| Technical read-only | {{YES_NO}} | {{DETAIL}} |
| Safe isolation/worktree | {{YES_NO}} | {{DETAIL}} |
| Role capability routing | {{YES_NO}} | {{DETAIL}} |
| Turn/usage status | {{YES_NO}} | {{DETAIL}} |

- Mode status: `{{FULL_DEGRADED_INLINE_HANDOFF}}`
- Missing guarantees: {{GAPS_OR_NONE}}

## Decision

- Goal: {{GOAL}}
- Risk summary: {{RISK}}
- Execution profile: `{{SPEED_BALANCED_QUALITY}}`
- Autonomy mode: `{{MANAGED_LOCAL_EXTENDED}}`
- Current stage gate: `{{GATE}}`
- Decision rationale/approval: {{DECISION_RECORD}}

## Permission envelope

- Allowed scope: {{ALLOWED_SCOPE}}
- Inspect-only scope: {{INSPECT_ONLY}}
- Forbidden scope: {{FORBIDDEN_SCOPE}}
- Decision delegation: {{DECISIONS}}
- Local writes/commands: {{LOCAL_AUTHORITY}}
- Capability tiers and highest-cost opt-in: {{ROLE_TIERS_TURN_LIMITS}}
- Git workspace/history/remote: {{GIT_AUTHORITY}}
- Dependencies/network: {{NETWORK_AUTHORITY}}
- Remote systems/critical production: {{REMOTE_AUTHORITY}}
- Secret references: {{NAMED_REFERENCE_OR_NONE}}
- Expiry: {{EXPIRY}}
- Approval source/time: {{APPROVAL_RECORD}}

## Task map and phase budget

| Task | Dependency | Status | Agent turns used/max | High-judgment turns |
| --- | --- | --- | --- | --- |
| {{TASK_ID}} | {{DEPENDENCY}} | {{STATUS}} | {{USED_MAX}} | {{USED}} |

- Current task: `{{TASK_ID}}`
- Total agent turns used/max: `{{USED_MAX}}`
- Broad checks used/max: `{{USED_MAX}}`
- Audit threshold: {{THRESHOLD}}

## Dispatches

| Turn | Task | Role | Stable thread ID | Tier | Brief/report | Status |
| --- | --- | --- | --- | --- | --- | --- |
| {{N}} | {{TASK}} | {{ROLE}} | `{{THREAD_ID}}` | {{TIER}} | {{PATHS}} | {{STATUS}} |

## Review

- Confirmed findings: {{FINDINGS_OR_NONE}}
- Rejected/adjacent findings: {{ADJUDICATION}}
- Fixer wave used: {{YES_NO}}
- Targeted re-review result: {{RESULT_OR_PENDING}}

## Verification

| Command | Exit | Counts | Relevant note | Baseline/current |
| --- | --- | --- | --- | --- |
| `{{COMMAND}}` | {{EXIT}} | {{COUNTS}} | {{NOTE}} | {{STATE}} |

- Pre-existing failures: {{FAILURES_OR_NONE}}
- Verification status: `{{STATUS}}`

## Recovery and next action

- Last safe checkpoint: {{CHECKPOINT}}
- Active turns: {{ACTIVE_OR_NONE}}
- Stop reason: {{REASON_OR_NONE}}
- Exact next action: {{ONE_ACTION}}
