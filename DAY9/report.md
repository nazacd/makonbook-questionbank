# DAY9 AI review

Test ids DAY9: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 6 | 2 | 54 |
| Math | 35 | 8 | 1 | 44 |
| **Total** | **81** | **14** | **3** | **98** |

Verdicts: key_correct 95, broken 1, ambiguous 1, key_wrong 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M2 #1 (csv 260)**: broken. D is the only decreasing exponential curve, but the question is defective because choices B and C use identical images; the original choice C graph must be restored by a teacher (duplicate issues merged).
- **R&W M1 #16 (csv 339)**: ambiguous. Ambiguous: the comma appositive (key D) and the colon (C, both solvers) are each grammatical because "scientists turn to stratigraphy" is a complete clause and nothing closes the inserted phrase, so neither can be proven wrong.
- **R&W M2 #16 (csv 366)**: key_wrong. Key D → C. Key D says sensitivity to warming is negatively correlated with the number of vertebrate hosts, but the data show a positive relationship, so D contradicts the text and C is the only consistent choice.

## Yellow

- solver medium: 6
- solver disagrees with the key: 4
- content: typo: 4
- transcription medium: 2
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 2; confidence high 95, medium 3, low 0.
- solve_b (sonnet): disagrees with the bank key on 5, with the final key on 4; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 2 (R&W M1 #16 (csv 339); R&W M2 #16 (csv 366)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 16; kept as figures 9 (graph 6, scatterplot 1, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 15.

## Explanations

- Bank explanation: usable 60, minor_issue 23, wrong 10, mismatch 0, missing 5.
- Final: drafted 54, kept from the bank 44.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| explain | sonnet | 10 | 641,223 | $1.80 |
| adjudicate | opus | 4 | 256,170 | $1.43 |
| **Subagents** | | 14 | **897,393** | **$3.23** |

Per question ≈ 9,157 tokens, ≈ $0.033 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Token counts for transcribe, solve_a, solve_b and adj-4 were not logged.
- 25 of 98 questions went to adjudication; several bank explanations were wrong (see report).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #1 (csv 238)** (yellow, no change, high): No change needed: the question is clear and key B is right; the flag came from a solver's addition error.
- **Math M1 #2 (csv 239)** (yellow, corrected, high): Restored the missing variable c in choice C so it reads c = 28m; c + m = 3, parallel to choice D.
- **Math M1 #4 (csv 241)** (yellow, corrected, high): Changed the variable z to x in the stem so it matches the choices, and updated the explanation to use x throughout.
- **Math M1 #7 (csv 244)** (yellow, corrected, high): Removed the stray "e" in "A line e of best fit"; the figure is clear and the key is right.
- **Math M2 #1 (csv 260)** (red, invented, redrawn, high): Choices B and C showed the same decreasing line, so I replaced C with a newly drawn increasing exponential curve (y = 4^(x-2)), the mirror of D, as a distinct distractor, and updated the explanation.
- **Math M2 #8 (csv 267)** (yellow, restored, corrected, high): Restored the cut-off "variables a, b, k, and m" and replaced the period after a with a comma; the key and explanation are already right.
- **Math M2 #14 (csv 273)** (yellow, corrected, high): Unscrambled the garbled last sentence to "What is the least possible value of a?".
- **Math M2 #16 (csv 275)** (yellow, corrected, high): Changed "increase of a by 8" to "increase of x by 8"; the function matches the original screenshot.
- **Math M2 #19 (csv 278)** (yellow, restored, high): Restored the missing "is at" in the last sentence; the table matches the original screenshot.
- **R&W M1 #16 (csv 339)** (red, restored, medium): Restored the closing comma after "(strata)" that the appositive needs, so the paired-punctuation test makes D the only answer and the colon in C no longer works.
- **R&W M2 #3 (csv 353)** (yellow, no change, high): No change needed: one solver was unsure, but the text is clean and the "but" contrast with a "first" who "will always be remembered" makes "uncertain" the only fit.
- **R&W M2 #13 (csv 363)** (yellow, corrected, high): Added the missing dash before "namely," made choice B's closing quote mark straight to match its opening, and italicized the novel titles.
- **R&W M2 #16 (csv 366)** (red, corrected, medium): Changed the key from D to C as the review found (D states the wrong direction of the relationship), hyphenated "three-host" and "two-host," added "a" to choice D, and italicized the species names, and rewrote the explanation for key C with the italicized names.
- **R&W M2 #19 (csv 1387)** (yellow, corrected, high): Fixed "si" to "is," removed the stray line breaks and added the missing space after the blank, italicized the painting title, and removed the stray period from choice C.
- **R&W M2 #20 (csv 370)** (yellow, corrected, high): Added the missing space after the period in choice D.
- **R&W M2 #21 (csv 371)** (yellow, no change, high): No change needed: the second solver was unsure, but the question is clear and key C is the only choice that avoids a comma splice.
- **R&W M2 #22 (csv 372)** (yellow, no change, high): No change needed: the second solver disagreed, but the question is clear and key C is right because "Estonia and Norway" restrictively identifies "fellow OECD nations."
