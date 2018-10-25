import unittest
from calc import *

class Test_Calc(unittest.TestCase):

    def setUp(self):
        self.calc = calculator()

    def tearDown(self):
        pass

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(4, 5), 9)
        self.assertEqual(self.calc.add(1, 4), 5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(7, 5), 2)
        self.assertEqual(self.calc.subtract(4, 4), 0)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(1, 5), 5)
        self.assertEqual(self.calc.multiply(4, 2), 8)
        self.assertEqual(self.calc.multiply(5, 4), 20)

    def test_division(self):
        self.assertEqual(self.calc.division(5, 2), 2.5)
        self.assertEqual(self.calc.division(5, -3), -(5 / 3))
        self.assertRaises(ValueError, self.calc.division, 5, 0)