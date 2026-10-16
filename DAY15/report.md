# DAY15 AI review

Test ids DAY15: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 51 | 3 | 0 | 54 |
| Math | 38 | 5 | 1 | 44 |
| **Total** | **89** | **8** | **1** | **98** |

Verdicts: key_correct 97, ambiguous 1. Adjudicated: 17.

## Red: a teacher decides before publishing

- **Math M2 #21 (csv 658)**: ambiguous. Ambiguous: x - 4 = 0 lies inside both A (-5 to 7) and B (-3 to 3), so B cannot be the only correct answer unless choice A is changed, for example to "-7 and -5".

## Yellow

- solver medium: 6
- transcription medium: 2
- content: ambiguous: 1
- content: other: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 0, with the final key on 0; confidence high 95, medium 2, low 1.
- solve_b (sonnet): disagrees with the bank key on 0, with the final key on 0; confidence high 93, medium 5, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 0.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 86; kept as figures 8 (graph 5, geometry 2, chart 1), the rest turned into text.
- Upscaled for the models: 53.

## Explanations

- Bank explanation: usable 68, minor_issue 17, wrong 9, mismatch 3, missing 1.
- Final: drafted 52, kept from the bank 46.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 609,544 | $1.71 |
| solve_a | opus | 10 | 534,379 | $2.99 |
| solve_b | sonnet | 10 | 535,696 | $1.50 |
| explain | sonnet | 10 | 664,824 | $1.86 |
| adjudicate | opus | 2 | 184,878 | $1.04 |
| **Subagents** | | 42 | **2,529,321** | **$9.10** |

Per question ≈ 25,809 tokens, ≈ $0.093 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Only 20 subagents can run at once, so the 10 explain batches were launched as solve agents finished.
- adjudicate adj-1: the agent died on a rate limit (usage limit) but its output file passed the check; its tokens are not logged.
- adjudicate adj-3: first output had a wrong qid (english-m2-24 for english-m1-24); re-run once and it passed. Tokens logged are first run + re-run.
- solve_a math-m2-b flagged math-m2-21 as having two choices that fit as written (A and B both give 0); left to adjudication and teacher review.
