---
name: prd
description: Turn board context and UX recommendations into a product requirements document that engineering and product can build from.
---

# PRD

## What this step is for

This is where design thinking becomes a buildable spec. You've articulated the problem, you have a UX direction — now turn it into a document that product and engineering can actually use. A good PRD is specific enough to build from and clear enough that someone who wasn't in the room understands what's being built and why.

## What you need before you start

- A clear problem articulation.
- A recommended UX direction.
- Who the user is.
- What the product goal is.
- Which screens or flows are involved.
- Known constraints and assumptions.

## What the output looks like

```markdown
# Product Requirements Document

## Summary
...

## Problem
...

## Goals
- ...

## Non-Goals
- ...

## Target Users
...

## User Stories
- As a ..., I want ..., so that ...

## Proposed Experience
...

## Functional Requirements
- ...

## UX Requirements
- ...

## Content Requirements
- ...

## States and Edge Cases
- Loading:
- Empty:
- Error:
- Permission:
- Success:

## Analytics and Success Metrics
- ...

## Dependencies
- ...

## Open Questions
- ...

## Launch Criteria
- ...
```

## Ground rules

- Keep requirements testable. If you can't tell whether it shipped correctly, the requirement isn't specific enough.
- Separate goals from non-goals. Saying what you're *not* doing is just as important as saying what you are.
- Include edge states. The happy path is the easy part — the edge cases are where things break.
- Don't write vague requirements like "make it intuitive." Describe the actual behavior you expect.
