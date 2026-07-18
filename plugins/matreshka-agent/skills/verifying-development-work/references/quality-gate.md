# Evidence-based quality gate

Use a quality gate to make verification repeatable without turning it into automatic enforcement. It is a selected matrix of existing, permitted repository checks, not a new build system or a hook.

## Select the gate

Start from current repository instructions, project profile, package scripts, CI configuration, task brief, and affected boundary. A profile may suggest a command but does not prove that it still exists or is permitted.

Use [the quality-gate template](../assets/quality-gate-template.md) to record the selected rows. Each row must name one claim, one command or inspection, source, expected signal, required evidence, risk, and whether it is required for the current task.

Never add a command simply because it is common. Do not install dependencies, enable network access, read secrets, call a remote service, mutate files, or run a broad suite unless the envelope and current gate explicitly permit it.

## Run and interpret

1. Confirm the exact current state and that each selected command still exists.
2. Run a required command once at its intended tier. Re-run only when the first result is flaky, incomplete, or invalidated by a state change.
3. Record `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED` for every row with command, exit code, counts, state identity, and a decisive note.
4. Inspect state after mutation-prone checks. Unexpected generated changes invalidate affected evidence until adjudicated.
5. Do not repair failures in the verifier role and do not convert an unavailable check into a pass.

The final verification status remains `VERIFIED`, `PARTIALLY_VERIFIED`, `FAILED`, `BLOCKED`, or `HANDOFF_REQUIRED`. The quality-gate rows explain why.

## Handoff and evolution

The controller may carry an approved gate from task to task only while its profile-input identity, project root, permissions, and command sources remain current. Record any skipped row and why. A task result can create a learning candidate only through the controller's opt-in directed-learning process; the verifier never promotes lessons.
