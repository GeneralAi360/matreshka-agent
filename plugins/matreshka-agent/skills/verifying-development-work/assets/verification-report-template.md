# Verification report — <task, phase, or branch>

## Verdict

- Technical/security status: `<VERIFIED | PARTIALLY_VERIFIED | FAILED | BLOCKED | HANDOFF_REQUIRED>`
- Verified state: `<project root and exact ref/hashes>`
- Verification tier: `<focused | task gate | phase/final>`
- Permission envelope used: `<scope and expiry>`
- Review blockers: `<none or unresolved IDs>`
- Completed verification scope: `<criteria proved>`
- Incomplete verification scope: `<criteria not proved or none>`
- Product/test/design-contract files changed by verifier: `none`
- Paths/diff range verified: `<exact scope>`
- Progress/ledger/repository reconciliation: `<MATCH | MISMATCH | NOT_APPLICABLE + summary>`
- Unresolved acceptance-critical placeholders: `<items or none>`
- Required security negative proofs: `<proved / failed / not run rows>`
- Exact non-complete verdict reason: `<required when not VERIFIED, or none>`

## Project Intelligence evidence

- Affected/current areas: `<AREA IDs or N/A>`
- Frozen `IC-xx` identities: `<IDs/hashes or none>`
- Area-local proof: `<commands/evidence>`
- Cross-area integration proof: `<commands/evidence or N/A>`
- Runtime identity/health/ownership evidence: `<evidence/caveat or N/A>`

## Technical/security acceptance matrix

| Claim | Verification | Exit code/counts | Result | Relevant note |
| --- | --- | --- | --- | --- |
| `<criterion>` | `<command/inspection>` | `<code; pass/fail/skip>` | `<proved/failed/unverified>` | `<note>` |

## Automated Browser E2E, if applicable

- Browser relevance: `<YES | NO | NOT_APPLICABLE>`
- Framework: `<Playwright | Cypress | Selenium | WebdriverIO | other | none>`
- Mode: `<PLAYWRIGHT_MANAGED | CHROME_CDP | HOST_BROWSER_TOOL | other | UNAVAILABLE>`
- Isolated context: `<YES | NO | DEGRADED | N/A>`
- Exact command: `<command or none>`
- Exit: `<code or none>`
- Counts: `<passed / failed / skipped or unavailable>`
- Console/network summary: `<safe summary or unavailable>`
- Evidence refs: `<screenshots/trace/video/report or none>`
- Unexpected mutation: `<paths or none>`
- Status: `<PASS | FAIL | NOT_RUN | BLOCKED | NOT_APPLICABLE>`

Automated E2E proves repository-declared browser behavior only. It does not imply visual-design or G4 acceptance.

## Visual Design Check, if applicable

- Design relevance/status: `<DESIGN_CURRENT | DESIGN_READY_TO_SAVE | other | NOT_APPLICABLE>`
- Root `DESIGN.md`: `<path / ready-to-save / none>`
- Frozen design identity/hash: `<identity or none>`
- Visual capability: `<browser/native render capability + isolation or UNAVAILABLE>`
- Viewports/states checked: `<desktop/tablet/mobile + loading/error/empty/etc>`
- UX flow/wayfinding evidence: `<safe refs/signals>`
- Layout/spacing/density: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Typography/color/contrast/depth: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Components/states consistency: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Responsive/touch/accessibility: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Motion/reduced-motion/perceived performance: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Cross-screen consistency: `<PASS/FAIL/UNCHECKABLE + evidence>`
- Apple-inspired core conflicts: `<none / findings; no visual-preset assumption>`
- Safe evidence refs: `<screenshots/visual report or none>`
- `DESIGN_VERIFICATION`: `<PASS | PARTIAL | FAIL | BLOCKED | UNCHECKABLE | NOT_APPLICABLE>`

A required material visual property that cannot be observed is `UNCHECKABLE`, not assumed PASS. Visual Design Check never edits code, `DESIGN.md` or prototypes.

## State integrity

- State before checks: `<status/hashes>`
- State after checks: `<status/hashes>`
- Unexpected generated changes: `<paths or none>`
- Pre-existing dirty files preserved: `<paths or none>`
- Frozen interface/design identities unchanged during verification: `<yes/no + evidence>`

## Progress, placeholder and design truth

| Item | Source | Acceptance impact | Current evidence | Resolution owner/status |
| --- | --- | --- | --- | --- |
| `<progress mismatch, assumption, placeholder, design identity mismatch, provider fact>` | `<progress/ledger/repo/spec/DESIGN.md>` | `<critical/optional>` | `<evidence>` | `<controller/user/operator; status>` |

## Failure attribution

| Failure | Current evidence | Baseline evidence | Attribution |
| --- | --- | --- | --- |
| `<failure>` | `<result>` | `<result or unavailable>` | `<task-owned/pre-existing/unresolved/environment>` |

## Blind G4 handoff boundary

G4 is a **separate fresh acceptance context**. This technical/visual report must not be supplied to the G4 checker. G4 receives source brief + actual product + permitted observations only and is forbidden from reading specification, U manifest, plan/tasks, Project Intelligence, `DESIGN.md`, prototypes, this verification report, design review/visual reports, progress/dashboard or completion claims.

## Gaps and controller handoff

- Skipped/unavailable technical checks: `<list/reason>`
- Skipped/unavailable Browser E2E: `<reason or none>`
- Skipped/unavailable Visual Design Check: `<reason or none>`
- Unverified claims: `<list or none>`
- Interface mismatch: `<INTERFACE_CHANGED evidence or none>`
- Design mismatch: `<DESIGN_CHANGED | DESIGN_DRIFT | DESIGN_CONFLICT | none>`
- External verification: `<operator / target / action / expected result / stop policy>`
- Assumptions: `<list or none>`
- Concerns/evidence limitations: `<list or none>`
- Permissions still required: `<list or none>`
- Exact next action: `<single controller action>`
