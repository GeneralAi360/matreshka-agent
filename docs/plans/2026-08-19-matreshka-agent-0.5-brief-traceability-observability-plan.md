# Implementation Plan — Matreshka Agent 0.5 Brief Traceability & Observability

- Status: `IMPLEMENTED_PENDING_NATIVE_RELEASE_VALIDATION`
- Specification: `docs/specs/2026-08-19-matreshka-agent-0.5-brief-traceability-observability-spec.md`
- Baseline: `7249a56e9afb5f5b70e56ddd0dc272e6bdab9ea0`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only until native/release gates pass; do not merge to `main` or claim `0.5.0` from this plan alone.

## Goal

Add source-intent traceability, safe observability, bounded decomposition and the supporting browser/project-intelligence layers on top of the 0.4 controller without weakening permission, Security by Design, independent review, fresh verification, recovery or finish boundaries.

## Current task map

| Task | Status | Result | Remaining external evidence |
| --- | --- | --- | --- |
| `T1` | `IMPLEMENTED` | Source brief, `U-` manifest, G1–G4, observability contracts/assets | latest native regression |
| `T2` | `IMPLEMENTED` | Build End-to-End → namespaced controller, public modes/scenarios | latest native launch UX |
| `T3` | `IMPLEMENTED` | state machine/ledger/recovery/permissions | latest recovery acceptance |
| `T4` | `IMPLEMENTED` | planner/reviewer/verifier consume U/S and blind G4 independently | latest native role isolation |
| `T5` | `IMPLEMENTED` | T0–T3 complexity + evidence-scoped cross-area `IC-xx` contracts | full-stack native proof |
| `T6` | `STATIC_HARDENING_IMPLEMENTED` | CI, deterministic validators, current package docs, dev integrity check | observable CI + native host acceptance + version/publisher release step |

## T1 — Source intent and observability

Implemented:

- redacted immutable run-local source brief;
- stable `U-` user-intent namespace separate from `S-` security requirements;
- G1 clarification completeness;
- G2 fresh brief→spec coverage;
- G3 bidirectional requirement/task/proof traceability;
- G4 fresh blind acceptance with restricted inputs;
- Russian dependency-free dashboard projection;
- exact/partial/unavailable timing and token observability semantics.

The dashboard is a projection only. It cannot grant permissions, prove tests, override ledger/evidence, start a server, bind a port, launch a browser or authorize external effects.

## T2 — Launch UX and scenarios

Public interaction modes:

```text
INTERVIEW
ASSISTED
FULL_AUTO
```

Project scenarios:

```text
NEW_PROJECT
CONTINUE_PROJECT
EXISTING_PROJECT
```

Internal controller autonomy remains separate. `FULL_AUTO` never implies `EXTENDED_AUTONOMOUS`, Git, network, dependency/browser install, secrets, deploy, destructive/test-data or remote authority.

Codex build card/wrapper explains the simple modes/scenarios in Russian and routes to the namespaced Matreshka Build End-to-End/controller chain.

## T3 — Durable state and recovery

Implemented:

- explicit `ACCEPTANCE` state between `VERIFY` and `FINISH` when G4 applies;
- baseline, source brief/manifest identity, G1–G4 state, current verification evidence and exact next action;
- project/browser/observability mismatch fields;
- canonical run state under `.matreshka/runs/<run-id>/`;
- recovery order that validates actual state/fresh evidence before projections;
- no automatic migration of old ledgers without exact state-write authority.

## T4 — Downstream engineering integration

Planning:

- maps every live U/S to tasks/proofs and each product task back to a source;
- uses exact paths/commands;
- preserves Security by Design and negative proofs;
- integrates current Project Intelligence when multi-area coordination is relevant.

Review:

- receives task-local U quotes, frozen `IC-xx`, scoped diff and evidence;
- detects source-intent narrowing, interface drift, specialist-boundary violations and security/correctness regressions;
- remains read-only and never fixes.

Verification:

- technical/security evidence remains mandatory;
- Browser E2E is a technical evidence axis when applicable;
- G4 is a separate restricted-input acceptance axis;
- `E2E PASS` cannot override `G4 FAIL/PARTIAL`.

Finish:

- requires verified current state and applicable docs-drift resolution;
- executes only explicitly authorized Git/remote actions;
- produces a Russian human-facing handoff with timing/token limitations when available.

## T5 — Complexity and Project Intelligence

Complexity tiers remain independent from profile/permissions:

- `T0`: one direct reviewable task;
- `T1`: normally 2–3;
- `T2`: normally 4–8;
- `T3`: normally 9–16;
- above safe T3: `SPLIT_REQUIRED` / `DECISION_MAP_REQUIRED`.

The previously deferred interface-map question is now resolved by Project Intelligence P3: Matreshka does **not** create a global decorative interface map. It creates/fixes `IC-xx` only when current evidence shows a real producer/consumer seam whose assumptions can drift. That gives the coordination benefit without adding state/token cost to single-area tasks.

Project Intelligence P1–P6 is implemented as a supporting controller layer:

```text
PROJECT_TOPOLOGY
AREA_CONTEXT_SET
CROSS_AREA_INTERFACE_CONTRACT
RUNTIME_MAP
DOCUMENTATION_DRIFT_GATE
SPECIALIST_ROLE_ROUTING
```

See `docs/plans/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-plan.md` for the detailed status.

## Browser/E2E supporting layer

Browser/E2E implementation B1–B7 is present at the instruction/contract/eval/projection layer. It prefers existing project E2E, separates browser/process/port/test-data permissions, forbids ambient personal browser profiles, and makes Browser G4 independent from technical E2E.

The disposable native web acceptance fixture remains a release evidence gate, not an implementation gap.

## T6 — Static hardening completed

The branch now has:

- `.github/workflows/package-validation.yml` for `main`, `dev/**` and PRs;
- `validate_package.py --self-test` for package shape/security/negative fixtures;
- `check_dev_05.py` for 0.5 component presence/cross-skill wiring/Russian dashboard/Browser/Project Intelligence/eval JSON integrity;
- read-only `doctor.py`;
- current package README for the 0.5 development architecture;
- dedicated Browser and Project Intelligence adversarial evals;
- compatibility between current Codex Build UX and the still-0.4 versioned package validator.

### Hardening finding fixed

The audit found a real static incompatibility: the richer `matreshka-build` argument hint and namespaced Codex default prompt no longer matched the existing 0.4 package validator's `[TASK]`/canonical-token requirements. The wrapper/card were adjusted so the validator contract and new user UX coexist.

## Native evidence already obtained

An earlier Codex TaskLedger acceptance against an older 0.5 development snapshot exercised the core source-intent chain and correctly ended `PARTIALLY_VERIFIED / DEGRADED`, not false `COMPLETE`, because required Python 3.11/native-verifier evidence was unavailable. It also proved persistence behaviorally and showed G2/G3/review/G4 operation.

That run is useful evidence for core behavior, but it does **not** validate the later Browser/E2E, Project Intelligence or updated dashboard changes.

## Remaining release gates — not implementation gaps

Before an actual `0.5.0` release claim:

1. observe successful CI for the final development HEAD;
2. run the latest deterministic package/self-test + 0.5 integrity + doctor on the final checkout;
3. run a disposable full-stack native acceptance exercising topology, IC contracts, area contexts, specialist routing, runtime map, E2E/Browser G4, docs drift and Russian dashboard;
4. run/record native smoke evidence for each host actually claimed in release documentation;
5. only then bump manifests/marketplaces/validator/doctor/root eval version from `0.4.0` to `0.5.0`;
6. finish publisher/security metadata required for public release.

Version bump is deliberately last so an unvalidated development branch cannot masquerade as a released 0.5 package.

## Stop conditions retained

- source/run artifacts would expose secrets/private payloads;
- G2/G4 cannot be made independent where the risk requires it;
- Project Intelligence or dashboard state is treated as permission/truth instead of revalidated context;
- interface/runtime/docs pressure would weaken security or evidence gates;
- task-count optimization would merge genuinely independent data/security boundaries;
- missing browser/process/test-data authority is silently substituted with setup actions.

## Current checkpoint

Implementation/static hardening of the 0.5 development scope is complete on the branch.

What remains is **external execution evidence and release publication work**, not missing P1–P6/G1–G4/Browser/dashboard code-contract components.

No merge to `main`, package publication or `0.5.0` version claim has been performed.
