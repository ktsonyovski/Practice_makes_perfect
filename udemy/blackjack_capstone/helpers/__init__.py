"""Helper functions for the blackjack game"""
import json
import random
import os

def read_json(json_file: str):
    """Read json file"""
    with open(json_file, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def deal_card(player_hand: list, deck: list) -> list:
    """Get random card from deck and append it to given hand."""
    card = random.choice(deck)
    player_hand.append(card)
    return card

def calculate_score(player_hand: list) -> int:
    """Calculate hand score."""
    return sum(player_hand)


JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "resources", "deck.json")
JSON_DATA = read_json(JSON_PATH)
DECK = JSON_DATA.get("BLACKJACK_DECK")
