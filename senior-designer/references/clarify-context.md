---
name: clarify-context
description: Use this subskill to decide whether to ask the user targeted questions or proceed with stated assumptions.
---

# Clarify Context

## Purpose

Use this subskill to decide whether to ask the user questions or proceed with assumptions.

## Confidence Test

Ask these internally:

- Do I know who the user is?
- Do I know what outcome the user wants?
- Do I know what the product wants?
- Do I know what artifact the user requested?
- Do I know whether I should critique, redesign, document, or build?
- Would missing information change the recommendation?

## Decision

### Proceed Without Questions

Proceed when:

- The requested artifact is clear.
- The board gives enough context.
- Missing details can be handled as assumptions.
- The solution can be useful without extra input.

State assumptions briefly.

### Ask Questions First

Ask questions when:

- The goal is ambiguous.
- The artifact type is unclear.
- The screen could serve multiple user types.
- There are conflicting annotations.
- A major constraint is missing.
- The user asks for "right UX" but the success metric is unclear.

Ask 2 to 4 questions maximum.

## Question Patterns

Use targeted questions:

- "Is this for first-time users, returning users, or admins?"
- "Which outcome matters most here: completion, conversion, trust, speed, or learning?"
- "Can the flow structure change, or should the solution stay within the current screens?"
- "Is this meant to become a PRD, FigJam flow, wireframe, or high-fidelity Figma screen?"
- "What is the main constraint: engineering effort, brand consistency, compliance, or time?"

## Output Format

If proceeding:

```markdown
## Clarification Decision

I can proceed with these assumptions:
- ...
```

If asking:

```markdown
## Clarifying Questions

1. ...
2. ...
3. ...
```

## Rules

- Do not ask more than 4 questions.
- Do not ask questions just to sound thorough.
- If confidence is medium, proceed and name assumptions.
- If the user asked for a quick answer, ask fewer questions or none.
