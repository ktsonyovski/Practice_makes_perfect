"""
Unit tests for the prime_number_checker function.

This module uses Python's unittest framework to validate the correctness of the
prime_number_checker function, which determines whether an integer is prime.

Test Cases Included:
--------------------
1. test_is_prime_with_valid_input_1:
   Ensures that the function returns "True" for a positive integer (e.g., 1).

2. test_is_not_prime_with_invalid_input_4:
   Ensures that the function returns "False" for a positive integer (e.g., 4).

3. test_is_prime_with_invalid_input_negative:
   Ensures that the function returns "False" for a negative integer (e.g., -1).

4. test_is_prime_with_valid_input_5:
   Ensures that the function returns "True" for a negative integer (e.g., 5).

5. test_is_prime_with_valid_input_15:
   Ensures that the function returns "False" for a negative integer (e.g., 15).

Usage:
------
Run this file directly to execute all tests:
    python -m unittest python_off_practice/prime_number_checker/test/test.py

Dependencies:
-------------
- unittest (standard library)
- prime_number_checker function from python_off_practice.prime_number_checker.src.prime_number_checker
"""

import unittest
from python_off_practice.prime_number_checker.src.prime_number_checker import is_prime

class TestIsPrime(unittest.TestCase):
    '''
    Unit test class for validating the behavior of the is_prime function
    '''
    def test_is_prime_with_valid_input_1(self):
        '''
        Verify the is_prime function returns True when provided with a valid positive integer (e.g., 1)
        '''
        self.assertEqual(is_prime(1), True)

    def test_is_not_prime_with_invalid_input_4(self):
        '''
        Verify the is_prime function returns False when provided with a valid positive integer (e.g., 4)
        '''
        self.assertEqual(is_prime(4), False)

    def test_is_prime_with_invalid_input_negative(self):
        '''
        Verify the is_prime function returns False when provided with a valid negative integer (e.g., -1)
        '''
        self.assertEqual(is_prime(-1), False)

    def test_is_prime_with_valid_input_5(self):
        '''
        Verify the is_prime function returns True when provided with a valid positive integer (e.g., 5)
        '''
        self.assertEqual(is_prime(5), True)

    def test_is_prime_with_valid_input_15(self):
        '''
        Verify the is_prime function returns False when provided with a valid positive integer (e.g., 15)
        '''
        self.assertEqual(is_prime(15), False)

if __name__ == "__main__":
    unittest.main()
