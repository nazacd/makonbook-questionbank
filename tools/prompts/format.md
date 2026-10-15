# Content format

Every text field (passage, stem, choices, explanation) uses this format and nothing else:

- Paragraphs separated by one blank line. A single line break stays a line break.
- Math: inline `\( ... \)`, display `\[ ... \]` (LaTeX). Never `$`. A plain number or a money amount
  like $5 is plain text.
- `*italic*`, `**bold**`, `<u>underlined</u>`. No other HTML.
- Lists: each line starts with `- `.
- Tables: GitHub pipe tables. First row is the header, second row is the separator `|---|---|`.
- Figures: `![short description](r2:<R2 key>)` on its own line, where it appears in the question.
- Paired passages: `**Text 1**` and `**Text 2**` as their own paragraphs before each text.
- A blank to fill: `______` (six underscores).
