#!/usr/bin/env python3
"""Validate vocab/words.jsonl, SAT MAKON's vocabulary list prepared for MakonBook's import.

  python3 tools/check_vocab.py [PATH]      PATH defaults to vocab/words.jsonl

One JSON object per line, one line per word, in study order. Checked here:
  - the file is UTF-8 and every line is a JSON object (no blank lines)
  - only the known fields; list, list_title, word, definition and example are present
    and are non-empty strings (part_of_speech and image are optional strings)
  - list: lower-case letters, digits and dashes, at most 64 characters
  - list_title: the same on every line of a list, and no two lists share a title;
    each list's lines are together (lists are shown in file order)
  - word: at most 100 characters, letters/spaces/hyphens/apostrophes only (no
    leftover PDF ligatures or broken characters), unique within its list ignoring
    case, and not repeated in a later list (duplicates keep the first)
  - definition, example: at most 1000 characters, one line, English (Latin letters)
  - example: one sentence that contains the word, or a simple inflection of it
    (abate -> abated; adapt to -> adapted to)
  - part_of_speech: one of PARTS_OF_SPEECH
  - image: a file that exists in vocab/images/
Prints the lists, the words per list and the total; exits 1 on errors.
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT = ROOT / "vocab" / "words.jsonl"

REQUIRED = ("list", "list_title", "word", "definition", "example")
OPTIONAL = ("part_of_speech", "image")
MAX_LEN = {"list": 64, "word": 100, "definition": 1000, "example": 1000}
LIST_ID = re.compile(r"[a-z0-9-]+")
WORD_CHARS = re.compile(r"[A-Za-z]+(?:[ '-][A-Za-z]+)*")
PARTS_OF_SPEECH = ("noun", "verb", "adjective", "adverb", "preposition", "conjunction",
                   "pronoun", "determiner", "interjection", "phrase")
IMAGE_TYPES = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg")

TOKEN = re.compile(r"[a-z]+(?:['-][a-z]+)*")
# A sentence ends at . ! or ? (maybe inside a closing quote or bracket) followed by a capital.
SENTENCE_BREAK = re.compile(r"[.!?][\"'”’)]*\s+[\"'“‘(]*[A-Z]")
SENTENCE_END = re.compile(r"[.!?][\"'”’)]*$")

# Irregular forms (base: inflections) of verbs and plurals likely in an SAT word list.
IRREGULAR = {
    "be": "am is are was were been being", "become": "became", "begin": "began begun",
    "break": "broke broken", "bring": "brought", "build": "built", "buy": "bought",
    "catch": "caught", "choose": "chose chosen", "come": "came", "dig": "dug",
    "do": "did done does", "draw": "drew drawn", "drive": "drove driven", "eat": "ate eaten",
    "fall": "fell fallen", "feel": "felt", "fight": "fought", "find": "found",
    "fly": "flew flown", "forbid": "forbade forbidden", "foresee": "foresaw foreseen",
    "foretell": "foretold", "forget": "forgot forgotten", "forgive": "forgave forgiven",
    "freeze": "froze frozen", "get": "got gotten", "give": "gave given", "go": "went gone",
    "grow": "grew grown", "have": "has had", "hear": "heard", "hide": "hid hidden",
    "hold": "held", "keep": "kept", "know": "knew known", "lay": "laid", "lead": "led",
    "leave": "left", "lend": "lent", "lie": "lay lain", "lose": "lost", "make": "made",
    "mean": "meant", "meet": "met", "mislead": "misled", "mistake": "mistook mistaken",
    "misunderstand": "misunderstood", "overcome": "overcame", "overtake": "overtook overtaken",
    "pay": "paid", "rise": "rose risen", "run": "ran", "say": "said", "see": "saw seen",
    "seek": "sought", "sell": "sold", "send": "sent", "show": "shown", "shrink": "shrank shrunk",
    "sing": "sang sung", "speak": "spoke spoken", "spend": "spent", "stand": "stood",
    "strike": "struck", "swear": "swore sworn", "take": "took taken", "teach": "taught",
    "tell": "told", "think": "thought", "throw": "threw thrown", "understand": "understood",
    "undertake": "undertook undertaken", "uphold": "upheld", "wake": "woke woken",
    "wear": "wore worn", "win": "won", "withdraw": "withdrew withdrawn",
    "withhold": "withheld", "withstand": "withstood", "write": "wrote written",
    "analysis": "analyses", "basis": "bases", "crisis": "crises", "criterion": "criteria",
    "hypothesis": "hypotheses", "phenomenon": "phenomena", "thesis": "theses",
    "child": "children", "man": "men", "woman": "women", "person": "people",
}
BASE_OF = {f: b for b, fs in IRREGULAR.items() for f in fs.split()}
VOWELS = "aeiou"


class Fail(Exception):
    pass


def bases(tok: str) -> set[str]:
    """tok and the base forms it may be a regular inflection of (stopped -> stop, cities -> city)."""
    out = {tok}
    if tok in BASE_OF:
        out.add(BASE_OF[tok])
    for suf, adds in (("ies", ("y",)), ("ied", ("y",)), ("ier", ("y",)), ("iest", ("y",)),
                      ("ing", ("", "e")), ("ed", ("", "e")), ("est", ("", "e")), ("er", ("", "e")),
                      ("es", ("",)), ("s", ("",))):
        stem = tok[: -len(suf)]
        if tok.endswith(suf) and len(stem) >= 2:
            out |= {stem + a for a in adds}
            if len(stem) >= 3 and stem[-1] == stem[-2] and stem[-1] not in VOWELS + "lsz":
                out.add(stem[:-1])  # stopped -> stop
    return out


def inflections(base: str) -> set[str]:
    """The regular inflections of base: -s/-es, -ed/-d, -ing, -er/-est, with the usual spelling changes."""
    out = {base, base + "s", base + "es", base + "ed", base + "d", base + "ing", base + "er", base + "est"}
    if base.endswith("e"):
        out |= {base[:-1] + "ing"}
    if base.endswith("y") and len(base) > 1 and base[-2] not in VOWELS:
        out |= {base[:-1] + s for s in ("ies", "ied", "ier", "iest")}
    if len(base) >= 3 and base[-1] not in VOWELS + "wxy" and base[-2] in VOWELS and base[-3] not in VOWELS:
        out |= {base + base[-1] + s for s in ("ed", "ing", "er", "est")}  # stop -> stopped
    out |= set(IRREGULAR.get(base, "").split())
    return out


def forms(tok: str) -> set[str]:
    """Every form that counts as tok or a simple inflection of it."""
    out = set()
    for b in bases(tok):
        out |= inflections(b)
    return out


def tokens(text: str) -> list[str]:
    text = text.lower().replace("’", "'")
    return [re.sub(r"'s?$", "", t) for t in TOKEN.findall(text)]


def uses_word(example: str, word: str) -> bool:
    """True when example contains word (every token in order, each maybe inflected)."""
    want = [forms(t) for t in tokens(word)]
    have = tokens(example)
    if not want:
        return False
    return any(all(have[i + j] in want[j] for j in range(len(want)))
               for i in range(len(have) - len(want) + 1))


def text_errors(v: str, where: str) -> list[str]:
    errs = []
    if v != v.strip():
        errs.append(f"{where}: leading or trailing whitespace")
    if "  " in v:
        errs.append(f"{where}: double space")
    for ch in sorted(set(v)):
        cat = unicodedata.category(ch)
        name = unicodedata.name(ch, "")
        if cat.startswith("C"):
            errs.append(f"{where}: control character {ch!r}")
        elif cat.startswith("L") and (not name.startswith("LATIN") or "LIGATURE" in name):
            errs.append(f"{where}: {ch!r} ({name or 'unnamed'}) is not a plain Latin letter")
        elif ch == "�":
            errs.append(f"{where}: replacement character (broken encoding)")
    return errs


def check_record(r: dict, where: str, images: Path) -> list[str]:
    errs = []
    unknown = sorted(set(r) - set(REQUIRED) - set(OPTIONAL))
    if unknown:
        errs.append(f"{where}: unknown fields {unknown}")
    for k in REQUIRED:
        if k not in r:
            errs.append(f"{where}: missing {k}")
    for k in REQUIRED + OPTIONAL:
        if k not in r:
            continue
        v = r[k]
        if not isinstance(v, str) or not v.strip():
            errs.append(f"{where}: {k} must be a non-empty string")
            continue
        if len(v) > MAX_LEN.get(k, 10**9):
            errs.append(f"{where}: {k} is {len(v)} characters (max {MAX_LEN[k]})")
        if k != "image":
            errs += text_errors(v, f"{where}: {k}")
    if errs:
        return errs
    if not LIST_ID.fullmatch(r["list"]):
        errs.append(f"{where}: list {r['list']!r} must be lower-case letters, digits and dashes")
    if not WORD_CHARS.fullmatch(r["word"]):
        errs.append(f"{where}: word {r['word']!r} has characters other than letters, spaces, hyphens, apostrophes")
    for k in ("definition", "example"):
        if "\n" in r[k] or "\r" in r[k]:
            errs.append(f"{where}: {k} must be one line")
    ex = r["example"]
    if "__" in ex:
        errs.append(f"{where}: example has a blank (__)")
    if not (ex[0].isupper() or ex[0].isdigit() or ex[0] in "\"“'‘"):
        errs.append(f"{where}: example must start with a capital letter")
    if not SENTENCE_END.search(ex):
        errs.append(f"{where}: example must end with . ! or ?")
    if SENTENCE_BREAK.search(ex):
        errs.append(f"{where}: example must be one sentence")
    if not uses_word(ex, r["word"]):
        errs.append(f"{where}: example does not use {r['word']!r} or an inflection of it")
    pos = r.get("part_of_speech")
    if pos is not None and pos not in PARTS_OF_SPEECH:
        errs.append(f"{where}: part_of_speech {pos!r} is not one of {', '.join(PARTS_OF_SPEECH)}")
    img = r.get("image")
    if img is not None:
        p = Path(img)
        if p.is_absolute() or ".." in p.parts or "\\" in img:
            errs.append(f"{where}: image {img!r} must be a path inside vocab/images/")
        elif p.suffix.lower() not in IMAGE_TYPES:
            errs.append(f"{where}: image {img!r} is not one of {', '.join(IMAGE_TYPES)}")
        elif not (images / p).is_file():
            errs.append(f"{where}: image {img!r} is not in {images}/")
    return errs


def check_file(p: Path) -> tuple[list[dict], list[str]]:
    raw = p.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        line = raw[: e.start].count(b"\n") + 1
        return [], [f"line {line}: not UTF-8 ({e.reason})"]
    if text.startswith("﻿"):
        return [], ["line 1: starts with a byte-order mark"]
    images = p.parent / "images"
    records, errs = [], []
    title_of: dict[str, str] = {}
    list_of_title: dict[str, str] = {}
    first_seen: dict[str, tuple[str, int]] = {}  # word (casefold) -> (list, line)
    order: list[str] = []
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines.pop()
    for n, line in enumerate(lines, 1):
        where = f"line {n}"
        if not line.strip():
            errs.append(f"{where}: blank line")
            continue
        try:
            r = json.loads(line)
        except json.JSONDecodeError as e:
            errs.append(f"{where}: invalid JSON ({e.msg})")
            continue
        if not isinstance(r, dict):
            errs.append(f"{where}: not a JSON object")
            continue
        where = f"line {n} ({r.get('word', '?')})"
        e = check_record(r, where, images)
        errs += e
        if e:
            continue
        records.append(r)
        lst, title = r["list"], r["list_title"]
        if lst not in title_of:
            title_of[lst] = title
            order.append(lst)
            if title in list_of_title:
                errs.append(f"{where}: title {title!r} is also used by list {list_of_title[title]}")
            list_of_title.setdefault(title, lst)
        else:
            if title != title_of[lst]:
                errs.append(f"{where}: list {lst} has two titles: {title_of[lst]!r} and {title!r}")
            if order[-1] != lst:
                errs.append(f"{where}: list {lst} continues after list {order[-1]} started; keep a list's lines together")
        key = r["word"].casefold()
        if key in first_seen:
            flst, fn = first_seen[key]
            if flst == lst:
                errs.append(f"{where}: {r['word']!r} is already in list {lst} (line {fn})")
            else:
                errs.append(f"{where}: {r['word']!r} is a duplicate of line {fn} (list {flst}); keep the first")
        else:
            first_seen[key] = (lst, n)
    if not lines:
        errs.append("the file is empty")
    return records, errs


def summary(records: list[dict]) -> str:
    counts = Counter(r["list"] for r in records)
    titles = {r["list"]: r["list_title"] for r in records}
    w = max((len(k) for k in counts), default=4)
    t = max((len(v) for v in titles.values()), default=5)
    rows = [f"  {k:<{w}}  {titles[k]:<{t}}  {n:>4}" for k, n in counts.items()]
    return "\n".join([f"{len(counts)} lists, {len(records)} words", *rows, f"  {'total':<{w}}  {'':<{t}}  {len(records):>4}"])


def main() -> None:
    p = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    try:
        if len(sys.argv) > 2:
            raise Fail("usage: check_vocab.py [PATH]")
        if not p.is_file():
            raise Fail(f"no {p}")
        records, errs = check_file(p)
        print(f"{p}:")
        print(summary(records) if records else "no valid records")
        if errs:
            print("\n".join(errs))
            raise Fail(f"{len(errs)} errors in {p}")
        print(f"check: ok ({p})")
    except Fail as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
