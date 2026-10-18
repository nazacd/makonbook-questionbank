# DAY17 AI review

Test ids DAY17: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 33 | 19 | 2 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **76** | **20** | **2** | **98** |

Verdicts: key_correct 96, broken 2. Adjudicated: 24.

## Red: a teacher decides before publishing

- **R&W M1 #7 (csv 849)**: broken. Broken as printed because the underline the stem relies on is missing; with the 'Given that ...' clause underlined, key B (it identifies the proximity relationship the conclusion rests on) is correct, so the underline is proposed as the fix.
- **R&W M1 #8 (csv 850)**: broken. Broken: the passage (Francie's reading plan) and the choices and bank explanation (a narrator in the countryside) come from different questions, so no choice states the passage's main idea; the duplicate issues are merged.

## Yellow

- solver medium: 14
- transcription medium: 6
- content: typo: 5
- solver disagrees with the key: 2
- content: choice_formatting: 1
- content: other: 1
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 93, medium 3, low 2.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 85, medium 13, low 0.
- Both disagree with the bank key: 1 (R&W M1 #8 (csv 850)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 91, medium 7, low 0.
- Question and choice images: 65; kept as figures 6 (geometry 2, graph 2, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 28.

## Explanations

- Bank explanation: usable 53, minor_issue 35, wrong 7, mismatch 1, missing 2.
- Final: drafted 52, kept from the bank 46.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 604,900 | $1.69 |
| solve_a | opus | 10 | 528,057 | $2.96 |
| solve_b | sonnet | 10 | 525,479 | $1.47 |
| explain | sonnet | 10 | 615,656 | $1.72 |
| adjudicate | opus | 4 | 258,414 | $1.45 |
| **Subagents** | | 44 | **2,532,506** | **$9.29** |

Per question ≈ 25,841 tokens, ≈ $0.095 at API list prices (90/10 input/output split assumed; the main session is not included).
