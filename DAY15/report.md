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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #15 (csv 629)** (yellow, restored, high): Restored the missing "in the US" at the end of choice D so it no longer seems to contradict the stem, which says the students were chosen at random from one district.
- **Math M1 #20 (csv 635)** (yellow, no change, high): No change needed: the stem and the equation match the original screenshot, and the key is right.
- **Math M2 #2 (csv 639)** (yellow, no change, high): No change needed: the box plot is readable despite the watermark, the stem matches it, and the key is right.
- **Math M2 #6 (csv 643)** (yellow, no change, high): No change needed: the four graphs are readable despite cursors and a watermark, the descriptions match them, and only B is right.
- **Math M2 #9 (csv 646)** (yellow, no change, high): No change needed: the solvers were unsure, but the figure clearly shows x as the acute angle below t, left of r, and y as the obtuse angle above t, left of s, so the question is clear and the key is right.
- **Math M2 #21 (csv 658)** (red, invented, high): Changed choice A from "7 and -5" to "-7 and -5" because 0 also lay between 7 and -5, making two choices correct; updated the explanation to match.
- **R&W M1 #6 (csv 654)** (yellow, corrected, invented, high): Capitalized "Researchers" and replaced "a small, flexible bone in ocelots" with "a small bone in the cats' throats", since the passage later says ocelots have a rigid hyoid and jaguars a flexible one.
- **R&W M1 #14 (csv 662)** (yellow, corrected, high): Fixed choice D, which repeated "increase" on both sides of the comparison; the bank explanation shows the first verb is "decrease".
- **R&W M1 #24 (csv 672)** (yellow, corrected, high): The question and key are sound; only the blank was changed from four underscores to the standard six.
