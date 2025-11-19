"""
Unit tests for the factorial function.

This module uses Python's unittest framework to validate the correctness of the
factorial function, which receives an integer and returns the factorial of that integer.

Test Cases Included:
--------------------
1. test_factorial_iterative_valid_integer:
   Ensures that the function returns 120 for a positive integer (e.g., 5).

2. test_factorial_recursive_valid_integer:
   Ensures that the function returns 120 for a positive integer (e.g., 5).

Usage:
------
Run this file directly to execute all tests:
    python -m unittest python_off_practice/factorial/test/test.py

Dependencies:
-------------
- unittest (standard library)
- factorial_iterative function from python_off_practice.factorial.src.factorial
- factorial_recursive function from python_off_practice.factorial.src.factorial
"""

import unittest
from python_off_practice.factorial.src.factorial import factorial_iterative
from python_off_practice.factorial.src.factorial import factorial_recursive


class TestFactorial(unittest.TestCase):
    '''
    Unit test class for validating the behavior of the factorial function
    '''
    
    def test_factorial_iterative_valid_integer(self):
        '''
        Verify the factorial_iteratice function returns 120 when provided with a valid positive integer (e.g., 5)
        '''
        self.assertEqual(factorial_iterative(5), 120)

    def test_factorial_recursive_valid_integer(self):
        '''
        Verify the factorial_recursive function returns 120 when provided with a valid positive integer (e.g., 5)
        '''
        self.assertEqual(factorial_recursive(5), 120)


if __name__ == "__main__":
    unittest.main()