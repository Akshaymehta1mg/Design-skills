---
name: prd
description: Use this subskill to turn board context and UX recommendations into a product requirements document.
---

# PRD

## Purpose

Use this subskill to turn board context and UX recommendations into a product requirements document.

## Required Inputs

- Problem articulation.
- Recommended UX direction.
- User type.
- Product goal.
- Screens or flow involved.
- Constraints and assumptions.

## Output Format

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

## States And Edge Cases
- Loading:
- Empty:
- Error:
- Permission:
- Success:

## Analytics And Success Metrics
- ...

## Dependencies
- ...

## Open Questions
- ...

## Launch Criteria
- ...
```

## Rules

- Keep requirements testable.
- Separate goals from non-goals.
- Include edge states.
- Do not write vague requirements like "make it intuitive"; specify the behavior.
