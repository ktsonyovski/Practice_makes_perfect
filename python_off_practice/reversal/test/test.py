'''
Test function which checks the reversal functions.
'''
import unittest
from python_off_practice.reversal.src.reversal import reversal_of_string
from python_off_practice.reversal.src.reversal import reversal_of_list


class TestReversalChecker(unittest.TestCase):
    '''
    Class containing test functons checking the reversal functions.
    '''

    def test_valid_reversal_of_string(self):
        '''
        Test function which inputs the reversal of the string "hello" and checks if the function returns "olleh".
        '''
        self.assertEqual(reversal_of_string("hello"), "olleh")

    def test_valid_reversal_of_list(self):
        '''
        Test function which checks the reversal of a list and all the included strings.
        The input list is not_reversed_list = ["local", "microsoft", "windows", "apps"]
        The expected result is ['sppa', 'swodniw', 'tfosorcim', 'lacol']
        '''
        not_reversed_list = ["local", "microsoft", "windows", "apps"]
        reversed_list = ['sppa', 'swodniw', 'tfosorcim', 'lacol']
        self.assertEqual(reversal_of_list(not_reversed_list), reversed_list)

if __name__ == "__main__":
    unittest.main()