'''
Program which receives an input string and reverses it.
'''

def reversal_of_string(new_string: str) -> str:
    '''
    Function which receives an input string and returns the reversal of that string.
    '''
    return new_string[::-1]

def reversal_of_list(new_list: list) -> list:
    '''
    Function which receives an input list and returns the reversal of that list and all the reversed strings inside.
    '''
    rev_new_list = [reversal_of_string(item) for item in new_list]
#    for item in new_list:
#        rev_new_list.append(reversal_of_string(item))
    return rev_new_list[::-1]

#not_reversed_string = input("Enter a string: ")
#print(reversal_of_string(not_reversed_string))

not_reversed_list = ["local", "microsoft", "windows", "apps"]
print(reversal_of_list(not_reversed_list))