# DAY3 AI review

Test ids DAY3: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 35 | 15 | 4 | 54 |
| Math | 44 | 0 | 0 | 44 |
| **Total** | **79** | **15** | **4** | **98** |

Verdicts: key_correct 94, broken 4. Adjudicated: 23.

## Red: a teacher decides before publishing

- **R&W M2 #4 (csv 795)**: broken. Broken: words are missing after the blank, so the sentence is ungrammatical with every choice. B (precipitating) is clearly the intended answer, but a teacher has to restore the missing text before the question can be used. The two duplicate grammar reports and the two duplicate typo reports were merged into one each.
- **R&W M2 #16 (csv 809)**: broken. Broken: keyed choice C says 'negatively correlated' where the passage supports a positive correlation (more vertebrate hosts, more sensitivity to warming), and D overclaims, so no choice works as printed; changing C to 'a parasite’s ... positively correlated' fixes it and keeps key C.
- **R&W M2 #19 (csv 812)**: broken. Broken: a stray semicolon after the blank makes keyed B read 'spectrum:;' and makes D correct as printed; both solvers chose D for this reason, and removing the semicolon restores B (a colon introducing the explanation) as the only correct answer.
- **R&W M2 #20 (csv 813)**: broken. Broken: a stray semicolon after the blank makes keyed A read 'wastes;;' and makes D correct as printed; both solvers chose D for this reason, and removing the semicolon restores A (a semicolon joining two independent clauses) as the only correct answer.

## Yellow

- solver medium: 8
- content: typo: 7
- transcription medium: 5
- solver disagrees with the key: 3
- content: grammar: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 4, with the final key on 4; confidence high 93, medium 4, low 1.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 4; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 3 (R&W M2 #13 (csv 806); R&W M2 #19 (csv 812); R&W M2 #20 (csv 813)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 93, medium 5, low 0.
- Question and choice images: 58; kept as figures 8 (graph 3, geometry 2, chart 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 23.

## Explanations

- Bank explanation: usable 76, minor_issue 13, wrong 9, mismatch 0, missing 0.
- Final: drafted 49, kept from the bank 49.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 616,149 | $1.73 |
| solve_a | opus | 10 | 541,681 | $3.03 |
| solve_b | sonnet | 10 | 541,769 | $1.52 |
| explain | sonnet | 17 | 1,096,973 | $3.07 |
| adjudicate | opus | 4 | 260,397 | $1.46 |
| **Subagents** | | 51 | **3,056,969** | **$10.81** |

Per question ≈ 31,193 tokens, ≈ $0.110 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- The Math and English exports used for DAY3 are the same pair of CSVs as DAY2 (they contain both tests). No new attachment came with the DAY3 request.
- Explain batches math-m1-b, english-m1-a, m1-b, m1-c, m2-a, m2-b and m2-c were re-run once: their issue entries had invalid severity, no source or no detail. tools/prompts/explain.md says to use "the same kinds as transcription" but doesn't list them and tells agents to read no other files.
- The script cut its error list off ("38 more"), so each re-run prompt got the errors that were visible for that batch, a note to check every issue in the batch, and a pointer to where the issue fields are defined (tools/prompts/transcribe.md). That pointer goes beyond the standard re-run prompt.
- On re-run some agents rewrote their issues and dropped details: english-m1-b dropped the notes about unitalicised titles on questions 13 and 15. A teacher may still see small typo issues in english-m1-05 to 08, 12 to 17 and english-m2-11 to 16.
- Transcription, solve and adjudication batches all passed on the first run. No R2 objects were missing.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **R&W M1 #8 (csv 840)** (yellow, restored, high): Restored the missing words "does the text" in the stem so it reads as the standard SAT main-purpose question.
- **R&W M1 #16 (csv 777)** (yellow, corrected, high): Replaced the spaced hyphen in choice D with an em dash to match the dash after "that", and removed a stray mid-sentence line break in the passage.
- **R&W M1 #17 (csv 789)** (yellow, corrected, high): Added the missing space before the blank after "he".
- **R&W M1 #20 (csv 786)** (yellow, corrected, high): Fixed the transcription misspellings of "Hernandez-Lopez" in distractors A and C so they differ from the other choices only in punctuation.
- **R&W M1 #21 (csv 785)** (yellow, no change, high): No change needed: one solver disagreed, but the question is clear and key D is right because C creates a comma splice.
- **R&W M1 #22 (csv 784)** (yellow, corrected, high): Restored the missing spaces in choice A ("forthisreason," to "for this reason,").
- **R&W M1 #25 (csv 781)** (yellow, corrected, high): Separated the run-together "ofthe" in choice C.
- **R&W M1 #26 (csv 780)** (yellow, corrected, high): Fixed transcription slips: run-together words and "Sofo" in choice C (title italicized as in the notes), the missing period in B, and the stray period in D; the explanation now italicizes the title too.
- **R&W M1 #27 (csv 779)** (yellow, corrected, high): Changed "TS0" (digit zero) to "TSO" in the stem to match the notes and choices; the notes match the screenshot.
- **R&W M2 #3 (csv 794)** (yellow, no change, high): No change needed: the review flagged only solver uncertainty, but the text is clean and the "but" contrast with Peck, who "will always be remembered," makes "uncertain" the one logical answer.
- **R&W M2 #4 (csv 795)** (red, restored, corrected, high): Restored the missing object and colon after the blank ("______ demand:") so the sentence parses, and fixed the misspelled distractor "monerizing" to "monetizing".
- **R&W M2 #9 (csv 801)** (yellow, corrected, high): Corrected the name "Rubayer" to "Rubayet" to match Text 2 and added the missing space after "(Text 2)".
- **R&W M2 #11 (csv 803)** (yellow, corrected, high): Fixed transcription typos in all four choices ("land- based", "IGE-1", "IGFS-groduction" and lowercase "some", "indogs").
- **R&W M2 #12 (csv 805)** (yellow, corrected, high): Corrected "efectively" in the stem and the garbled "wher theas number" in choice C; the graph is clear and matches the text.
- **R&W M2 #13 (csv 806)** (yellow, corrected, medium): Made choice A's opening quote mark curly to match its closing one and italicized the novel's title in all choices, as in the passage; content unchanged.
- **R&W M2 #15 (csv 808)** (yellow, corrected, high): Fixed the typo "ni the wild" to "in the wild" in choice B; the question and key were otherwise fine.
- **R&W M2 #16 (csv 809)** (red, corrected, invented, high): Changed "negatively" to "positively" in keyed choice C (the bank's wording contradicted the passage) and added the missing article; italicized species names in B.
- **R&W M2 #19 (csv 812)** (red, corrected, high): Removed the stray semicolon after the blank that made keyed B read "spectrum:;" and removed the stray quote mark at the start of the stem.
- **R&W M2 #20 (csv 813)** (red, corrected, high): Removed the stray semicolon after the blank that made keyed A read "wastes;;" and removed the stray quote mark at the start of the stem; the explanation still fits.
