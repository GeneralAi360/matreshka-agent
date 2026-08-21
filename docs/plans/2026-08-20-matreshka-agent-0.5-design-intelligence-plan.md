# Implementation Plan — Matreshka Agent 0.5 Design Intelligence Layer

- Status: `IMPLEMENTED_PENDING_NATIVE_VALIDATION`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-design-intelligence-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; no merge to `main` or `0.5.0` release claim from this plan.

## Goal

Add durable UX/UI design reasoning, exploration, consistency and verification to Matreshka while preserving the current source-intent, Project Intelligence, Browser/E2E, permission and security architecture.

## Task map

| Task | Result | Main files | Status |
| --- | --- | --- | --- |
| `D1` | UI/design relevance + recon contract | design skill/reference, Build/controller | `IMPLEMENTED` |
| `D2` | Apple-inspired core + UI craft/motion baseline | `design-core.md` | `IMPLEMENTED` |
| `D3` | root `DESIGN.md` durable contract + design identity | template, controller, ledger/permissions | `IMPLEMENTED` |
| `D4` | prototype divergence + picker workflow | `prototype-exploration.md`, design skill | `IMPLEMENTED` |
| `D5` | `DESIGN_CONTEXT_SET` + existing-first primitive policy | planner/task/dispatch/Project Intelligence | `IMPLEMENTED` |
| `D6` | independent design review | reviewing skill + controller routing | `IMPLEMENTED` |
| `D7` | visual browser design check separate from E2E/G4 | verifier + browser/design contracts | `IMPLEMENTED` |
| `D8` | design drift gate + finish/recovery | controller/finish/ledger/dashboard | `IMPLEMENTED` |
| `D9` | package integration as 11th skill | manifest/dev validator/wrappers/readmes/CI/integrity checker | `IMPLEMENTED` |
| `D10` | native acceptance | disposable full-stack UI fixture | `PENDING_NATIVE` |

## Implemented wiring

```text
building-end-to-end
  -> design relevance signal
  -> orchestrating-subagent-work
       -> Design Intelligence preflight
       -> designing-product-experience when required
       -> root DESIGN.md + design identity
       -> planner DESIGN_CONTEXT_SET
       -> UI/design specialist dispatch
       -> code/security + design review
       -> technical/browser E2E + VISUAL_DESIGN_CHECK
       -> G4 with DESIGN artifacts forbidden
       -> DESIGN_DRIFT_GATE
       -> DOCUMENTATION_DRIFT_GATE
       -> finish/recovery/dashboard
```

### Package integration

The development track intentionally keeps versioned manifests at `0.4.0`, but package inventory is now eleven bundled skills through `validate_dev_05.py`:

```text
building-end-to-end
orchestrating-subagent-work
designing-product-experience
specifying-software-work
planning-software-work
writing-portable-agent-prompt
implementing-with-tests
debugging-systematically
reviewing-agent-work
verifying-development-work
finishing-development-work
```

`matreshka-design.md` is included in the 0.5 Codex wrapper inventory. CI uses the 0.5 development validator and doctor wrappers rather than the release-line 0.4 inventory directly.

## Implementation invariants

- `DESIGN.md` is a durable design contract, not permission or behavioral proof.
- UI-relevant project with no `DESIGN.md` creates it when exact design-document writes are authorized; otherwise returns `DESIGN_READY_TO_SAVE`/handoff rather than silently omitting it.
- Existing UI truth is discovered before redesign. `EXISTING_PROJECT` does not get gratuitous rebranding.
- Apple-inspired principles are mandatory design-core reasoning, not an optional visual preset.
- Apple concepts guide Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight, wayfinding, feedback, direct manipulation, spatial consistency, typography and accessibility; Matreshka must not imitate Apple visuals blindly.
- Prototype exploration is only for unresolved material direction and does not become routine token-heavy ceremony.
- Prototype variants remain isolated until selection and diverge on genuine axes, not cosmetic color tweaks.
- `DESIGN_CONTEXT_SET` is narrow/task-local; backend-only tasks receive no irrelevant design payload.
- Design review is separate from technical correctness but stays inside execution-profile role/turn budgets.
- Browser E2E, Visual Design Check and G4 are separate evidence axes.
- `DESIGN_DRIFT` blocks clean completion; a legitimate contract change uses `DESIGN_CHANGED` / `DESIGN_UPDATE_REQUIRED` reconciliation instead of allowing one screen to drift.
- UI/motion-library recommendations do not grant dependency/network authority.
- Design changes cannot weaken security, privacy, accessibility, source intent or frozen cross-area interfaces.
- Dashboard/ledger/design artifacts are projections/coordination state and never grant permission.

## Required adversarial cases

1. UI project with no `DESIGN.md` -> persist when authorized before multi-screen implementation.
2. UI project without design-doc authority -> `DESIGN_READY_TO_SAVE`; no false persistence claim.
3. Mature existing UI without `DESIGN.md` -> reconstruct current design truth; no arbitrary redesign.
4. User says “I don't know what I want” -> 3 genuinely distinct prototype directions, not a long style questionnaire.
5. Three prototypes differ only by accent color -> reject fake divergence.
6. `FULL_AUTO` with no brand facts -> restrained reversible direction, no invented official brand/logo.
7. Random radius/color/spacing outside frozen design -> `DESIGN_DRIFT`.
8. Valid later user design decision changes invariant -> `DESIGN_CHANGED`, reconcile dependents and refresh identity.
9. Frontend task receives whole design history/screenshots -> narrow `DESIGN_CONTEXT_SET`.
10. Backend-only task receives UI design payload -> remove unless UX contract is actually required.
11. UI specialist wants hand-built dialog despite compatible existing accessible primitive -> reuse existing primitive.
12. Preferred UI library install in `FULL_AUTO` without dependency/network authority -> block/recommend only.
13. Keyboard/high-frequency interaction gets decorative 500ms animation -> design review blocks/removes.
14. Motion ignores reduced-motion/focus/touch -> design review blocks.
15. E2E/G4 pass but screen violates `DESIGN.md` -> no COMPLETE.
16. Visual feel materially uncheckable -> `UNCHECKABLE`/capability gap, not fabricated approval.
17. Existing `DESIGN.md` conflicts with accepted current UI -> reconcile conflict; do not blindly force either source.
18. Recovery loads old design hash after contract update -> revalidate identity/context before remaining UI dispatch.

## Static hardening gate

Before D10 native acceptance, the development checkout must run:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

A static PASS proves package shape and cross-component wiring only. It does not prove native browser/design behavior.

## Remaining evidence gate — D10

Run one disposable full-stack native acceptance that proves together:

- real frontend/backend/data/E2E topology without fake areas;
- Design Recon and root `DESIGN.md`;
- Apple-inspired design core applied as UX principles without forced Apple styling;
- prototype divergence when direction is intentionally ambiguous;
- frozen design identity + narrow `DESIGN_CONTEXT_SET`;
- shared `IC-xx` producer/consumer contract;
- specialist routing without budget inflation;
- technical verification + repository-native Browser E2E;
- Design Review + `VISUAL_DESIGN_CHECK` on representative viewports/states;
- G4 independence with design artifacts forbidden;
- Design Drift Gate + Documentation Drift Gate;
- Russian dashboard showing Project + Design Intelligence, timing and truthful token state;
- recovery data sufficient to resume from ledger rather than conversation.

D10 remains `PENDING_NATIVE`. This plan does not authorize a `0.5.0` release claim until that evidence and the wider release gates are satisfied.
