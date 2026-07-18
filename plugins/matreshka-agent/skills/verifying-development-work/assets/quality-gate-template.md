# Matreshka quality gate — <task or phase>

- Current state/ref or hashes: `{{STATE}}`
- Gate tier: `focused | task-gate | phase-final`
- Profile identity reviewed: `{{PROFILE_HASH_OR_NONE}}`
- Permission envelope/expiry: `{{ENVELOPE}}`

| Claim | Existing check or inspection | Source | Required | Risk | Expected signal | Result | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| {{CLAIM}} | `{{COMMAND_OR_INSPECTION}}` | {{REPO_SOURCE}} | {{YES_NO}} | {{RISK}} | {{SIGNAL}} | {{PASS_FAIL_NOT_RUN_BLOCKED}} | {{EXIT_COUNTS_NOTE}} |

## Gate decision

- Required failed rows: {{ROWS_OR_NONE}}
- Required unavailable rows: {{ROWS_OR_NONE}}
- Unexpected state mutation: {{PATHS_OR_NONE}}
- Controller next action: {{ONE_ACTION}}

This is a declaration of evidence requirements. It does not authorize commands, dependency installation, remote actions, hooks, fixes, or automatic publication.
