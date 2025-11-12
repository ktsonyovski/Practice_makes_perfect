'''
Program which returns the factorial of a number.
'''

def factorial_iterative(number: int) -> int:
    '''
    Iterative factorial function which takes an integer and returns it factorial.
    '''
    fact = 1
    for number in range(2, n + 1):
        fact *= number
    return fact

def factorial_recursive(number: int) -> int:
    '''
    Recursive factorial function which takes an integer and returns it factorial.
    '''
    return 1 if number == 1 else number * (factorial_recursive(number -1))

    