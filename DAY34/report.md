# DAY34 AI review

Test ids DAY34: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 42 | 11 | 1 | 54 |
| Math | 38 | 4 | 2 | 44 |
| **Total** | **80** | **15** | **3** | **98** |

Verdicts: key_correct 95, broken 3. Adjudicated: 21.

## Red: a teacher decides before publishing

- **Math M1 #15 (csv 1529)**: broken. As printed (and matching the bank CSV), y = x^2 and y = 8x + 16 give x = 4 ± 4√2, so no choice is correct and key C fails; the intended equation is unclear (x^2 + y + 3 = 3 would give B, not C), so a teacher must fix the question.
- **Math M2 #6 (csv 1542)**: broken. The original images confirm the stem has +3t while choice B has -3t, so the difference 4t^4 + 4t^3 - 9t^2 + 3t matches no choice; changing the stem's +3t to -3t makes B correct and keeps choice A's -3t distractor consistent.
- **R&W M2 #16 (csv 1898)**: broken. The bank's own passage has a semicolon after the blank, so key C yields ";;" and only A fits as printed; the semicolon is almost certainly an error, and removing it restores the intended key C (comma before the parenthetical "for example", semicolon joining the two independent clauses).

## Yellow

- solver medium: 9
- transcription medium: 4
- solver disagrees with the key: 2
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 93, medium 3, low 2.
- solve_b (sonnet): disagrees with the bank key on 5, with the final key on 5; confidence high 91, medium 6, low 1.
- Both disagree with the bank key: 2 (Math M1 #15 (csv 1529); Math M2 #6 (csv 1542)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 94, medium 4, low 0.
- Question and choice images: 129; kept as figures 10 (graph 6, geometry 3, scatterplot 1), the rest turned into text.
- Upscaled for the models: 125.

## Explanations

- Bank explanation: usable 64, minor_issue 15, wrong 8, mismatch 5, missing 6.
- Final: drafted 49, kept from the bank 49.

## Usage

Not logged.
