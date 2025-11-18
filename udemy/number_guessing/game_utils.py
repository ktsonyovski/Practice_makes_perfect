"""Utility functions for the number guessing game.
This module provides functions to generate a random number,
select difficulty, and handle the guessing logic.
"""
import random

def generate_random_number(custom_range: int = 100) -> int:
    """Generate a random integer between 1 and the specified custom range.

    Args:
        custom_range (int): The upper limit for the random number generation. Defaults to 100.

    Returns:
        int: A random integer between 1 and custom_range (inclusive).
    """
    if isinstance(custom_range, int) and custom_range > 1:
        return random.randint(1, custom_range)

    raise ValueError("The range must be an integer greater than 1")

def select_difficulty(setting: str) -> int:
    """Select the number of attempts based on difficulty level.

    Args:
        setting (str): The difficulty level chosen by the user.

    Returns:
        int: Number of attempts allowed (10 for 'easy', 5 for others).
    """
    return 10 if setting.lower() == "easy" else 5

def get_valid_guess(prompt: str) -> int:
    """Get a valid integer input from the user.

    Args:
        prompt (str): The prompt message to display.

    Returns:
        int: A valid integer entered by the user, or 0 if input is invalid.
    """
    valid_input = False
    while not valid_input:
        try:
            user_input = int(input(prompt))
            valid_input = True
            return user_input
        except ValueError:
            print("Please enter a valid number!")
    return 0

def guess_number(lives: int, guess: int, number: int) -> str:
    """Handle the guessing loop for the number guessing game.

    Args:
        lives (int): Number of attempts remaining.
        guess (int): The player's current guess.
        number (int): The target number to guess.

    Returns:
        str: Win message if correct, "Out of lives!" if attempts exhausted.
    """
    while lives > 1:
        if guess == number:
            return f"You got it! {guess}"

        if guess > number:
            print("Too high!")
        else:
            print("Too low!")
        lives -= 1
        print(f"Tries left: {lives}")
        guess = get_valid_guess("Guess again: ")
    return f"Out of lives! The number was {number}."
