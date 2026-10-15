# Check and write SAT explanations, tag questions

Read `tools/prompts/format.md` first. Then read your input file: a JSON array, one question per
item. Each item has:
- the transcribed question, with its figures in `figures["r2:<key>"]` (open them with the Read
  tool);
- the bank's key (`bank_key`, plus `bank_accepted` for grid-ins);
- the bank's explanation (`bank_explanation` text and/or `explanation_images`; open every
  image).

Read no other files.

## For each question

1. **Solve it yourself first,** then read the bank's explanation.
2. **Rate the bank explanation** with `bank_status`:
   - `usable`: correct and clear.
   - `minor_issue`: correct, with small flaws (wording, typos, a skipped step).
   - `wrong`: its reasoning or result is incorrect.
   - `mismatch`: it explains a different version of the question (other numbers or choices).
   - `missing`: there isn't one.

   For `wrong` and `mismatch`, put the exact words you dispute in `disputed_quote`, copied
   from the explanation.
3. **The final explanation** (`explanation`):
   - `policy: "draft"` (Math): always write a new one.
   - `policy: "keep_if_usable"` (Reading and Writing): if the bank's is `usable` or
     `minor_issue`, convert it to the content format without changing its wording, and set
     `explanation_source: "bank"`. Otherwise write a new one.
   - A new explanation (`explanation_source: "drafted"`) is written for a student: 2 to 6
     short steps that show why the answer is right. For Reading and Writing, add one line on
     why each wrong choice is wrong. End it with the line `**Answer:** X`.
4. **`answer_stated`:** the answer your final explanation concludes (a letter, or the number
   for grid-ins).
   - If you believe the bank key is wrong, explain the answer you believe is right, and say
     why the key fails in `key_concern`.
   - Otherwise `key_concern` is `null`.
5. **Tags:** `domain` and `skill` exactly as named in the list below. The `domain_hint` and
   `skill_hint` come from the bank and are usually right; fix them if the question says
   otherwise. `difficulty` is your estimate: `easy`, `medium` or `hard`, as on the real SAT.
6. **`issues`:** only problems you notice in the question itself, not in the explanation.
   Use the issue format in `format.md`. Usually this is empty.

Reading and Writing:
- Information and Ideas: Central Ideas and Details; Inferences; Command of Evidence (Textual);
  Command of Evidence (Quantitative)
- Craft and Structure: Words in Context; Text Structure and Purpose; Cross-Text Connections
- Expression of Ideas: Rhetorical Synthesis; Transitions
- Standard English Conventions: Boundaries; Form, Structure, and Sense

Math:
- Algebra: Linear equations in one variable; Linear functions; Linear equations in two
  variables; Systems of two linear equations in two variables; Linear inequalities in one or
  two variables
- Advanced Math: Nonlinear functions; Nonlinear equations in one variable and systems of
  equations in two variables; Equivalent expressions
- Problem-Solving and Data Analysis: Ratios, rates, proportional relationships, and units;
  Percentages; One-variable data: distributions and measures of center and spread;
  Two-variable data: models and scatterplots; Probability and conditional probability;
  Inference from sample statistics and margin of error; Evaluating statistical claims:
  observational studies and experiments
- Geometry and Trigonometry: Area and volume; Lines, angles, and triangles; Right triangles
  and trigonometry; Circles

## Output

Use the Write tool to save a JSON array to your output path, in the input order:

```json
{"qid": "...", "bank_status": "usable|minor_issue|wrong|mismatch|missing", "disputed_quote": null,
 "explanation": "...", "explanation_source": "bank|drafted", "answer_stated": "B", "key_concern": null,
 "domain": "...", "skill": "...", "difficulty": "easy|medium|hard", "issues": []}
```

Reply with one line only: `done <batch> <number of questions>`.
