# Design Skills

This repository contains two complementary skills for AI-assisted product design:

- **Senior Designer** helps understand a product problem, develop a strong design direction, and create the right design output.
- **UX Eval** reviews the designer’s reasoning and output, then explains what should be preserved, reconsidered, or clarified.

You can use either skill independently or use them together as a design-and-review workflow.

## Which skill should I use?

| Your situation | Use |
| --- | --- |
| You are beginning with a problem, brief, research, or rough idea | Senior Designer |
| You need help with a user story, journey, flow, hierarchy, wireframe, or interface content | Senior Designer |
| You already have a proposed solution or design output and want a structured review | UX Eval |
| You want the designer to improve its work after a review | Senior Designer followed by UX Eval, then Senior Designer again |

## How the two skills work together

```text
Problem, brief, research, or existing experience
                    ↓
             Senior Designer
                    ↓
       Design direction or artifact
                    ↓
                UX Eval
                    ↓
         Prioritised design feedback
                    ↓
       Senior Designer revision
```

The evaluator does not replace the designer. It gives the designer a second perspective and creates a focused revision conversation.

---

## Senior Designer

Senior Designer behaves like a senior product designer working alongside you. It does not immediately jump to screens or features.

It first builds a shared understanding of:

- The problem
- The user and their situation
- The product and existing journey
- Business, policy, technical, operational, and accessibility constraints
- What happens before, during, and after the experience

It asks questions only when the answers could materially change the design. When enough is known, it states its assumptions and continues.

### Senior Designer workflow

```text
Understand what was shared
        ↓
Confirm the current understanding
        ↓
Resolve material questions and assumptions
        ↓
Build an editable user story
        ↓
Frame the design problem
        ↓
Explore and choose a solution direction
        ↓
Map what the user understands at each stage
        ↓
Plan content, hierarchy, and surfaces
        ↓
Produce the requested design output
```

### What Senior Designer can help with

- Problem framing
- Editable user stories
- Solution exploration and product direction
- User journeys and flows
- Information architecture
- Stage-by-stage user understanding
- Wireframes and screen structure
- Interface content and microcopy
- Screen and interaction critique
- Research planning and research scripts
- High-fidelity design direction
- Sticky-note and board synthesis
- Reading product briefs and PRDs

### How it works with PRDs

Senior Designer treats a product brief or PRD as an input.

It can:

- Extract confirmed decisions and constraints
- Translate product requirements into design implications
- Identify missing or conflicting information
- Clarify the user story and journey
- Contribute UX, content, state, accessibility, and interaction requirements
- Return questions to the appropriate owner

It does not claim ownership of the authoritative product document, product strategy, business rules, delivery estimates, analytics ownership, or launch approval.

Read more in [`senior-designer/README.md`](senior-designer/README.md).

---

## UX Eval

UX Eval is a design-review partner. It evaluates both the proposed experience and the reasoning that produced it.

It reviews:

- Whether the designer understood enough about the problem, user, product, and constraints
- Whether important questions were asked
- Whether assumptions are visible and reasonable
- Whether the user story is supported by the supplied context
- Whether the solution addresses the underlying difficulty
- Whether the product is taking an appropriate role
- What the user understands and decides at every stage
- Whether information appears at the right time and in the right hierarchy
- Whether the artifact communicates the intended experience at its current maturity
- Whether control, transparency, recovery, trust, and consequences are handled appropriately

### UX Eval workflow

```text
Inspect the supplied material
        ↓
Identify the artifact and its maturity
        ↓
Review the designer’s understanding
        ↓
Evaluate the solution direction
        ↓
Map the user’s understanding
        ↓
Review the relevant artifact decisions
        ↓
Prioritise findings
        ↓
Discuss material questions
        ↓
Review the revision
```

UX Eval adapts to what it is reviewing. It does not judge a wireframe as though it were finished visual design or production code.

### How findings are prioritised

| Priority | Meaning |
| --- | --- |
| **Blocker** | The direction may fail, cause harm, break trust, or conflict with a critical constraint |
| **Important** | The issue is likely to create confusion, hesitation, unnecessary effort, or a weaker outcome |
| **Polish** | The central experience works, but craft or consistency can improve |
| **Open question** | Missing context prevents a confident judgment |

UX Eval does not produce a numerical score unless one is explicitly requested. A score is never treated as permission to ship.

Read more in [`ux-eval/README.md`](ux-eval/README.md).

---

## What you can provide

The skills can work with one or more of the following:

- A short product problem
- A design or research brief
- User research and behavioural information
- A product brief or PRD
- Screenshots
- Figma or FigJam context when the relevant integration is available
- A journey, flow, wireframe, visual design, or prototype
- An existing design-agent response
- Product, policy, technical, content, or operational constraints

You do not need to prepare every input before starting. The skills identify which missing information is important enough to ask about and which assumptions are safe to carry forward.

## What you receive

Depending on the request, Senior Designer may return:

- A clear understanding of the problem and context
- An editable user story
- A design-shaped problem statement
- Compared solution directions and a recommendation
- A map of what the user should understand at each stage
- A flow, journey, wireframe, screen direction, or interface content
- Assumptions, trade-offs, dependencies, and open questions

UX Eval may return:

- An overall assessment
- What is working and should be preserved
- Missing questions or unsupported assumptions
- A solution-quality assessment
- A stage-by-stage user-understanding review
- Artifact-appropriate findings
- Prioritised changes
- Questions that could change the evaluation
- A focused revision direction

---

## Installation

### 1. Download the repository

```bash
git clone https://github.com/Akshaymehta1mg/Design-skills.git
cd Design-skills
```

### 2. Install both skills

The installer defaults to the Claude Code skills directory:

```bash
python3 install.py
```

To install into another supported skills directory, provide the target explicitly:

```bash
python3 install.py --target /absolute/path/to/skills
```

For a project-scoped installation:

```bash
python3 install.py --target /absolute/path/to/project/.claude/skills
```

### 3. Verify the installation

```bash
python3 install.py --verify
```

When a custom target was used:

```bash
python3 install.py --verify --target /absolute/path/to/skills
```

### Install only one skill

```bash
python3 install.py senior-designer
python3 install.py ux-eval
```

### Update an existing installation

```bash
python3 install.py --force
```

The installer copies the selected skill folders and their references. Restart or begin a new AI session after installation so the environment can discover the updated skills.

---

## Repository structure

```text
Design-skills/
├── README.md
├── install.py
├── senior-designer/
│   ├── README.md
│   ├── SKILL.md
│   └── references/
│       ├── articulate-problem.md
│       ├── content-design.md
│       ├── figma-screen.md
│       ├── read-board.md
│       ├── read-prd.md
│       ├── research-plan.md
│       ├── research-script.md
│       ├── solution.md
│       ├── sticky-notes.md
│       ├── ui-review.md
│       ├── user-flow.md
│       ├── user-story.md
│       ├── user-understanding.md
│       └── wireframe.md
└── ux-eval/
    ├── README.md
    ├── SKILL.md
    └── references/
        ├── feedback-and-revision.md
        ├── map-user-understanding.md
        ├── review-the-artifact.md
        ├── review-the-solution.md
        └── understand-the-design.md
```

## Responsibilities and limits

These skills can evaluate coherence, completeness, clarity, hierarchy, interaction logic, and alignment with the context they receive.

They cannot confirm that:

- Assumptions about users are true
- Real users will behave as expected
- A design satisfies requirements that were not supplied
- Legal, policy, accessibility, engineering, business, or operational approval has been granted
- A design is ready to ship solely because it received a positive review

The skills make these limits visible so the user knows which decisions can continue and which require confirmation from another responsible person or team.
