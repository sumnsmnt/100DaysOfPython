
def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the user guess and folowers count and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
from art import logo
from game_data import data
import random
from art import vs

print(logo)

score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? 'A' or 'B' ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    clear()
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You are Right! Current Score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final Score: {score}")