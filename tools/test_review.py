"""python3 -m unittest tools/test_review.py"""

import unittest

from review import content_errors, matches, parse_num, same_number, split_accepted


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


if __name__ == "__main__":
    unittest.main()
