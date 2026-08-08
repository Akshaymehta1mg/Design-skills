# Review the Artifact

Select only the sections that match the review object and its maturity. An artifact may require more than one section, but never run checks simply because they exist.

## Shared assessment states

Use these states consistently:

- **Observed:** directly visible in the supplied material
- **Inferred:** a reasonable interpretation that is not explicitly shown
- **Not shown:** the material does not provide enough information
- **Not applicable:** outside the artifact’s purpose or maturity

“Not shown” is not automatically a design failure. State whether the missing information prevents evaluation or should be added to communicate intent.

## Problem framing

Review:

- Clear user and situation
- Specific difficulty rather than a broad topic
- Consequence of the current experience
- Desired change for the user and product
- Separation of supplied facts and assumptions
- A design opportunity that is open enough to explore but specific enough to act on

Do not require interface details.

## User story

Review:

- Believable starting situation
- Trigger for the journey
- User goal and motivation
- Obstacle, hesitation, or unmet need
- Successful end state
- Support from the supplied context
- Coherence with the proposed solution

Do not treat a persona profile as a user story unless it explains behaviour over time.

## Concept or solution direction

Review:

- Clear central idea
- Connection to the underlying difficulty
- Appropriate product role
- User value and product value
- Scope and boundaries
- Control, trust, reversibility, and consequences
- Before, during, and after experience
- Important feasibility assumptions

Do not require detailed screen states unless the concept claims to resolve them.

## User flow or journey

Review:

- Believable entry points
- Clear sequence and stage purpose
- Necessary decisions in a sensible order
- Branches based on meaningful differences
- Back, edit, cancel, exit, and resume behaviour
- Error and recovery paths appropriate to the task
- Clear completion and next state
- Connections to surrounding product journeys
- Unnecessary steps or repeated user work

Do not review final visual styling.

## Wireframe

Review:

- One clear job for each screen or surface
- Information needed for the current stage
- Strong information and action hierarchy
- One evident primary action where appropriate
- Clear labels and sufficiently realistic content to judge comprehension
- Appropriate page, overlay, sheet, inline, and dialog choices
- Consistent navigation and context retention
- Relevant empty, error, loading, success, permission, and recovery intentions
- Data the system should reuse rather than request again
- Unnecessary screens, controls, or explanations

Do not review final colour, type styling, illustration, motion polish, or production implementation. Accessibility may be assessed only where structural intent is visible, such as reading order, language clarity, focus order annotations, and target placement.

## Visual design

Review:

- Attention and information hierarchy
- Typography and readability
- Colour contrast and semantic use
- Spacing, alignment, grouping, and density
- Component and interaction consistency
- Icon and control clarity
- States and feedback represented in the design
- Design-system reuse or justified departures
- Brand fit when guidance is supplied
- Accessibility visible at the design level

Do not assume interaction behaviour that is not shown or annotated.

## Functional prototype

Review:

- Interaction predictability
- Transition clarity and context continuity
- Feedback after actions
- Validation, error, loading, empty, and success behaviour represented by the prototype
- Keyboard and focus behaviour when the prototype supports assessment
- Cancel, back, edit, undo, retry, and recovery behaviour
- Realistic content and data changes
- Whether motion supports understanding

Mark unimplemented branches as “not shown” unless the prototype’s stated scope requires them.

## Implemented experience

Review relevant design behaviour in the working product:

- End-to-end task completion
- Responsive behaviour within the stated platform scope
- Keyboard, screen-reader, focus, zoom, contrast, target-size, and motion accessibility
- Input validation and error recovery
- Loading, empty, offline, timeout, permission, and failure states
- Data persistence and protection against accidental loss where relevant
- Destructive-action protection through confirmation, undo, or another appropriate mechanism
- Performance feedback and perceived responsiveness
- Content consistency and live data behaviour
- Privacy and data-use communication where relevant

Do not claim comprehensive compliance from a limited inspection. Name what was and was not assessed.

## Cross-artifact consistency

When several artifacts describe one experience, check whether:

- The user story, flow, wireframe, and implementation describe the same journey
- Important states survive as fidelity increases
- Labels and product concepts remain stable
- Later artifacts introduce unexamined decisions
- Constraints or trade-offs are lost between stages

## Output for this review layer

Return only findings relevant to the artifact reviewed. For each finding, include its assessment state, location, user impact, priority, and revision direction.
