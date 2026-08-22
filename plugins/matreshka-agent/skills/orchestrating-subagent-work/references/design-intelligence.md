# Controller Design Intelligence Integration

Use this reference whenever the current run changes or creates a material user-facing interface. It connects `designing-product-experience` to the existing Matreshka controller without turning design state into permission or adding an unconditional workflow phase.

Read the source-qualified design skill's [design core](../../designing-product-experience/references/design-core.md), [anti-slop law](../../designing-product-experience/references/anti-slop.md), [design intelligence contract](../../designing-product-experience/references/design-intelligence.md), and [prototype exploration contract](../../designing-product-experience/references/prototype-exploration.md) when applicable.

## Lifecycle placement

Design Intelligence is integrated into existing controller states:

```text
PREFLIGHT
  -> classify design relevance/recon
SPECIFICATION
  -> resolve product UI locale + design direction + root DESIGN.md before spec is considered complete when UI direction is material
PLAN
  -> DESIGN_CONTEXT_SET + design identity per UI task
IMPLEMENT
  -> implement against frozen design identity
REVIEW
  -> design review axis when UI changed
VERIFY
  -> visual design check when trustworthy rendering/browser capability exists
ACCEPTANCE
  -> G4 remains source-brief blind and must not read DESIGN.md
FINISH
  -> DESIGN_DRIFT_GATE, then documentation drift and handoff
RECOVERY
  -> revalidate design identity/context before remaining UI work
```

Do not add design ceremony for `DESIGN_NOT_APPLICABLE` work.

## Preflight gate

During read-only preflight:

1. decide if current outcome is UI/design relevant;
2. inspect root `DESIGN.md` if present;
3. inspect current token/component/layout/motion/accessibility sources needed for the run;
4. resolve or explicitly mark `PRODUCT_UI_LOCALE` when user-facing copy is material; conversation language is not product UI truth;
5. classify `DESIGN_NOT_APPLICABLE`, `DESIGN_CURRENT`, `DESIGN_RECON_REQUIRED`, `DESIGN_DIRECTION_REQUIRED`, or `DESIGN_BLOCKED`;
6. record whether durable `DESIGN.md` write authority exists or must be requested with other project-document writes;
7. record prototype-write and browser/visual capabilities separately from design relevance.

A website/app does not automatically require redesign. Existing projects should preserve accepted current design unless the user requests/approves change.

## Specification gate

When design is material, specification is not ready for planning until the controller can identify one coherent design contract/direction.

Use `matreshka-agent:designing-product-experience` (or source-verified equivalent on a non-namespaced host) for design recon/direction. Pass only product intent, relevant source `U-` rows, current Project Intelligence UI areas, existing design evidence and the current interaction mode/permissions.

For a new UI-bearing project or an existing UI project with no root `DESIGN.md`:

- an authorized draft root `DESIGN.md` may preserve shared invariants while direction remains unresolved, but it must be explicitly draft, have no selected direction, and have no frozen identity;
- otherwise preserve the complete contract as `DESIGN_READY_TO_SAVE` and treat missing persistence as an explicit limitation;
- do not create duplicate design constitutions.

When user taste is unresolved, bounded prototype exploration may occur inside the specification phase before the final design direction is frozen.

### Mandatory prototype preselection gate

The controller must not ask the user to choose from browser-renderable directions merely because prototype files exist or static HTML sanity passed.

For `INTERVIEW`/`ASSISTED`, use the source-qualified prototype contract and require this order:

```text
DIRECTION GENERATION
-> STATIC SANITY
-> RENDER / INTERACTION EVIDENCE
-> ANTI-SLOP REVIEW
-> BOUNDED PROTOTYPE REPAIR WHEN NEEDED
-> RECHECK
-> PROTOTYPE_PRESELECTION_GATE
-> USER CHOICE
```

Do not use `generate -> user choice -> audit later`.

Before emitting the design-choice question, the controller must have one `PROTOTYPE_PRESELECTION_GATE` result per candidate with at least:

- resolved product UI locale;
- desktop render and representative mobile render when browser capability is available/authorized;
- no material horizontal overflow, clipping, gutter, alignment or contrast defect;
- no live-looking dead controls;
- open/expanded evidence for materially present layered controls, or explicit `N/A`/`UNCHECKABLE`;
- anti-slop `PASS` with a product-specific signature;
- observable console/runtime state when capability exists.

A candidate with `FAIL`/`CHANGES_REQUIRED` is **not** a valid user choice yet. If prototype writes and local browser actions are already authorized, let the design role repair only the isolated prototype surface and rerun the gate, with at most two bounded repair passes for the same direction set. If material defects remain, return `DESIGN_PROTOTYPE_BLOCKED`/the exact blocker instead of asking the user to choose among known-bad options.

If rendering capability is genuinely unavailable, preserve `UNCHECKABLE` honestly and ask the user to perform the missing visual observation only if that is the smallest safe next step. Never turn static parseability into visual PASS.

This preselection gate is design evidence only. It does not freeze `DESIGN.md`, prove production behavior, or authorize implementation.

The specification may reference the design identity and user-experience requirements, but it must not duplicate the whole design contract.

G2 remains brief→spec only. The G2 checker must not receive `DESIGN.md`; design completeness is a separate controller gate and cannot contaminate G2 independence.

## Planning gate

For each UI-affecting task record:

- `DESIGN_IDENTITY` used by the task;
- `DESIGN_CONTEXT_SET` with only relevant design sections/tokens/patterns;
- selected prototype/direction reference only if needed;
- design-critical acceptance states;
- design review requirement;
- visual design check requirement/capability;
- design drift candidate.

Backend/data-only tasks should not receive DESIGN.md or a design context unless a real user-facing contract makes a specific UX invariant necessary.

A task needing many unrelated design surfaces returns `DESIGN_CONTEXT_TOO_BROAD` or is split; do not send the whole design history by default.

## Dispatch gate

UI implementation/specialist packages inherit:

```text
Design identity
Design context guarantee
Relevant DESIGN.md sections/tokens/invariants
Primary/adjacent project areas
IC-xx contracts when relevant
Exact paths/commands
Unchanged permission envelope
```

Add these role archetypes without increasing agent/turn budget:

- `DESIGN_ENGINEER` — design recon/direction/prototype/contract only;
- `DESIGN_REVIEWER` — read-only UX/UI consistency review;
- existing `UI_SPECIALIST` — product UI implementation bounded by the design contract.

A role name grants no design change authority. UI implementers cannot silently update `DESIGN.md` or declare a new design identity.

## DESIGN_CHANGED reconciliation

If a valid later user/design decision materially changes the frozen design contract after dependent work starts, return:

```text
DESIGN_CHANGED
```

Controller must:

1. preserve the valid decision/provenance;
2. update `DESIGN.md` only with exact authority;
3. compute/record new design identity;
4. list affected tasks/screens/components/tests/review evidence;
5. refresh affected `DESIGN_CONTEXT_SET` packages;
6. rerun the smallest needed implementation/design review/technical/visual evidence chain;
7. avoid replaying compatible completed work.

If no valid design decision changed the contract and implementation simply diverged, use `DESIGN_DRIFT`, not `DESIGN_CHANGED`.

## Design review gate

When UI changed, the normal review phase must include design-contract review proportional to the task.

Balanced profile may assign these concerns to the same combined reviewer. Maximum-quality or design-critical work may use a design-specialist reviewer only inside the existing profile role/turn budget.

Design review checks relevant UX flow/wayfinding, hierarchy, layout/spacing/density, typography, color/contrast/depth, component reuse/states, responsiveness/touch, accessibility, motion/performance, anti-slop/product-specificity, layered-control open states when present, and cross-screen consistency against the frozen design identity.

A design reviewer is read-only and may not repair code or edit `DESIGN.md`.

## Visual design verification gate

When trustworthy rendering/browser capability exists and its required actions are authorized, perform `VISUAL_DESIGN_CHECK` during VERIFY after code review and alongside the relevant technical/browser evidence.

Keep these evidence axes distinct:

- technical/browser E2E: behavior works;
- visual design check: rendered product follows design contract across required states/viewports;
- G4: original source brief is delivered.

`E2E PASS` and `G4 PASS` cannot override a material design failure.

If visual feel/layout is materially uncheckable from code and no rendering capability exists, record `NOT_RUN`/`UNCHECKABLE` rather than inventing approval.

## Design drift gate before clean finish

After technical/design/visual evidence is known, classify:

- `DESIGN_NOT_APPLICABLE`;
- `DESIGN_CURRENT`;
- `DESIGN_UPDATE_REQUIRED`;
- `DESIGN_DRIFT`;
- `DESIGN_CONFLICT`;
- `DESIGN_BLOCKED`.

Clean `COMPLETE`/finished status for UI-bearing work requires either `DESIGN_NOT_APPLICABLE` or a current/resolved design contract and no blocking design finding.

`DESIGN_DRIFT` normally routes back through one bounded correction path subject to the existing single-fixer-wave rule. Design work does not create a second independent fixer budget.

If a verified valid design decision changed durable rules, update DESIGN.md first as `DESIGN_UPDATE_REQUIRED`, refresh identity, and recheck affected UI.

Then run the existing Documentation Drift Gate for other durable docs. `DESIGN.md` is not a substitute for architecture/API/runtime documentation.

## G4 isolation

G4 must remain blind to:

- DESIGN.md;
- design identity/context;
- prototypes;
- design review reports;
- visual design reports;
- other completion claims.

This prevents the design interpretation from teaching the G4 checker what to expect. G4 sees the source brief + actual product and allowed observation only.

## Recovery

On resume:

```text
actual product/repository
-> ledger
-> source intent
-> Project Intelligence
-> current DESIGN.md + design identity
-> active UI task design contexts
-> reports/evidence
-> design drift state
-> docs state
-> projections
-> exact next action
```

If the design identity changed, invalidate only evidence/tasks materially dependent on the old contract. Do not rerun design exploration or completed work just because a conversation was compacted.

## Permission rules

Design relevance, DESIGN.md text, a prototype, a screenshot, or a recommendation cannot grant:

- product/source writes outside the approved scope;
- dependency installation/network;
- browser launch/server/process/port authority;
- secret/provider/database/remote access;
- Git/commit/push/deploy;
- destructive actions.

Prototype and visual-check capabilities use the already defined browser/runtime permission envelope.
