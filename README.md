# Design Skills for AI-Assisted Product Design

Two skills that turn an LLM into a senior product designer and a rigorous UX evaluator. Built for Claude Code, adaptable to other AI coding/design tools.

## What's in the box

### senior-designer

An orchestrator skill that reads messy design context — Figma frames, screenshots, prompts, research briefs, `.md` files — and works through it the way a senior product designer would: understand first, articulate the problem, then solve.

It doesn't jump to UI suggestions. It reframes the problem, considers multiple solution directions (Prevent / Assist / Recover), picks a stance, and only then routes to the right artifact.

### ux-eval (Agent Evil)

An 8-gate UX evaluation framework that scores design outputs on solution quality, subtraction, consistency, fundamentals, and philosophy. Three gates (Problem, Innovation, Gut Check) are flagged for human review — the agent knows what it can't judge.

Produces a scored report card with binary pass/fail checks, rated factors (1-5), and actionable fix directions for every failure.

---

## What you can feed it (inputs)

The senior-designer skill accepts any mix of:

| Input type | Examples |
|---|---|
| **Text prompt** | A problem statement, design brief, or "how should we handle X?" question |
| **Figma link** | Any Figma or FigJam frame (requires Figma MCP server connected) |
| **Screenshot** | A photo or screenshot of an existing screen, flow, or whiteboard |
| **Markdown file** | A `.md` with research findings, PRD, or product context |
| **Research data** | User quotes, survey results, analytics numbers pasted into the prompt |
| **Existing design output** | A previous solution you want critiqued or iterated on |

You don't need all of these. A single sentence describing a UX problem is enough to start.

### Example prompts

**Problem-solving:**
> Users search "urine" on our diagnostics app and get 7 near-identical tests. Traffic is doctor-initiated — users have a prescription but can't map the shorthand to the right SKU. Help them pick the right test.

**Screen critique:**
> Critique this PDP: header with test name, "82,900 booked recently", two info boxes, price with strikethrough, orange BOOK button, then an offers strip. What's working and what would you change first?

**Artifact request:**
> Write the copy for when a booked home-collection slot gets cancelled by the lab (not the user's fault). User has already paid. Don't panic them, tell them what's next, offer reschedule.

**Evaluation:**
> Run a UX eval on the solution above.

---

## What you get back (outputs)

### From senior-designer

1. **Board understanding** — what the context shows, who the user is, what flow or state is implied
2. **Problem articulation** — user problem, business problem, friction diagnosis, success criteria
3. **Reframe check** — the problem stated in three forms: PM framing, user symptom, and a design-shaped articulation that names the specific mismatch the design must resolve
4. **UX solution** — diagnosis, recommended direction, copy suggestions, edge cases, tradeoffs
5. **Stance check** — each intervention classified as Prevent / Assist / Recover, with the primary named and alternatives sketched
6. **Routed artifact** (when requested) — one of:

| Artifact | When to ask |
|---|---|
| Wireframe | "wireframe this", "sketch the layout" |
| User flow | "map the flow", "show the journey" |
| PRD | "write a PRD", "product spec" |
| Research plan | "plan the research", "what should we test" |
| Interview script | "write a usability script" |
| UI review | "critique this screen", "UX audit" |
| Content design | "write the copy", "microcopy for this state" |
| Figma screen | "high-fidelity screen" |
| Sticky notes | "synthesize these notes" |

### From ux-eval

A scored report card across 8 gates:

| Gate | What it checks | Scored? |
|---|---|---|
| 0. Artifact Stage | Static mockup / prototype / shipping code | Sets N/A rules |
| 1. The Problem | Problem-solution alignment | Human review |
| 2. The Solution | Framing, efficiency, error tolerance, learnability | Yes (/24) |
| 3. Subtract | Word economy, auto-fill opportunities, unnecessary steps | Yes (/18) |
| 4. Consistency | Terminology, interaction patterns, navigation | Yes (/28) |
| 5. Fundamentals | Accessibility, visual hierarchy, responsiveness | Yes (/33) |
| 6. Philosophy | Trust, credibility, privacy | Yes (/6) |
| 7. Innovation | Multiple directions explored? Fresh but appropriate? | Human review |
| 8. Gut Check | Does something feel off that the checklist missed? | Human review |

Overall score out of 109 (adjusted for N/A checks), with a letter grade (A-F) and actionable fix directions for every failure.

---

## Installation

### Claude Code (recommended)

**Option 1: Run the installer**

```bash
git clone https://github.com/Akshaymehta1mg/Design-skills.git
cd Design-skills
python3 install.py
```

This copies both skills into `~/.claude/skills/`. Start a new Claude Code session and describe a design problem — the skill activates automatically.

**Option 2: Project-scoped install**

If you want the skills available only inside a specific project:

```bash
cd your-project
python3 /path/to/Design-skills/install.py --target ./.claude/skills
```

**Other commands:**

```bash
python3 install.py --verify          # check your install
python3 install.py --dry-run         # preview without copying
python3 install.py senior-designer   # install just one skill
python3 install.py --force           # overwrite existing install
python3 install.py --uninstall       # remove installed skills
```

**After installing:**

1. Start a new Claude Code session (or restart your current one).
2. No slash command needed. Just describe a design problem, paste a Figma link, or ask for a UX audit.
3. The skill triggers automatically based on your prompt.

---

### OpenAI Codex / ChatGPT

These skills were built for Claude Code's skill system, but the core logic is plain Markdown and works in any LLM that accepts system instructions.

**For ChatGPT (Custom GPT):**

1. Go to [chat.openai.com](https://chat.openai.com) > Explore GPTs > Create.
2. In the **Instructions** field, paste the contents of `senior-designer/SKILL.md`.
3. Under **Knowledge**, upload all files from `senior-designer/references/` as individual files.
4. For the evaluator, create a second Custom GPT with `ux-eval/SKILL.md` as instructions.
5. Name it, set a description, and save.

**For ChatGPT (project-level custom instructions):**

1. Open a ChatGPT project.
2. Go to Project Settings > Instructions.
3. Paste the contents of `senior-designer/SKILL.md`.
4. In the same project, upload the reference files so the model can access them when needed.

**For OpenAI Codex:**

1. In your Codex workspace, open the system prompt / agent instructions.
2. Paste `senior-designer/SKILL.md` as the base instructions.
3. Append the contents of the most relevant reference files (at minimum: `references/articulate-problem.md` and `references/solution.md`).
4. For the evaluator, use `ux-eval/SKILL.md` as the system prompt for a separate agent.

**For Cursor / Windsurf / other AI code editors:**

1. Copy the skill folder into your project's AI instructions directory (varies by editor):
   - Cursor: `.cursor/rules/` or project-level instructions
   - Windsurf: `.windsurfrules` or workspace settings
2. Or paste `SKILL.md` contents into the editor's custom instructions / system prompt field.

> **Note:** On non-Claude platforms, the `references/` routing (where the orchestrator calls specialist files on demand) won't work automatically. You'll need to either (a) paste the relevant reference file contents into the conversation when you need a specific artifact, or (b) include the key reference files in the system prompt / knowledge base upfront. The core reasoning — reframe check, stance check, problem articulation — works in any LLM.

---

## File structure

```
Design-skills/
  install.py                        # installer script
  README.md                         # this file
  senior-designer/
    SKILL.md                        # orchestrator (284 lines)
    references/
      articulate-problem.md         # problem framing + reframe check
      solution.md                   # UX solution + stance check
      clarify-context.md            # confidence-based question logic
      artifact-router.md            # routes to the right output type
      wireframe.md                  # wireframe generation
      user-flow.md                  # flow / journey mapping
      prd.md                        # PRD from design context
      research-plan.md              # research planning
      research-script.md            # interview / usability scripts
      ui-review.md                  # screen critique / UX audit
      content-design.md             # microcopy and content
      figma-screen.md               # high-fidelity screen specs
      sticky-notes.md               # sticky-note synthesis
      read-board.md                 # input interpretation
    evals/                          # test prompts and scored runs (not installed)
  ux-eval/
    SKILL.md                        # the full 8-gate evaluation framework
```

---

## How the skills work together

The intended workflow is:

1. **You describe a design problem** to Claude Code (or another LLM with the skill installed).
2. **senior-designer activates** — reads your input, articulates the problem (with a reframe check), considers multiple solution directions, picks a stance, and produces a solution + the artifact you need.
3. **You ask for an eval** — ux-eval (Agent Evil) takes the output from step 2 and scores it across 8 gates, producing a report card with a grade, failures, and fix directions.
4. **You iterate** — fix what the eval flagged, rerun, compare scores.

The eval is optional but useful. It catches things humans skip under deadline pressure: terminology drift, missing error states, over-explained empty states, inconsistent interaction patterns.

---

## Requirements

- Python 3.7+ (for `install.py`)
- Claude Code, ChatGPT, Codex, Cursor, or any LLM tool that accepts custom instructions
- No external dependencies — the installer uses only Python standard library
