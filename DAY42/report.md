# DAY42 AI review

Test ids DAY42: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 7 | 1 | 54 |
| Math | 42 | 1 | 1 | 44 |
| **Total** | **88** | **8** | **2** | **98** |

Verdicts: key_correct 96, broken 2. Adjudicated: 15.

## Red: a teacher decides before publishing

- **Math M2 #4 (csv 1902)**: broken. Broken: A (w = -188vx) is the correct algebra, but the original choice images for C and D are duplicates and the stem's 'positive numbers' contradicts the negative sign; the second duplicate_choice issue was merged as a repeat.
- **R&W M2 #16 (csv 2384)**: broken. As printed the passage already ends the sentence after the blank (".” In 1960"), so every choice doubles the punctuation and the solvers fell back to B; with the intended text "______ in 1960, for instance, judges recognized..." two independent clauses meet and key D's semicolon is correct, so the passage needs the proposed fix.

## Yellow

- solver medium: 7
- content: missing_info: 2
- transcription medium: 2
- content: image_text_mismatch: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 95, medium 2, low 1.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 93, medium 5, low 0.
- Both disagree with the bank key: 1 (R&W M2 #16 (csv 2384)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 104; kept as figures 7 (geometry 3, graph 2, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 97.

## Explanations

- Bank explanation: usable 74, minor_issue 15, wrong 5, mismatch 3, missing 1.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 771,558 | $2.16 |
| solve_a | opus | 10 | 694,590 | $3.89 |
| solve_b | sonnet | 10 | 692,929 | $1.94 |
| explain | sonnet | 10 | 820,074 | $2.30 |
| adjudicate | opus | 3 | 242,487 | $1.36 |
| **Subagents** | | 43 | **3,221,638** | **$11.64** |

Per question ≈ 32,873 tokens, ≈ $0.119 at API list prices (90/10 input/output split assumed; the main session is not included).
