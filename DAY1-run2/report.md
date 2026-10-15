# DAY1 AI review report

Scope: SAT MAKON practice test `DAY1` only. 98 questions: 54 Reading & Writing (27 per module) and 44 Math (22 per module). Output files are in `/home/user/review-output/DAY1/`: `questions.jsonl`, `report.md`, `preview.html`.

## 1. Counts

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| English (R&W) | 36 | 14 | 4 | 54 |
| Math | 30 | 11 | 3 | 44 |
| **Total** | **66** | **25** | **7** | **98** |

Verdicts: key_correct 91 · key_wrong 3 · broken 3 · ambiguous 1. Adjudicated by the main session: 33 questions (English 19, Math 14). Three bank keys were judged wrong or unsound, and two subagent claims were rejected (see §6).

## 2. Red questions (need a teacher decision before publishing)

- **English M1 #5** — key_wrong (B → D). Both solvers and the explanation checker chose D. B is arguable, so a teacher should confirm.
- **English M2 #11** — ambiguous. Solver A chose C (magical-realism link), solver B chose A (juxtaposition). Key A is defensible; C is a serious alternative.
- **English M2 #13** — broken. Printed choice D says "negatively correlated", which contradicts the data. Key D only works if the source says "positively". Both solvers avoided D (A=C medium, B=C low).
- **English M2 #19** — key_wrong. Key D ("designation, however;") is ungrammatical. B and C are both grammatical, so a teacher must choose one (proposed C).
- **Math M1 #8** — broken. The question image is cropped after "f(x) = 7x + 3,". Key D is plausible, but the full stem needs re-cropping.
- **Math M1 #12** — broken. Choices C and D are identical (x = by − 49). Key B is right for the printed choices. The bank explanation treats C as y(b−49), which would make two correct answers. Check the source.
- **Math M2 #17** — key_wrong (192 → 192.1). 56 × 1.852² = 192.07, which is 192.1 to the nearest tenth. Both solvers agree on 192.1.

## 3. Yellow questions (25)

Common reasons: a solver below high confidence (English M1 #2, #15, #25; English M2 #5, #8, #9, #16, #18, #20, #27; Math M2 #15, #20, #22), a solver disagreement that was resolved to the key (English M1 #27, English M2 #17), an explanation missing or wrong that was drafted (English M1 #17, Math M1 #13, #17; English M2 #10; Math M2 #9, #14, #19, #21), an image/stem mismatch (Math M1 #2), or a transcription at medium confidence (Math M2 #13). Full per-question detail is in `questions.jsonl` and the preview.

## 4. Solver stats (blind solves, haiku A and sonnet B)

- Solver A and B disagreed with each other on **7** questions.
- Solver A disagreed with the bank key on **6** questions; solver B on **6**.
- Both solvers disagreed with the bank key on **4**: English M1 #5, English M2 #13, English M2 #19, Math M2 #17.
- Confidence: solver A high 84 / medium 13 / low 1; solver B high 87 / medium 10 / low 1.
- Solvers never saw the key, explanation, or CSV. They saw only the transcribed question and figure images.

## 5. Transcription stats

- Transcription confidence: high 95, medium 2 (Math M2 #13, Math M1 #17), low 1 (Math M1 #8).
- Images referenced by DAY1: 81 unique objects (38 question-side, 43 explanation). All 81 downloaded from `media/`. 38 were upscaled 2–3× (narrower than 800 px).
- Question-side images: **4 kept as figures** (Math M1 #1 graph, Math M1 #2 bar chart, Math M2 #9 dot plot, English M2 #10 bar chart) and **34 converted to text or LaTeX** (equations, tables, text screenshots). Three table images (English M1 #11 and #12, M2 #8) were converted to Markdown tables.
- Explanation images (43, math only): OCR'd by the explanation checker. Several were cut off at the crop edge (noted in issues).
- Image-text mismatches: 1 (Math M1 #2: the stem says "frequency table" but the figure is a bar chart).
- Hard cases: cropped images (Math M1 #8), question text only in image with the CSV blank (most Math items), glyph corruption in choices (Math M2 #20 "lI", "| and ||"), underline lost (English M2 #8).

## 6. Adjudication (main session, 33 questions)

Where I overrode a bank key or a subagent claim:
- **English M1 #5**: key B → D proposed (explanation checker and both solvers agree). Marked red.
- **English M1 #16**: the explanation checker called the bank explanation wrong ("comma splice"). I rejected that claim: D is the only choice whose subject is the painting. Bank explanation kept.
- **Math M2 #9**: key D confirmed by reading the dot plot (median stays 724; mean drops 725.4 → 691.5). The bank's median reasoning was wrong, so a drafted explanation replaces it. Here the explanation checker was right.
- **Math M2 #17**: key 192 corrected to 192.1 (arithmetic check).
- **English M2 #19**: key D rejected (ungrammatical). Proposed C; B also valid.
- **English M2 #11**: ambiguous, not resolved.

Equivalent grid-in forms were accepted, not treated as disagreement: English M1 #20 (45/8 = 5.625), M1 #21 (1/8 = 0.125).

## 7. Explanation stats

Checker status (before adjudication): usable 64, minor_issue 19, wrong 7, mismatch 6, missing 2. Final: 14 explanations were replaced with drafted ones (where the bank was wrong, mismatched, or missing), 84 kept from the bank. 19 minor wording issues were kept as cosmetic.

Missing explanations: English M1 #17, Math M1 #13 (both drafted and checked).

## 8. Tags (domain / skill / difficulty) — read this before using them

- **Domain** comes from the bank's `domain_id`. English mapping is confirmed by stems: 2 Craft and Structure, 3 Information and Ideas, 4 Standard English Conventions, 5 Expression of Ideas. Math mapping is inferred (6 Algebra, 7 Advanced Math, 8 Problem-Solving and Data Analysis, 9 Geometry and Trigonometry) and spot-checked against stems.
- **English skill** comes from `type_id` clusters inferred from the stems (3 Words in Context, 4 Text Structure and Purpose, 5 Cross-Text Connections, 6 Central Ideas, 7 Command of Evidence, 8 Inferences, 9 Boundaries, 10 Form, Structure, and Sense, 11 Rhetorical Synthesis, 12 Transitions). Not all clusters were verified item by item.
- **Math skill** is my best-fit label per item from the stem. Some (e.g. Math M1 #11) are marked best-fit and need checking.
- **Difficulty is a position-based estimate** (items 1–8 easy, 9–16 medium, 17–27 hard within each module). The bank has no difficulty field. Do not treat it as measured.

## 9. Cost

Measured subagent usage (from harness usage lines, 20 of 40 subagents): 1,341,365 tokens (transcription M1 5 agents: 356,303; solve+explain M2 15 agents: 985,062). The other 20 subagents are not in my logs; I estimated 65k each (1.3M). Total ≈ **2.64M subagent tokens** for 98 questions. Split by agent count: Haiku 30 agents (≈1.98M), Sonnet 10 agents (≈0.66M). Assumed input/output split 90/10.

Prices (API list, per million tokens): Haiku 5.5 = $0.10 input / $0.50 output; Sonnet 5.5 = $2.00 input / $10.00 output. Batch API = 50%.

| Model | Steps covered | Agents | Approx. tokens | Approx. cost (list) |
|---|---|---:|---:|---:|
| Haiku 5.5 | transcription, blind solve A, explanation check | 30 | ~1.98M | ~$0.28 |
| Sonnet 5.5 | blind solve B | 10 | ~0.66M | ~$1.85 |
| **Total** | | **40** | **~2.64M** | **~$2.13** |

Per-step token counts were not captured separately, so the split is by model only.

Per question: **~$0.022** at list price, **~$0.011** with Batch API. Extrapolated to the full bank (2,870 Math + 3,507 R&W = 6,377 questions): **~$138** at list, **~$69** with Batch. This covers subagent tokens only. It excludes the orchestrator, retries, and prompt caching (which would lower input cost). It also assumes the same fan-out, which means about 2,600 subagents at full scale (0.41 per question).

Orchestrator (main session, Haiku 5.5): the session budget counter used about 0.3M tokens for the whole run, including data prep, adjudication and report writing. Its cost is small but not measured separately.

Wall clock (estimated from agent durations, not timed): about 30–40 minutes end to end. Batches ran in parallel within each phase.

## 10. What I would change

1. **Fewer, larger subagent calls.** Merge explanation check into the transcription call (it already reads the same images). That cuts 10 subagents.
2. **Deterministic checks in code, not models.** Grid-in answers can be checked numerically in a script. Duplicate choices, empty fields and image counts can be checked before solving. Many issues found here were mechanical.
3. **Separate the "is this a faithful transcription" pass from the solve.** Several flags came from the checker judging the bank wording, not the content.
4. **Tighten the explanation checker.** It made one wrong claim that I overturned (English M1 #16, "comma splice"). It was right on Math M2 #9, where the bank median reasoning was wrong. Require it to quote the exact text it disputes, and require a second check on any drafted explanation.
5. **Fix upstream data.** Every Math row has an empty `explained` field, and 2 English rows have no explanation. Crops cut off several images. Choice images need a numbered glyph check. The CSV loses underlines (English M2 #8) and stray characters appear in stems.
6. **Tag from a taxonomy table.** Ship a `type_id` → skill table so tags are not inferred per run.
7. **Use Batch API and prompt caching** for the full bank. Shared instructions can be cached.

## 11. Limitations

- Solvers are LLMs. A "key_correct" verdict with both solvers agreeing is strong evidence but not proof. The 33 adjudicated items were checked by me from the transcribed text and the bank explanations. I opened the figure images only for the cases where the figure mattered (Math M1 #2 and Math M2 #9); for other figure items I relied on solver agreement.
- The `preview.html` embeds downscaled screenshots (900 px JPEG). The converted text is the same as in `questions.jsonl`.
