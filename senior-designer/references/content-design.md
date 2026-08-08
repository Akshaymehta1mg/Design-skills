---
name: content-design
description: Define information hierarchy and write interface language that helps the user understand, decide, act, and recover.
---

# Content Design

## Purpose

Interface language is part of the experience. Use content to establish context, support decisions, explain consequences, set expectations, and help the user recover. Write only after understanding the user's stage and the job the content must do.

## Start with the moment

For each state, identify:

- what the user arrives thinking or expecting;
- what they need to understand now;
- what decision or action follows;
- what may create hesitation or mistrust;
- what the product knows, infers, recommends, or has done;
- what happens after the user acts.

If the content spans multiple stages, use `user-understanding.md` before drafting copy.

## Define the content job

Assign each content element a job:

- orient the user;
- explain a concept or status;
- support a decision;
- state a consequence;
- set an expectation;
- communicate a limitation;
- request permission or confirmation;
- show progress or feedback;
- help recovery;
- confirm completion and next steps.

Remove content that has no clear job in the current state.

## Set the hierarchy

Prioritize content in this order unless the user context requires otherwise:

1. What is happening or what the stage is for.
2. What the user needs to understand or decide.
3. Material consequence, limitation, cost, risk, or control.
4. The action that moves the user forward.
5. Supporting explanation or optional detail.

Do not use progressive disclosure to hide information that could change the user's decision.

## Write the interface language

- Use the user's vocabulary unless precision, safety, or regulation requires another term.
- Explain unfamiliar terms at the point where they affect understanding.
- Write action labels that describe the action or outcome.
- Keep product statements, recommendations, and user choices distinguishable.
- State uncertainty and limitations clearly.
- Use reassurance only when the interface provides the evidence or control to support it.
- Explain what changed after an action and what happens next.
- In error states, state what happened, what remains safe, and how to recover.
- Match detail to the user's prior knowledge and the consequence of the decision.

## Output structure

```markdown
# Content Design

## User Moment
...

## Content Goal
...

## Information Hierarchy
1. ...
2. ...

## Interface Copy
- Orientation:
- Primary message:
- Supporting message:
- Primary action:
- Secondary action:
- Helper or disclosure:
- Feedback:
- Error and recovery:
- Completion and next step:

## Content Rationale
- ...

## Terminology Decisions
- ...

## Assumptions or Open Questions
- ...
```

## Quality check

- The main message matches what the user needs at this stage.
- Important information appears before the decision it supports.
- The action label makes its consequence predictable.
- Language does not imply certainty, permission, or capability the product does not have.
- Material consequences are clear and not visually or verbally minimized.
- Terminology remains consistent across stages.
- Error and completion content explain the next available action.
- Every line earns its place in the hierarchy.
