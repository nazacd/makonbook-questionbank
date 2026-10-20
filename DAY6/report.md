# DAY6 AI review

Test ids DAY6: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 45 | 6 | 3 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **88** | **7** | **3** | **98** |

Verdicts: key_correct 95, ambiguous 3. Adjudicated: 13.

## Red: a teacher decides before publishing

- **R&W M1 #21 (csv 1073)**: ambiguous. Ambiguous: the final sentence attributes the Afroyim-style ruling to Perez v. Brownell, contradicting the prior sentence, so both "Additionally" (key) and "Nevertheless" can be defended and the solvers split at medium confidence.
- **R&W M2 #3 (csv 1082)**: ambiguous. Ambiguous: the text stresses confirmation and firmer ground, which supports "clarified" (both solvers' choice) as well as or better than the keyed "revolutionized", but word-precision preference is not a proof the key is wrong.
- **R&W M2 #24 (csv 1103)**: ambiguous. Transcription matches the image; key C ("Indeed,") holds if labor and gender themes are read as the political themes just mentioned, but D ("In addition,") is equally defensible if they are read as new themes, and the solvers split, so a teacher should decide.

## Yellow

- solver medium: 6
- transcription medium: 1
- content: ambiguous: 1
- solver low: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 91, medium 6, low 1.
- Both disagree with the bank key: 1 (R&W M2 #3 (csv 1082)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 127; kept as figures 8 (graph 4, chart 2, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 75.

## Explanations

- Bank explanation: usable 77, minor_issue 14, wrong 6, mismatch 1, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 630,726 | $1.77 |
| solve_a | opus | 10 | 536,835 | $3.01 |
| solve_b | sonnet | 10 | 535,648 | $1.50 |
| explain | sonnet | 10 | 660,109 | $1.85 |
| adjudicate | opus | 3 | 186,671 | $1.05 |
| **Subagents** | | 43 | **2,549,989** | **$9.17** |

Per question ≈ 26,020 tokens, ≈ $0.094 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Worker restart and usage limit interrupted the session after DAY6 prep; transcribe was launched fresh, no re-runs. Explain agents launched as concurrency slots freed.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #18 (csv 800)** (yellow, no change, high): No change needed: the only issue is the screenshot's cropped "To", and our transcription already reads "To the nearest whole number" correctly.
- **R&W M1 #3 (csv 1055)** (yellow, no change, high): No change needed: the text matches the screenshot, and the solver was only unsure. The question is clear and B is the only fit.
- **R&W M1 #7 (csv 1059)** (yellow, corrected, medium): Corrected the typo "neutral dust" to "neural dust" in choice D. The ambiguity flag needs no rewrite because B is the only choice the text supports.
- **R&W M1 #9 (csv 1061)** (yellow, corrected, high): Corrected grammar slips: added "a" in "Alleyne is a young monk", changed "has becomes" to "has become" in B, and added the missing period to A.
- **R&W M1 #20 (csv 1072)** (yellow, corrected, high): Corrected the blank to six underscores and the typed "--" to real dashes in A and C. Rewrote the explanation, which had no answer line and did not address the distractors.
- **R&W M1 #21 (csv 1073)** (red, invented, high): The last sentence credited the citizenship ruling to Perez v. Brownell, contradicting the previous sentence and making "Nevertheless" defensible; it now names Afroyim v. Rusk, so the sentence simply adds more about the same ruling.
- **R&W M1 #26 (csv 1078)** (yellow, corrected, high): Fixed "fil" to "film" in C, restored the missing "A" at the start of D, and matched the notes' spelling and italics ("Agnès", *Cléo from 5 to 7*) in the stem and choices.
- **R&W M2 #3 (csv 1082)** (red, invented, high): Replaced distractor B "clarified", which fit the text at least as well as the key, with "limited", so "revolutionized" is the only choice that matches a discovery that advanced understanding.
- **R&W M2 #15 (csv 1094)** (yellow, no change, high): No change needed: the transcription matches the screenshot, and the solvers were only moderately sure, but the freeze-drying detail clearly supports storing crops, so the key is right.
- **R&W M2 #24 (csv 1103)** (red, invented, medium): Replaced distractor D "In addition,", which was as defensible as the key, with "Instead,", so "Indeed," is the only transition that fits the elaboration of Gowda's political themes.
