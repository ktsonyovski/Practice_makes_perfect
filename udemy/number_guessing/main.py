"""Main module for the number guessing game.
This module serves as the entry point for the game,
utilizing helper functions from the game_utils module.
"""
import game_utils as gu  # pylint: disable=import-error

def number_guessing_game(custom_number: int) -> str:
    """Run a complete number guessing game session.

    Args:
        custom_number (int): The upper limit for the random number range.

    Returns:
        str: The result message indicating win or loss.
    """
    random_number = gu.generate_random_number(custom_number)
    print(f"I'm thinking of a number between 1 and {custom_number}")

    valid_difficulty = False
    while not valid_difficulty:
        difficulty = input("Select difficulty (easy/hard): ").lower()
        if difficulty in ["easy", "hard"]:
            valid_difficulty = True
        else:
            print("Please choose 'easy' or 'hard'.")
    lives = gu.select_difficulty(difficulty)

    print(f"You have {lives} attempts to guess the number!")
    guess = gu.get_valid_guess("Make a guess: ")

    return gu.guess_number(lives=lives, guess=guess, number=random_number)

if __name__ == "__main__":
    RESULT = number_guessing_game(100)
    print(RESULT)
