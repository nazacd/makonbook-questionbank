# DAY1 AI review

Test ids DAY1: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 40 | 12 | 2 | 54 |
| Math | 40 | 2 | 2 | 44 |
| **Total** | **80** | **14** | **4** | **98** |

Verdicts: key_correct 94, key_wrong 2, broken 1, ambiguous 1. Adjudicated: 20.

## Red: a teacher decides before publishing

- **Math M1 #12 (csv 13)**: broken. Key B (x = by - 49y) is correct, but the bank's choice images for C and D are the same expression, so the question as printed has a duplicate choice; the two duplicate_choice issues were merged into one.
- **Math M2 #17 (csv 40)**: key_wrong. Key 192 → 192.1. The bank key 192 rests on an arithmetic error (1.852^2 = 3.429904, not 3.429104), so k = 192.074624, which is 192.1 to the nearest tenth; the drafted explanation already reaches 192.1.
- **R&W M1 #5 (csv 5)**: key_wrong. Key B → D. The underlined air-cooling observation is framed as an effect beyond the fungi and is what the text says inspired the air-cooling device, so D is correct and B misreads it as evidence of the fungi's hypothermia; the drafted explanation already states D.
- **R&W M2 #13 (csv 39)**: ambiguous. Ambiguous: key D as printed states a negative correlation that reverses what the text implies (more vertebrate hosts, more sensitivity), likely a misprint of "positively", while C is consistent; the solvers split with medium confidence, so a teacher should decide between fixing D's wording or rekeying to C (duplicate typo issue merged, the "corrosion- inhibiting" example dropped as it is not in this question).

## Yellow

- solver medium: 11
- solver disagrees with the key: 5
- content: other: 1
- content: ambiguous: 1
- transcription medium: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 4, with the final key on 2; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 4; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 3 (Math M2 #17 (csv 40); R&W M1 #5 (csv 5); R&W M2 #19 (csv 45)).
- The two solvers disagree with each other: 5.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 38; kept as figures 4 (chart 3, graph 1), the rest turned into text.
- Upscaled for the models: 31.

## Explanations

- Bank explanation: usable 65, minor_issue 18, wrong 9, mismatch 4, missing 2.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 575,300 | $1.61 |
| solve_a | opus | 10 | 524,209 | $2.94 |
| solve_b | sonnet | 10 | 521,386 | $1.46 |
| explain | sonnet | 10 | 682,249 | $1.91 |
| adjudicate | opus | 4 | 263,463 | $1.48 |
| **Subagents** | | 44 | **2,566,607** | **$9.39** |

Per question ≈ 26,189 tokens, ≈ $0.096 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Transcribe, solve and explain agents were launched in two waves because of the 20-agent concurrency limit (10 explain batches started after solve slots freed).
- No batch re-runs and no failed agents.
- The math-m2-b explain agent flagged math-m2-17: it computed 192.1 where the bank key says 192 (1.852 squared = 3.429904). Left to adjudication; teacher should confirm.
