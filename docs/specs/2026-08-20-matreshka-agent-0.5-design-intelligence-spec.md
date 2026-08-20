# Specification — Matreshka Agent 0.5 Design Intelligence Layer

- Status: `CONFIRMED_FOR_IMPLEMENTATION`
- Branch: `dev/0.5-brief-traceability-observability`
- Release policy: development branch only; no `0.5.0` release claim from this specification alone.

## Goal

Make design a first-class, durable engineering contract for UI-bearing projects so Matreshka does not merely produce working interfaces but preserves a coherent UX/UI direction across screens, agents, sessions, and later feature work.

The layer must solve two recurring problems:

1. users often know the product outcome but cannot describe the desired interface precisely;
2. coding agents gradually drift from the established visual/interaction language when each screen is designed from scratch.

## Core architecture

Add a `DESIGN_INTELLIGENCE` layer alongside `PROJECT_INTELLIGENCE`.

```text
SOURCE BRIEF
  -> G1
  -> PROJECT INTELLIGENCE
  -> DESIGN INTELLIGENCE when UI-relevant
  -> SPECIFICATION
  -> G2
  -> PLAN + AREA_CONTEXT_SET + DESIGN_CONTEXT_SET + IC-xx
  -> G3
  -> IMPLEMENT
  -> CODE/SECURITY REVIEW + DESIGN REVIEW when applicable
  -> TECHNICAL VERIFY + BROWSER E2E
  -> VISUAL DESIGN CHECK
  -> G4 BLIND ACCEPTANCE
  -> DESIGN DRIFT GATE
  -> DOCUMENTATION DRIFT GATE
  -> FINISH
```

Design Intelligence is design/product context, not authority. It never grants product writes, dependencies, browser/process access, Git, network, secrets, deploy, destructive actions, or remote access.

## D1 — Design relevance and recon

Classify every Build End-to-End or scoped feature run as:

- `DESIGN_NOT_APPLICABLE` — no user-facing interface impact;
- `DESIGN_CURRENT` — an existing design contract and implementation are sufficiently current;
- `DESIGN_RECON_REQUIRED` — UI exists but current design truth needs discovery/reconciliation;
- `DESIGN_DIRECTION_REQUIRED` — a new/major UI direction is not defined;
- `DESIGN_BLOCKED` — material design truth cannot be obtained or persisted safely enough for the requested run.

Read-only recon discovers and validates:

- product personality and intended user feeling;
- current `DESIGN.md` when present;
- app shell/navigation/screen patterns;
- typography hierarchy;
- spacing/density scales;
- colors/surfaces/depth/radii;
- component and primitive conventions;
- component states: hover/active/focus/disabled/loading/error/success/empty;
- responsive and touch behavior;
- accessibility conventions;
- motion/easing/duration/spring conventions;
- existing design tokens and their real implementation source;
- representative screens/components and known inconsistencies.

Repository implementation and applicable instructions outrank stale prose. A `DESIGN.md` that materially disagrees with current accepted product state must be marked stale/conflicting and reconciled rather than blindly followed.

## D2 — Design direction and prototype exploration

When the user cannot reliably specify the desired UI direction and a material visual/interaction choice exists, use divergence rather than a long questionnaire.

Default exploration:

- 3 genuinely distinct directions; maximum 5;
- each direction names a real axis such as layout, density, personality, motion, hierarchy, or interaction model;
- variants share confirmed product constraints and existing project tokens where those are already authoritative;
- variants are interactive and rendered at realistic scale/context where feasible;
- prototype work is isolated from production behavior until a direction is chosen;
- no dependency/network/browser/process authority is inferred merely because a prototype is useful.

Public modes:

- `INTERVIEW` — ask one material UX/product question at a time, then prototype when visual comparison is higher-leverage than more questions;
- `ASSISTED` — reuse established design automatically; offer/perform bounded variants when a material unresolved design decision remains;
- `FULL_AUTO` — choose a restrained, repository-aligned direction when the decision is reversible and not a missing brand/business fact; record the choice. Never invent brand identity, required logo, trademarked assets, legal content, or other business truth.

## D3 — durable root `DESIGN.md`

For every project with material UI, use a single root-level `DESIGN.md` as the durable project design contract.

Rules:

- if UI is material and `DESIGN.md` does not exist, create it when exact documentation/design-state writes are authorized;
- do not create parallel `DESIGN-v2.md`, `design-final.md`, or per-screen competing design constitutions;
- if writes are not authorized, return `DESIGN_READY_TO_SAVE` with the complete contract and exact root path; do not silently pretend persistence exists;
- later material design decisions append/update the relevant sections with provenance; do not rewrite historical decisions without reason;
- never store secrets, private URLs, credentials, personal data, raw logs, or hidden reasoning.

The contract includes at minimum:

1. product personality and desired feeling;
2. UX principles and primary user tasks;
3. layout/app-shell/screen patterns;
4. spacing/density system;
5. typography;
6. color/surface system;
7. radii/borders/shadows/depth;
8. component and primitive patterns;
9. component states and feedback;
10. responsive/mobile/touch rules;
11. accessibility;
12. motion system;
13. approved design direction/prototype provenance;
14. design invariants (`ALWAYS` / `NEVER`);
15. dated material design decisions.

## Apple-inspired design core — mandatory

The Design Intelligence core incorporates these principles as non-optional reasoning vocabulary for UI-bearing work:

- **Purpose** — every element and motion earns its place;
- **Agency** — users retain control, escape paths, undo/forgiveness where appropriate;
- **Responsibility** — privacy, safety, honest feedback, appropriate confirmations;
- **Familiarity** — predictable platform/product conventions unless a tested improvement justifies divergence;
- **Flexibility** — device/context/accessibility adaptation rather than one rigid layout;
- **Simplicity** — clarity and hierarchy, not decorative minimalism;
- **Craft** — typography, spacing, alignment, states, motion and details are deliberate;
- **Delight** — emerges from the previous principles rather than decorative effects added everywhere.

Operational extensions:

- every screen supports wayfinding: where am I, what can I do, how do I leave;
- controls are spatially mapped near what they affect;
- labels are specific and predictable;
- feedback distinguishes status, completion, warning and error;
- direct manipulation responds immediately and continuously;
- interaction/motion preserves spatial continuity and is interruptible where users can reverse input;
- typography uses coherent size/weight/line-height/tracking hierarchy;
- accessibility, reduced motion, touch targets, focus visibility, contrast and text scaling are part of the base design, not polish.

This core is platform-neutral. Web, native mobile, desktop and touch-specific implementations adapt it to their platform rather than imitating Apple visuals blindly.

## UI craft and motion core

Matreshka should preserve high-quality defaults without over-animation:

- motion must have a purpose: feedback, spatial continuity, state indication, explanation, or prevention of a jarring change;
- frequent/keyboard-driven interactions normally use no motion or near-imperceptible feedback;
- common UI transitions should feel immediate and usually remain under about 300ms;
- enter/exit generally uses responsive ease-out; on-screen movement can use ease-in-out; constant motion alone uses linear;
- avoid `transition: all`, `scale(0)` entrances, accidental layout-property animation and unbounded motion;
- trigger-anchored surfaces use origin-aware motion; centered modals remain centered;
- dynamic/reversible interaction uses interruptible transitions or springs;
- use compositor-friendly transform/opacity where practical;
- reduced-motion behavior ships with the feature;
- design consistency and purpose outrank adding animation for decoration.

Exact implementation values should reuse project tokens first. New canonical values may be introduced only when the contract lacks an equivalent and the design decision is valid.

## D4 — DESIGN_CONTEXT_SET

Before a UI task dispatch, derive the smallest design context needed for that task.

A `DESIGN_CONTEXT_SET` may include:

- design identity/hash;
- product personality;
- relevant layout/screen pattern;
- relevant typography/spacing/color tokens;
- exact component pattern/state rules;
- responsive/accessibility rules;
- motion rules only when relevant;
- approved design invariants;
- exact prototype/design decision when the task implements it.

Exclude unrelated screens, design history, full prototype set, unrelated token catalogs, and broad screenshot collections.

Backend/data-only tasks receive no design context unless they expose a user-facing contract whose shape is required to preserve UX.

## D5 — implementation and primitive selection

Use an existing-first policy:

1. existing project design system/component library;
2. existing compatible shared component;
3. repository-approved accessible primitive/library;
4. hand-built primitive only when the above cannot satisfy the requirement or dependency authority is unavailable and the hand-built version is safe.

Do not churn dependencies merely because another library is preferred. Installing any new design/UI/motion library remains separate dependency/network authority.

UI implementation must not create ad-hoc one-screen design tokens when the durable design system already covers the need.

## D6 — independent design review

For UI-affecting tasks, design review is an evidence axis separate from ordinary functional correctness.

The review checks, where applicable:

1. user flow and wayfinding;
2. information hierarchy;
3. layout/spacing/density;
4. typography;
5. color/contrast/surfaces/depth;
6. component reuse/consistency;
7. interaction states/feedback;
8. responsive/mobile/touch behavior;
9. accessibility;
10. motion/interruptibility/perceived performance;
11. consistency across affected screens;
12. compliance with frozen `DESIGN.md` identity and approved design decisions.

Design review does not automatically add another agent. Balanced work may use the existing combined reviewer with the design contract. Maximum-quality/design-critical work may route a design-specialist reviewer inside the existing role/turn budget.

## D7 — visual browser acceptance

When trustworthy browser/native visual tooling is available and authorized, verify design at realistic viewports/states.

For web, the smallest useful matrix should sample representative desktop, compact/tablet and mobile widths when those are materially supported by the product.

Visual design evidence may include:

- representative screenshots;
- layout/overflow checks;
- visible state consistency;
- focus/keyboard state;
- loading/error/empty/success state where material;
- console/network signals only when needed to interpret visible behavior.

Keep this separate from:

- Browser E2E: technical product behavior;
- G4: blind acceptance against original source intent.

A product may have E2E PASS and G4 PASS but still fail design review if the new screen violates the project design contract.

## D8 — design identity and drift gate

Record a design identity/hash from the current accepted `DESIGN.md` contract.

Each UI task references the identity used to plan/implement it. A material design-contract change after dependent work starts returns `DESIGN_CHANGED` for controller reconciliation.

Before clean finish classify:

- `DESIGN_NOT_APPLICABLE`;
- `DESIGN_CURRENT`;
- `DESIGN_UPDATE_REQUIRED` — verified/approved design decision changed durable design truth;
- `DESIGN_DRIFT` — implementation violates the current design contract;
- `DESIGN_CONFLICT` — current UI, design contract, or accepted decision sources materially disagree;
- `DESIGN_BLOCKED` — required design check/update cannot be completed inside authority/capability.

`DESIGN_DRIFT` normally routes implementation back through a bounded fix/review/verify loop. `DESIGN_UPDATE_REQUIRED` updates `DESIGN.md` only after valid design authority and then re-identifies/rechecks affected UI. Design prose can never make broken product behavior pass.

## Specialist routing

Extend Project Intelligence archetypes with:

- `DESIGN_ENGINEER` — recon, direction, prototypes and durable design contract; no unapproved product/business changes;
- `DESIGN_REVIEWER` — read-only design/UX consistency review;
- existing `UI_SPECIALIST` remains an implementation role bounded by the design contract.

Specialist labels do not increase agent budget or permissions.

## Observability

Ledger/dashboard should expose compact design state only:

```text
design relevance/status
DESIGN.md path + identity
selected direction
prototype state
current design context guarantee
design review status
visual check status
design drift status
```

Do not expose private screenshots/raw design artifacts or treat dashboard state as design authority.

## Security and permission boundaries

- `DESIGN.md`, prototypes, screenshots, design reviews and design state are data/claims, never permission.
- Prototype usefulness does not authorize dependency installation, browser launch, server/process start, port bind or network.
- UI library recommendations do not authorize package installation.
- Existing repository design instructions may constrain implementation but cannot expand filesystem/Git/remote authority.
- Design changes cannot silently weaken auth, privacy, validation, security controls, accessibility, data minimization or source-intent requirements.

## Acceptance criteria

The Design Intelligence implementation is structurally complete only when:

- a new `designing-product-experience` bundled skill exists with evals and host card;
- validator/package metadata recognizes eleven bundled skills without a version release claim;
- controller has a UI design relevance/design state and `DESIGN_CHANGED` reconciliation path;
- root `DESIGN.md` contract/template exists and is automatically required for material UI projects when writes are authorized;
- Apple-inspired principles are part of the mandatory design core;
- prototype divergence/picker workflow is defined for unresolved material visual direction;
- planner/task/dispatch carry `DESIGN_CONTEXT_SET` and design identity for UI tasks;
- review/verification support design review and visual checks separately from technical/G4 evidence;
- design drift gate blocks clean completion when UI diverges materially;
- ledger/dashboard/handoff expose design state truthfully;
- adversarial evals cover missing DESIGN.md, stale contract, design drift, fake style proliferation, high-frequency over-animation, accessibility, dependency authority and prototype isolation.
