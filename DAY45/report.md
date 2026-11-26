# DAY45 AI review

Test ids DAY45: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 38 | 8 | 8 | 54 |
| Math | 42 | 2 | 0 | 44 |
| **Total** | **80** | **10** | **8** | **98** |

Verdicts: key_correct 90, key_wrong 8. Adjudicated: 19.

## Red: a teacher decides before publishing

- **R&W M1 #6 (csv 2454)**: key_wrong. Key C → D. Key C is wrong, since the text says nothing about what inspired Crowley and instead explains why Bloom praises Little, Big, so D is correct (both solvers agree with high confidence).
- **R&W M1 #7 (csv 2455)**: key_wrong. Key D → C. Key D is wrong, since the text neither traces how community science developed nor suggests future projects; it identifies the approach, lists its benefits and cites one study, which is choice C.
- **R&W M1 #8 (csv 2456)**: key_wrong. Key C → D. Key C is wrong because it reverses the passage, which explains that people's love of light and fear of the lonely night drive them into cities, so D is correct.
- **R&W M1 #9 (csv 2457)**: key_wrong. Key D → C. Key D is unsupported (the text never counts borrowed words); both examples show Spanish as the channel for Indigenous words into English, so the key should be C.
- **R&W M1 #10 (csv 2458)**: key_wrong. Key B → D. Key B asserts an unstated prediction; D directly restates the text's finding and conclusion, so the key should be D.
- **R&W M1 #12 (csv 2460)**: key_wrong. Key D → B. The hypothesis is comparative and only B compares wide- and narrow-headed fish under the stated conditions, so key D is wrong and should be B; the duplicate missing-article typo issue was merged into one.
- **R&W M1 #13 (csv 2461)**: key_wrong. Key A → D. Only D presents both Avey's indifference and the narrator's ambition, so key A is wrong and should be D.
- **R&W M2 #13 (csv 2485)**: key_wrong. Key A → D. Key A is wrong because it calls muralists unrecognized when the text says only muralists were recognized; D, constraints on Chicano artists in general, is the only choice that accounts for both Valdez and Sandoval.

## Yellow

- solver medium: 5
- solver disagrees with the key: 4
- transcription medium: 3
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 8, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 12, with the final key on 4; confidence high 95, medium 3, low 0.
- Both disagree with the bank key: 8 (R&W M1 #6 (csv 2454); R&W M1 #7 (csv 2455); R&W M1 #8 (csv 2456); R&W M1 #9 (csv 2457); R&W M1 #10 (csv 2458); R&W M1 #12 (csv 2460); R&W M1 #13 (csv 2461); R&W M2 #13 (csv 2485)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 103; kept as figures 5 (geometry 2, scatterplot 1, graph 1, chart 1), the rest turned into text.
- Upscaled for the models: 103.

## Explanations

- Bank explanation: usable 67, minor_issue 13, wrong 17, mismatch 0, missing 1.
- Final: drafted 55, kept from the bank 43.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 787,176 | $2.20 |
| solve_a | opus | 10 | 718,909 | $4.03 |
| solve_b | sonnet | 10 | 716,027 | $2.00 |
| explain | sonnet | 10 | 886,851 | $2.48 |
| adjudicate | opus | 4 | 327,933 | $1.84 |
| **Subagents** | | 44 | **3,436,896** | **$12.55** |

Per question ≈ 35,070 tokens, ≈ $0.128 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

explain math-m1-a failed its check once (a skill tag outside its domain); re-run once, then passed.
The protocol changed during the session (Fix step, original.jsonl); DAY45 follows the new one.
