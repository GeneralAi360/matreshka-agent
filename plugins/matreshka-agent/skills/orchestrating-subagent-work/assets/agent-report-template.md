# Agent Report — {{TASK_ID}} / {{ROLE}}

- Status: `{{STATUS}}`
- Stable thread ID: `{{THREAD_ID}}`
- Task baseline: `{{BASELINE}}`
- Current state or commit: `{{CURRENT_STATE}}`

## Scope completed

- {{COMPLETED_ITEM}}

## Scope not completed

- {{INCOMPLETE_ITEM_OR_NONE}}

## Files changed or reviewed

- `{{PATH_OR_DIFF_RANGE}}` — {{CHANGE_OR_REVIEW_NOTE}}

## Evidence

| Command/check | Exit | Counts | Relevant note |
| --- | --- | --- | --- |
| `{{COMMAND}}` | {{EXIT_CODE}} | {{COUNTS}} | {{NOTE}} |

## Findings

| Severity | Location | Requirement | Evidence | Minimal boundary |
| --- | --- | --- | --- | --- |
| {{CRITICAL_IMPORTANT_MINOR_OR_NONE}} | {{LOCATION}} | {{REQUIREMENT}} | {{EVIDENCE}} | {{BOUNDARY}} |

## Concerns and assumptions

- Assumptions: {{ASSUMPTIONS_OR_NONE}}
- Pre-existing failures: {{PRE_EXISTING_OR_NONE}}
- Adjacent issues not changed: {{ADJACENT_OR_NONE}}
- Permission still needed: {{PERMISSION_OR_NONE}}

## Exact next action

{{ONE_BOUNDED_ACTION}}
