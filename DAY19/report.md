# DAY19 AI review

Test ids DAY19: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 48 | 5 | 1 | 54 |
| Math | 42 | 2 | 0 | 44 |
| **Total** | **90** | **7** | **1** | **98** |

Verdicts: key_correct 98. Adjudicated: 12.

## Red: a teacher decides before publishing

- **R&W M1 #13 (csv 1011)**: key_correct. Key C is correct because the graph shows all three classes rising from 1986 to 2000 while A, B and D misstate or ignore change over time; the cropped sentence is a real defect but is downgraded to content since the assertion to complete is fully given, and the off_format issue is dropped as a duplicate of the crop.

## Yellow

- solver medium: 6
- transcription medium: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 0, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 1, with the final key on 1; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 96, medium 1, low 1.
- Question and choice images: 92; kept as figures 4 (graph 4), the rest turned into text.
- Upscaled for the models: 57.

## Explanations

- Bank explanation: usable 72, minor_issue 20, wrong 4, mismatch 2, missing 0.
- Final: drafted 48, kept from the bank 50.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 601,342 | $1.68 |
| solve_a | opus | 10 | 521,917 | $2.92 |
| solve_b | sonnet | 10 | 520,776 | $1.46 |
| explain | sonnet | 10 | 638,439 | $1.79 |
| adjudicate | opus | 2 | 135,736 | $0.76 |
| **Subagents** | | 42 | **2,418,210** | **$8.61** |

Per question ≈ 24,675 tokens, ≈ $0.088 at API list prices (90/10 input/output split assumed; the main session is not included).
