# DAY36 AI review

Test ids DAY 36: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 49 | 4 | 1 | 54 |
| Math | 44 | 0 | 0 | 44 |
| **Total** | **93** | **4** | **1** | **98** |

Verdicts: key_correct 97, ambiguous 1. Adjudicated: 5.

## Red: a teacher decides before publishing

- **R&W M2 #19 (csv 3741)**: ambiguous. Both solvers, with high confidence, and my own solve pick C, because "the former in ... and the latter in ..." has no finite verb and is an absolute phrase that takes a comma; but some style guides allow a semicolon before an elliptical (gapped) clause, so key A is not strictly disproven and a teacher should confirm the change to C.

## Yellow

- solver medium: 3
- content: unreadable_image: 1
- transcription medium: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 98, medium 0, low 0.
- solve_b (sonnet): disagrees with the bank key on 1, with the final key on 1; confidence high 95, medium 3, low 0.
- Both disagree with the bank key: 1 (R&W M2 #19 (csv 3741)).
- The two solvers disagree with each other: 0.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 16; kept as figures 6 (geometry 3, scatterplot 1, graph 1, chart 1), the rest turned into text.
- Upscaled for the models: 13.

## Explanations

- Bank explanation: usable 0, minor_issue 0, wrong 0, mismatch 0, missing 98.
- Final: drafted 98, kept from the bank 0.

## Usage

Not logged.
