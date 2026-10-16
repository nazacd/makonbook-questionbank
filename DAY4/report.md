# DAY4 AI review

Test ids DAY4: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 48 | 5 | 1 | 54 |
| Math | 39 | 3 | 2 | 44 |
| **Total** | **87** | **8** | **3** | **98** |

Verdicts: key_correct 95, ambiguous 2, broken 1. Adjudicated: 15.

## Red: a teacher decides before publishing

- **Math M1 #3 (csv 154)**: ambiguous. Every recorded temperature satisfies both A (40 <= t <= 90) and D (t <= 90), so as worded the question has two correct choices; a teacher should reword the stem or replace choice D.
- **Math M1 #8 (csv 159)**: ambiguous. The bank explanation's points (0, 2) and (2, 12) are not on the drawn line, and my reading (y-intercept about 5, x-intercept about -0.8, endpoints near (-1.45, -4) and (1.25, 12)) favors slope 6 and answer B, but the distorted photo does not allow a rigorous proof against A, so a teacher should check against a clean source figure.
- **R&W M1 #12 (csv 172)**: broken. Broken: key A claims Allentown-Bethlehem's delay rose from 1990 to 2000, but the graph shows it fell (about 40 to 34), so no choice is both accurate and supportive; A works if it names Beaumont, Texas, which rose from about 18 to 32 while staying below New York; the duplicate D typo issue was merged and downgraded to cosmetic because D is wrong either way.

## Yellow

- solver medium: 8
- solver disagrees with the key: 3
- content: choice_formatting: 1
- transcription medium: 1
- content: grammar: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 93, medium 4, low 1.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 90, medium 8, low 0.
- Both disagree with the bank key: 2 (Math M1 #8 (csv 159); Math M1 #12 (csv 661)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 27; kept as figures 5 (graph 2, scatterplot 1, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 26.

## Explanations

- Bank explanation: usable 76, minor_issue 14, wrong 8, mismatch 0, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 575,610 | $1.61 |
| solve_a | opus | 10 | 534,415 | $2.99 |
| solve_b | sonnet | 10 | 533,758 | $1.49 |
| explain | sonnet | 10 | 668,823 | $1.87 |
| adjudicate | opus | 3 | 196,261 | $1.10 |
| **Subagents** | | 43 | **2,508,867** | **$9.07** |

Per question ≈ 25,600 tokens, ≈ $0.093 at API list prices (90/10 input/output split assumed; the main session is not included).
