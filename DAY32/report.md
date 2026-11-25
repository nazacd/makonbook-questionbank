# DAY32 AI review

Test ids DAY32: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 44 | 8 | 2 | 54 |
| Math | 38 | 6 | 0 | 44 |
| **Total** | **82** | **14** | **2** | **98** |

Verdicts: key_correct 96, ambiguous 1, key_wrong 1. Adjudicated: 21.

## Red: a teacher decides before publishing

- **R&W M2 #16 (csv 1791)**: ambiguous. A is very likely right: keeping the same silver in a lighter coin lifts its silver share, while B's higher trade threshold would make things worse; the solvers split with only medium confidence, though, so under the rules this goes to a teacher as ambiguous, with a proposed change of key to A.
- **R&W M2 #27 (csv 1802)**: key_wrong. Key D → C. Key D is wrong because it is limited to three named minerals; C is the only choice that makes a general claim (any mineral numbered 9 can scratch any numbered 5), as both solvers found, so the key should be C.

## Yellow

- solver medium: 9
- content: typo: 4
- solver disagrees with the key: 3
- content: other: 1
- content: missing_info: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 2; confidence high 93, medium 5, low 0.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 2; confidence high 90, medium 8, low 0.
- Both disagree with the bank key: 2 (R&W M2 #20 (csv 1795); R&W M2 #27 (csv 1802)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 84; kept as figures 3 (graph 2, scatterplot 1), the rest turned into text.
- Upscaled for the models: 80.

## Explanations

- Bank explanation: usable 76, minor_issue 10, wrong 8, mismatch 2, missing 2.
- Final: drafted 49, kept from the bank 49.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 781,151 | $2.19 |
| solve_a | opus | 10 | 717,061 | $4.02 |
| solve_b | sonnet | 10 | 716,318 | $2.01 |
| explain | sonnet | 10 | 832,161 | $2.33 |
| adjudicate | opus | 4 | 339,100 | $1.90 |
| **Subagents** | | 44 | **3,385,791** | **$12.44** |

Per question ≈ 34,548 tokens, ≈ $0.127 at API list prices (90/10 input/output split assumed; the main session is not included).
