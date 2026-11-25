# DAY27 AI review

Test ids DAY27: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 41 | 11 | 2 | 54 |
| Math | 38 | 4 | 2 | 44 |
| **Total** | **79** | **15** | **4** | **98** |

Verdicts: key_correct 94, broken 2, key_wrong 2. Adjudicated: 22.

## Red: a teacher decides before publishing

- **Math M1 #4 (csv 1245)**: broken. Broken: the bank's own image shows sqrt(5x)+1, so g(7)=sqrt(35)+1 matches no choice; extending the radical over the +1 makes C (6) correct; the duplicate 'ambiguous' issue was dropped and merged into one blocking typo issue.
- **Math M2 #17 (csv 1280)**: key_wrong. Key 71 → 71/73. Key wrong: since each of the 73 angles is 180p, 73(180p) = 180(71) gives p = 71/73; the bank's 71 treats 180p as the angle sum, which would make each angle 12780 degrees.
- **R&W M1 #13 (csv 1598)**: broken. Broken: the table is cropped before the 2005–06 column that key D depends on, and the visible data (Neusiedl 77 to 50) cannot support D, so the question needs the full table restored.
- **R&W M2 #16 (csv 1628)**: key_wrong. Key D → C. Key changed from D to C: with no punctuation, "for" takes "its lush greenery" as its object and leaves the free-relative "what" without a gap, so "for" must close the clause and a colon must introduce the explanatory noun phrase, as both solvers found with high confidence.

## Yellow

- solver medium: 13
- content: image_text_mismatch: 3
- transcription medium: 3
- solver low: 3
- solver disagrees with the key: 3
- content: typo: 2
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 5, with the final key on 3; confidence high 93, medium 1, low 4.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 4; confidence high 83, medium 13, low 2.
- Both disagree with the bank key: 5 (Math M1 #4 (csv 1245); Math M2 #17 (csv 1280); R&W M1 #7 (csv 1592); R&W M1 #13 (csv 1598); R&W M2 #16 (csv 1628)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 93, medium 4, low 1.
- Question and choice images: 84; kept as figures 7 (geometry 2, graph 2, chart 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 74.

## Explanations

- Bank explanation: usable 66, minor_issue 19, wrong 8, mismatch 5, missing 0.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 809,484 | $2.27 |
| solve_a | opus | 10 | 730,256 | $4.09 |
| solve_b | sonnet | 10 | 723,536 | $2.03 |
| explain | sonnet | 10 | 854,711 | $2.39 |
| adjudicate | opus | 4 | 354,709 | $1.99 |
| **Subagents** | | 44 | **3,472,696** | **$12.76** |

Per question ≈ 35,435 tokens, ≈ $0.130 at API list prices (90/10 input/output split assumed; the main session is not included).
