---
name: solution
description: Explore, compare, and recommend a product experience direction after the user story and design problem are understood.
---

# Design the Solution

## Purpose

Choose how the product should help the user, then shape the experience around that choice. Review solution quality before designing screens. A stronger solution changes the user's ability to make progress; it does not only rearrange interface elements.

## 1. Set the decision frame

Carry forward:

- the working user story;
- the underlying design problem;
- the desired user and product outcomes;
- known capabilities and constraints;
- assumptions that could change the direction.

State what the solution must achieve and what it must avoid. If the frame is not stable enough to compare directions, return to the missing context rather than inventing precision.

## 2. Decide the product role

Choose the role the product plays at each important moment:

- **Explain:** help the user understand information, status, or consequences.
- **Guide:** structure the process while the user remains the decision-maker.
- **Recommend:** propose a direction with reasons, limits, and alternatives.
- **Act:** take action within explicit permission, scope, and controls.

The role may change across the journey, but each change must be intentional. Define:

- what the product knows;
- what it infers;
- what it proposes;
- what it may do;
- what requires user review or consent;
- how the user can change, pause, undo, or recover;
- how the product explains its reasoning and limitations.

Use less product autonomy when confidence, permission, reversibility, or consequence is unclear.

## 3. Choose the journey scope

Decide whether the problem needs:

- a one-time task;
- a repeated workflow;
- an ongoing product relationship;
- or a connected set of these.

Map the relevant time horizon:

- **Before:** trigger, current behavior, expectation, and entry point.
- **During:** understanding, decisions, actions, feedback, and recovery.
- **Immediately after:** confirmation, status, next step, and retained control.
- **Over time:** progress, reminders, changes, learning, or return behavior.

Do not make an ongoing system when the need is truly temporary. Do not end at transaction completion when the user's outcome continues beyond it.

## 4. Explore distinct directions

Create a small set of directions that differ in behavior or product role, not only in layout. For each direction, define:

- the central idea;
- how the journey changes;
- the product role;
- the degree of user control;
- what it requires from the product or operation;
- the main advantage;
- the main risk or trade-off;
- what would make the direction inappropriate.

Include prevention, support at the point of difficulty, and recovery as lenses when relevant. These lenses may be combined, but one should be the center of gravity.

## 5. Compare and choose

Compare directions against:

- fit with the user story;
- ability to resolve the underlying problem;
- clarity and effort for the user;
- product capability and constraint fit;
- safety, trust, consent, and reversibility;
- effect on the complete journey;
- implementation and operational complexity;
- durability as user needs or product conditions change.

Recommend one direction. Explain why it leads, why the alternatives do not lead, and which useful parts of them should remain.

## 6. Describe the experience architecture

For the recommended direction, define:

- entry points and triggers;
- stages in the journey;
- decisions and information required at each stage;
- system behavior and feedback;
- alternate, error, and recovery paths;
- completion and post-completion experience;
- ongoing states when relevant;
- dependencies and unresolved questions.

Route to `user-understanding.md` before finalizing the order of information and decisions.

## 7. Choose interaction surfaces intentionally

Classify each important interaction as a page, bottom sheet, inline disclosure, dialog, or system feedback.

- **Page:** a distinct destination, sustained task, or deep information space.
- **Bottom sheet:** a temporary contextual task that preserves the parent context and can be dismissed without losing progress.
- **Inline disclosure:** supporting information or a lightweight choice that belongs directly within the current content.
- **Dialog:** a focused interruption that requires immediate acknowledgement or a bounded decision.
- **System feedback:** a status or result communicated without creating a new task surface.

Decide using:

- continuity with the current context;
- depth and duration of the task;
- amount of information required;
- decision weight and consequence;
- reversibility and interruption;
- need to compare with the parent content;
- navigation expectations;
- accessibility and device constraints.

Do not use a bottom sheet as a default for every secondary action. Do not create a new page merely because a state needs to be shown.

## 8. Narrate the recommendation

Explain the recommendation in design language:

1. The user's need at the moment.
2. The experience principle guiding the decision.
3. What the product does.
4. What the user understands and controls.
5. Why the sequence and hierarchy work.
6. What is deliberately deferred, removed, or left manual.
7. The trade-off being accepted.

## Output structure

```markdown
## Recommended Direction

**Design problem**
...

**Product role**
...

**Journey scope**
...

**Directions considered**
| Direction | User fit | Product fit | Control and trust | Complexity | Main trade-off |
| --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... |

**Chosen direction and rationale**
...

**Experience architecture**
- Before:
- During:
- Immediately after:
- Over time:

**Important surface decisions**
- ...

**Edge and recovery paths**
- ...

**Trade-offs and dependencies**
- ...

**Open questions**
- ...

**Recommended next level of detail**
...
```

## Quality check

- The recommendation follows from the user story and design problem.
- The product role and degree of user control are explicit.
- The chosen direction was compared with meaningfully different alternatives.
- The solution covers the relevant time horizon.
- The experience uses product capabilities without hiding uncertainty or limitations.
- Information, actions, and surfaces have a reason tied to the user's stage.
- Risks and trade-offs are concrete.
- The narration explains the reasoning instead of presenting screens as the solution.
