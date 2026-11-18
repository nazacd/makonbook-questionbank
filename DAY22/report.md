# DAY22 AI review

Test ids DAY22: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 40 | 10 | 4 | 54 |
| Math | 39 | 4 | 1 | 44 |
| **Total** | **79** | **14** | **5** | **98** |

Verdicts: key_correct 93, ambiguous 2, key_wrong 2, broken 1. Adjudicated: 25.

## Red: a teacher decides before publishing

- **Math M1 #11 (csv 1075)**: ambiguous. Ambiguous: without a figure or a statement that B lies between A and C, both 5pi = 15pi/3 (C, the key) and 5pi/3 (A) are offered and defensible; the duplicate ambiguity issue was merged into one.
- **R&W M1 #18 (csv 1350)**: key_wrong. Key D → A. Key D is wrong because singular "helps" does not agree with the plural compound subject "determination and perseverance"; A "helped" is the only choice giving a grammatical finite verb, as both solvers found.
- **R&W M1 #21 (csv 1359)**: ambiguous. Ambiguous: SAT convention favors A, but D ("classical authors, however; many...") is also grammatical with "however" closing the first clause and is arguably more logical, so the key cannot be proven wrong and a teacher should decide.
- **R&W M2 #12 (csv 1371)**: key_wrong. Key A → B. Key A is wrong: A's finding of lower oxalic acid and trypsin inhibitors after soaking supports the claim, while B's finding of no significant effect directly weakens it, so the key should be B.
- **R&W M2 #17 (csv 1376)**: broken. Broken: the comma after the blank is in the bank's own image, not a transcription error, and with it B yields a doubled comma while C becomes correct; removing that comma restores B as the only correct answer.

## Yellow

- solver medium: 13
- transcription medium: 2
- solver disagrees with the key: 2
- content: image_text_mismatch: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 1; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 6, with the final key on 4; confidence high 88, medium 10, low 0.
- Both disagree with the bank key: 3 (R&W M1 #18 (csv 1350); R&W M1 #21 (csv 1359); R&W M2 #12 (csv 1371)).
- The two solvers disagree with each other: 3.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 120; kept as figures 0 (none), the rest turned into text.
- Upscaled for the models: 52.

## Explanations

- Bank explanation: usable 68, minor_issue 18, wrong 8, mismatch 3, missing 1.
- Final: drafted 52, kept from the bank 46.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 817,126 | $2.29 |
| solve_a | opus | 10 | 720,327 | $4.03 |
| solve_b | sonnet | 10 | 717,523 | $2.01 |
| explain | sonnet | 10 | 882,075 | $2.47 |
| adjudicate | opus | 5 | 437,160 | $2.45 |
| **Subagents** | | 45 | **3,574,211** | **$13.25** |

Per question ≈ 36,471 tokens, ≈ $0.135 at API list prices (90/10 input/output split assumed; the main session is not included).

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #11 (csv 1075)** (red, invented, high): Added that B lies on arc AC between A and C (and asked for the arc containing B), since without a figure B could lie outside arc AC, making 5pi/3 (choice A) also defensible.
- **Math M1 #18 (csv 1082)** (yellow, invented, high): Added "rounded to the nearest hundredth" because the exact value of y is 298/61 and choice C (4.89) is only its rounded value; the system and sentence already match the screenshot.
- **Math M2 #4 (csv 1090)** (yellow, restored, high): Choice B "4y(3y55)" was garbled; restored it as \( 4y(3y+5) \), the sign-error distractor that matches the pattern of choices C and D.
- **Math M2 #8 (csv 1094)** (yellow, no change, high): No change: the text matches the screenshot, and the question clearly asks for the time required to cover 60 km at 20 km/h; the solver was only unsure about "must".
- **Math M2 #19 (csv 1105)** (yellow, no change, high): No change: the stem and all four transcribed tables match the original screenshots exactly, and the key is right.
- **R&W M1 #5 (csv 1347)** (yellow, no change, high): No change needed: the transcription matches the screenshot, the question is clear, and key B is right; the flag came only from a solver's medium confidence.
- **R&W M1 #11 (csv 1337)** (yellow, corrected, invented, high): Removed "increase in" from every choice (the table shows rates, not increases), fixed "Europe Alps", D's missing "The" and verb agreement, and "graph" to "table"; rewrote A because "highest" for a ">1" range could not be proven false against "2 - 7".
- **R&W M1 #17 (csv 1349)** (yellow, no change, high): No change needed: "Recognizing her unique artistic style" introduces a second independent clause ("art historian Elizabeth Taylor has compared"), so only the period in C is correct; the dissenting solver misread the participle as modifying the first clause.
- **R&W M1 #18 (csv 1350)** (red, corrected, high): Changed the key from D to A, since the plural compound subject "Her determination and perseverance" rules out singular "helps to", and rewrote the explanation for the new key. **A person must:** Optional: the passage's fact is inaccurate (Ellen MacArthur set the fastest solo circumnavigation record in 2005; she was not the youngest, in 1997). A teacher may want to correct the first sentence; it does not affect the answer.
- **R&W M1 #21 (csv 1359)** (red, invented, medium): A ("authors; however,") was also correct, so I removed its comma after "however" to make it a clear error and rewrote the explanation, which argued for A although the key is D.
- **R&W M1 #24 (csv 1353)** (yellow, invented, high): Replaced distractor D "In conclusion," with "Nevertheless," because a summarizing transition could also be defended before a concluding final sentence (the old explanation even conceded it 'could work'), and rewrote the explanation to match.
- **R&W M1 #25 (csv 1356)** (yellow, no change, high): No change needed: one solver misread the relationship, but traditional media struggling is clearly an effect of the internet and mobile transformation, so the question is clear and key D is right.
- **R&W M2 #11 (csv 1370)** (yellow, no change, high): No change needed: the passage matches the original screenshot, and the question is clear with B as the only finding that directly shows the hierarchy holding across cultures.
- **R&W M2 #12 (csv 1371)** (red, corrected, high): Set the key to B per the review's key_wrong verdict (the bank's A supports rather than weakens the claim) and wrote the explanation for key B; the text matches the screenshot.
- **R&W M2 #15 (csv 1374)** (yellow, corrected, high): Removed the repeated "on Oahu" at the end of choice C; the passage matches the screenshot and key A is unchanged.
- **R&W M2 #16 (csv 1375)** (yellow, no change, high): No change needed: the passage matches the original screenshot, the underlined claim is clear, and D is the only quotation showing a realistic plot juxtaposed with folklore-derived elements.
- **R&W M2 #17 (csv 1376)** (red, corrected, high): Removed the comma after the blank (present in the bank's own image) because with it the key B produced a doubled comma and C became correct; without it B is the only correct choice.
- **R&W M2 #24 (csv 1383)** (yellow, no change, high): No change needed: the text matches the original, and the solvers' medium confidence came from 'Indeed', which does not fit because the last sentence adds a new effect rather than reinforcing the previous one.
- **R&W M2 #25 (csv 1384)** (yellow, no change, high): No change needed: the text matches the original and the key is clear, since the compiled rankings follow from the participants' responses.
