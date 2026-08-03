---
name: user-flow
description: Use this subskill to convert a board or recommendation into a clear user flow, journey, task flow, or FigJam-ready flow structure.
---

# User Flow

## Purpose

Use this subskill to convert a board or recommendation into a clear user flow, journey, task flow, or FigJam-ready flow structure.

## Process

1. Define the entry point.
2. Define the user's goal.
3. List each step in order.
4. Identify decision points.
5. Add system states.
6. Add failure and recovery paths.
7. End with the success state.

## Output Format

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

## Rules

- Use verbs for step names.
- Keep each step atomic.
- Include the user's intent, not only system actions.
- Show alternate paths only when they matter.
