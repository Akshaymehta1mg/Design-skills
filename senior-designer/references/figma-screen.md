---
name: figma-screen
description: Create or revise a high-fidelity screen — a real, buildable UI that uses the product's existing design system and looks like actual shipping product.
---

# Figma Screen

## What this step is for

This is where the design gets real. You're creating (or revising) a screen that looks like the actual product — using real components, real content, and the existing visual system. This isn't a wireframe or a sketch. It's what the thing should actually look like.

## How to think through it

### Step A: Component mapping (do this BEFORE writing any HTML)

This step produces a visible output — a table the designer can review. Don't skip it, don't do it mentally, don't merge it into the HTML generation. Output it as text first.

If a design system MCP is connected (Dopamine 2, Storybook, etc.):

1. List every UI element the screen needs (buttons, inputs, tabs, cards, bottom sheets, headers, etc.).
2. For each element, **query the MCP**: search for that component type, read its docs, check its variants and states.
3. Also query patterns — these show how the product composes pages (section order, layout, spacing).
4. Output a **Component Mapping Table** before writing any code:

```
| UI element | Design system component | Variant or state | Notes |
| --- | --- | --- | --- |
| ... | ... | ... | ... |
```

If no design system MCP is connected, use standard mobile patterns and name them clearly.

The table is the contract. Every element in the HTML must trace back to a row in this table. If a row says "Design System Component: —", that's an explicit decision to create something new — not a silent omission.

### Step B: Content plan (do this BEFORE writing any HTML)

For each screen or surface, write out the actual content — not structure labels, but real words:

- **What the user sees** — the specific information shown on this screen
- **What the copy says** — headline, body text, button labels, helper text, error messages
- **What the user decides** — the action they take and what happens next
- **What's deliberately hidden** — information withheld for privacy, simplicity, or progressive disclosure

This is where the UX thinking happens. The component mapping tells you *what to build with*. The content plan tells you *what to say*. Both must be visible outputs before you write HTML.

### Step C: Build the screen

1. Define the screen's purpose and its primary action.
2. Build the screen using the components from your mapping table and the content from your content plan. The CSS for each component should match the design system's tokens (colors, spacing, radius, font sizes) — not your own values.
3. Only create a custom element when the mapping table explicitly flagged it as "New component needed." If you find yourself writing CSS for a component that has a match in the table, stop and use the design system version instead.
4. If an existing component is close but not perfect, use it and document the missing capability rather than silently replacing it.
5. Include required states if they're relevant to the task.
6. Add concise labels or annotations only if the board needs them for clarity.

## Visual quality standards

A senior designer's screen looks like a real product, not a prototype someone rushed through. These are non-negotiable.

**Canvas and sizing:**
- Mobile screens: **360×800px** viewport. Standard Android. No exceptions unless designing for a specific device (iPhone 15: 393×852, iPad: 820×1180).
- Use proper mobile proportions. If elements look oversized or the screen feels like a blown-up desktop view, resize everything.
- Primary action buttons: 44–48px height, full-width or appropriately sized for thumb reach. Not 64px. Not 72px.

**Typography:**
- Follow the product's existing type scale. If one is provided (via Storybook or design system), match it exactly.
- If no type scale is provided, use a sensible mobile scale:
  - Page title: 20–22px, semibold/bold
  - Section heading: 16–18px, medium/semibold
  - Body text: 14–16px, regular
  - Caption / helper text: 11–12px, regular
  - Button labels: 14–16px, medium/semibold
- Establish clear visual hierarchy through size, weight, and color — not just size alone.
- Don't make headings and body text the same size. If they look similar, the hierarchy is broken.

**Icons:**
- **Never use emojis.** Not as icons, not as illustrations, not as decorative elements. Never. Emojis are not design.
- For small UI icons, use the **Hugeicons** library and reference icons by their library name.
- For illustrations and large decorative icons, use **thiings.co** and reference assets by their library name.
- When rendering via `show_widget`, use simple SVG paths for icons or reference them by label. Don't substitute Unicode symbols or emojis.

**Components and design system (this is the most important section):**
- If a design system MCP is connected — **you must query it and use its components.** This is not optional. A senior designer builds with the system, not around it.
- Before writing any artifact code, run through this checklist:
  1. Did I list the available components?
  2. Did I search for each component type I need (tabs, buttons, cards, inputs, etc.)?
  3. Did I read the docs for each component I'm using?
  4. Did I check available page patterns to understand how this product composes screens?
  5. Am I using the system's exact component names, variants, tokens, and spacing?
- Use available system components instead of rebuilding standard components with custom styling.
- If the system specifies spacing tokens, color tokens, or corner radius values — use them. Don't override with your own values.
- If an existing component is close but not perfect, use it, document the missing capability, and do not silently create a custom replacement.
- Only create a genuinely new component when nothing in the system fits. When you do, document it in the spec as "New component — not in the current system" so the team knows it needs to be added.
- If no design system is provided, use clean standard mobile patterns and document what you used so it can be translated into the actual system later.

**Spacing and layout:**
- Use an 8px grid. All spacing should be a multiple of 8 (8, 16, 24, 32, 40).
- Horizontal padding: 16–20px on mobile. Not edge-to-edge, not 32px margins.
- Vertical rhythm: consistent spacing between content blocks. Group related items tightly (8–12px), separate groups with more space (24–32px).
- Cards should have 12–16px internal padding. Not 24px — that wastes mobile real estate.

**Content:**
- Use realistic, context-appropriate content rather than placeholder text.
- Copy should sound like the product's voice. Read the existing UI before writing new copy.
- If the screen has a primary action, its label should describe the intended action or outcome.

## What the output looks like

```markdown
# Screen Specification

## Screen Purpose
...

## Viewport
360×800px (Android mobile)

## Design System Reference
[Storybook URL or component library name, if provided]

## Layout
- Status bar: ...
- Header / nav bar: ...
- Main content area: ...
- Bottom action / tab bar: ...

## Component Mapping
- [element] → [exact design system component and variant]
- ...

## Icon Usage
- [element] → [Hugeicons / icon-name] or [thiings / icon-name]
- ...

## Typography
- Page title: [size/weight from type scale]
- Section heading: [size/weight]
- Body: [size/weight]
- Caption: [size/weight]

## Content
- Headline: "..."
- Body: "..."
- CTA: "..."
- ...

## States
- Default:
- Loading:
- Empty:
- Error:
- Success:

## Interaction Notes
- ...
```

## How to deliver the artifact

**Always save as an HTML file and publish with the Artifact tool.** Never render the final design artifact inline in chat via `show_widget`. Inline diagrams are for reasoning — the artifact itself must be a standalone file the designer can share with their team.

Use `show_widget` only for quick thinking sketches during Steps 1–5 (flows, comparisons, problem diagrams). The actual design output in Step 6 is always a published HTML artifact.

**Multi-screen flows get tabs.** If the design has multiple screens or states (which it almost always does), the artifact must include a tab bar or screen switcher so the viewer can navigate between them. Don't stack screens vertically in one long scroll — tabs let reviewers focus on one screen at a time and compare.

**Phone frame at 360×800.** The artifact renders inside a phone-shaped frame at exactly 360×800px, centered on the page. The tab switcher sits outside the phone frame (above or below), not inside it.

**Pages vs. bottom sheets.** Not every screen is a tab. Classify each surface from the solution step:

- **Pages** represent a new destination or distinct task and receive their own view in the artifact.
- **Bottom sheets** represent contextual actions within a page and render as overlays on the parent view while keeping that context visible.

The test: if the user triggered this action from a specific page and will return to that same page when done, it's a bottom sheet — not a new tab.

**How to build bottom sheets in the HTML artifact:**
- The bottom sheet slides up from the bottom of the phone frame, covering 40–70% of the viewport height depending on content.
- It has a drag handle (small horizontal bar, 40×4px, centered, rounded) at the top and an optional close/X button.
- The parent page is visible behind it with a semi-transparent dark overlay (rgba(0,0,0,0.4)).
- The trigger button on the parent page opens the sheet; tapping the overlay or the close button dismisses it.
- Treat a page and its bottom-sheet overlay as two states of the same view rather than separate destinations.

**Edge cases and error states always included.** If the solution has error states, empty states, or recovery flows — add them as separate tabs. Every error or edge-case screen gets a visible retry/refresh button and clear recovery copy. Don't hide edge cases — they're the screens that ship broken when nobody designs them.

**Interactivity.** Buttons and actions in the artifact should advance to the intended state. Back behavior should work. Wire material branches and overlay triggers so the artifact communicates behavior rather than appearing as a slideshow.

## Visual quality when building HTML

- Phone frame: **360×800px**, centered on the page with a subtle device border.
- Use realistic mobile text sizes. 14px body, 20px title — not 24px body and 36px title.
- No emojis anywhere. Use simple SVG paths or labeled rectangles for icon placeholders.
- Show real, specific content — not placeholder text.
- Use a proper color palette. If the product's brand colors are known, use them. Otherwise use a clean neutral palette.
- Match the spacing to an 8px grid. Elements shouldn't float in random positions.
- All interactive elements (buttons, links, tabs) must have click handlers wired from the start. Don't ship a static artifact that needs "fixing" later.

## Post-artifact self-check

After writing the HTML, scan your own code before publishing. For every CSS class or styled element, ask: does this match a row in my Component Mapping Table?

- If you wrote custom CSS for a button, input, tab, card, bottom sheet, or any standard UI element — and the mapping table has a design system match for it — you broke the contract. Replace your custom CSS with the design system's tokens (colors, sizes, radius, spacing).
- If you used colors, font sizes, or spacing values that aren't from the design system's tokens — and the MCP provided those tokens — replace them.
- If you styled a component state (hover, active, error, success) differently from how the design system defines it — match the system.

This check exists because it's tempting to freestyle CSS when you know how to make things look good. But the point of a design system is that components look consistent across the product — not that each screen invents its own version.

## Ground rules

- If you're writing directly into Figma, follow the Figma tool workflow for file context.
- If you're describing the screen, provide a spec specific enough that another designer could build it in Figma without asking questions.
- If a Storybook or design system was provided and you didn't use its components, that's a failure. Go back and match them.
- Skip purely decorative changes unless they improve comprehension, trust, or task completion.
- The screen should look like it belongs in the existing product — not like a redesign from a different company.
