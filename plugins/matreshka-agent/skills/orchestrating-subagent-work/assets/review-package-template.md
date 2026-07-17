# Review Package — {{TASK_ID}}

## Review stage

- Stage: `{{INITIAL_OR_TARGETED_RE_REVIEW}}`
- Confirmed finding IDs for re-review: {{FINDING_IDS_OR_NONE}}
- Fix baseline: {{FIX_BASELINE_OR_NONE}}
- Fix current state: {{FIX_CURRENT_STATE_OR_NONE}}
- Covering evidence: {{COMMAND_EXIT_COUNTS_NOTE_OR_NONE}}
- Re-review boundary: only the confirmed IDs, fix diff, and covering evidence above; `N/A` for an initial review.

## Reviewer assignment

- Profile: `{{SPEED_BALANCED_QUALITY}}`
- Review role: `{{COMBINED_OR_SPEC_OR_SECURITY_CODE}}`
- Owned concerns: {{ROLE_OWNED_CONCERNS}}
- Excluded concerns: {{OTHER_REVIEWER_OWNERSHIP_OR_NONE}}
- Shared blocking rule: report any directly observed Critical issue to the controller even when it crosses the assigned concern; do not expand into the other reviewer's full scope.

## Review boundary

- Task brief: `{{BRIEF_PATH}}`
- Implementer report: `{{REPORT_PATH}}`
- Baseline: `{{TASK_BASE}}`
- Current state: `{{TASK_HEAD_OR_HASH_SET}}`
- Allowed diff: {{SCOPED_PATHS_OR_DIFF_ARTIFACT}}
- Excluded/pre-existing changes: {{EXCLUSIONS}}

## Acceptance criteria

- {{CRITERION_1}}
- {{CRITERION_2}}

## Verification summary

| Command | Exit | Counts | Relevant note |
| --- | --- | --- | --- |
| `{{COMMAND}}` | {{EXIT}} | {{COUNTS}} | {{NOTE}} |

Raw logs: `{{PATH_OR_NONE}}`

## Review checklist

- Combined reviewer: brief/spec compliance, correctness, quality, security, isolation, leakage, tests, and affected user experience.
- Spec reviewer: requirements, non-goals, public contracts, compatibility, user-visible behavior, and acceptance evidence.
- Security/code reviewer: correctness, failure behavior, authorization, isolation, leakage, secrets, state/concurrency, persistence/migrations, maintainability, and test sufficiency.

Mark an item `N/A` with a reason. Do not broaden the diff, rerun a broad suite without missing or contradictory evidence, mutate files, launch agents, or fix findings.

Return `APPROVED` or one consolidated `CHANGES_REQUIRED` list. For each finding provide severity, location, violated requirement, evidence, and minimal correction boundary.
