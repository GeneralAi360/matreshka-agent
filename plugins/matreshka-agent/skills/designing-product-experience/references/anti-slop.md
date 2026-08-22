# Matreshka Anti-Slop Design Law

Use this reference for every material UI direction, prototype, design review, and final visual check. It is a compact runtime law distilled from the project's anti-slop source so Matreshka can enforce the important rules without loading an 86 KB catalog into every task.

## Product-specific point of view

AI slop is generic design produced from familiar defaults rather than from the brief. Before designing, name one product-specific signature: an information model, spatial idea, visual system, bespoke geometry, data treatment, or interaction pattern that belongs to this product.

"Clean", "modern", "premium", "dashboard", "editorial", a palette swap, or a trendy font is not a sufficient signature.

Explicit user visual direction overrides these defaults. Record the exception as a deliberate design decision.

## Product UI language

Conversation language and product-interface language are separate facts.

- Never infer product UI locale only from the chat language.
- In `INTERVIEW` or `ASSISTED`, if meaningful product copy is required and UI locale is not explicit or established by the repository, ask one material language question before comparison prototypes.
- Prototype product copy uses the resolved product UI locale. Test chrome may use the conversation language.
- Check realistic wrapping, dates/numbers, control width, and text expansion when localization can affect layout.

## Suspicious default compositions

Do not reach reflexively for:

- kicker/eyebrow -> giant headline -> subline stacks;
- left-copy/right-panel split hero;
- repeated small-label-over-large-heading sections;
- filled-primary + outlined-secondary button pairs;
- rows of rounded metric/feature cards simply to fill space;
- pills/chips around every nav/status/category;
- generic pricing/testimonial/CTA/footer blocks;
- decorative fake app/macOS windows;
- the same skeleton recolored as multiple directions.

Application UI should use hierarchy, grouping, typography, lists/tables, and direct controls when those are better than another card.

## Suspicious default palette/material choices

Require a product-specific reason before using:

- blue-purple or candy gradients;
- cool blue-charcoal dark SaaS palettes;
- generic cream/beige editorial canvases;
- generic UI-kit gray as the dominant surface;
- one loud saturated accent everywhere;
- radial glows/aurora blobs;
- glass/blur over flat backgrounds;
- all-around fluffy shadows or fake shadow boxes;
- a faint border around every box.

Prefer disciplined palette, tonal elevation, fewer surfaces, and intentional depth.

## Typography

Do not make the product identity depend automatically on familiar AI defaults or on the next trendy free replacement. A neutral body/system font is acceptable when intentionally neutral. Signature type must be chosen from the brief and verified rendered.

Do not use one tiny tracked-uppercase label treatment everywhere or monospace as a costume for ordinary copy.

## Real primitives, art-directed styling

Prefer existing accessible project primitives/components. Do not hand-roll generic buttons, dialogs, menus, selects, popovers, date pickers, comboboxes, tabs, tooltips, drawers, or focus traps when a compatible primitive exists.

A prebuilt component still needs de-slopping: remove generic gradients, glows, pill styling, hover lifts, icon tiles, and default shadows that do not fit the chosen direction.

## Dropdown / select / popover quality gate

Closed state is not enough. Every affected select, dropdown, menu, combobox, date picker, popover, tooltip, context menu, dialog, or sheet must be judged open/expanded.

Verify:

- trigger and open surface share the design language;
- intentional width/min-width and no clipping;
- placement/collision near viewport edges;
- correct portal/z-index layering;
- long-menu scrolling;
- selected/hover/focus/active states;
- appropriate keyboard behavior and Escape;
- focus return where expected;
- touch/mobile usability;
- coherent theme and reduced-motion behavior.

A native platform `<select>` is acceptable only when native appearance is a deliberate product choice. Do not accidentally combine an art-directed custom interface with an unrelated system popup and call the design complete.

Never ship a fake dropdown that looks interactive but does nothing.

## Interaction defaults to reject

Avoid default hover lift/scale on buttons, growing underline animations, looping floating cards, decorative bounce on frequent actions, stray active-nav dots, glowing pills/status dots, and motion whose only purpose is to advertise interactivity.

Motion must explain state, preserve continuity, provide feedback, or express a product-specific moment.

### Content visible by default

Never make content existence depend on an entrance animation completing. Text and controls must remain visible/usable when JS, IntersectionObserver, scroll animation, hydration, screenshot capture, or motion runtime fails.

## Craft blockers

Before presenting prototypes and before final approval verify:

- no clipped text/control near overflow, masks, fixed heights, notches, or overlaps;
- deliberate gutters from viewport/container edges;
- intended centers are actually centered;
- parallel comparison rows/actions align;
- readable contrast everywhere, especially buttons;
- no hard shadow/glow/gradient seams;
- no horizontal overflow at supported compact/mobile widths;
- controls that look interactive actually work;
- open overlays are not cropped/hidden;
- visible focus remains present;
- touch targets remain usable;
- content survives reduced/no motion.

These are craft defects, not taste disagreements.

## Prototype anti-slop pass

Before showing a direction to the user:

1. name its product-specific signature;
2. name the main generic patterns deliberately avoided;
3. confirm sibling directions differ structurally, not only by color/type;
4. inspect key open interactive states;
5. confirm product copy is in the resolved UI locale;
6. remove dead controls and obvious craft defects;
7. redesign any direction that still looks like a reusable AI template.

## Final review

Design Review must re-check the implementation against this law and frozen `DESIGN.md`. Do not "fix" slop by swapping one trendy font/color/component for another. Restore product-specific intent, coherence, accessibility, and craft.

Task-local `DESIGN_CONTEXT_SET` should include only the anti-slop rules relevant to the affected surface.
