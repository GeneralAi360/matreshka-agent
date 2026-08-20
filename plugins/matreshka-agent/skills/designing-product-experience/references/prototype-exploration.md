# Design Prototype Exploration

Use this reference only when a material UX/UI direction is unresolved and seeing alternatives is more reliable than asking the user to describe taste abstractly.

The goal is divergence followed by an explicit selection, not permanent prototype infrastructure.

## When to prototype

Use prototype exploration when one or more are true:

- a new UI-bearing product has no established visual/interaction direction;
- the user explicitly says they do not know what style/layout they want;
- a major redesign has multiple credible interaction/hierarchy models;
- one decision will propagate across many screens/components and is expensive to discover late.

Do not prototype when:

- `DESIGN.md` already covers the pattern and no material design decision changed;
- the task is a small implementation inside an established component/system;
- the question is backend/data-only;
- prototype infrastructure would cost more than the design uncertainty warrants.

## Direction count

Default to **3** directions. Allow 2 for a narrow binary decision or up to 5 only when the design space is genuinely broad.

Every direction must have:

```text
name
axis
what changes
what remains invariant
when this direction wins
its main cost/tradeoff
```

Names describe the design direction: `Calm`, `Dense`, `Editorial`, `Direct`, `Playful`, `Focused`, etc. Never use `Option A/B/C` as the only distinction.

## Real divergence

Valid axes include:

- navigation/layout model;
- information density;
- hierarchy/type scale;
- surface/depth strategy;
- interaction/disclosure model;
- motion personality;
- touch/desktop workflow emphasis.

Invalid fake divergence:

- same layout with three accent colors;
- same card with 8px/10px/12px radius;
- copy changes with no structural/interaction difference;
- variants whose only distinction is an arbitrary font swap.

If two variants converge, merge/drop one rather than padding the set.

## Recon before variants

Use current project evidence:

- stack/styling method;
- existing tokens;
- shared components;
- app shell/context;
- product personality;
- target screen sizes/input modes;
- accessibility and motion constraints.

Existing confirmed design rules remain invariants unless the exploration explicitly challenges them through valid design authority.

## Prototype isolation

Prototype writes are not production feature implementation.

Preferred order:

1. **run-local static prototype** under an authorized Matreshka run-state/design path when sufficient for the decision;
2. **isolated project prototype route/surface** only when fidelity requires real project components and exact temporary write scope is authorized;
3. **inline design specification** when no safe prototype write/browser capability exists.

A useful default internal path when state writes are authorized:

```text
.matreshka/runs/<run-id>/design/prototypes/
```

Do not commit it by default.

A project route such as `/prototypes/<slug>` must be clearly isolated from production navigation/data and removed after selection unless the user explicitly asks to keep it.

Never infer permission for:

- dependency installation;
- network/browser download;
- local server/process start;
- port binding;
- browser launch;
- secrets/test credentials;
- Git actions.

## Prototype fidelity

Each direction should be complete enough to judge the decision:

- realistic surrounding context;
- realistic product-shaped content without private data;
- working primary interaction when that interaction differentiates the direction;
- representative loading/empty/error only when those states matter to the decision;
- proper reduced-motion/accessibility basics when motion is part of the comparison.

Do not build an entire product to choose a navigation/card direction.

## Picker behavior

When a browser-rendered comparison is possible, use a small neutral picker that is clearly test chrome, not product UI.

Requirements:

- one variant displayed at full realistic scale at a time;
- buttons/number keys `1..N` and left/right arrows switch instantly;
- a visible direction name and optional one-line axis description;
- picker does not inherit brand styling that could bias the comparison;
- picker never covers the design area being judged; move it top/bottom only as needed;
- replay control only when motion comparison requires it;
- switching variants itself is instant because it is a very high-frequency test action;
- the selected variant may persist locally in URL/query/state for reload convenience when safe.

Do not compare postage-stamp screenshots side by side when scale, spacing or interaction matters.

## Verification before user choice

Before presenting:

- every direction renders;
- differentiating interactions work;
- no obvious console/runtime error in the prototype path when observable;
- direction axes are still genuinely distinct;
- none violates confirmed security/source-intent/accessibility constraints merely to look different.

When browser evidence is available, capture at most one representative screenshot per direction unless more is required to explain a responsive/interaction difference.

## Handoff to user

Present one compact table:

| Direction | Axis | Best when | Main cost |
| --- | --- | --- | --- |
| Calm | restrained hierarchy, more whitespace | trust/readability matter | lower information density |
| Dense | compact data-first layout | expert daily workflow | visually busier |
| Editorial | stronger type/hierarchy | product needs character | consumes more vertical space |

Do not silently select a winner in `INTERVIEW`/`ASSISTED` when the user is explicitly comparing directions. If asked for a recommendation, give one grounded in product personality/frequency, but keep the choice explicit.

In `FULL_AUTO`, the controller may choose a restrained direction only when the decision is reversible and not a missing brand/business truth. Record the selected direction and rationale.

## Promotion

After a direction is selected:

1. record selected direction/prototype identity;
2. translate the winning rules into root `DESIGN.md`;
3. compute/record design identity;
4. remove/retire unselected prototype surfaces when cleanup is authorized;
5. route production implementation through the normal plan/task/RED-GREEN/review/verify workflow;
6. do not copy prototype shortcuts that violate production architecture/accessibility/security.

Prototype success is design evidence, not production verification.
