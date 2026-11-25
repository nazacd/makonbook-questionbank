# DAY40 AI review

Test ids DAY40: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 41 | 12 | 1 | 54 |
| Math | 40 | 4 | 0 | 44 |
| **Total** | **81** | **16** | **1** | **98** |

Verdicts: key_correct 97, key_wrong 1. Adjudicated: 18.

## Red: a teacher decides before publishing

- **R&W M2 #3 (csv 2231)**: key_wrong. Key A → D. Key changed to D: the street art is offered as an addition to the museum's collection, so "supplement" is the precise word, while "satisfy" implies an unmet need the text never mentions; both solvers and the explanation check agree.

## Yellow

- solver medium: 13
- transcription medium: 4
- solver disagrees with the key: 2
- content: typo: 1
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 1; confidence high 94, medium 3, low 1.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 1; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 1 (R&W M2 #3 (csv 2231)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 94, medium 4, low 0.
- Question and choice images: 84; kept as figures 10 (geometry 5, graph 3, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 75.

## Explanations

- Bank explanation: usable 76, minor_issue 17, wrong 5, mismatch 0, missing 0.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 796,185 | $2.23 |
| solve_a | opus | 10 | 735,457 | $4.12 |
| solve_b | sonnet | 10 | 727,367 | $2.04 |
| explain | sonnet | 10 | 836,787 | $2.34 |
| adjudicate | opus | 3 | 256,769 | $1.44 |
| **Subagents** | | 43 | **3,352,565** | **$12.17** |

Per question ≈ 34,209 tokens, ≈ $0.124 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #9 (csv 1746)** (yellow, restored, corrected, high): Added the missing "Data Set X" title above the first table and changed "the table shown" to "the tables shown", since there are two tables.
- **Math M1 #16 (csv 1752)** (yellow, redrawn, high): Redrew the blurry graph, which had stray dashed lines from the screenshot crossing the grid, using the readable points (0, 300) and (1, 750) on the same axes and grid; text unchanged.
- **Math M1 #21 (csv 1757)** (yellow, no change, high): No change needed: the transcription matches the original and the key is right.
- **Math M2 #22 (csv 1781)** (yellow, corrected, high): Put the costs fully in math as \(\$46n\) and \(\$23n\) so a bare $ does not sit next to a math delimiter; wording and choices match the original.
- **R&W M1 #12 (csv 2213)** (yellow, no change, high): No change needed: the question is clear and the key is right; the review only flagged solver uncertainty.
- **R&W M1 #14 (csv 2215)** (yellow, no change, high): No change needed: the table transcription matches the original screenshot exactly and the key is right; the solver was only unsure.
- **R&W M1 #15 (csv 2216)** (yellow, no change, high): No change needed: the text is clear and complete and key A is right; the solver was only unsure.
- **R&W M1 #23 (csv 2224)** (yellow, no change, high): No change needed: the question is clear and key A is right; one solver's disagreement does not hold up.
- **R&W M1 #24 (csv 2225)** (yellow, no change, high): No change needed: the question is clear and key C is right; the solver was only unsure.
- **R&W M2 #3 (csv 2231)** (red, corrected, high): Changed the key from A to D per the key_wrong verdict (the street art adds to the museum's collection, so "supplement" is the precise word) and rewrote the explanation for the new key.
- **R&W M2 #5 (csv 2233)** (yellow, no change, high): No change needed: the transcription and underlining match the original screenshot, and the key is right; the solver was only unsure.
- **R&W M2 #10 (csv 2238)** (yellow, no change, high): No change needed: the text matches, the graph is clear and readable, and the key is right; the solver was only unsure.
- **R&W M2 #14 (csv 2242)** (yellow, corrected, high): Corrected the typo "in the region about otherwise unrelated" to "in the region but otherwise unrelated".
- **R&W M2 #19 (csv 2247)** (yellow, no change, high): No change needed: the question is clear and the key is right; the solver was only unsure.
- **R&W M2 #20 (csv 2248)** (yellow, no change, high): No change needed: the question is clear and the key is right; the solver was only unsure.
- **R&W M2 #22 (csv 2250)** (yellow, invented, high): Replaced the key's wording "Then," with "Instead," (key letter unchanged) because "Then," only weakly fits and led a solver to prefer "With this in mind,"; "Instead," clearly signals the shredded paper replaced the retired ticker tape.
- **R&W M2 #26 (csv 2254)** (yellow, no change, high): No change needed: the transcription matches the screenshot word for word, and the key C is the only choice that presents the findings without defining a concept the audience already knows.
