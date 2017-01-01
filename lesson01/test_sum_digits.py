import unittest
from sum_digits import sum_digits

class TestSumDigits(unittest.TestCase):
    def test_sum_digits(self):
        self.assertEqual(sum_digits(0), 0)
        self.assertEqual(sum_digits(1), 1)
        self.assertEqual(sum_digits(123456), 21)
        self.assertEqual(sum_digits(99999999999), 99)
        self.assertEqual(sum_digits(-100000000000000000000001), 2)

if __name__ == "__main__":
    unittest.main()
