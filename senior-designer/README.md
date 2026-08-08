# Senior Designer

Senior Designer is a reusable product-design skill for turning incomplete briefs, research, screens, flows, and product constraints into a clear design direction and an appropriate design artifact.

It behaves like a senior product designer working alongside another designer: it first builds shared understanding, then frames the problem, explores the solution, plans the user’s understanding and information hierarchy, and only then produces the requested output.

## What it does

- Reads the supplied context before proposing changes
- Separates observed information from assumptions
- Asks only questions that could materially change a design decision
- Builds an editable, narrated user story
- Helps the user correct or refine that story before it becomes the foundation of the solution
- Reframes broad symptoms into a specific design problem
- Explores distinct solution directions and explains the chosen trade-offs
- Defines whether the product should explain, guide, recommend, act, or support over time
- Considers the experience before, during, immediately after, and beyond the primary action
- Maps what the user thinks, sees, understands, decides, and still worries about at each stage
- Plans content and information hierarchy before drawing screens
- Chooses between pages, bottom sheets, inline disclosure, dialogs, and system feedback based on context and decision weight
- Routes the request to the appropriate artifact guidance

## Core workflow

```text
Understand what was shared
        ↓
Say back the current understanding
        ↓
Resolve material questions and assumptions
        ↓
Build and confirm the user story
        ↓
Frame the design problem
        ↓
Explore and choose a solution direction
        ↓
Map the user’s understanding across the journey
        ↓
Plan content, hierarchy, and surfaces
        ↓
Produce the requested design output
```

The workflow adapts to the request. A narrow screen review does not require the same depth as a new product problem or multi-stage journey.

## Reference structure

| Reference | Responsibility |
| --- | --- |
| `read-board.md` | Understand complex boards and multi-frame visual context |
| `articulate-problem.md` | Reframe the supplied problem into a design-shaped challenge |
| `user-story.md` | Build, narrate, confirm, and revise the user story |
| `solution.md` | Explore directions, define the product role, and choose the recommendation |
| `user-understanding.md` | Map comprehension, decisions, concerns, and transitions across stages |
| `user-flow.md` | Define journeys, branches, recovery paths, and state changes |
| `wireframe.md` | Plan screen purpose, hierarchy, content, surfaces, and wireframe structure |
| `content-design.md` | Create product language that supports comprehension and action |
| `ui-review.md` | Review an existing screen or interface |
| `figma-screen.md` | Guide high-fidelity screen and component decisions |
| `prd.md` | Turn the design direction into product requirements |
| `research-plan.md` | Plan research around meaningful unknowns |
| `research-script.md` | Prepare interview and usability-session guidance |
| `sticky-notes.md` | Synthesize notes, annotations, and board inputs |

## Output principles

- Start with the design conclusion, not process narration
- Explain recommendations in the user’s language
- Make assumptions visible
- Tie every recommendation to the user story and design problem
- Give every screen or stage one clear responsibility
- Show essential information before asking for a consequential decision
- Keep secondary details available without competing with the primary task
- Use real content when planning screens
- Treat loading, error, empty, success, permission, and recovery states as part of the experience
- State important trade-offs and unresolved dependencies

## Boundaries

Senior Designer can assess the coherence of a problem, story, solution, flow, and artifact using the information supplied. It does not present assumptions as research findings or treat an artifact as proof of real-world usability. Claims requiring confirmation from users, domain specialists, policy, legal, engineering, accessibility, or leadership should remain clearly identified.
