"""Blackjack Capstone Project Code"""
import random

BLACKJACK_DECK = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

def deal_card(player_hand: list) -> list:
    """Get random card from deck and append it to given hand."""
    card = random.choice(BLACKJACK_DECK)
    player_hand.append(card)
    return card

def calculate_score(player_hand: list) -> int:
    """Calculate hand score."""
    return sum(player_hand)


def game():
    """Game logic"""
    print("BlackJack game.")
    dealer_hand = []
    player_hand = []
    continue_game = True

    deal_card(dealer_hand)
    deal_card(player_hand)
    deal_card(player_hand)
    print(f"The dealer hand is showing: {dealer_hand}")
    print(f"You have: {player_hand}")
    player_score = calculate_score(player_hand)

    while continue_game:
        user_choice= input("What do you want to do: ").lower()

        if user_choice == "pass":
            print(f"You have {player_score}")
            continue_game = False
        else:
            new_card = deal_card(player_hand)
            player_score = calculate_score(player_hand)
            if player_score > 21:
                print(f"You lose, bust! {player_score}")
                continue_game = False
            print(f"You got {new_card}")
            print(f"your new score is {player_score}")
    dealer_score = calculate_score(dealer_hand)

    while dealer_score < 17:
        deal_card(dealer_hand)
        dealer_score = calculate_score(dealer_hand)

    if player_score <= 21:
        if dealer_score > 21:
            print(f"You win, dealer is a bust {dealer_score}")
        elif dealer_score == player_score:
            print(f"Draw, got: {player_score} and {dealer_score}")
        elif player_score > dealer_score:
            print(f"Win {player_score}, {dealer_score}")
        else:
            print(f"Lose {player_score}, {dealer_score}")

game()
