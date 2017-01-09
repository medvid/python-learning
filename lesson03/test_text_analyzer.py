import unittest
from text_analyzer import *

class TestTextAnalyzer(unittest.TestCase):
    def test_is_word(self):
        self.assertTrue(is_word("latin"))
        self.assertTrue(is_word("кирилиця"))
        self.assertTrue(is_word("汉语; 漢語"))
        self.assertTrue(is_word("日本語"))
        self.assertTrue(is_word("العَرَبِيَّة"))

    def test_is_not_word(self):
        self.assertFalse(is_word(""))
        self.assertFalse(is_word(" "))
        self.assertFalse(is_word(".!@#$%^&*()"))
        self.assertFalse(is_word("  .  "))
        self.assertFalse(is_word("?!"))

    def test_is_char(self):
        self.assertTrue(is_char("a"))
        self.assertTrue(is_char("Є"))
        self.assertTrue(is_char("語"))

    def test_is_not_char(self):
        self.assertFalse(is_char(""))
        self.assertFalse(is_char(" "))
        self.assertFalse(is_char("."))
        self.assertFalse(is_char("/e"))

    def test_count_words(self):
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("a"), 1)
        self.assertEqual(count_words("?   "), 0)
        self.assertEqual(count_words("x ^ y"), 2)
        self.assertEqual(count_words("x^y"), 1)
        self.assertEqual(count_words("x^   y"), 2)
        self.assertEqual(count_words("^^^ ^^"), 0)
        self.assertEqual(count_words("ddddd   dddddd  dddddddddddd"), 3)

    def test_count_chars(self):
        self.assertEqual(count_chars(""), 0)
        self.assertEqual(count_chars("A"), 1)
        self.assertEqual(count_chars("тест"), 4)
        self.assertEqual(count_chars("_zz_zz_"), 4)

    def test_process_unique_words(self):
        words = {}
        self.assertEqual(len(words), 0)
        process_unique_words("aa bb cc", words)
        self.assertEqual(len(words), 3)
        process_unique_words("cc dd", words)
        self.assertEqual(len(words), 4)

if __name__ == "__main__":
    unittest.main();
