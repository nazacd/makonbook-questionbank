# DAY30 AI review

Test ids DAY30: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 40 | 13 | 1 | 54 |
| Math | 42 | 1 | 1 | 44 |
| **Total** | **82** | **14** | **2** | **98** |

Verdicts: key_correct 96, broken 1, key_wrong 1. Adjudicated: 20.

## Red: a teacher decides before publishing

- **Math M1 #7 (csv 1115)**: broken. Broken: the original image prints j/4 = k + 13m, giving j = 4(k + 13m), which matches no choice; changing the 4 to 7 (and dropping the stray "The question is:") makes key B correct; the duplicate 'other' issue was merged into the typo issue.
- **R&W M2 #14 (csv 1538)**: key_wrong. Key D → B. Key changed from D to B: the premise that surroundings affect sparrow hormones predicts a captive-versus-wild difference, which only B states, while D describes within-group individual variation; both solvers and the checker agree.

## Yellow

- solver medium: 14
- solver disagrees with the key: 2
- transcription medium: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 2, with the final key on 1; confidence high 93, medium 4, low 1.
- solve_b (sonnet): disagrees with the bank key on 4, with the final key on 3; confidence high 87, medium 11, low 0.
- Both disagree with the bank key: 2 (Math M1 #7 (csv 1115); R&W M2 #14 (csv 1538)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 97, medium 1, low 0.
- Question and choice images: 104; kept as figures 4 (geometry 2, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 81.

## Explanations

- Bank explanation: usable 72, minor_issue 18, wrong 6, mismatch 1, missing 1.
- Final: drafted 50, kept from the bank 48.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 799,623 | $2.24 |
| solve_a | opus | 10 | 716,380 | $4.01 |
| solve_b | sonnet | 10 | 716,982 | $2.01 |
| explain | sonnet | 10 | 833,313 | $2.33 |
| adjudicate | opus | 4 | 329,374 | $1.84 |
| **Subagents** | | 44 | **3,395,672** | **$12.44** |

Per question ≈ 34,649 tokens, ≈ $0.127 at API list prices (90/10 input/output split assumed; the main session is not included).
