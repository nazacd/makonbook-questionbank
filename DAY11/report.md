# DAY11 AI review

Test ids DAY11: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 8 | 0 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **89** | **9** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 15.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 10
- solver disagrees with the key: 3
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 1 (R&W M2 #21 (csv 477)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 21; kept as figures 6 (graph 3, geometry 2, chart 1), the rest turned into text.
- Upscaled for the models: 18.

## Explanations

- Bank explanation: usable 64, minor_issue 22, wrong 11, mismatch 0, missing 1.
- Final: drafted 50, kept from the bank 48.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 576,481 | $1.61 |
| solve_a | opus | 10 | 536,688 | $3.01 |
| solve_b | sonnet | 10 | 534,194 | $1.50 |
| explain | sonnet | 10 | 702,771 | $1.97 |
| adjudicate | opus | 3 | 194,242 | $1.09 |
| **Subagents** | | 43 | **2,544,376** | **$9.17** |

Per question ≈ 25,963 tokens, ≈ $0.094 at API list prices (90/10 input/output split assumed; the main session is not included).
