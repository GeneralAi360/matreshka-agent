# Implementation Plan — {{TITLE}}

- Status: `{{DRAFT_OR_READY}}`
- Confirmed design: `{{DESIGN_PATH_OR_REFERENCE}}`
- Project root: `{{REAL_PROJECT_ROOT}}`
- Baseline: `{{GIT_REF_OR_NO_GIT_BASELINE}}`
- Applicable instructions: {{INSTRUCTION_PATHS}}
- Recommended execution profile: `{{SPEED_BALANCED_QUALITY}}`
- Permission/remote boundary: {{BOUNDARY_SUMMARY}}

## Goal

{{ONE_OVERALL_OUTCOME}}

## Non-goals

- {{EXCLUDED_OUTCOME}}

## Constraints and pre-existing state

- {{CONSTRAINT_OR_EXISTING_FAILURE}}

## Coverage matrix

| Requirement ID | Requirement/source | Task | Verification evidence | Negative/rollback evidence |
| --- | --- | --- | --- | --- |
| `R1` | {{REQUIREMENT}} | `T1` | {{CHECK}} | {{NEGATIVE_OR_NA}} |

## Task map

| Task | Result | Depends on | Primary boundary | Write paths | Risk/tier |
| --- | --- | --- | --- | --- | --- |
| `T1` | {{RESULT}} | {{DEPENDENCY_OR_NONE}} | {{BOUNDARY}} | {{PATHS}} | {{RISK_TIER}} |

## Shared execution policy

- Writing agents: sequential in one checkout.
- Child agents: forbidden.
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

### Inputs

- Existing interfaces: {{EXACT_INTERFACES}}
- Required design section: {{SECTION_REFERENCE}}
- Task baseline: {{BASELINE}}

### Produces

- {{EXACT_INTERFACE_OR_BEHAVIOR}}

### Allowed files

Write only:

- `{{REAL_PATH}}`

Inspect-only:

- `{{REAL_PATH_OR_SCOPE}}`

### Non-goals and forbidden actions

- {{NON_GOAL}}
- No child agents or adjacent fixes.
- No Git, network, secret, deploy, migration application, or remote action. Controller-owned boundary or handoff: {{CONTROLLER_ACTION_OR_NONE}}.

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
- Conditional build/scan: {{COMMAND_OR_NA_WITH_REASON}}
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
- Context inputs: {{BRIEF_INTERFACES_PATHS_ONLY}}
- Report path: `{{REPORT_PATH}}`

### Stop and handoff conditions

- `NEEDS_CONTEXT`: {{CONDITION}}
- `BLOCKED`: {{CONDITION}}
- `SPLIT_REQUIRED`: a second independent result or boundary appears.
- `CONTEXT_TOO_BROAD`: task-local context cannot be preserved.
- `RECORD_FOR_FUTURE_TASK`: an adjacent issue is found.
- `STOP_AND_RESCOPE`: cohesion fails or a blocker remains after the single fixer wave.
- `HANDOFF_REQUIRED`: {{REMOTE_BOUNDARY_OR_NA}}

### Exact next task

On successful verification, proceed to `{{NEXT_TASK_OR_FINAL_GATE}}`.

---

## Phase/final verification

| Evidence | Command or operator | Expected result | Run once after |
| --- | --- | --- | --- |
| {{INTEGRATION_CHECK}} | `{{COMMAND}}` | {{RESULT}} | {{TASK_OR_PHASE}} |

## Remote handoff

- Local operator: {{LOCAL_OPERATOR}}
- Remote operator/system: {{REMOTE_OPERATOR_AND_SYSTEM_OR_NA}}
- Allowed preparation: {{PREPARATION}}
- Forbidden execution: {{FORBIDDEN_REMOTE_ACTION}}
- Final local status: `{{COMPLETE_PARTIAL_HANDOFF}}`

## Plan validation

- [ ] Every requirement maps to task and evidence.
- [ ] Every task maps to a requirement or justified enabling step.
- [ ] Paths, interfaces, and commands are inspected or in a bounded discovery gate.
- [ ] Shared write paths are sequenced.
- [ ] No task mixes independent outcomes or security boundaries.
- [ ] Permissions, budgets, reports, and stop conditions are explicit.
- [ ] No unresolved placeholder remains in a `PLAN_READY` artifact.
