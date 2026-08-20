# Agent Report — {{TASK_ID}} / {{ROLE}}

- Status: `{{STATUS}}`
- Stable thread ID: `{{THREAD_ID}}`
- Role archetype: `{{ROLE_ARCHETYPE}}`
- Primary area: `{{AREA_ID}}`
- Cross-area contracts: {{IC_IDS_AND_HASHES_OR_NONE}}
- Project-context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`
- Design relevance: `{{DESIGN_NOT_APPLICABLE_CURRENT_RECON_DIRECTION_BLOCKED}}`
- Design identity: `{{DESIGN_IDENTITY_OR_NONE}}`
- Design-context guarantee: `{{NARROW_DEGRADED_DESIGN_CONTEXT_TOO_BROAD_NOT_APPLICABLE}}`
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

## Design observations

- Frozen design identity preserved: {{YES_NO_NA_WITH_EVIDENCE}}
- Design mismatch/drift: {{DETAIL_OR_NONE}}
- Valid design decision changed during task: {{DETAIL_OR_NONE}}
- Shared component/design-system reuse: {{EVIDENCE_OR_NA}}
- Responsive/accessibility/motion concerns: {{DETAIL_OR_NONE}}
- Visual evidence/capability limitation: {{DETAIL_OR_NONE}}

A role report may observe design drift/change but cannot edit `DESIGN.md`, declare a new design identity, or widen design/product authority by itself.

## Evidence

| Command/check/interaction | Exit/signal | Counts | Relevant note |
| --- | --- | --- | --- |
| `{{COMMAND_OR_INTERACTION}}` | {{EXIT_OR_SIGNAL}} | {{COUNTS}} | {{NOTE}} |

## Findings

| Severity | Location | Requirement/design invariant | Evidence | Minimal boundary |
| --- | --- | --- | --- | --- |
| {{CRITICAL_IMPORTANT_MINOR_OR_NONE}} | {{LOCATION}} | {{REQUIREMENT}} | {{EVIDENCE}} | {{BOUNDARY}} |

## Design impact candidate

- Durable design truth changed: {{PERSONALITY_LAYOUT_TOKENS_COMPONENT_RESPONSIVE_A11Y_MOTION_OR_NONE}}
- Candidate `DESIGN.md` sections: {{SECTIONS_OR_NONE}}
- Candidate state: {{NONE_DESIGN_CHANGED_DESIGN_UPDATE_REQUIRED_DESIGN_DRIFT}}
- This is a candidate only; the controller owns design authority, identity reconciliation and the final Design Drift Gate.

## Documentation impact candidate

- Durable truth changed: {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW_OR_NONE}}
- Candidate docs: {{PATHS_OR_NONE}}
- This is a candidate only; the controller runs the post-verification documentation drift gate.

## Concerns and assumptions

- Assumptions: {{ASSUMPTIONS_OR_NONE}}
- Pre-existing failures/design debt: {{PRE_EXISTING_OR_NONE}}
- Adjacent issues not changed: {{ADJACENT_OR_NONE}}
- Permission still needed: {{PERMISSION_OR_NONE}}

## Exact next action

{{ONE_BOUNDED_ACTION}}
