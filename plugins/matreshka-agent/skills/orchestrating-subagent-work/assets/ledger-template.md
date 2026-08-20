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
| Local dashboard display | {{YES_NO}} | {{DETAIL_WITHOUT_IMPLIED_AUTHORITY}} |
| Browser E2E | {{YES_NO_DEGRADED}} | {{FRAMEWORK_COMMAND_MODE_ISOLATION}} |
| Browser screenshots/trace | {{YES_NO_DEGRADED}} | {{DETAIL}} |
| Browser console/network inspection | {{YES_NO_DEGRADED}} | {{DETAIL}} |

- Mode status: `{{FULL_DEGRADED_INLINE_HANDOFF}}`
- Missing guarantees: {{GAPS_OR_NONE}}

## Skill source map

| Needed role | Matreshka skill | Host-visible invocation | Source evidence | Result |
| --- | --- | --- | --- | --- |
| {{ROLE}} | `{{SKILL}}` | {{INVOCATION}} | {{SOURCE}} | {{SELECTED_FALLBACK_HANDOFF}} |

## Decision

- Goal: {{GOAL}}
- Risk summary: {{RISK}}
- Launch scenario: `{{NEW_PROJECT_CONTINUE_PROJECT_EXISTING_PROJECT_NOT_APPLICABLE}}`
- Public interaction mode: `{{INTERVIEW_ASSISTED_FULL_AUTO_NOT_APPLICABLE}}`
- Pending interaction mode: `{{MODE_AT_NEXT_SAFE_TRANSITION_OR_NONE}}`
- Execution profile: `{{SPEED_BALANCED_QUALITY}}`
- Internal controller autonomy: `{{MANAGED_LOCAL_EXTENDED}}`
- Effective permissions: {{EFFECTIVE_PERMISSION_SUMMARY}}
- Current stage gate: `{{GATE}}`
- Decision-map state: `{{NOT_REQUIRED_REQUIRED_READY_OR_BLOCKED}}`
- Delegated decisions: {{DELEGATED_DECISIONS_OR_NONE}}
- Assumption count: {{ASSUMPTION_COUNT}}
- Unresolved placeholder count: {{PLACEHOLDER_COUNT}}
- Decision rationale/approval: {{DECISION_RECORD}}

## Source intent and traceability

- Traceability mode: `{{NOT_APPLICABLE_INLINE_DURABLE}}`
- Source brief: `{{SOURCE_BRIEF_PATH_OR_INLINE}}`
- Source brief identity/hash: `{{SOURCE_BRIEF_IDENTITY_OR_NONE}}`
- Requirement manifest: `{{REQUIREMENT_MANIFEST_PATH_OR_INLINE}}`
- Requirement manifest identity/hash: `{{REQUIREMENT_MANIFEST_IDENTITY_OR_NONE}}`
- User-intent counts: {{U_OPEN_IN_SPEC_IN_TASK_IMPLEMENTED_VERIFIED_PLACEHOLDER_DEFERRED_DROPPED}}
- G1 clarification completeness: `{{PASS_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G2 brief-to-spec coverage: `{{PASS_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G2 report/evidence: {{G2_REPORT_OR_NONE}}
- G3 requirement-task traceability: `{{PASS_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G3 report/evidence: {{G3_REPORT_OR_NONE}}
- G4 blind acceptance: `{{PASS_PARTIAL_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G4 report/evidence: {{G4_REPORT_OR_NONE}}
- Material source-intent drift: {{DRIFT_OR_NONE}}

## Browser / E2E verification

- Web/browser relevance: `{{YES_NO_NOT_APPLICABLE}}`
- Existing E2E framework: `{{FRAMEWORK_OR_NONE}}`
- Existing E2E command: `{{COMMAND_OR_NONE}}`
- Browser mode: `{{PLAYWRIGHT_MANAGED_CHROME_CDP_HOST_BROWSER_TOOL_OTHER_UNAVAILABLE_NOT_APPLICABLE}}`
- Isolated browser context: `{{YES_NO_DEGRADED_NOT_APPLICABLE}}`
- Browser install/download required: `{{YES_NO}}`
- Local app/process start required: `{{YES_NO}}`
- Port bind/listen required: `{{YES_NO}}`
- Test-data mutation required: `{{YES_NO}}`
- Destructive test setup possible: `{{YES_NO}}`
- Destructive test environment proof: {{ENVIRONMENT_MUTATION_AUTHORITY_ROLLBACK_OR_NONE}}
- Automated E2E status: `{{PASS_FAIL_NOT_RUN_BLOCKED_NOT_APPLICABLE}}`
- Automated E2E counts: {{PASSED_FAILED_SKIPPED_OR_NONE}}
- Browser G4 status: `{{PASS_PARTIAL_FAIL_BLOCKED_HANDOFF_NOT_APPLICABLE}}`
- Browser G4 target: {{SAFE_URL_OR_ENV_LABEL_OR_NONE}}
- Browser evidence refs: {{SCREENSHOT_TRACE_VIDEO_REPORT_REFS_OR_NONE}}
- Browser console findings: {{COUNT_SUMMARY_OR_NONE_UNAVAILABLE}}
- Browser network findings: {{COUNT_SUMMARY_OR_NONE_UNAVAILABLE}}
- Browser blocked authority/capability: {{MISSING_AUTHORITY_OR_CAPABILITY_OR_NONE}}

## Durable project artifacts

- Context path: `{{CONTEXT_PATH_OR_NONE}}`
- Context source and review state: {{CONTEXT_SOURCE_REVIEW_OR_NONE}}
- ADR IDs: {{ADR_IDS_OR_NONE}}
- Progress path: `{{PROGRESS_PATH_OR_INLINE}}`
- Progress projection status: `{{CURRENT_STALE_MISSING_UNAUTHORIZED}}`
- Dashboard HTML path: `{{DASHBOARD_HTML_PATH_OR_NONE}}`
- Dashboard state path: `{{DASHBOARD_STATE_PATH_OR_NONE}}`
- Dashboard projection status: `{{CURRENT_STALE_MISSING_UNAUTHORIZED_UNSUPPORTED}}`
- Last projection update event: {{EVENT_TIME_OR_NONE}}
- Recorded source conflicts: {{CONFLICTS_OR_NONE}}

## Permission envelope

- Allowed scope: {{ALLOWED_SCOPE}}
- Inspect-only scope: {{INSPECT_ONLY}}
- Forbidden scope: {{FORBIDDEN_SCOPE}}
- Decision delegation: {{DECISIONS}}
- Matreshka source-intent/run-state authority: {{TRACEABILITY_STATE_AUTHORITY}}
- Local writes/commands: {{LOCAL_AUTHORITY}}
- Browser interaction: {{BROWSER_TARGET_MODE_INTERACTION_AUTHORITY}}
- Local process/runtime: {{LOCAL_PROCESS_START_STOP_AUTHORITY}}
- Port binding/listening: {{PORT_AUTHORITY}}
- Browser/dependency installation: {{BROWSER_DEPENDENCY_INSTALL_AUTHORITY}}
- Test-data mutation: {{TEST_DATA_MUTATION_AUTHORITY}}
- Destructive E2E setup: {{DESTRUCTIVE_TEST_AUTHORITY}}
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

| Task | Dependency | U/S requirements | Status | Agent turns used/max | High-judgment turns |
| --- | --- | --- | --- | --- | --- |
| {{TASK_ID}} | {{DEPENDENCY}} | {{U_AND_S_IDS}} | {{STATUS}} | {{USED_MAX}} | {{USED}} |

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
- Source-intent narrowing findings: {{U_REQUIREMENT_FINDINGS_OR_NONE}}
- Rejected/adjacent findings: {{ADJUDICATION}}
- Fixer wave used: {{YES_NO}}
- Targeted re-review result: {{RESULT_OR_PENDING}}

## Verification

| Command/interaction | Exit/signal | Counts | Relevant note | Baseline/current |
| --- | --- | --- | --- | --- |
| `{{COMMAND_OR_INTERACTION}}` | {{EXIT_OR_SIGNAL}} | {{COUNTS}} | {{NOTE}} | {{STATE}} |

- Pre-existing failures: {{FAILURES_OR_NONE}}
- Technical/security verification status: `{{STATUS}}`
- Quality-gate rows: {{PASS_FAIL_NOT_RUN_BLOCKED_SUMMARY}}
- Required browser E2E rows: {{PASS_FAIL_NOT_RUN_BLOCKED_NOT_APPLICABLE_SUMMARY}}
- Blind acceptance follows technical/security verification when G4 applies; browser G4 is one observation mode and never substitutes for required technical/security rows.

## Workspace and learning

- Run worktree: {{PATH_BRANCH_TASK_OWNERSHIP_OR_NONE}}
- Worktree cleanup authority: {{AUTHORITY_OR_NONE}}
- Learning mode: `{{OFF_PROPOSE_LOCAL_REVIEWED}}`
- Candidate IDs and evidence: {{CANDIDATES_OR_NONE}}
- Promotion/revalidation status: {{STATUS_OR_NONE}}

## Recovery and next action

- Loaded contract/plugin version: `{{LOADED_CONTRACT_AND_PLUGIN_VERSION}}`
- Version difference and in-memory compatibility: {{VERSION_DIFFERENCE_OR_NONE}}
- Source brief/manifest mismatch: {{INTENT_MISMATCH_OR_NONE}}
- Browser capability/evidence mismatch: {{BROWSER_MISMATCH_OR_NONE}}
- Progress/dashboard/ledger/actual-state mismatch: {{MISMATCH_OR_NONE}}
- Last safe checkpoint: {{CHECKPOINT}}
- Last verified checkpoint: {{VERIFIED_CHECKPOINT}}
- Active turns: {{ACTIVE_OR_NONE}}
- Stop reason: {{REASON_OR_NONE}}
- Exact next action: {{ONE_ACTION}}
