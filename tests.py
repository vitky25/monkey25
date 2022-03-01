from fraction import Fraction
import unittest


class TestInit(unittest.TestCase):
    # several of these will need to check to see if an exception is raised
    def test_divZero(self):
        with self.assertRaises(ZeroDivisionError, msg="Denominator of zero fails to raise DivByZero") as context1:
            a = Fraction(1, 0, 1/0)
            self.assertEqual(a.denominator, 0)
            self.assertIsInstance(a.denominator, int)
            self.assertIsInstance(a, Fraction)

    def test_default(self):
        b = Fraction()
        self.assertEqual(b.numerator, 0)
        self.assertIsInstance(b.numerator, int)
        self.assertIsInstance(b, Fraction)

    def test_oneArg(self):
        with self.assertRaises(TypeError) as context1:
            c = Fraction(3, 3, 1)

    def test_twoArg(self):
        with self.assertRaises(TypeError, msg="Cannot have in integer") as context1:
            c = Fraction(0, 1, 0)

    def test_threeArg(self):
        with self.assertRaises(TypeError, msg="Cannot have three arguments") as context1:
            c = Fraction(9, 8.5, 1)

    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="Cannot have in decimal") as context1:
            c = Fraction(1, 3, 1/3)

    def test_negDenom(self):
        with self.assertRaises(TypeError, msg="Cannot have negative denominator") as context1:
            c = Fraction(2, -3, 1)

    def test_reduced(self):
        with self.assertRaises(TypeError, msg="Need simplify") as context1:
            c = Fraction(6, 8)
            self.assertIsInstance(c.numerator, 3)
            self.assertIsInstance(c.denominator, 4)


class TestStr(unittest.TestCase):
    def test_displayfraction(self):
        a = Fraction(1, 2)
        self.assertEqual(" 1/2 ", a.__str__())

    def test_displayInt(self):
        a = Fraction(1, 2)
        self.assertIsInstance(a.numerator, int)
        self.assertIsInstance(a.denominator, int)
        self.assertEqual(" 1/2 ", a.__str__())

    def test_displayNeg(self):
        a = Fraction(1, 2)
        self.assertIsInstance(a.numerator, 1)
        self.assertIsInstance(a.denominator, 2)
        self.assertIsInstance(" 1/2 ", a.__str__())
