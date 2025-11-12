'''
Program which counts how many times a char is repeated in a string.
'''

def char_counter(new_char: str, new_string: str) -> int:
    '''
    Function which receives a char and a string as inputs and returns the times the char is repeated in the string.
    '''
    return new_string.count(new_char)

string_new = input("Enter a string: ")
char_new = input("Enter the char to count by: ")

print(char_counter(char_new, string_new))

