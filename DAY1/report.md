# DAY1 pilot: AI review of the SAT MAKON question bank

Scope: test `DAY1`, 98 questions (Math 44 = 22 + 22, Reading & Writing 54 = 27 + 27).
Files: `questions.jsonl` (one record per question), `preview.html` (side-by-side check page; open it locally, it loads the screenshots from `images/`), this report.
Run date: 2026-10-14. Nothing was written to R2, the database or the app repository (makonbook-api); R2 was read only.

## 1. Results at a glance

| Subject | green | yellow | red | total |
|---|---:|---:|---:|---:|
| Math | 17 | 24 | 3 | 44 |
| Reading & Writing | 28 | 23 | 3 | 54 |
| **Total** | **45** | **47** | **6** | **98** |

| Verdict | Count |
|---|---:|
| key_correct | 92 |
| key_wrong | 2 |
| ambiguous | 3 |
| broken | 1 |
| unsolvable | 0 |

### Every red question (key_wrong / broken / ambiguous)

| Subject · module · # (csv id) | Verdict | Reason |
|---|---|---|
| Math M2 #17 (40) | key_wrong → **192.1** | "To the nearest tenth": 56 × 1.852² = 192.07 → 192.1. The key 192 is the nearest whole number. Both solvers got 192.1. The alternative fix is to change the stem to "nearest whole number". |
| R&W M1 #5 (5) | key_wrong → **D** | The underlined finding (cooling of the surrounding air) is what inspired the air-cooling device, the practical application. B (evidence of hypothermia) misreads it. Both solvers chose D, and the bank's own explanation argues for B. |
| Math M1 #12 (13) | broken | Choices C and D are the same image ("x = by − 49"). The key B is still correct, but the item needs a new fourth choice. |
| Math M2 #22 (45) | ambiguous | Statement I says "angles B and C are equal" (both in the same triangle). Read literally, key B holds. If the source meant B and E, no choice is correct. A teacher should check the source. |
| R&W M2 #13 (39) | ambiguous | Keyed choice D says "negatively correlated", but the passage implies a positive correlation, so no choice is correct as written. Proposed fix: change "negatively" to "positively" in D (key stays D). |
| R&W M2 #18 (44) | ambiguous | Both the colon (B) and the semicolon (C, the key) correctly join the two clauses. The solvers split B/C. A teacher should replace B or accept it. |

### Yellow questions worth a teacher's eye (substantive, not cosmetic)

- **Math 2**: the text says "frequency table" but the image is a bar-chart screenshot with charting-tool UI chrome. The proposed fix is a real table.
- **Math 38**: every choice is missing its left side ("= 29(d/150)" instead of "c = …").
- **Math 43, 45**: the Roman numerals in the choices are OCR garbage ("lI only", "| and ||").
- **Math 9**: the function is defined only in a cropped image with a stray comma.
- **Math 42**: the question image is a re-typed chat screenshot with a "Question:" heading.
- **R&W 34**: the stem asks about "the underlined claim", but the passage has a blank and no underline (two item formats were mixed).
- **R&W 36**: the passage interprets the graph and gives the answer away, the graph title is cropped, and choice A mentions "Form 990", which appears nowhere else.
- **R&W 52**: the notes lack the standard "While researching a topic…" lead-in.

Breakdown of the 47 yellows:

- 20 have cosmetic issues only: typos, a stray "?", dash characters, "Question N" headings on explanations, garbled numerals.
- 17 have only explanation problems, possibly with cosmetic ones too; a drafted explanation is attached.
- 5 have no issue and are yellow only because a solver was below high confidence.
- 5 have content issues in the question itself.

See §7 on separating cosmetic issues from content issues.

## 2. Blind solves: agreement and noise

Two independent solvers per question saw only the transcribed question and its figures, never the key or the explanation. Solver 1 was Opus 5.5 and solver 2 was Sonnet 5.5, run per module in batches of 22 or 27 questions.

- **The two solvers disagreed on 3 of 98 questions (3.1%)**, all in R&W: 39, 44 and 45. Two of the three are genuinely flawed items (39, 44). On 45, Sonnet chose C with *high* confidence and was wrong.
- **At least one solver was below high confidence on 16 of 98 questions** (Math 4, R&W 12). Sonnet lowers its confidence more readily, and that tracks real problems fairly well: Math 13 and 45, and R&W 5, 39 and 44.
- **The solvers disagreed with the bank key 7 times across 5 questions.** Both disagreed on Math 40 and R&W 5 (the two key_wrong items). One disagreed on each of R&W 39 and 44 (ambiguous) and R&W 45 (a Sonnet error).
- **Math was clean.** Every Math answer from both solvers matched the key, except Math 40, where both solvers were right and the key was wrong.
- **Sonnet misread Math 45** (it treated statement I as giving the angles of both triangles), and Opus flagged the same wording as ambiguous. Using two different models paid off: their errors did not coincide.

## 3. Transcription

- **Question and choice images:** 38 are referenced (34 Math, of which 12 are choice images, and 4 R&W). 34 became text or LaTeX: 31 Math formula and text screenshots, including all 12 choice images, and 3 R&W tables. 4 stay as figures: a Math line graph (csv 1), a Math bar chart (2), a Math dot plot (32) and an R&W bar chart (36).
- **Explanation images:** all 43 Math explanation images were transcribed to markup by a separate OCR pass. 11 of those explanations were later replaced by drafts (§4). The R&W bank has text explanations and no explanation images.
- **Transcription confidence:** high on 96 questions, medium on 2 (Math 37: "−39ˣ" written with a Unicode superscript is ambiguous; R&W 34: mixed stem format).
- **Hard cases and why:**
  - Math 5: the fraction is 1/9 in a 563-px screenshot and reads as 1/3 without upscaling. Small text images should always be upscaled 2–3× before reading.
  - Math 13: the CSV text columns hold only choices b and c. The real choices exist only in the images, and two of the images are identical.
  - Math csv 22, 23, 30, 31, 42, 43 and 45: both the CSV passage and question columns are empty, so the whole question exists only as an image. Math 5, 9, 18 and 27 keep their key equation only in an image.
  - The explanation screenshots are ChatGPT dark-mode captures about 380 px wide (Math 13 and 42–45). OCR legibility was medium, and several are cropped (Math 26, 27, 29, 33, 36, 37 and 41 start or end mid-solution).
  - R&W 36: the chart is a browser screenshot with its title cut off.
  - The R&W text uses LaTeX hacks (`\(\underline{…}\)`, `\(\textit{…}\)`, `\(\hspace{1em}\)`) that were converted mechanically to `<u>`, `*…*` and lists. Blank lengths were normalized to `______`.
- **R2 keys:** every one of the 81 referenced objects exists under a **`media/` prefix**. 57 of the CSV keys return 404 without it, and the other 24 exist in both places with identical ETags. The `figures[].key` values in `questions.jsonl` keep the CSV form (without `media/`), as the bank stores it. The app's storage prefix must be applied when rendering.
- **Math layout:** for Math, `passage` is always null and the whole question (setup, display equations, figure, question) is in `stem` in reading order. The CSV's passage/question split for Math is arbitrary: it often puts the question in `passage` or leaves both columns empty.

## 4. Explanations

| | Math (44) | R&W (54) |
|---|---:|---:|
| Present in bank | 43 (all as images) | 53 (text) |
| Missing | 1 (csv 14) | 1 (csv 54) |
| Usable as is | 24 | 39 |
| Usable, minor issue | 9 ("Question N" heading off by one, notation slip, cropped last line) | 0 |
| Wrong / incomplete | 6 (17, 32, 37, 40, 44, 45) | 14 (5, 16, 17, 34, 36, 38, 39, 40, 41, 42, 44, 45, 46, 48) |
| Explains a different version of the question | 4 (13, 18, 42, 43) | 0 |
| **Drafted replacement** (`explanation_source = "drafted"`) | **11** | **15** |

- The Math explanations are screenshots of ChatGPT conversations. Four of them explain a different version of the question: other choices (13, 42), a different equation (18, 44) or different functions entirely (43). The bank's questions were evidently edited after their explanations were generated.
- The R&W explanations are text and mostly choose the right letter. Fourteen give a wrong reason (for example "tense" instead of subject–verb agreement in 41, or "emphasis" instead of a dangling modifier in 42), or argue for the wrong key (5).
- The explanation checker (Sonnet) made one bad call. It decided the R&W 45 key itself was wrong, which I overruled after checking the grammar (see the notes in the record). Checker output on red or contested items needs a second look.

## 5. Tags

Every record has a College Board domain, a skill name and an estimated difficulty (Math: 18 easy, 17 medium, 9 hard; R&W: 16 easy, 24 medium, 14 hard). The bank's `domain_id` for Math maps to 6 = Algebra, 7 = Advanced Math, 8 = Problem-Solving & Data Analysis, 9 = Geometry & Trigonometry. My tags differ from the bank on 4 Math items: 13 and 22 (Advanced Math, not Algebra or PSDA), 35 (Advanced Math, not Geometry) and 41 (Geometry: circle equation, not Advanced Math).

## 6. Cost and time

The pilot ran inside Claude Code (an orchestrator plus 13 subagents), so the figures below are **API-equivalent** costs at list prices: Opus 5.5 $4 / $20 per M tokens in / out and Sonnet 5.5 $2 / $10, cache reads $0.20 for both. Cache writes are assumed at 1.25× input. Input tokens come from the session logs. The logs did not record subagent output tokens reliably, so subagent output is estimated from the text written, giving a low–high range.

| Step | Model | Input tokens (of which cache reads) | Output tokens | Cost |
|---|---|---:|---:|---:|
| Orchestrator: data prep, R2, transcription of 98 questions, review decisions, drafting, report, preview | Opus 5.5 | 13.1 M (12.8 M) | ~98 k | ~$5.9 |
| Explanation OCR, 43 images (2 agents) | Sonnet 5.5 | 1.55 M (1.38 M) | 14–43 k | $0.86–1.14 |
| Blind solves, Opus (4 agents) | Opus 5.5 | 0.80 M (0.67 M) | 6–19 k | $0.89–1.14 |
| Blind solves, Sonnet (4 agents) | Sonnet 5.5 | 0.99 M (0.90 M) | 6–17 k | $0.47–0.57 |
| R&W explanation check (1 agent) | Sonnet 5.5 | 0.30 M (0.24 M) | 3–10 k | $0.24–0.31 |
| **Total** | | **≈16.7 M (16.0 M cached)** | **≈130–190 k** | **≈ $8.4–9.1** (≈ $10 including this write-up) |

- **Time:** about 17 minutes of wall-clock time for the whole pipeline (22:58–23:15 UTC), plus about 10 minutes for the report and preview. Subagents ran in parallel, about 9 subagent-minutes in total.
- **Cost per question:** about **$0.09–0.10**.
- **Extrapolating the same method to the whole bank** (about 2,870 Math + 3,507 R&W = 6,377 questions, 64 tests) gives about **$600–650** and roughly 20–30 h of sequential run time, parallelizable by test. However, 95% of the input tokens here are Claude Code harness overhead: every agent call re-reads a large system prompt and context. The real per-question payload is a few thousand tokens.
- **A direct-API pipeline is the realistic budget.** One call per step per question, with structured outputs and prompt caching. Estimated per question:
  - transcription: Opus with images, about 3 k in / 0.8 k out
  - two solves: Opus + Sonnet, about 1.5 k in / 1.5 k out each, thinking included
  - explanation OCR or check: Sonnet, about 2 k in / 0.8 k out
  - adjudication: Opus, about 3 k in / 0.6 k out

  That comes to about **$0.12 per question, or ≈ $770 for the bank at list price and ≈ $390 with the Batch API (50% off)**. The figures are estimates from the measured payload sizes, not a measured run. Running the cheap steps on Haiku 5.5 would lower them further, but that is untested here.
- **Human time is the real cost.** At this pilot's rates, the whole bank would need teacher review of about 6% red items (about 400 questions) and about 5% yellows with content issues (about 300). On top of that come about 27% drafted explanations (about 1,700) to sample-check, plus cosmetic fixes that can be accepted in bulk.

## 7. What to change before running all 64 tests

**Fix first (data and plumbing)**
1. Resolve R2 keys with the `media/` prefix, or fix the bank's keys. Otherwise 70% of images 404.
2. Upscale every image narrower than about 800 px by 2–3× before any model reads it (Math 5 shows why).

**Pipeline structure**
3. Make transcription its own per-question model call (Opus with vision): CSV row plus images in, the content-format record out, with an explicit rule that image text wins over CSV text. In the pilot the orchestrator transcribed all 98 questions in one growing context, which does not scale to 6,377.
4. Run the blind solves as plain API calls with no file access. Here the solver subagents had filesystem access and were only *instructed* not to open the CSV. Blindness could not be enforced, though nothing suggests it was broken.
5. Keep two different models for the solves (Opus + Sonnet). Their errors did not overlap. Add a third, adjudicating solve (Opus, higher effort) only when the two disagree or either is below high confidence (16% of questions here).
6. Keep the explanation check. 26 explanations (27%) had to be replaced, so much of this pass's value came from it. For Math, consider regenerating explanations from the corrected question rather than OCR-ing the ChatGPT screenshots: about a quarter of them are wrong or written for another version of the question.
7. Use the Batch API for everything except adjudication.

**Output schema and risk rules**
8. Give each issue a `severity` (cosmetic | content | blocking) and a `source` (question | explanation | figure). Make risk follow severity: cosmetic-only issues go to a "green-with-edits" bucket instead of yellow. Here 37 of the 47 yellows are cosmetic-only or explanation-only, which buries the 5 real content problems.
9. Store `proposed_fix` as a field-level patch, as now, but also record which issues it resolves, so a teacher can accept fixes one click at a time.
10. Record the solver model in each `blind_solves` entry (already done here as `solver`) and keep the reasoning. The reasoning makes reds quick to adjudicate.

**Needs a human every time**
- Every red item and every `proposed_key`. Key changes must be signed off by a teacher before they reach students.
- Ambiguous items: the fix is usually an edit to a choice, which is a content decision (for example R&W 44 B, Math 13's missing choice, Math 45's statement I).
- Spot-check about 10% of drafted explanations and every explanation on a red item.
- Figures: watermarked or cropped screenshots (Math 1, 32, R&W 36) need redrawing. That is a design task, not a review task.
- Final approval before anything is written back to the database.
