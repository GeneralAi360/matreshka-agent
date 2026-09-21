# Context Optimizer Bridge

Use this contract only when a source-qualified external **Matreshka Context Optimizer** result is available or when context pressure (`CONTEXT_TOO_BROAD`, repeated reads, oversized tool output) justifies running that separate skill.

Canonical external source: `GeneralAi360/Matreshk-context-optimizer` (repository may later be renamed to `Matreshka-context-optimizer`). Matreshka Agent consumes only the compact bridge object; it does **not** vendor or silently install the optimizer, CodeBurn, Caveman, or Graphify.

## Projection only

`contextOptimizer` is observability/advisory state. It cannot grant write/network/dependency/Git/browser authority, cannot change a task context guarantee, cannot mark verification PASS, and cannot authorize an optimizer `CHG-xxx`. Dashboard/ledger display remains projection only.

## Compact state

~~~text
contextOptimizer.status                 READY | DEGRADED | UNAVAILABLE
contextOptimizer.health                 OK | WARNING | CRITICAL | UNKNOWN
contextOptimizer.healthBasis            MEASURED | PARTIAL | STATIC_ONLY | UNKNOWN
contextOptimizer.runtimeMeasurement.status
contextOptimizer.runtimeMeasurement.value
contextOptimizer.runtimeMeasurement.unit       tokens | unknown
contextOptimizer.runtimeMeasurement.type
contextOptimizer.runtimeMeasurement.source
contextOptimizer.runtimeMeasurement.semantics CURRENT_CONTEXT | OBSERVED_SUBSET | UNKNOWN
contextOptimizer.staticContext.value           exact bytes
contextOptimizer.staticContext.unit            bytes
contextOptimizer.staticContext.fileCount
contextOptimizer.staticRisk
contextOptimizer.topFindings[]
contextOptimizer.recommendations[]
contextOptimizer.graphify.state
contextOptimizer.ledger.pendingVerification
contextOptimizer.ledger.rollbackRecommended
contextOptimizer.approvalRequired
~~~

## Non-negotiable measurement rules

1. Runtime tokens remain host/provider telemetry. `CURRENT_CONTEXT` may be displayed only when source semantics prove current context.
2. Static instruction/package bytes are exact engineering measurements, **not token counts**.
3. Estimated savings, Graphify size thresholds, or CodeBurn finding `tokensSaved` never become runtime token usage.
4. `UNKNOWN` remains `UNKNOWN`; Matreshka must not infer a number from characters, bytes, time, turns, model family, or context-window size.
5. Existing Matreshka `usage` counters remain authoritative for run token reporting. `contextOptimizer.runtimeMeasurement` is a separate context diagnostic and must not be added to `usage.totalTokens`.

## Controller behavior

- Record source identity/version/path when bridge data is ingested.
- Keep only compact top findings/recommendations in run-state; raw optimizer reports stay outside the always-on controller context.
- If `ledger.pendingVerification > 0`, surface it as optimizer work awaiting re-measure/quality verification; do not call it verified.
- `rollbackRecommended > 0` is a recommendation, not permission to execute rollback.
- `approvalRequired=true` means a proposed optimizer mutation still needs the same explicit authority/approval contract as any other mutation.
- Graphify `RECOMMENDED`/`STALE` never authorizes dependency install/build/update.
- On resume, stale bridge state is advisory until refreshed against current project/optimizer state.

## When to consult

Consult the external optimizer when evidence indicates context waste and doing so is proportionate: `CONTEXT_TOO_BROAD`, recurring broad file reads, tool-result dominance, repeated compaction, many global skills/MCPs, or a large unfamiliar repository. Do not invoke it mechanically on every task.
