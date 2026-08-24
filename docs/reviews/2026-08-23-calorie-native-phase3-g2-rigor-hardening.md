# Phase 3 — native v3 G2 rigor hardening

Status: `VERIFIED_LOCAL_DEVELOPMENT_CHECKS`

## Audit finding

Native v3 run `20260823T132152Z` delivered the product successfully:

- 13/13 U requirements verified;
- technical and security verification passed;
- Browser E2E and real-process restart persistence passed;
- implemented-direction Visual Design Check passed;
- fresh independent G4 v2 passed;
- Design Drift and Documentation Drift gates resolved.

The run truthfully retained `G2=CLEAN_DEGRADED_INLINE`. The host did not provide
the fresh pre-PLAN G2 checker guarantee, so later G4, implementation, Browser
E2E, design/docs reconciliation, and finish evidence cannot rewrite that
historical gate identity.

This is a process-rigor finding, not a delivered-product failure. The intended
terminal semantics are now explicit:

```text
DELIVERY_STATUS=COMPLETE
RUN_RIGOR=DEGRADED
RIGOR_DEGRADATIONS=G2_INDEPENDENCE
G2_EVIDENCE_CLASS=CLEAN_DEGRADED_INLINE
```

`RUN_RIGOR=FULL` requires every applicable independence/capability guarantee for
the selected mode, execution profile, and host contract. Delivery completion
does not imply full process rigor.

## Preserved history

- Historical prototype `UNCHECKABLE` evidence was not rewritten.
- The later production Visual Design Check `PASS` remains separate evidence.
- The first G4 `PARTIAL` remains historical evidence.
- The second fresh G4 `PASS` is current acceptance evidence, not a rewrite of the first result or of G2.
- This note does not claim a Matreshka 0.5 release.

## Contract changes

- G2 now records an explicit evidence class: `CLEAN_FRESH_NATIVE`, `CLEAN_FRESH_EXTERNAL`, `CLEAN_DEGRADED_INLINE`, `GAP`, or `BLOCKED`.
- Ledger, finish handoff, progress, and dashboard state carry delivery status, run rigor, explicit degradation reasons, and G2 class.
- Dashboard/progress remain projections and cannot promote a degraded class.
- A targeted executable regression covers both completed delivery with degraded rigor and a material G2 gap blocking PLAN.

## Verification

The deterministic development suite passed 9/9 checks, and the targeted G2 rigor
eval passed 2/2 cases. No commit, push, PR, merge, or release action is part of
this phase.
