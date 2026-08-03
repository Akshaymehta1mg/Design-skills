---
name: artifact-router
description: Use this subskill to choose the correct final artifact after the design problem and solution direction are clear.
---

# Artifact Router

## Purpose

Use this subskill to choose the correct final artifact after the design problem and solution direction are clear.

## Routing Table

| User asks for | Route to |
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

## Decision Rules

- If the user explicitly names an artifact, use that artifact.
- If the user asks for "right UX" without an artifact, answer with `solution.md`.
- If the user asks to "make it on the board," use `sticky-notes.md`, `user-flow.md`, or `figma-screen.md` depending on the output.
- If the user asks for implementation-ready product detail, use `prd.md`.
- If the user asks what to test or validate, use `research-plan.md`.
- If the user asks what to ask users, use `research-script.md`.
- If the user asks to improve the interface structure but not visual polish, use `wireframe.md`.
- If the user asks for final UI, use `figma-screen.md`.

## Output Format

```markdown
## Artifact Decision

**Selected artifact**
...

**Reason**
...

**Subskill to call**
...
```

## Rules

- Choose one primary artifact unless the user asks for multiple.
- If multiple artifacts are useful, produce the requested one first and mention the next useful one.
- Do not ask the user to choose if their prompt already implies a clear artifact.
