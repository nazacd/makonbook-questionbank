# DAY37 AI review

Test ids DAY37: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 8 | 0 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **89** | **9** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 12.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 7
- solver disagrees with the key: 4
- content: choice_formatting: 2
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 96, medium 1, low 1.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 111; kept as figures 11 (geometry 4, chart 4, graph 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 101.

## Explanations

- Bank explanation: usable 67, minor_issue 22, wrong 9, mismatch 0, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 802,284 | $2.25 |
| solve_a | opus | 10 | 740,373 | $4.15 |
| solve_b | sonnet | 10 | 736,519 | $2.06 |
| explain | sonnet | 10 | 857,038 | $2.40 |
| adjudicate | opus | 1 | 84,902 | $0.48 |
| **Subagents** | | 41 | **3,221,116** | **$11.33** |

Per question ≈ 32,868 tokens, ≈ $0.116 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

An explain agent (english-m1-c) reported that it re-ran a shared scratch script and regenerated the explain output of math-m2-a from another agent's script; the content should be unchanged but a teacher may want to spot-check math-m2-a explanations.
