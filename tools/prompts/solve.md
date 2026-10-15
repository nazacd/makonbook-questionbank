# Solve SAT questions

You are taking SAT questions, Reading and Writing or Math. Read your input file: a JSON array,
one question per item. Text uses `\( \)` for math, `<u>` for underlines and
`![...](r2:key)` for figures. Each figure's image is at `figures["r2:<key>"]`: open it with the
Read tool. Read no other files, and don't search for answers anywhere.

For each question, work it out carefully on your own, then give:
- `answer`:
  - "mcq": exactly one letter, A to D.
  - "grid_in": a number, either an integer, a decimal or a fraction like `17/2`, with no units
    or commas. If several answers work, give one of them.
  - `"none"`: if no choice is correct or the question can't be answered as written. Say why in
    the reasoning.
- `confidence`: `high` only if you would bet on it. `medium` if another choice is plausible.
  `low` if you are guessing or the question seems broken.
- `reasoning`: 1 to 3 sentences, with the deciding step or rule.

Use the Write tool to save a JSON array to your output path, in the input order:

```json
{"qid": "english-m1-05", "answer": "D", "confidence": "high", "reasoning": "..."}
```

Reply with one line only: `done <batch> <number of questions>`.
