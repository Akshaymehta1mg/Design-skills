---
name: user-story
description: Build a narrated, editable account of the user's context, behavior, difficulty, and desired progress before defining the experience.
---

# User Story

## Purpose

A user story is the working narrative that connects context to design. It explains how a person reaches the experience, what they are trying to do, what they do today, where they become stuck, and what would help them progress.

Treat it as a design hypothesis. It may be incomplete or partly wrong, especially when the prompt contains limited context.

## Build the narrative

Cover the parts that materially affect the design:

1. **Situation:** What is happening around the user when the need appears?
2. **Trigger:** What causes them to enter the product or journey now?
3. **Goal:** What outcome are they trying to reach in their own terms?
4. **Current behavior:** How do they handle the need today, inside or outside the product?
5. **Breakdown:** Where does progress slow, stop, or become uncertain?
6. **Understanding:** What do they already know, and what are they trying to make sense of?
7. **Emotional context:** What creates urgency, hesitation, effort, or loss of confidence?
8. **Desired progress:** What would make them feel able to continue?
9. **Afterward:** What do they expect to happen once the immediate task is complete?

Do not add personal details that do not affect the design. Do not turn demographic assumptions into motivations or behaviors.

## Separate confidence levels

Mark the basis of the story:

- **Known:** supplied directly or visible in the material.
- **Inferred:** a reasonable interpretation supported by the available context.
- **Assumed:** needed to continue but not supported yet.
- **Missing:** important information that could change the narrative or solution.

## Present it for correction

Write the story as a short connected narration, followed by the assumptions and gaps. Explicitly invite the user to correct what is inaccurate, remove what does not belong, and add missing context.

Do not require confirmation when the story is sufficient for safe progress. Continue with clearly marked assumptions unless a missing answer could change the problem, product role, journey architecture, or safety of the direction.

## Correction loop

When the user changes the story:

1. Incorporate the correction without defending the earlier inference.
2. Restate only the changed part and the revised complete meaning.
3. Identify affected design decisions.
4. Update the problem framing, solution direction, flow, or hierarchy where necessary.
5. Preserve unaffected work.
6. Keep unresolved assumptions visible.

The story remains editable throughout the design process. Later design decisions may reveal a missing or contradictory part of the narrative; return to it when needed.

## Output structure

```markdown
## Working User Story

**Narrative**
...

**What is known**
- ...

**What is inferred or assumed**
- ...

**What could change the direction**
- ...

**Design consequence**
...

**Correction invitation**
...
```

## Quality check

- The narrative starts in the user's context, not on a product screen.
- The user has a clear goal and a believable reason to act.
- The breakdown is specific enough to design for.
- Emotional context is connected to behavior rather than added for tone.
- The desired progress is expressed as a user outcome, not a feature.
- Assumptions are easy for the user to find and correct.
- The story supports the problem framing and solution without predetermining them.
