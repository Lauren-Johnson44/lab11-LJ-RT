# https://github.com/Lauren-Johnson44/lab11-LJ-RT.git
# Partner 1: Lauren Johnson
# Partner 2: Re'Niyah Tape

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,5), 10)
        self.assertEqual(add(3, -7), -4)
        self.assertEqual(add(-3, -6), -9)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,2), 2)
        self.assertEqual(subtract(123, 123), 0)
        self.assertEqual(subtract(-3, -2), -1)



    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(7, 5), 35)
        self.assertEqual(mul(-3, 8), -24)
        self.assertEqual(mul(-2, -9), 18)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(7, 21), 3)
        self.assertEqual(div(-4, 44), -11)
        self.assertEqual(div(-5, -100), 20)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0,5)




    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(3, 3), 1)
        self.assertEqual(logarithm(4,16),2)
        self.assertAlmostEqual(logarithm(10, 1000), 3)


    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 3)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(6.3, 8.4), 10.5)
        self.assertEqual(hypotenuse(6, -8), 10)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        with self.assertRaises(ValueError):
           square_root(-111)

    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()