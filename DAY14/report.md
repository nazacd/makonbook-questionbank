# DAY14 AI review

Test ids DAY14: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 7 | 0 | 54 |
| Math | 34 | 8 | 2 | 44 |
| **Total** | **81** | **15** | **2** | **98** |

Verdicts: key_correct 96, key_wrong 1, ambiguous 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M1 #1 (csv 464)**: key_wrong. Key -22 → 9. Key -22 needs a^c = -15, impossible for an exponential base a > 0, so the only valid answer is 9 (both solvers agree); the duplicate typo issue was merged into one.
- **Math M1 #17 (csv 480)**: ambiguous. The system is undefined: all three equations share no point (A, as both solvers found), while f(x) with y = -3 or the two graphed lines meet once (key B), so a teacher must decide.

## Yellow

- solver medium: 12
- transcription medium: 3
- content: typo: 2
- content: other: 1
- content: ambiguous: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 1 (Math M1 #17 (csv 480)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 37; kept as figures 5 (graph 3, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 34.

## Explanations

- Bank explanation: usable 74, minor_issue 14, wrong 8, mismatch 1, missing 1.
- Final: drafted 50, kept from the bank 48.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 563,034 | $1.58 |
| solve_a | opus | 10 | 516,743 | $2.89 |
| solve_b | sonnet | 10 | 514,723 | $1.44 |
| explain | sonnet | 10 | 648,448 | $1.82 |
| adjudicate | opus | 5 | 316,722 | $1.77 |
| **Subagents** | | 45 | **2,559,670** | **$9.50** |

Per question ≈ 26,119 tokens, ≈ $0.097 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

adj-4 re-run once: first output was missing english-m2-21; fixed on re-run.
