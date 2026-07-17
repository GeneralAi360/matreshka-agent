---
name: designing-software-work
description: >-
  Explore and design a software change before implementation. Use for a raw product idea, new feature, ambiguous requirements, multiple architectural options, risky behavior change, or a request to brainstorm and produce a software design without writing production code.
---

# Design Software Work

Turn an idea into a confirmed, testable design. Do not implement the design or produce an implementation task sequence.

Read [design-quality.md](references/design-quality.md) for risk-specific checks, question policy, and self-review. Copy [design-document-template.md](assets/design-document-template.md) only when producing a saved design artifact.

## Establish the design boundary

1. Restate the desired user or system outcome in plain language.
2. Inspect applicable repository instructions, current architecture, public interfaces, data models, tests, and nearby patterns in read-only mode.
3. Separate confirmed facts, inspected evidence, assumptions, decisions, constraints, and non-goals.
4. Identify actors, trust boundaries, external systems, compatibility needs, and irreversible effects.
5. Return `SPLIT_REQUIRED` when the request contains several independent outcomes or unrelated security and experience boundaries.

Do not ask the user for paths, commands, or conventions that safe repository inspection can answer. Do not change files while investigating unless permission explicitly includes creating the design document.

## Clarify one decision at a time

Ask only a question whose answer materially changes the architecture, acceptance result, security boundary, or irreversible choice. Ask one question per turn. Provide two or three concrete answer choices and recommend one when useful.

Explain consequences in non-technical language when the user is not a programmer. Avoid a questionnaire dump.

If the user delegated design decisions inside a valid permission envelope, choose the recommended option, record the assumption and rationale, and continue without asking again. Never delegate away a production, destructive, legal, cost, or secret decision that lies outside that envelope.

## Compare approaches before selecting one

Propose two or three viable approaches. For each, compare:

- fit with the existing codebase;
- correctness and security implications;
- implementation and migration complexity;
- operational and rollback characteristics;
- testing burden;
- future flexibility and lock-in.

Recommend one approach and explain why it best fits the confirmed constraints. Do not present superficial variations as different architectures.

## Build the design progressively

Describe the design at a depth proportional to risk. Cover the applicable areas:

1. Goals, non-goals, and measurable acceptance outcomes.
2. Components, responsibilities, and ownership boundaries.
3. Public interfaces, inputs, outputs, and compatibility.
4. Data flow, state transitions, persistence, and idempotency.
5. Validation, failure handling, retries, timeouts, and degraded behavior.
6. Authentication, authorization, isolation, secret handling, and data exposure.
7. Observability, support, and operational behavior.
8. Migration, rollout, rollback, and cleanup.
9. Testing strategy and evidence needed to prove the design.

Mark irrelevant sections `N/A` with a reason. For a small local change, keep the document to several focused paragraphs. For high-risk work, include an explicit threat/risk analysis and rollback boundary.

## Pass the confirmation gate

In managed mode, present the recommendation and design for user confirmation before planning or implementation. Approval of the design does not grant write access to product code.

In an autonomous mode, proceed only when the permission envelope explicitly delegates the design decision for this scope. Save the chosen approach, assumptions, and rationale in the controller ledger or design artifact.

If the user requests design only, stop after the confirmed design and do not call implementation skills.

## Self-review before handoff

Check the complete design against the inspected source of truth. Remove placeholders and resolve or flag:

- contradictory requirements;
- undefined ownership or interfaces;
- unhandled failure states;
- hidden remote actions or secret needs;
- migration without rollback;
- acceptance criteria with no verification path;
- scope that cannot remain independently reviewable;
- assumptions stated as facts.

Return one of:

- `DESIGN_CONFIRMED` with the design path or complete inline design;
- `NEEDS_CONTEXT` with one exact blocking question;
- `SPLIT_REQUIRED` with proposed design boundaries;
- `BLOCKED` with the conflicting decision or missing authority.

Hand the confirmed design to `planning-software-work` only when implementation planning is requested or delegated.
