# DAY26 AI review

Test ids DAY26: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 40 | 8 | 6 | 54 |
| Math | 41 | 2 | 1 | 44 |
| **Total** | **81** | **10** | **7** | **98** |

Verdicts: key_correct 93, key_wrong 4, broken 1. Adjudicated: 19.

## Red: a teacher decides before publishing

- **Math M2 #15 (csv 1322)**: key_wrong. Key 270 → 240. Key 270 is wrong: the marked points (-8, 12) and (0, 1) give slope -11/8, so line k is 165x + 120y = 120 and p + w = 240; the bank used a slope of -11/9.
- **R&W M1 #5 (csv 1665)**: key_correct. Key A stands: the underlined sentence extends feathers beyond the winged dinosaurs mentioned first, and solver 2 credited it with the Yutyrannus example that comes in the following sentence; the blocking missing_info issue is dropped because the passage is complete enough to answer (only the final period is missing), the explanation-name mismatch is dropped as an explanation problem, and the explanation is rewritten to stop naming a dinosaur the passage does not mention.
- **R&W M1 #13 (csv 1673)**: key_correct. Key A stands: only A ties the clothing to a change in her sense of self; the missing_info issue is dropped because the passage ending in "writing," is the standard lead-in to the quotation in the choices, so the claim is complete.
- **R&W M1 #17 (csv 1677)**: broken. The transcription matches the bank image, but the printed sentence is defective because no choice yields a grammatical sentence with "catching—an in-person glimpse" (D is the intended answer); the separate off_format issue is dropped since the dash is in the original, not a transcription error.
- **R&W M2 #14 (csv 2269)**: key_wrong. Key B → A. Key B is wrong: the possessor of the peer republics is the singular "the Karelian Republic," so pronoun-antecedent agreement requires "its" (A).
- **R&W M2 #15 (csv 2270)**: key_wrong. Key C → D. Key C is wrong: the blank continues the participial modifier "enacted in 1987 and ______", so only the parallel participle "containing" (D) is grammatical.
- **R&W M2 #18 (csv 2273)**: key_wrong. Key D → A. Key D is wrong: the semicolon after the blank is already printed, so D creates a double semicolon and only "pristine, though" (A) is grammatical.

## Yellow

- solver medium: 8
- solver disagrees with the key: 2

## Solvers

- solve_a (opus): disagrees with the bank key on 4, with the final key on 0; confidence high 96, medium 2, low 0.
- solve_b (sonnet): disagrees with the bank key on 5, with the final key on 5; confidence high 89, medium 8, low 1.
- Both disagree with the bank key: 2 (Math M2 #15 (csv 1322); R&W M2 #18 (csv 2273)).
- The two solvers disagree with each other: 5.

## Transcription

- Confidence: high 94, medium 2, low 2.
- Question and choice images: 136; kept as figures 4 (graph 2, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 74.

## Explanations

- Bank explanation: usable 72, minor_issue 20, wrong 5, mismatch 1, missing 0.
- Final: drafted 51, kept from the bank 47.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 848,387 | $2.38 |
| solve_a | opus | 10 | 730,464 | $4.09 |
| solve_b | sonnet | 10 | 729,983 | $2.04 |
| explain | sonnet | 10 | 839,929 | $2.35 |
| adjudicate | opus | 4 | 332,327 | $1.86 |
| **Subagents** | | 44 | **3,481,090** | **$12.72** |

Per question ≈ 35,521 tokens, ≈ $0.130 at API list prices (90/10 input/output split assumed; the main session is not included).
