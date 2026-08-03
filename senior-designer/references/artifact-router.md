---
name: artifact-router
description: Figure out which artifact to produce once the problem and solution direction are clear.
---

# Pick the Right Artifact

## What this step is for

You've understood the problem and have a direction. Now figure out what to actually make. This step matches what the designer is asking for to the right output format.

## Routing table

| What they're asking for | Where to go |
| --- | --- |
| PRD, product requirements, product spec | `prd.md` |
| User flow, journey, task flow, flowchart | `user-flow.md` |
| Research plan, validation plan, test plan | `research-plan.md` |
| Interview script, usability test script | `research-script.md` |
| Wireframe, layout, low-fidelity screen | `wireframe.md` |
| UI critique, UX review, heuristic audit | `ui-review.md` |
| Sticky notes, board comments, FigJam notes | `sticky-notes.md` |
| Figma screen, high-fidelity UI, component design | `figma-screen.md` |
| Microcopy, content, labels, empty states | `content-design.md` |

## How to decide

- If they explicitly named an artifact, use that one.
- If they asked for "the right UX" without naming an artifact, go with `solution.md`.
- If they said "make it on the board," use `sticky-notes.md`, `user-flow.md`, or `figma-screen.md` depending on what the output actually is.
- If they want implementation-ready product detail, use `prd.md`.
- If they want to know what to test or validate, use `research-plan.md`.
- If they want to know what to ask users, use `research-script.md`.
- If they want to improve the interface structure but aren't worried about visual polish, use `wireframe.md`.
- If they want final UI, use `figma-screen.md`.

## What the output looks like

```markdown
## Artifact Decision

**Selected artifact**
...

**Why this one**
...

**What to build with**
...
```

## Ground rules

- Choose one primary artifact unless they explicitly ask for multiple.
- If more than one artifact would be useful, produce the one they asked for first and mention the next useful one.
- Don't ask them to choose if their prompt already makes the artifact clear.
