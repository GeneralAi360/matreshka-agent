# Implementation Plan — Matreshka Agent 0.5 Brief Traceability & Observability

- Status: `IN_PROGRESS`
- Specification: `docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md`
- Baseline: `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Branch: `dev/0.5-brief-traceability-observability`
- Current delivery policy: implement on the development branch; do not merge to `main` in this plan.

## Goal

Add a user-intent traceability layer and a safe live run projection on top of the existing 0.4 controller without weakening permission, Security by Design, independent review, fresh verification, recovery, or finish boundaries.

## Task map

| Task | Status | Result | Primary files | Gate |
|---|---|---|---|---|
| `T1` | `IMPLEMENTED` | Source-brief, `U-` manifest, G1–G4, observability contracts and templates | new references/assets under `building-end-to-end` | static/package validation pending |
| `T2` | `IMPLEMENTED` | Build End-to-End passes original intent; controller owns materialization, gates, projection and recovery | `building-end-to-end/SKILL.md`, `orchestrating-subagent-work/SKILL.md` | behavior/native execution pending |
| `T3` | `IMPLEMENTED` | State machine and ledger make traceability/recovery explicit | controller contract, permission/ledger contract/template | recovery/native execution pending |
| `T4` | `IMPLEMENTED` | Planner/reviewer/verifier consume `U-` rows without weakening `S-` evidence; blind verifier mode is separate | planning, review, verify contracts and evals | behavior/native execution pending |
| `T5` | `PARTIAL` | Complexity tier implemented; optional run-local interface map intentionally deferred until reinvention evidence justifies it | planning complexity reference + plan skill/evals | task-sizing behavior pending |
| `T6` | `PENDING` | 0.5 package/version/docs/root evals/CI/native smoke | manifests, validator, root evals, changelog, READMEs, workflow | full offline self-test + native handoff |

## T1 — Contracts and artifacts

Implemented:

- `skills/building-end-to-end/references/brief-traceability.md`
- `skills/building-end-to-end/references/run-observability.md`
- `skills/building-end-to-end/assets/source-brief-template.md`
- `skills/building-end-to-end/assets/requirement-manifest-template.md`
- `skills/building-end-to-end/assets/dashboard-state-template.js`
- `skills/building-end-to-end/assets/dashboard-template.html`

Rules:

- source brief is redacted, immutable run state, not committed by default;
- user-intent IDs use `U-` and security IDs remain `S-`;
- only user authority can set `DROPPED`;
- dashboard is a projection and has no authority;
- dashboard does not itself authorize serving/opening/network activity.

## T2 — Entry/controller integration

Implemented in `building-end-to-end`:

- preserve the original user request and material product decisions for structured controller handoff;
- pass `SOURCE_BRIEF` without paraphrase loss and `SOURCE_DECISIONS` separately;
- do not write source-brief/run files from the wrapper;
- do not widen permissions because a user selected a less interactive mode or requested a dashboard.

Implemented in `orchestrating-subagent-work`:

- after bounded state-write permission and ledger initialization, materialize the source brief and requirement manifest;
- run G1 before specification completion;
- run G2 in a fresh independent context before planning;
- run G3 before first implementation dispatch;
- include task-local `U-` rows/quotes in implementation/review packages;
- keep existing technical/security verification mandatory;
- run G4 only afterward;
- update dashboard projection only from controller-owned state;
- block `COMPLETE` on material intent drift.

## T3 — Durable recovery

Implemented:

- explicit `ACCEPTANCE` state after technical `VERIFY` and before `FINISH`;
- source brief path/hash;
- requirement manifest path/hash;
- `U-` status counts;
- G1/G2/G3/G4 state;
- blind-acceptance report;
- dashboard projection path/status;
- last verified checkpoint and exact next action;
- recovery order that validates actual state/evidence before ledger, source intent, and projections.

Canonical path ambiguity was removed from the controller permission contract:

```text
docs/context.md | compatible existing CONTEXT.md
docs/specs/
docs/plans/
docs/adr/
docs/runs/<run-id>/progress.md
.matreshka/runs/<run-id>/...
.matreshka/learning/candidates/
```

Remaining README/documentation references to the older `docs/matreshka/...` wording are a T6 cleanup item, not controller authority.

## T4 — Downstream skill integration

Planning now:

- includes `U-` and `S-` rows in coverage;
- enforces G3 forward/backward mapping;
- rejects orphan `U-` and unjustified product tasks.

Review now:

- receives the exact relevant `U-` quote in addition to spec/task acceptance;
- treats material source-requirement narrowing as Important unless a valid current user/deferred decision says otherwise;
- never changes requirement status itself.

Verification now:

- keeps normal technical/security verification unchanged in strength;
- adds a separate fresh-context blind-acceptance mode with intentionally restricted inputs;
- rejects contaminated blind packages that contain spec/manifest/task/report interpretations;
- reports only observable delivery status and never fixes.

Focused eval contracts were added for source-brief handoff, later-user-decision history, dashboard authority, blind drift detection, remote-only blind evidence, and blind-context contamination.

## T5 — Cost/complexity hardening

Implemented complexity tier independent of execution profile:

- `T0`: one direct reviewable task; no artificial decomposition;
- `T1`: about 2–3 reviewable tasks;
- `T2`: about 4–8;
- `T3`: about 9–16;
- above the safe ceiling: `SPLIT_REQUIRED` / `DECISION_MAP_REQUIRED`.

The numeric tier is a decomposition budget, not a safety profile. High-risk T0 work may still require maximum quality. Parallel writers remain disabled in one checkout.

A mandatory merge pass removes task boundaries that add cold-start/context cost without independent review, rollback, evidence, security, or ownership value.

Focused eval contracts cover long-spec T0, high-risk T0 + maximum quality, and >16 independent-task split behavior.

Deferred by design: a controller-owned run-local interface map. Add it only if native/baseline runs show cross-task reinvention is a material cost/quality problem; do not create a new state artifact solely because Autopilot has one.

## T6 — Release hardening

Before a `0.5.0` release claim:

- finish README/changelog cleanup for the unified canonical paths;
- add CI for package validator/self-test/doctor;
- update versioned manifests/marketplaces/validator only when the 0.5 scope is release-ready;
- complete publisher/security metadata or explicitly keep development-preview status;
- add root workflow/adversarial cases for G1–G4, private brief handling, stale dashboard, dropped-authority, and blind-check contamination;
- run package validator/self-test/doctor against the complete branch;
- run native smoke tests on each claimed host;
- compare plain-agent / minimal-controller / full-candidate cost and acceptance results.

## Stop conditions

- A brief artifact would require storing a secret/private payload outside the approved state boundary.
- G2/G4 cannot be made independent on the active host and the risk makes a procedural restriction insufficient.
- Requirement traceability starts acting as permission or business truth rather than provenance.
- Dashboard requires new network/process authority that the user did not grant.
- Adding traceability materially weakens technical/security verification or independent review.
- Complexity-tier pressure would merge genuinely independent security/data boundaries merely to hit a number.

## Current execution checkpoint

`T1`–`T4` are implemented at the instruction/contract/eval-definition layer on the development branch. `T5` complexity tier is implemented; the interface-map half is deliberately evidence-gated. `T6` remains the release-hardening phase.

No merge to `main`, package publication, deploy, or native-host success claim has been performed by this plan.