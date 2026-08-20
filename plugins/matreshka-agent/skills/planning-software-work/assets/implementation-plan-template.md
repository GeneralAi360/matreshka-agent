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

## Design Intelligence snapshot

- Design relevance/state: `{{DESIGN_NOT_APPLICABLE_CURRENT_RECON_DIRECTION_BLOCKED}}`
- Root design contract: `{{DESIGN_MD_PATH_OR_INLINE_OR_NONE}}`
- Frozen design identity: `{{DESIGN_IDENTITY_OR_NONE}}`
- Product personality: {{PERSONALITY_OR_NA}}
- Selected direction/prototype: {{DIRECTION_OR_EXISTING_OR_NONE}}
- Design review required for this phase: `{{YES_NO}}`
- Visual design check capability/status: `{{AVAILABLE_DEGRADED_UNAVAILABLE_NOT_APPLICABLE}}`

For UI-bearing work, all dependent tasks plan against one frozen design identity. `DESIGN_CHANGED` requires controller reconciliation; unexplained UI divergence is `DESIGN_DRIFT`. Backend-only work should normally stay `DESIGN_NOT_APPLICABLE`.

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

| Task | Result | Primary area | Role archetype | Area context | Design context | Design ID | Interfaces | Depends on | Write paths | Risk/tier |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `T1` | {{RESULT}} | `{{AREA_ID}}` | `{{ROLE_ARCHETYPE}}` | `{{NARROW_DEGRADED}}` | `{{NARROW_DEGRADED_NA}}` | {{DESIGN_ID_OR_NA}} | {{IC_IDS_OR_NONE}} | {{DEPENDENCY_OR_NONE}} | {{PATHS}} | {{RISK_TIER}} |

## Shared execution policy

- Writing agents: sequential in one checkout.
- Child agents: forbidden.
- Project areas/design surfaces do not create extra agent budget automatically.
- Specialist role labels reuse existing Matreshka skills and grant no extra authority.
- `DESIGN_ENGINEER` owns design recon/direction/contract only; `DESIGN_REVIEWER` is read-only; `UI_SPECIALIST` implements frozen design rather than redefining it.
- Fixer waves: maximum one per task, including design findings.
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

### Design Intelligence routing

- Design relevance: `{{DESIGN_NOT_APPLICABLE_CURRENT_RECON_DIRECTION_BLOCKED}}`
- Root design contract: `{{DESIGN_MD_PATH_OR_NONE}}`
- Frozen design identity: `{{DESIGN_IDENTITY_OR_NONE}}`
- Design context guarantee: `{{NARROW_DEGRADED_DESIGN_CONTEXT_TOO_BROAD_NOT_APPLICABLE}}`
- Include only: {{RELEVANT_LAYOUT_COMPONENT_TOKENS_STATES_RESPONSIVE_A11Y_MOTION}}
- Explicitly exclude: {{UNRELATED_SCREENS_HISTORY_PROTOTYPES}}
- Approved direction/prototype: {{DIRECTION_OR_NONE}}
- Design review assignment: {{COMBINED_DESIGN_REVIEWER_OR_NA}}
- Visual design check: {{REQUIRED_NOT_REQUIRED_UNAVAILABLE}}

### Inputs

- Existing interfaces: {{EXACT_INTERFACES}}
- Required specification section: {{SECTION_REFERENCE}}
- Required design sections/invariants: {{DESIGN_SECTION_REFERENCES_OR_NA}}
- Task baseline: {{BASELINE}}

### Produces

- {{EXACT_INTERFACE_OR_BEHAVIOR}}
- Design-critical states/viewports: {{DEFAULT_FOCUS_LOADING_ERROR_EMPTY_SUCCESS_RESPONSIVE_OR_NA}}
- Potential durable design impact: {{NONE_OR_PERSONALITY_LAYOUT_TOKENS_COMPONENT_RESPONSIVE_A11Y_MOTION}}
- Potential durable documentation impact: {{NONE_OR_INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW}}

### Allowed files

Write only:

- `{{REAL_PATH}}`

Inspect-only:

- `{{REAL_PATH_OR_SCOPE}}`

### Role boundary

- Owned responsibility: {{ROLE_OWNED_RESPONSIBILITY}}
- Forbidden neighboring responsibility: {{ROLE_FORBIDDEN_RESPONSIBILITY}}
- UI implementation follows frozen design identity; implementer does not edit `DESIGN.md` to make code compliant.

### Non-goals and forbidden actions

- {{NON_GOAL}}
- Do not redefine a frozen `IC-xx`; return material contract drift to controller.
- Do not redefine the frozen design identity; return `DESIGN_CHANGED` for valid new design authority or `DESIGN_DRIFT` for unexplained implementation divergence.
- No child agents or adjacent fixes.
- No Git, network, secret, browser, unapproved process, dependency install, deploy, migration application, or remote action. Controller-owned boundary or handoff: {{CONTROLLER_ACTION_OR_NONE}}.

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
- Design-contract/code check: {{CHECK_OR_NA_WITH_REASON}}
- Visual design check/state matrix: {{INTERACTION_OR_NA_UNAVAILABLE_WITH_REASON}}
- Conditional build: {{COMMAND_OR_NA_WITH_REASON}}
- Evidence: command/interaction / exit/signal / counts / relevant note.

### Execution and review budget

- Risk/capability tier: {{RISK_TIER}}
- Profile: `{{SPEED_BALANCED_QUALITY}}`
- Unique roles: {{MAX}}
- Agent turns: {{MAX}}
- Reviewer assignments:

  | Role | Owned concerns | Excluded concerns | Recheck boundary |
  | --- | --- | --- | --- |
  | `{{CONTROLLER_OR_COMBINED_OR_SPEC}}` | {{OWNED}} | {{EXCLUDED_OR_NONE}} | {{FINDINGS_OR_NA}} |
  | `{{SECURITY_CODE_DESIGN_OR_NA}}` | {{OWNED_OR_NA}} | {{EXCLUDED_OR_NA}} | {{FINDINGS_OR_NA}} |
- Context inputs: {{AREA_CONTEXT_SET_INTERFACE_REFS_AND_DESIGN_CONTEXT_SET}}
- Report path: `{{REPORT_PATH}}`

### Stop and handoff conditions

- `NEEDS_CONTEXT`: {{CONDITION}}
- `BLOCKED`: {{CONDITION}}
- `INTERFACE_CHANGED`: frozen interface identity no longer matches required behavior; controller reconciliation required.
- `DESIGN_CHANGED`: valid material design decision changed frozen contract; controller reconciliation required.
- `DESIGN_DRIFT`: implementation violates frozen design contract without valid design change.
- `DESIGN_CONTEXT_TOO_BROAD`: task-local design context cannot be preserved without hiding a required design dependency/conflict.
- `SPLIT_REQUIRED`: a second independent result or boundary appears.
- `CONTEXT_TOO_BROAD`: task-local project context cannot be preserved without hiding a required dependency.
- `RECORD_FOR_FUTURE_TASK`: an adjacent issue is found.
- `STOP_AND_RESCOPE`: cohesion fails or a blocker remains after the single fixer wave.
- `HANDOFF_REQUIRED`: {{REMOTE_OR_VISUAL_BOUNDARY_OR_NA}}

### Exact next task

On successful verification, proceed to `{{NEXT_TASK_OR_FINAL_GATE}}`.

---

## Phase/final verification

| Evidence | Command/interaction or operator | Expected result | Run once after |
| --- | --- | --- | --- |
| {{AREA_OR_INTEGRATION_CHECK}} | `{{COMMAND_OR_INTERACTION}}` | {{RESULT}} | {{TASK_OR_PHASE}} |
| {{VISUAL_DESIGN_CHECK_OR_NA}} | {{BROWSER_RENDER_OPERATOR_OR_NA}} | {{DESIGN_RESULT}} | {{UI_PHASE_OR_NA}} |

## Design impact candidates

| Durable design truth | DESIGN.md sections | Expected gate after fresh verification |
| --- | --- | --- |
| {{PERSONALITY_LAYOUT_TOKENS_COMPONENT_RESPONSIVE_A11Y_MOTION_OR_NONE}} | {{SECTIONS_OR_NONE}} | `{{DESIGN_CURRENT_DESIGN_UPDATE_REQUIRED_DESIGN_DRIFT}}` |

This predicts impact only. Controller owns Design Drift Gate and design identity reconciliation.

## Documentation impact candidates

| Durable truth | Candidate docs | Expected gate after fresh verification |
| --- | --- | --- |
| {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW_OR_NONE}} | {{PATHS_OR_NONE}} | `{{DOCS_NOT_REQUIRED_DOCS_CURRENT_DOCS_UPDATE_REQUIRED}}` |

This predicts impact only. Controller performs real documentation drift gate against verified current behavior after implementation/design reconciliation.

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
- [ ] Every task has one primary area and bounded `AREA_CONTEXT_SET`.
- [ ] Every UI task has one frozen design identity and bounded `DESIGN_CONTEXT_SET`, or explicit `DESIGN_NOT_APPLICABLE`.
- [ ] Root `DESIGN.md` exists/persists when required and authorized, or missing persistence is explicit.
- [ ] Every cross-area producer/consumer seam that can drift has one `IC-xx` contract and freeze order.
- [ ] Dependent tasks reference same interface/design identities rather than redefining them.
- [ ] Runtime dependencies identify ownership/status/log seams and do not imply process authority.
- [ ] Specialist/design roles stay inside selected agent/turn budget and existing permissions.
- [ ] Paths, interfaces, design sources and commands are inspected or in bounded discovery gate.
- [ ] Shared write paths are sequenced.
- [ ] No task mixes independent outcomes/security/design boundaries.
- [ ] Design review/visual design check are separate from technical E2E and G4.
- [ ] Permissions, budgets, reports, and stop conditions are explicit.
- [ ] Design/documentation impact candidates are identified without rewriting contracts before valid authority/evidence.
- [ ] No unresolved placeholder remains in a `PLAN_READY` artifact.
