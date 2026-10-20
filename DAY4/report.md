# DAY4 AI review

Test ids DAY4: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 48 | 5 | 1 | 54 |
| Math | 39 | 3 | 2 | 44 |
| **Total** | **87** | **8** | **3** | **98** |

Verdicts: key_correct 95, ambiguous 2, broken 1. Adjudicated: 15.

## Red: a teacher decides before publishing

- **Math M1 #3 (csv 154)**: ambiguous. Every recorded temperature satisfies both A (40 <= t <= 90) and D (t <= 90), so as worded the question has two correct choices; a teacher should reword the stem or replace choice D.
- **Math M1 #8 (csv 159)**: ambiguous. The bank explanation's points (0, 2) and (2, 12) are not on the drawn line, and my reading (y-intercept about 5, x-intercept about -0.8, endpoints near (-1.45, -4) and (1.25, 12)) favors slope 6 and answer B, but the distorted photo does not allow a rigorous proof against A, so a teacher should check against a clean source figure.
- **R&W M1 #12 (csv 172)**: broken. Broken: key A claims Allentown-Bethlehem's delay rose from 1990 to 2000, but the graph shows it fell (about 40 to 34), so no choice is both accurate and supportive; A works if it names Beaumont, Texas, which rose from about 18 to 32 while staying below New York; the duplicate D typo issue was merged and downgraded to cosmetic because D is wrong either way.

## Yellow

- solver medium: 8
- solver disagrees with the key: 3
- content: choice_formatting: 1
- transcription medium: 1
- content: grammar: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 93, medium 4, low 1.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 90, medium 8, low 0.
- Both disagree with the bank key: 2 (Math M1 #8 (csv 159); Math M1 #12 (csv 661)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 27; kept as figures 5 (graph 2, scatterplot 1, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 26.

## Explanations

- Bank explanation: usable 76, minor_issue 14, wrong 8, mismatch 0, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 575,610 | $1.61 |
| solve_a | opus | 10 | 534,415 | $2.99 |
| solve_b | sonnet | 10 | 533,758 | $1.49 |
| explain | sonnet | 10 | 668,823 | $1.87 |
| adjudicate | opus | 3 | 196,261 | $1.10 |
| **Subagents** | | 43 | **2,508,867** | **$9.07** |

Per question ≈ 25,600 tokens, ≈ $0.093 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #3 (csv 154)** (red, invented, corrected, high): Replaced choice D (t <= 90, also true for every recorded temperature) with t >= 90 so only A is true, and fixed the stray space in "( °F)".
- **Math M1 #8 (csv 159)** (red, redrawn, invented, medium): The photo was too distorted to tell slope 5 (key A) from slope 6 (choice B), and the bank explanation argued B; redrew line n through (-1, 0), (0, 5) and (1, 10) so slope 5 is exact and key A stands, and rewrote the explanation to match. **A person must:** A teacher should confirm the redrawn graph against a clean copy of the source: the original photo is skewed and its line could be read as slope 5 or 6; it was redrawn with slope 5 to match key A.
- **Math M1 #12 (csv 661)** (yellow, corrected, high): Wrote the condition d > 5/9c as d > (5/9)c so it cannot be read as 5/(9c); choices C and D already put the whole expression under the radical, which is what the original intends.
- **Math M2 #21 (csv 192)** (yellow, no change, high): No change needed: the transcription matches the original and the key is right; the second solver's choice A does not satisfy the equation.
- **Math M2 #22 (csv 193)** (yellow, no change, high): No change needed: the figure is clear, the stem matches it, and the reasoning confirms key B.
- **R&W M1 #5 (csv 165)** (yellow, corrected, high): Replaced the hyphen and spaced dash around "up to 97 kilometers per hour (km/hr)" with em dashes, and added the missing article to choices A and C so all four choices fit "largely ______ of the fact".
- **R&W M1 #12 (csv 172)** (red, corrected, invented, high): Key A named Allentown-Bethlehem, whose delay fell from about 40 to about 34 hours, so A now names Beaumont, Texas, which rose from about 18 to 32 while staying below New York City; also fixed "200" to "2000" in D. **A person must:** Optional: the graph legend reads "New York City; New York" and "Allentown-Bethlehem; Pennsylvania" with semicolons instead of commas. The bar values cannot be read exactly enough to redraw the graph.
- **R&W M1 #14 (csv 174)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear, and key A follows from birds spreading more seeds from abundant non-native plants.
- **R&W M1 #18 (csv 178)** (yellow, corrected, high): Removed the stray quote mark at the start of the stem, made the dashes around the example list matching em dashes, and fixed the OCR slip "Katle" to "Katie".
- **R&W M2 #24 (csv 211)** (yellow, corrected, high): Added the missing space between the blank and "volcanologists"; otherwise the question is clear and key D is right.
- **R&W M2 #25 (csv 212)** (yellow, no change, high): No change needed: the review flagged only solver uncertainty, but the passage and choices are clean and key D is right.
