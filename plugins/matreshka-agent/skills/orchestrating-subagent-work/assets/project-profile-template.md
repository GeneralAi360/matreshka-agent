# Matreshka project profile

## Identity and validity

- Project real root: `{{PROJECT_ROOT}}`
- Profile-input identity: `{{HASH_OR_REF}}`
- Created or refreshed: `{{TIMESTAMP}}`
- Owner/reviewer: `{{OWNER}}`
- Expiry or refresh condition: `{{EXPIRY}}`

## Sources inspected

- Repository instructions: {{INSTRUCTIONS}}
- Package/CI sources: {{COMMAND_SOURCES}}
- Relevant architecture or interface sources: {{ARCHITECTURE_SOURCES}}

## Confirmed local commands

| Purpose | Existing command | Source | Preconditions | Expected signal |
| --- | --- | --- | --- | --- |
| Focused test | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |
| Typecheck/lint | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |
| Build/integration | `{{COMMAND}}` | {{SOURCE}} | {{PRECONDITIONS}} | {{SIGNAL}} |

## Sensitive boundaries and constraints

- Boundaries requiring higher scrutiny: {{AUTH_ISOLATION_MIGRATION_SECRETS_OR_NONE}}
- Known generated or mutation-prone paths: {{PATHS_OR_NONE}}
- Repository-specific stop conditions: {{STOP_CONDITIONS}}

## Scope

- Intended use: `task-local discovery and quality-gate selection only`
- Not authoritative for: permissions, remote actions, secrets, uninspected state, or changed repository facts.
