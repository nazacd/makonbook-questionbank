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
