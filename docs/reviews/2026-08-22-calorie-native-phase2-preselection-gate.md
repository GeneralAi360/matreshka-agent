# Matreshka Agent 0.5 — Calorie Native Phase 2: Prototype Preselection Gate

- Date: 2026-08-22
- Branch: `dev/0.5-brief-traceability-observability`
- Native host: Codex
- Test project: `matreshka-calorie-acceptance-v2`
- Status: `HARDENED_PENDING_NATIVE_RETEST`

## Native evidence

The v2 run correctly proved the previous Phase-1 fixes:

- `PRODUCT_UI_LOCALE=ru-RU` was resolved before prototype copy;
- durable run state existed before prototype writes;
- `stateIntegrity=VALID`;
- ordinary local SQLite CRUD/settings correctly classified `S-ATOMIC-EFFECT=N/A`;
- all five automatic security families were classified explicitly;
- root `DESIGN.md` remained draft/unfrozen while `DESIGN_DIRECTION_REQUIRED`;
- production implementation did not start.

However the controller presented three prototype directions to the user and asked for a choice after only static prototype sanity. A later read-only audit found all three candidates materially unready:

1. `Дневная лента` — horizontal overflow/cropping at 390px; generic cream-shell slop; fake add action.
2. `Баланс цели` — cramped/cropped compact state and right-side mobile clipping; generic worksheet/dashboard composition; reusable outside calorie tracking.
3. `Полки приёмов` — two-column mobile clipping; generic rounded-card grid/color variation; fake actions.

The audit also found focus-visible unproven. No layered/select/menu controls were present, so the layered-control row was correctly `NOT_APPLICABLE`.

Reported gate state:

```text
PROTOTYPE_1_ANTI_SLOP=CHANGES_REQUIRED
PROTOTYPE_2_ANTI_SLOP=CHANGES_REQUIRED
PROTOTYPE_3_ANTI_SLOP=CHANGES_REQUIRED
MOBILE_RENDER_CHECK=FAIL
DESIGN_PROTOTYPE_GATE=FAIL
STATE_INTEGRITY=VALID
PRODUCTION_IMPLEMENTATION_STARTED=NO
```

## Root cause

The design contracts contained anti-slop and pre-user verification language, but orchestration did not make the verification result a hard prerequisite for emitting the user-choice question. The effective native sequence was:

```text
generate prototypes
-> static sanity
-> ask user to choose
-> audit only when explicitly requested later
```

The correct sequence is:

```text
generate prototypes
-> static sanity
-> rendered/interaction checks
-> anti-slop review
-> bounded prototype-only repair when needed
-> recheck
-> PROTOTYPE_PRESELECTION_GATE
-> ask user to choose
```

## Hardening

### Mandatory `PROTOTYPE_PRESELECTION_GATE`

Each candidate presented as a valid choice must record:

- locale;
- desktop render;
- representative mobile render;
- compact/tablet when materially different;
- horizontal overflow;
- clipping/gutters/alignment/contrast;
- focus/touch basics;
- dead controls;
- layered controls/open states or N/A;
- anti-slop status + product-specific signature;
- console/runtime evidence when observable;
- safe evidence refs/capability gaps.

Static parseability is not visual/design proof.

### Dead-control firewall

A prototype may be partial but must not lie about interactivity. Live-looking buttons/links/tabs/toggles/selects with placeholder anchors or no representative response are blocking prototype defects. Out-of-scope actions must be rendered as clearly non-interactive explanatory chrome.

### Bounded repair before handoff

When prototype writes and local render actions are already authorized, failed candidates should be repaired inside the isolated prototype scope before the user is asked to choose. At most two bounded repair passes are allowed for the same direction set. Persistent material defects return `DESIGN_PROTOTYPE_BLOCKED` rather than creating an infinite polish loop.

### Uncheckable rendering

When trustworthy rendering is unavailable, the internal gate remains `UNCHECKABLE`; source/static HTML cannot be promoted to visual PASS. A user may manually inspect the prototypes, but the controller must label the internal evidence gap honestly.

## Regression coverage

Added `skills/designing-product-experience/evals/preselection-evals.json` with cases for:

- known-bad prototype set blocked before user choice;
- prototype-only repair before choice;
- uncheckable rendering not fabricated as PASS.

`check_dev_05_behavioral_contracts.py` now requires those cases and the controller/prototype preselection markers.

## Context-cost note

The preselection hardening adds instruction text to the UI design hot path. The deterministic `ui-design-increment` byte budget was deliberately reviewed and raised from 65,000 to 72,000 bytes. This is still a package-load byte guardrail, not runtime-token telemetry. Future growth still requires an explicit budget change/review.

## Next native test

Preserve v2 as failed orchestration evidence. Run a clean v3 project with the same product brief and resolved locale. The expected behavior is that Matreshka repairs/blocks bad prototype candidates internally and only asks the user to choose after `PROTOTYPE_PRESELECTION_GATE=PASS` (or explicitly degraded `UNCHECKABLE` when rendering cannot be performed).
