# DAY2 AI review

Test ids DAY2: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 48 | 5 | 1 | 54 |
| Math | 41 | 2 | 1 | 44 |
| **Total** | **89** | **7** | **2** | **98** |

Verdicts: key_correct 96, broken 1, key_wrong 1. Adjudicated: 16.

## Red: a teacher decides before publishing

- **Math M1 #3 (csv 548)**: broken. Broken: the stem is missing from the bank (no text, no image), so no key can be checked; the three missing_info issues were the same defect and are merged into one.
- **R&W M2 #18 (csv 747)**: key_wrong. Key C → B. Key changed from C to B: after the indefinite phrase "a ... oil painting" the title is a nonrestrictive appositive that needs a comma on each side, which only B provides.

## Yellow

- solver medium: 3
- content: other: 1
- solver low: 1
- content: image_text_mismatch: 1
- content: off_format: 1
- content: typo: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 1; confidence high 95, medium 1, low 2.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 3; confidence high 93, medium 4, low 1.
- Both disagree with the bank key: 1 (Math M1 #3 (csv 548)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 97, medium 0, low 1.
- Question and choice images: 28; kept as figures 11 (graph 4, geometry 4, chart 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 26.

## Explanations

- Bank explanation: usable 48, minor_issue 38, wrong 11, mismatch 1, missing 0.
- Final: drafted 54, kept from the bank 44.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 11 | 646,875 | $1.81 |
| solve_a | opus | 10 | 544,605 | $3.05 |
| solve_b | sonnet | 10 | 540,689 | $1.51 |
| explain | sonnet | 14 | 851,842 | $2.39 |
| adjudicate | opus | 4 | 258,074 | $1.45 |
| **Subagents** | | 49 | **2,842,085** | **$10.21** |

Per question ≈ 29,000 tokens, ≈ $0.104 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- math-m1-03: the bank row has no question text and no image, only four answer choices. Transcribe math-m1-a was re-run once ("empty stem"); the stem now holds a placeholder marker, not bank text. The question is blocking and needs its source text restored.
- Explain re-run once for math-m1-a, math-m2-b, english-m1-b and english-m1-c because their issue entries used invalid kinds, severities or sources. explain.md says "use the same kinds as transcription" but doesn't list them.
- english-m1-16: on re-run the explain agent dropped its issue instead of fixing it. The stem asks for the "most logical transition", but the question tests apostrophes. A teacher should check the stem.
- Adjudicate adj-3 was re-run once because english-m2-18 had an issue with no kind or detail.
- No R2 objects were missing. All other batches passed on the first run.
