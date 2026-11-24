# DAY25 AI review

Test ids DAY 25: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 41 | 6 | 7 | 54 |
| Math | 33 | 3 | 8 | 44 |
| **Total** | **74** | **9** | **15** | **98** |

Verdicts: key_correct 83, broken 13, key_wrong 2. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M1 #7 (csv 2829)**: broken. Broken: the table that defines g is missing from the bank (unreadable SVG), so key D cannot be verified; duplicate missing_image issues merged into one.
- **Math M1 #17 (csv 2839)**: broken. Broken: the data figure is missing from the bank (unreadable SVG) and the choices differ only in intercept, so key A cannot be verified; duplicate missing_image issues merged into one.
- **Math M1 #18 (csv 2840)**: broken. Broken: the volume table is missing from the bank (unreadable SVG), so the key 320 cannot be verified; duplicate missing_image issues merged into one.
- **Math M1 #20 (csv 2842)**: broken. Broken: the table of points is missing from the bank (unreadable SVG), so the key -717 cannot be verified; duplicate missing_image issues merged into one.
- **Math M1 #22 (csv 2844)**: broken. Broken: the figure that fixes which angles x and y are is missing from the bank (unreadable SVG), and neither equal nor supplementary angles give 61, so key C cannot be verified without it; duplicate missing_image issues merged into one.
- **Math M2 #2 (csv 2846)**: broken. Broken: the table of salt and water values is an unreadable image, so no choice can be checked; the key B cannot be confirmed until the table is restored (duplicate missing_image issues merged into one).
- **Math M2 #9 (csv 2853)**: broken. Broken: the margins-of-error table is an unreadable image, so the group with the largest sample cannot be identified and key B cannot be verified (duplicate missing_image issues merged into one).
- **Math M2 #17 (csv 2861)**: broken. Broken: the figure defining angles x and y is an unreadable image; neither x = y nor x + y = 180 gives a listed choice (key 58 gives 58 + 123 = 181), so key C cannot be checked without the figure.
- **R&W M1 #10 (csv 3543)**: broken. Broken: the required table is missing, so neither the key C nor solver 1's A can be verified, and the wording "at any station" may also admit A; the three duplicate missing_image issues were merged into one.
- **R&W M1 #11 (csv 3544)**: broken. Broken: the table is missing; D is the only choice that compares Austria's fungus count with both other countries and the key is very likely right, but the data cannot be verified until the figure is restored (duplicate missing_image issues merged).
- **R&W M2 #10 (csv 3570)**: broken. Broken: the table image is unreadable, so the sales figures in the choices cannot be verified and the key D cannot be confirmed; restore the table.
- **R&W M2 #12 (csv 3572)**: broken. Broken: the table image is unreadable, so the data claims in every choice are unverifiable; D is logically plausible but needs the restored table to confirm.
- **R&W M2 #18 (csv 3578)**: broken. Broken: a nonessential element must open and close with the same mark, and it closes with a dash while no choice offers a dash, so no option is fully correct; changing the closing dash to a comma (matching the original's apparent intent) makes key A correct.
- **R&W M2 #19 (csv 3579)**: key_wrong. Key C → D. Key wrong: with C, B, or A the verb "modeled" is left uncoordinated, while D sets off "crossing ... countries" with paired commas inside the compound predicate "was ... long, and ... modeled," so D is the only grammatical choice (both solvers agree).
- **R&W M2 #20 (csv 3580)**: key_wrong. Key D → C. Key wrong: the subject "documentation" already has the main verb "became," so D's finite "generated artworks" creates two verbs, while C's comma-bounded participial phrase "generating artworks ..." is the only grammatical option (both solvers agree).

## Yellow

- solver medium: 4
- solver disagrees with the key: 3
- content: missing_image: 2
- transcription medium: 2
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 11, with the final key on 9; confidence high 84, medium 3, low 11.
- solve_b (sonnet): disagrees with the bank key on 13, with the final key on 11; confidence high 79, medium 8, low 11.
- Both disagree with the bank key: 9 (Math M1 #7 (csv 2829); Math M1 #17 (csv 2839); Math M1 #18 (csv 2840); Math M1 #20 (csv 2842); Math M1 #22 (csv 2844); Math M2 #9 (csv 2853); Math M2 #17 (csv 2861); R&W M2 #19 (csv 3579); R&W M2 #20 (csv 3580)).
- The two solvers disagree with each other: 8.

## Transcription

- Confidence: high 84, medium 2, low 12.
- Question and choice images: 14; kept as figures 0 (none), the rest turned into text.
- Upscaled for the models: 0.

## Explanations

- Bank explanation: usable 0, minor_issue 0, wrong 0, mismatch 0, missing 98.
- Final: drafted 98, kept from the bank 0.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 747,508 | $2.09 |
| solve_a | opus | 10 | 726,968 | $4.07 |
| solve_b | sonnet | 10 | 722,435 | $2.02 |
| explain | sonnet | 10 | 776,396 | $2.17 |
| adjudicate | opus | 4 | 315,637 | $1.77 |
| **Subagents** | | 44 | **3,288,944** | **$12.13** |

Per question ≈ 33,560 tokens, ≈ $0.124 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

14 questions have question images that could not be read from R2 (the SVG files fail to open: math-m1-02, 07, 17, 18 and others; see the prep warnings). The solvers could not check those figures, so those questions are flagged blocking and red for a teacher.
