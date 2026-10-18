# Content format

Every text field (passage, stem, choices, explanation) uses this format and nothing else:

- Paragraphs separated by one blank line. A single line break stays a line break. Each further
  blank line is an empty line of space (teachers add these in the editor); reviews write one.
- Math: inline `\( ... \)`, display `\[ ... \]` (LaTeX). Never `$`. A plain number or a money amount
  like $5 is plain text.
- `*italic*`, `**bold**`, `***bold italic***`, `<u>underlined</u>`. Italic may hold bold (`*a **b** c*`). No other HTML.
- Lists: each line starts with `- `.
- Tables: GitHub pipe tables. First row is the header, second row is the separator `|---|---|`.
- Figures: `![short description](r2:<R2 key>)` on its own line, where it appears in the question.
- Paired passages: `**Text 1**` and `**Text 2**` as their own paragraphs before each text.
- A blank to fill: `______` (six underscores).

# Issues

Every `issues` entry is `{"kind": ..., "severity": ..., "source": ..., "detail": ...}` with
exactly these values. Anything else fails the check.

- `kind`: wrong_key, missing_key, typo, grammar, missing_choice, duplicate_choice,
  choice_formatting, unreadable_image, missing_image, image_text_mismatch, ambiguous,
  missing_info, off_format, other.
- `severity`:
  - `cosmetic`: the meaning is unchanged.
  - `content`: it could confuse a student or change an answer.
  - `blocking`: the question can't be answered as shown, for example cropped, with a
    missing choice, or unreadable.
- `source`: `question` or `figure`. Problems in an explanation are never issues.
- `detail`: one sentence that quotes the problem.
