# Profiles and Budgets

Choose execution rigor from risk. Choose autonomy separately.

## Risk routing

Treat these signals as high risk: authentication, authorization, tenant or organization isolation, row-level security, destructive or data-transforming migrations, payments, secrets, provider credentials, persistence guarantees, production configuration, and irreversible remote actions.

Treat documentation, fixtures, serializers, pure deterministic functions, small type changes, and safe local tests as low risk when they do not alter a public or security contract.

Route everything else to balanced execution unless evidence justifies another profile.

## Maximum speed

Use for bounded low-risk work with clear acceptance criteria.

```text
implementer -> controller verification -> optional reviewer
```

- Unique agents per task: one implementer; at most one reviewer.
- Agent turns per task: at most four if a reviewer and fix are needed.
- Fix waves: one, using the same implementer thread when resume exists.
- Re-review: omit for Minor-only changes when controller verification covers the change.
- Prohibit for high-risk boundaries.

Escalate to balanced before dispatch if a public contract, persistence behavior, or security boundary appears.

## Balanced

Use by default.

```text
implementer -> combined reviewer -> same implementer fixes -> same reviewer rechecks
```

- Unique agents per task: at most two.
- Agent turns per task: at most four.
- Fix waves: exactly zero or one.
- Review: one combined pass covering brief, correctness, quality, security, isolation, leakage, tests, and UI experience when applicable.
- Repeat Critical or Important after the fix: `STOP_AND_RESCOPE`.

Require same-thread follow-up for the fix and re-review. If resume is unavailable, declare `DEGRADED_MODE`. For a low-risk task, the controller may apply one small consolidated correction and perform controller verification, clearly stating that no independent re-review occurred. For high-risk work, return `HANDOFF_REQUIRED`.

## Maximum quality

Use for high-risk code or production handoff.

```text
implementer -> spec reviewer + security/code reviewer -> same implementer fixes -> each reviewer rechecks own findings
```

- Unique agents per task: at most three.
- Agent turns per task: at most six.
- Fix waves: exactly zero or one consolidated wave.
- Reviewers: two independent read-only roles; parallel execution is allowed only with immutable or technically read-only packages.
- Re-review: each original reviewer checks only its confirmed findings once.
- Repeat Critical or Important: `STOP_AND_RESCOPE`.

Do not run this profile when the implementer and both reviewer threads cannot be resumed. Return `HANDOFF_REQUIRED` rather than replacing them with fresh roles.

## Phase budget

Before the first task, record:

- approved number of tasks;
- maximum total agent turns;
- maximum high-judgment turns;
- broad test or build count;
- target time or cost range when measurable;
- audit threshold;
- rescope authority.

Do not add tasks, reviewers, or turns beyond the phase budget without rescope and permission.

## Capability tiers

Select by role difficulty, not by brand name:

| Tier | Use |
| --- | --- |
| fast/economical | Read-only discovery, fixtures, mechanical types, deterministic transformations |
| standard | Clear implementation tasks, focused tests, ordinary planning |
| high-judgment | Architecture, auth, persistence, migrations, security, critical review |
| highest-cost/experimental reasoning | Only a specifically approved role and question after ordinary high-judgment work is insufficient |

Never select the highest-cost or experimental reasoning tier automatically, including for high-risk work. Use it only when the user explicitly includes that tier, the exact role, and its turn limit in both the phase budget and permission envelope. Record why the ordinary high-judgment tier is insufficient. If that approval is absent, remain within the approved tiers or return `HANDOFF_REQUIRED`; do not infer permission from a maximum-quality profile.

Do not fix model brand names in the portable contract. Resolve an approved capability tier to a host-supported model and reasoning setting only at dispatch time. If a critical role cannot receive the needed approved tier, record the gap and choose `HANDOFF_REQUIRED` when it invalidates the profile.

## Context budgets

Aim for:

- task brief: 800–1,500 words; hard limit 2,000;
- dispatch text: 300–500 words plus exact paths;
- agent report: 500–800 words;
- reviewer package: brief, report, scoped diff or hashes, compact test summary, and applicable checklist.

Never send the full conversation, whole implementation plan, unrelated task history, all previous reports, branch-wide diff, or raw test logs when a smaller package suffices.

## Verification tiers

During implementation:

```text
focused RED -> minimal implementation -> focused GREEN
```

At the task gate, run only applicable checks:

- task suite;
- one to three nearest regressions;
- targeted typecheck or lint;
- diff/whitespace check;
- build when the build path changed;
- secret or security scan when relevant.

After the fixer wave, run the covering check and one nearest regression. Run a broad suite at a phase or final gate, not after every correction.

Store evidence as command, exit code, pass/fail counts, and a relevant note. Preserve raw logs outside the controller context when needed for diagnosis.
