'''
Test function which checks the Even/Odd checker function
'''
import unittest
from python_off_practice.even_odd_checker.src.even_odd import even_odd_checker


class TestEvenOddChecker(unittest.TestCase):
    '''
    Test class of functions which test the even odd checker function.
    '''
    
    def test_valid_even_positive_integer(self):
        '''
        Test case checking the Even/Odd function with input "2" and expecting output "Even"
        '''
        self.assertEqual(even_odd_checker(2), "Even")

    def test_valid_odd_positive_integer(self):
        '''
        Test case checking the Even/Odd function with input "3" and expecting output "Odd"
        '''
        self.assertEqual(even_odd_checker(3), "Odd")

if __name__ == "__main__":
    unittest.main()
