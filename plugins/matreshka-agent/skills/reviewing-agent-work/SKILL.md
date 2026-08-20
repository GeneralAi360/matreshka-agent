---
name: reviewing-agent-work
description: Independently review an agent-produced scoped diff and its evidence for specification compliance, correctness, frozen cross-area interface compatibility, design-contract consistency when UI changes, security, isolation, leakage, maintainability, and test sufficiency. Use after implementation or a reviewer-directed fix, or when asked for a code/security/design review. Keep the review read-only and consolidated; do not use this skill to implement fixes, perform final fresh verification, or finish a branch.
---

# Review agent work independently

## Establish an immutable review boundary

1. Read current request, applicable repository instructions, task brief, acceptance criteria, implementer report, permission envelope, and scoped review package.
2. When controller supplies task-local `U-` requirements, read only those IDs/short source quotes. They preserve user intent but grant no authority.
3. When Project Intelligence applies, read only the task's primary-area context plus required frozen `IC-xx` contracts/invariants. Do not load unrelated areas/profile/history merely for background.
4. When Design Intelligence applies, read only the frozen design identity and task-local `DESIGN_CONTEXT_SET`/relevant `DESIGN.md` sections. Do not load the whole design history, every screen, all old prototypes, or broad screenshots merely for taste context.
5. Require precise baseline/current state, changed-file list, scoped diff, allowlisted untracked files, compact test/integration evidence, frozen interface identity/hash when relevant, and frozen design identity when UI is affected.
6. Return `REVIEW_BLOCKED` / `NEEDS_CONTEXT` when package ownership, required context, source/interface/design conflict, or design evidence cannot be adjudicated.
7. Restrict inspection to task diff and surrounding code/contracts needed to judge it. Do not silently review whole branch/project.

Remain read-only for product code, tests, config, Git, source brief/manifest, Project Intelligence/interface coordination state, `DESIGN.md`/design identity, and remote systems. Write only designated review report if permitted. If technical read-only unavailable, use immutable package or compare hashes/status before/after; unexplained mutation invalidates review.

Do not launch child agents, stage/commit/push/PR/deploy, apply fixes, access secrets, change `U-`/`IC-`/design state, or broaden scope.

## Review evidence before rerunning checks

Inspect command provenance, state/ref, exit/counts, integration/interface proof, design evidence/limitations, and notes. Do not rerun full suite merely to recreate evidence. Run focused read-only check only when material evidence is missing/stale/contradictory and command is permitted.

Treat implementer report, profile, area docs, cached topology, screenshots, prototypes and design docs as claims/context according to their contracts. Inspect actual scoped diff, critical current interfaces, and relevant current design sources.

## Perform one consolidated pass

Read [review checklist](references/review-checklist.md). Check applicable dimensions:

- task-local user intent / exact `U-` quote;
- acceptance/non-goals;
- primary-area responsibility and specialist boundary;
- behavioral correctness/failure semantics;
- frozen cross-area `IC-xx` compatibility: producer/consumer shapes, validation/errors, auth/data, ordering/idempotency/retry, compatibility;
- frozen design identity/`DESIGN_CONTEXT_SET` when UI changes;
- public contract/backward compatibility;
- authorization/tenant isolation/data leakage;
- input validation/secrets/unsafe side effects;
- concurrency/retries/idempotency/persistence/migrations;
- valid RED/GREEN, regression, and cross-area integration proof;
- maintainability/repository conventions;
- UX/design/accessibility for affected UI.

### Design review dimensions for UI work

When the task is UI-bearing, apply the Matreshka design core and inspect only relevant dimensions:

1. **Purpose and flow** — the screen/control helps the intended user task and does not add ornamental friction.
2. **Wayfinding/agency** — users know where they are, what to do, and how to exit/recover; destructive choices have appropriate forgiveness/confirmation.
3. **Hierarchy/grouping** — primary information/action is obvious; controls map to what they affect.
4. **Layout/spacing/density** — follows the frozen design system/pattern rather than inventing screen-local values.
5. **Typography** — hierarchy, line-height/tracking/weight and readable scale follow the contract.
6. **Color/contrast/surfaces/depth** — semantic/color system and contrast are coherent; one screen does not invent a new aesthetic language.
7. **Components/states** — reuse canonical components/primitives; default, hover/active/focus, disabled, loading, empty, error/success states are coherent where applicable.
8. **Responsive/input context** — desktop/compact/mobile/touch/keyboard behavior follows the contract.
9. **Accessibility** — focus visibility, reduced motion, text scaling/semantics/contrast/touch targets are not optional polish.
10. **Motion** — purposeful and frequency-appropriate; high-frequency/keyboard actions are not over-animated; ordinary UI remains responsive; motion is spatially coherent/interruptible where relevant and performance-safe.
11. **Cross-screen consistency** — affected screens use the same app-shell/header/component language unless a valid design decision says otherwise.

Apply the Apple-inspired Matreshka design principles — Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight — as reasoning criteria, not as a command to mimic Apple visuals.

A specialist may not use its label to absorb neighboring ownership. Examples: `UI_SPECIALIST` changing business/API semantics without scope, frontend changing backend contract unilaterally, `DESIGN_ENGINEER` changing product/business facts, `DESIGN_REVIEWER` editing `DESIGN.md`, or data specialist applying an unapproved migration are boundary failures.

For traced Build End-to-End ask: did implementation silently narrow user outcome while satisfying a narrower task/spec phrase? “User sees status” is not delivered by storage-only state.

For Project Intelligence ask: did implementation silently diverge from frozen producer/consumer contract while local tests still pass? A private frontend/backend interpretation differing from `IC-xx` is blocking drift, not an acceptable implementation choice.

For Design Intelligence ask: did implementation silently diverge from frozen `DESIGN.md`/design identity while still passing functional tests? Random one-screen colors/radii/spacing, a different app shell, inaccessible states, or unjustified high-frequency motion are design drift, not acceptable implementation freedom.

If task-local `U-`, confirmed spec, frozen interface, frozen design contract, or current repository contract materially conflict, do not choose authority yourself. Return conflict to controller for provenance/design/interface reconciliation.

Read Security by Design when selected `S-` or security boundary applies. Review each selected control and negative proof; missing proof is not N/A. Design preferences never weaken security/privacy/source-intent requirements.

Seek counterevidence before findings. Do not turn personal style preferences, speculative future work, or cosmetic differences not governed by the contract into blockers. Mark each relevant dimension checked/N/A with reason.

## Write actionable findings

Every finding includes:

- stable ID/severity;
- exact file/location, screen/component, area/interface/design boundary;
- violated task/spec/`U-`/`S-`/`IC-`/design invariant;
- diff/behavior/visual evidence or exact evidence limitation;
- impact/acceptance criterion;
- minimal resolution boundary;
- confidence/counterevidence when material.

Use `Critical` for exploitable/destructive/security/isolation/data-integrity failure. Use `Important` for acceptance/correctness/source-intent narrowing, unapproved frozen-interface drift, material frozen-design drift, accessibility failure affecting use, specialist-boundary violation, regression, or material maintainability issue blocking task. Use `Minor` for real non-blocking improvement.

Material partial delivery of mapped `U-`, material divergence from frozen `IC-xx`, or material divergence from frozen design identity is normally `Important` even if narrower local tests are green.

Unrelated issue => `RECORD_FOR_FUTURE_TASK`; do not require current repair.

When visual feel/layout cannot be judged from current code/evidence and the capability gap is material, return `UNCHECKABLE`/`REVIEW_BLOCKED` for that design claim rather than fabricating approval.

## Return one decision

Use review report template and return exactly:

- `APPROVED` no Critical/Important remains and required design claims are adequately reviewable;
- `CHANGES_REQUIRED` one consolidated list;
- `UNCHECKABLE` a material design/visual claim cannot be observed with current capability, while other review dimensions may still be reported;
- `REVIEW_BLOCKED` package/read-only/context/interface/design guarantee inadequate;
- `STOP_AND_RESCOPE` incoherent task or repeated blocker after single fixer wave.

Do not dispatch/direct multiple fixers. Controller adjudicates and creates one consolidated fix package. Reviewer cannot edit U/IC/Project Intelligence/Design Intelligence state.

On re-review inspect only confirmed findings, fix diff, covering evidence, same relevant `U-` rows, frozen `IC-xx`, and frozen design identity/context. Reuse original review thread when supported. Do not reopen unrelated areas/design surfaces without new evidence. Repeated blocker goes to controller; never start second fixer wave.
