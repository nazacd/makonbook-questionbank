# Running the AI review of a practice test

The review prepares one SAT MAKON practice test (for example `DAY2`: 44 Math + 54 Reading and
Writing questions) for the teachers' review queue.

| Step | Who | What it does |
|---|---|---|
| Transcribe | Sonnet subagents | Copy each question into the text format, turning images into text and LaTeX |
| Solve | Opus and Sonnet subagents | Two blind solves, without the key |
| Explain | Sonnet subagents | Check the bank's explanation, write new ones, tag the question |
| Adjudicate | Opus subagents | Decide only the questions the script flags |
| Fix | Opus subagents | Write a corrected version of every question that isn't green |
| Everything else | `tools/review.py` | Picks rows, downloads images, compares answers, merges, checks, writes the report and preview |

You, the main session, are the coordinator.
- You run `tools/review.py`, launch subagents, and commit.
- You never read the question files, images, inputs or outputs yourself, and you never solve,
  transcribe or edit them. That keeps this session small. Everything you need is in the
  script's printout.
- If a step looks wrong, re-run its batch. Never patch an output by hand.

## Before you start

- Get the latest tools first: `git pull origin main`. Start a new session for each test, or
  pull again before the next one.
- Run this main session on **Sonnet** (choose it in the model menu when starting the session). It only coordinates; Opus does its
  work as a subagent. On DAY2 an Opus main session was about 40% of the whole run's cost.
- Work from the repository root. Run `pip install -q boto3 pillow resvg-py` if they're missing.
- The two CSV exports (Math and English) are attached to the first message. Find their paths.
- R2 credentials are in the environment (`R2_*`). R2 is **read only**. Never print the
  credentials or put them in a file.
- Don't touch any database. Don't change the script or the prompts. If something in them
  blocks you, stop and say what.

## For each test T

Do the tests one after another: finish and commit one before starting the next.

### 1. Prepare

```
python3 tools/review.py prep T --math <math csv> --english <english csv>
```

The command prints the transcription batches, each as `step model batch n input -> output`.

### 2. Transcribe

Launch one subagent per batch, all in one message. Use the model the table names and this
prompt:

> Read tools/prompts/transcribe.md and follow it exactly. Batch: `<batch>`. Input:
> `<input path>`. Output: `<output path>`.

### 3. Solve and explain

When all transcription agents are done, run:

```
python3 tools/review.py stage T solve
python3 tools/review.py stage T explain
```

Then launch all the batches both commands print, in one message. That's solve_a (opus),
solve_b (sonnet) and explain (sonnet), 30 agents for a full test. Use these prompts:

- solve_a and solve_b: `Read tools/prompts/solve.md and follow it exactly. Batch: <batch>.
  Input: <input path>. Output: <output path>.` solve_a and solve_b read the same input and
  write different outputs.
- explain: the same, with `tools/prompts/explain.md`.

### 4. Adjudicate

```
python3 tools/review.py stage T adjudicate
```

The command prints how many questions are flagged and why. Launch its batches (opus) with
`tools/prompts/adjudicate.md`, using the same prompt shape.

### 5. Finish

1. Log the token counts. Each finished subagent reports `total_tokens`. After each step, log
   them in one command:

   ```
   python3 tools/review.py log-usage T transcribe/math-m1-a=81234 transcribe/math-m1-b=79012 ...
   ```

2. Write `work/T/notes.md`: at most 10 lines on anything unusual. That covers re-runs, failed
   agents, R2 objects that were missing, and anything a teacher should know. Leave it empty
   if nothing happened.
3. Run:

   ```
   python3 tools/review.py finish T
   ```

   This writes `T/questions.jsonl`, `T/report.md` and `T/preview.html` and checks them.
4. Commit only the `T/` folder, with the message `Review T`, and push.

### 6. Fix

Every question that isn't green gets a corrected version for teachers to approve or deny.

```
python3 tools/review.py fix T
```

Launch the batches it prints (opus), all in one message, with this prompt:

> Read tools/prompts/fix.md and follow it exactly. Batch: `<batch>`. Input: `<input path>`.
> Output: `<output path>`.

Log their tokens (`log-usage T fix/fix-1=...`), then run:

```
python3 tools/review.py fix-finish T
```

It checks every fix, draws the redrawn figures into `figures/`, and adds each fix to
`T/questions.jsonl`. If it lists batches to re-run, re-run them as in "When something fails",
then run `fix-finish` again. Commit `T/` and `figures/` with the message `Fix T`, and push.

Reply with the summary lines `finish` and `fix-finish` printed.

## Fixing a test reviewed before the fix step existed

Run step 6 alone for it: `fix T`, the agents, `fix-finish T`, commit `Fix T`. Nothing else
changes. The tests are independent; do them one after another.

## When something fails

- **`stage` refuses because an output is missing or invalid.** It lists the batches to re-run,
  each with a file holding its full error list. Re-run each listed batch: launch a new agent
  with the same prompt, plus `Your previous output failed the check. Fix every error listed in
  <error file>, keeping everything else.` Then run the command again.
- **`finish` reports check errors.** It names the batch to re-run for each one. Re-run them
  the same way, then run `finish` again.
- **Retries.** At most 2 re-runs per batch. If a batch still fails, write it in `notes.md`,
  stop, and report. Don't commit a test that failed its check.
- **Progress.** `python3 tools/review.py status T` shows what is done. Use it if you lose
  track.

## Rules the script enforces (for reference)

- **Solvers are blind.** Their input has only the transcribed question and its figures, never
  the key or the explanation.
- **Math explanations are always rewritten** (the bank's are often screenshots of older
  versions of the question). Reading and Writing explanations are kept when they are usable.
- **Adjudication flags a question when:**
  - a solver disagrees with the key, is below high confidence, or the two solvers disagree;
  - the transcription is below high confidence;
  - any content or blocking issue was found;
  - the explanation checker doubts the key, or its explanation reaches another answer;
  - a Reading and Writing bank explanation is wrong or mismatched.
- **Risk:**
  - **red:** any verdict other than key_correct, a low-confidence transcription, or a blocking
    issue.
  - **yellow:** a solver that disagrees or isn't sure, a medium-confidence transcription, or a
    content issue.
  - **green:** everything else.
- **The bank key only changes on `key_wrong` with written proof.** Even then the question is
  red, so a teacher confirms it.
- **Fixes never replace the reviewed question.** They sit beside it (`fix` in each record), so
  teachers see the original and the fixed version side by side and approve or deny.
