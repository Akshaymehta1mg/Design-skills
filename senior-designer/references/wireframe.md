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

**Components:**
- If a design system MCP is connected (Dopamine 2, Storybook, etc.) — **query it before building.** List the components, search for the ones you need, and read their docs. Even at wireframe fidelity, reference real component names so the design translates cleanly to high-fi.
- Match the component names, states, and variants from the design system. If the system has `HorizontalTabs/highlighted`, reference that — don't describe a custom tab bar.
- Also check available patterns — they show how the product composes pages. A wireframe that follows the product's existing page patterns feels right even at low fidelity.
- Only introduce a new component when nothing in the system fits. Flag it explicitly: "New component — no match in current system."
- If no design system is provided, use standard mobile patterns (bottom sheet, card, list item, tab bar) and name them clearly.

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

## When rendering as show_widget

If you're producing the wireframe as an inline visual (SVG or HTML via `show_widget`):

- Set the viewport to **360×800** or a proportional slice of it.
- Use a clean sans-serif font (system-ui) at realistic mobile sizes.
- No emojis. Use simple SVG shapes for icon placeholders, or reference the icon by name in a label.
- Keep it grayscale or near-grayscale — this is a wireframe, not a mockup.
- Show real content, not "Lorem ipsum". Use realistic names, prices, labels.
- If you're showing multiple screens, keep them at the same scale. Don't stretch one to fill space.

## Ground rules

- Structure over styling. Always. That's the whole point of a wireframe.
- One clear primary action per screen. If there are two, you haven't decided yet.
- Make the hierarchy explicit — don't leave it for someone to figure out later.
- Skip decorative detail unless it actually affects whether someone understands the screen.
- If a Storybook or design system was provided and you ignored it, you've failed this step.
