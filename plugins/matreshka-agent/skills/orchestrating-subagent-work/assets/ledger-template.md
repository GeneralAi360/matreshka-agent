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

## Skill source map

| Needed role | Matreshka skill | Host-visible invocation | Source evidence | Result |
| --- | --- | --- | --- | --- |
| {{ROLE}} | `{{SKILL}}` | {{INVOCATION}} | {{SOURCE}} | {{SELECTED_FALLBACK_HANDOFF}} |

## Decision

- Goal: {{GOAL}}
- Risk summary: {{RISK}}
- Interaction mode: `{{GUIDED_ASSISTED_AUTONOMOUS_LOCAL_NOT_APPLICABLE}}`
- Pending interaction mode: `{{MODE_AT_NEXT_SAFE_TRANSITION_OR_NONE}}`
- Execution profile: `{{SPEED_BALANCED_QUALITY}}`
- Autonomy mode: `{{MANAGED_LOCAL_EXTENDED}}`
- Effective permissions: {{EFFECTIVE_PERMISSION_SUMMARY}}
- Current stage gate: `{{GATE}}`
- Decision-map state: `{{NOT_REQUIRED_REQUIRED_READY_OR_BLOCKED}}`
- Delegated decisions: {{DELEGATED_DECISIONS_OR_NONE}}
- Assumption count: {{ASSUMPTION_COUNT}}
- Unresolved placeholder count: {{PLACEHOLDER_COUNT}}
- Decision rationale/approval: {{DECISION_RECORD}}

## Durable project artifacts

- Context path: `{{CONTEXT_PATH_OR_NONE}}`
- Context source and review state: {{CONTEXT_SOURCE_REVIEW_OR_NONE}}
- ADR IDs: {{ADR_IDS_OR_NONE}}
- Progress path: `{{PROGRESS_PATH_OR_INLINE}}`
- Progress projection status: `{{CURRENT_STALE_MISSING_UNAUTHORIZED}}`
- Last progress update event: {{EVENT_TIME_OR_NONE}}
- Recorded source conflicts: {{CONFLICTS_OR_NONE}}

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
- Project profile/quality gate authority: {{PROFILE_GATE_AUTHORITY}}
- Directed learning mode/candidate authority: {{LEARNING_AUTHORITY}}
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
- Quality-gate rows: {{PASS_FAIL_NOT_RUN_BLOCKED_SUMMARY}}

## Workspace and learning

- Run worktree: {{PATH_BRANCH_TASK_OWNERSHIP_OR_NONE}}
- Worktree cleanup authority: {{AUTHORITY_OR_NONE}}
- Learning mode: `{{OFF_PROPOSE_LOCAL_REVIEWED}}`
- Candidate IDs and evidence: {{CANDIDATES_OR_NONE}}
- Promotion/revalidation status: {{STATUS_OR_NONE}}

## Recovery and next action

- Loaded contract/plugin version: `{{LOADED_CONTRACT_AND_PLUGIN_VERSION}}`
- Version difference and in-memory compatibility: {{VERSION_DIFFERENCE_OR_NONE}}
- Progress/ledger/actual-state mismatch: {{MISMATCH_OR_NONE}}
- Last safe checkpoint: {{CHECKPOINT}}
- Active turns: {{ACTIVE_OR_NONE}}
- Stop reason: {{REASON_OR_NONE}}
- Exact next action: {{ONE_ACTION}}
