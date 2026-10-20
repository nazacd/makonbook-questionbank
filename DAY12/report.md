# DAY12 AI review

Test ids DAY12: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 43 | 10 | 1 | 54 |
| Math | 43 | 0 | 1 | 44 |
| **Total** | **86** | **10** | **2** | **98** |

Verdicts: key_correct 96, key_wrong 2. Adjudicated: 18.

## Red: a teacher decides before publishing

- **Math M1 #13 (csv 386)**: key_wrong. Key A → C. Key A is wrong because 40% is not "most" and the sample covers only the center's members; the random sample supports C, as both solvers found with high confidence.
- **R&W M2 #14 (csv 526)**: key_wrong. Key D → B. Key D is wrong because it says the correlation is negative when the data show a positive one (parasites needing more vertebrate hosts declined with warming), and B is the only choice consistent with the text; I kept the missing-article issue once, as cosmetic, and dropped the duplicate.

## Yellow

- solver medium: 6
- solver disagrees with the key: 4

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 0; confidence high 95, medium 3, low 0.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 4; confidence high 93, medium 5, low 0.
- Both disagree with the bank key: 2 (Math M1 #13 (csv 386); R&W M2 #14 (csv 526)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 25; kept as figures 13 (graph 8, geometry 4, scatterplot 1), the rest turned into text.
- Upscaled for the models: 24.

## Explanations

- Bank explanation: usable 70, minor_issue 13, wrong 13, mismatch 2, missing 0.
- Final: drafted 52, kept from the bank 46.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 588,712 | $1.65 |
| solve_a | opus | 10 | 549,886 | $3.08 |
| solve_b | sonnet | 10 | 548,716 | $1.54 |
| explain | sonnet | 10 | 720,651 | $2.02 |
| adjudicate | opus | 3 | 198,697 | $1.11 |
| **Subagents** | | 43 | **2,606,662** | **$9.39** |

Per question ≈ 26,598 tokens, ≈ $0.096 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #13 (csv 386)** (red, corrected, high): Removed the stray space in "High- Intensity"; the held key is already C, the correct answer per the review, and the explanation already supports C.
- **R&W M1 #13 (csv 498)** (yellow, no change, high): No change needed: the solver was only medium-confident, but the passage and choices are clear and key A is correct.
- **R&W M1 #23 (csv 508)** (yellow, no change, high): No change needed: the text is clear and "Of course" correctly signals the obvious concession that tickers were retired by 2008.
- **R&W M2 #3 (csv 515)** (yellow, no change, high): No change needed: the "but" contrast with Machado, who "will always be remembered," makes "uncertain" the only fit; the dissenting solver misread the contrast.
- **R&W M2 #4 (csv 516)** (yellow, no change, high): No change needed: the question is clear and "precipitating" (suddenly bringing about) demand matches buyers suddenly thronging the market.
- **R&W M2 #11 (csv 523)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the text and choices are clean and C is the only quotation showing realism juxtaposed with Portuguese folklore.
- **R&W M2 #14 (csv 526)** (red, corrected, medium): Changed the key from D to B per the key_wrong verdict (D states a negative correlation, the reverse of the data), added the missing article "a" to choice D, and wrote the explanation for key B.
- **R&W M2 #18 (csv 530)** (yellow, no change, high): No change needed: the second solver's C creates a comma splice before "both ... contributed", so A is the only correct choice and the question is clear.
- **R&W M2 #19 (csv 531)** (yellow, no change, high): No change needed: the second solver disagreed, but the main clause is complete before the comma, so only the absolute phrase with "pledging" avoids a comma splice.
- **R&W M2 #20 (csv 532)** (yellow, no change, high): No change needed: "Costa Rica and Switzerland" is a restrictive appositive of "fellow OECD nations", so no punctuation is correct and the key B is right.
- **R&W M2 #21 (csv 533)** (yellow, no change, high): No change needed: the solver was only moderately confident, but the text is clear and complete, and "Granted," is the only transition that concedes the bromine pattern before the europium exception.
- **R&W M2 #27 (csv 539)** (yellow, no change, high): No change needed: the notes and choices are complete and correctly transcribed, and only D both makes a generalization about flag symbols and supports it with an example.
