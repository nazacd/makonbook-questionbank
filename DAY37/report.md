# DAY37 AI review

Test ids DAY37: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 8 | 0 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **89** | **9** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 12.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 7
- solver disagrees with the key: 4
- content: choice_formatting: 2
- solver low: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 96, medium 1, low 1.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 111; kept as figures 11 (geometry 4, chart 4, graph 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 101.

## Explanations

- Bank explanation: usable 67, minor_issue 22, wrong 9, mismatch 0, missing 0.
- Final: drafted 47, kept from the bank 51.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 802,284 | $2.25 |
| solve_a | opus | 10 | 740,373 | $4.15 |
| solve_b | sonnet | 10 | 736,519 | $2.06 |
| explain | sonnet | 10 | 857,038 | $2.40 |
| adjudicate | opus | 1 | 84,902 | $0.48 |
| **Subagents** | | 41 | **3,221,116** | **$11.33** |

Per question ≈ 32,868 tokens, ≈ $0.116 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

An explain agent (english-m1-c) reported that it re-ran a shared scratch script and regenerated the explain output of math-m2-a from another agent's script; the content should be unchanged but a teacher may want to spot-check math-m2-a explanations.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #22 (csv 1671)** (yellow, corrected, high): The question and figure match the original and the key is right; added the valid entry ".866" to the accepted list and updated the explanation to list every accepted form.
- **R&W M1 #13 (csv 2032)** (yellow, corrected, high): Changed the single quotes around 'Sad but True' in the passage to double quotes to match the choices; the question is otherwise clear and the key is right.
- **R&W M1 #14 (csv 2034)** (yellow, corrected, high): Lowercased the first word of choices A, B and D so they complete the sentence after "imply that," and made the blank the standard six underscores.
- **R&W M1 #25 (csv 2068)** (yellow, restored, high): Restored the dropped opening word "A" in choices A and D, which began mid-sentence.
- **R&W M2 #3 (csv 2087)** (yellow, restored, high): Restored the missing article "a" in choices A and C so all four choices fit "is largely ______ of the fact" and match the explanation's "a consequence."
- **R&W M2 #12 (csv 2102)** (yellow, no change, high): No change needed: the text and graph match the original, the graph is clear, and the current explanation already respects the assumption that P1's ratings were equal.
- **R&W M2 #13 (csv 2103)** (yellow, corrected, medium): Italicized the novel title *My Name Is Red* in all four choices to match the passage, and rewrote the explanation to give clear reasons for each choice.
- **R&W M2 #21 (csv 2121)** (yellow, corrected, high): Changed the five-underscore blank to the standard six and removed the period after it, since every choice already ends with a period.
- **R&W M2 #23 (csv 2122)** (yellow, corrected, medium): Changed the five-underscore blank to the standard six; the question is otherwise fine and the key stands.
