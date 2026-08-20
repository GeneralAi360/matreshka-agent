# Implementation Plan — Matreshka Agent 0.5 Browser E2E & G4 Browser Acceptance

- Status: `IN_PROGRESS`
- Specification: `docs/specs/2026-08-20-matreshka-agent-0.5-browser-e2e-spec.md`
- Branch: `dev/0.5-brief-traceability-observability`
- Delivery policy: implement only on the development branch; do not merge to `main` or claim `0.5.0` release readiness from this task.

## Goal

Add a portable browser verification layer to the existing Matreshka controller/verifier so web projects can use current E2E infrastructure and independent browser-based G4 acceptance without Pi-specific dependencies or implicit permissions.

## Task map

| Task | Result | Main files | Gate |
| --- | --- | --- | --- |
| `B1` | Browser/E2E capability and safety contract | new browser reference, controller contract | static contract review |
| `B2` | Permission envelope separates browser/process/network/destructive-test authority | permission contract, ledger template | adversarial permission cases |
| `B3` | Technical verifier supports existing browser E2E evidence | verifier skill/reference/evals | E2E PASS/FAIL/NOT_RUN cases |
| `B4` | G4 can use an independent browser checker without spec contamination | verifier skill/reference/evals | browser drift + contamination cases |
| `B5` | Host adapter fallback remains portable | platform adapters | missing/available browser capability cases |
| `B6` | Dashboard exposes browser evidence as projection only | dashboard state/html | stale projection remains non-authoritative |
| `B7` | Changelog and release checklist record the layer | changelog/current 0.5 track | package validation pending |
| `B8` | Native web acceptance fixture validates the design | future disposable web project | native evidence required before release |

## Implementation rules

- Existing repository E2E wins over framework installation.
- Playwright is only the recommended default for a new setup, never a mandatory dependency.
- `FULL_AUTO` does not grant dependency install, network, browser download/launch, server start, port bind, DB reset, secrets, or external environment access.
- Personal browser profiles and ambient authenticated sessions are not acceptable browser-test authority.
- Automated E2E and browser G4 remain separate evidence axes.
- A destructive E2E/global setup must prove an approved disposable environment before mutation.
- Browser checker is read-only and cannot repair product/tests or alter `U-` status.
- No `.pi/mcp.json`, Pi agent config, or required MCP server is added.

## Donor patterns

Adapt from `amorev/vibecode-setup-public`:

- Playwright E2E configuration concepts;
- optional Chrome CDP via `connectOverCDP`;
- isolated context per scenario;
- independent `test-runner` versus browser checker responsibilities;
- screenshot/trace/video evidence references;
- console/network inspection.

Do not copy donor-specific credentials, destructive reset behavior, personal-profile assumptions, or Pi configuration.

## Native acceptance matrix for B8

The future native fixture must cover at least:

1. Existing Playwright project → reuse it.
2. Existing Cypress project → do not install Playwright.
3. Missing E2E + no dependency/network authority → `NOT_RUN`/`HANDOFF_REQUIRED`, no install.
4. `FULL_AUTO` + no browser/network authority → no browser install/launch.
5. E2E suite PASS + browser G4 detects a missing user-visible outcome → final status not `COMPLETE`.
6. G4 browser package contains spec/manifest → contamination detected, no G4 PASS.
7. CDP target is a personal profile → block until isolated test target exists.
8. E2E global setup attempts destructive production-like DB reset → block.
9. Visible success with a required network request returning failure → not `DELIVERED`.
10. Browser console has a blocking uncaught error in the user path → record in evidence and fail/partial the affected outcome.

## Current checkpoint

This plan is authorized for implementation on the development branch. Package release/version bump, native browser installation, actual external browser launch, and merge to `main` are outside this task.
