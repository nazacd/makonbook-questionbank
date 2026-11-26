# DAY44 AI review

Test ids DAY44: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 33 | 13 | 8 | 54 |
| Math | 39 | 4 | 1 | 44 |
| **Total** | **72** | **17** | **9** | **98** |

Verdicts: key_correct 90, broken 5, key_wrong 3. Adjudicated: 32.

## Red: a teacher decides before publishing

- **Math M2 #14 (csv 2003)**: broken. Broken: as printed, CV = PR with R = 41 gives P = CV/41, which is none of the choices, and the original relation cannot be recovered with confidence (the choices hint at different exponents).
- **R&W M1 #9 (csv 2508)**: key_correct. Key D is right because the narrator says he "gave free rein to the sadness in his heart" through his melancholy tunes; the crop removes only line-end letters, so I lowered it to cosmetic, and I dropped the "translated b" typo issue as a transcription error that transcription_fix corrects.
- **R&W M1 #15 (csv 2514)**: broken. Broken: the intended answer (opponents influenced by the red uniforms) is clear, but choices A and B are identical so B is equally correct and the original B text cannot be recovered; the three duplicate_choice reports are merged into one and the missing stem is downgraded from blocking to content because the blank makes the task clear.
- **R&W M1 #16 (csv 2515)**: broken. Broken: the passage needs a noun (such as "photograph") between the possessive and the title, but the choices are verb forms copied from english-m1-17, so no choice works and key A cannot stand.
- **R&W M2 #11 (csv 2537)**: broken. Broken: the passage (IGF-1 and dog size, a student's conclusion) is paired with the stem and choices of a different question about dogs' brain responses to languages, so no choice can be chosen; the separate missing_info issue duplicates the mismatch and is dropped.
- **R&W M2 #12 (csv 2564)**: key_wrong. Key A → B. Key A is wrong because the graph shows Kalmarinjärvi dropping from about 198 to 152 ice days; only B (Lake Baikal, about 96 to 109) correctly gives an increase.
- **R&W M2 #22 (csv 2612)**: broken. The passage is missing from both the image and the bank, so the question cannot be answered as shown; the bank explanation quotes the passage, which is proposed as the fix (with it, key A "Indeed," is correct). The two duplicate missing_info issues were merged into one.
- **R&W M2 #23 (csv 2613)**: key_wrong. Key A → D. Key changed from A to D: A is consistent with the student's conclusion, while D shows other genes also affect size, so IGF-1 variation cannot account for the variance by itself; the bank explanation belongs to a different question.
- **R&W M2 #27 (csv 2626)**: key_wrong. Key A → C. Key changed from A to C because A's claim that the formula overrepresents more populated districts contradicts the notes, while C accurately states that the formula overrepresents less populated rural districts; the two duplicate choice-D issues were merged into one.

## Yellow

- solver medium: 9
- content: missing_info: 8
- solver disagrees with the key: 2
- transcription medium: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 7, with the final key on 4; confidence high 90, medium 4, low 4.
- solve_b (sonnet): disagrees with the bank key on 9, with the final key on 6; confidence high 89, medium 7, low 2.
- Both disagree with the bank key: 7 (Math M2 #14 (csv 2003); R&W M1 #16 (csv 2515); R&W M2 #11 (csv 2537); R&W M2 #12 (csv 2564); R&W M2 #22 (csv 2612); R&W M2 #23 (csv 2613); R&W M2 #27 (csv 2626)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 93, medium 3, low 2.
- Question and choice images: 109; kept as figures 10 (chart 4, graph 3, geometry 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 92.

## Explanations

- Bank explanation: usable 64, minor_issue 13, wrong 13, mismatch 5, missing 3.
- Final: drafted 58, kept from the bank 40.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 8 | 687,654 | $1.93 |
| solve_a | opus | 10 | 702,284 | $3.93 |
| solve_b | sonnet | 10 | 700,415 | $1.96 |
| explain | sonnet | 10 | 942,511 | $2.64 |
| adjudicate | opus | 6 | 516,055 | $2.89 |
| **Subagents** | | 44 | **3,548,919** | **$13.35** |

Per question ≈ 36,213 tokens, ≈ $0.136 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- A usage limit cut off all 10 transcription agents; 8 were re-run. english-m2-a and english-m2-c kept the saved outputs that passed the check (token counts for those two are not logged).
- transcribe english-m1-c needed 2 re-runs (empty stems on english-m1-19 and english-m1-20).
- explain english-m1-b re-run once: english-m1-16 has choices that cannot fill the blank (flagged by the explainer as a blocking missing_info issue).
- english-m1-15 has identical choices A and B (bank data issue).
