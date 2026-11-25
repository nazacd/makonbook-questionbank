# DAY38 AI review

Test ids DAY38: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 43 | 11 | 0 | 54 |
| Math | 38 | 5 | 1 | 44 |
| **Total** | **81** | **16** | **1** | **98** |

Verdicts: key_correct 97, broken 1. Adjudicated: 18.

## Red: a teacher decides before publishing

- **Math M1 #4 (csv 1607)**: broken. Broken: the bank has no question text or image, only four factorizations, so the key D cannot be checked; the three duplicate missing_info issues are merged into one.

## Yellow

- solver medium: 15
- transcription medium: 3
- content: other: 1
- content: typo: 1
- solver disagrees with the key: 1
- content: choice_formatting: 1
- solver low: 1
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 92, medium 5, low 1.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 86, medium 10, low 2.
- Both disagree with the bank key: 1 (Math M1 #4 (csv 1607)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 94, medium 3, low 1.
- Question and choice images: 65; kept as figures 8 (graph 3, geometry 3, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 64.

## Explanations

- Bank explanation: usable 68, minor_issue 20, wrong 8, mismatch 0, missing 2.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 783,812 | $2.19 |
| solve_a | opus | 10 | 731,884 | $4.10 |
| solve_b | sonnet | 10 | 727,149 | $2.04 |
| explain | sonnet | 10 | 835,717 | $2.34 |
| adjudicate | opus | 3 | 255,800 | $1.43 |
| **Subagents** | | 43 | **3,334,362** | **$12.10** |

Per question ≈ 34,024 tokens, ≈ $0.123 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

math-m1-04 has no question text and no image in the bank row (blocking, flagged in the report).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #2 (csv 1605)** (yellow, no change, high): No change needed: the graph clearly crosses the y-axis at y = 9 (6 is only the horizontal asymptote), and the stem, choices and key D match the original.
- **Math M1 #4 (csv 1607)** (red, invented, medium): The stem was missing entirely, so I wrote the factoring stem the choices and key imply: 11x^2 - 1,100y^2. **A person must:** The bank has no stem for this question; the stem was reconstructed from the choices and key. Check it against the source if available.
- **Math M1 #17 (csv 1620)** (yellow, no change, high): No change needed: the accepted list already holds both solutions, 5 and 6, and the explanation says either is correct.
- **Math M2 #3 (csv 1628)** (yellow, restored, high): Restored the missing word "What" at the start of the final question sentence.
- **Math M2 #11 (csv 1641)** (yellow, redrawn, high): Redrew the graph because the original is cropped at the top (y-axis end and label cut off); the line runs from (0, 135) to (156, 0) as in the original and as the answer choices require.
- **Math M2 #21 (csv 1651)** (yellow, no change, high): No change needed: the stem and both equations match the original screenshot exactly, and the key is right.
- **R&W M1 #15 (csv 2054)** (yellow, no change, medium): No change needed: the solvers were unsure, but the text presents 10.5% chromium as the ferritic threshold that austenitic steel falls below, and only A follows.
- **R&W M1 #19 (csv 2060)** (yellow, no change, high): No change needed: one solver chose the comma splice, but the question is clear and key D is correct.
- **R&W M1 #21 (csv 2063)** (yellow, no change, high): No change needed: the solver was unsure, but the cause-effect link from extensive research to the book's reputation makes B the only fit.
- **R&W M2 #3 (csv 2076)** (yellow, corrected, high): Added the missing article "a" to choices A and C so every choice fits "largely ______ of the fact" grammatically, as B and D already do.
- **R&W M2 #7 (csv 2080)** (yellow, no change, high): No change needed: the passage matches the screenshot word for word and the question is clear; the solver's medium confidence does not reflect a defect.
- **R&W M2 #10 (csv 2085)** (yellow, no change, high): No change needed: the text, stem and choices are complete and consistent, and the key is right.
- **R&W M2 #12 (csv 2088)** (yellow, no change, medium): No change needed: the graph is legible and matches the description, the stem is complete, and the explanation already supports key C.
- **R&W M2 #13 (csv 2096)** (yellow, restored, corrected, high): Restored the passage (missing from the bank, transcribed from the screenshot with the underlined claim) and italicized the novel title in the choices to match the passage.
- **R&W M2 #20 (csv 2106)** (yellow, no change, high): No change needed: the sentence and choices are clear, and the explanation already describes every choice correctly.
- **R&W M2 #21 (csv 2107)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and key A is right because "Spain" is a restrictive appositive after "fellow OECD member nation" and takes no punctuation.
- **R&W M2 #23 (csv 2109)** (yellow, no change, high): No change needed: the solvers were unsure, but the question is clear and key D is right because "Then" (at that time, in 1986) introduces what replaced the retired ticker tape.
