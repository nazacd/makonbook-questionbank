# DAY41 AI review

Test ids DAY41: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 5 | 3 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **89** | **6** | **3** | **98** |

Verdicts: key_correct 95, key_wrong 2, broken 1. Adjudicated: 13.

## Red: a teacher decides before publishing

- **R&W M2 #10 (csv 2324)**: key_wrong. Key A → C. Key A is consistent with alarm communication to conspecifics, while C (solitary caterpillars making sound in isolation with no receiver) directly undercuts the communication claim, as both solvers found with high confidence.
- **R&W M2 #12 (csv 2326)**: broken. The item is garbled: the graph shows P6's correlations (about 0.43 abstract vs 0.27 cubist), but the key A contradicts the stated equal-ratings premise, C only restates it, and B/D are unsupported, so no choice works as printed.
- **R&W M2 #19 (csv 2333)**: key_wrong. Key D → B. The material after the blank is a dependent "since" clause, so any semicolon or period (A, C, D) creates a fragment; only B, with "however" set off by commas, is grammatical.

## Yellow

- solver medium: 6
- solver disagrees with the key: 2
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 1; confidence high 94, medium 2, low 2.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 3; confidence high 92, medium 5, low 1.
- Both disagree with the bank key: 2 (R&W M2 #10 (csv 2324); R&W M2 #19 (csv 2333)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 88; kept as figures 6 (graph 4, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 72.

## Explanations

- Bank explanation: usable 81, minor_issue 10, wrong 7, mismatch 0, missing 0.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 764,386 | $2.14 |
| solve_a | opus | 10 | 695,647 | $3.90 |
| solve_b | sonnet | 10 | 693,219 | $1.94 |
| explain | sonnet | 10 | 805,105 | $2.25 |
| adjudicate | opus | 3 | 231,054 | $1.29 |
| **Subagents** | | 43 | **3,189,411** | **$11.53** |

Per question ≈ 32,545 tokens, ≈ $0.118 at API list prices (90/10 input/output split assumed; the main session is not included).
