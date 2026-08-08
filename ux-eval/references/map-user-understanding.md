# Map User Understanding

Use this reference when the design contains stages, screens, decisions, or transitions. Evaluate what the user needs to understand over time, not only what information is present.

## 1. Build the stage map

For each meaningful stage, capture:

| Field | Review question |
| --- | --- |
| User arrives thinking | What is the user likely to believe, expect, or worry about on arrival? |
| Information received | What does the design communicate now? |
| Intended understanding | What must the user understand before continuing? |
| Decision or action | What is the user expected to decide or do? |
| Decision support | What information, comparison, explanation, or feedback helps? |
| Remaining uncertainty | What important question may still be unanswered? |
| Expected next state | What does the user believe will happen next? |

Keep the map focused on meaningful changes in understanding. Do not create a row for every minor interaction.

## 2. Review timing

Flag when:

- A decision is requested before its supporting information appears
- A consequence is explained after commitment
- Reassurance is separated from the moment of concern
- Advanced detail appears before the user understands the basic choice
- Information is repeated without adding clarity
- A concept, term, or control appears without introduction
- The user must remember information that should remain visible

## 3. Review hierarchy

At each stage, identify:

- The one thing that needs the most attention
- Information required to make the current decision
- Supporting information that can remain secondary
- Detail that should be available on demand
- Information that should not appear yet

Check whether visual and content hierarchy reflect this order. Do not equate greater visual weight with greater user value without considering the current decision.

## 4. Review cognitive and emotional load

Check whether the stage:

- Introduces too many new ideas at once
- Uses language the intended user is unlikely to understand
- Presents choices that are not meaningfully different
- Requires unnecessary recall, calculation, comparison, or data entry
- Creates avoidable fear, pressure, or uncertainty
- Gives enough feedback to build confidence without over-explaining

## 5. Review surface choice

Evaluate where information and actions appear:

### Page or full destination

Prefer when the user is entering a new task, needs room to understand or compare, may spend meaningful time, or should be able to return to the state as a destination.

### Bottom sheet, drawer, or temporary overlay

Prefer when the user needs a short supporting decision, selection, explanation, or confirmation while keeping the parent context visible or easy to return to.

### Inline disclosure

Prefer when the detail directly explains nearby content and can expand without interrupting the task.

### Blocking dialog

Reserve for urgent decisions or consequences that require attention before the user can safely continue. Do not use a blocking surface when undo or inline feedback would preserve flow and control more effectively.

Flag surfaces that fragment the journey, hide necessary context, or give a minor decision disproportionate weight.

## 6. Review transitions

For each meaningful transition, check:

- Whether the trigger is clear
- Whether the destination is predictable
- Whether important context carries forward
- Whether the user receives immediate feedback
- Whether back, cancel, edit, and recovery behaviour are understandable
- Whether the next state answers “what happened?” and “what can I do now?”

## 7. Output for this review layer

Return:

- The stage map
- Understanding gaps in journey order
- Information shown too early or too late
- Hierarchy problems
- Surface-choice concerns
- Unresolved questions or emotional concerns
- The stage where the experience is most likely to lose the user
