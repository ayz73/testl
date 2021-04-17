import unittest
from fractions_class import Fraction
import fractions_class

class fractions_class_test(unittest.TestCase):
    def test_gcf(self):
        self.assertEqual(fractions_class.gcf(78, 66), 6)
        self.assertEqual(fractions_class.gcf(10, 0), 0)
        self.assertEqual(fractions_class.gcf(-100, -5), -5)
        self.assertEqual(fractions_class.gcf(100, -5), -5)

class fractions_test(unittest.TestCase):

    def test_fractions_add(self):
        f_1 = Fraction(1, 2)
        f_2 = Fraction(1, 4)
        self.assertEqual(str(f_1 + f_2), "3/4")

        f_2.den = 8
        self.assertEqual(str(f_1 + f_2), "5/8")

        f_3 = Fraction(-1, 2)
        f_4 = Fraction(2, -5)
        self.assertEqual(str(f_3 + f_4), "-9/10")

    def test_fractions_sub(self):
        f_1 = Fraction(1, 2)
        f_2 = Fraction(1, 4)
        self.assertEqual(str(f_1 - f_2), "1/4")

        f_2.den = 8
        self.assertEqual(str(f_1 - f_2), "3/8")

        f_3 = Fraction(-1, 2)
        f_4 = Fraction(2, -5)
        self.assertEqual(str(f_3 - f_4), "-1/10")

    def test_fractions_mul(self):
        f_1 = Fraction(1, 2)
        f_2 = Fraction(1, 4)
        self.assertEqual(str(f_1 * f_2), "1/8")

        f_1.num = 5
        f_2.den = 8
        self.assertEqual(str(f_1 * f_2), "5/16")

        f_3 = Fraction(-1, 2)
        f_4 = Fraction(2, -5)
        self.assertEqual(str(f_3 * f_4), "1/5")
    
    def test_get_num(self):
        f_1 = Fraction(1, 5)
        f_2 = Fraction(3, 4)
        self.assertEqual(f_1.get_num(), 1)
        self.assertEqual(f_2.get_num(), 3)

        f_1.num = 2
        f_2.num = 5
        self.assertEqual(f_1.get_num(), 2)
        self.assertEqual(f_2.get_num(), 5)

    def test_get_den(self):
        f_1 = Fraction(1, 5)
        f_2 = Fraction(3, 4)
        self.assertEqual(f_1.get_den(), 5)
        self.assertEqual(f_2.get_den(), 4)

        f_1.den = 6
        f_2.den = 5
        self.assertEqual(f_1.get_den(), 6)
        self.assertEqual(f_2.get_den(), 5)


if __name__ == "__main__":
    unittest.main()