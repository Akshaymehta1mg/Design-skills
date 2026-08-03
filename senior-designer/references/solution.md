---
name: solution
description: Use this to generate the UX recommendation after the problem has been articulated. This is where you actually solve it.
---

# Design the Solution

## What this step is for

You've named the problem. Now solve it. Walk through this the way you'd present in a design crit — diagnosis first, then your recommendation, then why, then the details.

## How to think through it

1. **What's broken and why?**
   - What specific thing isn't working?
   - Why is it failing? (Not "it's confusing" — *why* is it confusing?)
   - What does the user do (or not do) as a result?

2. **Pick a direction:**
   - Simplify it
   - Reorder it
   - Clarify it
   - Add guidance
   - Remove friction
   - Change the hierarchy
   - Split the flow
   - Add feedback states
   - Build trust
   - Make recovery cheaper

3. **Design the recommendation:**
   - What screens or flows change?
   - What copy changes?
   - What interactions change?
   - What states change (loading, error, empty, success)?
   - Does the information architecture shift?
   - Does the visual hierarchy need to change?

4. **Be honest about the tradeoffs:**
   - How hard is this to build?
   - Does it introduce a learning curve?
   - What's the business impact?
   - Does it affect accessibility?
   - What are the edge cases?
   - Does it break consistency with the rest of the product?

5. **What's the next step?**
   - Test it with users
   - Wireframe it
   - Build a Figma screen
   - Write a PRD
   - Turn it into a research plan
   - Add notes to the board

## What the output looks like

```markdown
## UX Recommendation

**What's broken**
...

**What I'd do**
...

**Why this works**
...

**What changes**
- ...

**Edge cases to handle**
- ...

**Tradeoffs**
- ...

**Next step**
...
```

## Ground rules

- Be opinionated. Say what you'd actually do, not "there are several options." But explain your reasoning.
- Tie every recommendation back to the problem you named. If it doesn't connect, it's decoration.
- Include copy recommendations when the words are part of the friction. They usually are.
- "Make it cleaner" is not a recommendation. Say *how*.

## Stance check (do this before you're done)

This is the step most designers skip, and it's where the best work happens. It's easy to commit to one approach without realising you had a choice. This check forces you to see the choice.

Look at every intervention you proposed and classify it by where it sits in the user's journey:

- **Prevent** — removes the friction entirely. The user never hits the problem. (e.g., let them upload a prescription so they never see the confusing search results.)
- **Assist** — helps the user at the friction point. They still encounter it, but the interface supports them through it. (e.g., richer cards and a disambiguation strip on the search page.)
- **Recover** — makes it cheap to fix a mistake. The user went wrong, but getting back on track is easy. (e.g., a "not the right test?" rescue link on the detail page.)

Now answer three questions:

1. **Which stance is the primary one in your solution?** Pick one. "All three equally" is a dodge — every solution has a centre of gravity.
2. **If you led with a different stance, what would the solution look like?** Actually sketch it in a paragraph. Not "we could also prevent it" — describe what the Prevent-first version looks like, concretely. Then do the same for the third stance.
3. **Given the constraints, is your primary stance the right one?** If yes, explain why the other two aren't the lead. If you're not sure, that's worth saying.

If you can't answer question 2 with a genuinely different alternative, the divergent thinking didn't happen — you defaulted to one approach without exploring. Go back and try.

This isn't a formality. When a solution feels obvious, it's usually because one stance took over your thinking without you noticing. Making the alternatives explicit is how you catch that.
