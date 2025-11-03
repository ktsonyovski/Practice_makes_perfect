
"""
This program prompts the user to enter a string and then prints progressively longer
suffixes of the string starting from the last character up to the full string.

For example, if the input is "hello", the output will be:
o
lo
llo
ello
hello
"""
input_string = input("Please type in a string: ")
index = len(input_string) - 1

while index >= 0:
    print(input_string[index:])
    index -= 1
