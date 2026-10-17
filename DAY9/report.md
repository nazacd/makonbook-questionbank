# DAY9 AI review

Test ids DAY9: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 6 | 2 | 54 |
| Math | 35 | 8 | 1 | 44 |
| **Total** | **81** | **14** | **3** | **98** |

Verdicts: key_correct 95, broken 1, ambiguous 1, key_wrong 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M2 #1 (csv 260)**: broken. D is the only decreasing exponential curve, but the question is defective because choices B and C use identical images; the original choice C graph must be restored by a teacher (duplicate issues merged).
- **R&W M1 #16 (csv 339)**: ambiguous. Ambiguous: the comma appositive (key D) and the colon (C, both solvers) are each grammatical because "scientists turn to stratigraphy" is a complete clause and nothing closes the inserted phrase, so neither can be proven wrong.
- **R&W M2 #16 (csv 366)**: key_wrong. Key D → C. Key D says sensitivity to warming is negatively correlated with the number of vertebrate hosts, but the data show a positive relationship, so D contradicts the text and C is the only consistent choice.

## Yellow

- solver medium: 6
- solver disagrees with the key: 4
- content: typo: 4
- transcription medium: 2
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 2; confidence high 95, medium 3, low 0.
- solve_b (sonnet): disagrees with the bank key on 5, with the final key on 4; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 2 (R&W M1 #16 (csv 339); R&W M2 #16 (csv 366)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 16; kept as figures 9 (graph 6, scatterplot 1, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 15.

## Explanations

- Bank explanation: usable 60, minor_issue 23, wrong 10, mismatch 0, missing 5.
- Final: drafted 54, kept from the bank 44.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| explain | sonnet | 10 | 641,223 | $1.80 |
| adjudicate | opus | 4 | 256,170 | $1.43 |
| **Subagents** | | 14 | **897,393** | **$3.23** |

Per question ≈ 9,157 tokens, ≈ $0.033 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Token counts for transcribe, solve_a, solve_b and adj-4 were not logged.
- 25 of 98 questions went to adjudication; several bank explanations were wrong (see report).
