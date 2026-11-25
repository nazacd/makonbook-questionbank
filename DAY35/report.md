# DAY35 AI review

Test ids DAY35: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 44 | 9 | 1 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **87** | **10** | **1** | **98** |

Verdicts: key_correct 97, broken 1. Adjudicated: 23.

## Red: a teacher decides before publishing

- **R&W M1 #26 (csv 1935)**: broken. Broken: the attached image is the Boym notes from a different question, so the Basquiat sentences are missing (C is only inferable from the choices); the duplicate content-level missing_info issue was dropped as redundant with the blocking one.

## Yellow

- solver medium: 7
- solver disagrees with the key: 2
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 0, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 91, medium 7, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 97, medium 0, low 1.
- Question and choice images: 132; kept as figures 9 (graph 4, geometry 3, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 126.

## Explanations

- Bank explanation: usable 52, minor_issue 29, wrong 12, mismatch 1, missing 4.
- Final: drafted 58, kept from the bank 40.

## Usage

Not logged.
