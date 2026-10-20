# DAY11 AI review

Test ids DAY11: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 46 | 8 | 0 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **89** | **9** | **0** | **98** |

Verdicts: key_correct 98. Adjudicated: 15.

## Red: a teacher decides before publishing

None.

## Yellow

- solver medium: 10
- solver disagrees with the key: 3
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 1 (R&W M2 #21 (csv 477)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 21; kept as figures 6 (graph 3, geometry 2, chart 1), the rest turned into text.
- Upscaled for the models: 18.

## Explanations

- Bank explanation: usable 64, minor_issue 22, wrong 11, mismatch 0, missing 1.
- Final: drafted 50, kept from the bank 48.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 576,481 | $1.61 |
| solve_a | opus | 10 | 536,688 | $3.01 |
| solve_b | sonnet | 10 | 534,194 | $1.50 |
| explain | sonnet | 10 | 702,771 | $1.97 |
| adjudicate | opus | 3 | 194,242 | $1.09 |
| **Subagents** | | 43 | **2,544,376** | **$9.17** |

Per question ≈ 25,963 tokens, ≈ $0.094 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M2 #22 (csv 373)** (yellow, no change, high): No change needed: the text matches the original screenshot, the question is clear, and key B is right; the solvers were only moderately sure.
- **R&W M1 #11 (csv 442)** (yellow, restored, high): Restored the missing sentence with the blank that the choices complete, so students know what comparison they are finishing.
- **R&W M1 #19 (csv 450)** (yellow, no change, high): No change needed: the text is clean and key A is the only conventional punctuation; the solver was only moderately sure.
- **R&W M1 #21 (csv 452)** (yellow, no change, high): No change needed: the text is clean and key B is clearly the most logical transition; the solver was only moderately sure.
- **R&W M1 #24 (csv 455)** (yellow, corrected, high): Replaced the incorrect semicolon before the dependent clause 'whereas red foxes have only thirty-four' with a comma in choice B.
- **R&W M2 #8 (csv 466)** (yellow, no change, high): No change needed: the solvers were only moderately sure, but the paired texts and choices are clear and B is the only question both authors would answer the same way (no).
- **R&W M2 #14 (csv 472)** (yellow, corrected, high): Italicized the novel title in all four choices to match the passage, and rewrote the explanation in the bank's format with a closing answer line.
- **R&W M2 #19 (csv 475)** (yellow, no change, high): No change needed: one solver chose C, but the Italian festival is the example of her international reach, so A is the only logical and correctly punctuated choice, and the explanation already says so.
- **R&W M2 #21 (csv 477)** (yellow, corrected, high): Italicized the album title *Loud Jazz*; the solvers' disagreement does not reflect a flaw, since B is the only logical and correctly punctuated choice.
