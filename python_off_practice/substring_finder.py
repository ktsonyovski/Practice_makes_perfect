
"""
This program prompts the user to enter a word and a character. It then searches for each
occurrence of the character in the word and prints a 3-character substring starting from
that position. The loop continues until no more valid matches are found that allow for a
3-character slice.

Example:
If the input word is "alphabet" and the character is "a", the output will be:
alp
abe
"""
input_string = input("Please type in a word: ")
input_char = input("Please type in a character: ")

index = input_string.find(input_char)

while index != -1 and index + 3 <= len(input_string):
    print(input_string[index:index+3])
    # Move past the current character to find the next occurrence
    index = input_string.find(input_char, index + 1)