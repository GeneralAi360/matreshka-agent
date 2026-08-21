# Implementation Plan — Matreshka Agent 0.5 Design Intelligence Layer

- Status: `IMPLEMENTED_PENDING_NATIVE_VALIDATION`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-design-intelligence-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; no merge to `main` or `0.5.0` release claim from this plan.

## Goal

Add durable UX/UI design reasoning, exploration, consistency and verification to Matreshka while preserving source-intent, Project Intelligence, Browser/E2E, permission and security architecture.

## Task map

| Task | Result | Main files | Status |
| --- | --- | --- | --- |
| `D1` | UI/design relevance + recon | design skill/reference, Build/controller | `IMPLEMENTED` |
| `D2` | Apple-inspired core + UI craft/motion baseline | `design-core.md` | `IMPLEMENTED` |
| `D3` | root `DESIGN.md` + design identity | template, controller, ledger/permissions | `IMPLEMENTED` |
| `D4` | prototype divergence + picker workflow | prototype contract, design skill | `IMPLEMENTED` |
| `D5` | `DESIGN_CONTEXT_SET` + existing-first primitives | spec/planner/task/implement/Project Intelligence | `IMPLEMENTED` |
| `D6` | independent Design Review | review package/skill/report + controller/budget routing | `IMPLEMENTED` |
| `D7` | Visual Design Check separate from E2E/G4 | verifier/report + browser/design contracts | `IMPLEMENTED` |
| `D8` | design drift + finish/recovery/dashboard | controller/finish/ledger/dashboard | `IMPLEMENTED` |
| `D9` | package + static/behavioral hardening as 11th skill | manifests/wrappers/readmes/CI/checkers | `IMPLEMENTED` |
| `D10` | native acceptance | disposable full-stack UI fixture | `PENDING_NATIVE` |

## Implemented wiring

```text
building-end-to-end
  -> DESIGN_RELEVANCE_SIGNAL
  -> orchestrating-subagent-work
       -> Design Intelligence preflight
       -> designing-product-experience when required
       -> root DESIGN.md + design identity
       -> specifying-software-work references frozen design identity
       -> planning DESIGN_CONTEXT_SET
       -> UI/design specialist implementation
       -> implementation report preserves area/IC/design identities
       -> code/security + design review
       -> technical/browser E2E + VISUAL_DESIGN_CHECK
       -> G4 with DESIGN artifacts forbidden
       -> DESIGN_DRIFT_GATE
       -> DOCUMENTATION_DRIFT_GATE
       -> finish/recovery/dashboard
```

### Package integration

Versioned manifests remain `0.4.0`, while the development inventory is eleven bundled skills through `validate_dev_05.py`:

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

`matreshka-design.md` is the 11th optional Codex wrapper. Development CI uses the 0.5 validator/doctor adapters around the proven 0.4 validation core.

## Implementation invariants

- `DESIGN.md` is a durable design contract, not permission or behavioral proof.
- UI-relevant project with no `DESIGN.md` creates it only with exact design-document write authority; otherwise returns `DESIGN_READY_TO_SAVE`/handoff.
- Existing UI truth is discovered before redesign; `EXISTING_PROJECT` gets no gratuitous rebranding.
- Apple-inspired principles are mandatory design-core reasoning, not an Apple visual preset.
- Apple concepts guide Purpose, Agency, Responsibility, Familiarity, Flexibility, Simplicity, Craft, Delight, wayfinding, feedback, direct manipulation, spatial consistency, typography and accessibility.
- Prototype exploration is only for unresolved material direction and variants diverge on genuine axes, not cosmetic color tweaks.
- `DESIGN_CONTEXT_SET` is narrow/task-local; backend-only tasks receive no irrelevant design payload.
- Software specification references frozen design identity and user-experience constraints without duplicating the whole design system.
- Implementation must confirm area context, frozen `IC-xx`, design identity/context and stop on `INTERFACE_CHANGED`, `DESIGN_CHANGED` or `DESIGN_DRIFT` rather than rewriting contracts.
- Design Review is separate from technical correctness but stays inside execution-profile role/turn budgets.
- Balanced uses combined reviewer for applicable design concerns; maximum-quality has only two reviewer slots total and a named `DESIGN_REVIEWER` consumes one existing slot.
- Browser E2E, Visual Design Check and G4 are separate evidence axes.
- `DESIGN_DRIFT` blocks clean completion; valid contract changes use `DESIGN_CHANGED` / `DESIGN_UPDATE_REQUIRED` reconciliation.
- UI/motion-library recommendations do not grant dependency/network authority.
- Design changes cannot weaken security, privacy, accessibility, source intent or frozen cross-area interfaces.
- Dashboard/ledger/design artifacts are projections/coordination state and never grant permission.

## Required adversarial cases

### Core Design Intelligence suite — 18

1. missing `DESIGN.md` + authorized write;
2. missing design-doc authority;
3. existing product reconstruct-before-change;
4. user does not know desired style;
5. fake prototype divergence;
6. FULL_AUTO cannot invent brand;
7. random design tokens => drift;
8. valid design change => reconciliation;
9. narrow design context;
10. backend gets no irrelevant design payload;
11. existing primitive first;
12. dependency install not authorized;
13. high-frequency over-animation;
14. accessibility design blocker;
15. E2E/G4 pass but design fails;
16. visual capability unavailable;
17. stale design contract conflicts with current product;
18. recovery sees changed design identity.

### Cross-skill behavioral contract cases

Specification:
- `design-identity-preserved`;
- `ui-direction-unresolved-before-spec`.

Implementation:
- `ui-task-preserves-area-interface-design`;
- `implementation-detects-design-contract-change`.

Review:
- `design-review-detects-screen-drift`;
- `design-review-uncheckable-visual-feel`.

Verification:
- `visual-design-fails-while-e2e-passes`;
- `visual-design-uncheckable-without-renderer`;
- `g4-contaminated-by-design-artifacts`.

## Static hardening gate

Before D10 native acceptance, execute on the same development checkout:

```bash
python3 -B plugins/matreshka-agent/scripts/validate_dev_05.py \
  plugins/matreshka-agent --marketplace-root . --self-test

python3 -B plugins/matreshka-agent/scripts/check_dev_05.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/check_dev_05_behavioral_contracts.py \
  plugins/matreshka-agent --marketplace-root .

python3 -B plugins/matreshka-agent/scripts/doctor_dev_05.py \
  plugins/matreshka-agent --marketplace-root .
```

CI runs the same four-layer sequence on Python 3.11.

Static PASS proves package shape, component wiring and required behavioral-eval coverage only. It does not prove that a native coding-agent host will execute every design behavior correctly.

## Remaining evidence gate — D10

Run one disposable full-stack native acceptance that proves together:

- real frontend/backend/data/E2E topology without fake areas;
- Design Recon and root `DESIGN.md`;
- Apple-inspired design core applied as UX principles without forced Apple styling;
- prototype divergence when direction is intentionally ambiguous;
- frozen design identity + narrow `DESIGN_CONTEXT_SET`;
- shared `IC-xx` producer/consumer contract;
- specialist routing without budget inflation;
- specification → implementation → review → verification preserves design identity;
- technical verification + repository-native Browser E2E;
- independent Design Review + `VISUAL_DESIGN_CHECK` at representative viewports/states;
- G4 independence with design artifacts forbidden;
- Design Drift Gate + Documentation Drift Gate;
- Russian dashboard showing Project + Design Intelligence, timing and truthful token state;
- recovery data sufficient to resume from ledger rather than conversation.

D10 remains `PENDING_NATIVE`. This plan does not authorize a `0.5.0` release claim until that native evidence and wider release gates are satisfied.
