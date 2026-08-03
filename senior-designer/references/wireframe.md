---
name: wireframe
description: Create a low-fidelity screen or flow structure — the bones of the design before any visual polish.
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
7. If this needs to work on mobile, describe how the layout adapts.

## What the output looks like

```markdown
# Wireframe Specification

## Screen Purpose
...

## Primary User Action
...

## Layout
- Header:
- Main content:
- Supporting content:
- Footer/actions:

## Content Blocks
- ...

## Interaction Notes
- ...

## States
- Default:
- Loading:
- Empty:
- Error:
- Success:

## Mobile Behavior
...
```

## Ground rules

- Structure over styling. Always. That's the whole point of a wireframe.
- One clear primary action per screen. If there are two, you haven't decided yet.
- Make the hierarchy explicit — don't leave it for someone to figure out later.
- Skip decorative detail unless it actually affects whether someone understands the screen.
