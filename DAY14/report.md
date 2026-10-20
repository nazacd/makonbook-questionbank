# DAY14 AI review

Test ids DAY14: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 7 | 0 | 54 |
| Math | 34 | 8 | 2 | 44 |
| **Total** | **81** | **15** | **2** | **98** |

Verdicts: key_correct 96, key_wrong 1, ambiguous 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M1 #1 (csv 464)**: key_wrong. Key -22 → 9. Key -22 needs a^c = -15, impossible for an exponential base a > 0, so the only valid answer is 9 (both solvers agree); the duplicate typo issue was merged into one.
- **Math M1 #17 (csv 480)**: ambiguous. The system is undefined: all three equations share no point (A, as both solvers found), while f(x) with y = -3 or the two graphed lines meet once (key B), so a teacher must decide.

## Yellow

- solver medium: 12
- transcription medium: 3
- content: typo: 2
- content: other: 1
- content: ambiguous: 1
- solver disagrees with the key: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 1; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 2, with the final key on 2; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 1 (Math M1 #17 (csv 480)).
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 95, medium 3, low 0.
- Question and choice images: 37; kept as figures 5 (graph 3, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 34.

## Explanations

- Bank explanation: usable 74, minor_issue 14, wrong 8, mismatch 1, missing 1.
- Final: drafted 50, kept from the bank 48.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 563,034 | $1.58 |
| solve_a | opus | 10 | 516,743 | $2.89 |
| solve_b | sonnet | 10 | 514,723 | $1.44 |
| explain | sonnet | 10 | 648,448 | $1.82 |
| adjudicate | opus | 5 | 316,722 | $1.77 |
| **Subagents** | | 45 | **2,559,670** | **$9.50** |

Per question ≈ 26,119 tokens, ≈ $0.097 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

adj-4 re-run once: first output was missing english-m2-21; fixed on re-run.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #1 (csv 464)** (red, corrected, high): Fixed the semicolons in the coordinates and the missing period before "What"; the key is already 9, the only valid value, so the key and explanation stay.
- **Math M1 #2 (csv 465)** (yellow, corrected, high): Changed "where a represents" to "where x represents" to match the variable in the function; the existing explanation is already correct.
- **Math M1 #5 (csv 468)** (yellow, corrected, high): Removed "off an elevated surface", which contradicted the launch from the ground (0 feet), and added "was" to "the object launched from the ground".
- **Math M1 #6 (csv 469)** (yellow, corrected, high): Said c is "the other zero" so c = -9 is excluded, added the missing article, and replaced the semicolon in the vertex coordinates with a comma.
- **Math M1 #9 (csv 472)** (yellow, no change, high): No change needed: the pipe table matches the original (the detached 15 | 10 row is part of the same table) and the question is clear with the key 11 correct.
- **Math M1 #17 (csv 480)** (red, corrected, invented, redrawn, high): Rewrote the ungrammatical, ambiguous question to name the system (f with the horizontal line y = -3) so only B works, and redrew the graph alone since the table was already written as text.
- **Math M1 #22 (csv 485)** (yellow, corrected, redrawn, high): Redrew the cropped circle figure (title and bottom cut off) and fixed the stray space before the question mark.
- **Math M2 #9 (csv 494)** (yellow, corrected, high): Fixed the stem's grammar, set the choices in math notation, and wrote choice D with the congruence sign and the correct vertex order (ABC to CDA).
- **Math M2 #10 (csv 495)** (yellow, corrected, invented, high): Fixed the grammar, defined x, and added that she works every day so 5 weeks is clearly 35 working days; set the choices in math notation.
- **Math M2 #15 (csv 500)** (yellow, corrected, high): Fixed the stem's grammar and math formatting and removed the stray period from choice D.
- **R&W M1 #12 (csv 605)** (yellow, corrected, high): Italicized the two species names as the SAT prints them; the question and key D are otherwise sound.
- **R&W M1 #14 (csv 607)** (yellow, corrected, high): Italicized the work titles in the passage and choices as the SAT prints them; wording and key A unchanged.
- **R&W M1 #23 (csv 616)** (yellow, no change, high): No change needed: the solver was only moderately confident, but the text is clean and 'Of course' is the only transition that fits.
- **R&W M2 #8 (csv 629)** (yellow, corrected, high): Put the Text 1/Text 2 labels on their own paragraphs per format and changed the em dash in the date range to an en dash; content and key A unchanged.
- **R&W M2 #14 (csv 635)** (yellow, corrected, high): Italicized the species name Cycina tenera in the passage and choice C; wording and key B unchanged.
- **R&W M2 #20 (csv 640)** (yellow, restored, high): Restored the artist's first name: the garbled "portraitist like Udé’s" now reads "portraitist Iké Udé’s".
- **R&W M2 #26 (csv 647)** (yellow, no change, high): No change needed: the solver was only moderately confident, but the notes are complete, match the original, and the key is clear.
