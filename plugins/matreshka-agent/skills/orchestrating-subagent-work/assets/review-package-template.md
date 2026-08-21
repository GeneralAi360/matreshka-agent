# Review Package — {{TASK_ID}}

## Review stage

- Stage: `{{INITIAL_OR_TARGETED_RE_REVIEW}}`
- Confirmed finding IDs for re-review: {{FINDING_IDS_OR_NONE}}
- Fix baseline: {{FIX_BASELINE_OR_NONE}}
- Fix current state: {{FIX_CURRENT_STATE_OR_NONE}}
- Covering evidence: {{COMMAND_EXIT_COUNTS_NOTE_OR_NONE}}
- Re-review boundary: only confirmed IDs, fix diff, unchanged frozen contracts/design identity, and covering evidence; `N/A` for initial review.

## Reviewer assignment

- Profile: `{{SPEED_BALANCED_QUALITY}}`
- Review role: `{{COMBINED_OR_SPEC_OR_SECURITY_CODE_OR_DESIGN_REVIEWER}}`
- Owned concerns: {{ROLE_OWNED_CONCERNS}}
- Excluded concerns: {{OTHER_REVIEWER_OWNERSHIP_OR_NONE}}
- Shared blocking rule: directly observed Critical issue returns to controller even when outside owned concern; do not expand into another reviewer's full scope.

## Review boundary

- Task brief: `{{BRIEF_PATH}}`
- Implementer report: `{{REPORT_PATH}}`
- Baseline: `{{TASK_BASE}}`
- Current state: `{{TASK_HEAD_OR_HASH_SET}}`
- Allowed diff: {{SCOPED_PATHS_OR_DIFF_ARTIFACT}}
- Excluded/pre-existing changes: {{EXCLUSIONS}}

## Project Intelligence boundary

- Primary area: `{{AREA_ID}}`
- Adjacent areas: {{AREA_IDS_OR_NONE}}
- Area context guarantee: `{{NARROW_DEGRADED_CONTEXT_TOO_BROAD}}`
- Frozen interfaces: {{IC_IDS_AND_HASHES_OR_NONE}}
- Runtime evidence needed for review: {{STATUS_LOG_OR_NONE}}

Reviewer does not load unrelated topology/profile/history merely for background.

## Design Intelligence boundary

Use only when UI/design is material.

- Design relevance: `{{DESIGN_STATUS_OR_NOT_APPLICABLE}}`
- Root design contract: `{{DESIGN_MD_PATH_OR_READY_TO_SAVE_OR_NONE}}`
- Frozen design identity/hash: `{{DESIGN_IDENTITY_OR_NONE}}`
- Design context guarantee: `{{NARROW_DEGRADED_NOT_APPLICABLE}}`
- Included `DESIGN_CONTEXT_SET`: {{DESIGN_SECTIONS_TOKENS_PATTERNS_OR_NONE}}
- Explicitly excluded design history/prototypes/screens: {{EXCLUSIONS_OR_NONE}}
- Design review required: {{YES_NO}}
- Visual evidence refs available to review: {{SAFE_SCREENSHOT_OR_RENDER_REFS_OR_NONE}}

A reviewer may not redefine root `DESIGN.md`, select a new direction, or infer design authority from screenshots. A material valid contract change goes back as `DESIGN_CHANGED`; implementation deviation is `DESIGN_DRIFT`.

## Source-intent / acceptance criteria

- Task-local U/S requirements: {{U_S_IDS_AND_SHORT_QUOTES}}
- Acceptance criteria:
  - {{CRITERION_1}}
  - {{CRITERION_2}}

Do not include full source brief for ordinary review when task-local U rows suffice.

## Verification summary supplied to reviewer

| Command/check | Exit/signal | Counts | Relevant note |
| --- | --- | --- | --- |
| `{{COMMAND_OR_CHECK}}` | {{EXIT}} | {{COUNTS}} | {{NOTE}} |

Raw logs: `{{PATH_OR_NONE}}`

## Review checklist

- Combined reviewer: source/task/spec compliance, correctness, quality, security, isolation, interfaces, tests, affected UX/design.
- Spec reviewer: requirements/non-goals/public contracts/compatibility/user-visible behavior/acceptance evidence.
- Security/code reviewer: correctness/failure/auth/isolation/leakage/secrets/state/concurrency/persistence/migrations/maintainability/test sufficiency.
- Design reviewer: frozen design identity, UX flow/wayfinding, hierarchy/layout/spacing/density, typography/color/contrast/depth, component reuse/states, responsive/touch, accessibility, purposeful motion/perceived performance, cross-screen consistency, Apple-inspired core as UX principles rather than a visual preset.

Mark N/A with reason. Do not broaden diff, rerun broad suite without missing/contradictory evidence, mutate files, launch agents, edit `IC-xx`/`DESIGN.md`, or fix findings.

Return `APPROVED`, `CHANGES_REQUIRED`, `REVIEW_BLOCKED`, or `STOP_AND_RESCOPE`. Every finding provides ID, severity, location/contract boundary, violated requirement/invariant, evidence and minimal correction boundary.
