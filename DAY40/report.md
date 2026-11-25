# DAY40 AI review

Test ids DAY40: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 41 | 12 | 1 | 54 |
| Math | 40 | 4 | 0 | 44 |
| **Total** | **81** | **16** | **1** | **98** |

Verdicts: key_correct 97, key_wrong 1. Adjudicated: 18.

## Red: a teacher decides before publishing

- **R&W M2 #3 (csv 2231)**: key_wrong. Key A → D. Key changed to D: the street art is offered as an addition to the museum's collection, so "supplement" is the precise word, while "satisfy" implies an unmet need the text never mentions; both solvers and the explanation check agree.

## Yellow

- solver medium: 13
- transcription medium: 4
- solver disagrees with the key: 2
- content: typo: 1
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 1; confidence high 94, medium 3, low 1.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 1; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 1 (R&W M2 #3 (csv 2231)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 94, medium 4, low 0.
- Question and choice images: 84; kept as figures 10 (geometry 5, graph 3, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 75.

## Explanations

- Bank explanation: usable 76, minor_issue 17, wrong 5, mismatch 0, missing 0.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 796,185 | $2.23 |
| solve_a | opus | 10 | 735,457 | $4.12 |
| solve_b | sonnet | 10 | 727,367 | $2.04 |
| explain | sonnet | 10 | 836,787 | $2.34 |
| adjudicate | opus | 3 | 256,769 | $1.44 |
| **Subagents** | | 43 | **3,352,565** | **$12.17** |

Per question ≈ 34,209 tokens, ≈ $0.124 at API list prices (90/10 input/output split assumed; the main session is not included).
