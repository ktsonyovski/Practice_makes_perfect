"""
This script prompts the user to input a word and displays it centered within a decorative frame of asterisks.

Functionality:
- Prompts the user to enter a word.
- Creates a frame of 30 asterisks to serve as the top and bottom borders.
- Centers the input word within the frame, adjusting spacing based on whether the word length is even or odd.
- Ensures the word is displayed within a 30-character wide frame, with appropriate padding on both sides.

Example Output:
If the user inputs "Hello", the output will be:
******************************
*           Hello            *
******************************
"""
input_string = input("Word: ")
frame = "*" * 30
print(frame)
if len(input_string) % 2 == 0:
    space = int((28 - len(input_string)) / 2)
    print("*" + " " * space + input_string + " " * space + "*")
else:
    space = int((27 - len(input_string)) / 2)
    print("*" + " " * space + " " + input_string + " " * space + "*")
print(frame)
