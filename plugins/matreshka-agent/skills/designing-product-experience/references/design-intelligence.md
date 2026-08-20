# Design Intelligence Contract

Use this contract when a project has material UI/UX, when a new screen/component would rely on shared visual/interaction rules, or when existing design consistency must survive further development.

Design Intelligence is descriptive design state. It never grants filesystem, command, Git, network, browser, process, port, dependency, secret, provider, database, deploy, migration, destructive, or remote authority.

## D1 — DESIGN_RELEVANCE

Classify the current task/run:

- `DESIGN_NOT_APPLICABLE` — no material user-facing interface impact;
- `DESIGN_CURRENT` — current accepted design contract/patterns are sufficient;
- `DESIGN_RECON_REQUIRED` — design exists but needs current-state reconstruction/reconciliation;
- `DESIGN_DIRECTION_REQUIRED` — material UX/UI direction is genuinely unresolved;
- `DESIGN_BLOCKED` — a required design fact/capability/authority is unavailable.

Do not trigger design ceremony only because a repository contains CSS. A backend-only task remains design-not-applicable unless it changes a user-facing contract that requires UX reasoning.

## D2 — DESIGN_RECON

Read-only recon validates current design truth from:

1. root `DESIGN.md` when present;
2. applicable repository instructions;
3. current accepted UI implementation and design tokens;
4. shared component primitives and state patterns;
5. representative current screens;
6. documented user/product design decisions;
7. screenshots/prototypes only as supporting evidence.

Record:

```text
DESIGN_RECON
status: CURRENT | PARTIAL | STALE | CONFLICT | UNAVAILABLE
contract_path: <root/DESIGN.md or none>
contract_identity: <hash/none>
product_personality: <short>
app_shell: <pattern/source>
layout_density: <pattern/source>
typography: <tokens/source>
color_surfaces: <tokens/source>
radius_border_depth: <tokens/source>
components: <system/source>
states: <system/source>
responsive_touch: <rules/source>
accessibility: <rules/source>
motion: <tokens/rules/source>
known_drift: <items or none>
```

Current code/config does not automatically outrank an intentionally approved design contract when the implementation itself is the drift under investigation. On conflict, identify both sources and require controller/user reconciliation rather than choosing whichever is newer.

## D3 — DESIGN.md durable contract

For a UI-bearing project use exactly one canonical root contract:

```text
<project-root>/DESIGN.md
```

If it does not exist and exact design/documentation writes are authorized, create it before substantial multi-screen UI implementation relies on undocumented design decisions.

If the project already has other design documentation, `DESIGN.md` may reference compatible detailed docs, but it remains the compact canonical contract/index. Do not create competing root constitutions.

If write authority is absent, retain the complete contract inline and return `DESIGN_READY_TO_SAVE` with the exact intended root path. A missing persistent file must remain visible as a recovery/consistency limitation.

### Design identity

Compute/record a stable content identity/hash after the contract is accepted. Every UI task uses one design identity.

Material contract change after dependent work begins yields:

```text
DESIGN_CHANGED
```

Controller then:

1. stops affected UI work at the next safe boundary;
2. validates the new design authority/decision;
3. updates `DESIGN.md` when authorized;
4. records new identity;
5. identifies affected tasks/screens/components/tests/review;
6. refreshes `DESIGN_CONTEXT_SET`;
7. reruns the smallest required implementation/design-review/visual-check chain.

A task cannot silently declare a new design identity.

## D4 — DESIGN_CONTEXT_SET

Before every UI implementation/review task derive a narrow design context.

Required only when relevant:

```text
Design identity
Product personality
Screen/layout pattern
Typography tokens
Spacing/density tokens
Color/surface tokens
Radius/border/depth tokens
Component/primitive pattern
Interactive states
Responsive/touch rules
Accessibility rules
Motion rules
Design invariants
Selected prototype/direction
Explicit exclusions
Context guarantee: NARROW | DEGRADED | DESIGN_CONTEXT_TOO_BROAD
```

Do not forward the entire design history, all screenshots, all prototype variants, every component spec, or the whole `DESIGN.md` when a small task needs only a subset.

If correctness depends on several unrelated design systems/surfaces, split or return `DESIGN_CONTEXT_TOO_BROAD` rather than hiding the conflict.

## D5 — UI primitive policy

Use existing-first selection:

1. current project design system/library;
2. current compatible shared component;
3. repository-approved accessible primitive/library;
4. a new primitive only when required and safe.

Before recommending a new library inspect existing package/config evidence. Do not create dependency churn for taste. Any package installation/download remains outside Design Intelligence authority.

A one-off custom primitive is a design-maintainability finding when a shared pattern already exists and can satisfy accessibility/behavior.

## D6 — DESIGN_REVIEW

UI-affecting implementation requires design review proportional to the change. It does not automatically create an extra agent.

Review dimensions:

- flow/wayfinding;
- hierarchy/grouping;
- layout/spacing/density;
- typography;
- color/contrast/surfaces/depth;
- shared component reuse;
- default/hover/active/focus/disabled/loading/error/success/empty states;
- responsive/mobile/touch behavior;
- accessibility;
- motion purpose/frequency/easing/timing/interruptibility/performance/reduced-motion;
- cross-screen consistency;
- frozen design identity/invariants.

Return:

```text
DESIGN_REVIEW
status: APPROVED | CHANGES_REQUIRED | UNCHECKABLE | BLOCKED
contract_identity: <hash>
findings:
- severity: Critical | Important | Minor
  location: <screen/component/file>
  invariant: <DESIGN.md section>
  evidence: <observable/code evidence>
  correction_boundary: <minimal>
visual_capability_gap: <none or exact limitation>
```

A design reviewer remains read-only. A reviewer may not update the design contract to make an implementation appear compliant.

## D7 — VISUAL_DESIGN_CHECK

Use browser/native visual tooling only when available and authorized. This is separate from Browser E2E and G4.

For web, select representative viewports from actual product support. A reasonable starting sample for a general responsive web product is one desktop, one compact/tablet-like, and one mobile width, but repository/project requirements override generic dimensions.

Check relevant states, not only the happiest static screenshot:

- primary content state;
- loading/empty/error/success where affected;
- focus/keyboard navigation where relevant;
- overflow/wrapping/responsive layout;
- touch/pointer affordance where relevant;
- motion/reduced-motion only when materially changed.

Return:

```text
VISUAL_DESIGN_CHECK
status: PASS | PARTIAL | FAIL | NOT_RUN | BLOCKED
contract_identity: <hash>
viewports: <list>
screens_states: <list>
evidence_refs: <safe refs>
blocking_findings: <summary>
limitations: <none or exact>
```

Do not infer pixel-perfect correctness from a screenshot alone. Use screenshots as evidence for visual state/consistency, not as permission or behavioral proof.

## D8 — DESIGN_DRIFT_GATE

Before clean finish classify:

- `DESIGN_NOT_APPLICABLE`;
- `DESIGN_CURRENT`;
- `DESIGN_UPDATE_REQUIRED` — a valid approved design decision changed durable design truth and `DESIGN.md` must be refreshed;
- `DESIGN_DRIFT` — implementation violates the current contract without valid design change authority;
- `DESIGN_CONFLICT` — contract/current accepted UI/user decision sources disagree materially;
- `DESIGN_BLOCKED` — required check/update cannot be completed in current authority/capability.

### Examples of material drift

- one new screen invents random colors/radii/spacing outside the frozen system;
- a new page uses a different app-shell/header hierarchy without a design decision;
- a form introduces new input/error/focus behavior inconsistent with the contract;
- a modal/popover breaks the established component/interaction pattern;
- a high-frequency keyboard action gains slow decorative motion;
- reduced-motion/focus/mobile rules are omitted on a newly introduced interaction;
- an existing shared primitive is bypassed by an inaccessible one-off replacement.

### What is not automatically drift

- an implementation-specific internal class name;
- a one-pixel browser rendering difference with no design-system significance;
- a new component explicitly added to the design contract through valid design authority;
- a platform-specific adaptation required by the contract's flexibility rules.

## Recovery

On resume/recovery:

1. validate project root/current state;
2. locate root `DESIGN.md` or recorded inline contract;
3. recompute/validate design identity;
4. compare current accepted UI and design contract for material drift/conflict;
5. validate selected direction/prototype provenance if still relevant;
6. rebuild only the affected `DESIGN_CONTEXT_SET` for remaining tasks;
7. preserve completed/verified work whose design identity remains compatible;
8. rerun design review/visual check only where changed identity/state invalidates old evidence;
9. update dashboard/progress last.

Do not restart design exploration merely because conversation context was lost.

## Project Intelligence relationship

Project Intelligence answers **where/what the system is**. Design Intelligence answers **how the user-facing experience should behave and feel**.

Typical UI task package:

```text
U-/S- requirements
+ AREA_CONTEXT_SET
+ DESIGN_CONTEXT_SET
+ IC-xx when cross-area
+ exact paths/commands
+ implementation/review evidence
```

Neither context set grants permission.

## Dashboard projection

Project only compact design state:

```text
design relevance/state
DESIGN.md path/identity
selected direction
prototype state
design context guarantee
design review status
visual check status
design drift state
```

Never project raw private screenshots, brand assets, full design docs, personal data or secret-bearing browser evidence.
