# Vocabulary drawings

The pictures in `vocab/images/` are drawn as code: each word is a Python function that returns a
400×400 SVG, rendered to an 800×800 PNG. `vocab/image-prompts/prompts.jsonl` lists the 500 words
to picture, in study order, each with a `scene` describing what to show.

- `common.py`: the SVG frame (`svg(body, bg, defs)`) and shared shapes: arrows (`arrow`,
  `carrow` curved, `arc_arrow` around a circle), trees (`bush`, `pine`), the sleep sign (`zzz`),
  number formatting (`f`), and `INK`, the dark color for outlines and details.
- `batch_NN.py`: one batch of drawings, ending with `PICTURES = {word: function}`.
  `batch_01.py` holds the first 30 (dormant, converge, hoard, …) and is the style reference.
- `make.py`: renders pictures and contact sheets to `work/vocab_drawings/` (git-ignored);
  with `--install` it copies them to `vocab/images/` and links them in `vocab/words.jsonl`.

```sh
python3 tools/vocab_drawings/make.py --batch 2               # render batch 2 + contact sheets
python3 tools/vocab_drawings/make.py --word lift rapid       # re-render a few while fixing them
python3 tools/vocab_drawings/make.py --batch 2 --install     # put batch 2 in vocab/images/
python3 tools/check_vocab.py
```

## Style

Match `batch_01.py` so the set looks like one book:

- **Flat shapes, no outlines on everything.** Solid fills, a few highlights (a lighter circle or a
  white arc at low opacity), `INK` (#264653) only for small dark details: eyes, axes, thin lines.
- **One idea per picture, readable at flashcard size** (about 200 px wide on a phone): big shapes,
  no tiny details that carry the meaning. Fill the frame, keeping about 10 px clear at the edges.
- **Show the meaning, not just the topic.** Use contrast (one red bird among gray ones for
  *conspicuous*), scale (a tiny boat over a whale for *immense*), or steps joined by arrows for a
  change (sugar cube → crumbs → clear water for *dissolve*).
- **A soft background per picture** (pale sky, sand, mint, cream…) and colors from the
  batch 1 palette: teal #2a9d8f, yellow #e9c46a, orange #f4a261, coral #e76f51, red #e63946,
  blues #457b9d #4895ef #a8dadc #caf0f8, greens #2d6a4f #40916c #52b788 #6a994e #a7c957,
  browns #7f5539 #8d6e63, grays #adb5bd #6c757d.
- **No text, letters or numbers** (the `zzz` sleep sign is the one exception), no real people,
  brands, logos or national flags.
- The prompt's `scene` is a brief, not a contract: simplify it if a simpler picture shows the
  meaning more clearly.

## Checking

Look at every picture: the contact sheets for the set, and the PNG itself at full size for each
one. Common faults: a part drawn outside the frame or hidden behind another shape, a self-crossing
path filled oddly, objects floating (no shadow or ground), a detail too small to read, or a picture
that shows the topic but not the word (*hibernation* needs the sleeping bear, not just a cave).
Fix and re-render with `--word` until each one is right, then `--install`.
