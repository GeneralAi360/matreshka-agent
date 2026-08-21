# Implementation report — `<task ID and title>`

## Status

- Result: `<COMPLETE | PARTIALLY_VERIFIED | BLOCKED | SPLIT_REQUIRED | CONTEXT_TOO_BROAD | INTERFACE_CHANGED | DESIGN_CHANGED | DESIGN_DRIFT | STOP_AND_RESCOPE | HANDOFF_REQUIRED>`
- Project root: `<resolved root or NO_GIT_MODE>`
- Baseline/current state: `<refs or hashes>`
- Permission envelope used: `<scope and expiry>`

## Project Intelligence boundary

- Primary area: `<AREA_ID>`
- Adjacent areas: `<IDs or none>`
- Area context guarantee: `<NARROW | DEGRADED | CONTEXT_TOO_BROAD | NOT_APPLICABLE>`
- Frozen `IC-xx`: `<IDs + identities/hashes or none>`
- Runtime dependency/observation: `<service/status/log or none>`
- Interface mismatch: `<INTERFACE_CHANGED details or none>`

## Design Intelligence boundary

- Design relevance: `<DESIGN_NOT_APPLICABLE | DESIGN_CURRENT | other controller state>`
- Root design contract: `<DESIGN.md | DESIGN_READY_TO_SAVE | none>`
- Design identity/hash used: `<identity or none>`
- Design context guarantee: `<NARROW | DEGRADED | NOT_APPLICABLE>`
- `DESIGN_CONTEXT_SET`: `<sections/tokens/patterns supplied or none>`
- Design role boundary: `<UI/FRONTEND/GENERAL + forbidden neighboring responsibility>`
- Design observation: `<preserved / DESIGN_CHANGED / DESIGN_DRIFT / none>`

## Scope

- Completed: `<acceptance results>`
- Not completed: `<remaining results>`
- Changed files: `<exact paths>`
- Pre-existing dirty files left untouched: `<paths or none>`
- Contract/state files unexpectedly changed: `<IC/DESIGN/prototype/lockfile/generated paths or none>`

## Focused cycle

### RED

- Command: `<command>`
- State: `<baseline/current ref/hash>`
- Exit code: `<code>`
- Counts: `<passed / failed / skipped>`
- Expected failure reason: `<reason>`

### GREEN

- Command: `<same focused command>`
- State: `<current ref/hash>`
- Exit code: `<code>`
- Counts: `<passed / failed / skipped>`
- Relevant note: `<what now works>`

### Exception, if any

- Reason: `<why executable RED unavailable>`
- Alternate check: `<check and result>`
- Remaining verifier: `<operator/design visual checker/none>`

## Task gate

| Command / evidence | State | Exit code/signal | Counts | Relevant note |
| --- | --- | ---: | --- | --- |
| `<focused suite>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |
| `<nearby regression>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |
| `<targeted static/diff check>` | `<ref/hash>` | `<code>` | `<counts>` | `<note>` |
| `<IC integration proof or N/A>` | `<state>` | `<signal>` | `<counts>` | `<note>` |
| `<task-local accessibility/design check or N/A>` | `<state>` | `<signal>` | `<counts>` | `<note>` |

Independent Design Review / Visual Design Check are **not** claimed from this implementer report.

## Security evidence

- Selected `S-` requirements: `<IDs or none>`
- Negative proof implemented/run: `<evidence or none>`
- Residual security blocker: `<detail or none>`

## Design / documentation impact candidates

- Durable design truth changed legitimately: `<yes/no + DESIGN_CHANGED candidate>`
- Implementation appears to drift from frozen design: `<DESIGN_DRIFT evidence or none>`
- Candidate root `DESIGN.md` update: `<required/none; controller decides and authorizes>`
- Durable non-design documentation truth changed: `<interface/topology/runtime/data/security/env/workflow or none>`
- Candidate docs: `<paths or none>`

These are candidates only. Controller owns Design Drift Gate and Documentation Drift Gate.

## Handoff

- Assumptions: `<list or none>`
- Pre-existing failures: `<evidence or none>`
- Adjacent findings: `<RECORD_FOR_FUTURE_TASK items or none>`
- Permissions still required: `<actions or none>`
- Concerns/evidence gaps: `<list or none>`
- Exact next action: `<controller action>`
