"""Docstring"""
import os
import json
import random

# General data
JFILE = os.path.join(os.path.dirname(__file__),\
                    '..', 'resources', 'game_data.json')

with open(JFILE, "r", encoding="utf-8") as file:
    data = json.load(file)

FAMOUS_PEOPLE_LIST = data["data"]

def select_random_person_data() -> dict:
    """Selects random person from game_data.json file"""
    chosen_person = random.choice(FAMOUS_PEOPLE_LIST)
    return chosen_person

def fetch_specific_data(person: dict, key: str):
    """Fetches person key data"""
    return person[key]

def game_loop():
    """Docnstring"""
    first_person = select_random_person_data()
    second_person = select_random_person_data()

    if first_person == second_person:
        second_person = select_random_person_data()

    first_name = fetch_specific_data(first_person, "name")
    first_occupation = fetch_specific_data(first_person, "description")
    first_country = fetch_specific_data(first_person, "country")

    second_name = fetch_specific_data(second_person, "name")
    second_occupation = fetch_specific_data(second_person, "description")
    second_country = fetch_specific_data(second_person, "country")

    print("🤔 Who has more followers from these two celebrities?")
    print(f"👤 A: {first_name} - a {first_occupation} from {first_country}")
    print(f"👤 B: {second_name} - a {second_occupation} from {second_country}")
    print()

    return first_person, second_person

def win_logic(user_guess: str,
            first_person: dict,
            second_person: dict,
            lives: int) -> int:
    """Determine win logic"""
    first_name = fetch_specific_data(first_person, "name")
    second_name = fetch_specific_data(second_person, "name")
    first_fw_count = fetch_specific_data(first_person, "follower_count")
    second_fw_count = fetch_specific_data(second_person, "follower_count")

    if user_guess == "a":
        if first_fw_count > second_fw_count:
            print("🎉 Correct!")
            print(f"{first_name} has more followers ({first_fw_count}M vs {second_fw_count}M)")
        else:
            print("❌ Wrong!")
            print(f"{first_name} has fewer followers ({first_fw_count}M vs {second_fw_count}M)")
            lives -= 1
    elif user_guess == "b":
        if first_fw_count > second_fw_count:
            print("❌ Wrong!")
            print(f"{second_name} has fewer followers ({second_fw_count}M vs {first_fw_count}M)")
            lives -= 1
        else:
            print("🎉 Correct!")
            print(f"{second_name} has more followers ({second_fw_count}M vs {first_fw_count}M)")
    return lives
