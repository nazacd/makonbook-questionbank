# DAY18 AI review

Test ids DAY18: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 7 | 1 | 54 |
| Math | 39 | 5 | 0 | 44 |
| **Total** | **85** | **12** | **1** | **98** |

Verdicts: key_correct 97, key_wrong 1. Adjudicated: 16.

## Red: a teacher decides before publishing

- **R&W M1 #12 (csv 863)**: key_wrong. Key B → A. Key B (colonies with both bacteria) would undercut the conclusion that neither bacterium mattered, so the key is wrong and A is the only choice that supports it; the drafted explanation already explains A.

## Yellow

- solver medium: 6
- solver disagrees with the key: 5
- transcription medium: 2
- content: image_text_mismatch: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 5; confidence high 94, medium 4, low 0.
- Both disagree with the bank key: 1 (R&W M1 #12 (csv 863)).
- The two solvers disagree with each other: 5.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 50; kept as figures 3 (scatterplot 1, graph 1, geometry 1), the rest turned into text.
- Upscaled for the models: 37.

## Explanations

- Bank explanation: usable 70, minor_issue 19, wrong 8, mismatch 1, missing 0.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 577,527 | $1.62 |
| solve_a | opus | 10 | 519,741 | $2.91 |
| solve_b | sonnet | 10 | 519,949 | $1.46 |
| explain | sonnet | 10 | 618,797 | $1.73 |
| adjudicate | opus | 3 | 185,250 | $1.04 |
| **Subagents** | | 43 | **2,421,264** | **$8.75** |

Per question ≈ 24,706 tokens, ≈ $0.089 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

english-m1-20 had identical choice text in the source row (duplicate_choice flagged by prep); no other issues.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #18 (csv 860)** (yellow, no change, high): No change needed: our stem already reads "The graph of \(y = f(x) - 9\)" (the missing y was only in the old CSV text), the graph is readable, and the key is right.
- **Math M1 #22 (csv 864)** (yellow, corrected, high): Corrected the typo "postive" to "positive" in the stem; nothing else changed.
- **Math M2 #6 (csv 870)** (yellow, no change, high): No change needed: the four pipe tables match the choice images exactly, and only one table satisfies the inequality in every row.
- **Math M2 #10 (csv 874)** (yellow, no change, high): No change needed: the image-text mismatch was in the old CSV text ("Choose the correct option."); our stem is a faithful transcription of the image, and key D is right.
- **Math M2 #22 (csv 886)** (yellow, invented, high): Choice D read only "x + w", which is not a statement; completed it as the false distractor "x + w = 180" (most likely the lost original) and rewrote the explanation, which said D was not a comparison.
- **R&W M1 #12 (csv 863)** (red, corrected, high): Set the key to A per the key_wrong verdict (the bank's B, colonies with both bacteria, contradicts the conclusion), fixed the misspelled genus "Crocebacter" to "Croceibacter", and wrote the explanation for A as a change since the answer changed.
- **R&W M1 #20 (csv 871)** (yellow, corrected, high): Choice C's capital "Considering" shows a period was dropped in transcription, so C is restored as "surroundings, though. Considering", a real distractor that leaves a fragment instead of a near-duplicate of A.
- **R&W M1 #26 (csv 877)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the notes and choices are clear and C is the only choice that states a difference between the two birds.
- **R&W M2 #12 (csv 900)** (yellow, no change, high): No change needed: the second solver's C is weaker because which hand is used says nothing about the direction of a gesture, while B shows Yupno time tied to the real slope rather than to an imagined axis around the speaker.
- **R&W M2 #18 (csv 926)** (yellow, no change, high): No change needed: the second solver disagreed, but "the djeser and heqat have since fallen out of use" is an independent clause, so only the period in C avoids a comma splice or run-on.
- **R&W M2 #19 (csv 927)** (yellow, corrected, high): Removed the stray period after the blank ("is ______. Proto-Atlantic-Congo"): every choice supplies its own end punctuation, and with the period A read "however;." while C ("hypothetical, however.") became correct, which is likely why the solver disagreed.
- **R&W M2 #21 (csv 929)** (yellow, corrected, high): Changed choice D's straight quotation mark to a curly one to match the passage and the other choices, italicized the album title Low Blow as SAT style does, and reworded the explanation's line for D so it no longer nests quotation marks.
- **R&W M2 #22 (csv 930)** (yellow, no change, high): No change needed: the solver disagreed with the key, but the text is clean and D is right, since the previous sentence already makes the contrast ("this wasn’t the case with all elements") and "Sometimes" introduces the cases where isolation took years.
