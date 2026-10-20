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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #12 (csv 13)** (red, invented, high): The bank's choice images for C and D are identical (x = by - 49), so D was replaced with a new distractor, x = (b - 49)/y, that models the common error of dividing instead of multiplying; the explanation was updated to match.
- **Math M2 #14 (csv 37)** (yellow, no change, high): No change needed: the solver was only medium-confident, but f(x) = -39^x is decreasing and concave down, j > m forces h < k, and the question has one clear answer.
- **Math M2 #17 (csv 40)** (red, corrected, high): The bank answer 192 came from squaring 1.852 as 3.429104; the correct conversion gives 192.1 to the nearest tenth, so the accepted answer is 192.1 and the explanation is rewritten to match.
- **Math M2 #22 (csv 45)** (yellow, corrected, high): Fixed the bank's typo in choices C and D, where the Roman numeral II was written with a lowercase L ("lI"); the stem matches the original screenshot and the key B is correct.
- **R&W M1 #5 (csv 5)** (red, corrected, high): The bank key B was wrong: the underlined observation of cooler surrounding air is what the text says inspired the air-cooling device, so the key is D, with an explanation supporting D.
- **R&W M1 #15 (csv 15)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the text is complete and clear and key B is the only logical completion.
- **R&W M1 #25 (csv 24)** (yellow, no change, high): No change needed: the notes and choices are clear and key A is the only choice that both explains the law and gives a specific example.
- **R&W M1 #27 (csv 26)** (yellow, corrected, high): Italicized the title Pan Indian Rhythms in all four choices to match the notes; the question was otherwise fine.
- **R&W M2 #7 (csv 33)** (yellow, no change, high): No change needed: the text is clear and key C is the only choice supported by 'a different balance of reward and risk'.
- **R&W M2 #8 (csv 34)** (yellow, corrected, high): Replaced the stem, which referred to a nonexistent 'underlined claim', with the standard stem for completing the blank; the table in the text matches the original image.
- **R&W M2 #9 (csv 35)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and key B is the only choice that ties head shape to a speech-versus-nonspeech difference.
- **R&W M2 #10 (csv 36)** (yellow, invented, high): Reworded "incurred a lower percentage of the total penalties", which could be read as lower than self-dealing (false: 55% vs 40%) and nudged toward D, to say its share of penalties was smaller than its share of forms; the chart's cropped title hides no data, so the figure is kept.
- **R&W M2 #13 (csv 39)** (red, corrected, medium): Fixed D's "negatively correlated" to "positively correlated" (more vertebrate hosts went with more decline, so the printed word reversed the logic) and added the missing article, removed stray spaces in "two- host" and "warming- driven", and wrote a new explanation since the old one had no answer line.
- **R&W M2 #16 (csv 42)** (yellow, no change, high): No change needed: the solver was unsure, but the appositive "A theoretical relationship between tax rates and revenues" can only modify "the curve", so C is the one right answer.
- **R&W M2 #17 (csv 43)** (yellow, no change, high): No change needed: one solver misread the participial phrase, but "her photos captivated viewers" is a second independent clause, so only the period in D is correct.
- **R&W M2 #18 (csv 44)** (yellow, no change, high): No change needed: the solvers were unsure, but the text is clear and key C is right, since two independent clauses must be joined with a semicolon and a colon is ruled out because the second clause already uses one before "a community."
- **R&W M2 #19 (csv 45)** (yellow, corrected, medium): Restored the missing opening dash after "Proto-Indo-European" to pair with the closing "--" and removed the stray space in "Indo- European"; the key and explanation are unchanged.
- **R&W M2 #27 (csv 53)** (yellow, no change, high): No change needed: the solvers were only moderately sure, but the notes support B as the one generalization about rails-with-trails (about 400 vs. more than 2,000 rail trails).
