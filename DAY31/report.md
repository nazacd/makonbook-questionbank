# DAY31 AI review

Test ids DAY31: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 43 | 9 | 2 | 54 |
| Math | 40 | 3 | 1 | 44 |
| **Total** | **83** | **12** | **3** | **98** |

Verdicts: key_correct 95, broken 1, ambiguous 1, key_wrong 1. Adjudicated: 24.

## Red: a teacher decides before publishing

- **Math M1 #10 (csv 1384)**: broken. The original image itself prints y = 13 at x = 1, which contradicts y = 4(x^2) + 5 (it should be 9), so the printed data is defective; the intended answer is still D (41), and the fix changes 13 to 9.
- **R&W M2 #14 (csv 1735)**: ambiguous. Key B looks wrong (raising the trade threshold would worsen, not relieve, a crisis caused by coins under 80% silver, while A raises silver percentage at no extra silver cost), but the solvers split at medium confidence, so it goes to a teacher with a proposed key change to A.
- **R&W M2 #27 (csv 1748)**: key_wrong. Key D → C. Key D is wrong because it only describes the scale ordering three named minerals; C is the only choice that generalizes (any mineral at 8 can scratch any at 5), and both solvers independently chose C.

## Yellow

- solver medium: 8
- solver disagrees with the key: 4
- transcription medium: 1
- content: typo: 1
- content: grammar: 1
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 4, with the final key on 3; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 2; confidence high 90, medium 8, low 0.
- Both disagree with the bank key: 2 (R&W M2 #19 (csv 1740); R&W M2 #27 (csv 1748)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 84; kept as figures 8 (graph 6, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 82.

## Explanations

- Bank explanation: usable 68, minor_issue 17, wrong 5, mismatch 3, missing 5.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 787,967 | $2.21 |
| solve_a | opus | 10 | 723,278 | $4.05 |
| solve_b | sonnet | 10 | 721,278 | $2.02 |
| explain | sonnet | 10 | 830,542 | $2.33 |
| adjudicate | opus | 4 | 345,727 | $1.94 |
| **Subagents** | | 44 | **3,408,792** | **$12.54** |

Per question ≈ 34,783 tokens, ≈ $0.128 at API list prices (90/10 input/output split assumed; the main session is not included).
