# makonbook-questionbank

Staging area for the AI review of SAT MAKON's practice tests. Every reviewed test is imported
once into the MakonBook database, where editors and teachers continue from there. Nothing
here is served to students.

- `tools/REVIEW.md`: how a Claude Code session reviews one test (start there).
- `tools/review.py`: the mechanical steps (prep, staging, merge, check, report, preview).
  Tests: `cd tools && python3 -m unittest test_review.py`.
- `tools/prompts/`: what each kind of subagent is told.
- `figures/`: figures the fix step redrew (PNG). The API uploads them to MakonBook's bucket
  on import, under the same name.
- `DAY2/`, `DAY3/`, …: one folder per reviewed test, with `questions.jsonl` (the import
  input), `report.md` and `preview.html`.
- `DAY1/`: the pilot. It uses an older record format, so re-run it with the current tools
  before importing.

`python3 tools/review.py check DAY2` validates a folder.

Keep this repository private: it holds the school's test content.

Records carry the bank's original screenshots (`source.images`, R2 keys) for the
editor panel. Tests reviewed before that was added get them with
`python3 tools/review.py add-images . --math <math csv> --english <english csv>`
(safe to run again: it only fills records that lack them).
