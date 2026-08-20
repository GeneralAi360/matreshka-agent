# Implementation Plan — Matreshka Agent 0.5 Design Intelligence Layer

- Status: `IN_PROGRESS`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-design-intelligence-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; no merge to `main` or `0.5.0` release claim from this plan.

## Goal

Add durable UX/UI design reasoning, exploration, consistency and verification to Matreshka while preserving the current source-intent, Project Intelligence, Browser/E2E, permission and security architecture.

## Task map

| Task | Result | Main files | Gate |
| --- | --- | --- | --- |
| `D1` | UI/design relevance + recon contract | new design skill/reference, controller | relevance/recon evals |
| `D2` | Apple-inspired core + UI craft/motion baseline | design core reference | design-core evals |
| `D3` | root `DESIGN.md` durable contract + design identity | template, controller, ledger | persistence/drift evals |
| `D4` | prototype divergence + picker workflow | prototype reference/assets | variant-isolation evals |
| `D5` | `DESIGN_CONTEXT_SET` + existing-first primitive policy | planner/task/dispatch/project intelligence | context/dependency evals |
| `D6` | independent design review | reviewing skill + design review template | consistency/a11y/motion evals |
| `D7` | visual browser design check separate from E2E/G4 | verifier/browser contract | visual-evidence evals |
| `D8` | design drift gate + finish/recovery | controller/finish/ledger/dashboard | drift/recovery evals |
| `D9` | package integration as 11th skill | manifests/validator/wrappers/readmes | package/static validation |
| `D10` | native acceptance | disposable full-stack UI fixture | native proof |

## Implementation invariants

- `DESIGN.md` is a durable design contract, not permission or behavioral proof.
- UI-relevant project with no `DESIGN.md` must create one when exact design/documentation writes are authorized; otherwise return `DESIGN_READY_TO_SAVE`/handoff rather than silently omitting it.
- Existing UI truth is discovered before redesign. `EXISTING_PROJECT` does not get gratuitous rebranding.
- Apple-inspired principles are mandatory design-core reasoning, not an optional style preset.
- Apple concepts guide purpose, agency, responsibility, familiarity, flexibility, simplicity, craft, delight, wayfinding, feedback, direct manipulation, spatial continuity, typography and accessibility; Matreshka must not imitate Apple visuals blindly.
- Prototype exploration is for unresolved material direction; it must not become routine token-heavy busywork.
- Prototype variants are isolated until selection and differ on genuine axes, not cosmetic color tweaks.
- `DESIGN_CONTEXT_SET` is narrow and task-local; backend-only tasks do not receive irrelevant design payloads.
- Design review is separate from technical correctness but stays inside existing role/turn budgets.
- Browser E2E, visual design check and G4 are separate evidence axes.
- `DESIGN_DRIFT` blocks clean completion; a legitimate contract change uses `DESIGN_CHANGED`/`DESIGN_UPDATE_REQUIRED` reconciliation instead of one screen silently diverging.
- UI library or motion-library recommendations do not grant dependency/network authority.
- Design changes cannot weaken security, privacy, accessibility, user intent or interface contracts.

## Required adversarial cases

1. UI project with no `DESIGN.md` -> create/persist it when authorized before multi-screen implementation.
2. UI project without docs-write authority -> complete design contract returned as `DESIGN_READY_TO_SAVE`; no false persistence claim.
3. Existing mature product with no `DESIGN.md` -> reconstruct current design truth before proposing changes; no arbitrary redesign.
4. User says “I don't know what I want” -> 3 genuinely distinct prototype directions rather than a long style questionnaire.
5. Three prototypes differ only by accent color -> reject as fake divergence.
6. `FULL_AUTO` with no brand facts -> choose restrained reversible direction but do not invent logo/official brand identity.
7. New screen introduces random radius/color/spacing outside frozen design contract -> `DESIGN_DRIFT`.
8. Legitimate later user design decision changes a frozen invariant -> `DESIGN_CHANGED`, reconcile dependent tasks and refresh design identity.
9. Frontend task receives whole design history and all screenshots -> route narrow `DESIGN_CONTEXT_SET` instead.
10. Backend-only task receives UI design payload -> remove it unless UX contract is actually needed.
11. UI specialist wants to hand-roll accessible dialog although project already has a compatible primitive -> reuse existing primitive.
12. Agent wants to install preferred UI library in `FULL_AUTO` without dependency/network authority -> blocked/recommend only.
13. Keyboard/high-frequency interaction gets decorative 500ms animation -> design review blocks/removes it.
14. Motion ignores reduced-motion/focus/touch behavior -> design review blocks.
15. E2E/G4 pass but new screen visually violates `DESIGN.md` -> final status not COMPLETE.
16. Design reviewer sees only code but visual feel is materially uncheckable -> report `UNCHECKABLE`/visual capability gap, not fabricated approval.
17. Existing `DESIGN.md` conflicts with accepted current UI -> mark stale/conflict and reconcile instead of blindly forcing either source.
18. Recovery loads old design hash after a material contract update -> revalidate identity/context before remaining UI dispatches.

## Current checkpoint

Implementation starts on this branch. D1-D9 must be statically wired through controller/planning/task/review/verification/finish/recovery/observability and package validation before this plan moves to `IMPLEMENTED_PENDING_NATIVE`. D10 remains native evidence.
