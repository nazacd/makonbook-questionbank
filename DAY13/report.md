# DAY13 AI review

Test ids DAY13: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 37 | 17 | 0 | 54 |
| Math | 37 | 7 | 0 | 44 |
| **Total** | **74** | **24** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 31.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 18
- transcription medium: 5
- content: typo: 4
- content: other: 2
- content: image_text_mismatch: 2
- content: missing_info: 2
- solver disagrees with the key: 2
- content: grammar: 1
- content: off_format: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 0, with the final key on 0; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 85, medium 13, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 93, medium 5, low 0.
- Question and choice images: 23; kept as figures 5 (graph 4, scatterplot 1), the rest turned into text.
- Upscaled for the models: 23.

## Explanations

- Bank explanation: usable 63, minor_issue 24, wrong 6, mismatch 2, missing 3.
- Final: drafted 53, kept from the bank 45.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 561,216 | $1.57 |
| solve_a | opus | 10 | 520,254 | $2.91 |
| solve_b | sonnet | 10 | 518,611 | $1.45 |
| explain | sonnet | 10 | 692,353 | $1.94 |
| adjudicate | opus | 6 | 389,906 | $2.18 |
| **Subagents** | | 46 | **2,682,340** | **$10.06** |

Per question ≈ 27,370 tokens, ≈ $0.103 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #20 (csv 438)** (yellow, no change, high): No change needed: the accepted list we hold is already ["0.34", ".34"] (the wrong "1/3" is gone), and the stem is clear with the right key.
- **Math M1 #21 (csv 439)** (yellow, corrected, high): Corrected "values of z" to "values of x" so it matches the table header in the original, and added the missing period after the point.
- **Math M2 #1 (csv 441)** (yellow, no change, high): No change needed: the graph is readable (zero at x = -5, asymptotes x = 1 and y = -1, matching f(x) = -1 + 6/(1 - x)) and the stem's alt text already describes it correctly.
- **Math M2 #9 (csv 450)** (yellow, corrected, high): Corrected the typo "possible values of a" to "possible values of x", the variable used everywhere else.
- **Math M2 #11 (csv 452)** (yellow, corrected, high): Corrected "a atm" to \(x\) atm (and set y as math), added the dropped percent signs on 34, 22 and 48, and fixed "oxygen- nitrogen".
- **Math M2 #17 (csv 458)** (yellow, corrected, high): Fixed three transcription typos in the stem: "a minutes" to \(x\) minutes, "my-plane" to \(xy\)-plane, and "x- intercept" to \(x\)-intercept.
- **Math M2 #20 (csv 461)** (yellow, no change, high): No change needed: the review found no issues, the transcription matches the bank, and the key is right.
- **R&W M1 #3 (csv 542)** (yellow, corrected, restored, high): Restored the missing words "the" before "probability" and "as the" before "finding", and added the final period.
- **R&W M1 #7 (csv 546)** (yellow, restored, high): Restored the underline on the two italic challenges, which the stem refers to as the underlined portion and the bank explanation identifies.
- **R&W M1 #14 (csv 553)** (yellow, corrected, high): Changed the first data column header from "1995" to "1950" to match the table title and the passage (the original screenshot has the same slip in its header).
- **R&W M1 #20 (csv 559)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the question is clear and B is the only correct choice.
- **R&W M1 #21 (csv 560)** (yellow, no change, high): No change needed: the question is clear, the key is right, and the explanation already gives the correct reasoning for each choice.
- **R&W M1 #23 (csv 562)** (yellow, corrected, invented, high): Restored the missing article 'A' in choice B and replaced choice D, which only repeated the stem, with a new distractor that states only the 2021 conclusion; rewrote the explanation to cover D.
- **R&W M2 #6 (csv 572)** (yellow, restored, corrected, high): Restored the cut-off end of Text 2 ('individuals don't matter much.'), replaced the '---' with an em dash, and italicized the book titles.
- **R&W M2 #8 (csv 574)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the question is clear and B is the only supported main idea.
- **R&W M2 #11 (csv 577)** (yellow, corrected, high): Removed the stray fragment "Early snow melt reduces the amount of soil moisture available for the" that had been spliced into the passage from choice A.
- **R&W M2 #12 (csv 578)** (yellow, corrected, high): Removed the stray words "about household" from the first sentence.
- **R&W M2 #14 (csv 580)** (yellow, corrected, high): Content is correct; only the blank was changed from five to the standard six underscores.
- **R&W M2 #17 (csv 583)** (yellow, corrected, high): The question and key are right (a solver's C fails because "what" is already the object of "for"); only the blank was changed from five to the standard six underscores.
- **R&W M2 #18 (csv 584)** (yellow, corrected, high): Added the missing space after the period in choice C and changed the blank to the standard six underscores.
- **R&W M2 #20 (csv 586)** (yellow, no change, high): No change needed: one solver preferred the comma, but the text after the blank is a complete independent clause (the whereas clause is subordinate), so only the colon avoids a comma splice and the key A is right.
- **R&W M2 #23 (csv 589)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the question is clear and the regional figures confirm the claim about the region, so 'Indeed' is the key.
- **R&W M2 #24 (csv 590)** (yellow, no change, high): No change needed: the question is clear and naming the course to reflect Nazareth's view is an action taken toward that end, so the key B is right.
- **R&W M2 #26 (csv 592)** (yellow, restored, high): Restored the standard SAT introduction line before the notes, since the stem refers to 'the student' and the notes had no lead-in; the key D is right.
