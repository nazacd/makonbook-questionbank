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
