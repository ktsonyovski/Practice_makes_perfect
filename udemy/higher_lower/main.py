"""Higher lower game code file."""
from helpers import game_loop, win_logic

def game():
    """Game docstring"""
    print("🎉 Welcome to the Higher Lower Game! 🎉")
    print("Guess who has more Instagram followers!\n")

    lives = 3
    score = 0
    while lives:
        first_person, second_person = game_loop()
        print(f"❤️ You have {lives} lives remaining!")
        print("="*80)
        user_guess = input("Who has more followers? Choose A or B: ").strip().lower()
        score += 1
        lives = win_logic(user_guess, first_person, second_person, lives)

    print("💔 Out of lives! Game Over.")
    print(f"🏆 Your final score: {score} points")

if __name__ == "__main__":
    game()
