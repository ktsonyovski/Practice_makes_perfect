'''
Test prime number checker function
'''
import unittest
from python_off_practice.prime_number_checker.src.prime_number_checker import is_prime

class TestIsPrime(unittest.TestCase):
    '''
    Test class which verifies the is_prime function
    '''
    def test_is_prime_with_valid_input_1(self):
        '''
        Test is_prime function with input 1
        '''
        self.assertEqual(is_prime(1), True)

    def test_is_not_prime_with_invalid_input_4(self):
        '''
        Test is_prime function with input 4
        '''
        self.assertEqual(is_prime(4), False)

    def test_is_prime_with_invalid_input_negative(self):
        '''
        Test is_prime function with negative input
        '''
        self.assertEqual(is_prime(-1), False)

    def test_is_prime_with_valid_input_5(self):
        '''
        Test is_prime function with input 5
        '''
        self.assertEqual(is_prime(5), True)

    def test_is_prime_with_valid_input_15(self):
        '''
        Test is_prime function with input 15
        '''
        self.assertEqual(is_prime(15), False)

if __name__ == "__main__":
    unittest.main()
