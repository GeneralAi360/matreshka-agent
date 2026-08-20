# Implementation Plan — Matreshka Agent 0.5 Project Intelligence Layer

- Status: `IMPLEMENTED_PENDING_NATIVE_VALIDATION`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-project-intelligence-layer-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: development branch only; no merge to `main` or `0.5.0` release claim from this plan.

## Goal

Implement a portable Project Intelligence Layer for the existing Matreshka controller: current project topology, area-scoped context routing, shared cross-area interface contracts, safe runtime mapping, documentation-drift control, and bounded specialist role routing.

## Task map

| Task | Status | Result | Main files | Remaining gate |
| --- | --- | --- | --- | --- |
| `P1` | `IMPLEMENTED` | `PROJECT_TOPOLOGY` and reusable profile shape | project-intelligence reference, project-profile reference/template | native full-stack topology proof |
| `P2` | `IMPLEMENTED` | `AREA_CONTEXT_SET` routing into task briefs/dispatch | controller, task brief, dispatch/report templates | native context-isolation proof |
| `P3` | `IMPLEMENTED` | Controller-owned/frozen `IC-xx` contracts for cross-area seams | interface-contract template, planner/controller/reviewer | native producer/consumer proof |
| `P4` | `IMPLEMENTED` | Safe `RUNTIME_MAP` with ownership/permission separation | project-intelligence, controller, permission/ledger | native runtime ownership proof |
| `P5` | `IMPLEMENTED` | Documentation impact/drift gate after verified behavior | project-intelligence, finish, ledger/handoff | native docs-drift proof |
| `P6` | `IMPLEMENTED` | Specialist role archetypes without authority/budget inflation | controller/planner/task/dispatch/review | native routing proof |
| `P7` | `IMPLEMENTED` | Project Intelligence observable/recoverable | ledger, dashboard state/html, recovery | native projection/recovery proof |
| `P8` | `STATIC_HARDENING_IMPLEMENTED` | deterministic integrity check + CI wiring + docs/evals | `scripts/check_dev_05.py`, workflow, README, eval suite | CI evidence + native acceptance |

## P1 — Project Topology

Read-only discovery identifies real architectural areas instead of assuming a frontend/backend template. Each area can record ID, kind, purpose, roots, entry points, verified commands/source, produced/consumed interfaces, state/data ownership, security/trust boundary, applicable instructions and freshness identity.

A full-stack repository may expose `AREA-FRONTEND`, `AREA-BACKEND`, `AREA-DATA`, `AREA-E2E`; a small CLI may remain one/two cohesive areas. Area count is descriptive and never creates permissions or agent budget.

## P2 — Area Context Router

Every controller-dispatched task receives a bounded `AREA_CONTEXT_SET`: task-local U/S requirements, primary area, only necessary adjacent interfaces/invariants, exact paths/commands and security/data/runtime facts. Unrelated area history/docs/reports/raw logs/full source brief/full branch diff are excluded.

If correctness cannot survive context reduction, controller returns `CONTEXT_TOO_BROAD` or splits the work instead of hiding dependencies.

## P3 — Cross-Area Interface Contract

For real producer/consumer seams the controller creates one shared `IC-xx` before dependent writer dispatch. Default run-local path:

```text
.matreshka/runs/<run-id>/interfaces/IC-xx-<safe-slug>.md
```

Producer and consumers pin the same contract identity/hash. Material change after freeze returns `INTERFACE_CHANGED` to controller reconciliation. Single-area internal helper seams do not receive decorative contracts.

## P4 — Runtime Map

Runtime state records verified service/process ownership, start/stop/status/log commands, evidenced ports/sockets, environment class and mutation implications. Read-only observation never grants process start/stop/kill, port bind, network, test-data or destructive authority.

Unknown ownership of an occupied port produces an exact blocker/context request, not broad process killing.

## P5 — Documentation Drift Gate

After fresh technical/security verification and before clean finish, controller classifies:

```text
DOCS_NOT_REQUIRED
DOCS_CURRENT
DOCS_UPDATE_REQUIRED
DOCS_BLOCKED
DOCS_CONFLICT
```

Durable public/interface/topology/runtime/persistence/security/env/test/deploy/user-workflow truth is checked. Private refactors normally return `DOCS_NOT_REQUIRED`. Required documentation updates are docs-only, evidence-backed and separately authorized.

## P6 — Specialist Role Routing

Supported role archetypes reuse existing Matreshka skills:

- `GENERAL_IMPLEMENTER`
- `FRONTEND_IMPLEMENTER`
- `BACKEND_IMPLEMENTER`
- `DATA_MIGRATION_IMPLEMENTER`
- `UI_SPECIALIST`
- `TEST_E2E_SPECIALIST`
- `DOCUMENTATION_MAINTAINER`
- `BROWSER_CHECKER`
- `REMOTE_OPERATOR`
- `FILE_TRANSFER_OPERATOR`

They narrow responsibility/context but never create extra skill identity, agent-turn budget, filesystem scope or permissions. Execution-only operators return evidence and cannot decide follow-up actions.

## P7 — State, recovery and dashboard

Ledger/run state now preserves compact topology, affected/current area, context guarantee, active interface identities, runtime map state, docs drift and current specialist. Recovery revalidates stale topology/interface/runtime/profile facts against the current repository before reuse.

The Russian dashboard can display Project Intelligence compactly but remains a projection and cannot dispatch work, grant authority or satisfy a verification gate.

## Static hardening completed

The development branch now contains:

- `skills/orchestrating-subagent-work/references/project-intelligence.md`;
- `skills/orchestrating-subagent-work/assets/project-intelligence-template.md`;
- `skills/orchestrating-subagent-work/assets/interface-contract-template.md`;
- integration in controller, controller-contract, permission/ledger, planner, plan/task/dispatch/report templates, reviewer, finish/handoff, project profile and dashboard;
- a 14-case Project Intelligence adversarial suite;
- `scripts/check_dev_05.py`, which checks required 0.5 files, cross-skill markers, JSON syntax and key Project Intelligence cases;
- GitHub Actions execution of package validator/self-test, 0.5 integrity checker and doctor on `dev/**`/`main` pushes and PRs.

During hardening an actual compatibility defect was found and fixed: the richer Codex Build wrapper/default prompt had diverged from the current 0.4 package validator's expected `[TASK]` hint/canonical skill token. The UX remains rich in the wrapper body/card while static validator compatibility is restored.

## Adversarial coverage

The dedicated suite covers at least:

1. real full-stack topology;
2. CLI without fake frontend/backend split;
3. interface freeze before producer/consumer work;
4. interface drift mid-run;
5. narrow area context;
6. unknown process/port ownership;
7. observe-runtime without start permission;
8. public contract docs drift;
9. private refactor with no docs work;
10. UI-specialist boundary;
11. no agent-budget inflation from area count;
12. execution-only remote operator;
13. recovery from stale topology/interface cache;
14. documentation conflict without write authority.

## Remaining native gate

Project Intelligence is implemented and statically hardened, but `0.5.0` is not claimed until a disposable native full-stack acceptance run proves the actual host behavior:

```text
frontend + backend + data/E2E topology
→ frozen IC contract
→ narrow area contexts
→ specialist routing within budget
→ runtime observation/permissions
→ Playwright/browser evidence
→ G4
→ docs drift
→ Russian dashboard
```

The native test must audit artifacts/evidence rather than trusting the controller's self-reported PASS.

## Current checkpoint

`P1`–`P7`: `IMPLEMENTED`.

`P8`: static hardening is implemented; observable CI result and native full-stack acceptance remain external evidence gates.

No merge to `main`, package version bump, publication or release claim has been performed by this plan.
