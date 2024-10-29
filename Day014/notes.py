####### Steps to solve the problem. ########

# This the step 3, making it a function to remove the repetative task for account a & b
def format_data(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"

# This is step 5 (ii), making it a function as it should be reusable
def check_answer(guess, a_followers, b_followers):
    """Take the user guess and folowers count and returns if they got it right"""
    # if a_followers > b_followers and guess == "a":
    #     pass
    # elif a_followers > b_followers and guess == "b":
    #     pass
    # elif b_followers > a_followers and guess == "a":
    #     pass
    # elif b_followers > a_followers and guess == "b":
    #     pass
    # else:
    #     pass
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
# 1. Display the ASCII art
from art import logo
print(logo)

account_b = random.choice(data)
# 8. Make the game repeatable
continue_game = True
while continue_game:

    # 2. Generate a random account from the game data
    from game_data import data
    import random
    # 9. Put the 2nd position account in the first position in next round
    account_a = account_b
    # account_a = random.choice(data)
    account_b = random.choice(data)
        # (i)Compare both accounts, if they are same choose another one
    if account_a == account_b:
        account_b = random.choice(data)

        # (ii)Printing the data of account a & b
    print(f"Compare A: {format_data(account_a)}.")
        # (iii)Adding the V/S art in between two account
    from art import vs
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    # 3. Format the account data into pritable format
    # account_name = account_a["name"]
    # account_description = account_a["description"]
    # account_country = account_a["country"]
    # print(f"{account_name}, a {account_description}, from {account_country}")

    # 4. Ask user for a guess
    guess = input("Who has more followers? 'A' or 'B' ").lower()

    # 5. Check if user is correct
        # (i)Get followers count of each account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

        # (ii)Use if statement to check if user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)

    # 10. Clear the screen between every round
    import os
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')
    clear()
    print(logo)
    # 6 (i). Give user feedback on their guess
    score = 0
    if is_correct:
        # 6 (ii). Keep the score
        score += 1
        print(f"You are Right! Current Score: {score}")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Final Score: {score}")

    # 8. Make the game repeatable

    # 9. Put the 2nd position account in the first position in next round

    # 10. Clear the screen between every round