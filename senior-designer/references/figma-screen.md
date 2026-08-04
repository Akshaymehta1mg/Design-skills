---
name: figma-screen
description: Create or revise a high-fidelity screen — a real, buildable UI that uses the product's existing design system and looks like actual shipping product.
---

# Figma Screen

## What this step is for

This is where the design gets real. You're creating (or revising) a screen that looks like the actual product — using real components, real content, and the existing visual system. This isn't a wireframe or a sketch. It's what the thing should actually look like.

## How to think through it

1. Look at nearby frames and the existing visual system. What patterns are already established?
2. Identify reusable components, styles, typography, spacing, and interaction patterns.
3. Define the screen's purpose and its primary action.
4. Create or revise the screen, staying within the existing design direction wherever possible.
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
- For small UI icons (nav, actions, status, form elements): use the **Hugeicons** library. Reference by name: "Hugeicons / chevron-right", "Hugeicons / search", etc.
- For illustrations, onboarding graphics, empty states, and large decorative icons: use **thiings.co** (https://www.thiings.co/things). Reference by name: "thiings / clipboard", "thiings / check-circle", etc.
- When rendering via `show_widget`, use simple SVG paths for icons or reference them by label. Don't substitute Unicode symbols or emojis.

**Components and design system:**
- If the user provided a **Storybook**, component library, or design system reference — **use those exact components.** Match the names, variants, and states from the system.
- Don't invent a custom card when the system has "Card/Default". Don't create a new button style when "Button/Primary/Medium" exists.
- If the system specifies spacing tokens, color tokens, or corner radius values — use them.
- If no design system is provided, use clean standard mobile patterns and document what you used so it can be translated into the actual system later.

**Spacing and layout:**
- Use an 8px grid. All spacing should be a multiple of 8 (8, 16, 24, 32, 40).
- Horizontal padding: 16–20px on mobile. Not edge-to-edge, not 32px margins.
- Vertical rhythm: consistent spacing between content blocks. Group related items tightly (8–12px), separate groups with more space (24–32px).
- Cards should have 12–16px internal padding. Not 24px — that wastes mobile real estate.

**Content:**
- Use realistic content. Real names, real prices, real copy. Not "User Name" or "$XX.XX".
- Copy should sound like the product's voice. Read the existing UI before writing new copy.
- If the screen has a CTA, the label should be a specific verb, not "Submit" or "Continue" unless that's genuinely the right word.

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

## When rendering as show_widget

If you're producing the screen as an inline visual:

- Set the SVG viewBox or HTML container to **360×800** (or a proportional crop for a single section).
- Use realistic mobile text sizes. 14px body, 20px title — not 24px body and 36px title.
- No emojis anywhere. Use simple SVG paths or labeled rectangles for icon placeholders.
- Show real, specific content — not placeholder text.
- Use a proper color palette. If the product's brand colors are known, use them. Otherwise use a clean neutral palette.
- Match the spacing to an 8px grid. Elements shouldn't float in random positions.

## Ground rules

- If you're writing directly into Figma, follow the Figma tool workflow for file context.
- If you're describing the screen, provide a spec specific enough that another designer could build it in Figma without asking questions.
- If a Storybook or design system was provided and you didn't use its components, that's a failure. Go back and match them.
- Skip purely decorative changes unless they improve comprehension, trust, or task completion.
- The screen should look like it belongs in the existing product — not like a redesign from a different company.
