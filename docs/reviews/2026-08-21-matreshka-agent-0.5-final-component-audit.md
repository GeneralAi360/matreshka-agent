# Matreshka Agent 0.5 — Final Component and Wiring Audit

- Audit date: `2026-08-21`
- Branch: `dev/0.5-brief-traceability-observability`
- Audited implementation snapshot: `4db55ec39414110815d9ededee3d831f4b977c8e`
- Baseline `main`: `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Branch relation at audit: `149 commits ahead / 0 behind`
- Versioned manifests: intentionally `0.4.0`
- Release label: `0.5 DEVELOPMENT PREVIEW`

## Verdict

```text
COMPONENT INVENTORY              STATIC PASS
CROSS-COMPONENT WIRING           STATIC PASS
DESIGN DOWNSTREAM WIRING         STATIC PASS
BEHAVIORAL EVAL COVERAGE         CONFIGURED / STATICALLY PRESENT
DETERMINISTIC CI PIPELINE         CONFIGURED
FINAL-HEAD CI EXECUTION RESULT    NOT OBSERVABLE FROM CURRENT CONNECTOR
NATIVE CORE EVIDENCE              PARTIAL (older TaskLedger snapshot)
NATIVE PROJECT INTELLIGENCE       PENDING
NATIVE BROWSER/VISUAL EVIDENCE    PENDING
NATIVE DESIGN INTELLIGENCE        PENDING
0.5.0 RELEASE CLAIM               NOT ALLOWED YET
```

No confirmed 0.5 implementation component remains intentionally `PENDING_IMPLEMENTATION`. Remaining gates are **execution/native/release evidence**, not missing architecture files.

## Proof vocabulary

This audit deliberately separates:

- **PRESENT** — required file/contract/template/eval exists;
- **WIRED** — upstream/downstream contracts explicitly carry the state through the workflow;
- **COVERED** — deterministic static check or behavioral eval case exists for the seam;
- **EXECUTED** — checker/test was actually run on this exact snapshot and result observed;
- **NATIVE_PROVEN** — real supported host exercised the behavior successfully.

`PRESENT + WIRED + COVERED` must never be reported as `NATIVE_PROVEN`.

## 1. Package inventory

Expected development inventory is exactly eleven bundled skills:

1. `building-end-to-end`
2. `orchestrating-subagent-work`
3. `designing-product-experience`
4. `specifying-software-work`
5. `planning-software-work`
6. `writing-portable-agent-prompt`
7. `implementing-with-tests`
8. `debugging-systematically`
9. `reviewing-agent-work`
10. `verifying-development-work`
11. `finishing-development-work`

Expected optional Codex wrapper inventory is also exactly eleven, including `matreshka-design.md`.

`validate_dev_05.py` extends the proven 0.4 validator inventory in memory instead of prematurely changing release-line version metadata.

Verdict: `PRESENT / WIRED / COVERED`.

## 2. End-to-end component graph

The current development contract is:

```text
building-end-to-end
  |
  +-- launch scenario: NEW / CONTINUE / EXISTING
  +-- public mode: INTERVIEW / ASSISTED / FULL_AUTO
  +-- SOURCE_BRIEF + SOURCE_DECISIONS
  +-- DESIGN_RELEVANCE_SIGNAL
  v
orchestrating-subagent-work
  |
  +-- permission envelope / ledger / recovery identity
  +-- U- requirements + S- security
  +-- G1
  +-- PROJECT INTELLIGENCE
  |    +-- P1 PROJECT_TOPOLOGY
  |    +-- P2 AREA_CONTEXT_SET
  |    +-- P3 frozen IC-xx
  |    +-- P4 RUNTIME_MAP
  |    +-- P5 DOCUMENTATION_DRIFT_GATE
  |    +-- P6 SPECIALIST_ROLE_ROUTING
  |
  +-- DESIGN INTELLIGENCE (UI-material only)
  |    +-- D1 relevance/recon
  |    +-- D2 direction/prototype exploration
  |    +-- D3 root DESIGN.md + design identity
  |    +-- D4 DESIGN_CONTEXT_SET
  |    +-- D5 existing-first primitives
  |    +-- D6 Design Review
  |    +-- D7 VISUAL_DESIGN_CHECK
  |    +-- D8 DESIGN_DRIFT_GATE
  |
  +-- specifying-software-work
  +-- G2
  +-- planning-software-work
  +-- G3
  +-- implementing-with-tests
  +-- reviewing-agent-work
  +-- verifying-development-work
  |    +-- technical/security
  |    +-- Automated Browser E2E
  |    +-- Visual Design Check
  +-- G4 BLIND ACCEPTANCE
  +-- Design Drift Gate
  +-- Documentation Drift Gate
  +-- finishing-development-work
  v
FINISH / HANDOFF / RECOVERY
```

Verdict: `STATIC PASS`.

## 3. Source intent and launch UX

### Present/wired

- `SOURCE_BRIEF` remains separate from later decisions.
- `U-xx` user outcomes remain separate from `S-xx` security controls.
- G1/G2/G3/G4 retain independent responsibilities.
- `INTERVIEW`, `ASSISTED`, `FULL_AUTO` are public modes.
- `AUTONOMOUS_LOCAL` remains internal controller autonomy only.
- `CONTINUE_PROJECT` and `EXISTING_PROJECT` have different recovery/adoption behavior.
- Build wrapper passes `DESIGN_RELEVANCE_SIGNAL` but does not own Design Intelligence state.

### Key safety invariant

`FULL_AUTO` does not imply Git/network/browser/process/design-doc/prototype/secret/deploy authority.

Verdict: `PRESENT / WIRED / COVERED`; older TaskLedger gave partial native evidence for source/G2/G3/G4 and permission boundaries.

## 4. Project Intelligence P1–P6

| Capability | Present | Downstream wiring |
| --- | --- | --- |
| P1 Project Topology | yes | preflight → profile/ledger → spec/plan → task/recovery/dashboard |
| P2 Area Context Router | yes | plan → task brief → dispatch → implementation/review |
| P3 `IC-xx` | yes | controller freeze → spec/plan/task → implement/review/verify/docs/recovery |
| P4 Runtime Map | yes | preflight/ledger/task/verify/permission/recovery |
| P5 Docs Drift Gate | yes | verified behavior → finish/handoff |
| P6 Specialist Routing | yes | planner/task/dispatch/budget/review |

`INTERFACE_CHANGED` is a formal controller reconciliation status.

Project specialist table now also coordinates with Design Intelligence via `DESIGN_ENGINEER` / `DESIGN_REVIEWER` without merging the two intelligence layers.

Verdict: `STATIC PASS / NATIVE PENDING`.

## 5. Design Intelligence D1–D9

### D1 — Design relevance and recon

Controller preflight explicitly inspects root `DESIGN.md`, current tokens/components/shell/screens/accessibility/motion and classifies design state.

Verdict: `PRESENT / WIRED / COVERED`.

### D2 — direction and prototype exploration

- default 3 genuinely distinct directions, maximum 5;
- real axes, not cosmetic color variants;
- isolated from production until selection;
- no implicit browser/server/dependency permission.

Verdict: `PRESENT / WIRED / 18-core-eval coverage`.

### D3 — root `DESIGN.md` and identity

One canonical root design contract. Missing write authority produces `DESIGN_READY_TO_SAVE`; implementation cannot rewrite it to hide drift.

Verdict: `PRESENT / WIRED / COVERED`.

### D4 — Design Context Router

UI tasks receive frozen design identity + task-local `DESIGN_CONTEXT_SET`; backend-only tasks do not receive irrelevant UI payload.

Now wired through:

```text
controller
→ specification reference
→ plan
→ task brief
→ implementer
→ implementation report
→ review package/report
→ verification report
→ finish/recovery
```

Verdict: `STATIC PASS`.

### D5 — existing-first primitive policy

Existing design system/components/primitives are preferred. New UI/motion library recommendation is not dependency/network permission.

Verdict: `PRESENT / WIRED / COVERED`.

### D6 — Design Review

Review contracts explicitly check UX flow/wayfinding, hierarchy, layout/spacing/density, typography, color/contrast/depth, component reuse/states, responsive/touch, accessibility, motion/perceived performance, cross-screen consistency and frozen design identity.

Visual feel that cannot be observed is `UNCHECKABLE`, not guessed.

Verdict: `STATIC PASS / NATIVE PENDING`.

### D7 — Visual Design Check

Verification report now physically separates:

```text
Technical/Security
Automated Browser E2E
Visual Design Check
Blind G4 handoff boundary
```

`DESIGN_VERIFICATION` may be PASS/PARTIAL/FAIL/BLOCKED/UNCHECKABLE.

Verdict: `STATIC PASS / NATIVE PENDING`.

### D8 — Design Drift Gate

- legitimate accepted contract change → `DESIGN_CHANGED` reconciliation;
- durable design update required → `DESIGN_UPDATE_REQUIRED` with explicit write authority;
- implementation deviation → `DESIGN_DRIFT`;
- unresolved conflict/blocker prevents clean COMPLETE.

Verdict: `STATIC PASS / NATIVE PENDING`.

### D9 — package/hardening integration

11th skill, Codex wrapper, dev validator/doctor, component checker, behavioral-contract checker, CI/docs/plan/changelog integration are present.

Verdict: `STATIC PASS`.

## 6. Apple-inspired design core

The design core requires the reasoning principles:

- Purpose
- Agency
- Responsibility
- Familiarity
- Flexibility
- Simplicity
- Craft
- Delight

plus wayfinding, feedback, grouping/mapping, direct manipulation, spatial consistency, typography hierarchy and accessibility/reduced motion/touch/focus/contrast.

Explicit invariant: this is **not an Apple visual preset**. It cannot justify unrequested glass/iOS styling.

Verdict: `PRESENT / WIRED into Design skill, controller, review, docs / NATIVE PENDING`.

## 7. Downstream wiring defects found and fixed during final hardening

### H-DESIGN-01 — main controller under-linked Design Intelligence

Before hardening, design contracts existed but controller did not explicitly load/own every design transition.

Fixed: main controller now owns design relevance, root contract/identity, design context, review/visual evidence, drift and recovery.

### H-DESIGN-02 — controller/permission/P6 contracts incomplete

Fixed:

- controller contract has D1–D8 invariants and design statuses;
- permission contract separates design-doc/prototype/visual-evidence authority;
- P6 role table includes Design Engineer/Reviewer and design context.

### H-DESIGN-03 — specification did not pin design identity

Fixed: specification skill/template reference frozen design identity and UX-critical constraints without duplicating root design system.

### H-DESIGN-04 — implementation did not formally consume Project/Design context

Fixed: implementation now confirms `AREA_CONTEXT_SET`, `IC-xx`, design identity and `DESIGN_CONTEXT_SET` before writing and stops on interface/design identity changes.

### H-DESIGN-05 — reports lost design identity/evidence

Fixed: implementation report, review package, review report and verification report carry the required Project/Design boundaries and evidence axes.

### H-DESIGN-06 — Design Reviewer could inflate agent budget

Fixed: balanced uses combined reviewer; maximum-quality still has only two reviewer slots after implementer. A named Design Reviewer consumes one existing slot.

### H-DESIGN-07 — behavioral coverage was concentrated in design skill only

Fixed: specification/implementation/review/verification suites now contain required cross-skill design cases, and `check_dev_05_behavioral_contracts.py` requires them.

### H-DESIGN-08 — docs/CI validation sequence drift

Fixed: root/package README, design plan, changelog and workflow all describe the four-layer development validation pipeline.

## 8. Browser / Design / G4 independence

Required relation:

```text
Automated Browser E2E
        !=
Visual Design Check
        !=
G4 Blind Acceptance
```

G4 is explicitly contaminated if it receives spec/manifest/plan/Project Intelligence/`DESIGN.md`/prototype/design-review/visual-report/progress/dashboard claims.

Verdict: `STATIC PASS / dedicated verification eval coverage / NATIVE PENDING`.

## 9. Permission and security integration

Confirmed static invariants:

- design state is not authority;
- design-doc write != product write;
- prototype write != production integration;
- browser interaction != test-data mutation;
- runtime observation != process action;
- Design Reviewer is read-only;
- design cannot weaken U/S/security/privacy/accessibility/IC contracts;
- UI library recommendation != dependency/network authority;
- personal browser profile remains invalid test context;
- one-writer and one-fixer-wave remain in force.

Verdict: `STATIC PASS`.

## 10. Budget integration

- maximum speed remains for genuinely low-risk bounded work;
- balanced: implementer + one combined reviewer, max two unique agents;
- maximum quality: implementer + two reviewer slots, max three unique agents;
- Design Reviewer never creates a fourth agent;
- prototype/design high-judgment turns consume budget;
- visual verification is read-only evidence and does not create another fixer wave.

Verdict: `STATIC PASS`.

## 11. Deterministic validation pipeline

Current workflow is configured for Python 3.11:

```text
validate_dev_05.py --self-test
→ check_dev_05.py
→ check_dev_05_behavioral_contracts.py
→ doctor_dev_05.py
```

### What each layer protects

`validate_dev_05.py`
- all original package/security/manifest/eval/link/secret/symlink/offline/self-test checks;
- exact development inventory extended to 11 skills and 11 Codex wrappers.

`check_dev_05.py`
- static cross-component presence/wiring from Build through controller/design/spec/plan/implement/review/verify/finish/recovery/dashboard;
- exact skill/wrapper inventory;
- Project and Design core eval coverage;
- dashboard state↔HTML contract.

`check_dev_05_behavioral_contracts.py`
- required design cases in specification/implementation/review/verification;
- reviewer-budget design markers;
- explicit CI linkage of all four validation layers.

`doctor_dev_05.py`
- read-only/offline development-aware package diagnostics.

### Observed result limitation

For audited snapshot `4db55ec...`, the available GitHub combined-status endpoint returns an empty legacy status list. The available workflow-run wrapper in this environment only exposes PR-triggered runs, while these development commits are push-triggered. Therefore this audit does **not** fabricate an Actions PASS/FAIL result.

Verdict: `CONFIGURED; EXECUTION RESULT NOT OBSERVABLE HERE`.

## 12. Native evidence status

### Existing evidence

An earlier Codex TaskLedger run proved important core behavior:

- SOURCE_BRIEF/U tracking;
- G2/G3;
- RED→GREEN;
- independent review + one fix + targeted re-review;
- persistence across separate processes;
- G4 detecting an acceptance limitation;
- permission boundaries;
- honest `PARTIALLY_VERIFIED / DEGRADED` instead of false COMPLETE.

That run predates final Browser/Project/Design wiring and cannot be reused as proof for them.

### Still required

D10 disposable full-stack native acceptance must prove in one current-snapshot run:

1. real topology without fake areas;
2. root `DESIGN.md` and design identity;
3. Apple-inspired UX principles without forced Apple styling;
4. prototype divergence for intentionally ambiguous direction;
5. `AREA_CONTEXT_SET` + `DESIGN_CONTEXT_SET`;
6. shared frozen `IC-xx`;
7. spec → plan → implementation preserves design identity;
8. specialist routing without budget inflation;
9. Runtime Map permission boundaries;
10. repository-native Browser E2E;
11. independent Design Review;
12. Visual Design Check on representative desktop/mobile/states;
13. G4 with design artifacts forbidden;
14. Design Drift + Documentation Drift gates;
15. Russian dashboard with Project/Design Intelligence and truthful metrics;
16. recovery/resume from durable state rather than conversation.

Verdict: `NATIVE PENDING`.

## 13. Release decision

Do **not** merge/release as `0.5.0` based only on this audit.

Release proposal requires:

```text
final-head deterministic validation PASS
+ observable CI result
+ current-snapshot full-stack native acceptance
+ native evidence for each host claimed in release docs
+ version/marketplace/root-eval metadata bump to 0.5.0
+ publisher/security release metadata review
```

Until then the honest state is:

```text
0.5 DEVELOPMENT PREVIEW
IMPLEMENTATION: COMPLETE FOR CONFIRMED SCOPE
STATIC WIRING: PASS BY AUDIT
NATIVE VALIDATION: PENDING
```
