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

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #2 (csv 2824)** (yellow, invented, medium): The figure is missing, so the stem no longer refers to it and names triangle ABC directly; with only the text given, B is the one sufficient statement. **A person must:** The original figure is missing from the bank; if it can be recovered, check that it gives no angle measure that would make choice C also sufficient, and restore it.
- **Math M1 #7 (csv 2829)** (red, invented, medium): The table image is unreadable and missing, so a pipe table of values for g(x) = -3x + 27 was written into the stem so that b = 27 (key D). **A person must:** The original table is missing from the bank; the table here was made up to fit key D. If the original table can be recovered, use it instead.
- **Math M1 #17 (csv 2839)** (red, invented, redrawn, medium): The data figure is unreadable and missing, so a scatterplot of points along d = -48.1 + 2.02t was drawn and a sentence introducing it was added. **A person must:** The original scatterplot is missing from the bank; this one was made up to fit key A. If the original can be recovered, use it instead.
- **Math M1 #18 (csv 2840)** (red, invented, medium): The volume table is unreadable and missing, so a pipe table with volumes 32π and 864π (height 8, scale factor 3) was written into the stem to fit key 320. **A person must:** The original table is missing from the bank; the volumes 32π and 864π were chosen to fit key 320. If the original table can be recovered, use it instead.
- **Math M1 #20 (csv 2842)** (red, invented, medium): The table image is unreadable and missing, so a pipe table of points on y = 2x^2 - 15x - 711 was written into the stem so that f(0) = -717. **A person must:** The original table is missing from the bank; the table here was made up to fit key -717. If the original table can be recovered, use it instead.
- **Math M1 #22 (csv 2844)** (red, invented, redrawn, medium): The original figure is lost and no standard angle relation with y=2x+7 gives 61, so I drew a new parallel-lines figure with x and y as same-side interior angles and changed the equation to y=2x-3 so the key C (61) is the only answer.
- **Math M2 #2 (csv 2846)** (red, invented, high): The table image is unreadable, so I wrote a pipe table with values (62, 2), (93, 3), (155, 5) that fit the key B and keep the 1/62 and 62 distractors meaningful.
- **Math M2 #8 (csv 2852)** (yellow, corrected, high): The figure is missing and not needed, so I removed the references to it ("shown", "(not shown)"); the text fully determines the answer.
- **Math M2 #9 (csv 2853)** (red, invented, high): The table image is unreadable, so I wrote a pipe table of estimates and margins of error in which Group 3 has the smallest margin, matching key B.
- **Math M2 #11 (csv 2855)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the question is clear, the key 0.63 is right, and .63 is already accepted.
- **Math M2 #17 (csv 2861)** (red, invented, redrawn, medium): The figure was missing and, with y = 2x + 7, no angle relationship gives a listed choice (58 + 123 = 181); I drew x and y as same-side interior angles and changed the equation to y = 2x + 6 so the key 58 works exactly, which is very likely the original. **A person must:** The bank's figure could not be opened and no original screenshot was supplied; compare the redrawn figure and the changed equation (y = 2x + 7 became y = 2x + 6) with the original question if it can be found.
- **R&W M1 #8 (csv 3541)** (yellow, no change, high): No change: one solver was only moderately sure, but the passage is complete and the key is clearly supported.
- **R&W M1 #10 (csv 3543)** (red, invented, medium): Changed "at any station" to "at that station" so a lower count at station 1 (choice A) can no longer also complete the claim; the missing table still has to be restored by a person. **A person must:** Restore the table: the original table image cannot be opened and no screenshot was supplied. Write it as a pipe table with the counts of each fish species at stations 1-3, and check that station 3 shows 31 blackspotted rockskippers, 610 streaky rockskippers and 16 barred flagtails.
- **R&W M1 #11 (csv 3544)** (red, no change, medium): The text and choices need no change; only the missing table must be restored, and the key D is the only choice that compares Austria's fungus count with both other countries. **A person must:** Restore the table: the original table image cannot be opened and no screenshot was supplied. Write it as a pipe table of damaging insect and fungus species reported by Austria, Bulgaria and Belgium, and check that Austria shows 51 fungus species and Bulgaria and Belgium fewer.
- **R&W M1 #19 (csv 3552)** (yellow, no change, high): No change: one solver chose "them," but the antecedent is the singular "wobble" (the redshifts and blueshifts sit inside a dash interruption), so the question is clear and the key is right.
- **R&W M1 #22 (csv 3555)** (yellow, no change, high): No change: one solver disagreed, but the question is clear and the key is right; Chernow's abundant sources are the opposite of the common lack of sources, so only a contrast transition fits.
- **R&W M2 #4 (csv 3564)** (yellow, no change, high): No change: one solver disagreed, but the question is clear and the key is right; the ethicists assume character means never acting against it, and Kamtekar answers that we expect only frequent, not unfailing, helpfulness.
- **R&W M2 #10 (csv 3570)** (red, no change, low): Left unchanged: the question needs its data table, which is unreadable and has no original screenshot, and the figures cannot be restored with certainty. **A person must:** Restore the table of home video game system unit sales: the question image import-10-english-module_2-q10-visual.svg is unreadable and no original screenshot was supplied, so the table's systems and figures cannot be recovered. Add it as a pipe table (system, units sold) after the passage and confirm that the Game & Watch is about 18,600,000 and the ColecoVision about 2,000,000 so D is the only correct choice.
- **R&W M2 #12 (csv 3572)** (red, no change, low): Left unchanged: the question needs its data table, which is unreadable and has no original screenshot, and the values cannot be restored with certainty. **A person must:** Restore the table of broadleaf arrowhead data (by day 5, 10, 15, 20: open flowers per growth unit, sex allocation, and male flowers' estimated reproductive success): the question image import-10-english-module_2-q12-visual.svg is unreadable and no original screenshot was supplied. Add it as a pipe table after the passage and confirm that allocation becomes strongly female biased by day 20 while male reproductive success stays constant, so D is the only correct choice.
- **R&W M2 #17 (csv 3577)** (yellow, no change, high): No change: a solver was only moderately sure, but the question is clear and the key is right; "by being passed down" modifies "survived," so no punctuation belongs between "day" and "by."
- **R&W M2 #18 (csv 3578)** (red, corrected, high): Changed the closing dash after "sinkholes" to a comma so the nonessential element is set off by a matching pair of commas, as the review proposed; the explanation is updated to match.
- **R&W M2 #19 (csv 3579)** (red, corrected, high): Changed the key from C to D: only "and, crossing" sets off the participial phrase with paired commas and joins "was ... long" with "modeled"; wrote the explanation for the new key.
- **R&W M2 #20 (csv 3580)** (red, corrected, high): Changed the key from D to C because "became" is already the main verb, so only the participial phrase "information, generating" is grammatical; also removed the stray word "documenting" from "mailings documenting to friends."; wrote the explanation for the new key.
- **R&W M2 #22 (csv 3582)** (yellow, restored, high): Replaced the nonsensical "by reading gender conventions" with "by evading gender conventions," the word the context (writers hiding behind male pseudonyms) and the near-identical spelling make nearly certain; the answer is unaffected.
