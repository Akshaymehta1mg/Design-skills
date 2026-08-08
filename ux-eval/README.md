# UX Eval

UX Eval is a design-review skill for evaluating both a proposed product experience and the reasoning that produced it.

It acts as a constructive evaluation partner after a designer or design agent has framed a problem, proposed a direction, mapped a flow, created a wireframe, designed an interface, built a prototype, or implemented an experience.

## What it evaluates

- Whether the designer understood enough about the problem, user, product, and constraints
- Whether the questions asked were useful and material
- Whether important assumptions were stated and reasonable
- Whether the user story is supported by the supplied context
- Whether the solution addresses the underlying difficulty
- Whether the product is taking an appropriate role
- What the user understands, decides, and still worries about at every stage
- Whether information appears at the right time and in the right hierarchy
- Whether page, sheet, inline, dialog, and feedback choices fit the interaction
- Whether the artifact communicates the intended experience at its current maturity
- Whether control, transparency, recovery, trust, and consequences are handled appropriately

## Core workflow

```text
Inspect the available material
        ↓
Identify the artifact and its maturity
        ↓
Review the designer’s understanding
        ↓
Reconstruct the user story
        ↓
Evaluate the solution direction
        ↓
Map the user’s understanding
        ↓
Apply the relevant artifact review
        ↓
Prioritise findings
        ↓
Discuss material questions with the designer
        ↓
Review the revision
```

The evaluator applies only the criteria relevant to the supplied artifact. A wireframe is reviewed for structure, hierarchy, content, actions, states, and surface choices—not for final visual polish or production implementation.

## Evidence states

UX Eval distinguishes between:

- **Observed** — directly visible in the supplied material
- **Inferred** — a reasonable interpretation that is not explicitly shown
- **Not shown** — the material does not provide enough information
- **Not applicable** — outside the artifact’s purpose or maturity

“Not shown” is not automatically treated as a design failure.

## Finding priorities

| Priority | Meaning |
| --- | --- |
| Blocker | The direction may fail, cause harm, break trust, or conflict with a critical constraint |
| Important | The issue is likely to create confusion, hesitation, unnecessary effort, or a weaker outcome |
| Polish | The central experience works, but craft or consistency can improve |
| Open question | Missing context prevents a confident judgment |

Every finding describes what was observed, why it matters, where it appears, what should be reconsidered, and how confident the evaluator is.

## Reference structure

| Reference | Responsibility |
| --- | --- |
| `understand-the-design.md` | Review the assignment, questions, assumptions, and user story |
| `review-the-solution.md` | Evaluate problem fit, product role, decisions, control, and the complete journey |
| `map-user-understanding.md` | Review what users know, decide, expect, and worry about across stages |
| `review-the-artifact.md` | Apply criteria appropriate to the artifact and its maturity |
| `feedback-and-revision.md` | Prioritise findings, support designer dialogue, and review revisions |

## Output principles

- Evaluate design thinking before interface polish
- Ask only questions that could change the evaluation
- Prefer a few prioritised findings over a large checklist
- Explain why each concern matters to the specific user and outcome
- Preserve decisions that are working
- Distinguish missing evidence from missing design
- Reconsider findings when the designer provides relevant context
- Review changed areas and their effects instead of repeating the complete evaluation
- Avoid numerical scoring unless explicitly requested
- Never translate a high score into permission to ship

## Boundaries

UX Eval can assess internal coherence, completeness, clarity, interaction logic, and alignment with the supplied context. It cannot confirm that the context is true, that users will behave as assumed, or that undisclosed business, legal, policy, brand, accessibility, or technical requirements have been satisfied.
