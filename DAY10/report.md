# DAY10 AI review

Test ids DAY10: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 34 | 19 | 1 | 54 |
| Math | 40 | 3 | 1 | 44 |
| **Total** | **74** | **22** | **2** | **98** |

Verdicts: key_correct 96, broken 2. Adjudicated: 26.

## Red: a teacher decides before publishing

- **Math M1 #8 (csv 291)**: broken. The figure is defective: line n can be read as passing through (-1, 0) and (0, 5) (slope 5, key A) or through (0, 5) and (1, 11) (slope 6, B), and a pixel fit gives slope about 5.6, so neither key can be proven; the wrong_key issue was dropped because the key cannot be proven wrong, and the figure needs to be redrawn.
- **R&W M2 #17 (csv 421)**: broken. Marked broken because choices B and D are identical in the bank, but the key C is still right (a title before a name takes no commas, and no comma goes between subject and verb), so the proposed fix makes D a distinct wrong choice.

## Yellow

- solver medium: 16
- content: typo: 9
- transcription medium: 5
- solver disagrees with the key: 4
- content: grammar: 3
- content: image_text_mismatch: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 86, medium 12, low 0.
- Both disagree with the bank key: 2 (Math M1 #8 (csv 291); R&W M2 #21 (csv 425)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 92, medium 6, low 0.
- Question and choice images: 24; kept as figures 5 (graph 3, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 24.

## Explanations

- Bank explanation: usable 56, minor_issue 37, wrong 5, mismatch 0, missing 0.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 581,465 | $1.63 |
| solve_a | opus | 10 | 534,768 | $2.99 |
| solve_b | sonnet | 10 | 533,396 | $1.49 |
| explain | sonnet | 10 | 619,730 | $1.74 |
| adjudicate | opus | 4 | 258,997 | $1.45 |
| **Subagents** | | 44 | **2,528,356** | **$9.30** |

Per question ≈ 25,799 tokens, ≈ $0.095 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

adj-1 adjudication agent hit an API rate limit at the end of its run; its output file was complete (6/6) and passed the stage check, token usage for adj-1 not logged.
Source row issue: english-m2-17 has identical choice text (duplicate_choice) in the bank.
