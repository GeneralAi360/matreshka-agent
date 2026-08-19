# Complexity Tiers

Use a complexity tier to bound decomposition overhead. It answers **how many independently reviewable change units this product needs**, not how risky the work is and not how much authority exists.

Keep these dimensions independent:

```text
Complexity tier: T0 / T1 / T2 / T3
Execution profile: maximum speed / balanced / maximum quality
Permission envelope: exact allowed actions
```

A small authentication fix can be `T0 + maximum quality`. A large low-risk documentation migration can be `T2 + balanced`. Tier never weakens security or grants permissions.

## Tier guide

| Tier | Product shape | Preferred reviewable tasks |
| --- | --- | ---: |
| `T0` | one coherent result, one primary boundary, safely reviewable in one change unit | 1 direct task; no artificial decomposition |
| `T1` | one feature with a few distinct but tightly related results | 2–3 tasks |
| `T2` | several features/layers or one feature crossing several independent boundaries | 4–8 tasks |
| `T3` | three or more genuinely independent subsystems/data or security boundaries | 9–16 tasks |
| above `T3` | cannot fit the safe single-run budget | `SPLIT_REQUIRED` / `DECISION_MAP_REQUIRED` |

These are budgets, not quotas. Never invent tasks to hit a number and never merge independent security/data outcomes merely to stay under a number.

## Determine tier from the product, not document length

Specification depth, number of paragraphs, number of files, and user verbosity do not determine complexity tier.

Use:

- independently observable outcomes;
- subsystem/data/security boundaries;
- migration/rollback boundaries;
- external provider boundaries;
- public contracts that need independent review;
- dependency graph and safe rollback units.

A detailed specification for one page may still be T0. A short sentence that requires auth, migration, provider activation, and persistence may be T2 or require split.

## Boundary-cost test

A new task is justified only when it buys independent review, rollback, evidence, ownership, or safe context isolation.

Before keeping a task, ask:

1. Does it produce an observable/reviewable result on its own?
2. Does it own a distinct subsystem, public contract, data/security boundary, migration, or rollback point?
3. Would merging it with a neighbor make review/evidence less trustworthy?
4. Is its expected work larger than the cold-start/context cost it creates?

If the answer is no and it shares the same files/seam as a neighbor, merge it into that task.

## Mandatory merge pass

After drafting tasks, merge avoidable fragmentation:

- adjacent tasks that touch the same boundary and cannot be reviewed independently;
- tiny setup tasks whose only consumer is the immediately following task;
- tasks with no direct `U-`, functional, `S-`, or named enabling-step justification;
- chains where an intermediate task demonstrates nothing and has no independent rollback/security boundary.

Then re-evaluate the tier. Do not keep a higher task count merely because it was the first draft.

## T0 behavior

T0 means **one direct task**, not “skip engineering discipline.”

The controller may avoid a multi-task map, but still requires as applicable:

- exact task brief/allowlist;
- focused RED/GREEN evidence;
- selected `U-`/`S-` mappings;
- independent review according to execution profile/risk;
- technical/security verification;
- G4 blind acceptance for traced Build End-to-End work;
- authorized finish/handoff.

Do not turn T0 into permission for controller self-review on high-risk work.

## Parallelism

Complexity tiers describe decomposition only. They do not authorize parallel writers.

Matreshka keeps one writer per checkout. Independent read-only roles may run in parallel when their packages are disjoint. Any future parallel writer execution requires separately authorized isolated workspaces plus explicit overlap/integration evidence; tier or dependency-wave language alone never grants it.

## Stop rules

Return `SPLIT_REQUIRED` when the trustworthy plan requires more than 16 reviewable tasks in one run, unless repository constraints prove a larger single-run plan is safer and the controller explicitly rescopes the budget. Do not hide a >16 plan by creating oversized multi-boundary tasks.

Record the selected tier, task count, reason, and any deliberate deviation in the plan and controller ledger.