# DAY7 AI review

Test ids DAY7: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 44 | 10 | 0 | 54 |
| Math | 38 | 5 | 1 | 44 |
| **Total** | **82** | **15** | **1** | **98** |

Verdicts: key_correct 97, broken 1. Adjudicated: 17.

## Red: a teacher decides before publishing

- **Math M2 #15 (csv 230)**: broken. Broken: all four choices are blank, so key A cannot be checked, though 3x(x + 8)(x + 9) gives b = 8; the three duplicate missing_choice issues are merged into one.

## Yellow

- solver medium: 10
- transcription medium: 6
- solver disagrees with the key: 5
- content: ambiguous: 1
- content: other: 1
- content: off_format: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 3; confidence high 95, medium 2, low 1.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 89, medium 8, low 1.
- Both disagree with the bank key: 2 (Math M2 #15 (csv 230); R&W M1 #21 (csv 235)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 91, medium 7, low 0.
- Question and choice images: 21; kept as figures 7 (graph 5, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 21.

## Explanations

- Bank explanation: usable 65, minor_issue 27, wrong 5, mismatch 0, missing 1.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 564,218 | $1.58 |
| solve_a | opus | 10 | 525,483 | $2.94 |
| solve_b | sonnet | 10 | 524,194 | $1.47 |
| explain | sonnet | 10 | 692,693 | $1.94 |
| adjudicate | opus | 3 | 193,681 | $1.08 |
| **Subagents** | | 43 | **2,500,269** | **$9.01** |

Per question ≈ 25,512 tokens, ≈ $0.092 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- explain math-m2-b failed the check once (skill/domain mismatch); re-run once, then passed.
- math-m2-15 has no choices and no image in the bank (blocking missing_choice); needs a teacher.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #12 (csv 205)** (yellow, no change, high): No change needed: the transcription is clear and the key is right; the review flagged only medium transcription confidence.
- **Math M1 #15 (csv 208)** (yellow, corrected, high): Replaced the stray quote marks with degree symbols and added the missing degree unit on angle D.
- **Math M1 #22 (csv 215)** (yellow, corrected, high): Removed the stray space after the thousands comma in choices B and D so they read 4,116 and 1,728.
- **Math M2 #4 (csv 219)** (yellow, corrected, medium): Changed "distinct positive numbers" to "distinct nonzero numbers" because the equation makes v negative when w and x are positive; the display fraction already makes the denominator 159x unambiguous.
- **Math M2 #7 (csv 222)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and the key is right.
- **Math M2 #15 (csv 230)** (red, invented, high): All four choices were blank, so I wrote choices with the key value 8 at A and distractors from the factoring (the other root 9, the sum 17, the product 72).
- **R&W M1 #13 (csv 227)** (yellow, corrected, high): Restored the missing article "A" at the start of choice D.
- **R&W M1 #16 (csv 230)** (yellow, no change, high): No change needed: the transcription matches the original and the question is clear with key A correct.
- **R&W M1 #21 (csv 235)** (yellow, corrected, high): Removed the stray quotation marks around the passage and italicized the journal title Science Advances.
- **R&W M2 #6 (csv 247)** (yellow, corrected, high): The question already underlines both phrases the original marks and is clear; I only added the missing "**Answer:** C" line to the explanation.
- **R&W M2 #8 (csv 249)** (yellow, no change, high): No change needed: the stray quotation marks the review flagged are not present in the current passage, and the question is clear with A as the only main idea.
- **R&W M2 #11 (csv 252)** (yellow, no change, high): No change needed: the solver was unsure, but 'better explained' maps clearly to the traceability rating and the key is right.
- **R&W M2 #12 (csv 253)** (yellow, no change, high): No change needed: the second solver's disagreement was an error; the question is clear and key B is right.
- **R&W M2 #14 (csv 255)** (yellow, no change, high): No change needed: the question is clear and both solvers agree on key B.
- **R&W M2 #19 (csv 260)** (yellow, no change, high): No change needed: the passage already uses a six-underscore blank with no stray quotation marks, and key B is right.
- **R&W M2 #26 (csv 267)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and key C is the only choice giving a specific example (water treatment) of what municipalities provide.
