# Agent Report — {{TASK_ID}} / {{ROLE}}

- Status: `{{STATUS}}`
- Stable thread ID: `{{THREAD_ID}}`
- Role archetype: `{{ROLE_ARCHETYPE}}`
- Primary area: `{{AREA_ID}}`
- Cross-area contracts: {{IC_IDS_AND_HASHES_OR_NONE}}
- Context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`
- Task baseline: `{{BASELINE}}`
- Current state or commit: `{{CURRENT_STATE}}`

## Scope completed

- {{COMPLETED_ITEM}}

## Scope not completed

- {{INCOMPLETE_ITEM_OR_NONE}}

## Files changed or reviewed

- `{{PATH_OR_DIFF_RANGE}}` — {{CHANGE_OR_REVIEW_NOTE}}

## Interface/runtime observations

- Frozen interface contract preserved: {{YES_NO_NA_WITH_EVIDENCE}}
- Interface mismatch requiring controller reconciliation: {{DETAIL_OR_NONE}}
- Runtime ownership/status issue: {{DETAIL_OR_NONE}}

## Evidence

| Command/check | Exit | Counts | Relevant note |
| --- | --- | --- | --- |
| `{{COMMAND}}` | {{EXIT_CODE}} | {{COUNTS}} | {{NOTE}} |

## Findings

| Severity | Location | Requirement | Evidence | Minimal boundary |
| --- | --- | --- | --- | --- |
| {{CRITICAL_IMPORTANT_MINOR_OR_NONE}} | {{LOCATION}} | {{REQUIREMENT}} | {{EVIDENCE}} | {{BOUNDARY}} |

## Documentation impact candidate

- Durable truth changed: {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW_OR_NONE}}
- Candidate docs: {{PATHS_OR_NONE}}
- This is a candidate only; the controller runs the post-verification documentation drift gate.

## Concerns and assumptions

- Assumptions: {{ASSUMPTIONS_OR_NONE}}
- Pre-existing failures: {{PRE_EXISTING_OR_NONE}}
- Adjacent issues not changed: {{ADJACENT_OR_NONE}}
- Permission still needed: {{PERMISSION_OR_NONE}}

## Exact next action

{{ONE_BOUNDED_ACTION}}
