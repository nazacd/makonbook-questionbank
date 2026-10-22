# Image prompts for the vocabulary list

500 ready-to-paste prompts for Gemini (or any image generator), one per word, for the words that are easiest to show in a picture: about 10 per unit, so every list has pictures. Each prompt names the word, gives its meaning, describes one scene, and asks for the same flat illustration style with no text in the picture.

Claude can also draw them, in the style of the first 30 pictures: see [tools/vocab_drawings/README.md](../../tools/vocab_drawings/README.md). The steps below are for making them in the Gemini app instead.

| Page | Prompts |
|---|---|
| [Units 1–10](units-01-10.md) | 100 |
| [Units 11–20](units-11-20.md) | 101 |
| [Units 21–30](units-21-30.md) | 100 |
| [Units 31–40](units-31-40.md) | 100 |
| [Units 41–50](units-41-50.md) | 99 |

## How to use them in the Gemini app

1. Open a page above. On GitHub each prompt has a copy button (top right of its box).
2. Paste one prompt into Gemini as its own message and send it. Each prompt is complete on its own, so you can do them in any order. If the pictures start to drift in style, start a new chat.
3. Check the picture: no letters or words in it, the meaning is clear, nothing looks wrong. If not, ask Gemini to try again ("same prompt, try again", or say what to fix).
4. Download it and rename it to the file name shown next to the word (for example `skepticism-toward.png`). Keep `.jpg` if the app saves a JPEG: the name before the dot is what matters.
5. Put the files in `vocab/images/`. On GitHub: open that folder on your branch, then **Add file → Upload files**. A file with the same name replaces the old one.
6. When a batch is in, ask Claude to link the new pictures in `words.jsonl` (the `image` field) and run `python3 tools/check_vocab.py`.

30 of these words already have a drawn picture; their prompts are marked "replaces the current drawing". Skip them if you want to keep the drawings.

The Gemini app may limit how many images you can make per day, so this may take several days. Pictures from the app may carry a small Gemini mark in a corner.

## Files

- `units-*.md`: the prompts, by unit, for copying.
- `prompts.jsonl`: the same prompts as data, one per line, in study order, for a script that sends them through an API: `list`, `word`, `file` (the name to save as), `has_drawing`, `scene` (the picture described in the prompt) and `prompt` (the full text to send).

Every prompt ends with the same style text:

> Style: flat vector illustration with soft, friendly colors, simple clean shapes, a plain light background, and one clear focal point. Keep it uncluttered so the meaning is obvious at a glance. Do not include any text, words, letters, or numbers anywhere in the image.

To change the look of all pictures, change that text in every prompt (it is identical in each), or rebuild the prompts from each record's `scene`.
