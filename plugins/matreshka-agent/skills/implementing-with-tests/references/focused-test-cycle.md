# Focused test cycle

## Choose a stable test seam

Test the smallest externally observable behavior that proves the acceptance criterion:

1. Prefer an existing public function, endpoint contract, command, component behavior, or persistence boundary.
2. Reuse the repository's established test framework, naming, fixtures, and helpers.
3. Avoid asserting private call order or internal structure unless that structure is itself the contract.
4. Keep the test deterministic. Control time, randomness, networking, and environment state with existing project patterns.
5. Cover one behavioral delta per focused cycle. Split independent deltas.

## Classify RED correctly

A valid RED must satisfy all of these conditions:

- the focused command starts successfully;
- the new or adjusted assertion is exercised;
- the failure explains the missing or incorrect behavior;
- unrelated baseline failures do not hide the signal;
- the test would pass if the intended behavior existed.

Classify other outcomes explicitly:

| Outcome | Response |
| --- | --- |
| Test already passes | Strengthen the observable assertion or report that no implementation delta is proved |
| Test does not execute | Fix allowlisted test setup or return `BLOCKED` |
| Unrelated test fails first | Narrow the command or establish the pre-existing baseline |
| Failure cause is ambiguous | Pause implementation and diagnose the cause |
| Reproduction requires a forbidden remote action | Prepare a local substitute or return `HANDOFF_REQUIRED` |

## Keep GREEN minimal

Implement the smallest coherent behavior, not merely the smallest line count. Include required validation and error handling when they are part of the acceptance contract. Avoid opportunistic refactors, broad formatting, dependency upgrades, and adjacent cleanup.

If the focused test exposes a second independent defect, preserve the first coherent change unit and record the second defect for future work.

## Permit exceptions narrowly

Allow a test-first exception only when no meaningful executable test can be written with the available environment and permissions. Examples may include prose-only documentation, a platform-generated lockfile, unavailable device hardware, or a remote-only behavior outside the local operator boundary.

Before changing the artifact:

1. State why an executable RED is impossible or misleading.
2. Identify the nearest alternate check, such as a parser, schema validator, static inspection, render preview, or prepared remote verification command.
3. Record who must perform any missing verification.
4. Set the final status to `PARTIALLY_VERIFIED` or `HANDOFF_REQUIRED` when acceptance still depends on that check.

## Record compact evidence

For each command, record:

```text
COMMAND: <exact command with secrets omitted>
EXIT_CODE: <integer or unavailable>
COUNTS: <passed / failed / skipped, when available>
NOTE: <one decisive observation>
STATE: <baseline or current revision/hash>
```

Keep raw logs outside the main report. Reference their safe location only when needed, and never copy credentials or sensitive payloads.
