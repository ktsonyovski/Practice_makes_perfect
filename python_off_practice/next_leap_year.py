"""
This program finds the next leap year after a user-provided year.

How it works:
1. The user enters a year as an integer.
2. The program starts from the following year and checks each subsequent year.
3. It uses the standard leap year rule:
     - A year is a leap year if it is divisible by 4,
       except for years that are divisible by 100,
       unless they are also divisible by 400.
4. The loop stops when the next leap year is found.
5. The program then prints the next leap year after the input.

Example:
    Input: 2023
    Output: The next leap year after 2023 is 2024
"""

year_input = int(input("Year: "))
next_year = year_input

while True:
    next_year += 1
    if (next_year % 4 == 0 and next_year % 100 != 0) or (next_year % 400 == 0):
        break

print(f"The next leap year after {year_input} is {next_year}")
