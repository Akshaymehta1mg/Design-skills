---
name: read-prd
description: Read a product brief or PRD and translate its relevant content into design understanding, constraints, implications, and open questions without taking ownership of the authoritative product requirements.
---

# Read a Product Brief or PRD

## Purpose

Use the product brief or PRD as an input to design work. Understand what product has decided, identify what those decisions mean for the experience, and surface gaps that prevent responsible design decisions.

Do not silently complete missing product strategy, business rules, policy, analytics, delivery, or engineering decisions. Return those gaps to the responsible owner as questions or explicit assumptions.

## 1. Read the complete document

Review the full document and any supplied supporting material before extracting requirements. Preserve the language and intent of confirmed decisions while separating them from proposals, assumptions, and unresolved questions.

Identify:

- The user and situation
- The problem being addressed
- The desired user outcome
- Product and business goals
- Non-goals and scope boundaries
- Existing user stories
- Functional behavior that affects the experience
- Platform and technical constraints
- Policy, legal, operational, content, and accessibility constraints
- Dependencies and ownership boundaries
- Success measures relevant to the experience
- Known risks
- Open questions

## 2. Classify what the document says

Mark important statements as:

- **Confirmed decision** — explicitly approved or stated as required
- **Constraint** — limits what the design or product may do
- **Proposal** — a direction under consideration, not yet final
- **Assumption** — treated as true without confirmation
- **Unknown** — information the document does not provide
- **Conflict** — two requirements or statements cannot both be satisfied as written

Do not turn a proposal or assumption into a requirement through confident wording.

## 3. Build the design understanding

Summarise the document from a design perspective:

- Who is affected and in what situation
- What progress the user is trying to make
- Where the current experience breaks down
- What outcome the product expects
- What is in scope and out of scope
- Which systems, teams, policies, and operations shape the journey
- What happens before, during, immediately after, and later

If the document contains several audiences, goals, or journeys, separate them before combining them into one design direction.

## 4. Translate requirements into design implications

For each requirement relevant to the experience, state:

1. What the requirement says
2. Which user, stage, or system it affects
3. What decision it creates for the experience
4. Which information, action, state, or recovery path may be required
5. What remains unclear

Focus on implications rather than screen prescriptions. A product requirement may affect the journey, product role, hierarchy, content, permissions, control, state handling, or hand-off without dictating a specific interface.

## 5. Review the user story

Check whether the supplied user story explains:

- The user’s starting situation
- The trigger for the journey
- The user’s goal and motivation
- The current obstacle or uncertainty
- The consequence of failure
- The successful end state

If the user story is missing, incomplete, or unsupported, use `user-story.md` to draft an editable design hypothesis. Do not present the draft as a confirmed product requirement.

## 6. Identify design-blocking gaps

Ask whether different plausible answers would change:

- The problem framing
- The user or journey in scope
- The product’s role
- Available information or system behavior
- User control, consent, safety, or reversibility
- The flow architecture
- Information hierarchy
- Content accuracy
- Required states and recovery

Only escalate gaps that materially affect the design. Carry lower-impact unknowns as named assumptions.

For each material gap, record:

- The unanswered question
- The design decision that depends on it
- The responsible owner
- Whether design can proceed with an assumption

## 7. Define the designer’s contribution

Senior Designer may contribute:

- Design understanding
- User-story clarification
- Journey and flow implications
- Experience principles
- Information and content requirements
- Interaction and state requirements
- Error, permission, empty, success, and recovery considerations
- Accessibility implications
- Design dependencies
- Questions for product, engineering, policy, legal, content, research, or operations
- A recommendation for the next design artifact

Senior Designer must not claim ownership of:

- Authoritative product strategy
- Business rules not supplied by product
- Revenue or commercial commitments
- Engineering architecture
- Delivery estimates
- Analytics ownership
- Launch approval
- Final product-wide acceptance criteria

## 8. When asked to write a PRD

Do not fabricate a complete authoritative PRD from design assumptions.

Offer a design contribution that product can incorporate, such as:

- UX intent
- User journey
- Flow and state behavior
- Interaction requirements
- Content requirements
- Accessibility considerations
- Design risks and dependencies
- Open product questions

Clearly label decisions that require confirmation from the product owner or another responsible function.

## Output

Return the smallest useful set of sections:

### Design understanding

The user, problem, outcome, scope, and journey as understood from the document.

### Confirmed design inputs

Decisions and constraints that the design can rely on.

### Design implications

How relevant requirements affect the journey, information, actions, states, control, content, and recovery.

### Gaps and conflicts

Material unknowns, assumptions, or contradictions and the decisions they affect.

### Questions by owner

Only questions whose answers could change the design.

### Recommended design response

The appropriate next design activity or artifact, without creating additional deliverables unless requested.

## Completion check

- The complete document was read before interpretation.
- Confirmed decisions are separated from proposals and assumptions.
- Product language was translated into design implications rather than copied into screens.
- Missing product decisions were not silently invented.
- User-story gaps are visible.
- Design-blocking questions name their owner and consequence.
- The output stays within design responsibility.
