# Rx Validation Revamp — No-Rx Path

> **Working assumption stated up front:** No Figma frames, screenshots, or board attached. This response is generated from the text brief only. The brief is unusually thorough — quantified failure modes (3.6% stall, 42.7% cancellation past 30 min) plus a qualitative frame ("ambush" calls) — so confidence is medium-high and I am proceeding to solutioning rather than proposing further research. Product context (online pharmacy, Rx-listed SKUs, doctor tele-consultation for validation) is inferred from the domain of the requesting user and standard pharmacy operating patterns; called out as assumptions below.

---

## Step 1 — Board Understanding

**What this appears to show**
A strategy brief for redesigning the prescription-validation flow on the "no-Rx path" — the checkout path where a user has ordered Rx-listed medicines without uploading a prescription. In that path, a doctor tele-consultation is triggered after checkout to validate the order before fulfilment.

**Likely user goal**
Get the medicine delivered. The user's mental model at this point is transactional ("I've placed my order"), not clinical ("I've booked a consultation").

**Flow or state shown (inferred)**
```
Cart → Address → Payment → Order Placed
                                 │
                                 ▼
                    [Silent] Doctor validation triggered
                                 │
                                 ▼
                    Outbound synchronous call from doctor
                                 │
              ┌──────────────────┼──────────────────┐
              ▼                  ▼                  ▼
        Call answered      Call missed         User waits
              │                  │                  │
         Approved →         "On hold"          >30 min → cancel
         fulfilment         (silent stall)      (42.7% spike)
```

**Important notes and annotations (from the brief)**
- 3.6% of all Rx orders stall silently after missed calls — no notification, no retry schedule shared with the user.
- Validation status is hard to find after the user leaves the order-success screen.
- 42.7% cancel when wait exceeds 30 minutes.
- The word "ambush" is a strong qualitative signal — users experience the doctor call as surprise, not as expected next step.

**Visible friction**
- Mismatch between user's mental model at "Order placed" (transaction closed) and the system's next move (medical consultation opening).
- No visible commitment device — user cannot schedule, confirm readiness, or see the doctor's queue.
- No retry loop the user controls — a missed call becomes a silent hold state.
- Status surface is buried — the tracking of an active, time-sensitive event is treated like a passive shipment tracker.

**Assumptions**
- No-Rx path exists because regulation (or policy) requires a licensed practitioner to sign off before Rx-listed SKUs ship.
- Doctors are 1mg-side (staff or contracted panel), not third-party — meaning capacity is a controllable variable, not a fixed external one.
- Mobile-first traffic; app has push, SMS, and (assumed) WhatsApp as available notification channels.
- Users often place these orders on behalf of a family member — "the patient" and "the buyer" may not be the same person.
- Payment is captured before validation completes (which is why cancellation involves refunds and is business-costly).

**Unclear points**
- What is causing the 30-minute wait? Doctor availability, queueing, batch dispatch of calls, or something else? The stance shifts if the wait is a capacity problem vs a UX problem.
- Regulatory ceiling: can validation be async (in-app chat + Rx image capture) or must it be a synchronous voice call?
- Is the doctor calling from a masked number the user doesn't recognise? If yes, ambush is worsened by unknown-caller ID.
- Does the SKU catalogue mix Rx and non-Rx items in one order? If yes, the "order placed" narrative for the non-Rx items complicates any full-order pause.

---

## Step 2 — Reflection

Here is what I think the brief is about: the moment after "Order Placed" is doing two contradictory jobs at once. For the user it closes a purchase. For the system it opens a medical consultation. The four failure modes named in the brief — ambush, silent stall, hidden status, wait-abandonment — are not independent bugs. They are four surface symptoms of one underlying mismatch. My work below is anchored on identifying that mismatch and fixing it at the source, not patching each symptom in isolation.

---

## Step 3 — Problem Articulation

**User**
An adult buying Rx-listed medicines online without uploading a prescription. Often mid-flow ("I need to reorder Mom's BP meds before her tablet runs out today"). Emotional state: pragmatic, transactional, mildly time-pressured. Experience level: familiar with e-commerce checkout; not familiar with tele-consultation as a step *inside* an e-commerce flow.

**User goal**
Receive the medicine, quickly and predictably. Minimise cognitive and time cost. Never do surprise work.

**Current friction**
The interface tells the user the order is placed, then silently hands them off to a doctor who calls unannounced. When the call is missed, the interface does not tell the user their order is now on hold, does not give a retry time, and does not offer a place to self-serve. If the user does find the status, it is buried and non-actionable. The 30-minute wait threshold — after which nearly half of users abandon — is invisible to the user in the moment, but is where the most business damage happens.

**Product goal**
Meet the regulatory requirement of practitioner sign-off while (a) preserving the sale that has already been captured, (b) reducing inbound support load, and (c) rebuilding trust in the post-order experience.

**Design challenge**
How might we convert the invisible, system-owned validation step into a visible, user-owned commitment — so that the doctor consultation is expected, participated in, and recoverable when things go wrong?

**Success looks like**
- Zero "ambush" surprise: the user knows before the "Order Placed" screen exists that a call is coming.
- Silent-stall rate collapses toward 0% — every miss triggers a self-serve recovery loop the user can complete in seconds.
- 30-minute cancellation spike flattens materially (target: halve it) because users have a scheduled window, not an open-ended wait.
- Support tickets tagged "where is my order / validation status" fall out of the top-N contact reasons.

**Assumptions**
- Validation must involve a licensed doctor (regulatory constraint we cannot design away).
- The doctor call can be initiated *inside* the app (VoIP), not only via the user's SIM.
- Users will accept a small increase in checkout length in exchange for predictability at the post-checkout stage.

### Reframe check (required)

**Form 1 — PM framing (as given by the brief).**
"Rx validation on the no-Rx path has four problems: ambush calls, silent stalls after missed calls, opaque post-order status, and a 42.7% cancellation spike past 30 minutes of wait. Fix the four."

**Form 2 — User-symptom restatement.**
"Users are startled when a doctor calls out of the blue after they thought their order was done. When they miss the call, their order gets stuck and they don't know it. They can't find their order status. If the wait drags past thirty minutes, they give up and cancel."

*True. Not useful — this only names the pain, not the design lever.*

**Form 3 — Design-shaped articulation.**
**The interface treats prescription validation as a system-owned background job the user waits on (the same pattern as payment processing or delivery dispatch) — when it is actually a user-owned appointment the user must participate in. The design lever is not more notifications, better copy, or a smarter tracker. It is converting an invisible wait into a visible commitment: moving the consultation earlier so the user schedules it, showing it as a booked appointment rather than a status badge, and treating a missed call as a rescheduling event, not a hold state.**

Everything downstream — where the consultation is inserted in the flow, what surface represents it, what words we use, how we handle miss and retry — is answered from Form 3, not from Form 1.

**Self-check.** Form 1 says "eliminate ambush, reduce stalls, improve visibility, optimise conversion". Form 3 says "the interface is picking the wrong metaphor for what this step actually is". These are meaningfully different. Form 3 does not assume the four PM bullets are four separate features to build — it identifies one root mismatch that, if fixed, causes the four symptoms to resolve together (or fall in priority).

---

## Step 4 — Clarification Decision

I can proceed with these assumptions. Confidence is medium-high, and the prompt explicitly discourages additional research or clarifying questions.

Stated assumptions I am proceeding on:
- Doctor consultation is a regulatory necessity, not an optional confirmation.
- The doctor call can be moved inside the app (VoIP or click-to-connect), not only PSTN.
- Order lines can include Rx and non-Rx SKUs; if so, non-Rx lines are eligible to dispatch independently.
- Adding a step inside checkout is acceptable if it visibly *saves* the user time at the post-checkout stage (which it does — moving unknown wait to known appointment).
- Doctor capacity is a variable the business can plan around, not a fixed external constraint.

What would change the recommendation:
- If validation must be truly synchronous voice with no VoIP path (SIM only) — Recover-heavy patterns get more weight.
- If regulation permits async validation (photo Rx + doctor review + async approval), the whole ambush category disappears and the design shifts to a lightweight asynchronous review with a callback only for exceptions.

---

## Step 5 — UX Recommendation

**Diagnosis**
The current design commits the user to a transaction ("Order Placed"), then quietly opens a second transaction (a medical consultation) inside the confirmation. The four named failure modes are consequences of that single misplaced commit boundary. Ambush is the moment the second transaction is revealed. Silent stall is what happens when the second transaction fails without a UI for it. Opaque status is the second transaction lacking a surface. The 30-min cancellation cliff is the emotional cost of an unbounded wait for something the user did not knowingly sign up for.

Attempting to fix each of the four symptoms independently (better notifications, better tracker, better retry) leaves the mismatch intact and produces a well-instrumented ambush rather than no ambush.

**Recommended direction**
Reframe validation from a background job to an appointment. Move the commit boundary *after* the consultation is scheduled, not before. Then design the surrounding surfaces (post-order, miss recovery, dispatch) around an appointment metaphor.

Three composed layers:

1. **Pre-commit — insert a "Doctor consultation" step before Payment.**
   New step after Address, before Payment: "This order needs a quick doctor consult (about 3 minutes) before we can dispatch. Choose a time." Options: **Now (call in ~30 seconds)** as default, or **Pick a slot in the next 2 hours**. "Order Placed" now means "your consultation is booked and paid" — an accurate promise.

2. **Post-commit — Consultation card is the primary post-order surface.**
   The confirmation screen shows the consultation card *above* the delivery card, with live states: `Scheduled 4:20 PM` → `Doctor prepping` → `Incoming in 30s (Answer in App)` → `In call` → `Approved` → `Dispatching`. Persistent chip in the app header until consult closes. Deep-linked from push and SMS.

3. **Miss / retry — a missed call is a rescheduling event, not a hold state.**
   If the user doesn't answer within 30 seconds, do not put the order on hold. Fire push + SMS + WhatsApp with a one-tap **"I'm ready now — reconnect"** that queues an immediate callback. Two consecutive misses offer an in-line reschedule (three slot chips), never a silent wait. The status card never says "on hold"; the words are always "Waiting for you" or "Reschedule".

Composition rule: the three layers are designed to reinforce, not duplicate. Layer 1 makes ambush structurally impossible (there is no unannounced call — the user booked it). Layer 2 makes status structurally locatable (it is the primary post-order surface, not a buried badge). Layer 3 makes stall structurally impossible (there is no path from "missed" to "silent hold" without the user's own action).

**Why this works**
It corrects the mental-model mismatch named in Form 3. Once the user knows they have a scheduled appointment, waiting, missing, and rescheduling become expected mechanics of an appointment — not surprise friction attached to a transaction. It also reduces load on the tracker surface: the tracker no longer has to communicate "there is a phone call about to happen you didn't expect", because the user already scheduled it.

**Key changes to make**

| Surface | Current | Proposed |
|---|---|---|
| Checkout | Cart → Address → Payment → Order Placed | Cart → Address → **Consultation slot** → Payment → Order Placed |
| Order Placed | "Order placed. Track your order." | "Consultation scheduled 4:20 PM. Delivery estimated 6:30 PM once approved." |
| Post-order surface | Shipment tracker (dominant) + Rx status (buried) | Consultation card (dominant, live) + shipment card (secondary, greyed until approval) |
| Doctor-call channel | Outbound PSTN from unknown number | In-app VoIP with "Answer" screen; PSTN as fallback only, from a recognisable branded caller ID |
| Missed call | Silent hold, no user-facing retry | Immediate multi-channel nudge with one-tap "Reconnect now" + inline reschedule |
| Copy for wait | "Rx Validation Pending" | "Consultation at 4:20 PM · in 8 min" |
| Copy for miss | "Order on hold" | "You missed Dr. Sharma. Ready to reconnect?" |
| Language everywhere | "Rx validation" (system-facing) | "Doctor consultation" (user-facing) |

**Copy recommendations**
- Replace "Rx Validation" with "Doctor consultation" across every user-visible surface. "Validation" is a compliance word; "consultation" is a service word. The service word matches what is actually happening for the user.
- On the scheduled state: countdown, not just timestamp. "Dr. Sharma will call in 8 minutes." A countdown is a commitment; a timestamp is a promise the user has to remember.
- Never use "on hold" for a missed call. That phrase teaches the user their order is stuck. Use "Waiting for you" — which locates responsibility correctly (mine, not theirs) and offers a clear next action.
- On the "Now" default in checkout, add expectation-setting: "Stay on this screen — the doctor will call in about 30 seconds." That five-word instruction converts the highest-drop-off possibility (user backgrounds the app) into a lightweight readiness cue.

**Edge states**

- *"Now" chosen, but the user is not actually available.* Ten-second countdown between choosing Now and the call, with a "Actually, schedule instead" escape hatch. Prevents the user from committing to Now under mild pressure and then missing.
- *No doctor free within the promised window.* Show queue position honestly ("You are 3rd in Dr. Sharma's queue, ~7 min wait") and expose a rebook control *before* the wait exceeds the 30-min danger threshold. Do not let the user drift into the cliff.
- *Doctor rejects the prescription.* Explicit next-step screen with three exits: "Upload a prescription now" / "Switch to a non-Rx alternative" / "Cancel & refund". Never leave the user in an unresolved rejected state.
- *Order has mixed Rx and non-Rx items.* Dispatch non-Rx lines immediately and communicate a split shipment. Do not hostage the whole cart to consultation status.
- *User loses connectivity mid-call.* Auto-resume within a 60-second window on reconnection; do not restart consult from scratch. Doctor sees a "user reconnecting" state, not a dropped call.
- *Second miss.* After two misses, the surface pivots from "Reconnect now" to "Pick a new time" — do not keep offering the same failing loop.
- *Buyer is not the patient.* Add an optional "Who is this for?" field in the consultation step; doctor sees it before the call. Reduces first-minute question time and lowers doctor-side capacity pressure.

**Tradeoffs**

- Adds one step to checkout. Real drop-off risk. Mitigations: "Now" is default and single-tap; the step is positioned as reducing wait, not adding it; the step doubles as a payment-anchor (paying after commit reduces refund exposure).
- Requires real capacity planning on the doctor side. Scheduled slots make staffing gaps visible in a way the current async-ambush model hides. This is uncomfortable but strictly better: currently, gaps are absorbed by a 42.7% cancellation rate.
- Engineering cost is real: in-app VoIP, scheduling primitive, live status card. Higher than adding badges to a tracker. Justified by the size of the cancellation-rate opportunity.
- Introducing "consultation" as user-facing language is a small brand shift. Word this carefully — this must not read as "this is now a tele-health product." It reads as "your order includes a quick doctor check."
- If regulation later permits async validation, some of Layer 1 becomes ceremony. The design should degrade gracefully: async approval slots in as a case where the "consultation" state simply resolves to Approved without a call, in seconds. No re-architecture needed.

**Next step**
Because the design introduces new states and new branches, the highest-value next artifact is a **user flow / state diagram** covering pre-commit → scheduled → incoming → in-call → post-call, plus miss/retry and reject/split loops. Wireframes for the consultation card and the miss-recovery moment come after that. See Step 6.

### Stance check (before finalising)

**Classification of the proposed interventions.**
- Layer 1 (consultation slot inside checkout) — **Prevent**. Removes the ambush moment entirely by making the consultation an expected, scheduled event before the user believes the transaction has closed.
- Layer 2 (consultation card as primary post-order surface, in-app VoIP) — **Assist**. Supports the user during the wait and the call itself.
- Layer 3 (multi-channel nudge + one-tap reconnect + inline reschedule) — **Recover**. Makes it cheap to fix a miss.

**1. Primary stance.**
Prevent. Specifically, prevent the mental-model mismatch by moving the commit boundary from "before the doctor call" to "after the doctor consultation is scheduled". The other two layers are supporting; they inherit their effectiveness from this shift.

**2. If I led with a different stance (Assist-first), the solution would look like this.**
Keep checkout unchanged. User taps "Place Order" and lands on a substantially richer confirmation screen. Under the delivery ETA, a "Prescription review" card materialises with a live status feed: doctor's name and photo, position in queue ("Dr. Sharma is with 2 patients before you"), a live ETA, and a bright "Call me now" CTA once the doctor is ready. A persistent status chip carries the same information across every app screen, so the tracker is never more than one tap away. Push notifications escalate through readiness → incoming → in-progress. On missed calls, an aggressive nudge stack (in-app banner + push + SMS + WhatsApp) with a "Tap to resume" one-tap reconnect kicks in within 30 seconds; two misses opens an inline three-slot reschedule. The doctor call comes in through the app (VoIP) with fallback to PSTN from a branded caller ID the user is primed to recognise. Order status is elevated to a top-level tab. In effect: validation still happens after checkout, still surprises the user briefly at first contact, but so much support scaffolding surrounds the moment that the surprise is neutralised in most cases.

This is a coherent, shippable, less-invasive alternative. It changes zero engineering primitives in checkout, only enriches post-order. It probably reduces the 3.6% stall figure meaningfully. It is genuinely competitive with the Prevent-first version on a scoped, near-term basis.

**3. Given the constraints, is Prevent the right primary stance? Why not the other two?**

Yes, Prevent is right — and here is why not Assist-first and not Recover-first.

*Not Assist-first.* Even a beautifully scaffolded post-order tracker cannot fix the fact that the user made an order commitment for a delivery and the system quietly opened a medical appointment. Every notification, every status chip, every "Dr. Sharma calling now" banner is downstream of a user who did not knowingly agree to a call. The 3.6% silent-stall rate is fixable by Assist mechanics — that is largely a communication problem. But the 42.7% cancellation cliff past 30 minutes is not a communication problem. It is an expectations problem: users cancel because they are waiting for something they never signed up for, and the wait becomes unreasonable in retrospect. Assist-first treats the symptoms well and the root cause weakly.

*Not Recover-first.* Recovery only fires after a failure. Better retry loops and multi-channel nudges could reduce stall rates significantly, but they do nothing for a user who waits 32 minutes and cancels before any miss occurs. Recovery is a floor, not a ceiling — it lifts the worst cases without shifting the median experience. As a primary stance it leaves the biggest business number (the cancellation cliff) untouched.

*Prevent as the primary is uniquely load-bearing.* Once the user has scheduled the consult, Assist and Recover become efficient rather than compensatory. A tracker (Assist) reinforces an expectation the user already holds; a reconnect flow (Recover) reschedules an appointment the user knows they have. In the Prevent-first architecture, the other two layers are amplifiers. In the Assist-first architecture, they are levees.

---

## Step 6 — Artifact Decision

**Selected artifact**
None to produce right now — the user did not request a specific artifact. Per the "no specific artifact" branch of the router: deliver the UX solution in text (above) and recommend the most useful next artifact.

**Recommended next artifact: user-flow / state diagram**

*Reason.* The proposed design introduces multiple new states (scheduled, prepping, incoming, in-call, approved, needs-info, rejected) with meaningful branching (miss × 1, miss × 2, split shipment, reconnect, reschedule, out-of-network mid-call). The design is state-heavy before it is screen-heavy. A user flow is the artifact that will surface most of the remaining unknowns cheaply — capacity assumptions, dispatch triggers, notification timing — and lock the model before any high-fidelity screens are committed.

**Subskill to call**
`references/user-flow.md` (state-diagram form, not linear task flow — the branching is the point)

**Second-priority artifact: content-design pass**

The proposed reframe leans heavily on copy: "consultation" not "validation", "Waiting for you" not "on hold", countdowns not timestamps, "Reconnect now" not "Retry". Once the flow is locked, a copy pass across every state string is the highest-leverage next move. Route to `references/content-design.md`.

**Third-priority: wireframe of the two most load-bearing screens.**
- The new consultation step inside checkout (with Now / Schedule).
- The post-order consultation card in its five live states.
Route to `references/wireframe.md`.

---

## Final Check

- Explained the board? Yes — flagged that no board exists and worked from the brief.
- Articulated the actual UX problem? Yes — Form 3 names the mismatch (system-owned wait vs user-owned appointment).
- Asked only necessary questions? Zero questions asked; assumptions stated instead, per prompt constraint.
- Routed correctly? No artifact requested → routed to the "no specific artifact" branch and recommended user-flow as the highest-value next step.
- Produced the requested artifact? User did not request one; recommendation delivered.
- Separated facts from assumptions? Yes — assumptions explicitly labelled in each section.
