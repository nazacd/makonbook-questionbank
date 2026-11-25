# DAY43 AI review

Test ids DAY43: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 7 | 1 | 54 |
| Math | 38 | 6 | 0 | 44 |
| **Total** | **84** | **13** | **1** | **98** |

Verdicts: key_correct 97, key_wrong 1. Adjudicated: 15.

## Red: a teacher decides before publishing

- **R&W M2 #15 (csv 2437)**: key_wrong. Key A → D. Key A contradicts the text, which says recognition was restricted to muralists, so muralists did not lack recognition; D is the only choice that explains both Valdez and Sandoval, and both solvers chose it with high confidence.

## Yellow

- solver medium: 12
- transcription medium: 3
- solver disagrees with the key: 3
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 3; confidence high 91, medium 7, low 0.
- Both disagree with the bank key: 1 (R&W M2 #15 (csv 2437)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 122; kept as figures 10 (graph 6, chart 2, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 113.

## Explanations

- Bank explanation: usable 79, minor_issue 11, wrong 6, mismatch 1, missing 1.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 780,641 | $2.19 |
| solve_a | opus | 10 | 701,229 | $3.93 |
| solve_b | sonnet | 10 | 700,609 | $1.96 |
| explain | sonnet | 10 | 799,670 | $2.24 |
| adjudicate | opus | 3 | 241,438 | $1.35 |
| **Subagents** | | 43 | **3,223,587** | **$11.67** |

Per question ≈ 32,893 tokens, ≈ $0.119 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #11 (csv 1840)** (yellow, no change, high): No change needed: the transcription matches the original, and although the top of the figure is cropped just above y = 12, the line, the points and both axes' tick values needed to estimate the slope are all visible.
- **Math M2 #7 (csv 1859)** (yellow, restored, high): Restored the missing question line, which the four choices make clear asks students to compare the two teams' standard deviations.
- **Math M2 #9 (csv 1861)** (yellow, no change, high): No change needed: the original figure is cropped just above the x-axis, but the x-axis and the whole curve are visible, and the transcription matches the original.
- **Math M2 #11 (csv 1864)** (yellow, no change, high): No change needed: the transcription matches the original word for word, and the question has one clear answer.
- **Math M2 #16 (csv 1869)** (yellow, no change, high): No change needed: the transcription matches the original, and the key is right even though a solver was unsure.
- **Math M2 #21 (csv 1874)** (yellow, no change, high): No change needed: the stem and all four choices match the original screenshots, and the explanation correctly lists every possible sum of four angles.
- **R&W M1 #8 (csv 2403)** (yellow, no change, high): No change needed: the passage matches the original screenshot word for word and the key is right.
- **R&W M1 #12 (csv 2407)** (yellow, no change, high): No change needed: the question is clear and complete, and the solver's doubt does not reflect a real flaw.
- **R&W M2 #12 (csv 2434)** (yellow, no change, high): No change needed: the question is clear and the key is right; the solver's choice B fails because a positive age-similarity correlation would make older rocks more mixed, the reverse of the claim.
- **R&W M2 #13 (csv 2435)** (yellow, no change, high): No change needed: the graph is readable, the text matches the original, and the current explanation already reads P6's values correctly (about 0.43 and 0.27).
- **R&W M2 #15 (csv 2437)** (red, no change, high): The review's fix (key D) is already in our version, and the explanation already argues for D, so nothing needs to change.
- **R&W M2 #18 (csv 2440)** (yellow, corrected, high): The question is clear and the key is right; only the explanation was rewritten, because it began with leftover chat text ("the correct answer is indeed") and had no answer line.
- **R&W M2 #19 (csv 2441)** (yellow, corrected, high): The question is clear and the key is right (one solver's choice A misreads "though"); only the explanation was rewritten, because it began with leftover chat text and had no answer line.
- **R&W M2 #23 (csv 2445)** (yellow, corrected, medium): The question is clear and the key is right; only the explanation was rewritten to remove chatty wording and add the answer line.
