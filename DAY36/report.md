# DAY36 AI review

Test ids DAY 36: 98 questions. Models: transcribe sonnet, solve_a opus, solve_b sonnet, explain sonnet, adjudicate opus, fix opus.

## Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| R&W | 47 | 4 | 3 | 54 |
| Math | 37 | 1 | 6 | 44 |
| **Total** | **84** | **5** | **9** | **98** |

Verdicts: key_correct 90, broken 7, key_wrong 1. Adjudicated: 14.

## Red: a teacher decides before publishing

- **Math M1 #9 (csv 2963)**: broken. Broken: all four answer tables are blank and their images are unreadable, so key B cannot be checked; duplicate issues merged.
- **Math M1 #17 (csv 2971)**: broken. Broken: the scatterplot the question depends on is unreadable, so key D cannot be verified; duplicate issues merged.
- **Math M2 #5 (csv 2981)**: broken. Broken: all four answer tables are blank and their images are unreadable, so key D cannot be checked; duplicate issues merged.
- **Math M2 #12 (csv 2988)**: key_correct. Key B stands: parallel lines give alternate interior angles and B gives vertical angles, and the naming ABC/EBD makes AB and EB corresponding sides, so AB=EB gives AAS; the missing figure is downgraded to content since the answer follows from the text.
- **Math M2 #15 (csv 2991)**: broken. Broken: the graph that determines the slope and intercept signs is unreadable, so key A cannot be verified; duplicate issues merged.
- **Math M2 #19 (csv 2995)**: broken. Broken: the table the question depends on is an unreadable image, so the key -3640 cannot be checked; duplicate missing_image issues merged into one.
- **R&W M1 #11 (csv 3706)**: broken. Broken: the table the question asks about is an unreadable image, so key D (1986) cannot be verified; duplicate missing_image issues merged into one.
- **R&W M2 #9 (csv 3731)**: broken. Broken: the graph needed to choose among A, B and C is an unreadable image, so key B cannot be verified (D is out of scope as it compares Form 990 filers); duplicate missing_image issues merged and the stray-word issue kept.
- **R&W M2 #19 (csv 3741)**: key_wrong. Key A → C. Key A is wrong: the material after the blank is a verbless absolute phrase, which cannot follow a semicolon and must attach to the main clause with a comma, so C is correct, as both solvers found with high confidence.

## Yellow

- solver medium: 4
- content: missing_image: 1
- transcription medium: 1

## Solvers

- solve_a (opus): disagrees with the bank key on 8, with the final key on 7; confidence high 90, medium 1, low 7.
- solve_b (sonnet): disagrees with the bank key on 8, with the final key on 7; confidence high 86, medium 5, low 7.
- Both disagree with the bank key: 8 (Math M1 #9 (csv 2963); Math M1 #17 (csv 2971); Math M2 #5 (csv 2981); Math M2 #15 (csv 2991); Math M2 #19 (csv 2995); R&W M1 #11 (csv 3706); R&W M2 #9 (csv 3731); R&W M2 #19 (csv 3741)).
- The two solvers disagree with each other: 2.

## Transcription

- Confidence: high 89, medium 1, low 8.
- Question and choice images: 16; kept as figures 1 (geometry 1), the rest turned into text.
- Upscaled for the models: 0.

## Explanations

- Bank explanation: usable 0, minor_issue 0, wrong 0, mismatch 0, missing 98.
- Final: drafted 98, kept from the bank 0.

## Usage

Not logged.
