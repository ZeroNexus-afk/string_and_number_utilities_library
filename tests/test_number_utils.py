import unittest
import sys
import os

# Khai báo đường dẫn để import được file trong thư mục src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import number_utils

class TestNumberUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(number_utils.is_prime(5))
        self.assertTrue(number_utils.is_prime(11))
        self.assertFalse(number_utils.is_prime(4))
        self.assertFalse(number_utils.is_prime(1))
        self.assertFalse(number_utils.is_prime(-5))

    def test_factorial(self):
        self.assertEqual(number_utils.factorial(5), 120)
        self.assertEqual(number_utils.factorial(0), 1)
        # Test bắt lỗi khi truyền số âm
        with self.assertRaises(ValueError):
            number_utils.factorial(-1)

    def test_is_even_odd(self):
        self.assertTrue(number_utils.is_even(4))
        self.assertFalse(number_utils.is_even(5))
        self.assertTrue(number_utils.is_odd(5))
        self.assertFalse(number_utils.is_odd(4))

    def test_gcd_lcm(self):
        self.assertEqual(number_utils.gcd(48, 18), 6)
        self.assertEqual(number_utils.gcd(0, 5), 5)
        self.assertEqual(number_utils.lcm(4, 6), 12)
        self.assertEqual(number_utils.lcm(0, 5), 0)

    def test_fibonacci(self):
        self.assertEqual(number_utils.fibonacci(0), 0)
        self.assertEqual(number_utils.fibonacci(1), 1)
        self.assertEqual(number_utils.fibonacci(10), 55)
        with self.assertRaises(ValueError):
            number_utils.fibonacci(-1)

    def test_sum_of_digits(self):
        self.assertEqual(number_utils.sum_of_digits(123), 6)
        self.assertEqual(number_utils.sum_of_digits(-456), 15)
        self.assertEqual(number_utils.sum_of_digits(0), 0)

if __name__ == '__main__':
    unittest.main()
