# Feedback and Revision

Use this reference to turn the evaluation into a focused design conversation and to review subsequent revisions.

## 1. Prioritise findings

Assign one priority:

### Blocker

Use when the direction may:

- Fail to address the stated problem
- Cause material harm
- Remove necessary user understanding or control
- Break trust at a critical moment
- Conflict with a known policy, safety, privacy, legal, business, or technical constraint
- Make the primary task impossible or fundamentally misleading

### Important

Use when the issue is likely to:

- Create confusion or hesitation
- Make an important decision harder
- Add avoidable effort
- Hide a relevant consequence
- Weaken comprehension, recovery, or task completion
- Create a noticeable mismatch with the product context

### Polish

Use when the central experience remains sound but craft, consistency, readability, or presentation can improve.

### Open question

Use when missing context could materially change the judgment. Name the decision that depends on the answer.

Do not elevate every issue. If everything is a blocker, the prioritisation is not useful.

## 2. Support every finding

Write findings in this structure:

**Finding:** concise description  
**State:** observed, inferred, or not shown  
**Location:** stage, screen, surface, element, or decision  
**Why it matters:** effect on this user, task, or outcome  
**Revision direction:** what the designer should reconsider, without prescribing unnecessary visual detail  
**Confidence:** high, medium, or low, with a short reason when not high

Do not use generic directions such as “make it intuitive,” “simplify,” or “improve the hierarchy.” Name the decision that should change.

## 3. Balance the review

Identify what is working when it is relevant to decisions the designer should preserve. Avoid praise that merely softens criticism.

The review should make clear:

- What should remain
- What should change first
- What can wait
- What cannot be judged from the supplied material

## 4. Ask the designer only material questions

Ask when:

- The designer’s intent is unclear and affects the finding
- A constraint may explain an apparent weakness
- A supplied assumption needs confirmation
- Two plausible interpretations lead to different evaluations

Group related questions. Do not ask for information already present. Do not make the designer defend every minor choice.

After the designer replies, classify each affected finding as:

- **Kept** — the concern remains
- **Revised** — wording, confidence, or priority changed
- **Withdrawn** — new context resolves the concern
- **Accepted trade-off** — the cost is understood and deliberately retained

## 5. Default evaluation format

Use only the sections relevant to the request:

### Overall assessment

One sentence describing the strongest quality and the most important risk.

### What is working

Decisions that should be preserved.

### Understanding gaps

Important missed questions, unsupported assumptions, or user-story gaps.

### Solution assessment

How well the direction fits the supplied problem, user, product, and constraints.

### User-understanding map

Include when the work contains a staged experience.

### Prioritised findings

List blockers first, then important improvements, polish, and open questions. Avoid repeating the same concern in multiple sections.

### Questions for the designer

Only questions that could change the evaluation.

### Revision direction

Describe the order of changes and what success would look like in the next version.

### Limits of the review

Name claims requiring confirmation from users, domain specialists, leadership, legal, policy, accessibility, engineering, or another responsible reviewer.

## 6. Optional scoring

Do not score by default. If the user explicitly requests scoring:

- Score only dimensions supported by the artifact
- Mark unsupported dimensions as not applicable
- Explain the evidence behind each rating
- Keep critical risks separate from the numerical result
- Never translate a high score into permission to ship
- Describe the score as a comparison aid between revisions, not an objective measure of design quality

Possible dimensions include problem alignment, user-story coherence, solution fit, user understanding, flow clarity, and artifact craft. Do not include a dimension that cannot be evaluated from the supplied material.

## 7. Review a revision

Compare the updated work with the earlier findings. For each material change, mark:

- **Resolved** — the underlying concern is addressed
- **Partially resolved** — improvement is visible but the concern remains
- **Still open** — the relevant issue is unchanged
- **Accepted decision** — the designer intentionally retained a trade-off with sufficient reasoning
- **New concern** — the revision introduced another material issue

Check for effects elsewhere in the journey. A local fix may create a new hierarchy, consistency, control, or comprehension problem.

End with:

- What improved
- What remains most important
- Whether the work is ready for its next design or review stage
- What still requires confirmation outside the evaluation
