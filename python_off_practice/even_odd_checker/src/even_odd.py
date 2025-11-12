'''
Program which receives an integer number and returns if it is even or odd.
'''

def even_odd_checker(number: int) -> str:
    '''
    Function which receives an integer number and returns even or odd string, depending on the input.
    '''
    return "Even" if number % 2 == 0 else "Odd"

new_num = int(input("Enter a number: "))
print(even_odd_checker(new_num))