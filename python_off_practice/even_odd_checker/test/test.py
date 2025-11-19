
"""
Unit tests for the even_odd_checker function.

This module uses Python's unittest framework to validate the correctness of the
even_odd_checker function, which determines whether an integer is even or odd.

Test Cases Included:
--------------------
1. test_valid_even_positive_integer:
   Ensures that the function returns "Even" for an even positive integer (e.g., 2).

2. test_valid_odd_positive_integer:
   Ensures that the function returns "Odd" for an odd positive integer (e.g., 3).

Usage:
------
Run this file directly to execute all tests:
    python -m unittest python_off_practice/even_odd_checker/test/test.py

Dependencies:
-------------
- unittest (standard library)
- even_odd_checker function from python_off_practice.even_odd_checker.src.even_odd
"""

import unittest
from python_off_practice.even_odd_checker.src.even_odd import even_odd_checker


class TestEvenOddChecker(unittest.TestCase):
    '''
    Unit test class for validating the behavior of the even_odd_checker function
    '''
    
    def test_valid_even_positive_integer(self):
        '''
        Verify that even_odd_checker returns 'Even' when provided with an even positive integer (e.g., 2).
        '''
        self.assertEqual(even_odd_checker(2), "Even")

    def test_valid_odd_positive_integer(self):
        '''
        Verify that even_odd_checker returns 'Odd' when provided with an odd positive integer (e.g., 3).
        '''
        self.assertEqual(even_odd_checker(3), "Odd")

if __name__ == "__main__":
    unittest.main()
