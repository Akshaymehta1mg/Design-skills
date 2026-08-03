---
name: articulate-problem
description: Use this subskill after reading the board and before proposing UX solutions to transform observed screens, flows, and notes into a clear design problem.
---

# Articulate Problem

## Purpose

Use this subskill after reading the board and before proposing UX solutions. It transforms observed screens, flows, and notes into a clear design problem.

## Process

1. Identify the user:
   - Primary user type
   - Experience level
   - Intent
   - Emotional state
   - Constraints

2. Identify the job:
   - What the user is trying to accomplish
   - What progress means to them
   - What blocks progress

3. Identify the product goal:
   - Activation
   - Conversion
   - Retention
   - Trust
   - Comprehension
   - Collaboration
   - Efficiency
   - Error recovery

4. Identify the current friction:
   - Unclear next step
   - Too many choices
   - Missing feedback
   - Poor information hierarchy
   - Broken flow logic
   - Weak motivation
   - Trust gap
   - Accessibility issue
   - Copy mismatch

5. Frame the problem:
   - User problem
   - Product problem
   - Design challenge
   - Success criteria

## Reframe check (required)

Before ending this step, state the problem in three forms. This takes a minute and stops the whole design pass from being answered against a shallow problem statement.

**Form 1 — PM framing.** The problem as stated upstream (from PM, research brief, or ticket). Take this as given — research validated it. Do not relitigate whether it is the right problem.

**Form 2 — User-symptom restatement.** The same problem in user language. Usually starts *"Users can't…"* or *"Users get confused when…"*. This is true but not useful — it names the pain without naming what to change.

**Form 3 — Design-shaped articulation.** The same problem restated in a way that names the specific mismatch the design must resolve. Shape: *"the interface is treating X like Y, when the user is doing Z"* or *"the surface asks A, but the user's real task is B"*. Everything downstream — solution direction, stance choice, artifact — should be answerable from Form 3, not Form 1.

**Self-check.** If Form 3 is Form 1 with the noun changed, you have not reframed. Look for the mismatch between what the interface offers and what the user is actually trying to do. That mismatch is the design lever.

**Example — diagnostics search:**

- Form 1: *"Users can't book the right diagnostic test on the SRP."*
- Form 2: *"Users are confused by too many similar-looking results."*
- Form 3: *"The SRP is built as a shopping surface, but doctor-initiated users are doing a translation task from prescription shorthand to app SKU. The design must bridge that gap — not filter or rank."*

## Output Format

```markdown
## Problem Articulation

**User**
...

**User goal**
...

**Current friction**
...

**Product goal**
...

**Design challenge**
How might we ...

**Success looks like**
...

**Assumptions**
...
```

## Rules

- Frame the problem before the solution.
- Keep the problem human and specific.
- Avoid generic UX language unless it is tied to visible evidence.
- Use "How might we..." only after the problem is clear.
