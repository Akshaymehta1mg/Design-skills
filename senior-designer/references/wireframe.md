---
name: wireframe
description: Create a low-to-mid-fidelity screen or flow structure — the bones of the design before any visual polish.
---

# Wireframe

## What this step is for

This is where you work out the structure of a screen before anyone worries about colors, typography, or visual polish. What goes where, what's the primary action, what hierarchy makes sense. Get the bones right first.

## How to think through it

1. What's this screen for? What's the one thing it needs to accomplish?
2. What's the primary action the user should take?
3. What are the secondary actions?
4. What's the right information hierarchy — what should they see first, second, third?
5. Place the required content in an order that supports the hierarchy.
6. Think through the states — what does this look like when it's loading, empty, broken, or successful?
7. How does the layout adapt across breakpoints?

## Visual quality standards

These are non-negotiable. A wireframe from a senior designer looks like a senior designer made it — not like a developer threw boxes on a page.

**Canvas and sizing:**
- Mobile screens: **360×800px** viewport. This is the standard Android frame. Design within it.
- Use real mobile proportions. If the screen looks like a desktop browser window resized, it's wrong.
- Buttons, inputs, and touch targets should be sized for thumbs — 44–48px height for primary actions, not 64px or bigger.

**Typography hierarchy:**
- Establish a clear type scale. Headings, subheadings, body, captions — each should be a visibly different size and weight.
- Don't make everything the same size. If the title and the body text look similar, the hierarchy is broken.
- Keep text sizes realistic for mobile: 14–16px body, 18–22px headings, 11–12px captions.

**Icons and imagery:**
- **Never use emojis** in wireframes or any design artifact. Not for icons, not for illustrations, not for anything. Emojis are not design.
- For small UI icons (navigation, actions, status indicators): use the **Hugeicons** library.
- For illustrations and large decorative icons: use **thiings.co** (https://www.thiings.co/things).
- Reference icons by name and library, e.g., "Hugeicons / arrow-left" or "thiings / clipboard".

**Components (do this before writing any HTML):**

If a design system MCP is connected (Dopamine 2, Storybook, etc.) — query it and produce a **Component Mapping Table** before writing any code. For each UI element in the wireframe, search the MCP for a match, read its docs, and record the mapping. Even at wireframe fidelity, use real component names so the design translates cleanly to high-fi.

```
| UI Element     | Design System Component     | Notes              |
|----------------|-----------------------------|--------------------|
| Tab bar        | HorizontalTabs/highlighted  | —                  |
| Input field    | TextInput/Default           | —                  |
| Share panel    | BottomSheet/Default         | —                  |
| Custom: badge  | —                           | New component needed |
```

The table is the contract — every element in the HTML traces back to a row. If a row has no design system match, that's an explicit decision, not a silent skip. Don't invent styled versions of components that exist in the system.

If no design system is provided, use standard mobile patterns (bottom sheet, card, list item, tab bar) and name them clearly.

**Spacing and layout:**
- Use consistent spacing. Pick an 8px grid and stick to it.
- Content should have breathing room — don't pack everything edge-to-edge.
- Group related items visually. Separate unrelated groups with whitespace, not dividers everywhere.

## What the output looks like

```markdown
# Wireframe Specification

## Screen Purpose
...

## Primary User Action
...

## Layout (360×800px mobile)
- Status bar: ...
- Header: ...
- Main content: ...
- Supporting content: ...
- Bottom action / nav: ...

## Content Blocks
- ...

## Component Mapping
- [element] → [design system component name] or [standard pattern]
- ...

## Icon Usage
- [element] → [library / icon name]
- ...

## Interaction Notes
- ...

## States
- Default:
- Loading:
- Empty:
- Error:
- Success:
```

## How to deliver the artifact

**Always save as an HTML file and publish with the Artifact tool.** Don't render the wireframe inline in chat via `show_widget`. Inline diagrams are for reasoning during Steps 1–5. The wireframe itself is a shareable artifact the designer sends to their team.

**Multi-screen flows get tabs.** If the wireframe covers multiple screens (it usually does), include a tab bar or screen switcher so the viewer can flip between them — don't stack screens in one long scroll.

**Phone frame at 360×800.** The wireframe renders inside a phone-shaped frame at 360×800px, centered on the page. Tab switcher sits outside the frame.

**Pages vs. bottom sheets.** Classify each surface from the solution step:

- **Pages** (distinct destination or task) → own tab. Examples: home, search, detail page, checkout.
- **Bottom sheets** (contextual action on a page) → slide-up overlay on the parent page's tab. Examples: share, filter, sort, date picker, confirmation, quick selection.

If the user triggered it from a page and returns to that page when done, it's a bottom sheet — not a new tab. In the wireframe, bottom sheets appear as a panel covering the lower 40–70% of the phone frame, with a drag handle at top and the parent page dimmed behind. The trigger button on the parent page toggles the sheet open.

**Include edge-case screens.** Error states, empty states, and recovery flows should be separate tabs with visible retry/refresh actions. These screens matter most and get skipped most — don't skip them.

**Interactivity.** Wire up buttons and CTAs to advance between screens. Back buttons should work. Bottom sheet triggers should open the sheet with a slide-up transition. The wireframe should feel navigable, not static.

## Visual quality when building HTML

- Phone frame: **360×800px**, centered, subtle device border.
- Clean sans-serif font (system-ui) at realistic mobile sizes.
- No emojis. Use simple SVG shapes for icon placeholders, or reference the icon by name in a label.
- Keep it grayscale or near-grayscale — this is a wireframe, not a mockup.
- Show real content, not "Lorem ipsum". Use realistic names, prices, labels.
- All interactive elements must have click handlers from the start.

## Post-artifact self-check

After writing the HTML, scan your code before publishing. For every styled element, check it against the Component Mapping Table you produced earlier:

- If you wrote custom styles for a component that has a design system match in the table — replace it with the system's structure.
- If you used layout, spacing, or sizing values that contradict the design system's patterns — match them.
- Even at wireframe fidelity, the component *structure* (height, padding, border-radius pattern) should match the system. The *colors* can stay grayscale.

## Ground rules

- Structure over styling. Always. That's the whole point of a wireframe.
- One clear primary action per screen. If there are two, you haven't decided yet.
- Make the hierarchy explicit — don't leave it for someone to figure out later.
- Skip decorative detail unless it actually affects whether someone understands the screen.
- If a Storybook or design system was provided and you ignored it, you've failed this step.
