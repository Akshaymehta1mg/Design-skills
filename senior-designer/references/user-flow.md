---
name: user-flow
description: Turn a board or recommendation into a clear user flow, journey, task flow, or FigJam-ready flow structure.
---

# User Flow

## What this step is for

This is where you map out the path a user takes from start to finish. Where do they enter? What decisions do they face? Where can things go wrong? What does success look like? A good flow makes the experience legible — to the team building it and to anyone reviewing it later.

## How to think through it

1. Where does the user enter this flow? What brought them here?
2. What's their goal — what does "done" look like for them?
3. Walk through each step in order.
4. Flag the decision points — where do they choose between paths?
5. Add the system states (loading, processing, waiting).
6. Map out the failure and recovery paths — what happens when things go wrong, and how do they get back on track?
7. End with the success state.

## What the output looks like

```markdown
# User Flow

## Entry Point
...

## Success State
...

## Main Path
1. ...
2. ...
3. ...

## Decision Points
- If ..., then ...

## Edge Paths
- ...

## Recovery Paths
- ...

## FigJam Structure
- Start node:
- Screen nodes:
- Decision nodes:
- Error nodes:
- Success node:
```

## Ground rules

- Use verbs for step names. "Select plan" not "Plan selection."
- Keep each step atomic — one action per step.
- Include the user's intent, not just what the system does. "User picks a delivery date" not "System displays calendar."
- Show alternate paths only when they actually matter for the design. Not every edge case needs to be on the flow.
