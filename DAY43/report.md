# DAY43 AI review

Test ids DAY43: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 7 | 1 | 54 |
| Math | 38 | 6 | 0 | 44 |
| **Total** | **84** | **13** | **1** | **98** |

Verdicts: key_correct 97, key_wrong 1. Adjudicated: 15.

## Red: a teacher decides before publishing

- **R&W M2 #15 (csv 2437)**: key_wrong. Key A → D. Key A contradicts the text, which says recognition was restricted to muralists, so muralists did not lack recognition; D is the only choice that explains both Valdez and Sandoval, and both solvers chose it with high confidence.

## Yellow

- solver medium: 12
- transcription medium: 3
- solver disagrees with the key: 3
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 3; confidence high 91, medium 7, low 0.
- Both disagree with the bank key: 1 (R&W M2 #15 (csv 2437)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 122; kept as figures 10 (graph 6, chart 2, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 113.

## Explanations

- Bank explanation: usable 79, minor_issue 11, wrong 6, mismatch 1, missing 1.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 780,641 | $2.19 |
| solve_a | opus | 10 | 701,229 | $3.93 |
| solve_b | sonnet | 10 | 700,609 | $1.96 |
| explain | sonnet | 10 | 799,670 | $2.24 |
| adjudicate | opus | 3 | 241,438 | $1.35 |
| **Subagents** | | 43 | **3,223,587** | **$11.67** |

Per question ≈ 32,893 tokens, ≈ $0.119 at API list prices (90/10 input/output split assumed; the main session is not included).
