import unittest
from calculator import *

#https://github.com/OTrepse/Lab10-GustavoT-RyanE
# Partner 1 = Gustavo Torres
# Partner 2 = Ryan Esperto


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(20, 30), 50)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(20, 30), -10)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual((mul(3,5),15))
        self.assertEqual(mul(4,5),20)
        self.assertEqual(mul(0,0),0)

    def test_divide(self): # 3 assertions
        with self.assertRaises(ValueError):
            div(0, 0)

        self.assertEqual(div(0, 8), 0)

        with self.assertRaises(ValueError):
            div(8, 0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            div(0, 0)


    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 1000), 3)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(4, 16), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
         # call log function inside, example:
          with self.assertRaises(ValueError):
              log(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(0, 0), 0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)

        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()