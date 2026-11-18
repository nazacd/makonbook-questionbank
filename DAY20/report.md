# DAY20 AI review

Test ids DAY20: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 7 | 0 | 54 |
| Math | 39 | 3 | 2 | 44 |
| **Total** | **86** | **10** | **2** | **98** |

Verdicts: key_correct 96, broken 1, ambiguous 1. Adjudicated: 14.

## Red: a teacher decides before publishing

- **Math M2 #18 (csv 926)**: broken. Choice D is missing in both the bank and the original, so the question is broken as printed, though B (side 20, perimeter 60) is the correct answer among the given choices.
- **Math M2 #20 (csv 929)**: ambiguous. The seven integers sum to 420, and the eighth must be 4 mod 8, above 60 and below 80, so both 68 and 76 work; the stem should ask for the greatest possible value to make 76 the unique answer.

## Yellow

- solver medium: 11
- content: grammar: 2
- content: missing_info: 1
- content: choice_formatting: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 1, with the final key on 0; confidence high 92, medium 6, low 0.
- solve_b (sonnet): disagrees with the bank key on 0, with the final key on 0; confidence high 91, medium 7, low 0.
- Both disagree with the bank key: 0.
- The two solvers disagree with each other: 1.

## Transcription

- Confidence: high 98, medium 0, low 0.
- Question and choice images: 104; kept as figures 4 (graph 3, chart 1), the rest turned into text.
- Upscaled for the models: 64.

## Explanations

- Bank explanation: usable 74, minor_issue 20, wrong 1, mismatch 2, missing 1.
- Final: drafted 45, kept from the bank 53.

## Usage

| Step | Model | Agents | Tokens | Est. API cost |
|---|---|---:|---:|---:|
| transcribe | sonnet | 10 | 821,926 | $2.30 |
| solve_a | opus | 10 | 730,267 | $4.09 |
| solve_b | sonnet | 10 | 725,022 | $2.03 |
| explain | sonnet | 10 | 882,959 | $2.47 |
| adjudicate | opus | 3 | 253,434 | $1.42 |
| **Subagents** | | 43 | **3,413,608** | **$12.31** |

Per question ≈ 34,832 tokens, ≈ $0.126 at API list prices (90/10 input/output split assumed; the main session is not included).

## Notes from the session

Prep flagged math-m2-18 (choice D empty in the bank row); no agent re-runs were needed.

## Fixes

Every question that isn't green, corrected for students; teachers approve or deny each fix.

- **Math M1 #11 (csv 898)** (yellow, corrected, high): Capitalized "What" at the start of the last sentence; the original has the same lowercase typo.
- **Math M2 #5 (csv 913)** (yellow, no change, high): No change: the stem matches the original, and like SAT interpretation items it leaves x and y undefined on purpose, since working out what 3x means is the skill being tested.
- **Math M2 #9 (csv 917)** (yellow, corrected, high): Added the missing ", where m" so the sentence reads "= m, where m is a constant"; the original has the same garbled wording.
- **Math M2 #18 (csv 926)** (red, invented, corrected, high): Choice D was empty in both the bank and the original, so I wrote a distractor, 30√3 (the perimeter you get if you take the height as the side length), and cleaned up the stem's wording ("height length" to "height", "length of perimeter" to "perimeter").
- **Math M2 #20 (csv 929)** (red, invented, high): The original asks for "the value of the largest integer", but both 68 and 76 work, so I changed the stem to ask for "the greatest possible value of the largest integer" and accepted only 76.
- **R&W M1 #6 (csv 950)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the passage and choices are clean and key D is the only accurate description of the structure.
- **R&W M1 #7 (csv 951)** (yellow, restored, high): Restored the em dash in "at a great price—*free*", which the original screenshot shows as a stray cursor bar and our text had dropped.
- **R&W M1 #11 (csv 955)** (yellow, no change, high): No change needed: the question is clear and key D is the only choice that weakens the claim that bear hibernation research will help astronauts.
- **R&W M2 #3 (csv 974)** (yellow, corrected, high): Added the article "a" to choices A and D so every choice fits "Cullen became ______ poet" grammatically, leaving meaning as the only test.
- **R&W M2 #8 (csv 979)** (yellow, no change, high): No change needed: the solvers were only moderately sure, but the father's curt "No!" said "with terrible finality" clearly makes B the one right answer.
- **R&W M2 #11 (csv 982)** (yellow, restored, high): Restored the cut-off end of choice D (the last two lines of Stevenson's final stanza, which the explanation quotes as "fast asleep in bed") and added its closing quotation mark.
- **R&W M2 #24 (csv 995)** (yellow, no change, high): No change needed: the solver was only moderately sure, but the text is complete and clear, and the cholesterol sentence is plainly an instance of the bodily flaws just mentioned.
