# Matreshka Run Ledger

## Identity

- Contract version: `{{CONTRACT_VERSION}}`
- Plugin version: `{{PLUGIN_VERSION}}`
- Run ID: `{{RUN_ID}}`
- Updated at: `{{TIMESTAMP_ISO8601}}`
- User-facing language: `{{USER_LANGUAGE}}`
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
| Token counters | {{YES_NO_PARTIAL}} | {{COUNTER_SOURCE_AND_SEMANTICS}} |
| Local dashboard display | {{YES_NO}} | {{DETAIL_WITHOUT_IMPLIED_AUTHORITY}} |
| Browser E2E | {{YES_NO_DEGRADED}} | {{FRAMEWORK_COMMAND_MODE_ISOLATION}} |
| Browser screenshots/trace | {{YES_NO_DEGRADED}} | {{DETAIL}} |
| Browser console/network inspection | {{YES_NO_DEGRADED}} | {{DETAIL}} |
| Visual design rendering/check | {{YES_NO_DEGRADED}} | {{VIEWPORT_SCREENSHOT_RENDER_CAPABILITY}} |

- Mode status: `{{FULL_DEGRADED_INLINE_HANDOFF}}`
- Missing guarantees: {{GAPS_OR_NONE}}

## Observability metrics

- Timing status: `{{EXACT_PARTIAL_UNAVAILABLE}}`
- Run started at: `{{STARTED_AT_ISO8601_OR_NONE}}`
- Run finished at: `{{FINISHED_AT_ISO8601_OR_NONE}}`
- Wall-clock elapsed: `{{ELAPSED_SECONDS_OR_NONE}}`
- Implementation/fix/reverify elapsed: `{{IMPLEMENTATION_SECONDS_OR_NONE}}`
- Timing source/limitations: {{TIMING_SOURCE_OR_LIMITATION}}
- Token usage status: `{{EXACT_PARTIAL_UNAVAILABLE}}`
- Total tokens: `{{TOTAL_TOKENS_OR_NONE}}`
- Observed partial tokens: `{{OBSERVED_TOKENS_OR_NONE}}`
- Input tokens: `{{INPUT_TOKENS_OR_NONE}}`
- Output tokens: `{{OUTPUT_TOKENS_OR_NONE}}`
- Reasoning tokens: `{{REASONING_TOKENS_OR_NONE}}`
- Cached tokens: `{{CACHED_TOKENS_OR_NONE}}`
- Usage counter source/semantics: {{USAGE_SOURCE_OR_LIMITATION}}
- Agent/controller turns used: `{{TURNS_USED}}`

Never estimate unavailable timing or token totals. `PARTIAL` token usage is an exact observed subset, not the total. Do not add repeated cumulative counters twice.

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
- Delivery status: `{{COMPLETE_PARTIALLY_VERIFIED_BLOCKED_HANDOFF_REQUIRED_OR_OTHER}}`
- Run rigor: `{{FULL_DEGRADED}}`
- Rigor degradations: `{{RIGOR_DEGRADATIONS_OR_NONE}}`
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
- G2 evidence class: `{{CLEAN_FRESH_NATIVE_CLEAN_FRESH_EXTERNAL_CLEAN_DEGRADED_INLINE_GAP_BLOCKED}}`
- G2 gate identity/sequence: `{{PRE_PLAN_GATE_IDENTITY_AND_POSTHOC_AUDIT_NOTE_OR_NONE}}`
- G2 report/evidence: {{G2_REPORT_OR_NONE}}
- G3 requirement-task traceability: `{{PASS_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G3 report/evidence: {{G3_REPORT_OR_NONE}}
- G4 blind acceptance: `{{PASS_PARTIAL_BLOCKED_PENDING_NOT_APPLICABLE}}`
- G4 report/evidence: {{G4_REPORT_OR_NONE}}
- Material source-intent drift: {{DRIFT_OR_NONE}}

## Project Intelligence

- Intelligence state path: `{{PROJECT_INTELLIGENCE_PATH_OR_INLINE}}`
- Topology status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE}}`
- Topology identity/source: {{TOPOLOGY_IDENTITY_AND_SOURCE}}
- Area count: `{{AREA_COUNT}}`
- Affected areas: {{AREA_IDS}}
- Current primary area: `{{AREA_ID_OR_NONE}}`
- Area-context guarantee for current task: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD_NOT_APPLICABLE}}`
- Current included context sources: {{CONTEXT_SOURCES_OR_NONE}}
- Current explicit context exclusions: {{CONTEXT_EXCLUSIONS_OR_NONE}}
- Active cross-area interface contracts: {{IC_IDS_HASHES_STATUS_OR_NONE}}
- Interface contract drift/conflict: {{INTERFACE_DRIFT_OR_NONE}}
- Runtime-map status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE_NOT_APPLICABLE}}`
- Runtime services relevant to run: {{SERVICE_IDS_OR_NONE}}
- Runtime ownership/blocker: {{RUNTIME_OWNERSHIP_OR_NONE}}
- Documentation drift state: `{{DOCS_NOT_REQUIRED_DOCS_CURRENT_DOCS_UPDATE_REQUIRED_DOCS_BLOCKED_DOCS_CONFLICT_PENDING}}`
- Documentation impact paths: {{DOC_PATHS_OR_NONE}}
- Current specialist archetype: `{{ROLE_ARCHETYPE_OR_NONE}}`
- Specialist routing rationale/budget: {{RATIONALE_AND_BUDGET_OR_NONE}}

Project Intelligence is descriptive coordination state. It cannot grant authority, replace current repository evidence, satisfy verification, or add agent budget.

## Design Intelligence

- Design relevance/state: `{{DESIGN_NOT_APPLICABLE_CURRENT_RECON_REQUIRED_DIRECTION_REQUIRED_BLOCKED_READY_TO_SAVE}}`
- Root design contract path: `{{DESIGN_MD_PATH_OR_INLINE_OR_NONE}}`
- Root design contract current/stale/conflict state: `{{CURRENT_STALE_CONFLICT_UNAVAILABLE_NOT_APPLICABLE}}`
- Frozen design identity/hash: `{{DESIGN_IDENTITY_OR_NONE}}`
- Product personality: {{PRODUCT_PERSONALITY_OR_NONE}}
- Approved/selected direction: {{DESIGN_DIRECTION_OR_EXISTING_OR_NONE}}
- Direction selection authority/source: {{USER_FULL_AUTO_EXISTING_RECON_OR_NONE}}
- Prototype state/path: {{NONE_INLINE_RUN_LOCAL_PROJECT_SANDBOX_SELECTED_RETIRED}}
- Prototype evidence refs: {{SAFE_REFS_OR_NONE}}
- Current task design-context guarantee: `{{NARROW_DEGRADED_DESIGN_CONTEXT_TOO_BROAD_NOT_APPLICABLE}}`
- Current included design context: {{DESIGN_CONTEXT_SOURCES_OR_NONE}}
- Current explicit design exclusions: {{DESIGN_CONTEXT_EXCLUSIONS_OR_NONE}}
- Design review status: `{{APPROVED_CHANGES_REQUIRED_UNCHECKABLE_BLOCKED_PENDING_NOT_APPLICABLE}}`
- Visual design check status: `{{PASS_PARTIAL_FAIL_NOT_RUN_BLOCKED_UNCHECKABLE_NOT_APPLICABLE}}`
- Visual design viewports/states: {{VIEWPORTS_STATES_OR_NONE}}
- Visual design evidence refs: {{SAFE_SCREENSHOT_REPORT_REFS_OR_NONE}}
- Design drift gate: `{{DESIGN_NOT_APPLICABLE_DESIGN_CURRENT_DESIGN_UPDATE_REQUIRED_DESIGN_DRIFT_DESIGN_CONFLICT_DESIGN_BLOCKED_PENDING}}`
- Design drift/update detail: {{DESIGN_DRIFT_OR_UPDATE_DETAIL_OR_NONE}}
- Material design decision history refs: {{DECISION_REFS_OR_NONE}}

Design Intelligence/`DESIGN.md` is durable UX/UI context and bounded evidence. It cannot grant implementation, dependency, browser/process, Git, remote, secret, provider, destructive, or design-change authority by itself. G4 must not consume this section.

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
- Project profile path: `{{PROJECT_PROFILE_PATH_OR_NONE}}`
- Project profile current/stale state: {{PROFILE_STATE_OR_NONE}}
- Design contract path: `{{DESIGN_MD_PATH_OR_NONE}}`
- ADR IDs: {{ADR_IDS_OR_NONE}}
- Progress path: `{{PROGRESS_PATH_OR_INLINE}}`
- Progress projection status: `{{CURRENT_STALE_MISSING_UNAUTHORIZED}}`
- Dashboard HTML path: `{{DASHBOARD_HTML_PATH_OR_NONE}}`
- Dashboard state path: `{{DASHBOARD_STATE_PATH_OR_NONE}}`
- Dashboard projection status: `{{CURRENT_STALE_MISSING_UNAUTHORIZED_UNSUPPORTED}}`
- Last projection update event: {{EVENT_TIME_OR_NONE}}
- Recorded source/design/context conflicts: {{CONFLICTS_OR_NONE}}

## Permission envelope

- Allowed scope: {{ALLOWED_SCOPE}}
- Inspect-only scope: {{INSPECT_ONLY}}
- Forbidden scope: {{FORBIDDEN_SCOPE}}
- Decision delegation: {{DECISIONS}}
- Matreshka source-intent/run-state authority: {{TRACEABILITY_STATE_AUTHORITY}}
- Project Intelligence state/profile authority: {{PROJECT_INTELLIGENCE_STATE_AUTHORITY}}
- Design recon/read authority: {{DESIGN_READ_AUTHORITY}}
- Root `DESIGN.md` / design-state writes: {{DESIGN_STATE_WRITE_AUTHORITY}}
- Prototype write/cleanup authority: {{DESIGN_PROTOTYPE_AUTHORITY}}
- Local product writes/commands: {{LOCAL_AUTHORITY}}
- Documentation writes: {{DOCUMENTATION_AUTHORITY}}
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

| Task | Dependency | U/S requirements | Area | Role archetype | Interfaces | Area context | Design ID/context | Status | Agent turns used/max | High-judgment turns |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{TASK_ID}} | {{DEPENDENCY}} | {{U_AND_S_IDS}} | `{{AREA_ID}}` | `{{ROLE_ARCHETYPE}}` | {{IC_IDS_OR_NONE}} | {{NARROW_DEGRADED}} | {{DESIGN_ID_AND_CONTEXT_OR_NA}} | {{STATUS}} | {{USED_MAX}} | {{USED}} |

- Current task: `{{TASK_ID}}`
- Total agent turns used/max: `{{USED_MAX}}`
- Broad checks used/max: `{{USED_MAX}}`
- Audit threshold: {{THRESHOLD}}

## Dispatches

| Turn | Task | Area | Role archetype | Design identity | Stable thread ID | Tier | Brief/report | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| {{N}} | {{TASK}} | `{{AREA_ID}}` | `{{ROLE_ARCHETYPE}}` | {{DESIGN_ID_OR_NA}} | `{{THREAD_ID}}` | {{TIER}} | {{PATHS}} | {{STATUS}} |

## Review

- Confirmed findings: {{FINDINGS_OR_NONE}}
- Source-intent narrowing findings: {{U_REQUIREMENT_FINDINGS_OR_NONE}}
- Cross-area interface findings: {{INTERFACE_FINDINGS_OR_NONE}}
- Design findings: {{DESIGN_FINDINGS_OR_NONE}}
- Design evidence limitation: {{VISUAL_REVIEW_LIMITATION_OR_NONE}}
- Rejected/adjacent findings: {{ADJUDICATION}}
- Fixer wave used: {{YES_NO}}
- Targeted re-review result: {{RESULT_OR_PENDING}}

## Verification

| Command/interaction | Exit/signal | Counts | Relevant note | Baseline/current |
| --- | --- | --- | --- | --- |
| `{{COMMAND_OR_INTERACTION}}` | {{EXIT_OR_SIGNAL}} | {{COUNTS}} | {{NOTE}} | {{STATE}} |

- Latest applicable test-gate counts: {{PASSED_FAILED_SKIPPED_OR_NONE}}
- Area-local evidence: {{AREA_EVIDENCE_SUMMARY}}
- Cross-area integration/contract evidence: {{INTERFACE_EVIDENCE_OR_NONE}}
- Runtime evidence/caveat: {{RUNTIME_EVIDENCE_OR_NONE}}
- Pre-existing failures: {{FAILURES_OR_NONE}}
- Technical/security verification status: `{{STATUS}}`
- Quality-gate rows: {{PASS_FAIL_NOT_RUN_BLOCKED_SUMMARY}}
- Required browser E2E rows: {{PASS_FAIL_NOT_RUN_BLOCKED_NOT_APPLICABLE_SUMMARY}}
- Design verification: {{DESIGN_REVIEW_AND_VISUAL_STATUS_OR_NOT_APPLICABLE}}
- Design drift gate runs from frozen design identity + current verified/rendered state; design docs never substitute for technical/security evidence.
- Documentation drift gate runs after design reconciliation and verified current behavior; docs never substitute for technical/security evidence.
- Blind acceptance follows sufficient technical/security/design evidence when G4 applies; G4 must not read `DESIGN.md`, design state, review or visual reports.

## Workspace and learning

- Run worktree: {{PATH_BRANCH_TASK_OWNERSHIP_OR_NONE}}
- Worktree cleanup authority: {{AUTHORITY_OR_NONE}}
- Prototype cleanup state: {{OWNED_PROTOTYPE_PATHS_AND_AUTHORITY_OR_NONE}}
- Learning mode: `{{OFF_PROPOSE_LOCAL_REVIEWED}}`
- Candidate IDs and evidence: {{CANDIDATES_OR_NONE}}
- Promotion/revalidation status: {{STATUS_OR_NONE}}

## Recovery and next action

- Loaded contract/plugin version: `{{LOADED_CONTRACT_AND_PLUGIN_VERSION}}`
- Version difference and in-memory compatibility: {{VERSION_DIFFERENCE_OR_NONE}}
- Source brief/manifest mismatch: {{INTENT_MISMATCH_OR_NONE}}
- Project Intelligence topology/profile mismatch: {{TOPOLOGY_PROFILE_MISMATCH_OR_NONE}}
- Interface-contract mismatch: {{INTERFACE_MISMATCH_OR_NONE}}
- Runtime ownership/state mismatch: {{RUNTIME_MISMATCH_OR_NONE}}
- Design contract/identity mismatch: {{DESIGN_IDENTITY_MISMATCH_OR_NONE}}
- Design context/review/visual mismatch: {{DESIGN_EVIDENCE_MISMATCH_OR_NONE}}
- Documentation drift mismatch: {{DOCS_MISMATCH_OR_NONE}}
- Browser capability/evidence mismatch: {{BROWSER_MISMATCH_OR_NONE}}
- Timing/usage mismatch: {{OBSERVABILITY_MISMATCH_OR_NONE}}
- Progress/dashboard/ledger/actual-state mismatch: {{MISMATCH_OR_NONE}}
- Last safe checkpoint: {{CHECKPOINT}}
- Last verified checkpoint: {{VERIFIED_CHECKPOINT}}
- Active turns: {{ACTIVE_OR_NONE}}
- Stop reason: {{REASON_OR_NONE}}
- Exact next action: {{ONE_ACTION}}
