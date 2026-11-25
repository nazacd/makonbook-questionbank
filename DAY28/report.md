# DAY28 AI review

Test ids DAY28: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 38 | 10 | 6 | 54 |
| Math | 42 | 2 | 0 | 44 |
| **Total** | **80** | **12** | **6** | **98** |

Verdicts: key_correct 92, key_wrong 3, broken 3. Adjudicated: 21.

## Red: a teacher decides before publishing

- **R&W M1 #19 (csv 1467)**: key_wrong. Key B → C. Key B is wrong because it leaves two independent clauses joined by only a comma; C is the only choice that separates them correctly, and both solvers agree with high confidence.
- **R&W M2 #9 (csv 1506)**: broken. Broken: the bank's own table image gives 2.00 vs. 16.00 for symptom severity reduction, which makes key D false and leaves no correct choice; the value is probably 92.00 (choice A's range points to it), but a teacher should confirm it before the table is fixed. The typo issue about choice A was folded into the table mismatch, and the duplicate grammar issue was dropped.
- **R&W M2 #10 (csv 1507)**: key_wrong. Key B → A. Key B is wrong because it denies the average advantage the conclusion starts from and shows the complementary outlier pulling purchasing down rather than up; A is the only choice where removing the complementary outlier erases the advantage, and both solvers chose A with high confidence.
- **R&W M2 #11 (csv 1508)**: broken. Broken: the public ranks medicinal plants 12, its lowest of the five, so key D is false and no choice supports the conclusion; the data fit the conclusion only if the service is physical health (public rank 7, its best), which the proposed fix restores in the passage and choice D.
- **R&W M2 #17 (csv 1514)**: broken. Broken: as printed, key B creates the fragment "enacted in 1987." and only A is grammatical, but A makes the illogical claim that independence grew since 1985 among constitutions enacted in 1987; the intended key is B with a comma ("constitutions; enacted in 1987," modifying Haiti's constitution), so the fix is to restore that comma.
- **R&W M2 #21 (csv 1518)**: key_wrong. Key D → C. The key is wrong: D gives "Serra" two finite verbs ("intends" and "assembles") joined only by a comma, so only C, a participial phrase set off by commas, is grammatical.

## Yellow

- solver medium: 11
- solver disagrees with the key: 8
- solver low: 2
- content: off_format: 1
- content: other: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 10, with the final key on 7; confidence high 90, medium 5, low 3.
- solve_b (sonnet): disagrees with the bank key on 10, with the final key on 7; confidence high 87, medium 8, low 3.
- Both disagree with the bank key: 9 (Math M1 #4 (csv 1201); Math M1 #5 (csv 1202); R&W M1 #17 (csv 1465); R&W M1 #19 (csv 1467); R&W M2 #9 (csv 1506); R&W M2 #10 (csv 1507); R&W M2 #11 (csv 1508); R&W M2 #17 (csv 1514); R&W M2 #21 (csv 1518)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 127; kept as figures 7 (graph 4, geometry 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 79.

## Explanations

- Bank explanation: usable 63, minor_issue 19, wrong 14, mismatch 2, missing 0.
- Final: drafted 58, kept from the bank 40.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 855,234 | $2.39 |
| solve_a | opus | 10 | 732,016 | $4.10 |
| solve_b | sonnet | 10 | 730,625 | $2.05 |
| explain | sonnet | 10 | 840,498 | $2.35 |
| adjudicate | opus | 4 | 348,657 | $1.95 |
| **Subagents** | | 44 | **3,507,030** | **$12.85** |

Per question ≈ 35,786 tokens, ≈ $0.131 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

- math-m1-04 and math-m1-05 look swapped in the bank: the 04 figure and explanation image show the 05 savings-account question (table), not the scatterplot.
- math-m1-05 has no scatterplot figure attached, so a student cannot answer it as shown; the figure list needs the scatterplot (Screenshot_2024-08-08_at_2.02.55AM.png) added by a teacher.
- math-m1-04's figure alt text still calls its image a scatterplot; it is the table.
- adj-1 was re-run once because its first output failed the figure check on these two questions.
