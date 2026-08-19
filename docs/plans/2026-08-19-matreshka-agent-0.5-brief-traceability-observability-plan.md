# Implementation Plan — Matreshka Agent 0.5 Brief Traceability & Observability

- Status: `PHASED_PLAN`
- Specification: `docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md`
- Baseline: `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Branch: `dev/0.5-brief-traceability-observability`
- Current delivery policy: implement on the development branch; do not merge to `main` in this plan.

## Goal

Add a user-intent traceability layer and a safe live run projection on top of the existing 0.4 controller without weakening permission, Security by Design, independent review, fresh verification, recovery, or finish boundaries.

## Task map

| Task | Result | Primary files | Gate |
|---|---|---|---|
| `T1` | Source-brief, `U-` manifest, G1–G4, observability contracts and templates | new references/assets under `building-end-to-end` | internal-link/package structure check |
| `T2` | Build End-to-End passes original intent; controller owns materialization, gates, projection and recovery | `building-end-to-end/SKILL.md`, `orchestrating-subagent-work/SKILL.md` | focused scenario review |
| `T3` | State machine and ledger make traceability/recovery explicit | controller contract, ledger contract/template | recovery + stale-dashboard adversarial cases |
| `T4` | Planner/reviewer/verifier consume `U-` rows without weakening `S-` evidence | planning, review, verify contracts and evals | G2/G3/G4 negative scenarios |
| `T5` | Complexity tiers and optional run-local interface map reduce task/context overhead without unsafe parallel writers | planning/controller references | task-sizing evals |
| `T6` | 0.5 package/version/docs/evals/native smoke | manifests, validator, root evals, changelog, READMEs | full offline self-test + native handoff |

## T1 — Contracts and artifacts

Create:

- `skills/building-end-to-end/references/brief-traceability.md`
- `skills/building-end-to-end/references/run-observability.md`
- `skills/building-end-to-end/assets/source-brief-template.md`
- `skills/building-end-to-end/assets/requirement-manifest-template.md`
- `skills/building-end-to-end/assets/dashboard-state-template.js`
- `skills/building-end-to-end/assets/dashboard-template.html`

Rules:

- source brief is redacted, immutable run state, not committed by default;
- user-intent IDs use `U-` and security IDs remain `S-`;
- only user authority can `DROPPED` a row;
- dashboard is a projection and has no authority;
- dashboard does not itself authorize serving/opening/network activity.

## T2 — Entry/controller integration

`building-end-to-end`:

- preserve the original user request and material product decisions for structured controller handoff;
- do not write source-brief/run files itself;
- do not widen permissions because a user selected a less interactive mode.

`orchestrating-subagent-work`:

- after bounded state-write permission and ledger initialization, materialize the source brief and requirement manifest;
- run G1 before specification completion;
- run G2 in a fresh independent context before planning;
- run G3 before first implementation dispatch;
- include task-local `U-` rows/quotes in implementation/review packages;
- keep existing technical/security verification;
- run G4 only afterward;
- update dashboard projection only from controller-owned state;
- block `COMPLETE` on material intent drift.

## T3 — Durable recovery

Add explicit ledger fields for:

- source brief path/hash;
- requirement manifest path/hash;
- `U-` status counts;
- G1/G2/G3/G4 state;
- blind-acceptance report;
- dashboard projection path/status;
- last verified checkpoint and exact next action.

Recovery order remains actual state/evidence first. Dashboard and requirement status claims are reconciled; neither is trusted blindly.

## T4 — Downstream skill integration

Planning:

- coverage matrix includes `U-` and `S-` rows;
- no orphan `U-` and no unjustified product task.

Review:

- task review receives the exact relevant `U-` quote in addition to spec/task acceptance;
- source requirement narrowing is Important unless explicit user/deferred authority says otherwise.

Verification:

- existing technical/security verification remains unchanged in strength;
- define a fresh-context blind-acceptance protocol with intentionally restricted inputs;
- blind checker reports only observable delivery status and never fixes.

## T5 — Cost/complexity hardening

After traceability is stable, add a complexity tier independent of execution profile:

- `T0`: no subtask decomposition when one context is safely sufficient;
- `T1`: about 2–3 reviewable tasks;
- `T2`: about 4–8;
- `T3`: about 9–16;
- above the safe ceiling: `SPLIT_REQUIRED`.

The numeric tier is a decomposition budget, not a safety profile. High-risk T0 work may still require maximum quality. Parallel writers remain disabled in one checkout; any future parallel writer support requires separately authorized isolated workspaces and additional evals.

Add a controller-owned run-local interface map only if evidence shows cross-task reinvention is material.

## T6 — Release hardening

Before a `0.5.0` release claim:

- resolve the existing `docs/...` vs `docs/matreshka/...` path inconsistency;
- add CI for package validator/self-test/doctor;
- complete publisher/security metadata or explicitly keep development-preview status;
- add workflow/adversarial cases for G1–G4, secret/private brief handling, stale dashboard, dropped-authority, and blind-check contamination;
- run native smoke tests on each claimed host;
- compare plain-agent / minimal-controller / full-candidate cost and acceptance results.

## Stop conditions

- A brief artifact would require storing a secret/private payload outside the approved state boundary.
- G2/G4 cannot be made independent on the active host and the risk makes a procedural restriction insufficient.
- Requirement traceability starts acting as permission or business truth rather than provenance.
- Dashboard requires new network/process authority that the user did not grant.
- Adding traceability materially weakens technical/security verification or independent review.

## Current execution checkpoint

This development pass starts with `T1` and `T2`. `T3`–`T6` remain explicit subsequent tasks rather than being silently folded into the first change unit.