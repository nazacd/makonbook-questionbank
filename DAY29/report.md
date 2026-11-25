# DAY29 AI review

Test ids DAY29: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 36 | 10 | 8 | 54 |
| Math | 43 | 1 | 0 | 44 |
| **Total** | **79** | **11** | **8** | **98** |

Verdicts: key_correct 90, key_wrong 5, broken 3. Adjudicated: 21.

## Red: a teacher decides before publishing

- **R&W M1 #12 (csv 2284)**: key_wrong. Key D → B. The hypothesis compares wide-headed with narrow-headed fish, and D has no comparison group while B shows exactly the predicted difference, so the key should be B; the two missing-article issues are merged into one.
- **R&W M1 #14 (csv 1563)**: key_wrong. Key B → D. The passage says the 200 series (dishwashers) has less nickel and more manganese than the 300 series (aerospace), so B contradicts the text and D follows directly; the key should be D.
- **R&W M1 #18 (csv 1567)**: broken. B is the correct restrictive, comma-free form, but choices C and D are identical in both the bank and our copy, so the question is defective; I merged the three duplicate reports into one and proposed no fix because the original wording of C or D cannot be recovered with confidence.
- **R&W M2 #6 (csv 1582)**: broken. Broken as printed because the underline is missing in both the bank and the transcription; key B fits if "more than 7,000 in all" is underlined (the bank explanation also points to the attendance count), so the fix adds that underline.
- **R&W M2 #15 (csv 1646)**: broken. Broken: the keyed choice B says "negatively correlated", which contradicts the passage (more vertebrate hosts went with more decline). The bank's own explanation describes a positive relationship, so the choice was likely corrupted from "positively". C overreaches, so it is no clean replacement.
- **R&W M2 #16 (csv 1647)**: key_wrong. Key B → A. Key wrong: B attaches the opening phrase "Knowing that..." to "the researchers' theory", a dangling modifier. A is the only choice whose subject is "the researchers".
- **R&W M2 #24 (csv 1657)**: key_wrong. Key A → C. Key changed from A to C: A never mentions the sculpture or its dimensions, while C alone gives its size (roughly 2 feet wide and 9 feet tall); the duplicate cosmetic issue about choice D was merged into one.
- **R&W M2 #25 (csv 1658)**: key_wrong. Key B → A. Key changed from B to A: the goal is to identify the painting and only A names Portrait of Mme. Picasso, while B names no painting; the duplicate cosmetic issue about choice C was merged into one.

## Yellow

- solver medium: 7
- solver disagrees with the key: 4
- transcription medium: 2
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 6, with the final key on 1; confidence high 95, medium 3, low 0.
- solve_b (sonnet): disagrees with the bank key on 9, with the final key on 4; confidence high 92, medium 6, low 0.
- Both disagree with the bank key: 5 (R&W M1 #12 (csv 2284); R&W M1 #14 (csv 1563); R&W M2 #16 (csv 1647); R&W M2 #24 (csv 1657); R&W M2 #25 (csv 1658)).
- The two solvers disagree with each other: 5.

## Transcription

- Confidence: high 96, medium 2, low 0.
- Question and choice images: 62; kept as figures 9 (graph 5, geometry 2, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 58.

## Explanations

- Bank explanation: usable 57, minor_issue 26, wrong 13, mismatch 0, missing 2.
- Final: drafted 54, kept from the bank 44.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 804,887 | $2.25 |
| solve_a | opus | 10 | 726,252 | $4.07 |
| solve_b | sonnet | 10 | 727,427 | $2.04 |
| explain | sonnet | 10 | 861,703 | $2.41 |
| adjudicate | opus | 4 | 330,129 | $1.85 |
| **Subagents** | | 44 | **3,450,398** | **$12.62** |

Per question ≈ 35,208 tokens, ≈ $0.129 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Source row issue: english-m1-18 has two identical choices in the bank (duplicate choice text 'towns, that dot the island of puerto rico').
