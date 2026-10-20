"""python3 -m unittest tools/test_review.py"""

import unittest

from review import content_errors, matches, parse_num, render_svg, same_number, split_accepted, svg_errors, upload_key, v_fix


class Numbers(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(parse_num(".125"), parse_num("1/8"))
        self.assertEqual(parse_num("-5/9") * 9, -5)
        for bad in ("", "abc", "1/0", "1,200", "2x"):
            self.assertIsNone(parse_num(bad), bad)

    def test_same_number(self):
        self.assertTrue(same_number("45/8", "5.625"))
        self.assertTrue(same_number("2/3", ".6667"))
        self.assertTrue(same_number(".666", "2/3"))
        self.assertFalse(same_number("192", "192.1"))  # the DAY1 wrong key must not pass
        self.assertFalse(same_number("0.34", "1/3"))
        self.assertFalse(same_number("2/3", ".7"))

    def test_matches(self):
        acc = split_accepted("-14,-21")  # questions with more than one right answer
        self.assertTrue(matches("-21", "-14", acc, "grid_in"))
        self.assertFalse(matches("14", "-14", acc, "grid_in"))
        self.assertTrue(matches("D", "d", [], "mcq"))
        self.assertFalse(matches("none", "D", [], "mcq"))


class Content(unittest.TestCase):
    def test_ok(self):
        text = ("**Text 1**\n\nIf \\(x^2 = 4\\), then\n\n\\[x = \\pm 2\\]\n\n<u>underlined</u> *it*\n\n"
                "| a | b |\n|---|---|\n| 1 | 2 |\n\n- one\n- two\n\n![a graph](r2:sat/g.png)")
        self.assertEqual(content_errors(text, "t", {"sat/g.png"}), [])
        self.assertEqual(content_errors("I and II are | and ||", "t", set()), [])

    def test_errors(self):
        for text in ("\\(x", "x\\)", "<b>x</b>", "<u>x", "**x", "![g](r2:other.png)", "a�b",
                     "| a | b |\n| 1 | 2 |"):
            self.assertTrue(content_errors(text, "t", {"sat/g.png"}), text)


SVG = ('<svg xmlns="http://www.w3.org/2000/svg" width="300" height="200" viewBox="0 0 300 200">'
       '<rect width="300" height="200" fill="white"/><line x1="20" y1="180" x2="280" y2="20" stroke="black"/>'
       '<text x="30" y="40" font-family="sans-serif" font-size="16">y = 2x</text></svg>')

MCQ = {"qid": "math-m1-01", "type": "mcq", "passage": None, "stem": "Which is \\(2 + 2\\)?",
       "choices": {"A": "3", "B": "4", "C": "4", "D": "6"}, "key": "B", "accepted": [],
       "figures": [{"key": "sat/g.png", "kind": "graph", "alt": "a line"}],
       "explanation": "It is 4.\n\n**Answer:** B"}


def fix(**kw):
    f = {"qid": "math-m1-01", "kinds": [], "changes": {}, "figures": [], "needs_person": None,
         "note": "Fine as is.", "check": "Only B works.", "confidence": "high"}
    f.update(kw)
    return f


class Fixes(unittest.TestCase):
    def test_svg(self):
        self.assertEqual(svg_errors(SVG), [])
        png = render_svg(SVG)
        self.assertTrue(png.startswith(b"\x89PNG"))
        self.assertRegex(upload_key(png), r"^mb/[0-9a-f]{20}\.png$")
        for bad in ("<svg/>", "not xml", SVG.replace('width="300"', 'width="2000"'),
                    SVG.replace("<rect", '<image href="file:///etc/passwd"/><rect'),
                    SVG.replace("<rect", "<script>alert(1)</script><rect"),
                    SVG.replace("<rect", '<rect onclick="x()"')):
            self.assertTrue(svg_errors(bad), bad)

    def test_no_change(self):
        self.assertEqual(v_fix(fix(), MCQ), [])
        self.assertTrue(v_fix(fix(changes={"choices.C": "5"}), MCQ))  # changes need kinds

    def test_invented_distractor(self):
        self.assertEqual(v_fix(fix(kinds=["invented"], changes={"choices.C": "5"}), MCQ), [])

    def test_redrawn(self):
        stem = "The graph:\n\n![a line through the origin](new:g1)\n\nWhich is \\(2 + 2\\)?"
        f = fix(kinds=["redrawn"], changes={"stem": stem},
                figures=[{"name": "g1", "kind": "graph", "alt": "a line", "svg": SVG}])
        self.assertEqual(v_fix(f, MCQ), [])
        f["changes"]["stem"] = "Which is \\(2 + 2\\)?"  # drawn but not placed
        self.assertIn("figures not placed: ['g1']", v_fix(f, MCQ))

    def test_errors(self):
        for f in (fix(kinds=["guessed"]), fix(kinds=["corrected"], changes={"choices.E": "x"}),
                  fix(kinds=["corrected"], changes={"key": "C"}),  # a new key needs a new explanation
                  fix(kinds=["corrected"], changes={"key": "C", "explanation": "**Answer:** B"}),
                  fix(kinds=["corrected"], changes={"stem": "Unclosed \\(x"}),
                  fix(confidence="sure"), fix(note="")):
            self.assertTrue(v_fix(f, MCQ), f)
        self.assertEqual(v_fix(fix(kinds=["corrected"], changes={"key": "C", "explanation": "Now C.\n\n**Answer:** C"}),
                               MCQ), [])


if __name__ == "__main__":
    unittest.main()
