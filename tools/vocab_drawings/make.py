#!/usr/bin/env python3
"""Draw, preview and install the vocabulary pictures (vocab/images/).

  python3 tools/vocab_drawings/make.py [--batch NN ...] [--word WORD ...] [--install]

Each batch_NN.py in this folder has PICTURES = {word: function returning an SVG string}.
make.py renders the selected pictures (default: all batches) to work/vocab_drawings/
(git-ignored): <file>.svg, an 800x800 <file>.png, and contact sheets sheet-01.png, ... with
20 labelled pictures each, for checking them by eye. <file> is the word with spaces as
hyphens, as in vocab/image-prompts/prompts.jsonl.

--install also copies the PNGs to vocab/images/ and sets "image" for those words in
vocab/words.jsonl (other lines are left byte for byte). Run tools/check_vocab.py after.
Needs Pillow and Chromium ($CHROMIUM, default /opt/pw-browsers/chromium).
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WORDS = ROOT / "vocab" / "words.jsonl"
IMAGES = ROOT / "vocab" / "images"
WORK = ROOT / "work" / "vocab_drawings"
CHROMIUM = os.environ.get("CHROMIUM", "/opt/pw-browsers/chromium")
SIZE = 800
PER_SHEET = 20


class Fail(Exception):
    pass


def file_name(word: str) -> str:
    return word.replace(" ", "-") + ".png"


def load(batches: list[str]) -> dict[str, tuple[str, object]]:
    """word -> (batch, drawing function), from the selected batch_NN.py modules."""
    sys.path.insert(0, str(HERE))
    names = sorted(p.stem for p in HERE.glob("batch_*.py"))
    if batches:
        want = {f"batch_{int(b):02d}" for b in batches}
        missing = want - set(names)
        if missing:
            raise Fail(f"no {', '.join(sorted(missing))}.py in {HERE}")
        names = [n for n in names if n in want]
    out = {}
    for n in names:
        for word, fn in importlib.import_module(n).PICTURES.items():
            if word in out:
                raise Fail(f"{word!r} is drawn in both {out[word][0]} and {n}")
            out[word] = (n, fn)
    return out


def render(svg_text: str, png: Path) -> None:
    html = png.with_suffix(".html")
    html.write_text("<!doctype html><html><head><style>html,body{margin:0;padding:0;overflow:hidden}"
                    f"svg{{display:block;width:{SIZE}px;height:{SIZE}px}}</style></head><body>"
                    + svg_text + "</body></html>", encoding="utf-8")
    shot = png.with_suffix(".shot.png")
    # A window taller than the picture: headless Chromium's viewport is shorter than --window-size.
    subprocess.run([CHROMIUM, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=1", f"--window-size={SIZE},{SIZE + 200}",
                    f"--screenshot={shot}", html.as_uri()], check=True, capture_output=True, timeout=90)
    Image.open(shot).convert("RGB").crop((0, 0, SIZE, SIZE)).save(png, optimize=True)
    shot.unlink()
    html.unlink()


def sheets(words: list[str]) -> list[Path]:
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except OSError:
        font = ImageFont.load_default()
    cols, cell, pad = 5, 240, 30
    out = []
    for k in range(0, len(words), PER_SHEET):
        part = words[k:k + PER_SHEET]
        rows = -(-len(part) // cols)
        sheet = Image.new("RGB", (cols * cell, rows * (cell + pad)), "white")
        d = ImageDraw.Draw(sheet)
        for i, w in enumerate(part):
            x, y = (i % cols) * cell, (i // cols) * (cell + pad)
            sheet.paste(Image.open(WORK / file_name(w)).resize((cell - 10, cell - 10)), (x + 5, y + 5))
            d.text((x + cell // 2, y + cell + 10), w, fill="black", font=font, anchor="mm")
        p = WORK / f"sheet-{k // PER_SHEET + 1:02d}.png"
        sheet.save(p)
        out.append(p)
    return out


def install(words: list[str]) -> None:
    IMAGES.mkdir(exist_ok=True)
    for w in words:
        (IMAGES / file_name(w)).write_bytes((WORK / file_name(w)).read_bytes())
    lines = WORDS.read_text(encoding="utf-8").split("\n")
    todo = set(words)
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        r = json.loads(line)
        if r["word"] in todo:
            todo.discard(r["word"])
            r.pop("image", None)
            r["image"] = file_name(r["word"])
            lines[i] = json.dumps(r, ensure_ascii=False)
    WORDS.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--batch", nargs="+", default=[], help="batch numbers (default: all)")
    ap.add_argument("--word", nargs="+", default=[], help="only these words")
    ap.add_argument("--install", action="store_true", help="copy to vocab/images/ and link in words.jsonl")
    a = ap.parse_args()
    try:
        pictures = load(a.batch)
        known = [json.loads(l)["word"] for l in WORDS.read_text(encoding="utf-8").splitlines() if l.strip()]
        unknown = sorted(set(pictures) - set(known))
        if unknown:
            raise Fail(f"not words in {WORDS.relative_to(ROOT)}: {unknown}")
        if a.word:
            missing = sorted(set(a.word) - set(pictures))
            if missing:
                raise Fail(f"no drawing for {missing}")
        chosen = [w for w in known if w in pictures and (not a.word or w in a.word)]  # study order
        WORK.mkdir(parents=True, exist_ok=True)
        for w in chosen:
            text = pictures[w][1]()
            (WORK / file_name(w)).with_suffix(".svg").write_text(text, encoding="utf-8")
            render(text, WORK / file_name(w))
        print(f"{len(chosen)} pictures in {WORK.relative_to(ROOT)}/")
        for p in sheets(chosen):
            print(f"  {p.relative_to(ROOT)}")
        if a.install:
            install(chosen)
            print(f"installed {len(chosen)} in {IMAGES.relative_to(ROOT)}/ and linked them in "
                  f"{WORDS.relative_to(ROOT)}; now run python3 tools/check_vocab.py")
    except (Fail, subprocess.CalledProcessError) as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
