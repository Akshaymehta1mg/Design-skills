# UX Eval — Rx Validation Revamp (No-Rx Path)

Agent Evil, walking gates 0 → 8 against the framework in `ux-eval/SKILL.md`, evaluating `output.md` in this same folder.

---

## GATE 0 — Artifact stage

**Declared stage:** Static mockup (best-fit; the artifact is a text design brief plus a copy-pair table and a state list, with no visual layout). N/A logic applied generously per parent instruction.

**Guiding rule applied:** Score the design intent expressed in the brief, not the fidelity of the artifact. Every check tagged `(N/A if static mockup)`, `(N/A if not shipping code)`, or otherwise untestable at the brief stage is removed from the denominator; it is never scored as 0.

---

## GATE 1 — The Problem (Human review)

**Agent 1 stated:** "The interface treats prescription validation as a system-owned background job the user waits on (the same pattern as payment processing or delivery dispatch) — when it is actually a user-owned appointment the user must participate in."

**Context (parent-provided) states:** 1mg no-Rx checkout path; four failure modes named in the brief — ambush calls, 3.6% silent stall, hidden validation status, 42.7% cancellation past 30 minutes; existing design system should be preserved unless a change is justified.

**Alignment:** Match, and stronger than the brief asked for. Agent 1 collapsed four failure symptoms into one root mismatch — a reframe, not a restatement.

**Status:** NEEDS HUMAN REVIEW — a human must validate whether the appointment metaphor is the right root frame for Indian pharmacy users (vs. an "approval" metaphor closer to how loans or KYC feel), and whether shifting the commit boundary before Payment is acceptable to the business given checkout drop-off risk.

---

## GATE 2 — The Solution

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 2.1 | Auto-save / data loss prevention? | **N/A** | — | The design authors no user-generated content (except an optional "Who is this for?" field). N/A per Gate 0. |
| 2.2 | Confirmation before irreversible actions? | **Yes** | 1/1 | Two explicit examples: 10-second countdown with an "Actually, schedule instead" escape hatch before the Now call commits, and the doctor-rejection screen with three named exits ("Upload a prescription now" / "Switch to a non-Rx alternative" / "Cancel & refund"). Reversibility is designed at both the commit and the rejection edges. |
| 2.3 | Progressive disclosure? | **Yes** | 1/1 | Consultation card dominates only while the consult is live; delivery card is greyed until approval; the inline reschedule (three slot chips) appears only after two misses, not on the first. Advanced states surface on demand. |
| 2.4 | Error messages present for all form fields and actions? | **No** | 0/1 | Edge-case coverage is strong (rejection, missed call, double miss, connectivity loss, mixed cart, buyer≠patient) but **mainline** error states are unspec'd: no state for "checkout network loss while picking a slot"; no state for "no slots available in the next 2 hours"; no state for the race where payment succeeds but the scheduled slot expires; no state for "consultation VoIP fails, PSTN fallback also unavailable". **Direction:** Spec a one-line inline state for each of those four gaps in the copy table before wireframing — they are on the mainline, not in edges. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 2.5 | Error message clarity | **4/5** | "You missed Dr. Sharma. Ready to reconnect?" (names the person, locates responsibility, offers one action). "Waiting for you" (says who owns the next move, in three words). Rejection screen names three concrete exits rather than dumping the user in an unresolved rejected state. Clear, specific, actionable. Loses one point because "Approved" is a system-language state label the user sees — it explains what happened but reads as compliance, not service. **Direction:** rewrite "Approved" to "Ready to dispatch" in user-facing state chips. |
| 2.6 | Step efficiency | **4/5** | Best-case flow: Cart → Address → **Consultation slot (Now default, 1 tap)** → Payment → Order Placed → Answer in App → Approved = 6 taps for a compliance-gated purchase. That is tight. One removable step candidate: the Consultation slot step could nest under Payment as a single "Consultation + payment" screen with the slot picker collapsed to a chip row above the pay button, saving one distinct step. Tight, one step could merge. |
| 2.7 | Onboarding weight | **4/5** | No onboarding is proposed; the design teaches by doing. The five-word instruction ("Stay on this screen — the doctor will call in about 30 seconds") is a minimum-viable readiness cue that would otherwise require a splash screen. Light, invisible, effective. |
| 2.8 | **Framing reframe quality** | **5/5** | Form 3 is textbook. "The interface treats prescription validation as a system-owned background job the user waits on … when it is actually a user-owned appointment the user must participate in" is precisely the shape *"the interface is treating X (validation) like Y (background job), when the user is doing Z (an appointment)"*. It names the specific mismatch, points to concrete design levers (commit-boundary placement, appointment metaphor, miss-as-reschedule not miss-as-hold), and every downstream decision — Layer 1's consultation slot, Layer 2's card dominance, Layer 3's reconnect flow — reads as an *answer* to Form 3, not to Form 1's four-bullet PM brief. Self-check is honest ("Form 1 says 'fix four things', Form 3 says 'the metaphor is wrong'"). Agent 1's Form 2 restatement is correctly labelled "True. Not useful" — the designer recognised the trap and moved past it. |

**Textual (no score):**
- Steps for the primary task: 6 taps in best case (Cart → Address → Slot → Payment → Answer → done).
- Merge candidate: Slot + Payment could live on one screen with the slot as a chip row above the pay CTA.
- **Flag for human:** Will Indian pharmacy users accept a scheduling step inside checkout, or read it as friction? Needs live testing.
- **Flag for human:** Is "consultation" the right user-facing word, or does it inflate expectations (users may expect real medical advice, not a compliance check)? Tonal judgment.

**Gate 2 score: 19 / 23** (1 N/A)

---

## GATE 3 — Subtract

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 3.1 | Can any two adjacent steps be merged? | **Yes** | 1/1 | The design *demonstrably* subtracts elsewhere: missed-call + hold + retry collapse into one "Reconnect now" tap; multi-channel nudge (push + SMS + WhatsApp) deep-links to one destination; consultation and delivery statuses live on one screen. The design adds a checkout step deliberately to save time later; that trade is examined and justified. Nothing removable is left. |
| 3.2 | Is the user doing work the system could auto-fill? | **Yes** | 1/1 | "Now" is single-tap default; countdown ("in 8 min") is derived not entered; auto-resume within 60s of connectivity loss (no manual re-dial); doctor name and identity are prefilled ("Dr. Sharma"), not user-typed. The optional "Who is this for?" field is the only additional manual input, and it is explicitly optional with a stated benefit (doctor sees it, faster call). |
| 3.3 | Empty states that over-explain? | **N/A** | — | No empty state is designed in the brief. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 3.4 | Copy conciseness | **4/5** | Tight: "Waiting for you" (3 words), "Reconnect now" (2), "Consultation at 4:20 PM · in 8 min" (7), "You missed Dr. Sharma. Ready to reconnect?" (7). The one long string is the checkout-step body: "This order needs a quick doctor consult (about 3 minutes) before we can dispatch. Choose a time." (16 words, could be 9). **Direction:** rewrite to "One quick doctor call before we ship — about 3 minutes. Pick a time." |
| 3.5 | Label efficiency | **4/5** | Verb-first, specific: "Reconnect now", "Pick a new time", "Answer in App", "Now", "Pick a slot in the next 2 hours". Small nit: "Actually, schedule instead" (escape-hatch label) has three words where "Schedule instead" (two) would land the same. |
| 3.6 | Jargon score | **5/5** | The whole recommendation is anchored on replacing "Rx validation" (compliance word) with "Doctor consultation" (service word). "Waiting for you" not "on hold". Countdown ("in 8 min") not medical timestamp. "You missed Dr. Sharma" — plain. A non-clinical user reads every word. Deliberate. |

**Textual — copy that could be shorter (before → after):**

- "This order needs a quick doctor consult (about 3 minutes) before we can dispatch. Choose a time." → "One quick doctor call before we ship — about 3 minutes. Pick a time."
- "Actually, schedule instead" → "Schedule instead"
- "Stay on this screen — the doctor will call in about 30 seconds." → keep as-is; already tight and load-bearing.
- "Consultation scheduled 4:20 PM. Delivery estimated 6:30 PM once approved." → "Doctor call at 4:20 PM · Delivery ~6:30 PM after the call."
- State label "Approved" → "Ready to dispatch" (removes compliance register from a user-facing chip).
- State label "Dispatching" → "On its way" (matches the user's mental model at that moment).

**Textual — inputs that could be auto-filled:**
- User's most recent successful doctor consult slot (if any) → pre-select as the suggested "Pick a slot" default.
- Buyer's saved emergency contact number → prefill for PSTN fallback.
- "Who is this for?" → pre-populate from address book selection ("Delivery for: Mom") if the delivery address contact name differs from the account holder.

**Flag for human:**
- Does every state in the five-state chip belong? Prepping → Incoming → In call → Approved → Dispatching — could Prepping and Incoming collapse into one for the user? Needs product taste.
- Does the "Buyer is not the patient" field belong in the consultation step or in Cart? Ordering call.

**Gate 3 score: 15 / 17** (1 N/A)

---

## GATE 4 — Consistency

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 4.1 | System state always visible? | **Yes** | 1/1 | Persistent header chip carries state ("Consultation at 4:20 PM · in 8 min" through "In call" through "Approved") across every app screen until consult closes. Five named states with clear transitions. Position is knowable at any moment. |
| 4.2 | Feedback visible after every interaction? | **Yes** | 1/1 | Slot tap → Payment; Now tap → 10-second countdown; Answer in App → In call state; Reconnect now → immediate callback queued; Reschedule → three chips. Every tap has a described consequence. |
| 4.3 | Similar components behave the same way? | **Yes** | 1/1 | The consultation card behaves identically on the order-placed screen and on the persistent header chip (deep-linked from push, SMS, WhatsApp). Bottom-sheet reschedule follows standard app patterns. No contradictory behaviours documented. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 4.4 | Terminology consistency | **3/5** | Consistent on the big move ("Rx validation" → "Doctor consultation" applied across the copy table). Two real drifts: (a) "doctor consult" (short) appears once inside the checkout step body while everywhere else uses "consultation" — pick one; (b) "Approved" is a system-word state label that leaks into user-facing state chips, competing with "Ready" language used elsewhere (Layer 2's "Answer in App"). Also, the label vocabulary for the reconnect action is not fully locked: the prose says "one-tap 'I'm ready now — reconnect'" and the table says "one-tap 'Reconnect now'" and copy row says "Ready to reconnect?" — three subtly different verbs/phrasings for one action. **Direction:** freeze one label per concept: "consultation" (never "consult"); "Ready to dispatch" (never "Approved"); "Reconnect now" (the button label — everywhere). |
| 4.5 | Interaction pattern consistency | **4/5** | Standard patterns throughout: chip picker for slot, bottom sheet for reschedule, one-tap deep link from every notification channel to the consultation card, VoIP with PSTN fallback (single call-behaviour promise). One thing left un-specified: the persistent header chip's tap behaviour (does it always open the consultation card, or is behaviour state-dependent?). Small predictability gap. |
| 4.6 | Label specificity | **4/5** | "Reconnect now" beats generic "Retry"; "Pick a new time" beats generic "Reschedule"; "Answer in App" beats generic "Answer"; slot chip "Now (call in ~30 seconds)" spells out the promise. Nit: "Consultation" alone is generic — always pair with a modifier ("Doctor consultation", "Consultation at 4:20 PM"). |
| 4.7 | Error tone consistency | **4/5** | Every miss- and problem-state string is factual, person-specific, and locates responsibility gently: "You missed Dr. Sharma. Ready to reconnect?" / "Waiting for you" / "You are 3rd in Dr. Sharma's queue, ~7 min wait". Same voice across all three. Rejection screen sticks to the voice with three explicit exits. Would tighten to 5 with an explicit tone-of-voice guide on the doctor-rejection copy (which currently exists only as slot names, not full strings). |
| 4.8 | Navigation predictability | **3/5** | The design *deliberately* introduces two new patterns to the 1mg checkout: (a) a scheduling step inside checkout — new for a pharmacy flow, though standard for tele-health and appointment apps; and (b) a persistent header chip across the app that carries an active order-state event — new for 1mg. Both are justified and well-scaffolded, but the brief itself acknowledges "a small brand shift". The rest of the flow (address, payment, confirmation) uses existing marketplace patterns. Mix of existing and new. **Direction:** in the wireframe, verify the header chip pattern against any pre-existing 1mg persistent-notification component; if one exists, reuse it, do not invent a new one. |

**Textual — terminology inconsistencies to fix:**

1. **"consult" (short) vs "consultation" (full)** — one drift on the checkout step copy: "This order needs a quick doctor consult". Standardise on "consultation" in every user-visible surface; keep the shorter form only in internal design language.
2. **"Approved" (user-facing state chip) vs the surrounding service register** — "Approved" is compliance vocabulary. Every other user-facing string in the brief uses service language ("Waiting for you", "Doctor prepping", "Answer in App"). Rewrite to "Ready to dispatch" for consistency of register.
3. **Reconnect action label** — surface three variants: "I'm ready now — reconnect" (prose), "Reconnect now" (table), "Ready to reconnect?" (copy row). Freeze the button label as "Reconnect now" and use "Ready to reconnect?" only as the question above it.
4. **"consultation" (user copy) vs "consultation card" (design copy)** — split is fine; enforce that "card" never leaks into user-visible strings.
5. **"on hold" (banned) vs "Waiting for you" (canonical)** — the brief explicitly bans "on hold". Good discipline; carry into every downstream copy pass so no state string ever reintroduces it.

**Textual — interactions that differ from context:**
- Scheduling step inside checkout is a new pattern for 1mg pharmacy (not for tele-health).
- Persistent header chip carrying a live order-state event across screens is a new-ish component; verify collision with existing offer strips and toasts.

**Textual — components that could reuse existing patterns:**
- Bottom-sheet reschedule → reuse the existing 1mg bottom-sheet component.
- Slot chips → reuse whatever chip component already exists on 1mg filter surfaces (unspec'd — worth confirming in wireframe).
- Header chip → verify whether a persistent-notification bar already exists on 1mg (order tracking, delivery ETA); if yes, reuse it rather than invent.

**Gate 4 score: 21 / 28**

---

## GATE 5 — Design Fundamentals

**Applying Gate 0 rule generously:** The artifact is a text brief with no visual layout, colour spec, typography scale, icon set, or interaction fidelity. Every binary check and any rated check that cannot be assessed without pixels is marked N/A. Only IA (evaluable from described structure) and typography intent (partially inferable from described hierarchy) are scored.

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 5.1 | WCAG AA compliance met? | **N/A** | — | No visual spec exists to audit. |
| 5.2 | Keyboard navigation works (design intent)? | **N/A** | — | No accessibility semantics described at brief stage. |
| 5.3 | Screen reader compatible? | **N/A** | — | Explicitly N/A for static mockup. |
| 5.4 | Colour contrast sufficient? | **N/A** | — | No colours specified. |
| 5.5 | All images have alt text? | **N/A** | — | No informational images. |
| 5.6 | Text resizable to 200%? | **N/A** | — | No type scale specified. |
| 5.7 | Captions for media? | **N/A** | — | No media. |
| 5.8 | Touch targets ≥ 44×44? | **N/A** | — | No visual spec. |
| 5.10 | Single-direction scrolling? | **N/A** | — | No layout spec. |
| 5.11 | Responsive across breakpoints? | **N/A** | — | Mobile-first single-viewport scope. |
| 5.12 | Colour communicates meaning consistently? | **N/A** | — | No colours. |
| 5.13 | Loading / progress states present? | **N/A** | — | Static mockup rule. The design *names* five live states (Scheduled → Prepping → Incoming → In call → Approved), which is loading-state intent, but pixels are absent. |
| 5.14 | Feedback within 100ms? | **N/A** | — | Static mockup rule. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 5.15 | Typography quality | **3/5** | The brief describes hierarchy at the *surface* level (consultation card dominant, delivery card secondary/greyed, persistent header chip), and at the *state-list* level (countdown emphasized, timestamp secondary). Intent is present but scale, weight, and type-system role are absent. Score reflects "clear hierarchy, some inconsistency untested". |
| 5.16 | Icon clarity | **N/A** | — | No icons specified in the brief. |
| 5.17 | Information architecture | **5/5** | Strongest gate for this artifact. The IA is precisely tuned to the reframe: consultation card (dominant, live) above delivery card (secondary, greyed) exactly matches the user's mental model of "the active event I must participate in" vs "the passive shipment I'm waiting on". The persistent header chip mirrors real-life appointment-app patterns (Uber ride in progress, Zomato delivery ETA). Cart → Address → Slot → Payment ordering places the commit boundary in the right structural place. Structure matches the user mental model that Form 3 named. |
| 5.18 | Search effectiveness | **N/A** | — | This is not a search feature. |

**Textual:**
- Accessibility failures: none evaluable at brief stage. **Flags for the next iteration (wireframe):**
  - `[major]` Header chip must be reachable by keyboard and announced by screen reader as an interactive live-region.
  - `[major]` "Answer in App" call-answer UI must expose an accessible "Answer" and "Decline" pair, not a swipe-only pattern.
  - `[major]` "Reconnect now" push/SMS deep link must land on a focus-managed target so screen-reader users are placed on the primary action, not on the top of the screen.
  - `[minor]` Slot picker chips at 320-360px viewport risk sub-44 touch targets; audit early.
  - `[minor]` Rejection screen with three exits — verify tab order and logical reading order.
- Missing loading/empty states: slot-picker loading state; no-slots-available state; scheduled-slot-expired state; PSTN fallback unavailable state.
- **Flag for human:** Does the consultation card visually earn its dominance without shouting? Needs designer judgement in the wireframe.
- **Flag for human:** Is a persistent header chip the right pattern, or does it join a pile of other 1mg chips and become noise? Taste + system knowledge.

**Gate 5 score: 8 / 10** (23 N/A points: 13 binary + 5 for 5.16 + 5 for 5.18)

---

## GATE 6 — Design Philosophy

**Applying Gate 0 rule generously:** Every binary check is either tagged N/A for a stage prior to shipping code, or is untestable at the brief stage because no screens are drawn.

| ID | Question | Answer | Note |
|----|----------|--------|------|
| 6.1 | Broken links / errors / outdated content? | **N/A** | Nothing implemented to audit. |
| 6.2 | HTTPS and security indicators? | **N/A** | Not shipping code (tag exemption). |
| 6.3 | Privacy policy accessible? | **N/A** | No data-collection screens are drawn. The "Who is this for?" field is named but not scoped. **Flag for wireframe:** consent notice belongs at that input, plus a plain-language "this is used by the doctor for this consultation only". |
| 6.4 | Social proof present? | **N/A** | Screen type does not warrant testimonials; the doctor's name ("Dr. Sharma") + branded caller ID is the functional trust signal, and the brief handles it. |
| 6.5 | Contact information easy to find? | **N/A** | Feature-specific surfaces, not global. Note: the rejection screen offers three concrete exits and the miss-recovery loop is entirely self-serve — good trust behaviour. |
| 6.6 | Data-usage transparency? | **N/A** | No data-collection screens drawn. Flag: prescription/consult transcript retention needs a plain-language notice at the point of the call (and probably in the "Buyer is not the patient" field UI). |

**Flag for human (all Gate 6 rated territory):**
- Does the brief feel professional and trustworthy? Feeling, not fact.
- Does branding "Doctor consultation" as user-facing language raise unrealistic clinical expectations (users may expect medical *advice*, not compliance)? Tonal call.
- Does introducing a doctor's name and photo build trust or feel manufactured? Cultural + taste.
- Is the trade — a longer checkout in exchange for a predictable post-checkout — actually acceptable to the growth team? Business context.

**Gate 6 score: N/A** (all 6 checks N/A at this artifact stage; gate contributes 0 to earned and 0 to denominator)

---

## GATE 7 — Innovation + Good Taste (Human review)

**Status:** NEEDS HUMAN REVIEW.

**Questions for the human reviewer:**
- The brief explored two full stances with real depth (Prevent as primary, Assist as sketched alternative). Recover was reasoned against but never *sketched*. Would you like the third stance sketched too, or is a rebuttal enough at this stage?
- Is the "validation-is-actually-an-appointment" reframe genuinely fresh for 1mg, or is it a pattern that Practo / Tata Health / other Indian tele-consult products have already converged on and this brief is catching up to?
- Is the "consultation slot inside checkout" pattern borrowed from real life (booking a doctor's slot at a clinic, salon booking) — and would 1mg's specific user recognise it without instruction?
- Is the "Now (call in ~30 seconds)" default a fresh moment or does it feel like Uber "pool now" behaviour transplanted into pharmacy?
- Would the persistent header chip feel like helpful continuity or intrusive surveillance? Taste question.

---

## GATE 8 — Gut + Experience Check (Human review)

**Status:** NEEDS HUMAN REVIEW.

**Questions for the human reviewer:**
- The design assumes doctor capacity is "a controllable variable, not a fixed external one". Have you seen tele-consultation capacity actually planned around a scheduled-slot model in an Indian pharmacy context? If not, this assumption is the single biggest ship risk.
- The design also assumes users will accept a longer checkout in exchange for post-checkout predictability. Have you seen that trade succeed in Indian e-commerce, or does the industry data say drop-off wins every time?
- Does moving payment *after* the consultation slot risk creating a new failure mode — user picks a slot, then payment fails, then the slot is orphaned? The brief doesn't handle this race.
- Is "consultation" the right user-facing word given that some users may think it means real medical advice, and get disappointed when it's a two-minute compliance check?
- Have you seen any competitor (Netmeds, PharmEasy, Apollo 24/7) try this appointment-metaphor pattern for Rx validation? Any lessons from that?
- Would you personally trust this flow if you were reordering your parent's BP meds late at night with a 5-minute window before catching a train?

---

## Stance-Check assessment (dedicated paragraph)

**The Stance Check partly worked, but with the same asymmetry seen in iteration-1.** It read as genuine divergent thinking on the Assist-alternative arm and as reasoned rebuttal on the Recover arm — not as ceremony overall, but not fully symmetric either. The evidence: Question 2's Assist-first alternative is a real architectural sketch, ~150 words, with concrete design elements — doctor's photo and queue position on the confirmation screen, live ETA, "Call me now" CTA, persistent status chip across app screens, escalating notification stack (in-app banner + push + SMS + WhatsApp), a 30-second nudge threshold, one-tap "Tap to resume" reconnect, inline three-slot reschedule after two misses, in-app VoIP with branded PSTN fallback, order status elevated to a top-level tab. That is what a genuinely-explored alternative looks like; the designer honestly assesses it as "coherent, shippable, less-invasive" and "genuinely competitive on a scoped, near-term basis". That is intellectual honesty, not ceremony. However — the Recover-first arm was *not* sketched. Question 3 argues against Recover as primary ("Recovery only fires after a failure... it does nothing for a user who waits 32 minutes and cancels before any miss occurs") but the reader never sees what a Recover-first architecture would concretely look like. This is the same gap the iteration-1 eval flagged. The reasoning against Recover is substantive (it identifies a structural blind spot: the pre-miss abandonment cohort), so the check is not ceremonial — but the spec asks for *both* alternatives sketched, and only one was. **Verdict: working as intended for two of three stances, incomplete for the third. Consider tightening the sub-skill to explicitly require a two-to-four-sentence concrete sketch of the non-chosen stances before their rebuttal.**

The other honest test — did Form 3 change the shape of the solution vs Form 1? — clearly yes. The whole recommendation reads as an answer to "the metaphor is wrong", not to "fix these four bullets". The three composed layers (Prevent / Assist / Recover) each derive from Form 3's diagnosis, not from Form 1's failure list. That is the reframe check doing real work.

---

## Report card

```
╔══════════════════════════════════════════════════╗
║            UX EVAL REPORT CARD                   ║
║            Agent Evil — v1.0                     ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  OVERALL SCORE:  63/78  ( 81%  · Grade: B )      ║
║  (31 N/A points removed from 109 max)            ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  GATE SCORES                                     ║
║                                                  ║
║  1 · The Problem      ⚠️  HUMAN REVIEW  (Match)  ║
║  2 · The Solution     19/23  ( 83% )             ║
║  3 · Subtract         15/17  ( 88% )             ║
║  4 · Consistency      21/28  ( 75% )             ║
║  5 · Fundamentals     8/10   ( 80% )             ║
║  6 · Philosophy       N/A    (entire gate)       ║
║  7 · Innovation       ⚠️  HUMAN REVIEW           ║
║  8 · Gut Check        ⚠️  HUMAN REVIEW           ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  BINARY FAILURES (every No)                      ║
║                                                  ║
║  [2.4] Error messages present for all form       ║
║        fields and actions? →                     ║
║        Mainline error states unspec'd. Add a     ║
║        one-line inline state for:                ║
║         (a) checkout network loss while          ║
║             picking a slot                       ║
║         (b) no slots available in the next       ║
║             2 hours                              ║
║         (c) payment success but scheduled slot   ║
║             expires (race)                       ║
║         (d) VoIP fails AND PSTN fallback         ║
║             unavailable                          ║
║        These are mainline, not edges. Add        ║
║        them to the copy table before wireframe.  ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  LOW RATINGS (every score ≤ 2)                   ║
║                                                  ║
║  (none — the lowest rated score is 3/5 at 4.4    ║
║   Terminology consistency, 4.8 Navigation        ║
║   predictability, and 5.15 Typography quality;   ║
║   all three are direction-for-next-artifact,     ║
║   not gate-blockers.)                            ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  INSIGHTS                                        ║
║                                                  ║
║  Strongest gate:  Gate 3 (Subtract) — 88%.       ║
║   Copy is service-first ("consultation" not      ║
║   "validation"), locates responsibility          ║
║   correctly ("Waiting for you" not "on hold"),   ║
║   and uses countdowns instead of timestamps.     ║
║   Auto-fill and single-tap defaults are          ║
║   present at every commit-heavy moment.          ║
║                                                  ║
║  Weakest gate:    Gate 4 (Consistency) — 75%.    ║
║   Real terminology drift on "consult" vs         ║
║   "consultation", "Approved" as system-word      ║
║   state leak, and three variants of the          ║
║   reconnect action label. Two new navigation     ║
║   patterns (in-checkout scheduling, persistent   ║
║   header chip) introduced without an explicit    ║
║   reuse pass against the existing 1mg system.    ║
║                                                  ║
║  Biggest risk:    The design bets on doctor-     ║
║   capacity being a controllable variable that    ║
║   can be planned into scheduled slots. If it     ║
║   isn't — if the business is a supply-           ║
║   constrained tele-consult panel — the           ║
║   scheduled-slot model creates a new visible     ║
║   failure mode (empty slots the user can see)    ║
║   where the current async-ambush model hides     ║
║   it in a wait. That is stated in the trade-     ║
║   off table honestly, but it deserves an         ║
║   engineering + ops signoff before wireframe.    ║
║                                                  ║
║  Quick wins:                                     ║
║   1. Freeze terminology: "consultation" (never   ║
║      "consult"); "Ready to dispatch" (never      ║
║      "Approved"); "Reconnect now" as the only    ║
║      button label. One-line edit to the copy     ║
║      table, high consistency lift.               ║
║   2. Add four mainline error states to the       ║
║      copy table (network loss, no slots, slot    ║
║      expired, both call paths down) — one line   ║
║      each, before wireframing begins.            ║
║   3. Rewrite the checkout-step body from 16      ║
║      words to 9: "One quick doctor call before   ║
║      we ship — about 3 minutes. Pick a time."    ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  ITEMS FOR HUMAN REVIEW                          ║
║                                                  ║
║  Gate 1: Alignment = Match, and Form 3 is        ║
║   stronger than the raw brief asked for.         ║
║   Human validation: is the appointment           ║
║   metaphor the right root frame for Indian       ║
║   pharmacy users? Is moving the commit           ║
║   boundary before Payment acceptable to the      ║
║   business given drop-off risk?                  ║
║                                                  ║
║  Gate 2 flags:                                   ║
║   — Will Indian pharmacy users accept a          ║
║     scheduling step inside checkout, or read     ║
║     it as friction? Live testing.                ║
║   — Is "consultation" the right user-facing      ║
║     word, or does it inflate expectations?       ║
║                                                  ║
║  Gate 3 flags:                                   ║
║   — Do all five live states earn their place,    ║
║     or could Prepping + Incoming collapse for    ║
║     the user?                                    ║
║   — Does "Who is this for?" belong in the        ║
║     consultation step or in Cart?                ║
║                                                  ║
║  Gate 5 flags (all deferred to wireframe):       ║
║   — Contrast, keyboard nav, and screen-reader    ║
║     ordering for the header chip + Answer/       ║
║     Decline pair.                                ║
║   — Slot-chip touch targets at 320-360px.        ║
║   — Whether the header chip pattern conflicts    ║
║     with existing 1mg toasts / offer strips.     ║
║                                                  ║
║  Gate 6 flags:                                   ║
║   — Consent + data-handling notice at the        ║
║     "Who is this for?" field and at the call     ║
║     itself.                                      ║
║   — Prescription/consult transcript retention    ║
║     policy needs plain-language surfacing.       ║
║                                                  ║
║  Gate 7 (Innovation):                            ║
║   — Should Recover-first be sketched too, or    ║
║     is rebuttal sufficient? (Same gap as         ║
║     iteration-1.)                                ║
║   — Is the reframe fresh for 1mg or already      ║
║     converged in Indian tele-consult apps?       ║
║   — Does the "Now (call in ~30 sec)" default     ║
║     feel like real-life or transplanted Uber?    ║
║                                                  ║
║  Gate 8 (Gut):                                   ║
║   — Is doctor-capacity actually a controllable   ║
║     variable in the 1mg operating model?         ║
║   — Payment-succeeds-then-slot-expires race:    ║
║     is it real, and does it need explicit       ║
║     handling before ship?                        ║
║   — Have you seen a competitor try this          ║
║     appointment-metaphor Rx flow, and what       ║
║     happened?                                    ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  TERMINOLOGY ISSUES                              ║
║                                                  ║
║  1. "doctor consult" (short, checkout step) vs   ║
║     "Doctor consultation" (everywhere else) —    ║
║     one drift. Freeze on "consultation" for      ║
║     every user-visible surface; keep "consult"   ║
║     out of user copy.                            ║
║  2. "Approved" (user-facing state chip in the    ║
║     five-state list) — compliance word in a      ║
║     service register. Rewrite to "Ready to       ║
║     dispatch".                                   ║
║  3. Reconnect action label has three variants:   ║
║     "I'm ready now — reconnect" (prose),         ║
║     "Reconnect now" (table), "Ready to           ║
║     reconnect?" (copy row). Freeze the button    ║
║     label as "Reconnect now"; use "Ready to      ║
║     reconnect?" only as the question above it.   ║
║  4. "Consultation card" is internal design       ║
║     language; ensure "card" never leaks into     ║
║     user-visible strings.                        ║
║  5. Explicit ban on "on hold" is good discipline ║
║     — carry into every downstream copy pass so   ║
║     no state string re-introduces it.            ║
║  6. "Dispatching" (state chip) — consider "On    ║
║     its way" for the user register at that       ║
║     moment.                                      ║
║                                                  ║
║  ACCESSIBILITY FAILURES                          ║
║                                                  ║
║  None evaluable at brief stage — all 13 binary   ║
║  accessibility checks N/A. Flags for wireframe:  ║
║   [major] Persistent header chip must be a       ║
║           keyboard-reachable, SR-announced       ║
║           live-region                            ║
║   [major] Answer/Decline pair on incoming        ║
║           call: must not be swipe-only           ║
║   [major] Deep-linked reconnect target from      ║
║           push/SMS must land focus on the        ║
║           primary action                         ║
║   [major] Slot-picker chip touch targets at     ║
║           320-360px viewports                    ║
║   [minor] Rejection-screen three-exit tab       ║
║           order and reading order                ║
║                                                  ║
║  COPY REWRITES                                   ║
║                                                  ║
║  Before → After                                  ║
║                                                  ║
║  "This order needs a quick doctor consult        ║
║   (about 3 minutes) before we can dispatch.      ║
║   Choose a time."                                ║
║    → "One quick doctor call before we ship —     ║
║       about 3 minutes. Pick a time."             ║
║                                                  ║
║  "Actually, schedule instead"                    ║
║    → "Schedule instead"                          ║
║                                                  ║
║  "Consultation scheduled 4:20 PM. Delivery       ║
║   estimated 6:30 PM once approved."              ║
║    → "Doctor call at 4:20 PM · Delivery ~6:30    ║
║       PM after the call."                        ║
║                                                  ║
║  State chip "Approved"                           ║
║    → "Ready to dispatch"                         ║
║                                                  ║
║  State chip "Dispatching"                        ║
║    → "On its way"                                ║
║                                                  ║
║  Add: checkout-network-loss slot-picker state    ║
║       (missing)                                  ║
║    → "Couldn't load slots. Check your            ║
║       connection and tap to retry."              ║
║                                                  ║
║  Add: no-slots-available state (missing)         ║
║    → "No slots in the next 2 hours. Try          ║
║       again in a few minutes, or reach out       ║
║       to support."                               ║
║                                                  ║
║  Add: slot-expired-post-payment state (missing)  ║
║    → "Your consultation time was taken while     ║
║       you paid. Here are the next slots."        ║
║                                                  ║
║  Add: both-call-paths-down state (missing)       ║
║    → "Can't reach the doctor right now. We'll    ║
║       hold your order — try again in 5 minutes." ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

**One-sentence honest summary:** A strong strategic brief that earns its B grade on the reframe alone — Form 3 is a genuine design-shaped articulation and the whole recommendation reads as an answer to it — but drops points on mainline error-state completeness and on terminology drift that a text brief has no excuse for.
