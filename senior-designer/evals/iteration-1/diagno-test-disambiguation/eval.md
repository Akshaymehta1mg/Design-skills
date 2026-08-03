# UX Eval — "Urine" Disambiguation Brief

Agent Evil, walking gates 0 → 8 against the framework in `ux-eval/SKILL.md`, evaluating `output.md` in this same folder.

---

## GATE 0 — Artifact stage

**Declared stage:** Static mockup (best-fit; the artifact is a text design brief with no visual layout, so it is even less concrete than a static mockup — per instructions, N/A logic is applied generously in Gates 5 and 6).

**Guiding rule applied:** Score the design intent expressed in the brief, not the fidelity of the artifact. Every check tagged `(N/A if static mockup)`, `(N/A if not shipping code)`, or otherwise untestable at the brief stage is removed from the denominator; it is never scored as 0.

---

## GATE 1 — The Problem (Human review)

**Agent 1 stated:** "Users searching an ambiguous term like 'urine' on 1mg Diagnostics get 7 near-identical result cards and cannot tell which one matches their doctor's handwritten shorthand; both SRP and PDP need intervention."

**Context (parent-provided) states:** 1mg diagnostics booking app, doctor-initiated traffic, "urine" query returns 7 look-alike SKUs on the SRP; interventions must span SRP disambiguation, PDP rescue, and a light Prevent nudge.

**Alignment:** Match. The brief also correctly reframes it as a *translation task, not a shopping task* — that reframing is stronger than the raw prompt asked for.

**Status:** NEEDS HUMAN REVIEW — a human must validate that "correct SKU booked" is genuinely the leverage metric (vs. e.g., total conversion, cancel rate, LTV) and that partner-lab SKU distinctness is truly a constraint rather than a solvable catalog problem.

---

## GATE 2 — The Solution

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 2.1 | Auto-save / data loss prevention? | **N/A** | — | No user work is authored; the task is search → book, not form-filling. N/A per Gate 0 rule (not applicable to artifact type). |
| 2.2 | Confirmation before irreversible actions? | **Yes** | 1/1 | The PDP rescue strip ("Is this the test on your prescription? [Yes, continue] [Not sure — see similar]") is an explicit soft-confirmation interstitial before BOOK, which the brief itself names as the one-tap commit. |
| 2.3 | Progressive disclosure? | **Yes** | 1/1 | Chips render only when query returns >3 near-name matches; contrast lines only when a genuine confusable is on-screen; bottom sheet reveals the 2–3 neighbours on demand rather than crowding the PDP. |
| 2.4 | Error messages present for all form fields and actions? | **No** | 0/1 | The brief spec's soft error-prevention (contrast lines, rescue strip, "Other" fuzzy match) but never spec's mainline error states: zero-results, network failure on chip filter, OCR failure on Scan Rx, illegible-prescription fallback (only mentioned as an edge). **Direction:** Spec an inline empty state for "no matches" on both search and chip-filter, a retry state for network failure, and an OCR-failure fallback that hands off to typed search — one line each, not decorative. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 2.5 | Error message clarity | **3/5** | Differentiator copy ("Different from Culture — this test does not identify bacteria") explains what and gestures at why, but a marginal patient may not know what "identifies bacteria" means diagnostically. "Not sure — see similar tests" is a good recovery affordance. It identifies + suggests fix, but doesn't anticipate the confused-but-doesn't-know-it user. **Direction:** Rewrite the contrast line in outcome language — e.g., "Different from Culture — this test looks for infection signs; Culture confirms the exact bacteria and antibiotic. Ask your doctor which they wrote." |
| 2.6 | Step efficiency | **4/5** | Best-case flow: type "urine" → tap alias chip → tap enriched card → tap BOOK = 4 steps, or 3 if the chip resolves to a single canonical card. Very tight for an ambiguous query. The only merge candidate is "chip tap could auto-scroll or auto-select if it collapses to one card" — worth exploring but not obvious win. |
| 2.7 | Onboarding weight | **4/5** | No onboarding is proposed; the design teaches by doing. The chip label "What did your doctor write?" is itself a mini-onboarding sentence — light, invisible, effective. |

**Textual (no score):**
- Steps for the primary task: 3–4 taps in the best case (type → chip → card → book), collapsing to 3 when the chip resolves to a single canonical card.
- Merge candidate: chip tap on a single-canonical-match query could auto-advance to the PDP, skipping the intermediate SRP card tap. Trade-off is loss of the enriched subline moment; the brief prefers to keep it, defensibly.
- **Flag for human:** Can a first-time user reach the correct SKU without help? Needs real prescription-in-hand testing (which the brief itself proposes — good).
- **Flag for human:** Will a low-literacy user recognise "R/E" and "C/S" on the chip row, or does the chip label itself need to be more descriptive?

**Gate 2 score: 13 / 18** (1 N/A)

---

## GATE 3 — Subtract

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 3.1 | Can any two adjacent steps be merged? | **Yes** | 1/1 | The brief already merges: alias duplicates → one card ("Urine Routine Examination (R / RE / R/E / R/M)"); lab variants collapse under the canonical card; the chip row filters to a single card in the ideal case. |
| 3.2 | Is the user doing work the system could auto-fill? | **Yes** | 1/1 | The brief names Scan-Rx (OCR auto-extract) and the display-layer alias consolidation. It is honest that OCR is a phase-2 bet, but the design is aware of the auto-fill opportunity and stages it. |
| 3.3 | Empty states that over-explain? | **N/A** | — | No empty state is designed in the brief. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 3.4 | Copy conciseness | **4/5** | "What did your doctor write?" (5 words), "Also written as: R, RE, R/E, R/M" (parseable at a glance), "Is this the test on your prescription?" (7 words) — all tight. The contrast lines carry the most weight and could tighten further. |
| 3.5 | Label efficiency | **4/5** | Labels are verb-forward and specific: "Yes, continue", "Not sure — see similar", "Switch", "Book". None waste a word. Small nit: "Not sure — see similar tests" could be "Not sure — show similar" (one fewer word, sharper). |
| 3.6 | Jargon score | **5/5** | Deliberate patient-facing translation: "Contains 42 tests" replaced with "Checks for: UTI, kidney function, protein, sugar"; "R/E" and "C/S" appear only in the alias echo (which is *where* the user needs to recognise them). Report TAT in plain hours. A non-technical caregiver reads every word. |

**Textual — copy that could be shorter:**
- "Not sure — see similar tests" → "Not sure — show similar" (saves one word, sharper verb).
- "Different from Culture — this test does not identify bacteria" → "Different from Culture — screens only; doesn't confirm bacteria" (tighter, and "confirm" is more patient-parseable than "identify").
- "Have a prescription? Scan it and we'll find your tests." → "Have a prescription? Scan it — we'll find every test." (drops one word, adds a stronger promise).
- "Search test name, or scan your prescription" → same; already tight.
- "Also written as: R, RE, R/E, R/M · Checks for: UTI, kidney, protein · Report in 24 hrs" → keep, but consider `Also: R · RE · R/E · R/M` on very narrow phones.

**Textual — inputs that could be auto-filled:**
- Prescription photo → all detected tests (Scan-Rx flow; brief already notes this).
- User's search term should pre-select the closest chip on first render, not require a second tap.
- If the user arrived from a shared PDP link, the alias line should echo whatever alias the sharer used (query param carry-through).

**Flag for human:**
- Does the "Other" chip need to exist in v1, or does it dilute the primary chips visually? Needs designer taste.
- Do all 7 SKUs need to be preserved as separate SKUs behind the display consolidation, or is catalog cleanup the actual leverage move?

**Gate 3 score: 15 / 17** (1 N/A)

---

## GATE 4 — Consistency

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 4.1 | System state always visible? | **Yes** | 1/1 | The user always knows which surface they are on (SRP vs. PDP), and the rescue strip locates them in relation to the correctness question. |
| 4.2 | Feedback visible after every interaction? | **Yes** | 1/1 | Chip tap filters the list; card tap opens PDP; rescue strip tap opens bottom sheet; Switch tap changes tests. Every documented interaction has a described consequence. |
| 4.3 | Similar components behave the same way? | **Yes** | 1/1 | The alias line appears identically on SRP card and PDP; the chip pattern (`What did your doctor write?`) uses the same filter semantics as any other filter chip on a Diagnostics SRP; the bottom-sheet-of-similar-tests pattern is standard. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 4.4 | Terminology consistency | **4/5** | "Test" and "SRP/PDP" used consistently. Minor slip: the same action is called `Scan Rx` (flow diagram), `Scan your prescription` (home hint), `scan it` (home hint), `Upload prescription to verify` (PDP CTA). Four phrasings for one action — pick one. **Direction:** Standardise on "Scan prescription" everywhere the user sees it; keep "Scan-Rx" only in internal design language. |
| 4.5 | Interaction pattern consistency | **4/5** | Chip → filter, card → detail, strip → sheet — all standard mobile diagnostics-app patterns. No same-gesture-different-outcome traps described. The one thing the brief doesn't say is whether the rescue strip is dismissible on the current PDP or persists across the session — a small consistency question worth answering. |
| 4.6 | Label specificity | **4/5** | "Yes, continue" (vs generic "OK"), "Not sure — see similar" (specific), "Switch" on bottom-sheet items (concrete), "Book" (the existing pattern, unchanged). All self-explanatory. Small ambiguity: "Other" chip label is generic — "Something else" or "Different wording" would be sharper. |
| 4.7 | Error tone consistency | **4/5** | The three sentence-shaped copy interventions (contrast line, alias echo, rescue-strip question) all read in the same factual, patient-facing register. Consistent voice. Would tighten to 5 with an explicit tone guide for the alias-table content (which the brief itself flags as legal/medical territory). |
| 4.8 | Navigation predictability | **5/5** | The mental model — search → filter → card → detail → confirm — is fully aligned with existing marketplace / diagnostics app patterns. The rescue strip does not rewrite navigation; it inserts a soft check in the same lane. |

**Textual — terminology inconsistencies to fix:**
- `Scan Rx` / `Scan your prescription` / `scan it` / `Upload prescription to verify` — collapse to **"Scan prescription"** in all user-facing copy.
- "Similar tests" (rescue strip) vs "commonly-confused neighbours" (design language) — the first is user copy, the second internal; that split is fine, just don't leak the second into UI.
- "Alias" is entirely design-internal; user copy uses "commonly written as" — good discipline, keep it.

**Textual — interactions that differ from context:**
- Rescue strip is a new-ish pattern for 1mg PDPs; verify it doesn't collide visually with existing PDP promo strips (health blog snippets, offer banners). If it does, the strip's cost is real.

**Textual — components that could reuse existing patterns:**
- Bottom sheet for similar tests should reuse the existing 1mg bottom-sheet component (which the brief doesn't specify — worth confirming).
- Chip row should reuse whatever chip component the 1mg SRP already uses for filters (again, unspec'd — worth confirming).

**Gate 4 score: 24 / 28**

---

## GATE 5 — Design Fundamentals

**Applying Gate 0 rule generously:** The artifact is a text brief with no visual layout, color spec, typography scale, or interaction fidelity. Every binary check and any rated check that cannot be assessed without pixels is marked N/A. Only the checks evaluable from described intent (IA, search behaviour, described type hierarchy) are scored.

### Binary

| ID | Question | Answer | Points | Note |
|----|----------|--------|--------|------|
| 5.1 | WCAG AA compliance met? | **N/A** | — | No visual spec exists to audit. |
| 5.2 | Keyboard navigation works (design intent)? | **N/A** | — | No accessibility semantics described at brief stage. |
| 5.3 | Screen reader compatible? | **N/A** | — | Explicitly N/A for static mockup (and even more so for a text brief). |
| 5.4 | Colour contrast sufficient? | **N/A** | — | No colours specified. |
| 5.5 | All images have alt text? | **N/A** | — | No images in the artifact. |
| 5.6 | Text resizable to 200%? | **N/A** | — | No type scale specified. |
| 5.7 | Captions for media? | **N/A** | — | No media. |
| 5.8 | Touch targets ≥ 44×44? | **N/A** | — | No visual spec. |
| 5.10 | Single-direction scrolling? | **N/A** | — | Horizontal chip row is proposed, but scroll behaviour is not spec'd — untestable at brief stage. |
| 5.11 | Responsive across breakpoints? | **N/A** | — | Mobile-first single-viewport scope. |
| 5.12 | Colour communicates meaning consistently? | **N/A** | — | No colours. |
| 5.13 | Loading / progress states present? | **N/A** | — | Static mockup rule. |
| 5.14 | Feedback within 100ms? | **N/A** | — | Static mockup rule. |

### Rated

| ID | Factor | Score | Reasoning |
|----|--------|-------|-----------|
| 5.15 | Typography quality | **3/5** | The brief describes a hierarchy — name (primary), aliases + purpose + logistics (subline), price + BOOK (right rail) — with roles clearly assigned, but no scale, weight, or type system is specified. Intent is present but unpainted. Score reflects "clear hierarchy, some inconsistency untested". |
| 5.16 | Icon clarity | **N/A** | — | No icons specified in the brief. |
| 5.17 | Information architecture | **5/5** | This is the strongest gate for this artifact. The IA is precisely-tuned to the user's actual question: chip row asks "what did your doctor write?" (grouped by user query, not by SKU), cards consolidate aliases behind one canonical name, PDP places the alias echo above the fold, rescue strip places the correctness check *before* commit. Structure matches user mental model exactly. |
| 5.18 | Search effectiveness | **5/5** | Chip filters, alias-consolidated cards, contrast lines, "Other" fuzzy match with confidence scoring, and a Scan-Rx alternative path. This is a substantial search-quality upgrade over "type box + result list", and it engages every lever the framework rewards. |

**Textual:**
- Accessibility failures: none evaluable at brief stage. **Flag for human/next iteration:** when the wireframe lands, audit contrast on the alias subline (it will be small type on white), touch-target on the chip row on <360px viewports, and screen-reader ordering of the PDP rescue strip vs BOOK.
- Missing loading/empty states: chip-filter loading, zero-match state on the SRP, OCR-in-progress state, OCR-failure state, PDP-not-found state. All fair calls for the next artifact (wireframe), not blocking at brief stage.
- **Flag for human:** Does the visual hierarchy of the PDP put the rescue strip in the right vertical position — above the price rail but below the test name? Needs designer judgement in the wireframe.
- **Flag for human:** Should the alias echo animate in, or appear statically? Purposeful vs. decorative — needs taste.

**Gate 5 score: 13 / 15** (18 N/A points: 13 binary + 5 for rated 5.16)

---

## GATE 6 — Design Philosophy

**Applying Gate 0 rule generously:** Every binary check in this gate is either tagged N/A for a stage prior to shipping code, or is untestable at the brief stage because no screens are drawn. All binary checks are N/A.

| ID | Question | Answer | Note |
|----|----------|--------|------|
| 6.1 | Broken links / errors / outdated content? | **N/A** | Nothing implemented to audit. |
| 6.2 | HTTPS and security indicators? | **N/A** | Not shipping code (tag exemption). |
| 6.3 | Privacy policy accessible? | **N/A** | No data-collection screens are designed in this brief; Scan-Rx is named but not scoped. **Flag for the next artifact:** prescription upload MUST show a plain-language "we don't store your image beyond match" (or accurate equivalent) affordance. |
| 6.4 | Social proof present? | **N/A** | Doctor-initiated diagnostic-test surface does not warrant testimonials/reviews (tag exemption). |
| 6.5 | Contact information easy to find? | **N/A** | Feature-specific surfaces, not global (tag exemption). The "Talk to a 1mg advisor" escape hatch in the illegible-prescription edge is a nice touch — carry it forward. |
| 6.6 | Data-usage transparency? | **N/A** | No data-collection screens designed yet. Same flag as 6.3 for the wireframe. |

**Flag for human (all Gate 6 rated territory):**
- Does the brief feel professional and trustworthy? Feeling, not fact.
- Does the alias echo — "Commonly written as R, RE, R/E, R/M" — read as expert care or as clinical overload? A caregiver's perception, not mine.
- Does the rescue-strip pattern feel patronising ("we think you might be wrong") or reassuring ("we've got you")? Tonal call.
- Is the Scan-Rx nudge honest given that OCR is phase-2? If it appears in v1 without a working OCR path, it becomes broken UX. Needs product decision.

**Gate 6 score: N/A** (all 6 checks N/A at this artifact stage; gate contributes 0 to earned and 0 to denominator)

---

## GATE 7 — Innovation + Good Taste (Human review)

**Status:** NEEDS HUMAN REVIEW.

**Questions for the human reviewer:**
- The brief explored two full stances (Assist as primary, Prevent-first as alternative) with real depth. Was a third direction (say, "post-booking correction" — book fast, correct within a grace window) considered and rejected, or not considered at all?
- Is the "translate a paper prescription word into an app SKU" reframe actually novel for 1mg, or is it a pattern the diagnostics category has already converged on that this brief is catching up to?
- The alias chip labelled "What did your doctor write?" is a strong candidate for a small, fresh moment — is it fresh, or is it a language most Indian diagnostics apps already use?
- Would users recognise the "Also written as R, RE, R/E, R/M" line as a helpful mirror of their prescription, or does it look like clinical noise?
- Is the Scan-Rx CTA on the search-empty state inspired by real-life ("hand it to the pharmacist") or invented?

---

## GATE 8 — Gut + Experience Check (Human review)

**Status:** NEEDS HUMAN REVIEW.

**Questions for the human reviewer:**
- The brief punts key layout tradeoffs (chip row pushing first result below the fold, rescue strip competing with BOOK) to the wireframe stage. Is that punt honest, or is it hiding a decision the designer didn't want to make?
- The "confident-but-wrong" user (page 5 of the Stance Check) is a sharp insight. Do you believe this segment is real and material, or is it a rhetorical device to justify Assist?
- The catalog-consolidation-is-really-the-fix caveat is called out honestly. Does it deserve to be *more* prominent — as in, should the recommendation lead with "fix the catalog first, this UI is the fallback"?
- Have you seen the pattern of "translate paper shorthand into digital SKU" succeed or fail in an adjacent product (Practo, Tata 1mg Meds, Netmeds, Lupin lab apps)?
- Would you personally trust a patient to book the right test after using this SRP? Not the same as passing every binary check.

---

## Stance-Check assessment (dedicated paragraph)

**The Stance Check appears to have worked.** It read as genuine divergent thinking, not ceremony, and the evidence is in the *shape* of the alternative and the *specificity* of the why-nots. First, the Prevent-first alternative in Question 2 is not a paragraph of "we could also do OCR" — it sketches a full alternative architecture: camera as the front door of the diagnostics home, review-screen checklist of extracted tests with alias resolution baked in, search demoted to a secondary path, an in-search interrupt when an ambiguous term is typed, and named investment areas (OCR accuracy on Indian handwriting, alias dictionary, correction UI). That is what a genuinely-explored alternative looks like. Second, the why-nots in Question 3 identify substantive, non-symmetric reasons: Prevent fails as primary because it depends on an OCR + alias-dictionary bet that is a quarter-plus of engineering and content, with unproven adoption for users already comfortable typing; Recover fails as primary because it cannot save the "confident-but-wrong" user — the one who is sure "Urine R" and "Urine Routine" must be the same test and taps BOOK without hesitation. That "confident-but-wrong" insight is *only* surfaced when you actually think about who each stance can and cannot help. If the Stance Check were ceremony, it would produce a shallow trio of "Prevent is harder, Recover is later, so Assist" without the observation that Recover has a structural blindspot. The Stance Check produced a real reason to pick Assist, not a rationalisation. **Verdict: working as intended.**

The one thing to watch: the check produced two stances explored deeply (Assist chosen, Prevent alternative sketched), but Recover's alternative-form was never separately sketched — only justified against. A stricter reading of the spec would ask for both alternatives to be sketched. Consider tightening the subskill copy to require the sketch, not just the rebuttal.

---

## Report card

```
╔══════════════════════════════════════════════════╗
║            UX EVAL REPORT CARD                   ║
║            Agent Evil — v1.0                     ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  OVERALL SCORE:  65/78  ( 83%  · Grade: B )      ║
║  (26 N/A points removed from 104 max)            ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  GATE SCORES                                     ║
║                                                  ║
║  1 · The Problem      ⚠️  HUMAN REVIEW  (Match)  ║
║  2 · The Solution     13/18  ( 72% )             ║
║  3 · Subtract         15/17  ( 88% )             ║
║  4 · Consistency      24/28  ( 86% )             ║
║  5 · Fundamentals     13/15  ( 87% )             ║
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
║        Spec inline states for zero-results,      ║
║        network failure on chip filter, OCR       ║
║        failure, and illegible-prescription       ║
║        fallback. Currently only edge cases       ║
║        acknowledge these paths.                  ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  LOW RATINGS (every score ≤ 2)                   ║
║                                                  ║
║  (none — the lowest rated score is 3/5 at 2.5    ║
║   and 5.15; both are notes-for-next-artifact,    ║
║   not gate-blockers.)                            ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  INSIGHTS                                        ║
║                                                  ║
║  Strongest gate:  Gate 3 (Subtract) — 88%.       ║
║   Copy is patient-facing and lean; the alias     ║
║   consolidation eliminates duplicate cards; the  ║
║   Scan-Rx staging is honest about phasing.       ║
║                                                  ║
║  Weakest gate:    Gate 2 (The Solution) — 72%.   ║
║   Mainline error states (zero-results,           ║
║   network, OCR-fail) are unspec'd; the           ║
║   contrast-line copy assumes clinical            ║
║   literacy the marginal user does not have.      ║
║                                                  ║
║  Biggest risk:    The recommendation punts the   ║
║   layout tradeoffs (chip row eating fold space;  ║
║   rescue strip competing with BOOK) to the       ║
║   wireframe stage — honest, but real answers     ║
║   only surface when drawn.                       ║
║                                                  ║
║  Quick wins:                                     ║
║   1. Standardise "Scan prescription" as the      ║
║      one user-facing label; delete "Scan Rx" /   ║
║      "scan it" / "Upload prescription to         ║
║      verify" variants from the copy table.       ║
║   2. Rewrite the contrast lines in outcome       ║
║      language (screens vs. confirms bacteria,    ║
║      not "identifies" bacteria).                 ║
║   3. Add a one-line zero-results state to        ║
║      the copy table before the wireframe        ║
║      pass.                                       ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  ITEMS FOR HUMAN REVIEW                          ║
║                                                  ║
║  Gate 1: Alignment = Match. Validate whether     ║
║   "correct SKU booked" is truly the leverage     ║
║   metric, and whether partner-lab SKU            ║
║   distinctness is a real constraint.             ║
║                                                  ║
║  Gate 2 flags:                                   ║
║   — Can a first-time user reach the correct      ║
║     SKU without help? (Real testing.)            ║
║   — Will low-literacy users recognise R/E and    ║
║     C/S on the chip row?                         ║
║                                                  ║
║  Gate 3 flags:                                   ║
║   — Does "Other" chip earn its place in v1 or    ║
║     dilute the primaries?                        ║
║   — Is catalog consolidation the real fix, with  ║
║     this UI as the fallback?                     ║
║                                                  ║
║  Gate 5 flags:                                   ║
║   — Wireframe pass must audit contrast on the    ║
║     alias subline, touch-target on chips at      ║
║     360px, and SR ordering of rescue strip vs    ║
║     BOOK.                                        ║
║                                                  ║
║  Gate 6 flags:                                   ║
║   — Prescription upload needs a data-handling    ║
║     notice at the point of collection.           ║
║   — Does the rescue strip feel reassuring or     ║
║     patronising? Tonal call.                     ║
║   — Is Scan-Rx an honest CTA in v1 given OCR     ║
║     is phase-2?                                  ║
║                                                  ║
║  Gate 7 (Innovation):                            ║
║   — Was a third stance (post-book correction     ║
║     grace window) considered?                    ║
║   — Is the "translate paper to SKU" reframe      ║
║     novel for 1mg or already-converged?          ║
║                                                  ║
║  Gate 8 (Gut):                                   ║
║   — Do you buy the "confident-but-wrong" user    ║
║     as real and material?                        ║
║   — Should catalog fix lead the recommendation   ║
║     over UI fix?                                 ║
║   — Have you seen this pattern succeed or fail   ║
║     in Practo / Netmeds / Tata 1mg Meds?         ║
║                                                  ║
╠══════════════════════════════════════════════════╣
║                                                  ║
║  TERMINOLOGY ISSUES                              ║
║                                                  ║
║  1. "Scan Rx" / "Scan your prescription" /       ║
║     "scan it" / "Upload prescription to verify"  ║
║     — four phrasings for one action. Collapse    ║
║     all user-facing copy to "Scan prescription". ║
║     Keep "Scan-Rx" only in internal design       ║
║     language.                                    ║
║  2. "Alias" is internal only — never leak into   ║
║     user copy. "Commonly written as" is the      ║
║     user-facing phrase. (Discipline is currently ║
║     good; keep it.)                              ║
║  3. "Similar tests" (user copy) vs                ║
║     "commonly-confused neighbours" (design copy) ║
║     — split is fine; enforce it.                 ║
║                                                  ║
║  ACCESSIBILITY FAILURES                          ║
║                                                  ║
║  None evaluable at brief stage — all 13 binary   ║
║  accessibility checks N/A. Flags for wireframe:  ║
║   [minor] audit contrast on alias subline        ║
║   [major] audit touch-target on chip row at      ║
║           <360px viewports                       ║
║   [major] audit screen-reader ordering of PDP    ║
║           rescue strip vs BOOK button            ║
║   [minor] "Other" chip is a generic label —      ║
║           consider "Something else" for SR       ║
║           clarity                                ║
║                                                  ║
║  COPY REWRITES                                   ║
║                                                  ║
║  Before → After                                  ║
║                                                  ║
║  "Different from Culture — this test does not    ║
║   identify bacteria."                            ║
║    → "Different from Culture — this one screens; ║
║       it doesn't confirm which bacteria."        ║
║                                                  ║
║  "Not sure — see similar tests"                  ║
║    → "Not sure — show similar"                   ║
║                                                  ║
║  "Have a prescription? Scan it and we'll find    ║
║   your tests."                                   ║
║    → "Have a prescription? Scan it — we'll find  ║
║       every test."                               ║
║                                                  ║
║  "Upload prescription to verify" (PDP CTA)       ║
║    → "Scan prescription"                         ║
║                                                  ║
║  Chip label "Other"                              ║
║    → "Something else"                            ║
║                                                  ║
║  Add: SRP zero-results state (missing)           ║
║    → "No exact match. Try 'urine routine' or     ║
║       'urine culture' — or scan your             ║
║       prescription."                             ║
║                                                  ║
║  Add: OCR-failure state (missing)                ║
║    → "Couldn't read the handwriting. Try again,  ║
║       or type the test name."                    ║
║                                                  ║
╚══════════════════════════════════════════════════╝
```

**One-sentence honest summary:** A tight, well-reasoned upstream brief that reframes an ambiguous-search task as a translation task, does the divergent-thinking work the Stance Check demands, and defers the hardest visual tradeoffs to the wireframe stage where they belong — B grade because it is stronger in strategy than in the mainline error and edge-state completeness that a downstream artifact will have to fill in.
