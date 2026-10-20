# DAY16 AI review

Test ids DAY16: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 6 | 1 | 54 |
| Math | 37 | 4 | 3 | 44 |
| **Total** | **84** | **10** | **4** | **98** |

Verdicts: key_correct 94, broken 2, unsolvable 1, ambiguous 1. Adjudicated: 17.

## Red: a teacher decides before publishing

- **Math M2 #10 (csv 95)**: unsolvable. As printed b is undetermined (y = 0 and 5a = 27 satisfy the system for every b), so the intended answer 4 needs the stem to say the system has infinitely many solutions.
- **Math M2 #15 (csv 100)**: ambiguous. With a read as the leading coefficient, b - a = 22 - 3 = 19 matches the key, but a is undefined and the unused c suggests a typo (for example c - b = 110), so a teacher must confirm the definition of a.
- **Math M2 #18 (csv 103)**: broken. The original image itself prints cx/3, so the equation as given has no constant term and no solution; with the evident fix c/3 the key 1464 (600 + 360 + 504) is correct, so the question is broken but fixable.
- **R&W M2 #15 (csv 758)**: broken. Broken: the stem comes from another question, B and C are duplicates, and D comes from the fish-vortex item, so although Plerogyra discus (maximum depth 15 m) is the intended answer, no single letter is uniquely correct; I merged the duplicate issue reports, and the original choices C and D must be restored from the source.

## Yellow

- solver medium: 8
- solver disagrees with the key: 2
- content: typo: 1
- content: ambiguous: 1
- transcription medium: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 91, medium 5, low 2.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 89, medium 7, low 2.
- Both disagree with the bank key: 2 (Math M2 #18 (csv 103); R&W M2 #15 (csv 758)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 32; kept as figures 4 (geometry 2, graph 2), the rest turned into text.
- Upscaled for the models: 28.

## Explanations

- Bank explanation: usable 79, minor_issue 13, wrong 2, mismatch 1, missing 3.
- Final: drafted 45, kept from the bank 53.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 573,181 | $1.60 |
| solve_a | opus | 10 | 529,207 | $2.96 |
| solve_b | sonnet | 10 | 527,970 | $1.48 |
| explain | sonnet | 10 | 634,470 | $1.78 |
| adjudicate | opus | 3 | 199,542 | $1.12 |
| **Subagents** | | 43 | **2,464,370** | **$8.94** |

Per question ≈ 25,146 tokens, ≈ $0.091 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- Only 20 subagents can run at once, so the 10 explain batches were launched as solve agents finished.
- prep reported 1 problem in the source rows (see report.md if it affects a question).
- No batch needed a re-run.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #3 (csv 47)** (yellow, no change, high): No change needed: the question is clear and key D is right; the second solver simply mis-added 25 + 24.
- **Math M1 #8 (csv 53)** (yellow, corrected, high): Fixed the typo "values of a" to "values of x" (and set x and y in math); the choice tables match the original screenshots exactly.
- **Math M1 #22 (csv 67)** (yellow, no change, high): No change needed: g(x) = x/m + 21 reads unambiguously as (x/m) + 21, and all four correct values are already accepted.
- **Math M2 #10 (csv 95)** (red, restored, high): As printed, b was undetermined (y = 0, a = 27/5 works for any b); restored the standard condition "the system has infinitely many solutions" that the key and explanation assume, and rewrote the explanation to match.
- **Math M2 #15 (csv 100)** (red, corrected, restored, medium): Defined the missing a as the leading coefficient in f(x) = a(x - 2)^2 + 10 (the reading the key requires), fixed the grammar ("graphs", "parabolas", "y-intercepts") and set the math in LaTeX; explanation updated to drop the guess about a.
- **Math M2 #17 (csv 102)** (yellow, corrected, invented, high): Fixed the grammar and changed "One of x-intercept" to "The other x-intercept" so c can only be 11, and dropped -5 from the accepted answers.
- **Math M2 #18 (csv 103)** (red, invented, high): The original prints cx/3 as the last term, which leaves no constant term to match 168; changed it to c/3 so the identity holds and the key 1464 works, and removed the explanation's note about the misprint.
- **R&W M1 #14 (csv 68)** (yellow, corrected, high): Replaced the hyphen in "English-one" with an em dash; the question and key are otherwise fine.
- **R&W M1 #21 (csv 75)** (yellow, no change, high): No change needed: the solver was unsure, but the blank's antecedent is the plural "the artworks", so the question is clear and the key A is right.
- **R&W M1 #24 (csv 78)** (yellow, corrected, high): Fixed "mezzo- soprano", restored the em dashes around the "from ... to ..." aside, and italicized the Italian terms.
- **R&W M2 #6 (csv 87)** (yellow, no change, high): No change needed: the solvers were only moderately sure, but the question is clear and B is the only choice that challenges the underlined claim that the honor is well known among tourists.
- **R&W M2 #14 (csv 759)** (yellow, corrected, high): Restored the missing opening article "A" at the start of every choice; the content and key are unchanged.
- **R&W M2 #15 (csv 758)** (red, corrected, invented, medium): Replaced the stem borrowed from the fish-vortex question with the table-completion stem, added the blank, fixed "si" to "is", and wrote new choices C and D (C was a duplicate of B, D came from another question) using the table's other species so only B fits.
- **R&W M2 #27 (csv 106)** (yellow, corrected, high): Restored the missing opening word "A" in choices A and B; the meaning and key are unchanged.
