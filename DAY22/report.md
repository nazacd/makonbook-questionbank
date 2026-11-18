# DAY22 AI review

Test ids DAY22: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 40 | 10 | 4 | 54 |
| Math | 39 | 4 | 1 | 44 |
| **Total** | **79** | **14** | **5** | **98** |

Verdicts: key_correct 93, ambiguous 2, key_wrong 2, broken 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M1 #11 (csv 1075)**: ambiguous. Ambiguous: without a figure or a statement that B lies between A and C, both 5pi = 15pi/3 (C, the key) and 5pi/3 (A) are offered and defensible; the duplicate ambiguity issue was merged into one.
- **R&W M1 #18 (csv 1350)**: key_wrong. Key D → A. Key D is wrong because singular "helps" does not agree with the plural compound subject "determination and perseverance"; A "helped" is the only choice giving a grammatical finite verb, as both solvers found.
- **R&W M1 #21 (csv 1359)**: ambiguous. Ambiguous: SAT convention favors A, but D ("classical authors, however; many...") is also grammatical with "however" closing the first clause and is arguably more logical, so the key cannot be proven wrong and a teacher should decide.
- **R&W M2 #12 (csv 1371)**: key_wrong. Key A → B. Key A is wrong: A's finding of lower oxalic acid and trypsin inhibitors after soaking supports the claim, while B's finding of no significant effect directly weakens it, so the key should be B.
- **R&W M2 #17 (csv 1376)**: broken. Broken: the comma after the blank is in the bank's own image, not a transcription error, and with it B yields a doubled comma while C becomes correct; removing that comma restores B as the only correct answer.

## Yellow

- solver medium: 13
- transcription medium: 2
- solver disagrees with the key: 2
- content: image_text_mismatch: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 1; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 4; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 3 (R&W M1 #18 (csv 1350); R&W M1 #21 (csv 1359); R&W M2 #12 (csv 1371)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 120; kept as figures 0 (none), the rest turned into text.
- Upscaled for the models: 52.

## Explanations

- Bank explanation: usable 68, minor_issue 18, wrong 8, mismatch 3, missing 1.
- Final: drafted 52, kept from the bank 46.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 817,126 | $2.29 |
| solve_a | opus | 10 | 720,327 | $4.03 |
| solve_b | sonnet | 10 | 717,523 | $2.01 |
| explain | sonnet | 10 | 882,075 | $2.47 |
| adjudicate | opus | 5 | 437,160 | $2.45 |
| **Subagents** | | 45 | **3,574,211** | **$13.25** |

Per question ≈ 36,471 tokens, ≈ $0.135 at API list prices (90/10 input/output split assumed; the main session is not included).
