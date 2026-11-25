# DAY33 AI review

Test ids DAY33: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 37 | 14 | 3 | 54 |
| Math | 37 | 5 | 2 | 44 |
| **Total** | **74** | **19** | **5** | **98** |

Verdicts: key_correct 93, broken 2, key_wrong 2, ambiguous 1. Adjudicated: 27.

## Red: a teacher decides before publishing

- **Math M2 #14 (csv 1506)**: broken. Broken because choices C and D are blank; the math supports A (removing the maximum 78.2 lowers the mean, but the 5th and 6th values both lie in the 50-55 bin so the median need not drop), and the standard missing choices are proposed.
- **Math M2 #18 (csv 1510)**: key_wrong. Key A → C. Key A gives only the upper bound; x = 1 satisfies it but cannot form a triangle with 8 and 13, so the correct answer is C (5 < x < 21).
- **R&W M1 #10 (csv 1812)**: key_wrong. Key A → C. Key A is an unsupported inference about how many categories individuals choose, while C is directly confirmed by the table (58 > 53, 56 < 63), so the key should be C.
- **R&W M1 #23 (csv 1825)**: ambiguous. Marked ambiguous: the second sentence restates the first (the two functions become 'bifunctional'), so 'That is,' is very likely the intended answer, but 'Moreover' does not strictly contradict the text, so a key change to C is proposed for a teacher to approve.
- **R&W M2 #17 (csv 1846)**: broken. Broken: the printed passage already contains the period and closing quotation mark after the blank, which makes key C impossible and turns D into the only fit, so the passage was evidently corrupted from the version the key was written for; a teacher should restore the original sentence boundary.

## Yellow

- solver medium: 15
- solver disagrees with the key: 4
- content: image_text_mismatch: 1
- content: choice_formatting: 1
- transcription medium: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 5, with the final key on 3; confidence high 92, medium 6, low 0.
- solve_b (sonnet): disagrees with the bank key on 7, with the final key on 5; confidence high 86, medium 12, low 0.
- Both disagree with the bank key: 4 (Math M2 #18 (csv 1510); R&W M1 #10 (csv 1812); R&W M1 #23 (csv 1825); R&W M2 #17 (csv 1846)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 79; kept as figures 8 (geometry 3, graph 2, chart 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 71.

## Explanations

- Bank explanation: usable 58, minor_issue 18, wrong 15, mismatch 3, missing 4.
- Final: drafted 56, kept from the bank 42.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 785,548 | $2.20 |
| solve_a | opus | 10 | 723,755 | $4.05 |
| solve_b | sonnet | 10 | 720,325 | $2.02 |
| explain | sonnet | 10 | 844,221 | $2.36 |
| adjudicate | opus | 5 | 424,295 | $2.38 |
| **Subagents** | | 45 | **3,498,144** | **$13.01** |

Per question ≈ 35,695 tokens, ≈ $0.133 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Source row issue: math-m2-14 has empty choices C and D in the bank export (blocking missing_choice flagged at prep).
