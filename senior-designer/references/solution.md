---
name: solution
description: Use this subskill to generate the core UX recommendation after the board has been read and the problem has been articulated.
---

# Solution

## Purpose

Use this subskill to generate the core UX recommendation after the board has been read and the problem has been articulated.

## Process

1. Diagnose:
   - What is not working?
   - Why is it not working?
   - What user behavior or confusion does it create?

2. Choose direction:
   - Simplify
   - Reorder
   - Clarify
   - Add guidance
   - Remove friction
   - Change hierarchy
   - Split the flow
   - Add feedback states
   - Improve trust
   - Improve recovery

3. Design the recommendation:
   - Screen or flow change
   - Copy change
   - Interaction change
   - State change
   - Information architecture change
   - Visual hierarchy change

4. Consider tradeoffs:
   - Engineering cost
   - Learning curve
   - Business impact
   - Accessibility
   - Edge cases
   - Consistency with existing product

5. Define next step:
   - Validate with users
   - Make wireframe
   - Create Figma screen
   - Write PRD
   - Turn into research plan
   - Add sticky notes to board

## Output Format

```markdown
## UX Recommendation

**Diagnosis**
...

**Recommended direction**
...

**Why this works**
...

**Changes to make**
- ...

**Edge states**
- ...

**Tradeoffs**
- ...

**Next step**
...
```

## Rules

- Be opinionated but explain the reasoning.
- Tie each recommendation back to the problem.
- Include copy recommendations when UI language is part of the friction.
- Avoid generic advice like "make it cleaner" without saying how.

## Stance check (before finalising)

A senior designer diverges before converging. It is easy to commit to one stance without noticing you had a choice. This check forces you to see the choice.

Classify each intervention you proposed by its stance in the user's journey:

- **Prevent** — removes the friction moment entirely (e.g., let the user upload a prescription so they never see the ambiguous search).
- **Assist** — supports the user at the friction moment (e.g., a disambiguation strip and richer cards on the search page).
- **Recover** — makes it cheap to fix when the user goes wrong (e.g., a "not the right test?" rescue link on the detail page).

Then answer three questions:

1. Which stance is the *primary* one in your solution? Pick one — "all three equally" is a dodge. Every solution has a centre of gravity.
2. If you led with a different stance, what would the solution look like? Describe the alternative concretely, in one paragraph. Not "we could also prevent it" — actually sketch the Prevent-first version.
3. Given the constraints, is your chosen primary the right one? If yes, name *why not the other two*.

If you cannot answer question 2 with a genuinely different alternative, the divergent thinking did not happen — you defaulted to one stance without exploring. Go back and try.

This step is not a formality. When a solution feels obvious, it is usually because one stance dominated your thinking silently. Making the alternatives explicit is how you catch that.
