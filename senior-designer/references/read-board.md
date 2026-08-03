---
name: read-board
description: Use this subskill to inspect selected Figma or FigJam content and convert messy visual context into a clear board interpretation.
---

# Read Board

## Purpose

Use this subskill to inspect selected Figma or FigJam content and convert messy visual context into a clear board interpretation.

## Inputs

Inspect:

- Selected frames and their order.
- Frame names and section labels.
- Screenshots and UI states.
- Flow arrows and connectors.
- Sticky notes, comments, and annotations.
- Highlighted areas, circles, callouts, and text notes.
- User prompt and recent conversation.

## Process

1. Identify the artifact type:
   - App screen
   - User flow
   - Concept sketch
   - Product critique
   - Research synthesis board
   - Roadmap or planning board
   - Mixed context

2. Identify the likely product area:
   - Onboarding
   - Activation
   - Search or discovery
   - Checkout or conversion
   - Settings or admin
   - Collaboration
   - Support or recovery
   - Analytics or reporting
   - Other

3. Parse visible evidence:
   - Main screens
   - Primary actions
   - User decision points
   - System states
   - Error or edge states
   - Notes or objections from reviewers

4. Infer the story:
   - Who is using this?
   - What are they trying to do?
   - What happens before this moment?
   - What happens after this moment?
   - Where does the flow feel uncertain or broken?

5. Mark ambiguity:
   - Missing user type
   - Missing business goal
   - Missing entry point
   - Missing success state
   - Missing constraints
   - Conflicting annotations

## Output Format

```markdown
## Board Understanding

**What this appears to show**
...

**Likely user goal**
...

**Flow or state shown**
...

**Important notes and annotations**
...

**Visible friction**
...

**Assumptions**
...

**Unclear points**
...
```

## Rules

- Do not solve yet.
- Do not invent product context without marking it as an assumption.
- Treat annotations as first-class context.
- If selected content is too sparse, say what is missing.
