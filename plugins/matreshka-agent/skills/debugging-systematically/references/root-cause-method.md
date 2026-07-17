# Root-cause method

## Build a symptom statement

Write one observable statement before investigating:

```text
Given <state/input>, when <action>, the system produces <actual result> instead of <expected result>, observed at <boundary> on <current state>.
```

Include only confirmed facts. Keep reports, assumptions, and suspected causes separate.

## Narrow the boundary

Trace from the symptom inward:

1. Confirm the outer contract and its actual output.
2. Inspect the immediate producer of the incorrect value or decision.
3. Compare inputs and outputs at the nearest boundary.
4. Repeat until the input is correct but the output first becomes incorrect.
5. Inspect the condition that controls that transformation.

For distributed or asynchronous flows, follow a stable correlation identifier, timestamp window, message key, or transaction boundary. Do not combine unrelated events merely because they are close in time.

## Distinguish cause layers

Use separate labels:

- **Trigger:** the input or event that exposes the problem.
- **Defect:** the incorrect code, contract, state, data, or configuration.
- **Propagation:** the path that carries the incorrect state.
- **Symptom:** the user-visible or test-visible failure.
- **Amplifier:** retries, caching, concurrency, or observability gaps that increase impact without creating the defect.

Fixing only the trigger or symptom may leave the defect intact.

## Design discriminating experiments

Prefer experiments that produce different outcomes for competing hypotheses:

- compare current state with a known baseline;
- reduce the input to a minimal reproducer;
- replace one boundary with a deterministic fake already used by the project;
- inspect before-and-after values at a single boundary;
- hold all variables constant except one configuration or code path;
- repeat with a fixed seed, clock, scheduler, or network condition.

Do not edit production logic or tests as a diagnostic experiment. Use existing read-only observations, an already available deterministic fake, or a disposable run-owned diagnostic artifact outside product scope. If a code or test mutation is needed to prove the counterfactual, describe it as a bounded handoff to `implementing-with-tests`.

## Handle flaky behavior

Bound repetition before starting. Record the number of runs, failures, seed, timing, concurrency, and environment. Compare distributions or ordering rather than treating one passing retry as resolution.

Investigate common classes without assuming them:

- shared mutable state or order dependence;
- uncontrolled time or randomness;
- incomplete async cleanup;
- race conditions and missing synchronization;
- external service variability;
- resource exhaustion;
- test isolation or fixture leakage.

Stop when the repetition budget is exhausted. Report frequency and confidence; do not invent certainty.

## Attribute pre-existing failures

When safe and practical, run the same focused reproduction on the recorded baseline or an equivalent clean state. Do not overwrite the current worktree to do so. Use a safe existing checkout, immutable artifact, or controller-provided baseline.

If baseline reproduction is unavailable, state that attribution is unresolved. A historical failure log can support but does not by itself prove current ownership.

## Require causal proof

Strong root-cause evidence usually combines:

1. a stable reproduction;
2. the first incorrect boundary;
3. a code/configuration/data condition explaining it;
4. a focused counterfactual or regression test;
5. rejection of close alternatives.

Use confidence labels such as `PROVED`, `HIGH_CONFIDENCE`, or `LEADING_HYPOTHESIS`. Reserve `PROVED` for a complete causal chain.
