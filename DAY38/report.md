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
