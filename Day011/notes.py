########## Black Jack Game Rules ##########

# The deck is unlimitted in size
# There is no jokers
# The Jack/King/Queen all counts as 10
# The Accan count as 11 or 1
# Use the following list as the deck of cards
# [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn
# Cards are not removed from the deck as they are drawn



# Todo 1: Create a deal_card() function that uses the list below to return
# a random card. 11 is the Ace.

import random

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# Todo 3: Create a function called calculate_score() that takes a 
# List of cards as input and returns the score.

def calculate_score(cards):
    """Take a list of cards and return the the score calculated from the cards"""
    # return sum(cards)

    # Todo 4: Inside calculate_score() check for a blackjack 
    # (a hand with only 2 cards: ace + 10) and return 0 instead of 
    # the actual score. 0 will represent a blackjack in the game.

    # if 11 in cards and 10 in cards and len(cards) == 2:
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    # Todo 5: Inside calculate_score() check for an Ace(11). If the
    # score is alread over 21, remove the 11 and replace it with 1.

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Todo 10: Create a function called compare() and pass in the user_score and
# computer_score. If the computer and user both have the same score,
# then it's draw. If the computer has a blackjack (0), then the user
# loses. If the user has a blackjack (0), then the user wins. If the
# user_score is over 21, then the user loses. if the computer_score
# is over 21, then the computer loses. If none of the above, then the
# player with the highest score wins.

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose"
    elif user_score == 0:
        return "You Win"
    elif user_score > 21:
        return "Score more than 21, You Lose"
    elif computer_score > 21:
        return "opponent's score more then 21, You Win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You Lose"

def play_game():
    # Todo 2: Deal he user and computer 2 cards each usinhg deal_card()
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Todo 8: The score will need to be rechecked with every new card
    # drawn and the steps in 'Todo 6' need to be repeated until the game ends.

    while not is_game_over:

        # Todo 6: Call calculate_score(). if the computer or the user has
        # a blackjack (0) or if the user's score is over 21, then the game ends.

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer cards: {computer_cards[0]}")

        # Todo 7: If the game has not ended, ask the user if they want to draw
        # another card. If yes, then use the deal_card() function to add 
        # another card to the user_cards list. If no, then the game has ended.

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Todo 9: Once the user is done and no longer wants to draw more more
    # cards, it's time to let the computer play. The computer should keep
    # drawing cards as long as it has a score less than 17.
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} and final score: {user_score}")
    print(f"Opponenet's final hand: {computer_cards} and final score: {computer_score}")
    print(compare(user_score, computer_score))

# Todo 11: Ask the user if they want to restart the game. if they answer
# 'yes', clear the console and start a new game of blackjack and
# show the logo of the game.

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while input("Do you want to play Backjack Game? Type 'y' or 'n': ") == "y":
    logo = """ 
.------.              _     _            _    _            _    
|A_  _ |             | |   | |          | |  (_)          | |   
|( \/ ).-----.       | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |       | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |       | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |       |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                              _/ |                
      `------'                             |__/          
"""
    clear()
    print (logo)
    play_game()


