# Matreshka Project Intelligence — {{RUN_ID}}

- Status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE}}`
- Project root: `{{PROJECT_ROOT}}`
- Baseline/current identity: `{{BASELINE_OR_HASH}}`
- Updated at: `{{TIMESTAMP_ISO8601}}`
- Refresh condition: {{REFRESH_CONDITION}}

## Project topology

| Area ID | Kind | Purpose | Roots / entry points | Commands/source | Produces | Consumes | Data/security boundary | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{AREA_ID}}` | {{KIND}} | {{PURPOSE}} | {{ROOTS_ENTRIES}} | {{COMMANDS_SOURCE}} | {{INTERFACES}} | {{INTERFACES}} | {{BOUNDARY}} | {{CURRENT_STALE_PARTIAL}} |

- Area count: {{COUNT}}
- Affected areas for current run: {{AREA_IDS}}
- Current primary area: `{{AREA_ID_OR_NONE}}`

## Area context index

| Area | Validated sources | Neighbor contracts/invariants | Default exclusions | Freshness |
| --- | --- | --- | --- | --- |
| `{{AREA_ID}}` | {{SOURCES}} | {{INTERFACES}} | {{EXCLUSIONS}} | {{CURRENT_STALE}} |

## Cross-area interfaces

| Contract | Source requirements | Producer | Consumers | Identity/hash | Status | Proof |
| --- | --- | --- | --- | --- | --- | --- |
| `IC-01` | {{U_S_IDS}} | `{{AREA_ID}}` | {{AREA_IDS}} | `{{HASH}}` | {{DRAFT_FROZEN_CHANGED_VERIFIED}} | {{EVIDENCE_OR_PENDING}} |

- Interface directory: `{{RUN_INTERFACE_DIR_OR_INLINE}}`
- Contract conflict/drift: {{CONFLICT_OR_NONE}}

## Runtime map

| Service | Area | Environment | Start | Stop/ownership | Status/health | Logs | Port/socket | Required authority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{SERVICE_ID}}` | `{{AREA_ID}}` | {{LOCAL_TEST_LOCAL_DEV_STAGING_PRODUCTION_UNKNOWN}} | {{COMMAND_OR_NONE}} | {{COMMAND_OR_OWNERSHIP}} | {{OBSERVATION}} | {{LOG_SOURCE}} | {{PORT_OR_NONE}} | {{PERMISSIONS}} |

- Runtime-map status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE_NOT_APPLICABLE}}`
- Unknown process ownership: {{DETAIL_OR_NONE}}

## Current task context routing

- Task: `{{TASK_ID_OR_NONE}}`
- Primary area: `{{AREA_ID_OR_NONE}}`
- Adjacent areas: {{AREA_IDS_OR_NONE}}
- Interface contracts: {{IC_IDS_OR_NONE}}
- Included context sources: {{SOURCES}}
- Explicitly excluded areas/sources: {{EXCLUSIONS}}
- Context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`

## Specialist routing

- Selected archetype: `{{ROLE_ARCHETYPE_OR_NONE}}`
- Why specialization is useful: {{RATIONALE_OR_NONE}}
- Existing Matreshka skill used: `{{SKILL_NAME}}`
- Additional permissions granted by specialization: `NONE`
- Role/turn budget impact: {{WITHIN_EXISTING_BUDGET}}

## Documentation drift

- State: `{{DOCS_NOT_REQUIRED_DOCS_CURRENT_DOCS_UPDATE_REQUIRED_DOCS_BLOCKED_DOCS_CONFLICT_PENDING}}`
- Durable truths changed: {{INTERFACE_TOPOLOGY_RUNTIME_DATA_SECURITY_ENV_WORKFLOW_OR_NONE}}
- Candidate affected docs: {{PATHS_OR_NONE}}
- Docs updated after verification: {{PATHS_OR_NONE}}
- Evidence/current-state source: {{EVIDENCE}}
- Missing authority/conflict: {{DETAIL_OR_NONE}}

## Safety notes

- This file is run-state context, not permission or verification evidence by itself.
- Revalidate repository facts before reuse after baseline/current-state changes.
- Do not include secret values, environment contents, raw logs, private URLs, personal data, browser-session data, or hidden reasoning.
