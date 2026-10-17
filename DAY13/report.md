# DAY13 AI review

Test ids DAY13: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 37 | 17 | 0 | 54 |
| Math | 37 | 7 | 0 | 44 |
| **Total** | **74** | **24** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 31.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 18
- transcription medium: 5
- content: typo: 4
- content: other: 2
- content: image_text_mismatch: 2
- content: missing_info: 2
- solver disagrees with the key: 2
- content: grammar: 1
- content: off_format: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 0, with the final key on 0; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 85, medium 13, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 93, medium 5, low 0.
- Question and choice images: 23; kept as figures 5 (graph 4, scatterplot 1), the rest turned into text.
- Upscaled for the models: 23.

## Explanations

- Bank explanation: usable 63, minor_issue 24, wrong 6, mismatch 2, missing 3.
- Final: drafted 53, kept from the bank 45.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 561,216 | $1.57 |
| solve_a | opus | 10 | 520,254 | $2.91 |
| solve_b | sonnet | 10 | 518,611 | $1.45 |
| explain | sonnet | 10 | 692,353 | $1.94 |
| adjudicate | opus | 6 | 389,906 | $2.18 |
| **Subagents** | | 46 | **2,682,340** | **$10.06** |

Per question ≈ 27,370 tokens, ≈ $0.103 at API list prices (90/10 input/output split assumed; the main session is not included).
