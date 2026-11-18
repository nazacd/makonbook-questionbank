# DAY23 AI review

Test ids DAY23: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 36 | 14 | 4 | 54 |
| Math | 40 | 4 | 0 | 44 |
| **Total** | **76** | **18** | **4** | **98** |

Verdicts: key_correct 94, ambiguous 4. Adjudicated: 26.

## Red: a teacher decides before publishing

- **R&W M1 #24 (csv 1248)**: ambiguous. Ambiguous: both C (kin selection improves relatives' survival) and B (group work better ensured survival) state an evolutionary advantage of eusociality, and the solvers split at medium confidence, so a teacher should decide.
- **R&W M2 #14 (csv 1265)**: ambiguous. Ambiguous: both solvers chose A, which expresses regret over his dishonesty at least as well as keyed C, whose line is about keeping his name, but a literary-interpretation dispute cannot be proved, so a teacher should decide.
- **R&W M2 #15 (csv 1266)**: ambiguous. Ambiguous: every choice is accurate to the table and the cue "intrigued" supports B while the demonstration aim supports D, so nothing singles out one answer; the two duplicate ambiguity issues were merged and the bank explanation's misquoted numbers need a teacher rewrite once a key is chosen.
- **R&W M2 #20 (csv 1271)**: ambiguous. Ambiguous: a period and a colon are both standard between these two independent clauses, and the solvers split with medium confidence, so keyed B cannot be proven unique or wrong.

## Yellow

- solver medium: 18
- content: ambiguous: 2
- content: grammar: 2
- content: other: 1
- solver disagrees with the key: 1
- content: typo: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 3, with the final key on 3; confidence high 88, medium 10, low 0.
- solve_b (sonnet): disagrees with the bank key on 3, with the final key on 3; confidence high 83, medium 15, low 0.
- Both disagree with the bank key: 1 (R&W M2 #14 (csv 1265)).
- The two solvers disagree with each other: 4.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 122; kept as figures 8 (graph 5, geometry 1, scatterplot 1, chart 1), the rest turned into text.
- Upscaled for the models: 91.

## Explanations

- Bank explanation: usable 66, minor_issue 25, wrong 7, mismatch 0, missing 0.
- Final: drafted 48, kept from the bank 50.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 837,404 | $2.34 |
| solve_a | opus | 10 | 739,166 | $4.14 |
| solve_b | sonnet | 10 | 731,345 | $2.05 |
| explain | sonnet | 10 | 885,281 | $2.48 |
| adjudicate | opus | 5 | 432,456 | $2.42 |
| **Subagents** | | 45 | **3,625,652** | **$13.43** |

Per question ≈ 36,996 tokens, ≈ $0.137 at API list prices (90/10 input/output split assumed; the main session is not included).
