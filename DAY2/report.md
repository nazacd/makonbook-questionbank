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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #3 (csv 548)** (red, invented, medium): Wrote a stem from the bank explanation's reading (y is the height, 61; x is the length, 3 times the height) because the bank has no question text, and rewrote the explanation that said the text was missing. **A person must:** The original question text is missing from the bank; the stem was rebuilt from the bank explanation (height y = 61, length x = 3 times the height). Check it against the source if one is available.
- **Math M2 #2 (csv 524)** (yellow, corrected, invented, high): Fixed the typo "substracting" and replaced distractors 50 and 61 with 55 (A's intercept) and 66 (adding 11), because as drawn B's intercept is about 44, which was nearly as close to 50 as to the key 39. **A person must:** Remove the stray thin curved line at the top right of the scatterplot image (a drawing artifact, not data).
- **Math M2 #18 (csv 540)** (yellow, no change, high): No change needed: the choices we hold already match the choice images (the CSV mismatch was fixed earlier), the equation matches the question image, and key B is right.
- **R&W M1 #16 (csv 718)** (yellow, corrected, high): Replaced the transition stem with the standard conventions stem, because the choices differ only in apostrophes and plurals.
- **R&W M1 #27 (csv 729)** (yellow, restored, high): Restored the missing opening word "A" in choice B, which began "stunning example" with no article or capital.
- **R&W M2 #6 (csv 735)** (yellow, no change, high): No change needed: the solver was only medium-confident, but the passage, choices and key are clear and correct.
- **R&W M2 #18 (csv 747)** (red, corrected, high): Key set to B per the key_wrong verdict: after the indefinite "a ... oil painting" the title is a nonrestrictive appositive needing commas on both sides; explanation written for key B.
- **R&W M2 #20 (csv 749)** (yellow, no change, high): No change needed: a solver picked C, but C creates a comma splice, and D correctly uses a colon after a complete clause to introduce an explanatory sentence.
- **R&W M2 #21 (csv 750)** (yellow, no change, high): No change needed: the solver was only medium-confident, but the question is clear and the key is right.
