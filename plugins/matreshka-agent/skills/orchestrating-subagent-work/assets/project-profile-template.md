# Matreshka project profile

## Identity and validity

- Project real root: `{{PROJECT_ROOT}}`
- Profile-input identity: `{{HASH_OR_REF}}`
- Created or refreshed: `{{TIMESTAMP}}`
- Owner/reviewer: `{{OWNER}}`
- Expiry or refresh condition: `{{EXPIRY}}`
- Profile status: `{{CURRENT_PARTIAL_STALE}}`

## Sources inspected

- Repository instructions: {{INSTRUCTIONS}}
- Package/workspace/CI sources: {{COMMAND_SOURCES}}
- Relevant architecture/interface sources: {{ARCHITECTURE_SOURCES}}
- Runtime/test sources: {{RUNTIME_TEST_SOURCES}}

## Project topology

| Area ID | Kind | Purpose | Roots / entry points | Produces / consumes | Data/security boundary | Status |
| --- | --- | --- | --- | --- | --- | --- |
| `{{AREA_ID}}` | {{KIND}} | {{PURPOSE}} | {{ROOTS_ENTRIES}} | {{INTERFACES}} | {{BOUNDARY}} | {{CURRENT_STALE_PARTIAL}} |

- Area count: {{COUNT}}
- Topology freshness evidence: {{EVIDENCE}}

## Area context index

| Area | Validated context sources | Required neighbor contracts/invariants | Default exclusions |
| --- | --- | --- | --- |
| `{{AREA_ID}}` | {{SOURCES}} | {{INTERFACES}} | {{EXCLUSIONS}} |

The index is routing guidance only. Revalidate paths/interfaces before task dispatch and never load all area sources by default.

## Confirmed local commands

| Purpose / area | Existing command | Source | Preconditions | Expected signal |
| --- | --- | --- | --- | --- |
| Focused test | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |
| Typecheck/lint | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |
| Build/integration | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |
| Browser E2E | `{{COMMAND_OR_NONE}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |

## Runtime map summary

| Service | Owning area | Environment | Start | Stop/ownership | Status/health | Logs | Port/socket | Separate authority required |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `{{SERVICE_ID}}` | `{{AREA_ID}}` | {{ENVIRONMENT}} | {{COMMAND_OR_NONE}} | {{COMMAND_OR_OWNERSHIP}} | {{OBSERVATION}} | {{LOG_SOURCE}} | {{PORT_OR_NONE}} | {{AUTHORITY}} |

- Runtime status: `{{CURRENT_PARTIAL_STALE_UNAVAILABLE_NOT_APPLICABLE}}`
- Unknown ownership or destructive caveat: {{DETAIL_OR_NONE}}

## Durable interface sources

| Interface | Producer | Consumers | Existing repository doc/definition | Freshness |
| --- | --- | --- | --- | --- |
| {{INTERFACE}} | `{{AREA_ID}}` | {{AREA_IDS}} | {{PATH_OR_CODE_SOURCE}} | {{CURRENT_STALE}} |

Run-specific `IC-xx` contracts remain under the run state and are not copied into this profile as task status.

## Sensitive boundaries and constraints

- Boundaries requiring higher scrutiny: {{AUTH_ISOLATION_MIGRATION_SECRETS_OR_NONE}}
- Known generated or mutation-prone paths: {{PATHS_OR_NONE}}
- Repository-specific stop conditions: {{STOP_CONDITIONS}}

## Scope

- Intended use: `validated project-local topology/context/runtime/quality-gate discovery`
- Not authoritative for: permissions, source intent, task status, remote actions, secrets, uninspected state, or changed repository facts.
- Refresh rule: any affected area/interface/runtime mismatch invalidates that subset until current evidence is inspected.
