# DAY5 AI review

Test ids DAY5: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 35 | 11 | 8 | 54 |
| Math | 37 | 7 | 0 | 44 |
| **Total** | **72** | **18** | **8** | **98** |

Verdicts: key_correct 90, key_wrong 4, ambiguous 4. Adjudicated: 32.

## Red: a teacher decides before publishing

- **R&W M1 #13 (csv 119)**: key_wrong. Key D → C. Key D fails because it is a general statement about Southern Black girls that shows no rejection of her own race, while C ("black ugly dream," wishing for blonde hair) directly shows the struggle, so the key should be C; the issue claiming A is equally defensible was dropped because A is clearly weaker.
- **R&W M1 #15 (csv 121)**: ambiguous. Ambiguous: the graph confirms C (about 17 on 11/26, about 38 on 11/27) and also A (peaks of 50 to 67 early versus about 15 to 20 just before the eruption), and because the stem's "geologists' conclusion" is never stated, which choice supports it cannot be settled.
- **R&W M1 #18 (csv 124)**: ambiguous. Ambiguous: the text partly supports A, B and D (the children hated the flowers for several reasons, including not understanding them), so the key cannot be proved wrong and a teacher should decide.
- **R&W M1 #20 (csv 126)**: ambiguous. Ambiguous: A and B are both grammatical noun phrases that include queens, and the choice between them rests on style and the disputed "that"-for-people convention, so neither key can be proved; the combined typo issue was dropped as a duplicate of the separate missing-"and" and "Boylyn" issues.
- **R&W M1 #22 (csv 128)**: ambiguous. Ambiguous: A's semicolon is certainly correct, but a dash between two independent clauses is also accepted by many guides, so D is defensible and a teacher should decide or replace D.
- **R&W M2 #8 (csv 141)**: key_wrong. Key C → B. Key C is wrong because the text describes no earlier scenario to counter; "was much lower" gives the proximity relationship the conclusion depends on, so B is correct, as both solvers found with high confidence.
- **R&W M2 #20 (csv 153)**: key_wrong. Key D → A. Key D is wrong because it leaves a comma splice before "the essay helps illustrate"; only A (a period after "Seaman") gives two complete sentences, as both solvers and the bank's own explanation agree.
- **R&W M2 #21 (csv 154)**: key_wrong. Key D → A. Key D ("Thus,") is wrong because the blank sentence is a concession answered by "Still,", not a result, so A ("Of course,") is the only logical transition; both solvers agree with high confidence.

## Yellow

- solver medium: 12
- transcription medium: 4
- content: ambiguous: 4
- solver disagrees with the key: 3
- content: typo: 3
- solver low: 2

## Solvers

- solve_a (opus): disagrees with the bank key on 8, with the final key on 4; confidence high 89, medium 8, low 1.
- solve_b (sonnet): disagrees with the bank key on 9, with the final key on 4; confidence high 87, medium 10, low 1.
- Both disagree with the bank key: 6 (R&W M1 #13 (csv 119); R&W M1 #18 (csv 124); R&W M1 #20 (csv 126); R&W M2 #8 (csv 141); R&W M2 #20 (csv 153); R&W M2 #21 (csv 154)).
- The two solvers disagree with each other: 5.

## Transcription

- Confidence: high 94, medium 4, low 0.
- Question and choice images: 28; kept as figures 3 (graph 1, geometry 1, chart 1), the rest turned into text.
- Upscaled for the models: 19.

## Explanations

- Bank explanation: usable 65, minor_issue 24, wrong 8, mismatch 1, missing 0.
- Final: drafted 54, kept from the bank 44.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 570,320 | $1.60 |
| solve_a | opus | 10 | 526,583 | $2.95 |
| solve_b | sonnet | 10 | 525,097 | $1.47 |
| explain | sonnet | 10 | 662,757 | $1.86 |
| adjudicate | opus | 6 | 402,101 | $2.25 |
| **Subagents** | | 46 | **2,686,858** | **$10.12** |

Per question ≈ 27,416 tokens, ≈ $0.103 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Note: explain agents were launched after the 20-subagent concurrency limit freed slots (no re-runs).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #8 (csv 115)** (yellow, no change, high): No change needed: the choice tables are already transcribed in full as pipe tables (the screenshot crop only clipped the last rows of B and D, which are still readable), so nothing is cropped in our version.
- **Math M1 #16 (csv 123)** (yellow, no change, high): The stem matches the original and the accepted list already holds every integer from -98 to -77, so the text needs no change; only non-integer answers in that range remain unaccepted. **A person must:** Grading: any number from -98 to -77 is correct (for example -80.5, from m = 11.5); the accepted list holds only the integers, so set the grader to accept the whole range -98 to -77 if it supports ranges.
- **Math M1 #17 (csv 124)** (yellow, redrawn, high): Redrew the hand-sketched figure, where the label D looked like a Greek letter, as a clean diagram with DEF twice the size of ABC and the 50° angle at A.
- **Math M1 #21 (csv 128)** (yellow, corrected, high): Replaced "the equation has more than one solution" (y = ... has infinitely many (x, y) solutions) with "the graph of the equation has more than one x-intercept" and removed a double space.
- **Math M2 #2 (csv 131)** (yellow, corrected, high): Wrote the variable x in the question as math; the accepted list already holds both solutions, 49 and -25.
- **Math M2 #14 (csv 143)** (yellow, corrected, invented, high): Reworded the stem to the standard SAT form (says the equation must be equivalent, fixes grammar) and rewrote choice C from 4096^{x+1} to 4096(4096)^x so the y-intercept 4096 really appears as a coefficient, removing the ambiguity the review found.
- **Math M2 #21 (csv 150)** (yellow, no change, high): No change needed: our version already writes the original's "l" bars as proper absolute value bars in LaTeX, and the question and key are clear.
- **R&W M1 #2 (csv 108)** (yellow, corrected, high): Removed the stray comma between "surveys ______ from 1940–2017" and "show", and closed up "United States– born" to "United States–born".
- **R&W M1 #5 (csv 111)** (yellow, no change, high): No change needed: the review found no issues; the underlined sentence clearly mirrors the previous one (poor/rich, did not want/did want), and the key is right.
- **R&W M1 #6 (csv 112)** (yellow, corrected, high): Changed "this bacteria" to "these bacteria" to fix the singular/plural mismatch; nothing else needed.
- **R&W M1 #12 (csv 118)** (yellow, corrected, high): Corrected the author's name from "Cisnero's" to "Cisneros's" and italicized the novel's title; "cannot out" is Cisneros's own wording and stays.
- **R&W M1 #13 (csv 119)** (red, corrected, high): Changed the key from D to C, as the review's key_wrong verdict found, and rewrote the explanation for key C.
- **R&W M1 #14 (csv 120)** (yellow, corrected, medium): Added the missing opening quotation mark to D and replaced the en dashes with hyphens in A ("public-auction," "four-letter"), which also removes the stray space.
- **R&W M1 #15 (csv 121)** (red, invented, high): Added a sentence stating the geologists' conclusion the stem refers to (a sharp rise in seismic activity just before the eruption), so the stem has a referent and only key C supports it; the figure is clear and stays.
- **R&W M1 #16 (csv 122)** (yellow, corrected, high): Rewrote the first sentence so "who" refers to the female characters rather than the plays, changed "hard–biting" to "hard-biting," and italicized the play titles; the meaning is unchanged.
- **R&W M1 #18 (csv 124)** (red, corrected, invented, high): Rewrote A so it claims only what the text states (her yard, not the whole neighborhood) and replaced B and D, which the text partly supported, with distractors the text contradicts; also fixed the em dashes in "sun-golden" and "witch-woman" and italicized the story title.
- **R&W M1 #20 (csv 126)** (red, corrected, invented, high): Fixed the missing "and" and the "Boylyn" misspelling, and replaced A and C with clear conventions errors (a wrong possessive; a comma before restrictive "that") so B is the only standard choice.
- **R&W M1 #22 (csv 128)** (red, invented, high): Replaced D (a dash, which can also join two independent clauses) with an ungrammatical relative clause so the semicolon in A is the only correct choice.
- **R&W M2 #4 (csv 138)** (yellow, corrected, high): Added the missing final period; the question and key were already sound.
- **R&W M2 #6 (csv 137)** (yellow, corrected, high): Fixed "like" to "little," "Davies" to "Davis," "Bliss" to "Bess," the missing possessive apostrophe, and italicized the album and opera titles.
- **R&W M2 #7 (csv 140)** (yellow, corrected, high): Fixed transcription slips the review found (missing "is", "migration" for "mitigation", "Moraexella", lowercase choice A), italicized the species names, and rewrote the explanation because it quoted the "migration" error.
- **R&W M2 #8 (csv 141)** (red, corrected, restored, high): Key B is already in our version; restored the garbled author names, added the missing "respondents" and "that" in the comparison, and made "researcher’s" plural to match "their" and the multiple researchers. **A person must:** Confirm the researchers' names: the garbled "Mike Moran, Daniel" was restored as "Mika R. Moran, Daniel A. Rodríguez" (authors of the Latin American park-use study); if unsure, use "Mika R. Moran and colleagues".
- **R&W M2 #18 (csv 151)** (yellow, no change, high): No change needed: one solver chose "rising", but the series "is ..., ______ ..., and then dips" clearly needs the finite present-tense verb "rises", and the key and current explanation are right.
- **R&W M2 #20 (csv 153)** (red, corrected, high): Key A is already in our version; restored the second editor's surname ("Debra Gwartney’s"), italicized the book title, and updated the explanation that quoted the title.
- **R&W M2 #21 (csv 154)** (red, corrected, high): Key A is already in our version; fixed "architect" to "architects" to agree with "their", and hyphenated "Nineteenth-century" and "plant- and animal-inspired".
- **R&W M2 #27 (csv 160)** (yellow, corrected, restored, high): Fixed the misplaced periods (".1" and ".4" now read 1 and 4), removed the stray "1", fixed choice C's missing article and "less harder", and restored the standard SAT notes intro so "the student" and "the notes" in the stem have a referent.
