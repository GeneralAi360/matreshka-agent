# Task {{TASK_ID}} — {{TITLE}}

## Goal

{{ONE_MEASURABLE_RESULT}}

## Project Intelligence routing

- Role archetype: `{{GENERAL_FRONTEND_BACKEND_DATA_UI_TEST_DOCS_BROWSER_OPERATOR}}`
- Primary area: `{{AREA_ID}}`
- Adjacent areas required for correctness: {{AREA_IDS_OR_NONE}}
- Cross-area interface contracts: {{IC_IDS_AND_HASHES_OR_NONE}}
- Context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`
- Included context sources: {{MINIMAL_AREA_CONTEXT_SOURCES}}
- Explicitly excluded areas/sources: {{EXCLUDED_UNRELATED_CONTEXT}}

Specialization and context routing do not grant additional authority. If a required interface/context invariant is missing, stop rather than guessing or inspecting the entire project by default.

## Inputs

- Confirmed design/spec: {{PATH_OR_NONE}}
- Existing interfaces and invariants: {{EXACT_INTERFACES}}
- Frozen interface identity when applicable: {{IC_HASH_OR_NONE}}
- Runtime dependency/observation: {{SERVICE_STATUS_LOG_OR_NONE}}
- Task baseline: {{GIT_REF_OR_HASH_SET}}

## Produces

- Interface or behavior: {{EXACT_OUTPUT_CONTRACT}}
- Acceptance criteria:
  - {{CRITERION_1}}
  - {{CRITERION_2}}
- Potential durable documentation impact: {{NONE_OR_AFFECTED_TRUTH_AND_DOC_CANDIDATE}}

## Allowed product and test files

Write only:

- `{{REAL_PATH_1}}`
- `{{REAL_PATH_2}}`

Inspect-only:

- `{{REAL_PATH_OR_SCOPE}}`

## Allowed run-state output

- Write only this role report: `{{REPORT_PATH}}`
- Optional run-owned evidence artifact: `{{EVIDENCE_PATH_OR_NONE}}`
- These outputs do not grant permission to modify product/test files outside the allowlist.

## Role-specific boundary

- Owned responsibility: {{ROLE_OWNED_RESPONSIBILITY}}
- Forbidden neighboring responsibility: {{ROLE_FORBIDDEN_RESPONSIBILITY}}
- Execution-only operator rule when applicable: execute only the exact requested action and return evidence; do not decide the follow-up action.

## Non-goals

- {{EXCLUDED_WORK_1}}
- {{EXCLUDED_WORK_2}}
- Do not redefine a frozen `IC-xx` contract. Return a material mismatch to the controller.
- Do not stage, commit, push, deploy, use secrets, install dependencies, start/stop unapproved processes, or call remote systems. Return those boundaries to the controller.
- Do not create child agents or fix adjacent issues.

## RED

- Add or identify: {{FOCUSED_FAILING_CHECK}}
- Run: `{{RED_COMMAND}}`
- Expected failure reason: {{EXPECTED_REASON}}

## GREEN

- Implement only: {{MINIMAL_CHANGE}}
- Run: `{{GREEN_COMMAND}}`
- Expected result: {{EXPECTED_RESULT}}

## Task gate

- Task suite: `{{TASK_COMMAND}}`
- Nearest regression: `{{REGRESSION_COMMAND}}`
- Targeted type/lint/diff check: `{{TARGETED_COMMAND}}`
- Cross-area contract/integration proof: {{INTERFACE_PROOF_OR_NA}}
- Evidence format: command / exit code / counts / relevant note.

## Report

Write the completed report only to `{{REPORT_PATH}}` using the agent report template. Report any observed interface mismatch, runtime ownership conflict, or durable-doc impact candidate without expanding scope.

## Stop conditions

Return the applicable status without expanding scope:

- `NEEDS_CONTEXT`: {{UNINSPECTABLE_FACT}}
- `BLOCKED`: {{MISSING_DEPENDENCY_OR_PERMISSION}}
- `INTERFACE_CHANGED`: a frozen cross-area contract no longer matches required behavior; controller reconciliation required.
- `SPLIT_REQUIRED`: more than one independent result or boundary appears.
- `CONTEXT_TOO_BROAD`: required context exceeds this task or cannot be safely routed.
- `STOP_AND_RESCOPE`: the task cannot remain one independently reviewable unit.
