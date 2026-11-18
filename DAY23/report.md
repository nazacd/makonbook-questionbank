# DAY23 AI review

Test ids DAY23: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 36 | 14 | 4 | 54 |
| Math | 40 | 4 | 0 | 44 |
| **Total** | **76** | **18** | **4** | **98** |

Verdicts: key_correct 94, ambiguous 4. Adjudicated: 26.

## Red: a teacher decides before publishing

- **R&W M1 #24 (csv 1248)**: ambiguous. Ambiguous: both C (kin selection improves relatives' survival) and B (group work better ensured survival) state an evolutionary advantage of eusociality, and the solvers split at medium confidence, so a teacher should decide.
- **R&W M2 #14 (csv 1265)**: ambiguous. Ambiguous: both solvers chose A, which expresses regret over his dishonesty at least as well as keyed C, whose line is about keeping his name, but a literary-interpretation dispute cannot be proved, so a teacher should decide.
- **R&W M2 #15 (csv 1266)**: ambiguous. Ambiguous: every choice is accurate to the table and the cue "intrigued" supports B while the demonstration aim supports D, so nothing singles out one answer; the two duplicate ambiguity issues were merged and the bank explanation's misquoted numbers need a teacher rewrite once a key is chosen.
- **R&W M2 #20 (csv 1271)**: ambiguous. Ambiguous: a period and a colon are both standard between these two independent clauses, and the solvers split with medium confidence, so keyed B cannot be proven unique or wrong.

## Yellow

- solver medium: 18
- content: ambiguous: 2
- content: grammar: 2
- content: other: 1
- solver disagrees with the key: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 3; confidence high 88, medium 10, low 0.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 83, medium 15, low 0.
- Both disagree with the bank key: 1 (R&W M2 #14 (csv 1265)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 122; kept as figures 8 (graph 5, geometry 1, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 91.

## Explanations

- Bank explanation: usable 66, minor_issue 25, wrong 7, mismatch 0, missing 0.
- Final: drafted 48, kept from the bank 50.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 837,404 | $2.34 |
| solve_a | opus | 10 | 739,166 | $4.14 |
| solve_b | sonnet | 10 | 731,345 | $2.05 |
| explain | sonnet | 10 | 885,281 | $2.48 |
| adjudicate | opus | 5 | 432,456 | $2.42 |
| **Subagents** | | 45 | **3,625,652** | **$13.43** |

Per question ≈ 36,996 tokens, ≈ $0.137 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #3 (csv 936)** (yellow, corrected, high): Removed the repeated opening sentence and stated the full vertex correspondence, since A corresponding to D alone does not fix whether B matches E or F.
- **Math M1 #8 (csv 941)** (yellow, invented, corrected, high): Made x a time in seconds instead of ounces drunk, because "ounces consumed per ounce drank" is self-contradictory (and "drank" is ungrammatical); the slope 0.03 is now the drinking rate.
- **Math M2 #4 (csv 970)** (yellow, redrawn, corrected, high): Redrew the graph with the x-axis labeled Day (the question says 7 days, the original said Year) and fixed the "platic" typo; the stem now names the unit kilograms.
- **Math M2 #17 (csv 983)** (yellow, corrected, high): Added the missing words "of x for which" so the stem asks for the x-intercept; the graph is clear and unchanged.
- **R&W M1 #8 (csv 1232)** (yellow, restored, high): Restored Montgomery's "that that simple little prayer", which the bank's screenshot also dropped, so the sentence reads correctly.
- **R&W M1 #9 (csv 1233)** (yellow, restored, high): Rewrote the garbled sentence in Text 2 (garbled in the original screenshot too) so it says what the context requires: people who must work full-time lack the time for the extensive practice poetry needs; the Text 1/Text 2 labels already follow our format.
- **R&W M1 #11 (csv 1235)** (yellow, corrected, high): Removed the stray extra noun in choice A ("varying abilities traits" to "varying traits").
- **R&W M1 #15 (csv 1239)** (yellow, corrected, high): Choice A now uses the full name Vinson Cunningham, since he is never introduced and the other choices all use his full name.
- **R&W M1 #22 (csv 1246)** (yellow, corrected, high): Fixed "classical musical" to "classical musicians" (parallel to "jazz composers and musicians") and "symbols" to "cymbals", and gave choices A and C the trailing comma that B and D have.
- **R&W M1 #24 (csv 1248)** (red, invented, high): Choice B also stated a survival advantage that explained eusociality's evolution, so it competed with key C; replaced B with a descriptive distractor built from the first two notes so only C states evolutionary value.
- **R&W M1 #26 (csv 1250)** (yellow, no change, high): No change: the notes match the screenshot, and A is the only choice that stays on urban-planning features (sewage and drainage systems, standardized weights and measures); C dilutes the goal with the decline and D centers on artifacts, so the solvers' uncertainty does not reflect a flaw.
- **R&W M2 #5 (csv 1256)** (yellow, corrected, high): Fixed grammar: added the missing "are" in the passage, capitalized choice A, and made choice D grammatical ("suggests that, like falcons and horses, cuttlefish"); explanation updated to quote the new D.
- **R&W M2 #6 (csv 1257)** (yellow, no change, high): No change: the transcription matches the screenshot, and D is clearly the main idea since Victor stresses that even the most learned philosophers left causes unknown and that he repined at these barriers.
- **R&W M2 #9 (csv 1260)** (yellow, no change, high): No change: the paired texts match the screenshot and A clearly captures Text 2's point that size and water density limit interaction, which the conventional view overlooks.
- **R&W M2 #11 (csv 1262)** (yellow, no change, medium): No change: the question is clear and C is the only finding in which the pop-music group outperforms the complex-music group on the problem-solving test, which weakens the claim.
- **R&W M2 #13 (csv 1264)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the claim is clear and only C shows the professor adjusting (contrasting his library and lecture hall with the rural 'wilderness').
- **R&W M2 #14 (csv 1265)** (red, invented, corrected, high): Rewrote the claim from 'expresses profound regret' (which choice A fits at least as well as C) to 'comes to value his good name more than his own life', which only C shows, and corrected D's speaker and listener (Proctor says it to Danforth about Abigail).
- **R&W M2 #15 (csv 1266)** (red, invented, corrected, medium): Replaced the vague 'was intrigued to find that' (which could point to the roses in B) with a stated claim about compost beneficiaries, so only D uses the data for both beneficiaries; added the missing 'a' in D; the table already matches the screenshot.
- **R&W M2 #17 (csv 1268)** (yellow, corrected, high): Restored the dropped 'B.' at the start of choice B and the dropped 'A' at the start of choice D.
- **R&W M2 #20 (csv 1271)** (red, invented, high): Choice D (a period) was as correct as keyed B (a colon), so D was replaced with an invented distractor that puts an incorrect comma between the verb and its object.
- **R&W M2 #23 (csv 1274)** (yellow, corrected, high): The question is clear and key D is right; only the explanation was rewritten to remove a stray line about another question ("22C and 23D") and to follow the format.
- **R&W M2 #25 (csv 1276)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and key B is right.
