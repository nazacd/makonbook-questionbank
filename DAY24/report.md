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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M2 #15 (csv 1056)** (yellow, redrawn, high): The text and key are right; the original screenshot also contains the stem sentence, so the student saw it twice, and the triangle is redrawn exactly (same labels and right angle) without the duplicated text.
- **Math M2 #22 (csv 1063)** (red, corrected, invented, high): Choice C (sides QR and NO) was also sufficient, so it is replaced with an angle fact that is already determined and gives no size information; choice B's grammar is fixed to "The measures of angles P and M".
- **R&W M1 #2 (csv 1280)** (yellow, no change, high): No change needed: the solver was unsure, but the text sets up comfort as the goal, so "more unsettled than soothed" is clearly the only logical completion and the key A is right.
- **R&W M1 #3 (csv 1281)** (yellow, invented, medium): "conventions" is close enough to "customs" that a strong student could defend it for informal social practices, so it is replaced with "statutes", a plausible but clearly wrong word (shaming and exclusion are not formal laws).
- **R&W M1 #5 (csv 1283)** (red, corrected, high): The bank's key D (celebrating the impact on civil rights) is unsupported by the neutral two-sentence text, so the key is set to A as the review found, with a new explanation for A.
- **R&W M1 #8 (csv 1286)** (red, invented, high): A and C both partly fit (A matched "sorry I could not travel both" better than key C, whose "impact on their journey" is not in the excerpt), so I rewrote C to state the excerpt's idea and made A a clear misreading (regretting a choice not yet made), keeping the key at C.
- **R&W M1 #9 (csv 1287)** (yellow, corrected, restored, high): Removed the stray "**" after the underlined sentence in Text 1 and restored the missing leading "A" in choice A.
- **R&W M1 #11 (csv 1289)** (yellow, no change, high): No change needed: the solvers were only medium-confident, but C is the only quotation showing both longing for lasting love and human transience ("fleeting shadows"), and the text is clean.
- **R&W M1 #20 (csv 1298)** (yellow, no change, high): No change needed: the question is clear and key B is right; the solver was only medium-confident.
- **R&W M1 #23 (csv 1301)** (yellow, no change, high): No change needed: the question is clear and key B is right; the solver was only medium-confident.
- **R&W M1 #26 (csv 1304)** (red, invented, medium): The original B (an ungrammatical size fact plus an unsupported 'single slab' claim) did not highlight anything surprising while D's 'walking' mystery did, so I rewrote B to state from the notes that production and transport still baffle scientists, and replaced D with a non-surprising production fact (tuff) so B is the only answer.
- **R&W M2 #1 (csv 1306)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the contrast with 'the absolute right to bear arms' makes 'regulations' clearly the one right word and the key is C.
- **R&W M2 #3 (csv 1308)** (yellow, no change, high): No change needed: the next sentence calls social capital 'an important resource,' which pins the blank to 'resources'; the key C is right and the question is clear.
- **R&W M2 #4 (csv 1309)** (yellow, no change, high): No change needed: the 'as a social construct, rather than a biological fact' frame requires 'viewed'; the key B is right and the question is clear.
- **R&W M2 #7 (csv 1312)** (yellow, no change, high): No change needed: 'revolutionized' is the only choice that takes 'the way people interact' as an object and describes a broad positive change before the 'However'; the key B is right.
- **R&W M2 #8 (csv 1313)** (red, invented, high): Rewrote key C so it follows directly from Text 2's finding (the concern may be unfounded for type 2 diabetes) instead of speculating about further research, and rewrote A so it contradicts the study instead of adding unsupported claims about training and oversight; the passage matches the original screenshot.
- **R&W M2 #12 (csv 1317)** (yellow, no change, medium): No change needed: the solvers were unsure, but only D sets an explicit negative feeling toward the city ("a cacophony that drowns the soul") against longing for the island "that made me whole"; A, B and C mainly voice nostalgia while describing the city neutrally.
- **R&W M2 #22 (csv 1327)** (yellow, no change, high): No change needed: the question is clear and the key is right, since the illusion exists in the present ("the armor is empty"), so the suit is made to look as if it "is" inhabited.
