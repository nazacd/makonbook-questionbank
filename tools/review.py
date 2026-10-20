#!/usr/bin/env python3
"""The mechanical half of the per-test AI review. tools/REVIEW.md has the procedure.

The models transcribe, solve, explain and adjudicate; this script does everything
else, so the session that runs the review never has to read the data itself:

  prep T --math CSV --english CSV   pick test T's rows, download its images from R2
                                    (read only), check the rows, stage transcription
  stage T solve|explain|adjudicate  check the previous step's output, write the next
                                    step's input batches
  status T                          what is done, what is missing or invalid
  log-usage T STEP/BATCH=TOKENS ... record subagents' token counts (for the report)
  finish T                          merge into T/questions.jsonl, write T/report.md
                                    and T/preview.html, then run check
  check PATH|T                      validate a questions.jsonl (exit 1 on errors)
  fix T                             after finish: stage the fix pass, a corrected version of
                                    every question that isn't green (downloads its images)
  fix-finish T                      check the fixes, draw their figures (figures/), add them
                                    to T/questions.jsonl as each record's "fix"
  add-images PATH... --math CSV --english CSV
                                    add the bank's original screenshots (R2 keys) to records
                                    reviewed before finish did it (source.images)
  add-original PATH... --math CSV --english CSV
                                    write T/original.jsonl, the bank's own text of each question
                                    (finish writes it for new tests), for the teachers' comparison

Work files live in work/T/ (git-ignored); the results in T/.
Needs Python 3.10+, Pillow and boto3 (for prep).
"""

from __future__ import annotations

import argparse
import base64
import csv
import io
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Which model does each step. The session passes these to its subagents.
MODELS = {
    "transcribe": "sonnet",
    "solve_a": "opus",
    "solve_b": "sonnet",
    "explain": "sonnet",
    "adjudicate": "opus",
    "fix": "opus",
}
STEPS = list(MODELS)
INPUT_OF = {"transcribe": "transcribe", "solve_a": "solve", "solve_b": "solve", "explain": "explain", "adjudicate": "adjudicate",
            "fix": "fix"}
BATCH_SIZE = {"math": 11, "english": 9}
ADJ_BATCH = 6
FIX_BATCH = 5
MIN_WIDTH = 800  # narrower images are upscaled before a model reads them

# API list prices per million tokens (input, output), for the report's estimate.
PRICES = {"opus": (4.0, 20.0), "sonnet": (2.0, 10.0), "haiku": (0.10, 0.50)}

CONFIDENCE = ("high", "medium", "low")
VERDICTS = ("key_correct", "key_wrong", "ambiguous", "unsolvable", "broken")
ISSUE_KINDS = (
    "wrong_key", "missing_key", "typo", "grammar", "missing_choice", "duplicate_choice",
    "choice_formatting", "unreadable_image", "missing_image", "image_text_mismatch",
    "ambiguous", "missing_info", "off_format", "other",
)
SEVERITIES = ("cosmetic", "content", "blocking")
ISSUE_SOURCES = ("question", "figure")
FIGURE_KINDS = ("graph", "chart", "geometry", "scatterplot", "table_image", "map", "other")
BANK_STATUS = ("usable", "minor_issue", "wrong", "mismatch", "missing")
DIFFICULTY = ("easy", "medium", "hard")
LETTERS = ("A", "B", "C", "D")

TAXONOMY = {
    "english": {
        "Information and Ideas": ["Central Ideas and Details", "Inferences", "Command of Evidence (Textual)",
                                  "Command of Evidence (Quantitative)"],
        "Craft and Structure": ["Words in Context", "Text Structure and Purpose", "Cross-Text Connections"],
        "Expression of Ideas": ["Rhetorical Synthesis", "Transitions"],
        "Standard English Conventions": ["Boundaries", "Form, Structure, and Sense"],
    },
    "math": {
        "Algebra": ["Linear equations in one variable", "Linear functions", "Linear equations in two variables",
                    "Systems of two linear equations in two variables", "Linear inequalities in one or two variables"],
        "Advanced Math": ["Nonlinear functions",
                          "Nonlinear equations in one variable and systems of equations in two variables",
                          "Equivalent expressions"],
        "Problem-Solving and Data Analysis": [
            "Ratios, rates, proportional relationships, and units", "Percentages",
            "One-variable data: distributions and measures of center and spread",
            "Two-variable data: models and scatterplots", "Probability and conditional probability",
            "Inference from sample statistics and margin of error",
            "Evaluating statistical claims: observational studies and experiments"],
        "Geometry and Trigonometry": ["Area and volume", "Lines, angles, and triangles",
                                      "Right triangles and trigonometry", "Circles"],
    },
}
# The bank's ids, as far as the DAY1 pilot could tell. Hints only: the explain step decides.
DOMAIN_HINT = {
    "english": {"2": "Craft and Structure", "3": "Information and Ideas", "4": "Standard English Conventions",
                "5": "Expression of Ideas"},
    "math": {"6": "Algebra", "7": "Advanced Math", "8": "Problem-Solving and Data Analysis",
             "9": "Geometry and Trigonometry"},
}
SKILL_HINT = {
    "english": {"3": "Words in Context", "4": "Text Structure and Purpose", "5": "Cross-Text Connections",
                "6": "Central Ideas and Details", "7": "Command of Evidence", "8": "Inferences", "9": "Boundaries",
                "10": "Form, Structure, and Sense", "11": "Rhetorical Synthesis", "12": "Transitions"},
    "math": {},
}


class Fail(Exception):
    pass


# ---------------------------------------------------------------- helpers

def folder(test: str) -> str:
    return re.sub(r"\s+", "", test)


def work(test: str) -> Path:
    return ROOT / "work" / folder(test)


def out_dir(test: str) -> Path:
    return ROOT / folder(test)


def read_json(p: Path):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def write_json(p: Path, data) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
        f.write("\n")


def val(row: dict, k: str) -> str:
    v = (row.get(k) or "").strip()
    return "" if v == "NULL" else v


def truthy(v: str) -> bool:
    return v.strip().lower() in ("true", "t", "1", "yes")


def issue(kind, severity, source, detail, by="script"):
    return {"kind": kind, "severity": severity, "source": source, "detail": detail, "by": by}


def manifest(test: str) -> dict:
    p = work(test) / "manifest.json"
    if not p.exists():
        raise Fail(f"no {p.relative_to(ROOT)}: run prep first")
    return read_json(p)


def source(test: str, qid: str) -> dict:
    return read_json(work(test) / "src" / f"{qid}.json")


# ---------------------------------------------------------------- numbers (grid-in)

def parse_num(s) -> Fraction | None:
    if s is None:
        return None
    t = str(s).strip().replace(" ", "").replace("−", "-")
    if not re.fullmatch(r"-?(\d+(\.\d*)?|\.\d+)(/\d+(\.\d*)?)?", t):
        return None
    try:
        if "/" in t:
            a, b = t.split("/")
            return Fraction(a) / Fraction(b)
        return Fraction(t)
    except (ValueError, ZeroDivisionError):
        return None


def decimals(s: str) -> int:
    s = str(s).strip()
    return len(s.split(".")[1]) if "." in s and "/" not in s else 0


def same_number(a: str, b: str) -> bool:
    """Equal, or one is the other written as a decimal the grid would accept
    (rounded or cut off at 2+ decimal places, e.g. 2/3 and .6667 or .666)."""
    x, y = parse_num(a), parse_num(b)
    if x is None or y is None:
        return False
    if x == y:
        return True
    for approx, exact in ((a, y), (b, x)):
        d = decimals(approx)
        if d < 2:
            continue
        scaled = parse_num(approx) * 10**d
        e = abs(exact) * 10**d
        sign = -1 if exact < 0 else 1
        if scaled in (sign * math.floor(e), sign * math.floor(e + Fraction(1, 2))):  # cut off or rounded
            return True
    return False


def split_accepted(raw: str) -> list[str]:
    return [p.strip() for p in raw.split(",") if p.strip()]


def matches(answer, key, accepted, qtype) -> bool:
    if answer is None:
        return False
    if qtype == "mcq":
        return str(answer).strip().upper() == str(key or "").strip().upper()
    return any(same_number(str(answer), a) for a in (accepted or [key]))


# ---------------------------------------------------------------- content format

INLINE_OPEN, INLINE_CLOSE = r"\(", r"\)"
DISPLAY_OPEN, DISPLAY_CLOSE = r"\[", r"\]"
IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]*)\)")
TAG_RE = re.compile(r"</?([a-zA-Z][a-zA-Z0-9]*)[^>]*>")


def content_errors(text: str, where: str, figure_keys: set[str]) -> list[str]:
    errs = []
    if not isinstance(text, str):
        return [f"{where}: not a string"]
    stack = None
    i = 0
    while i < len(text) - 1:
        two = text[i:i + 2]
        if two in (INLINE_OPEN, DISPLAY_OPEN):
            if stack:
                errs.append(f"{where}: math opened inside math")
            stack = two
            i += 2
            continue
        if two in (INLINE_CLOSE, DISPLAY_CLOSE):
            want = INLINE_OPEN if two == INLINE_CLOSE else DISPLAY_OPEN
            if stack != want:
                errs.append(f"{where}: unbalanced {two}")
            stack = None
            i += 2
            continue
        i += 1
    if stack:
        errs.append(f"{where}: math not closed")
    for m in TAG_RE.finditer(text):
        if m.group(1).lower() != "u" or m.group(0) not in ("<u>", "</u>"):
            errs.append(f"{where}: HTML other than <u> ({m.group(0)[:20]})")
            break
    if text.count("<u>") != text.count("</u>"):
        errs.append(f"{where}: unbalanced <u>")
    if text.count("**") % 2:
        errs.append(f"{where}: unbalanced **")
    for m in IMG_RE.finditer(text):
        ref = m.group(2)
        if not ref.startswith("r2:") or ref[3:] not in figure_keys:
            errs.append(f"{where}: image {ref!r} is not one of the question's figures")
    if "�" in text:
        errs.append(f"{where}: contains � (broken character)")
    lines = text.split("\n")
    for j, line in enumerate(lines):
        # A table is 2+ lines starting with "|"; its second line separates the header.
        if (line.lstrip().startswith("|") and (j == 0 or not lines[j - 1].lstrip().startswith("|"))
                and j + 1 < len(lines) and lines[j + 1].lstrip().startswith("|")):
            if not re.fullmatch(r"\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*", lines[j + 1]):
                errs.append(f"{where}: table without a header separator row")
    return errs


def refs(text) -> set[str]:
    if not isinstance(text, str):
        return set()
    return {m.group(2)[3:] for m in IMG_RE.finditer(text) if m.group(2).startswith("r2:")}


def issue_errors(items, where, sources=ISSUE_SOURCES) -> list[str]:
    errs = []
    if not isinstance(items, list):
        return [f"{where}: issues is not a list"]
    for k, it in enumerate(items):
        w = f"{where} issue {k}"
        if not isinstance(it, dict):
            errs.append(f"{w}: not an object")
            continue
        if it.get("kind") not in ISSUE_KINDS:
            errs.append(f"{w}: kind {it.get('kind')!r}")
        if it.get("severity") not in SEVERITIES:
            errs.append(f"{w}: severity {it.get('severity')!r}")
        if it.get("source") not in sources:
            errs.append(f"{w}: source {it.get('source')!r}")
        if not str(it.get("detail") or "").strip():
            errs.append(f"{w}: no detail")
    return errs


# ---------------------------------------------------------------- prep

def r2_client():
    try:
        import boto3
        from botocore.config import Config
    except ImportError:
        raise Fail("pip install boto3")
    missing = [k for k in ("R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET_NAME", "R2_ENDPOINT_URL")
               if not os.environ.get(k)]
    if missing:
        raise Fail(f"missing env vars: {', '.join(missing)}")
    return boto3.client(
        "s3",
        endpoint_url=os.environ["R2_ENDPOINT_URL"],
        aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"],
        region_name=os.environ.get("R2_REGION") or "auto",
        config=Config(retries={"max_attempts": 5}),
    ), os.environ["R2_BUCKET_NAME"]


def fetch_image(client, bucket, key: str, w: Path) -> dict:
    """Download one object (read only) and make the copy models read."""
    from PIL import Image

    name = re.sub(r"[^A-Za-z0-9._-]", "_", key)
    orig = w / "img" / "orig" / name
    model = w / "img" / (Path(name).stem + ".png")
    info = {"key": key, "orig": str(orig), "path": str(model)}
    if not orig.exists():
        data = None
        for k in (f"media/{key}", key):
            try:
                data = client.get_object(Bucket=bucket, Key=k)["Body"].read()
                info["r2_key"] = k
                break
            except Exception as e:  # noqa: BLE001 - only the error code is reported
                code = getattr(e, "response", {}).get("Error", {}).get("Code", type(e).__name__)
                info["error"] = str(code)
        if data is None:
            return info
        orig.parent.mkdir(parents=True, exist_ok=True)
        orig.write_bytes(data)
    info.pop("error", None)
    try:
        with Image.open(orig) as im:
            im.load()
            wd, ht = im.size
            info["width"], info["height"] = wd, ht
            factor = 1 if wd >= MIN_WIDTH else min(3, math.ceil(MIN_WIDTH / wd))
            info["upscaled"] = factor
            if not model.exists():
                im2 = im.convert("RGB") if im.mode not in ("RGB", "L") else im
                if factor > 1:
                    im2 = im2.resize((wd * factor, ht * factor), Image.LANCZOS)
                im2.save(model)
    except Exception as e:  # noqa: BLE001
        info["error"] = f"cannot open: {type(e).__name__}"
    return info


def load_rows(path: str, test: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if folder(r.get("test_id") or "") == folder(test)]


def cmd_prep(a) -> None:
    test = a.test
    w = work(test)
    client, bucket = r2_client()
    subjects = [("math", a.math), ("english", a.english)]
    questions, batches = [], {}
    test_ids = set()
    counts = Counter()
    for subject, path in subjects:
        if not path:
            continue
        rows = load_rows(path, test)
        if not rows:
            raise Fail(f"no {subject} rows with test_id {test!r} in {path}")
        rows.sort(key=lambda r: (val(r, "module"), int(val(r, "number") or 0), int(val(r, "id") or 0)))
        seen = Counter((val(r, "module"), val(r, "number")) for r in rows)
        by_module = defaultdict(list)
        for r in rows:
            test_ids.add(r["test_id"])
            module = val(r, "module")
            mnum = module.replace("module_", "m")
            number = int(val(r, "number") or 0)
            qid = f"{subject}-{mnum}-{number:02d}"
            if seen[(module, val(r, "number"))] > 1:
                qid += f"-{val(r, 'id')}"
            src = build_source(subject, r, qid, client, bucket, w)
            write_json(w / "src" / f"{qid}.json", src)
            by_module[mnum].append(qid)
            questions.append({k: src[k] for k in ("qid", "subject", "module", "number", "csv_id", "type")})
            counts[subject] += 1
            for f in src["source_flags"]:
                print(f"  {qid}: {f['severity']} {f['kind']}: {f['detail']}", flush=True)
        for mnum, qids in by_module.items():
            size = BATCH_SIZE[subject]
            n = math.ceil(len(qids) / size)
            per = math.ceil(len(qids) / n)
            for j in range(n):
                batches[f"{subject}-{mnum}-{'abcdefgh'[j]}"] = qids[j * per:(j + 1) * per]
    write_json(w / "manifest.json", {"test": folder(test), "test_ids": sorted(test_ids), "models": MODELS,
                                     "counts": dict(counts), "questions": questions, "batches": batches})
    stage_transcribe(test)
    flags = sum(len(source(test, q["qid"])["source_flags"]) for q in questions)
    print(f"\n{folder(test)}: {dict(counts)} questions, {len(batches)} batches, {flags} problems found in the rows.")
    print_batches(test, ["transcribe"])


def build_source(subject: str, r: dict, qid: str, client, bucket, w: Path) -> dict:
    flags = []
    answer = val(r, "answer")
    choices = {L: val(r, L.lower()) for L in LETTERS}
    images = {}
    keys = {"question": val(r, "image")}
    if subject == "math":
        keys.update({L: val(r, f"image_{L.lower()}") for L in LETTERS})
    for slot, key in keys.items():
        if key:
            info = fetch_image(client, bucket, key, w)
            images[slot] = info
            if "error" in info:
                flags.append(issue("missing_image", "blocking", "question" if slot == "question" else "figure",
                                   f"{slot} image {key} could not be read ({info['error']})"))
    explain_images = []
    if subject == "math" and val(r, "img_explain"):
        info = fetch_image(client, bucket, val(r, "img_explain"), w)
        explain_images.append(info)
    has_choice = {L: bool(choices[L] or L in images) for L in LETTERS}
    if re.fullmatch(r"[A-Da-d]", answer):
        qtype = "mcq"
    elif not answer:
        qtype = "mcq" if any(has_choice.values()) or subject == "english" else "grid_in"
    else:
        qtype = "grid_in"
    if subject == "english" and val(r, "response_type") not in ("", "multiple_choice"):
        flags.append(issue("off_format", "blocking", "question", f"response_type {val(r, 'response_type')}"))

    accepted = [] if qtype == "mcq" else split_accepted(answer)
    bank_key = answer.upper() if qtype == "mcq" else (accepted[0] if accepted else answer)
    if not answer:
        flags.append(issue("missing_key", "blocking", "question", "the bank has no answer"))
    elif qtype == "grid_in":
        bad = [x for x in accepted if parse_num(x) is None]
        if bad:
            flags.append(issue("wrong_key", "content", "question", f"answer {answer!r}: not a number: {bad}"))
        if any(has_choice.values()):
            flags.append(issue("off_format", "content", "question",
                               f"answer {answer!r} is not a letter, but the row has choices"))
    if qtype == "mcq":
        filled = [L for L in LETTERS if has_choice[L]]
        if filled and len(filled) < 4:
            flags.append(issue("missing_choice", "blocking", "question",
                               f"choices {', '.join(L for L in LETTERS if not has_choice[L])} are empty"))
        if not filled and "question" not in images:
            flags.append(issue("missing_choice", "blocking", "question", "no choices and no image"))
        norm = Counter(re.sub(r"\s+", " ", choices[L]).strip().lower() for L in LETTERS if choices[L])
        dup = [c for c, n in norm.items() if n > 1]
        if dup:
            flags.append(issue("duplicate_choice", "content", "question", f"identical choice text: {dup[0][:60]!r}"))
    if not val(r, "question") and not val(r, "passage") and "question" not in images:
        flags.append(issue("missing_info", "blocking", "question", "no question text and no image"))

    return {
        "qid": qid, "subject": subject, "module": val(r, "module"), "number": int(val(r, "number") or 0),
        "csv_id": int(val(r, "id") or 0), "test_id": r.get("test_id"), "type": qtype,
        "passage": val(r, "passage") or None, "question": val(r, "question"),
        "choices": choices if qtype == "mcq" else None,
        "images": images, "explanation_images": explain_images,
        "bank_key": bank_key, "bank_accepted": accepted, "bank_answer_raw": answer,
        "bank_explanation": val(r, "explained") or None,
        "domain_hint": DOMAIN_HINT[subject].get(val(r, "domain_id")),
        "skill_hint": SKILL_HINT[subject].get(val(r, "type_id")),
        "flags": {k: truthy(val(r, k)) for k in ("graph", "choice_graph", "written") if k in r},
        "source_flags": flags,
    }


# ---------------------------------------------------------------- step outputs

def batch_paths(test: str, step: str, batch: str) -> tuple[Path, Path]:
    w = work(test)
    return w / "in" / INPUT_OF[step] / f"{batch}.json", w / "out" / step / f"{batch}.json"


def step_batches(test: str, step: str) -> dict[str, list[str]]:
    if step == "fix":
        p = work(test) / "fix.json"
        return read_json(p)["batches"] if p.exists() else {}
    m = manifest(test)
    if step == "adjudicate":
        p = work(test) / "adjudicate.json"
        return read_json(p)["batches"] if p.exists() else {}
    return m["batches"]


def load_step(test: str, step: str) -> tuple[dict, list[str], list[str]]:
    """Returns ({qid: record}, errors, batches to re-run)."""
    recs, errs, rerun = {}, [], []
    for batch, qids in step_batches(test, step).items():
        _, out = batch_paths(test, step, batch)
        if not out.exists():
            errs.append(f"{step} {batch}: no output")
            rerun.append(batch)
            continue  # no error file: just run the batch
        try:
            data = read_json(out)
        except json.JSONDecodeError as e:
            data = f"{step} {batch}: not valid JSON ({e})"
        if not isinstance(data, list):
            msg = data if isinstance(data, str) else f"{step} {batch}: not a JSON array"
            errs.append(msg)
            rerun.append(batch)
            error_file(test, step, batch).parent.mkdir(parents=True, exist_ok=True)
            error_file(test, step, batch).write_text(msg + "\n", encoding="utf-8")
            continue
        got = {}
        bad = []
        for item in data:
            q = item.get("qid") if isinstance(item, dict) else None
            if q not in qids:
                bad.append(f"{step} {batch}: unexpected qid {q!r}")
                continue
            got[q] = item
            bad += [f"{step} {q}: {e}" for e in VALIDATORS[step](test, item)]
        missing = [q for q in qids if q not in got]
        if missing:
            bad.append(f"{step} {batch}: missing {', '.join(missing)}")
        ef = error_file(test, step, batch)
        if bad:
            errs += bad
            rerun.append(batch)
            ef.parent.mkdir(parents=True, exist_ok=True)
            ef.write_text("\n".join(bad) + "\n", encoding="utf-8")
        elif ef.exists():
            ef.unlink()
        recs.update(got)
    return recs, errs, rerun


def error_file(test: str, step: str, batch: str) -> Path:
    return work(test) / "errors" / step / f"{batch}.txt"


def v_transcribe(test, t) -> list[str]:
    src = source(test, t["qid"])
    errs = []
    keys = {i["key"] for i in src["images"].values() if "error" not in i}
    figs = t.get("figures")
    if not isinstance(figs, list):
        return ["figures is not a list"]
    fkeys = set()
    for f in figs:
        if not isinstance(f, dict) or f.get("key") not in keys:
            errs.append(f"figure {f!r:.80} is not one of the row's images")
            continue
        if f.get("kind") not in FIGURE_KINDS:
            errs.append(f"figure kind {f.get('kind')!r}")
        if not str(f.get("alt") or "").strip():
            errs.append("figure without alt text")
        fkeys.add(f["key"])
    if t.get("confidence") not in CONFIDENCE:
        errs.append(f"confidence {t.get('confidence')!r}")
    if not str(t.get("stem") or "").strip() and not any(
            i.get("kind") == "missing_info" and i.get("severity") == "blocking" for i in t.get("issues") or []):
        errs.append("empty stem without a blocking missing_info issue")
    texts = {"stem": t.get("stem")}
    if t.get("passage") is not None:
        texts["passage"] = t["passage"]
    ch = t.get("choices")
    if src["type"] == "mcq":
        if not isinstance(ch, dict) or set(ch) != set(LETTERS):
            errs.append("an mcq needs choices A, B, C and D")
        else:
            for L in LETTERS:
                texts[f"choice {L}"] = ch[L]
                if not str(ch[L] or "").strip() and not any(i.get("kind") == "missing_choice"
                                                            for i in t.get("issues") or []):
                    errs.append(f"choice {L} is empty with no missing_choice issue")
    elif ch is not None:
        errs.append("a grid-in has choices: null")
    used = set()
    for where, text in texts.items():
        errs += content_errors(text or "", where, fkeys)
        used |= refs(text)
    if fkeys - used:
        errs.append(f"figures not placed in the text: {sorted(fkeys - used)}")
    errs += issue_errors(t.get("issues", []), "transcription")
    return errs


def v_solve(test, s) -> list[str]:
    src = source(test, s["qid"])
    errs = []
    ans = s.get("answer")
    if src["type"] == "mcq":
        if ans not in LETTERS + ("none",):
            errs.append(f"answer {ans!r} (A-D or none)")
    elif ans != "none" and parse_num(ans) is None:
        errs.append(f"answer {ans!r} is not a number")
    if s.get("confidence") not in CONFIDENCE:
        errs.append(f"confidence {s.get('confidence')!r}")
    if not str(s.get("reasoning") or "").strip():
        errs.append("no reasoning")
    return errs


def v_explain(test, e) -> list[str]:
    src = source(test, e["qid"])
    errs = []
    if e.get("bank_status") not in BANK_STATUS:
        errs.append(f"bank_status {e.get('bank_status')!r}")
    if e.get("bank_status") in ("wrong", "mismatch") and not str(e.get("disputed_quote") or "").strip():
        errs.append("bank_status wrong/mismatch needs disputed_quote")
    if e.get("explanation_source") not in ("bank", "drafted"):
        errs.append(f"explanation_source {e.get('explanation_source')!r}")
    if src["subject"] == "math" and e.get("explanation_source") != "drafted":
        errs.append("math explanations are always drafted")
    if e.get("explanation_source") == "bank" and e.get("bank_status") not in ("usable", "minor_issue"):
        errs.append("a bank explanation that is wrong, mismatched or missing must be drafted")
    text = e.get("explanation")
    if not str(text or "").strip():
        errs.append("empty explanation")
    else:
        errs += content_errors(text, "explanation", set())
    if not str(e.get("answer_stated") or "").strip():
        errs.append("no answer_stated")
    dom, skill = e.get("domain"), e.get("skill")
    tax = TAXONOMY[src["subject"]]
    if dom not in tax:
        errs.append(f"domain {dom!r}")
    elif skill not in tax[dom]:
        errs.append(f"skill {skill!r} is not in {dom}")
    if e.get("difficulty") not in DIFFICULTY:
        errs.append(f"difficulty {e.get('difficulty')!r}")
    errs += issue_errors(e.get("issues", []), "explain")
    return errs


def v_adjudicate(test, d) -> list[str]:
    src = source(test, d["qid"])
    errs = []
    v = d.get("verdict")
    if v not in VERDICTS:
        errs.append(f"verdict {v!r}")
    pk = d.get("proposed_key")
    if v == "key_wrong":
        if src["type"] == "mcq" and (pk not in LETTERS or pk == src["bank_key"]):
            errs.append(f"key_wrong needs a different proposed_key A-D, got {pk!r}")
        if src["type"] == "grid_in" and parse_num(pk) is None:
            errs.append(f"key_wrong needs a numeric proposed_key, got {pk!r}")
        if not str(d.get("proof") or "").strip():
            errs.append("key_wrong needs proof")
    elif pk is not None and v == "key_correct":
        errs.append("key_correct with a proposed_key")
    acc = d.get("accepted")
    if acc is not None:
        if src["type"] != "grid_in" or not isinstance(acc, list) or not acc or any(parse_num(x) is None for x in acc):
            errs.append("accepted must be null, or a list of numbers for a grid-in")
    errs += issue_errors(d.get("issues", []), "adjudication")
    if d.get("explanation") is not None:
        errs += content_errors(d["explanation"], "explanation", set())
        if not str(d.get("answer_stated") or "").strip():
            errs.append("a replacement explanation needs answer_stated")
    fix = d.get("transcription_fix")
    if fix is not None:
        if not isinstance(fix, dict) or not fix or set(fix) - {"passage", "stem", "choices"}:
            errs.append("transcription_fix: an object with passage, stem and/or choices")
        else:
            if "choices" in fix and (src["type"] != "mcq" or not isinstance(fix["choices"], dict)
                                     or set(fix["choices"]) - set(LETTERS)):
                errs.append("transcription_fix.choices: an object with some of A-D")
            for k, v in fix.items():
                for t in (v.values() if isinstance(v, dict) else [v]):
                    errs += content_errors(t or "", f"transcription_fix.{k}", {i["key"] for i in src["images"].values()})
    if not str(d.get("reason") or "").strip():
        errs.append("no reason")
    return errs


VALIDATORS = {"transcribe": v_transcribe, "solve_a": v_solve, "solve_b": v_solve, "explain": v_explain,
              "adjudicate": v_adjudicate, "fix": lambda test, f: v_fix(f, fix_inputs(test)[f["qid"]])}


# ---------------------------------------------------------------- staging

def figure_paths(src: dict, figures: list[dict]) -> dict[str, str]:
    by_key = {i["key"]: i for i in src["images"].values()}
    return {f"r2:{f['key']}": by_key[f["key"]]["path"] for f in figures if f["key"] in by_key}


def stage_transcribe(test: str) -> None:
    for batch, qids in manifest(test)["batches"].items():
        items = []
        for q in qids:
            s = source(test, q)
            items.append({
                "qid": q, "subject": s["subject"], "type": s["type"], "passage": s["passage"],
                "question": s["question"], "choices": s["choices"],
                "images": {slot: {"r2_key": i["key"], "path": i["path"]} for slot, i in s["images"].items()
                           if "error" not in i},
                "bank_flags": s["flags"],
            })
        write_json(batch_paths(test, "transcribe", batch)[0], items)


def require(test: str, *steps: str) -> dict:
    got, errs, rerun = {}, [], defaultdict(list)
    for st in steps:
        recs, e, r = load_step(test, st)
        got[st] = recs
        errs += e
        if r:
            rerun[st] = r
    if errs:
        print("\n".join(errs[:40]))
        if len(errs) > 40:
            print(f"... {len(errs) - 40} more")
        print("\nRe-run these batches, then run this command again. Each batch's full error list is in")
        print("the file shown; add it to the re-run prompt:")
        for st, bs in rerun.items():
            for b in bs:
                ef = error_file(test, st, b)
                print(f"  {st} {b}" + (f": {ef.relative_to(ROOT)}" if ef.exists() else ": no output yet"))
        raise Fail("previous step incomplete")
    return got


def cmd_stage(a) -> None:
    test, step = a.test, a.step
    if step == "solve":
        t = require(test, "transcribe")["transcribe"]
        for batch, qids in manifest(test)["batches"].items():
            items = []
            for q in qids:
                s, tr = source(test, q), t[q]
                items.append({"qid": q, "type": s["type"], "passage": tr.get("passage"), "stem": tr["stem"],
                              "choices": tr.get("choices"), "figures": figure_paths(s, tr["figures"])})
            write_json(batch_paths(test, "solve_a", batch)[0], items)
        print_batches(test, ["solve_a", "solve_b"])
    elif step == "explain":
        t = require(test, "transcribe")["transcribe"]
        for batch, qids in manifest(test)["batches"].items():
            items = []
            for q in qids:
                s, tr = source(test, q), t[q]
                items.append({
                    "qid": q, "subject": s["subject"], "type": s["type"], "passage": tr.get("passage"),
                    "stem": tr["stem"], "choices": tr.get("choices"), "figures": figure_paths(s, tr["figures"]),
                    "bank_key": s["bank_key"], "bank_accepted": s["bank_accepted"],
                    "bank_explanation": s["bank_explanation"],
                    "explanation_images": [i["path"] for i in s["explanation_images"] if "error" not in i],
                    "policy": "draft" if s["subject"] == "math" else "keep_if_usable",
                    "domain_hint": s["domain_hint"], "skill_hint": s["skill_hint"],
                })
            write_json(batch_paths(test, "explain", batch)[0], items)
        print_batches(test, ["explain"])
    elif step == "adjudicate":
        got = require(test, "transcribe", "solve_a", "solve_b", "explain")
        queue = []
        for q in manifest(test)["questions"]:
            reasons = triage(source(test, q["qid"]), *(got[st][q["qid"]] for st in
                                                        ("transcribe", "solve_a", "solve_b", "explain")))
            if reasons:
                queue.append((q["qid"], reasons))
        batches = {}
        for j in range(0, len(queue), ADJ_BATCH):
            name = f"adj-{j // ADJ_BATCH + 1}"
            batches[name] = [q for q, _ in queue[j:j + ADJ_BATCH]]
            items = []
            for q, reasons in queue[j:j + ADJ_BATCH]:
                s = source(test, q)
                tr, sa, sb, ex = (got[st][q] for st in ("transcribe", "solve_a", "solve_b", "explain"))
                items.append({
                    "qid": q, "why": reasons, "type": s["type"],
                    "transcription": {k: tr.get(k) for k in ("passage", "stem", "choices", "figures", "confidence")},
                    "figures": figure_paths(s, tr["figures"]),
                    "original_images": {slot: i["path"] for slot, i in s["images"].items() if "error" not in i},
                    "original_csv": {"passage": s["passage"], "question": s["question"], "choices": s["choices"]},
                    "bank_key": s["bank_key"], "bank_accepted": s["bank_accepted"],
                    "solver_1": {k: sa[k] for k in ("answer", "confidence", "reasoning")},
                    "solver_2": {k: sb[k] for k in ("answer", "confidence", "reasoning")},
                    "explanation_check": {k: ex.get(k) for k in ("bank_status", "disputed_quote", "key_concern",
                                                                  "answer_stated", "explanation_source", "explanation")},
                    "bank_explanation": s["bank_explanation"],
                    "explanation_images": [i["path"] for i in s["explanation_images"] if "error" not in i],
                    "issues_so_far": collect_issues(s, tr, ex),
                })
            write_json(batch_paths(test, "adjudicate", name)[0], items)
        write_json(work(test) / "adjudicate.json", {"queue": dict(queue), "batches": batches})
        why = Counter(r.split(":")[0] for _, rs in queue for r in rs)
        print(f"{len(queue)} of {len(manifest(test)['questions'])} questions need adjudication.")
        for r, n in why.most_common():
            print(f"  {n:3}  {r}")
        if queue:
            print_batches(test, ["adjudicate"])
        else:
            print("Nothing to adjudicate: run finish.")


def collect_issues(src, tr, ex) -> list[dict]:
    out = list(src["source_flags"])
    out += [dict(i, by=MODELS["transcribe"]) for i in tr.get("issues") or []]
    out += [dict(i, by=MODELS["explain"]) for i in ex.get("issues") or []]
    return out


def triage(src, tr, sa, sb, ex) -> list[str]:
    """Why a question needs the adjudicator; empty when it doesn't."""
    why = []
    key, acc, qt = src["bank_key"], src["bank_accepted"], src["type"]
    for name, s in (("solver 1", sa), ("solver 2", sb)):
        if not matches(s["answer"], key, acc, qt):
            why.append(f"solver disagrees with key: {name} says {s['answer']}, key {key}")
        if s["confidence"] != "high":
            why.append(f"solver not sure: {name} {s['confidence']}")
    if qt == "mcq" and sa["answer"] != sb["answer"] or qt == "grid_in" and not same_number(sa["answer"], sb["answer"]):
        why.append("solvers disagree")
    if tr["confidence"] != "high":
        why.append(f"transcription {tr['confidence']}")
    for i in collect_issues(src, tr, ex):
        if i["severity"] != "cosmetic":
            why.append(f"{i['severity']} issue: {i['kind']}")
    if ex.get("key_concern"):
        why.append("explanation checker doubts the key")
    if not matches(ex.get("answer_stated"), key, acc, qt):
        why.append(f"explanation reaches another answer: {ex.get('answer_stated')}")
    if ex["bank_status"] in ("wrong", "mismatch") and src["subject"] == "english":
        why.append(f"bank explanation {ex['bank_status']}")
    return why


def print_batches(test: str, steps: list[str]) -> None:
    print(f"\n{'step':<11} {'model':<7} {'batch':<15} {'n':>3}  input -> output")
    for st in steps:
        for batch, qids in step_batches(test, st).items():
            i, o = batch_paths(test, st, batch)
            print(f"{st:<11} {MODELS[st]:<7} {batch:<15} {len(qids):>3}  {i.relative_to(ROOT)} -> {o.relative_to(ROOT)}")


# ---------------------------------------------------------------- status, usage

def cmd_status(a) -> None:
    test = a.test
    m = manifest(test)
    print(f"{m['test']}: {m['counts']}")
    for st in STEPS[:-1]:  # the fix pass has its own commands
        bs = step_batches(test, st)
        if not bs:
            print(f"  {st:<11} not staged")
            continue
        recs, errs, rerun = load_step(test, st)
        state = "done" if not errs else f"{len(bs) - len(rerun)}/{len(bs)} batches ok; re-run: {' '.join(rerun)}"
        print(f"  {st:<11} {len(recs):>3} questions  {state}")
        for e in errs[:5]:
            print(f"      {e}")
    if (out_dir(test) / "questions.jsonl").exists():
        print(f"  finished: {out_dir(test).relative_to(ROOT)}/questions.jsonl")


def cmd_log_usage(a) -> None:
    rows = []
    for e in a.entries:
        m = re.fullmatch(r"(\w+)/([\w-]+)=(\d+)", e.replace(",", "").replace("_tokens", ""))
        if not m or m.group(1) not in STEPS:
            raise Fail(f"{e!r}: write STEP/BATCH=TOKENS, e.g. solve_a/math-m1-a=81234")
        rows.append({"step": m.group(1), "model": MODELS[m.group(1)], "batch": m.group(2), "tokens": int(m.group(3))})
    p = work(a.test) / "usage.jsonl"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.writelines(json.dumps(r) + "\n" for r in rows)
    print(f"logged {len(rows)}")


# ---------------------------------------------------------------- finish

def risk_of(rec: dict) -> tuple[str, list[str]]:
    red, yellow = [], []
    if rec["verdict"] != "key_correct":
        red.append(f"verdict {rec['verdict']}")
    if rec["transcription"]["confidence"] == "low":
        red.append("transcription low")
    for i in rec["issues"]:
        if i["severity"] == "blocking":
            red.append(f"blocking: {i['kind']}")
        elif i["severity"] == "content":
            yellow.append(f"content: {i['kind']}")
    if rec["transcription"]["confidence"] == "medium":
        yellow.append("transcription medium")
    solves = rec["blind_solves"]
    for s in solves:
        if not s["matches_key"]:
            yellow.append(f"{s['solver']} disagrees with the key")
        if s["confidence"] != "high":
            yellow.append(f"{s['solver']} {s['confidence']}")
    if red:
        return "red", red
    if yellow:
        return "yellow", yellow
    return "green", []


def build_record(test, q, tr, sa, sb, ex, adj) -> dict:
    s = source(test, q)
    issues = adj["issues"] if adj else collect_issues(s, tr, ex)
    issues = [dict(i, by=i.get("by") or MODELS["adjudicate"]) for i in issues]
    verdict = adj["verdict"] if adj else "key_correct"
    key, accepted = s["bank_key"], s["bank_accepted"]
    if adj and adj.get("accepted"):
        accepted = adj["accepted"]
    if verdict == "key_wrong":
        key = adj["proposed_key"]
        if s["type"] == "grid_in" and not adj.get("accepted"):
            accepted = [key]
    explanation, ex_src, answer_stated = ex["explanation"], ex["explanation_source"], ex["answer_stated"]
    if adj and adj.get("explanation"):
        explanation, ex_src, answer_stated = adj["explanation"], "drafted", adj["answer_stated"]
    passage, stem, choices = tr.get("passage"), tr["stem"], tr.get("choices")
    fix = (adj or {}).get("transcription_fix") or {}
    if "passage" in fix:
        passage = fix["passage"]
    if "stem" in fix:
        stem = fix["stem"]
    if "choices" in fix:
        choices = {**choices, **fix["choices"]}
    rec = {
        "qid": q,
        "source": {"subject": s["subject"], "csv_id": s["csv_id"], "test_id": s["test_id"], "module": s["module"],
                   "number": s["number"], "images": {slot: i["key"] for slot, i in s["images"].items()}},
        "type": s["type"],
        "passage": passage, "stem": stem, "choices": choices,
        "figures": [{k: f[k] for k in ("key", "kind", "alt")} for f in tr["figures"]],
        "transcription": {"confidence": tr["confidence"], "by": MODELS["transcribe"], "notes": tr.get("notes") or "",
                          "fixed_by_adjudicator": sorted(fix)},
        "bank_key": s["bank_key"], "bank_accepted": s["bank_accepted"],
        "key": key, "accepted": accepted,
        "blind_solves": [
            {"solver": MODELS[st], "answer": x["answer"], "confidence": x["confidence"], "reasoning": x["reasoning"],
             "matches_key": matches(x["answer"], key, accepted, s["type"]),
             "matches_bank_key": matches(x["answer"], s["bank_key"], s["bank_accepted"], s["type"])}
            for st, x in (("solve_a", sa), ("solve_b", sb))],
        "verdict": verdict,
        "proposed_key": adj.get("proposed_key") if adj else None,
        "adjudication": {"by": MODELS["adjudicate"], "why": read_json(work(test) / "adjudicate.json")["queue"][q],
                         "reason": adj["reason"], "proof": adj.get("proof")} if adj else None,
        "issues": issues,
        "proposed_fix": adj.get("proposed_fix") if adj else None,
        "explanation": {"text": explanation, "source": ex_src, "answer_stated": answer_stated,
                        "bank_status": ex["bank_status"], "disputed_quote": ex.get("disputed_quote"),
                        "by": MODELS["adjudicate"] if adj and adj.get("explanation") else MODELS["explain"]},
        "tags": {"domain": ex["domain"], "skill": ex["skill"], "difficulty": ex["difficulty"],
                 "difficulty_source": "estimate"},
    }
    rec["risk"], rec["risk_reasons"] = risk_of(rec)
    return rec


def cmd_finish(a) -> None:
    test = a.test
    if not (work(test) / "adjudicate.json").exists():
        raise Fail("run: stage adjudicate")
    got = require(test, "transcribe", "solve_a", "solve_b", "explain", "adjudicate")
    m = manifest(test)
    records = []
    for qq in m["questions"]:
        q = qq["qid"]
        records.append(build_record(test, q, *(got[st][q] for st in ("transcribe", "solve_a", "solve_b", "explain")),
                                    got["adjudicate"].get(q)))
    od = out_dir(test)
    od.mkdir(parents=True, exist_ok=True)
    with open(od / "questions.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    write_original(od, [{"qid": q["qid"], **original_of(source(test, q["qid"]))} for q in m["questions"]])
    (od / "report.md").write_text(report(test, m, records), encoding="utf-8")
    (od / "preview.html").write_text(preview(test, records), encoding="utf-8")
    errs = check_records(records, m)
    print(f"wrote {od.relative_to(ROOT)}/questions.jsonl, report.md, preview.html")
    print(summary_line(records))
    if errs:
        print("\n".join(errs))
        adj = read_json(work(test) / "adjudicate.json")["batches"]
        where = {q: ("adjudicate", b) for b, qs in adj.items() for q in qs}
        where.update({q: ("explain", b) for b, qs in m["batches"].items() for q in qs if q not in where})
        rerun = defaultdict(list)
        for e in errs:
            q = e.split(":")[0]
            if q in where:
                rerun[where[q]].append(e)
        if rerun:
            print("\nRe-run these batches with the errors added to the prompt, then finish again:")
            for (st, b), es in rerun.items():
                print(f"  {st} {b}: " + " | ".join(es))
        raise Fail(f"{len(errs)} check errors")
    print("check: ok")


def summary_line(records) -> str:
    c = Counter(r["risk"] for r in records)
    v = Counter(r["verdict"] for r in records)
    return (f"{len(records)} questions: green {c['green']}, yellow {c['yellow']}, red {c['red']} | "
            + ", ".join(f"{k} {n}" for k, n in v.most_common()))


def label(r) -> str:
    s = r["source"]
    return f"{'Math' if s['subject'] == 'math' else 'R&W'} M{s['module'][-1]} #{s['number']} (csv {s['csv_id']})"


def report(test, m, records) -> str:
    L = [f"# {m['test']} AI review", ""]
    L.append(f"Test ids {', '.join(m['test_ids'])}: {len(records)} questions. Models: "
             + ", ".join(f"{k} {v}" for k, v in MODELS.items()) + ".")
    L += ["", "## Counts", "", "| Subject | green | yellow | red | total |", "|---|---:|---:|---:|---:|"]
    for subj in ("english", "math"):
        rs = [r for r in records if r["source"]["subject"] == subj]
        if rs:
            c = Counter(r["risk"] for r in rs)
            L.append(f"| {'R&W' if subj == 'english' else 'Math'} | {c['green']} | {c['yellow']} | {c['red']} | {len(rs)} |")
    c = Counter(r["risk"] for r in records)
    L.append(f"| **Total** | **{c['green']}** | **{c['yellow']}** | **{c['red']}** | **{len(records)}** |")
    L += ["", "Verdicts: " + ", ".join(f"{k} {n}" for k, n in Counter(r["verdict"] for r in records).most_common())
          + f". Adjudicated: {sum(1 for r in records if r['adjudication'])}."]

    L += ["", "## Red: a teacher decides before publishing", ""]
    reds = [r for r in records if r["risk"] == "red"]
    for r in reds:
        why = r["adjudication"]["reason"] if r["adjudication"] else "; ".join(r["risk_reasons"])
        key = f" Key {r['bank_key']} → {r['proposed_key']}." if r["verdict"] == "key_wrong" else ""
        L.append(f"- **{label(r)}**: {r['verdict']}.{key} {why}")
    if not reds:
        L.append("None.")

    L += ["", "## Yellow", ""]
    yc = Counter(re.sub(r"^(opus|sonnet|haiku) ", "solver ", x) for r in records if r["risk"] == "yellow"
                 for x in r["risk_reasons"])
    for k, n in yc.most_common():
        L.append(f"- {k}: {n}")
    if not yc:
        L.append("None.")

    L += ["", "## Solvers", ""]
    for j, st in enumerate(("solve_a", "solve_b")):
        ss = [r["blind_solves"][j] for r in records]
        cc = Counter(s["confidence"] for s in ss)
        L.append(f"- {st} ({MODELS[st]}): disagrees with the bank key on {sum(not s['matches_bank_key'] for s in ss)}, "
                 f"with the final key on {sum(not s['matches_key'] for s in ss)}; confidence high {cc['high']}, "
                 f"medium {cc['medium']}, low {cc['low']}.")
    both = [label(r) for r in records if not any(s["matches_bank_key"] for s in r["blind_solves"])]
    L.append(f"- Both disagree with the bank key: {len(both)}" + (f" ({'; '.join(both)})" if both else "") + ".")
    dis = sum(1 for r in records if not (matches(r["blind_solves"][0]["answer"], r["blind_solves"][1]["answer"],
                                                 [r["blind_solves"][1]["answer"]], r["type"])))
    L.append(f"- The two solvers disagree with each other: {dis}.")

    L += ["", "## Transcription", ""]
    cc = Counter(r["transcription"]["confidence"] for r in records)
    L.append(f"- Confidence: high {cc['high']}, medium {cc['medium']}, low {cc['low']}.")
    imgs = sum(len(source(test, r["qid"])["images"]) for r in records)
    kept = Counter(f["kind"] for r in records for f in r["figures"])
    L.append(f"- Question and choice images: {imgs}; kept as figures {sum(kept.values())} "
             f"({', '.join(f'{k} {n}' for k, n in kept.most_common()) or 'none'}), the rest turned into text.")
    L.append(f"- Upscaled for the models: {sum(1 for r in records for i in source(test, r['qid'])['images'].values() if i.get('upscaled', 1) > 1)}.")

    L += ["", "## Explanations", ""]
    bs = Counter(r["explanation"]["bank_status"] for r in records)
    L.append("- Bank explanation: " + ", ".join(f"{k} {bs[k]}" for k in BANK_STATUS) + ".")
    L.append(f"- Final: drafted {sum(r['explanation']['source'] == 'drafted' for r in records)}, "
             f"kept from the bank {sum(r['explanation']['source'] == 'bank' for r in records)}.")

    L += ["", "## Usage", ""]
    up = work(test) / "usage.jsonl"
    if up.exists():
        rows = [json.loads(x) for x in up.read_text().splitlines() if x.strip()]
        L += ["| Step | Model | Agents | Tokens | Est. API cost |", "|---|---|---:|---:|---:|"]
        tot_t = tot_c = 0
        for st in STEPS:
            rs = [x for x in rows if x["step"] == st]
            if not rs:
                continue
            t = sum(x["tokens"] for x in rs)
            pi, po = PRICES.get(MODELS[st], (0, 0))
            cost = t * 0.9 / 1e6 * pi + t * 0.1 / 1e6 * po
            tot_t += t
            tot_c += cost
            L.append(f"| {st} | {MODELS[st]} | {len(rs)} | {t:,} | ${cost:.2f} |")
        L.append(f"| **Subagents** | | {len(rows)} | **{tot_t:,}** | **${tot_c:.2f}** |")
        L += ["", f"Per question ≈ {tot_t // max(1, len(records)):,} tokens, ≈ ${tot_c / max(1, len(records)):.3f} "
                  "at API list prices (90/10 input/output split assumed; the main session is not included)."]
    else:
        L.append("Not logged.")

    notes = work(test) / "notes.md"
    if notes.exists() and notes.read_text().strip():
        L += ["", "## Notes from the session", "", notes.read_text().strip()]
    return "\n".join(L) + "\n"


def thumb(path: str) -> str | None:
    from PIL import Image

    try:
        with Image.open(path) as im:
            im = im.convert("RGB")
            if im.width > 640:
                im = im.resize((640, round(im.height * 640 / im.width)), Image.LANCZOS)
            b = io.BytesIO()
            im.save(b, "JPEG", quality=62, optimize=True)
            return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()
    except Exception:  # noqa: BLE001
        return None


def preview(test, records) -> str:
    imgs = {}
    for r in records:
        for i in source(test, r["qid"])["images"].values():
            if "error" not in i and i["key"] not in imgs:
                imgs[i["key"]] = thumb(i["orig"])
    data = []
    for r in records:
        s = source(test, r["qid"])
        data.append({**{k: r[k] for k in ("qid", "type", "passage", "stem", "choices", "bank_key", "key", "verdict",
                                          "proposed_key", "issues", "risk", "risk_reasons", "blind_solves",
                                          "explanation", "tags", "adjudication", "proposed_fix")},
                     "label": label(r), "subject": r["source"]["subject"],
                     "originals": {slot: i["key"] for slot, i in s["images"].items() if "error" not in i},
                     "csv": {"passage": s["passage"], "question": s["question"], "choices": s["choices"]}})
    payload = json.dumps({"q": data, "img": imgs}, ensure_ascii=False).replace("</", "<\\/")
    return PREVIEW.replace("__TITLE__", f"{folder(test)} review").replace("__DATA__", payload)


PREVIEW = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"></script>
<style>
:root{--bg:#f6f6f8;--card:#fff;--ink:#16141d;--muted:#666;--line:#e3e3e8;--green:#1a7f37;--yellow:#9a6700;--red:#cf222e;--accent:#6d4ad6}
@media (prefers-color-scheme:dark){:root{--bg:#01000f;--card:#16141d;--ink:#ececf1;--muted:#a3a3b0;--line:#2a2733;--green:#3fb950;--yellow:#d29922;--red:#f85149;--accent:#8b5cf6}}
body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.5 system-ui,sans-serif}
header{position:sticky;top:0;background:var(--bg);border-bottom:1px solid var(--line);padding:10px 16px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;z-index:2}
header h1{font-size:17px;margin:0 12px 0 0}
button{font:inherit;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:3px 12px;cursor:pointer}
button.on{background:var(--accent);border-color:var(--accent);color:#fff}
main{max-width:1200px;margin:0 auto;padding:16px}
.q{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:0 0 16px;padding:14px 16px}
.head{display:flex;gap:10px;flex-wrap:wrap;align-items:baseline;margin-bottom:8px}
.head b{font-size:16px}.chip{border-radius:999px;padding:1px 9px;font-size:13px;color:#fff}
.green{background:var(--green)}.yellow{background:var(--yellow)}.red{background:var(--red)}
.muted{color:var(--muted);font-size:13px}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:16px}@media(max-width:800px){.cols{grid-template-columns:1fr}}
.content img{max-width:100%;border:1px solid var(--line);border-radius:6px}
.orig img{max-width:100%;border:1px solid var(--line);border-radius:6px;display:block;margin-bottom:6px}
.choice{display:flex;gap:8px;margin:4px 0;align-items:baseline}.choice p{margin:0}.choice .l{font-weight:600;min-width:1.4em}.choice.key .l{color:var(--green)}
table{border-collapse:collapse;margin:6px 0}td,th{border:1px solid var(--line);padding:3px 8px}
ul.issues{margin:6px 0;padding-left:20px}details{margin-top:8px}summary{cursor:pointer;color:var(--muted)}
pre{white-space:pre-wrap;font:13px/1.4 ui-monospace,monospace;background:var(--bg);padding:8px;border-radius:6px}
</style></head><body>
<header><h1>__TITLE__</h1><span id="f"></span><span class="muted" id="n"></span></header>
<main id="list"></main>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s??'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
function inline(s,br){
  const math=[];s=s.replace(/\\\([\s\S]*?\\\)|\\\[[\s\S]*?\\\]/g,m=>{math.push(m);return '\u0000'+(math.length-1)+'\u0000'});
  s=esc(s).replace(/&lt;u&gt;/g,'<u>').replace(/&lt;\/u&gt;/g,'</u>')
    .replace(/!\[([^\]]*)\]\(r2:([^)\s]*)\)/g,(m,a,k)=>D.img[k]?`<img alt="${a}" title="${a}" src="${D.img[k]}">`:`[figure: ${a}]`)
    .replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\*([^*\s][^*]*)\*/g,'<i>$1</i>');
  if(br)s=s.replace(/\n/g,'<br>');
  return s.replace(/\u0000(\d+)\u0000/g,(m,i)=>esc(math[+i]));
}
function md(s){
  if(s==null)return '';
  return String(s).split(/\n\s*\n/).map(b=>{
    const lines=b.split('\n');
    if(lines.every(l=>l.trim().startsWith('|'))){
      const rows=lines.filter(l=>!/^\s*\|?\s*:?-{2,}/.test(l)).map(l=>l.trim().replace(/^\||\|$/g,'').split('|'));
      return '<table>'+rows.map((r,i)=>'<tr>'+r.map(c=>i?`<td>${inline(c.trim())}</td>`:`<th>${inline(c.trim())}</th>`).join('')+'</tr>').join('')+'</table>';
    }
    if(lines.every(l=>l.startsWith('- ')))return '<ul>'+lines.map(l=>`<li>${inline(l.slice(2))}</li>`).join('')+'</ul>';
    return '<p>'+inline(b,true)+'</p>';
  }).join('');
}
function card(q){
  const ch=q.choices?Object.entries(q.choices).map(([l,t])=>`<div class="choice ${l===q.key?'key':''}"><span class="l">${l}</span><div>${md(t)}</div></div>`).join(''):`<p><b>Answer:</b> ${esc(q.key)}</p>`;
  const solves=q.blind_solves.map(s=>`${esc(s.solver)}: <b>${esc(s.answer)}</b> (${s.confidence})${s.matches_key?'':' ✗'}`).join(' · ');
  const issues=q.issues.length?'<ul class="issues">'+q.issues.map(i=>`<li><b>${i.severity}</b> ${i.kind} (${i.source}, ${esc(i.by)}): ${esc(i.detail)}</li>`).join('')+'</ul>':'';
  const orig=Object.entries(q.originals).map(([s,k])=>D.img[k]?`<div class="muted">${s}</div><img src="${D.img[k]}">`:'').join('');
  const csv=`<pre>${esc([q.csv.passage,q.csv.question,q.csv.choices&&Object.entries(q.csv.choices).map(([l,t])=>l+') '+t).join('\n')].filter(Boolean).join('\n\n'))}</pre>`;
  return `<section class="q" data-risk="${q.risk}" data-subject="${q.subject}">
  <div class="head"><b>${esc(q.label)}</b><span class="chip ${q.risk}">${q.risk}</span><span>${q.verdict}</span>
  <span class="muted">key ${esc(q.bank_key)}${q.proposed_key?` → <b>${esc(q.proposed_key)}</b>`:''} · ${solves} · ${esc(q.tags.domain)} / ${esc(q.tags.skill)} · ${q.tags.difficulty} (estimate)</span></div>
  ${q.risk_reasons.length?`<div class="muted">${esc(q.risk_reasons.join('; '))}</div>`:''}
  ${q.adjudication?`<div><b>Adjudication:</b> ${esc(q.adjudication.reason)}${q.adjudication.proof?`<br><span class="muted">${esc(q.adjudication.proof)}</span>`:''}</div>`:''}
  ${issues}
  ${q.proposed_fix?`<details><summary>Proposed fix</summary><pre>${esc(JSON.stringify(q.proposed_fix,null,1))}</pre></details>`:''}
  <div class="cols"><div class="content">${md(q.passage)}${md(q.stem)}${ch}</div><div class="orig">${orig}<details><summary>CSV text</summary>${csv}</details></div></div>
  <details><summary>Explanation (${q.explanation.source}; bank ${q.explanation.bank_status})</summary><div class="content">${md(q.explanation.text)}</div>
  ${q.explanation.disputed_quote?`<p class="muted">Disputed in the bank's explanation: “${esc(q.explanation.disputed_quote)}”</p>`:''}</details>
  </section>`;
}
document.getElementById('list').innerHTML=D.q.map(card).join('');
const F={risk:'all',subject:'all'};
function apply(){let n=0;document.querySelectorAll('.q').forEach(e=>{const ok=(F.risk==='all'||e.dataset.risk===F.risk)&&(F.subject==='all'||e.dataset.subject===F.subject);e.style.display=ok?'':'none';n+=ok});document.getElementById('n').textContent=n+' shown';
  document.querySelectorAll('header button').forEach(b=>b.classList.toggle('on',F[b.dataset.k]===b.dataset.v))}
document.getElementById('f').innerHTML=[['risk','all'],['risk','red'],['risk','yellow'],['risk','green'],['subject','all'],['subject','english'],['subject','math']]
  .map(([k,v])=>`<button data-k="${k}" data-v="${v}">${k==='subject'&&v==='all'?'both subjects':v==='english'?'R&W':v}</button>`).join(' ');
document.querySelectorAll('header button').forEach(b=>b.onclick=()=>{F[b.dataset.k]=b.dataset.v;apply()});apply();
addEventListener('DOMContentLoaded',()=>window.renderMathInElement&&renderMathInElement(document.body,{delimiters:[{left:'\\(',right:'\\)',display:false},{left:'\\[',right:'\\]',display:true}],throwOnError:false}));
</script></body></html>
"""


# ---------------------------------------------------------------- check

def check_records(records: list[dict], m: dict | None = None) -> list[str]:
    errs = []
    seen = Counter(r.get("qid") for r in records)
    errs += [f"duplicate qid {q}" for q, n in seen.items() if n > 1]
    if m:
        want = {q["qid"] for q in m["questions"]}
        got = set(seen)
        if want - got:
            errs.append(f"missing: {sorted(want - got)}")
        if got - want:
            errs.append(f"unexpected: {sorted(got - want)}")
    else:
        per = Counter((r["source"]["subject"], r["source"]["module"]) for r in records)
        for (subj, mod), n in per.items():
            if n != {"math": 22, "english": 27}[subj]:
                errs.append(f"{subj} {mod}: {n} questions (expected {22 if subj == 'math' else 27})")
    for r in records:
        q = r.get("qid", "?")
        try:
            errs += [f"{q}: {e}" for e in check_record(r)]
        except (KeyError, TypeError, AttributeError) as e:
            errs.append(f"{q}: malformed record ({type(e).__name__}: {e})")
    return errs


def check_record(r: dict) -> list[str]:
    errs = []
    subj = r["source"]["subject"]
    if subj not in ("math", "english"):
        errs.append(f"subject {subj!r}")
    if r["type"] not in ("mcq", "grid_in"):
        errs.append(f"type {r['type']!r}")
    fkeys = {f["key"] for f in r["figures"]}
    for f in r["figures"]:
        if f["kind"] not in FIGURE_KINDS or not f["alt"]:
            errs.append(f"figure {f['key']}: kind/alt")
    texts = {"stem": r["stem"]}
    if r["passage"] is not None:
        texts["passage"] = r["passage"]
    if r["type"] == "mcq":
        if not isinstance(r["choices"], dict) or set(r["choices"]) != set(LETTERS):
            errs.append("mcq choices must be A-D")
        else:
            texts.update({f"choice {L}": r["choices"][L] for L in LETTERS})
        if r["key"] not in LETTERS:
            errs.append(f"key {r['key']!r}")
    else:
        if r["choices"] is not None:
            errs.append("grid-in with choices")
        if not r["accepted"] or any(parse_num(x) is None for x in r["accepted"]):
            errs.append(f"accepted {r['accepted']!r}")
        elif r["verdict"] != "broken" and not any(same_number(r["key"], x) for x in r["accepted"]):
            errs.append("key is not among accepted")
    used = set()
    for where, t in texts.items():
        errs += content_errors(t or "", where, fkeys)
        used |= refs(t)
    if fkeys - used:
        errs.append(f"figures not placed: {sorted(fkeys - used)}")
    if r["transcription"]["confidence"] not in CONFIDENCE:
        errs.append("transcription confidence")
    if len(r["blind_solves"]) != 2:
        errs.append("needs two blind solves")
    for s in r["blind_solves"]:
        if s["confidence"] not in CONFIDENCE:
            errs.append(f"solve confidence {s['confidence']!r}")
    if r["verdict"] not in VERDICTS:
        errs.append(f"verdict {r['verdict']!r}")
    if r["verdict"] == "key_wrong" and (r["proposed_key"] in (None, r["bank_key"]) or r["key"] != r["proposed_key"]):
        errs.append("key_wrong: proposed_key must differ from the bank key and become the key")
    if r["verdict"] != "key_wrong" and r["key"] != r["bank_key"]:
        errs.append("the key changed without key_wrong")
    if r["verdict"] != "key_correct" and not r["adjudication"]:
        errs.append(f"{r['verdict']} without adjudication")
    errs += issue_errors(r["issues"], "issues")
    e = r["explanation"]
    if e["source"] not in ("bank", "drafted") or e["bank_status"] not in BANK_STATUS or not e["text"]:
        errs.append("explanation source/status/text")
    else:
        errs += content_errors(e["text"], "explanation", set())
        if r["verdict"] in ("key_correct", "key_wrong") and not matches(e["answer_stated"], r["key"], r["accepted"],
                                                                         r["type"]):
            errs.append(f"explanation concludes {e['answer_stated']!r}, key is {r['key']!r}")
    if subj == "math" and e["source"] != "drafted":
        errs.append("math explanation not drafted")
    tg = r["tags"]
    if tg["domain"] not in TAXONOMY.get(subj, {}) or tg["skill"] not in TAXONOMY[subj][tg["domain"]]:
        errs.append(f"tags {tg['domain']!r} / {tg['skill']!r}")
    if tg["difficulty"] not in DIFFICULTY:
        errs.append(f"difficulty {tg['difficulty']!r}")
    errs += fix_errors(r.get("fix"))
    risk, reasons = risk_of(r)
    if r["risk"] != risk or r["risk_reasons"] != reasons:
        errs.append(f"risk {r['risk']!r} but the rules give {risk!r}")
    return errs


def cmd_check(a) -> None:
    p = Path(a.target)
    if not p.exists():
        p = out_dir(a.target)
    if p.is_dir():
        p = p / "questions.jsonl"
    mp = work(p.parent.name) / "manifest.json"
    m = read_json(mp) if mp.exists() else None
    if not p.exists():
        raise Fail(f"no {p}")
    records = []
    errs = []
    for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                errs.append(f"line {n}: {e}")
    errs += check_records(records, m)
    print(summary_line(records) if records else "no records")
    if errs:
        print("\n".join(errs))
        raise Fail(f"{len(errs)} errors in {p}")
    print(f"check: ok ({p})")


# ---------------------------------------------------------------- add-images

def cmd_add_images(a) -> None:
    """Records from before source.images existed get it from the CSVs."""
    keys = {}
    for subject, path in (("math", a.math), ("english", a.english)):
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                slots = {"question": val(r, "image")}
                if subject == "math":
                    slots.update({L: val(r, f"image_{L.lower()}") for L in LETTERS})
                keys[(subject, int(val(r, "id") or 0))] = {k: v for k, v in slots.items() if v}
    files = []
    for target in a.paths:
        p = Path(target)
        files += [p] if p.is_file() else sorted(p.glob("*/questions.jsonl")) or [p / "questions.jsonl"]
    for p in files:
        lines = p.read_text(encoding="utf-8").splitlines()
        out, added = [], 0
        for line in lines:
            if not line.strip():
                continue
            r = json.loads(line)
            src = r.get("source") or {}
            if "images" not in src and "qid" in r:
                src["images"] = keys.get((src.get("subject"), src.get("csv_id")), {})
                added += 1
            out.append(json.dumps(r, ensure_ascii=False))
        if added:
            p.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"{p}: {added} records updated")


# ---------------------------------------------------------------- fix pass

FIX_KINDS = ("corrected", "restored", "invented", "redrawn")
UPLOAD_PREFIX = "mb/"  # MakonBook's own bucket: the API uploads T/figures/ there on import
SVG_MAX = (800, 600)
SVG_TAGS = {"svg", "g", "path", "line", "polyline", "polygon", "rect", "circle", "ellipse", "text", "tspan",
            "defs", "marker", "title", "desc", "clipPath"}


def records_of(test: str) -> list[dict]:
    p = out_dir(test) / "questions.jsonl"
    if not p.exists():
        raise Fail(f"no {p.relative_to(ROOT)}: finish the review first")
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_records(test: str, records: list[dict]) -> None:
    with open(out_dir(test) / "questions.jsonl", "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def fix_inputs(test: str, _cache={}) -> dict:  # noqa: B006 - a per-run cache
    if test not in _cache:
        _cache[test] = {it["qid"]: it for b in step_batches(test, "fix")
                        for it in read_json(batch_paths(test, "fix", b)[0])}
    return _cache[test]


def cmd_fix(a) -> None:
    """Stage the fix pass for every question of a finished test that isn't green."""
    test = a.test
    records = records_of(test)
    targets = [r for r in records if r["risk"] != "green"]
    if not targets:
        print("Every question is green: nothing to fix.")
        return
    client, bucket = r2_client()
    w = work(test)
    items = []
    for r in targets:
        originals = {}
        for slot, key in (r["source"].get("images") or {}).items():
            info = fetch_image(client, bucket, key, w)
            if "error" not in info:
                originals[slot] = info["path"]
        figures = []
        for f in r["figures"]:
            info = fetch_image(client, bucket, f["key"], w)
            figures.append({**f, "path": info.get("path") if "error" not in info else None})
        adj = r.get("adjudication") or {}
        items.append({
            "qid": r["qid"], "subject": r["source"]["subject"], "type": r["type"],
            "passage": r["passage"], "stem": r["stem"], "choices": r["choices"],
            "key": r["key"], "accepted": r["accepted"], "figures": figures,
            "explanation": r["explanation"]["text"],
            "verdict": r["verdict"], "risk": r["risk"], "risk_reasons": r["risk_reasons"],
            "issues": r["issues"], "adjudication": {k: adj.get(k) for k in ("reason", "proof")} if adj else None,
            "proposed_fix": r.get("proposed_fix"), "original_images": originals,
        })
    batches = {}
    for j in range(0, len(items), FIX_BATCH):
        name = f"fix-{j // FIX_BATCH + 1}"
        batches[name] = [it["qid"] for it in items[j:j + FIX_BATCH]]
        write_json(batch_paths(test, "fix", name)[0], items[j:j + FIX_BATCH])
    write_json(w / "fix.json", {"batches": batches})
    c = Counter(r["risk"] for r in targets)
    print(f"{len(targets)} of {len(records)} questions to fix (red {c['red']}, yellow {c['yellow']}).")
    print_batches(test, ["fix"])


def svg_errors(svg) -> list[str]:
    """The fixer's figures: plain drawing only, nothing loaded or run."""
    import xml.etree.ElementTree as ET

    if not isinstance(svg, str) or not svg.strip():
        return ["svg missing"]
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as e:
        return [f"svg is not well-formed XML ({e})"]
    errs = []
    if root.tag != "{http://www.w3.org/2000/svg}svg":
        errs.append("svg: the root must be <svg xmlns=\"http://www.w3.org/2000/svg\">")
    if not root.get("viewBox"):
        errs.append("svg: no viewBox")
    for dim, most in zip(("width", "height"), SVG_MAX):
        try:
            if float(re.sub(r"px$", "", root.get(dim, ""))) > most:
                errs.append(f"svg: {dim} over {most}")
        except ValueError:
            errs.append(f"svg: {dim} must be a number")
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag not in SVG_TAGS:
            errs.append(f"svg: <{tag}> is not allowed")
        for attr, value in el.attrib.items():
            name = attr.split("}")[-1]
            if name == "href" and not value.startswith("#") or name.startswith("on") or name == "style" and "url(" in value:
                errs.append(f"svg: attribute {name}={value[:30]!r} is not allowed")
    return sorted(set(errs))


def render_svg(svg: str) -> bytes:
    """PNG bytes, twice the SVG's size, white background."""
    import tempfile

    try:
        import resvg_py
    except ImportError:
        raise Fail("pip install resvg-py")
    with tempfile.TemporaryDirectory() as empty:  # nothing to load from
        return bytes(resvg_py.svg_to_bytes(svg_string=svg, zoom=2, background="#ffffff", resources_dir=empty))


def upload_key(png: bytes) -> str:
    """The key the API gives an uploaded image: mb/<first 20 bytes of its SHA-256, in hex>.png."""
    import hashlib

    return f"{UPLOAD_PREFIX}{hashlib.sha256(png).hexdigest()[:40]}.png"


def v_fix(f: dict, src: dict) -> list[str]:
    errs = []
    kinds, changes, figures = f.get("kinds"), f.get("changes"), f.get("figures") or []
    if not isinstance(kinds, list) or set(kinds) - set(FIX_KINDS):
        return [f"kinds: a list of {', '.join(FIX_KINDS)}"]
    if not isinstance(changes, dict) or not isinstance(figures, list):
        return ["changes must be an object and figures a list"]
    allowed = {"passage", "stem", "explanation"} | (
        {f"choices.{L}" for L in LETTERS} | {"key"} if src["type"] == "mcq" else {"accepted"})
    if set(changes) - allowed:
        errs.append(f"changes: unknown {sorted(set(changes) - allowed)} (allowed: {', '.join(sorted(allowed))})")
    if not kinds and (changes or figures):
        errs.append("changes without kinds")
    if kinds and not changes and not figures:
        errs.append("kinds without changes")
    if ("redrawn" in kinds) != bool(figures):
        errs.append("redrawn and figures go together")
    names = set()
    for k, fig in enumerate(figures):
        if not isinstance(fig, dict) or not re.fullmatch(r"[a-z0-9_-]{1,20}", str(fig.get("name"))):
            errs.append(f"figure {k}: name (a-z, 0-9, _ or -)")
            continue
        names.add(fig["name"])
        if fig.get("kind") not in FIGURE_KINDS or not str(fig.get("alt") or "").strip():
            errs.append(f"figure {fig['name']}: kind/alt")
        errs += [f"figure {fig['name']}: {e}" for e in svg_errors(fig.get("svg"))]
    # The fixed question, as students would get it.
    fixed = {"passage": src["passage"], "stem": src["stem"], "choices": dict(src["choices"] or {}),
             "key": src["key"], "accepted": src["accepted"], "explanation": src["explanation"]}
    for field, value in changes.items():
        if field.startswith("choices."):
            fixed["choices"][field[8:]] = value
        elif field in fixed:
            fixed[field] = value
    fkeys = {x["key"] for x in src["figures"]} | {f"new/{n}" for n in names}
    texts = {"stem": fixed["stem"], "explanation": fixed["explanation"]}
    if fixed["passage"] is not None:
        texts["passage"] = fixed["passage"]
    if src["type"] == "mcq":
        texts.update({f"choices.{L}": fixed["choices"].get(L) for L in LETTERS})
        if fixed["key"] not in LETTERS:
            errs.append(f"key {fixed['key']!r}")
    elif not isinstance(fixed["accepted"], list) or not fixed["accepted"] or any(parse_num(x) is None for x in fixed["accepted"]):
        errs.append(f"accepted {fixed['accepted']!r}: a list of numbers")
    used = set()
    for where, t in texts.items():
        if not isinstance(t, str) or not t.strip():
            errs.append(f"{where}: empty")
            continue
        t = t.replace("](new:", "](r2:new/")
        errs += content_errors(t, where, fkeys)
        used |= refs(t)
    if names - {u[4:] for u in used if u.startswith("new/")}:
        errs.append(f"figures not placed: {sorted(names - {u[4:] for u in used})}")
    if ("key" in changes or "accepted" in changes) and "explanation" not in changes:
        errs.append("the answer changed: write a new explanation")
    if "explanation" in changes and isinstance(changes["explanation"], str):
        m = re.search(r"\*\*Answer:\*\*\s*(.+?)\s*$", changes["explanation"])
        want = fixed["key"] if src["type"] == "mcq" else (fixed["accepted"] or [""])[0]
        if not m or not matches(m.group(1).strip(" .*"), want, fixed["accepted"] or [], src["type"]):
            errs.append(f"the new explanation must end **Answer:** {want}")
    if f.get("needs_person") is not None and not str(f["needs_person"]).strip():
        errs.append("needs_person: null or what a person must do")
    for k in ("note", "check"):
        if not str(f.get(k) or "").strip():
            errs.append(f"no {k}")
    if f.get("confidence") not in CONFIDENCE:
        errs.append(f"confidence {f.get('confidence')!r}")
    return errs


def fix_errors(fix) -> list[str]:
    """A merged record's fix, for check."""
    if fix is None:
        return []
    errs = []
    if not isinstance(fix, dict) or set(fix) - {"kinds", "changes", "figures", "needs_person", "note", "check",
                                                 "confidence", "by"}:
        return ["fix: unexpected shape"]
    if set(fix.get("kinds") or []) - set(FIX_KINDS):
        errs.append("fix: kinds")
    for fig in fix.get("figures") or []:
        if not str(fig.get("key", "")).startswith(UPLOAD_PREFIX) or fig.get("kind") not in FIGURE_KINDS or not fig.get("alt"):
            errs.append(f"fix figure {fig.get('key')!r}: key/kind/alt")
        elif not (ROOT / "figures" / Path(fig["key"]).name).exists():
            errs.append(f"fix figure {fig['key']}: no figures/{Path(fig['key']).name} in the repository")
    return errs


def cmd_fix_finish(a) -> None:
    test = a.test
    if not step_batches(test, "fix"):
        raise Fail(f"run: fix {test}")
    fixes = require(test, "fix")["fix"]
    records = records_of(test)
    figdir = ROOT / "figures"
    for r in records:
        f = fixes.get(r["qid"])
        if f is None:
            continue
        changes, figs = dict(f["changes"]), []
        for fig in f.get("figures") or []:
            png = render_svg(fig["svg"])
            key = upload_key(png)
            figdir.mkdir(exist_ok=True)
            (figdir / Path(key).name).write_bytes(png)
            figs.append({"key": key, "kind": fig["kind"], "alt": fig["alt"]})
            for field, t in changes.items():
                if isinstance(t, str):
                    changes[field] = t.replace(f"](new:{fig['name']})", f"](r2:{key})")
        r["fix"] = {"kinds": f["kinds"], "changes": changes, "figures": figs, "needs_person": f.get("needs_person"),
                    "note": f["note"], "check": f["check"], "confidence": f["confidence"], "by": MODELS["fix"]}
    write_records(test, records)
    rp = out_dir(test) / "report.md"
    if rp.exists():
        text = rp.read_text(encoding="utf-8").split("\n## Fixes\n")[0].rstrip("\n")
        rp.write_text(text + "\n\n" + fix_report(records), encoding="utf-8")
    errs = check_records(records)
    c = Counter(k for r in records if r.get("fix") for k in r["fix"]["kinds"] or ["none"])
    person = sum(1 for r in records if (r.get("fix") or {}).get("needs_person"))
    print(f"fixes: {len(fixes)} questions; " + ", ".join(f"{k} {n}" for k, n in c.most_common())
          + f"; a person must step in on {person}")
    if errs:
        print("\n".join(errs))
        raise Fail(f"{len(errs)} check errors")
    print("check: ok")


def fix_report(records) -> str:
    L = ["## Fixes", "", "Every question that isn't green, corrected for students; teachers approve or deny each fix.", ""]
    for r in records:
        f = r.get("fix")
        if not f:
            continue
        kinds = ", ".join(f["kinds"]) or "no change"
        L.append(f"- **{label(r)}** ({r['risk']}, {kinds}, {f['confidence']}): {f['note']}"
                 + (f" **A person must:** {f['needs_person']}" if f.get("needs_person") else ""))
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- the bank's own text

def original_of(row: dict) -> dict:
    """The bank's text of a question, as SAT MAKON typed it: plain text, $ for math in Math,
    a few HTML tags in R&W. Its screenshots are source.images in the record."""
    if isinstance(row.get("choices"), dict):  # a review's source file
        choices = {L: row["choices"].get(L) or "" for L in LETTERS}
    else:  # a CSV row
        choices = {L: row.get(L.lower()) or "" for L in LETTERS}
    return {"passage": row.get("passage") or None, "question": row.get("question") or "",
            "choices": choices if any(choices.values()) else None,
            "answer": row.get("answer") or row.get("bank_answer_raw") or ""}


def write_original(od: Path, items: list[dict]) -> None:
    with open(od / "original.jsonl", "w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")


def cmd_add_original(a) -> None:
    rows = {}
    for subject, path in (("math", a.math), ("english", a.english)):
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                rows[(subject, int(val(r, "id") or 0))] = r
    files = []
    for target in a.paths:
        p = Path(target)
        files += [p] if p.is_file() else sorted(p.glob("*/questions.jsonl")) or [p / "questions.jsonl"]
    for p in files:
        items, missing = [], []
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            r = json.loads(line)
            row = rows.get((r["source"]["subject"], r["source"]["csv_id"]))
            if row is None:
                missing.append(r["qid"])
                continue
            items.append({"qid": r["qid"], **original_of(row)})
        write_original(p.parent, items)
        print(f"{p.parent.name}: {len(items)} questions" + (f"; not in the CSVs: {', '.join(missing)}" if missing else ""))


# ---------------------------------------------------------------- main

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("prep")
    p.add_argument("test")
    p.add_argument("--math")
    p.add_argument("--english")
    p.set_defaults(fn=cmd_prep)
    p = sub.add_parser("stage")
    p.add_argument("test")
    p.add_argument("step", choices=["solve", "explain", "adjudicate"])
    p.set_defaults(fn=cmd_stage)
    p = sub.add_parser("status")
    p.add_argument("test")
    p.set_defaults(fn=cmd_status)
    p = sub.add_parser("log-usage")
    p.add_argument("test")
    p.add_argument("entries", nargs="+", metavar="STEP/BATCH=TOKENS")
    p.set_defaults(fn=cmd_log_usage)
    p = sub.add_parser("finish")
    p.add_argument("test")
    p.set_defaults(fn=cmd_finish)
    p = sub.add_parser("check")
    p.add_argument("target", help="a test id, its folder, or a questions.jsonl")
    p.set_defaults(fn=cmd_check)
    p = sub.add_parser("fix")
    p.add_argument("test")
    p.set_defaults(fn=cmd_fix)
    p = sub.add_parser("fix-finish")
    p.add_argument("test")
    p.set_defaults(fn=cmd_fix_finish)
    p = sub.add_parser("add-original")
    p.add_argument("paths", nargs="+", help="test folders, questions.jsonl files, or the repository root")
    p.add_argument("--math", required=True)
    p.add_argument("--english", required=True)
    p.set_defaults(fn=cmd_add_original)
    p = sub.add_parser("add-images")
    p.add_argument("paths", nargs="+", help="test folders, questions.jsonl files, or the repository root")
    p.add_argument("--math", required=True)
    p.add_argument("--english", required=True)
    p.set_defaults(fn=cmd_add_images)
    a = ap.parse_args()
    if a.cmd == "prep" and not (a.math or a.english):
        ap.error("prep needs --math and/or --english")
    try:
        a.fn(a)
    except Fail as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
