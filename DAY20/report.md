# DAY20 AI review

Test ids DAY20: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 7 | 0 | 54 |
| Math | 39 | 3 | 2 | 44 |
| **Total** | **86** | **10** | **2** | **98** |

Verdicts: key_correct 96, broken 1, ambiguous 1. Adjudicated: 14.

## Red: a teacher decides before publishing

- **Math M2 #18 (csv 926)**: broken. Choice D is missing in both the bank and the original, so the question is broken as printed, though B (side 20, perimeter 60) is the correct answer among the given choices.
- **Math M2 #20 (csv 929)**: ambiguous. The seven integers sum to 420, and the eighth must be 4 mod 8, above 60 and below 80, so both 68 and 76 work; the stem should ask for the greatest possible value to make 76 the unique answer.

## Yellow

- solver medium: 11
- content: grammar: 2
- content: missing_info: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 92, medium 6, low 0.
- solve_b (sonnet): disagrees with the bank key on 0, with the final key on 0; confidence high 91, medium 7, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 104; kept as figures 4 (graph 3, chart 1), the rest turned into text.
- Upscaled for the models: 64.

## Explanations

- Bank explanation: usable 74, minor_issue 20, wrong 1, mismatch 2, missing 1.
- Final: drafted 45, kept from the bank 53.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 821,926 | $2.30 |
| solve_a | opus | 10 | 730,267 | $4.09 |
| solve_b | sonnet | 10 | 725,022 | $2.03 |
| explain | sonnet | 10 | 882,959 | $2.47 |
| adjudicate | opus | 3 | 253,434 | $1.42 |
| **Subagents** | | 43 | **3,413,608** | **$12.31** |

Per question ≈ 34,832 tokens, ≈ $0.126 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Prep flagged math-m2-18 (choice D empty in the bank row); no agent re-runs were needed.
