# Task {{TASK_ID}} — {{TITLE}}

## Goal

{{ONE_MEASURABLE_RESULT}}

## Inputs

- Confirmed design/spec: {{PATH_OR_NONE}}
- Existing interfaces and invariants: {{EXACT_INTERFACES}}
- Task baseline: {{GIT_REF_OR_HASH_SET}}

## Produces

- Interface or behavior: {{EXACT_OUTPUT_CONTRACT}}
- Acceptance criteria:
  - {{CRITERION_1}}
  - {{CRITERION_2}}

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

## Non-goals

- {{EXCLUDED_WORK_1}}
- {{EXCLUDED_WORK_2}}
- Do not stage, commit, push, deploy, use secrets, or call remote systems. Return those boundaries to the controller.
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
- Evidence format: command / exit code / counts / relevant note.

## Report

Write the completed report only to `{{REPORT_PATH}}` using the agent report template.

## Stop conditions

Return the applicable status without expanding scope:

- `NEEDS_CONTEXT`: {{UNINSPECTABLE_FACT}}
- `BLOCKED`: {{MISSING_DEPENDENCY_OR_PERMISSION}}
- `SPLIT_REQUIRED`: more than one independent result or boundary appears.
- `CONTEXT_TOO_BROAD`: required context exceeds this task.
- `STOP_AND_RESCOPE`: the task cannot remain one independently reviewable unit.
