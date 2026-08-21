# Profiles and Budgets

Choose execution rigor from risk. Choose autonomy separately. Project/Design Intelligence specialist labels never create extra budget by themselves.

## Risk routing

Treat these as high risk: authentication, authorization, tenant/organization isolation, row-level security, destructive/data-transforming migrations, payments, secrets/provider credentials, persistence guarantees, production configuration and irreversible remote actions.

Treat these as **design-critical/high-judgment experience signals** when material: core navigation/wayfinding, multi-step onboarding/checkout, accessibility-critical flows, cross-screen design-system changes, complex gestures/direct manipulation, mobile/touch architecture, high-frequency interaction redesign, or a new product-wide design direction. They increase review judgment but do not automatically make unrelated backend code maximum-quality.

Documentation, fixtures, serializers, pure deterministic functions, small type changes and safe local tests are low risk when they do not alter public/security/design contracts.

Route ordinary work to balanced unless evidence justifies another profile.

## Maximum speed

Use for bounded low-risk work with clear acceptance criteria.

```text
implementer -> controller verification -> optional reviewer
```

- Unique agents per task: one implementer; at most one reviewer.
- Agent turns per task: at most four if reviewer/fix needed.
- Fix waves: one, same implementer thread when resume exists.
- Re-review: omit for Minor-only changes when controller verification covers change.
- Prohibit for high-risk boundaries.
- Do not use maximum speed for a material unresolved product-wide design direction or design-critical accessibility/navigation change.

If small UI change is otherwise low-risk and frozen DESIGN.md makes it mechanical, maximum speed may remain valid; design relevance alone is not a reason to inflate rigor.

Escalate to balanced before dispatch if public contract, persistence/security boundary, frozen design identity, or material UX flow becomes uncertain.

## Balanced

Default profile.

```text
implementer -> combined reviewer -> same implementer fixes -> same reviewer rechecks
```

- Unique agents per task: at most two.
- Agent turns per task: at most four.
- Fix waves: zero or one.
- Review: one combined pass covers source/task/spec, correctness, quality, security, isolation, leakage, interfaces, tests, and affected UX/design when applicable.
- For UI work the combined reviewer receives frozen design identity + narrow DESIGN_CONTEXT_SET and applies Design Review dimensions; **do not add a separate Design Reviewer on top of balanced budget**.
- If a material visual property cannot be judged from allowed evidence, reviewer records `UNCHECKABLE`; later Visual Design Check may supply evidence without creating another code-writing role.
- Repeat Critical/Important after fix: `STOP_AND_RESCOPE`.

Require same-thread follow-up for fix/re-review. If resume unavailable, declare `DEGRADED_MODE`. For low-risk task, controller may apply one small consolidated correction and controller verification, clearly stating no independent re-review. High-risk work => `HANDOFF_REQUIRED`.

## Maximum quality

Use for high-risk code/production handoff or genuinely design-critical work where balanced review is insufficient.

Base shape still has **three unique agents maximum**:

```text
implementer -> reviewer A + reviewer B -> same implementer fixes -> each reviewer rechecks own findings
```

- Unique agents per task: at most three total (implementer + two reviewer slots).
- Agent turns per task: at most six.
- Fix waves: zero or one consolidated wave.
- Reviewers: two independent read-only slots; parallel only with immutable/technically read-only packages.
- Re-review: each original reviewer checks only owned confirmed findings once.
- Repeat Critical/Important: `STOP_AND_RESCOPE`.

Assign the **two reviewer slots by risk**, never by adding a fourth role:

| Task shape | Reviewer A | Reviewer B |
| --- | --- | --- |
| security/data critical, no material UI | spec/contract reviewer | security/code reviewer |
| security/data critical + material UI | spec/experience reviewer (includes frozen design contract) | security/code reviewer |
| design-critical UI, ordinary security | `DESIGN_REVIEWER` or spec/experience reviewer | code/spec reviewer |
| migration + design-critical UI mixed in one task | normally `SPLIT_REQUIRED` before review | normally split |

A named `DESIGN_REVIEWER` consumes one existing reviewer slot. It never creates a third reviewer slot. Likewise frontend/backend/design specialist labels do not add writer turns.

Do not run maximum quality when implementer and required reviewer threads cannot be resumed. Return `HANDOFF_REQUIRED` rather than replacing them with fresh roles and pretending independence/continuation.

## Phase budget

Before first task record:

- approved number of tasks;
- maximum total agent turns;
- maximum high-judgment turns;
- broad test/build count;
- visual-browser check count when design-critical and measurable;
- target time/cost range when measurable;
- audit threshold;
- rescope authority.

Do not add tasks/reviewers/turns beyond phase budget without rescope/permission. Prototype exploration and Design Reviewer usage consume explicit high-judgment/turn budget when they use agent turns; they are not free because they are “design”.

## Capability tiers

Select by role difficulty, not brand:

| Tier | Use |
| --- | --- |
| fast/economical | read-only discovery, fixtures, mechanical types, deterministic transformations |
| standard | clear implementation tasks, focused tests, ordinary planning |
| high-judgment | architecture, auth, persistence, migrations, security, material design direction, design-critical review |
| highest-cost/experimental reasoning | only specifically approved role/question after ordinary high-judgment insufficient |

Never select highest-cost/experimental automatically, including design work. User must explicitly include tier, exact role and turn limit in phase budget + permission envelope. Without approval remain within approved tiers or `HANDOFF_REQUIRED`.

Do not fix model brand names in portable contract. Resolve capability tier to host-supported model/reasoning only at dispatch. If critical role cannot receive needed tier, record gap and use `HANDOFF_REQUIRED` when it invalidates profile.

## Context budgets

Aim for:

- task brief: 800–1,500 words; hard 2,000;
- dispatch: 300–500 words plus paths;
- agent report: 500–800 words;
- reviewer package: task brief, report, scoped diff/hashes, compact test summary, applicable U/S/IC + design identity/context, and checklist.

Never send full conversation, implementation plan, Project Intelligence history, full DESIGN.md history/prototype set/screenshots, all previous reports, branch-wide diff or raw logs when smaller package suffices.

For design work, send only the current identity plus task-relevant design sections/tokens/invariants. Visual evidence should be the smallest decisive set, not a screenshot dump.

## Verification tiers

During implementation:

```text
focused RED -> minimal implementation -> focused GREEN
```

At task gate run applicable:

- task suite;
- one to three nearest regressions;
- targeted typecheck/lint;
- diff/whitespace check;
- cross-area integration proof when applicable;
- build when build path changed;
- secret/security scan when relevant;
- task-local accessibility/design semantic checks when applicable.

After fixer wave run covering check + one nearest regression. Run broad suite/E2E/Visual Design Check at phase/final gate, not after every correction.

Browser E2E and Visual Design Check are separate evidence rows. Visual check does not create extra reviewer/fixer budget and verifier remains read-only.

Store evidence as command/interaction, state, exit/signal, pass/fail counts and relevant note. Preserve raw logs/screenshots outside controller context when needed and safe.
