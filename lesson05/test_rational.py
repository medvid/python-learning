import unittest
import rational as r

class TestRational(unittest.TestCase):
    def test_init(self):
        self.assertEqual("1/1", str(r.Rational(1, 1)))
        self.assertEqual("2/3", str(r.Rational(2, 3)))
        self.assertEqual("7/5", str(r.Rational(35, 25)))

    def test_from_str(self):
        self.assertEqual("1/2", str(r.Rational.from_str("3/6")))

    def test_add(self):
        r1_1 = r.Rational(1, 1)
        r2_3 = r.Rational(2, 3)
        r5_2 = r.Rational(5, 2)
        self.assertEqual("2/1", str(r1_1.add(r1_1)))
        self.assertEqual("4/3", str(r2_3.add(r2_3)))
        self.assertEqual("2/1", str(r2_3.add(r2_3).add(r2_3)))
        self.assertEqual("5/3", str(r2_3.mul(r5_2)))
        self.assertEqual("3/5", str(r1_1.div(r5_2.mul(r2_3))))

if __name__ == "__main__":
    unittest.main()
