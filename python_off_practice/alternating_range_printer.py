
"""
Alternating Range Printer

This program prompts the user to enter a positive integer and then prints
all integers from 1 up to that number in an alternating pattern:
starting from the lowest and highest ends of the range and moving inward.

Example:
If the user enters 7, the output will be:
1
7
2
6
3
5
4

This creates a visually interesting zigzag pattern between the two ends of the range.
"""

number = int(input("Please type in a number: "))

low = 1
high = number

while low <= high:
    print(low)
    if low != high:
        print(high)
    low += 1
    high -= 1