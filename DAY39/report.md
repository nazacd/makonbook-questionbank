# DAY39 AI review

Test ids DAY39: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 43 | 9 | 2 | 54 |
| Math | 44 | 0 | 0 | 44 |
| **Total** | **87** | **9** | **2** | **98** |

Verdicts: key_correct 96, key_wrong 1, broken 1. Adjudicated: 12.

## Red: a teacher decides before publishing

- **R&W M2 #3 (csv 2156)**: key_wrong. Key D → B. Key changed from D to B: a confidence level of over 99% rules out claims that the event was ambiguous, while a certainty statistic cannot answer claims of inconspicuousness, and A and C do not fit; both solvers chose B.
- **R&W M2 #19 (csv 2172)**: broken. Broken: the bank's own text duplicates "conservation, though" after the blank and appears to have lost the second clause's subject (probably "efficiency, lowering the cost of use, may increase demand", which would make D correct), so a teacher must restore the passage; the earlier 'ambiguous' issue is replaced by this more precise blocking issue.

## Yellow

- solver medium: 9
- solver disagrees with the key: 2
- content: grammar: 1
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 1; confidence high 96, medium 1, low 1.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 2; confidence high 88, medium 9, low 1.
- Both disagree with the bank key: 1 (R&W M2 #3 (csv 2156)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 108; kept as figures 7 (graph 2, geometry 2, chart 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 66.

## Explanations

- Bank explanation: usable 72, minor_issue 21, wrong 5, mismatch 0, missing 0.
- Final: drafted 49, kept from the bank 49.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 801,952 | $2.25 |
| solve_a | opus | 10 | 732,241 | $4.10 |
| solve_b | sonnet | 10 | 730,042 | $2.04 |
| explain | sonnet | 10 | 856,714 | $2.40 |
| adjudicate | opus | 1 | 85,212 | $0.48 |
| **Subagents** | | 41 | **3,206,161** | **$11.27** |

Per question ≈ 32,715 tokens, ≈ $0.115 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **R&W M1 #5 (csv 2132)** (yellow, corrected, high): Added the missing article to choices A and D so every choice fits "is largely ______ of the fact" grammatically and grammar no longer points students toward B or C.
- **R&W M1 #8 (csv 2135)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the passage is clear and key A is right.
- **R&W M1 #11 (csv 2138)** (yellow, restored, high): Restored the missing conclusion sentence ending in a blank so the stem's "complete the conclusion" has something to complete, and italicized the species name in the passage; the table already matches the screenshot.
- **R&W M1 #24 (csv 2150)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the passage is clear and key C is right.
- **R&W M2 #1 (csv 2154)** (yellow, corrected, high): Replaced the straight single quotes around 'world' with standard double quotation marks; the stray quotes the review mentions around the passage are not in our version, and nothing else needed changing.
- **R&W M2 #3 (csv 2156)** (red, corrected, high): Key changed from the bank's D to B (ambiguity), as the review found, with the explanation rewritten for key B; our passage already has no stray quotation marks.
- **R&W M2 #8 (csv 2161)** (yellow, no change, high): No change needed: the passage matches the original screenshot word for word, and the question is clear with key A correct; the solver was only moderately confident.
- **R&W M2 #11 (csv 2164)** (yellow, no change, high): No change needed: the graph is clear and readable, the text matches it, and the current explanation already gives the correct reasoning for key B.
- **R&W M2 #13 (csv 2166)** (yellow, corrected, high): Formatting only: italicized the species names as the SAT does and added the missing period after the final blank; the content and key C are unchanged.
- **R&W M2 #19 (csv 2172)** (red, restored, invented, medium): Restored the second clause's subject: the bank text repeated "conservation, though" after the blank where "efficiency" belongs; changed distractor C from "conservation, though" (which could be read as a grammatical concessive clause) to "conservation though," so only D works, and rewrote the explanation.
- **R&W M2 #22 (csv 2175)** (yellow, no change, high): No change needed: the solvers were unsure, but the passage and choices are clean, the key D is right, and the current explanation already explains that the last sentence gives the overall tally.
