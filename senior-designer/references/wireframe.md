---
name: wireframe
description: Turn an agreed flow and comprehension sequence into low-to-mid-fidelity screen and surface structure.
---

# Wireframe

## Purpose

A wireframe communicates experience structure before visual polish. It should make the content, hierarchy, actions, transitions, and surface choices reviewable. Evaluate it for those decisions rather than for final color, typography, imagery, or motion.

## Before drawing

Confirm:

- the user story and entry context;
- the purpose and completion condition of the flow;
- the product role and degree of user control;
- the main path, important branches, and recovery paths;
- what the user should understand at each stage;
- the product information, capabilities, and constraints that affect the screens.

If any of these are still assumptions, keep them visible in the specification.

## Plan each stage

For every screen or surface, define:

1. **Purpose:** the single job of the stage.
2. **Arrives thinking:** the expectation or concern carried into it.
3. **Primary understanding:** what must become clear before the user continues.
4. **Primary information:** what deserves the strongest focus.
5. **Supporting information:** what helps the current decision without competing with it.
6. **Conditional information:** what appears only when relevant.
7. **Primary action:** the main action and its consequence.
8. **Secondary actions:** alternate, defer, back, change, or recovery actions.
9. **What is deferred:** information or choices intentionally moved elsewhere.
10. **Next state:** what the user and system expect after the action.

## Build the information hierarchy

Order content according to the user's decision process:

- orientation and current state;
- the primary takeaway;
- information required for the current decision;
- reassurance, evidence, or explanation;
- primary action;
- secondary or reference details.

Change this order when the user context requires it, and explain why. Do not give prominence to information only because it matters internally to the product.

Use progressive disclosure when details are useful but not required for the current decision. Do not hide consequences, limitations, cost, risk, or loss of control behind disclosure.

## Choose the surface

Classify each interaction intentionally:

| Surface | Use when | Avoid when |
| --- | --- | --- |
| Page | The user enters a distinct destination, sustained task, or deep information space | The action is temporary and depends on the parent context |
| Bottom sheet | The user completes a bounded contextual task while retaining the parent context | The content is deep, high consequence, or needs substantial navigation |
| Inline disclosure | The information or lightweight choice belongs directly beside its trigger | Expansion would make the primary content difficult to scan |
| Dialog | An immediate acknowledgement or bounded decision must interrupt the current action | The content requires exploration, comparison, or multiple steps |
| System feedback | The product needs to show status or consequence without creating a new task | The user must make a considered decision or enter substantial information |

Base the decision on:

- context continuity;
- task depth and duration;
- decision weight;
- information volume;
- reversibility;
- need to compare with parent content;
- interruption cost;
- navigation expectation;
- accessibility and device constraints.

Record the rationale for any surface that carries a consequential decision or could plausibly use another form.

## Map interaction and states

Include only states relevant to the requested fidelity, but do not omit states that change understanding or recovery:

- default;
- loading or processing;
- empty or unavailable;
- validation or error;
- permission or consent;
- partial completion;
- success;
- cancellation, undo, or recovery;
- return or ongoing state.

Show how the user moves back, changes a prior decision, exits, and resumes when these behaviors matter.

## Use the product system

When an existing design system or product pattern library is available:

1. Inspect the relevant components and composition patterns.
2. Map wireframe elements to existing patterns before creating new structures.
3. Preserve familiar behavior unless the problem requires a change.
4. Document gaps rather than silently inventing replacements.

At wireframe fidelity, component structure and behavior matter more than final styling.

## Fidelity and delivery

Match the output to the request:

- **Small structural wireframe:** show the minimum screens and content blocks needed to review the core idea.
- **Flow wireframe:** show connected screens, decisions, alternate paths, and recovery.
- **Detailed wireframe specification:** include content, states, interactions, component mapping, and responsive behavior.
- **Interactive artifact:** make important navigation, branches, overlays, and back behavior usable.

Use the user's requested medium. If none is specified, choose the lightest medium that makes the structural decision understandable. Do not add visual polish that implies decisions have been finalized when they have not.

## Output structure

```markdown
# Wireframe Specification

## Journey Context
...

## Screen and Surface Map
- ...

## Stage Specifications

### [Stage]
- Purpose:
- Arrives thinking:
- Primary understanding:
- Primary information:
- Supporting information:
- Conditional or deferred information:
- Primary action and consequence:
- Secondary actions:
- Surface and rationale:
- Next state:

## States and Recovery
- ...

## Component or Pattern Mapping
- ...

## Interaction Notes
- ...

## Assumptions and Open Decisions
- ...
```

## Quality check

- Every screen or surface has one clear purpose.
- The strongest visual focus matches the user's immediate need.
- The right information appears before the relevant decision.
- Primary and secondary actions are distinguishable.
- Progressive disclosure does not hide material consequences.
- Surface choices preserve context and match decision weight.
- The user can understand what happens next.
- Back, change, exit, and recovery behavior are addressed where needed.
- The wireframe communicates the solution without relying on final visual polish.
