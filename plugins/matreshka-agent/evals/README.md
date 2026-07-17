# Evaluation suites

This directory contains two complementary, machine-readable suites.

- `package-validation.json` lists deterministic structural and security gates enforced by `scripts/validate_package.py`.
- `workflow-evals.json` defines end-to-end, recovery, adversarial, and platform-compatibility cases.

Each skill also contains `evals/evals.json` with task cases and `expectations`, plus a separate `evals/trigger-evals.json` array for positive and negative trigger queries. The separation follows the executable format used by the current skill-creation tooling; the package validator rejects mixed trigger data inside task eval files.

## Baseline comparison

Run every workflow case in three fresh contexts:

1. `plain-agent`: the host coding agent receives only the task and permission envelope.
2. `minimal-controller`: the agent receives the permission gate, one plan, and final verification, without the full workflow skills.
3. `full-candidate`: the installed Matreshka Agent package is available.

Pin the repository snapshot, task prompt, permissions, available tools, model capability tier, and time limit. Do not reuse conversation history between variants. A reviewer who does not know which variant produced a result should grade acceptance, regressions, permission breaches, evidence quality, and unnecessary work.

Record agent turns, wall time, and token usage when the host exposes them. Missing telemetry is recorded as unavailable; the package does not add telemetry or send results anywhere.

Package validation is necessary but does not prove workflow quality. A public release requires successful local installation and representative workflow runs on every claimed platform.
