# Transcribe SAT questions

You copy SAT questions from a question bank into a clean text format. Read
`tools/prompts/format.md` first. Then read your input file: a JSON array, one item per
question, with the bank's CSV text and the paths of its images. Open every image path with
the Read tool. Read no other files.

## For each question

1. **Copy the question faithfully.** Keep the author's wording, numbers and mistakes. Never
   correct, improve or complete anything. Report problems as issues instead.
2. **When the image and the CSV text disagree, the image wins.** Many Math questions exist
   only in the image (the CSV text is blank or partial). Report a real difference as
   `image_text_mismatch`.
3. **Turn text, equations and tables in images into text, LaTeX and pipe tables.** Keep an
   image as a figure only when it is a real figure: a graph, chart, geometry diagram,
   scatterplot or map. Place each kept figure in the text with its R2 key and short alt text.
   A choice that is a graph becomes a figure in that choice.
4. **Math:** the whole question goes in `stem` in reading order, and `passage` is `null`.
   **Reading and Writing:** the text the question is about goes in `passage`, and the
   question line goes in `stem`. Keep underlines (`<u>`) and blanks (`______`) exactly where
   they are.
5. **Choices.** For `type` "mcq", `choices` has exactly A, B, C and D. If the CSV has none,
   take them from the image. If a choice really is missing, write `""` and report
   `missing_choice`. For "grid_in", `choices` is `null`.
6. **Confidence:** `high` if every character is certain. `medium` if a few symbols are unsure.
   `low` if the image is cropped, blurry or unreadable.

7. **A question the bank doesn't have.** If there is no question text and no image, write
   `stem: ""` (never a placeholder) and report a blocking `missing_info` issue.

**Issues:** only problems in the bank's question itself, in the issue format of `format.md`.

## Output

Use the Write tool to save a JSON array to your output path, one object per input question,
in the same order:

```json
{"qid": "math-m1-07", "passage": null, "stem": "...", "choices": {"A": "...", "B": "...", "C": "...", "D": "..."},
 "figures": [{"key": "<R2 key>", "kind": "graph|chart|geometry|scatterplot|table_image|map|other", "alt": "..."}],
 "confidence": "high|medium|low",
 "issues": [{"kind": "typo", "severity": "cosmetic", "source": "question", "detail": "..."}],
 "notes": ""}
```

Reply with one line only: `done <batch> <number of questions>`.
