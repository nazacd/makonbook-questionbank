# DAY8 AI review

Test ids DAY8: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 6 | 1 | 54 |
| Math | 38 | 5 | 1 | 44 |
| **Total** | **85** | **11** | **2** | **98** |

Verdicts: key_correct 96, key_wrong 1, broken 1. Adjudicated: 16.

## Red: a teacher decides before publishing

- **Math M2 #22 (csv 757)**: key_wrong. Key C → D. Each statement alone is side-side-angle (the 30 degree angle is opposite QR and TU), and an explicit counterexample shows it does not force similarity, so C is wrong and D is the key; the duplicate numbering issue was merged and the 'ambiguous' issue replaced by wrong_key.
- **R&W M1 #11 (csv 279)**: broken. Key A is right (less adjustment to fit the database's categories means higher category consistency), but choices C and D are duplicates of each other, so the printed question is defective and a teacher needs to restore the original distractor; the duplicate issues_so_far entry was merged.

## Yellow

- solver medium: 10
- transcription medium: 3
- content: other: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 1; confidence high 87, medium 11, low 0.
- Both disagree with the bank key: 1 (Math M2 #22 (csv 757)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 33; kept as figures 5 (geometry 2, graph 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 31.

## Explanations

- Bank explanation: usable 69, minor_issue 24, wrong 5, mismatch 0, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 571,075 | $1.60 |
| explain | sonnet | 10 | 644,083 | $1.80 |
| adjudicate | opus | 2 | 120,167 | $0.67 |
| **Subagents** | | 22 | **1,335,325** | **$4.08** |

Per question ≈ 13,625 tokens, ≈ $0.042 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Token counts for solve_a, solve_b and adj-1 were not logged.
- math-m2-22: explainer concluded D vs bank key C (SSA/SAS wording); see report.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #13 (csv 726)** (yellow, no change, high): No change needed: the transcription matches the screenshot exactly and the question is clear with a single answer.
- **Math M1 #19 (csv 732)** (yellow, no change, high): No change needed: the solver was unsure, but since A and B are acute the right angle is at C, the question is clear and key C is right.
- **Math M2 #13 (csv 748)** (yellow, invented, high): Replaced the impossible condition "c and d are greater than 1" (then 2/c - 7/d < 2, never 5) with "positive", which is consistent with solutions such as c = 1/5, d = 7; choices and key unchanged.
- **Math M2 #16 (csv 751)** (yellow, no change, high): No change needed: the transcription matches the screenshot, the key 23/30 is right, and the accepted list already holds the valid decimal forms.
- **Math M2 #19 (csv 754)** (yellow, no change, medium): No change needed: the transcription matches the screenshot and key D is correct.
- **Math M2 #22 (csv 757)** (red, corrected, high): Renumbered the statements from 1 and 2 to I and II so they match the choices, and rewrote the explanation to use I and II; the key stays D as the review found.
- **R&W M1 #11 (csv 279)** (red, corrected, invented, high): Choices C and D were duplicates, so D was replaced with a new distractor that reverses the detail comparison, C got its missing period, and the explanation now covers every choice.
- **R&W M1 #13 (csv 286)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and complete, and A is the only choice that ties the sounds to attacks, which supports the claim that they target predators.
- **R&W M1 #18 (csv 282)** (yellow, corrected, high): Fixed the typo "OLCD" to "OECD" and "convention" to "conventions" in the stem; the key C and the explanation are right.
- **R&W M1 #20 (csv 283)** (yellow, corrected, high): Changed "convention" to "conventions" in the stem; the question is otherwise clear and key A is right.
- **R&W M1 #23 (csv 292)** (yellow, corrected, high): Added the missing space between the blank and "the tickers"; nothing else needed changing.
- **R&W M2 #8 (csv 304)** (yellow, no change, high): No change: the solver was only moderately sure, but both texts are complete, the choices are distinct, and key C is the only statement both authors would accept.
- **R&W M2 #22 (csv 318)** (yellow, no change, high): No change: the solver was only moderately sure, but the sentence is clear and key B is the only grammatical completion.
