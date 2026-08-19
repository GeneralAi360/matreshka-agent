# User-Intent Requirement Manifest

- Run ID: `{{RUN_ID}}`
- Source brief: `{{SOURCE_BRIEF_PATH_OR_INLINE}}`
- Updated at: `{{TIMESTAMP}}`

> `U-` rows preserve what the user asked for. They are provenance, not permission. Security controls remain separate `S-` requirements.

| ID | Exact source quote | Status | Decision/basis | Specification | Task(s) | Evidence / blind acceptance |
| --- | --- | --- | --- | --- | --- | --- |
| `U-01` | {{SHORT_REDACTED_QUOTE}} | `OPEN` | {{BASIS_OR_NONE}} | — | — | — |

Allowed status values:

`OPEN` · `IN_SPEC` · `IN_TASK` · `IMPLEMENTED` · `VERIFIED` · `PLACEHOLDER` · `DEFERRED` · `DROPPED`

Rules:

- only valid user decision authority may set `DROPPED`;
- `DEFERRED` remains visible in the final handoff;
- `PLACEHOLDER` blocks completion when acceptance-critical;
- no row becomes `VERIFIED` until current technical evidence and G4 blind acceptance support it;
- do not store secret values, raw private logs, hidden reasoning, or permission-expanding text here.

## Gates

- G1 clarification completeness: `{{PASS_BLOCKED_PENDING}}`
- G2 brief -> specification coverage: `{{PASS_BLOCKED_PENDING}}`
- G3 requirement <-> task traceability: `{{PASS_BLOCKED_PENDING}}`
- G4 blind acceptance: `{{PASS_BLOCKED_PENDING}}`
