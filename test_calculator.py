import unittest
from calculator import *

# Partner 1 =
# Partner 2 = Ryan Esperto


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, -3), -5)
        self.assertEqual(add(20, 30), 50)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(-10, 4), -6)
        self.assertEqual(sub(20, 30), 50)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 0)


    def test_logarithm(self):
        self.assertAlmostEqual(log(10, 1000), 3)
        self.assertAlmostEqual(log(2, 8), 3)
        self.assertAlmostEqual(log(4, 16), 2)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 0)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()