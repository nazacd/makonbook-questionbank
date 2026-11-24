# DAY24 AI review

Test ids DAY24: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 38 | 12 | 4 | 54 |
| Math | 42 | 1 | 1 | 44 |
| **Total** | **80** | **13** | **5** | **98** |

Verdicts: key_correct 93, ambiguous 4, key_wrong 1. Adjudicated: 22.

## Red: a teacher decides before publishing

- **Math M2 #22 (csv 1063)**: ambiguous. Ambiguous: with angles Q=N and R=O, both PQ/MN (A, by AAS) and QR/NO (C, by ASA) are corresponding sides that settle congruence; the grammar issue is narrowed to choice B's number agreement, since noun-phrase choices are normal for an "which piece of information" stem.
- **R&W M1 #5 (csv 1283)**: key_wrong. Key D → A. Key D is wrong because the text never mentions the decision's impact on civil rights or takes a celebratory tone; it neutrally recounts the Plessy-to-Brown history, so A is correct.
- **R&W M1 #8 (csv 1286)**: ambiguous. Ambiguous, not provably wrong: both solvers chose A at medium confidence because the excerpt never shows an "impact on their journey" (C), but the intro's framing about "subsequent impact on their journey" partly supports C, and A's "path not chosen" also goes beyond the excerpt, so a teacher should decide.
- **R&W M1 #26 (csv 1304)**: ambiguous. Ambiguous: B is grounded in the notes ("monolithic" means carved from a single stone, and size and weight are what make production and transport baffling), but D's "walking" mystery is just as defensible, so a teacher should decide.
- **R&W M2 #8 (csv 1313)**: ambiguous. Ambiguous: a finding of no quality difference would lead the researchers to downplay Text 1's concern, which C does not do, but A adds unsupported claims about training and oversight, so neither choice can be proven correct.

## Yellow

- solver medium: 16
- transcription medium: 1
- content: typo: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 5, with the final key on 4; confidence high 88, medium 9, low 1.
- solve_b (sonnet): disagrees with the bank key on 5, with the final key on 4; confidence high 84, medium 12, low 2.
- Both disagree with the bank key: 4 (R&W M1 #5 (csv 1283); R&W M1 #8 (csv 1286); R&W M1 #26 (csv 1304); R&W M2 #8 (csv 1313)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 105; kept as figures 9 (graph 6, geometry 2, chart 1), the rest turned into text.
- Upscaled for the models: 72.

## Explanations

- Bank explanation: usable 72, minor_issue 17, wrong 7, mismatch 1, missing 1.
- Final: drafted 49, kept from the bank 49.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 808,841 | $2.26 |
| solve_a | opus | 10 | 737,971 | $4.13 |
| solve_b | sonnet | 10 | 730,335 | $2.04 |
| explain | sonnet | 10 | 855,594 | $2.40 |
| adjudicate | opus | 3 | 245,242 | $1.37 |
| **Subagents** | | 43 | **3,377,983** | **$12.21** |

Per question ≈ 34,469 tokens, ≈ $0.125 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

english-m1-a transcription needed 1 re-run (unbalanced bold marker in english-m1-09); explain math-m2-a needed 1 re-run (wrong skill tag on math-m2-08).
