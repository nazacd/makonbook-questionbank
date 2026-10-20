# DAY10 AI review

Test ids DAY10: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 34 | 19 | 1 | 54 |
| Math | 40 | 3 | 1 | 44 |
| **Total** | **74** | **22** | **2** | **98** |

Verdicts: key_correct 96, broken 2. Adjudicated: 26.

## Red: a teacher decides before publishing

- **Math M1 #8 (csv 291)**: broken. The figure is defective: line n can be read as passing through (-1, 0) and (0, 5) (slope 5, key A) or through (0, 5) and (1, 11) (slope 6, B), and a pixel fit gives slope about 5.6, so neither key can be proven; the wrong_key issue was dropped because the key cannot be proven wrong, and the figure needs to be redrawn.
- **R&W M2 #17 (csv 421)**: broken. Marked broken because choices B and D are identical in the bank, but the key C is still right (a title before a name takes no commas, and no comma goes between subject and verb), so the proposed fix makes D a distinct wrong choice.

## Yellow

- solver medium: 16
- content: typo: 9
- transcription medium: 5
- solver disagrees with the key: 4
- content: grammar: 3
- content: image_text_mismatch: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 2; confidence high 94, medium 4, low 0.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 86, medium 12, low 0.
- Both disagree with the bank key: 2 (Math M1 #8 (csv 291); R&W M2 #21 (csv 425)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 92, medium 6, low 0.
- Question and choice images: 24; kept as figures 5 (graph 3, scatterplot 1, geometry 1), the rest turned into text.
- Upscaled for the models: 24.

## Explanations

- Bank explanation: usable 56, minor_issue 37, wrong 5, mismatch 0, missing 0.
- Final: drafted 46, kept from the bank 52.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 581,465 | $1.63 |
| solve_a | opus | 10 | 534,768 | $2.99 |
| solve_b | sonnet | 10 | 533,396 | $1.49 |
| explain | sonnet | 10 | 619,730 | $1.74 |
| adjudicate | opus | 4 | 258,997 | $1.45 |
| **Subagents** | | 44 | **2,528,356** | **$9.30** |

Per question ≈ 25,799 tokens, ≈ $0.095 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

adj-1 adjudication agent hit an API rate limit at the end of its run; its output file was complete (6/6) and passed the stage check, token usage for adj-1 not logged.
Source row issue: english-m2-17 has identical choice text (duplicate_choice) in the bank.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #8 (csv 291)** (red, redrawn, high): Redrew the graph so line n passes exactly through (-1, 0), (0, 5) and (1, 10) (slope 5), matching the key A; the original line was drawn imprecisely and could be read as slope 6, and the explanation is rewritten for the bank key.
- **Math M1 #17 (csv 300)** (yellow, corrected, high): Fixed the transcription slip in choice B ("and y y > 0") to match the other choices.
- **Math M2 #21 (csv 326)** (yellow, no change, high): No change needed: one solver erred in solving for y, but the question is clear and the key C is right.
- **Math M2 #22 (csv 327)** (yellow, corrected, high): Added the missing commas and the missing word "be" in the stem, keeping the original figure.
- **R&W M1 #1 (csv 378)** (yellow, restored, high): Restored Twain's garbled opening words ("heaved a long and dismal whh") to "appeared on the sidewalk with", as in the novel.
- **R&W M1 #2 (csv 379)** (yellow, no change, high): No change needed: the solver was only unsure, but the text is clear and "instead" signals a departure from the usual above-sea-level focus, so only "innovative" fits.
- **R&W M1 #5 (csv 382)** (yellow, restored, high): Restored the missing verb in the opening fragment ("the Tulalip Tribes operate the Tulalip Cultural Center"), which the rest of the text and choice A make nearly certain.
- **R&W M1 #7 (csv 1442)** (yellow, corrected, high): Fixed the original's misspelling "okayake" to "okayeke" so the underlined sentence names the word defined earlier, replaced "by exampling" with "by showing", added "an" to choice B, and spelled Hoocąk consistently in the choices.
- **R&W M1 #8 (csv 385)** (yellow, corrected, restored, high): Restored the missing verb ("places that are customer facing") and corrected "Researcher" to "Researchers" for the three named people.
- **R&W M1 #12 (csv 389)** (yellow, corrected, high): Changed "Class I-V" to "Class I-IV" in choices A and D to match the graph legend, moved the period outside the parenthesis, and corrected the nonsensical "converted to cattle practices" to "converted to cattle pastures".
- **R&W M1 #14 (csv 391)** (yellow, corrected, high): Fixed the ungrammatical "were to adapt" in distractor C to "could be adapted"; the key and other choices are unchanged.
- **R&W M1 #24 (csv 401)** (yellow, corrected, high): Corrected "sky inland" to "sky island", the garbled key B to match the notes, "in located" in A, and added missing periods to two bullets.
- **R&W M1 #25 (csv 402)** (yellow, corrected, high): Made the notes' quotation read "poetics" to match key C, fixed "multifaced" to "multifaceted", and italicized the full book title.
- **R&W M2 #2 (csv 406)** (yellow, corrected, high): Added the missing "the" to the stem; the passage, choices and key are fine.
- **R&W M2 #7 (csv 411)** (yellow, corrected, restored, high): Fixed "North American" and "tended to selected", and restored the missing verb "sing" in Text 1.
- **R&W M2 #9 (csv 413)** (yellow, corrected, high): Corrected "convergence evolution" to "convergent evolution" in choice A and "biologist" to "biologists" for the two researchers in the passage.
- **R&W M2 #11 (csv 415)** (yellow, corrected, high): Fixed the stem's grammar ("describes") and the misspellings "Kalmarnjärvi" and "Mirrow Lake" to match the table and the original image; explanation rewritten with the corrected spelling.
- **R&W M2 #12 (csv 416)** (yellow, corrected, restored, medium): Restored the missing "D." at the start of choice C and repaired garbled passage words ("observing" to "obviating", "manipulative" to "nanoparticle", "invertebrate" to "invertebrates").
- **R&W M2 #16 (csv 420)** (yellow, no change, high): No change needed: the solver was unsure, but the question is clear and the key D is right.
- **R&W M2 #17 (csv 421)** (red, invented, high): Choices B and D were identical, so D became a distinct wrong option with a comma only after "advocate"; explanation rewritten to cover the new D.
- **R&W M2 #19 (csv 423)** (yellow, no change, high): No change needed: the solvers were only unsure, but the question is clear and key D is right.
- **R&W M2 #20 (csv 424)** (yellow, no change, high): No change needed: the question is clear and key B is right.
- **R&W M2 #21 (csv 425)** (yellow, no change, medium): No change needed: the solvers chose C, but "however" contrasts the first sentence with not playing on the song, and the explanation already reflects this; key B is right.
- **R&W M2 #24 (csv 428)** (yellow, corrected, high): Fixed two transcription typos: "July Falk" to "Jules Falk" in D and "5000" to "500" in B, matching the notes.
