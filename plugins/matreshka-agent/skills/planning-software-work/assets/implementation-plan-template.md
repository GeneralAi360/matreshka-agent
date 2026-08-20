# Implementation Plan — {{TITLE}}

- Status: `{{DRAFT_OR_READY}}`
- Confirmed specification: `{{SPECIFICATION_PATH_OR_REFERENCE}}`
- Project root: `{{REAL_PROJECT_ROOT}}`
- Baseline: `{{GIT_REF_OR_NO_GIT_BASELINE}}`
- Applicable instructions: {{INSTRUCTION_PATHS}}
- Recommended execution profile: `{{SPEED_BALANCED_QUALITY}}`
- Complexity tier: `{{T0_T1_T2_T3}}`
- Permission/remote boundary: {{BOUNDARY_SUMMARY}}

## Goal

{{ONE_OVERALL_OUTCOME}}

## Non-goals

- {{EXCLUDED_OUTCOME}}

## Constraints and pre-existing state

- {{CONSTRAINT_OR_EXISTING_FAILURE}}

## Project Intelligence snapshot

- Topology status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE}}`
- Affected areas: {{AREA_IDS}}
- Runtime-map status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE_NOT_APPLICABLE}}`
- Project-intelligence source/state: {{RUN_STATE_PROFILE_OR_INLINE}}

| Area ID | Kind | Purpose in this change | Roots / entry points | Produces / consumes | Key boundary |
| --- | --- | --- | --- | --- | --- |
| `{{AREA_ID}}` | {{KIND}} | {{PURPOSE}} | {{PATHS}} | {{INTERFACES}} | {{DATA_SECURITY_RUNTIME_BOUNDARY}} |

Do not manufacture frontend/backend or other areas to fill this table. A cohesive one-area project/task remains one area.

## Coverage matrix

| Requirement ID | Requirement/source | Task | Verification evidence | Negative/rollback evidence |
| --- | --- | --- | --- | --- |
| `U-01` | {{USER_REQUIREMENT_OR_NA}} | `T1` | {{CHECK}} | {{NEGATIVE_OR_NA}} |
| `S-01` | {{SECURITY_REQUIREMENT_OR_NA}} | `T1` | {{SECURITY_EVIDENCE}} | {{NEGATIVE_SECURITY_PROOF}} |

## Cross-area interface contracts

Create rows only when a user/system outcome crosses independently owned areas and producer/consumer assumptions can drift.

| Contract | Source requirements | Producer | Consumers | Run-state path | Freeze before | Integration proof |
| --- | --- | --- | --- | --- | --- | --- |
| `IC-01` | {{U_S_IDS}} | `{{AREA_ID}}` | {{AREA_IDS}} | `.matreshka/runs/<run-id>/interfaces/{{FILE}}` | `{{TASK_ID}}` | {{CHECK}} |

- No cross-area seam: {{YES_NO}}
- Contract-change policy: a frozen material contract change returns to controller reconciliation before dependent writer work continues.

## Task map

| Task | Result | Primary area | Role archetype | Context set | Interfaces | Depends on | Write paths | Risk/tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `T1` | {{RESULT}} | `{{AREA_ID}}` | `{{ROLE_ARCHETYPE}}` | `{{NARROW_DEGRADED}}` | {{IC_IDS_OR_NONE}} | {{DEPENDENCY_OR_NONE}} | {{PATHS}} | {{RISK_TIER}} |

## Shared execution policy

- Writing agents: sequential in one checkout.
- Child agents: forbidden.
- Project areas do not create extra agent budget automatically.
- Specialist role labels reuse existing Matreshka skills and grant no extra authority.
- Fixer waves: maximum one per task.
- Adjacent issues: record without changing.
- Broad suite/build: {{PHASE_GATE}}
- Phase agent-turn budget: {{USED_MAX}}
- High-judgment turn budget: {{USED_MAX}}
- Audit threshold: {{TIME_CONTEXT_OR_TURN_THRESHOLD}}
- Repeat Critical/Important after fix: `STOP_AND_RESCOPE`.

---

## Task T1 — {{TITLE}}

### Goal and coverage

- Result: {{ONE_MEASURABLE_RESULT}}
- Requirements: `{{REQUIREMENT_IDS}}`
- Security requirements: `{{SECURITY_REQUIREMENT_IDS_OR_NA}}`

### Project Intelligence routing

- Role archetype: `{{ROLE_ARCHETYPE}}`
- Primary area: `{{AREA_ID}}`
- Adjacent areas: {{AREA_IDS_OR_NONE}}
- Frozen interface contracts: {{IC_IDS_AND_HASHES_OR_NONE}}
- Area context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`
- Include only: {{TASK_LOCAL_CONTEXT_SOURCES}}
- Explicitly exclude: {{UNRELATED_AREAS_REPORTS_HISTORY}}
- Runtime dependency/observation: {{SERVICE_STATUS_LOG_OR_NONE}}

### Inputs

- Existing interfaces: {{EXACT_INTERFACES}}
- Required design section: {{SECTION_REFERENCE}}
- Task baseline: {{BASELINE}}

### Produces

- {{EXACT_INTERFACE_OR_BEHAVIOR}}
- Potential durable documentation impact: {{NONE_OR_INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW}}

### Allowed files

Write only:

- `{{REAL_PATH}}`

Inspect-only:

- `{{REAL_PATH_OR_SCOPE}}`

### Role boundary

- Owned responsibility: {{ROLE_OWNED_RESPONSIBILITY}}
- Forbidden neighboring responsibility: {{ROLE_FORBIDDEN_RESPONSIBILITY}}

### Non-goals and forbidden actions

- {{NON_GOAL}}
- Do not redefine a frozen `IC-xx`; return material contract drift to the controller.
- No child agents or adjacent fixes.
- No Git, network, secret, browser, unapproved process, deploy, migration application, or remote action. Controller-owned boundary or handoff: {{CONTROLLER_ACTION_OR_NONE}}.

### RED

- Check: {{FOCUSED_CHECK}}
- Command: `{{COMMAND}}`
- Expected failure reason: {{REASON}}

### GREEN

- Minimal behavior: {{BEHAVIOR}}
- Command: `{{COMMAND}}`
- Expected result: {{RESULT}}

### Task gate

- Task suite: `{{COMMAND}}`
- Nearest regression: `{{COMMAND}}`
- Targeted static/diff check: `{{COMMAND}}`
- Cross-area contract/integration proof: {{COMMAND_OR_NA_WITH_REASON}}
- Conditional security/dependency check: {{COMMAND_OR_NA_WITH_REASON}}
- Security negative proof: {{TEST_OR_REVIEW_OR_NA_WITH_REASON}}
- Conditional build: {{COMMAND_OR_NA_WITH_REASON}}
- Evidence: command / exit code / counts / relevant note.

### Execution and review budget

- Risk/capability tier: {{RISK_TIER}}
- Profile: `{{SPEED_BALANCED_QUALITY}}`
- Unique roles: {{MAX}}
- Agent turns: {{MAX}}
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | `{{CONTROLLER_OR_COMBINED_OR_SPEC}}` | {{OWNED}} | {{EXCLUDED_OR_NONE}} | {{FINDINGS_OR_NA}} |
  | `{{SECURITY_CODE_OR_NA}}` | {{OWNED_OR_NA}} | {{EXCLUDED_OR_NA}} | {{FINDINGS_OR_NA}} |
- Context inputs: {{AREA_CONTEXT_SET_AND_INTERFACE_REFS}}
- Report path: `{{REPORT_PATH}}`

### Stop and handoff conditions

- `NEEDS_CONTEXT`: {{CONDITION}}
- `BLOCKED`: {{CONDITION}}
- `INTERFACE_CHANGED`: frozen contract identity no longer matches required behavior; controller reconciliation required.
- `SPLIT_REQUIRED`: a second independent result or boundary appears.
- `CONTEXT_TOO_BROAD`: task-local context cannot be preserved without hiding a required dependency.
- `RECORD_FOR_FUTURE_TASK`: an adjacent issue is found.
- `STOP_AND_RESCOPE`: cohesion fails or a blocker remains after the single fixer wave.
- `HANDOFF_REQUIRED`: {{REMOTE_BOUNDARY_OR_NA}}

### Exact next task

On successful verification, proceed to `{{NEXT_TASK_OR_FINAL_GATE}}`.

---

## Phase/final verification

| Evidence | Command or operator | Expected result | Run once after |
| --- | --- | --- | --- |
| {{AREA_OR_INTEGRATION_CHECK}} | `{{COMMAND}}` | {{RESULT}} | {{TASK_OR_PHASE}} |

## Documentation impact candidates

| Durable truth | Candidate docs | Expected gate after fresh verification |
| --- | --- | --- |
| {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW_OR_NONE}} | {{PATHS_OR_NONE}} | `{{DOCS_NOT_REQUIRED_DOCS_CURRENT_DOCS_UPDATE_REQUIRED}}` |

This table predicts impact only. The controller performs the real documentation drift gate against verified current behavior after implementation.

## Remote handoff

- Local operator: {{LOCAL_OPERATOR}}
- Remote operator/system: {{REMOTE_OPERATOR_AND_SYSTEM_OR_NA}}
- Allowed preparation: {{PREPARATION}}
- Forbidden execution: {{FORBIDDEN_REMOTE_ACTION}}
- Final local status: `{{COMPLETE_PARTIAL_HANDOFF}}`

## Plan validation

- [ ] Every requirement maps to task and evidence.
- [ ] Every task maps to a requirement or justified enabling step.
- [ ] Current topology reflects repository evidence; no fake frontend/backend split was added.
- [ ] Every task has one primary area and a bounded `AREA_CONTEXT_SET`.
- [ ] Every cross-area producer/consumer seam that can drift has one `IC-xx` contract and freeze order.
- [ ] Dependent tasks reference the same contract identity rather than redefining it.
- [ ] Runtime dependencies identify ownership/status/log seams and do not imply process authority.
- [ ] Specialist roles stay inside the selected agent/turn budget and existing permissions.
- [ ] Paths, interfaces, and commands are inspected or in a bounded discovery gate.
- [ ] Shared write paths are sequenced.
- [ ] No task mixes independent outcomes or security boundaries.
- [ ] Permissions, budgets, reports, and stop conditions are explicit.
- [ ] Documentation impact candidates are identified without updating docs before verification.
- [ ] No unresolved placeholder remains in a `PLAN_READY` artifact.
