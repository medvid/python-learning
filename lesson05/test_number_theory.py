import number_theory
import unittest

class TestNumberTheory(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(1, number_theory.gcd(1, 1))
        self.assertEqual(2, number_theory.gcd(2, 2))
        self.assertEqual(5, number_theory.gcd(45, 55))
        self.assertEqual(1, number_theory.gcd(91, 19))
        self.assertEqual(6, number_theory.gcd(66, 36))
        self.assertEqual(300, number_theory.gcd(300, 300))
        self.assertEqual(9, number_theory.gcd(18, 9))

    def test_lcm(self):
        self.assertEqual(60, number_theory.lcm(6, 20))

if __name__ == "__main__":
    unittest.main()
