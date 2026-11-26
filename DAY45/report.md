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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #8 (csv 1929)** (yellow, no change, high): No change needed: the crop only clips the top of the "30" label, and the 5-unit scale, the points and the line of best fit are all clearly readable, so the question is answerable and the key is right.
- **Math M2 #17 (csv 1960)** (yellow, no change, high): No change needed: the transcription matches the original, and the graph clearly shows line g through (-10, 12) and (0, 1), which is all the question needs.
- **R&W M1 #5 (csv 2453)** (yellow, corrected, high): Added the missing articles to A and C so all four choices fit the sentence grammatically, and rewrote the muddled explanation.
- **R&W M1 #6 (csv 2454)** (red, corrected, high): Set the key to D, as the review found: the text explains why Bloom praises Little, Big and never discusses what inspired Crowley (the old key C).
- **R&W M1 #7 (csv 2455)** (red, corrected, high): Set the key to C, as the review found: the text names an approach, lists its benefits and mentions a study that used it, and it never traces a development or suggests future projects (the old key D).
- **R&W M1 #8 (csv 2456)** (red, corrected, high): Set the key to D as the review found; the bank's key C reverses the text, which says people crowd into cities and long for gas-lit streets. The text matches the original screenshot.
- **R&W M1 #9 (csv 2457)** (red, corrected, high): Set the key to C as the review found; the bank's key D claims equal numbers of borrowed words, which the text never counts. The text matches the original screenshot.
- **R&W M1 #10 (csv 2458)** (red, corrected, high): Set the key to D as the review found; the bank's key B makes a prediction the text never makes. The text matches the original screenshot.
- **R&W M1 #12 (csv 2460)** (red, corrected, high): Set the key to B as the review found (D has no narrow-headed comparison) and restored the missing leading article "A" in all four choices.
- **R&W M1 #13 (csv 2461)** (red, corrected, high): Set the key to D as the review found (A shows only Avey, not the narrator's attitude) and italicized the novel title in the stem.
- **R&W M1 #17 (csv 2464)** (yellow, no change, high): No change needed: the text matches the screenshot, and one solver's disagreement came from missing the comma splice in A.
- **R&W M1 #21 (csv 2467)** (yellow, no change, high): No change needed: the transcription matches the screenshot exactly and the key is right.
- **R&W M2 #5 (csv 2477)** (yellow, no change, high): No change needed: the poem matches the screenshot line for line and the key is clearly right; the solver's medium confidence did not reflect a flaw.
- **R&W M2 #11 (csv 2483)** (yellow, no change, high): No change needed: the graph is clear and readable, the text matches the screenshot, and the key is right.
- **R&W M2 #13 (csv 2485)** (red, corrected, high): Italicized the work's title Instant Mural in choices A, B and D to match the passage; the record's key is already D, the review's corrected key, and the explanation already supports D.
- **R&W M2 #17 (csv 2489)** (yellow, no change, high): No change needed: the text matches the original screenshot, and although one solver disagreed, the question is clear and key A is right.
- **R&W M2 #19 (csv 2491)** (yellow, no change, high): No change needed: the text matches the original screenshot, the question is clear, key C is right, and the current explanation already argues from subject-verb agreement.
- **R&W M2 #21 (csv 2493)** (yellow, no change, high): No change needed: the text matches the original screenshot, the question is clear, key C is right, and the current explanation already describes the concession correctly.
