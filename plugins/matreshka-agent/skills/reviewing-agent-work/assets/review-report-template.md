# Review report — `<task ID and title>`

## Decision

`<APPROVED | CHANGES_REQUIRED | REVIEW_BLOCKED | STOP_AND_RESCOPE>`

- Review role: `<COMBINED | SPEC | SECURITY_CODE | DESIGN_REVIEWER>`
- Reviewed baseline/current state: `<refs or hashes>`
- Reviewed files/diff range: `<exact scope>`
- Review integrity: `<technical read-only | immutable package | DEGRADED_MODE reason>`
- Evidence relied on: `<commands/state/visual refs>`
- Checks rerun: `<focused checks and reason, or none>`
- Completed review scope: `<criteria and owned concerns checked>`
- Incomplete review scope: `<unreviewed required concern or none>`
- Product/test files changed: `none`
- Pre-existing failures/dirty files: `<list or none>`

## Project Intelligence reviewed

- Primary area: `<AREA_ID or N/A>`
- Area context guarantee: `<NARROW | DEGRADED | N/A>`
- Frozen `IC-xx` identities: `<IDs/hashes or none>`
- Interface compatibility verdict: `<PRESERVED | DRIFT | UNCHECKABLE | N/A>`
- Runtime boundary observation: `<evidence/caveat or none>`

## Design Intelligence reviewed

- Design relevance: `<DESIGN_CURRENT | DESIGN_READY_TO_SAVE | other | N/A>`
- Root `DESIGN.md`: `<path or ready-to-save or none>`
- Frozen design identity/hash: `<identity or none>`
- Design context guarantee: `<NARROW | DEGRADED | N/A>`
- Design review evidence type: `<code + contract | rendered visual + contract | DEGRADED | N/A>`
- Design consistency verdict: `<PASS | FINDINGS | UNCHECKABLE | N/A>`
- Design change/drift signal: `<none | DESIGN_CHANGED | DESIGN_DRIFT | DESIGN_CONFLICT>`

## Blocking findings

### `<ID>` — `<Critical | Important>` — `<short title>`

- Location: `<file:line, IC boundary, DESIGN.md invariant, or rendered state>`
- Evidence: `<observable fact>`
- Impact: `<security, user, data, interface, design, accessibility, acceptance consequence>`
- Acceptance/invariant: `<violated U/S/IC/design requirement>`
- Required condition: `<minimum outcome needed>`
- Confidence/counterevidence: `<assessment>`

## Minor findings

- `<ID / location / evidence / improvement>`

## Adjacent findings

- `RECORD_FOR_FUTURE_TASK: <issue and evidence>`

## Coverage summary

| Acceptance/risk/design invariant | Diff/evidence checked | Result |
| --- | --- | --- |
| `<criterion>` | `<location, command, screenshot/render>` | `<pass/fail/unknown>` |

## Review dimensions

| Dimension | Result | Evidence or N/A reason |
| --- | --- | --- |
| Source intent / specification / correctness | `<checked/N/A>` | `<evidence>` |
| Project area ownership/context | `<checked/N/A>` | `<evidence>` |
| Frozen `IC-xx` / public compatibility | `<checked/N/A>` | `<evidence>` |
| Input validation/error/side effects | `<checked/N/A>` | `<evidence>` |
| Authorization/isolation/leakage/secrets | `<checked/N/A>` | `<evidence>` |
| Concurrency/retry/idempotency | `<checked/N/A>` | `<evidence>` |
| Persistence/migration/rollback | `<checked/N/A>` | `<evidence>` |
| Test sufficiency | `<checked/N/A>` | `<evidence>` |
| Maintainability/repository conventions | `<checked/N/A>` | `<evidence>` |
| UX flow / wayfinding / hierarchy | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Layout / spacing / density | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Typography / color / contrast / depth | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Component reuse / interaction states | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Responsive / touch / focus / accessibility | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Motion / perceived performance / reduced motion | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Cross-screen consistency / frozen `DESIGN.md` | `<checked/N/A/UNCHECKABLE>` | `<evidence>` |
| Apple-inspired core principles where applicable | `<checked/N/A/UNCHECKABLE>` | `<purpose/agency/etc evidence>` |

A design review that cannot observe a material visual property says `UNCHECKABLE`; it does not approve by taste inference from code alone.

## Controller handoff

- Confirmed findings for consolidated fix: `<IDs or none>`
- Interface reconciliation required: `<INTERFACE_CHANGED details or none>`
- Design reconciliation required: `<DESIGN_CHANGED / DESIGN_DRIFT / DESIGN_CONFLICT / none>`
- Disputed findings needing adjudication: `<IDs or none>`
- Assumptions: `<list or none>`
- Concerns/evidence limitations: `<list or none>`
- Permissions/evidence still needed: `<list or none>`
- Exact next action: `<single controller action>`
