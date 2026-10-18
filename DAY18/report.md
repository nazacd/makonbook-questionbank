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
