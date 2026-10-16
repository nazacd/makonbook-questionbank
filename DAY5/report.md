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
