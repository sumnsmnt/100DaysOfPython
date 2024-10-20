import random

print("Welcome to Number Guessing Game!")
print("Guess the number which is between 1 and 100")

easy_level = 10
hard_level = 5

# Choosing a random number between 1 and 100
answer = random.randint(1, 100)


# Function to check user's guess against actual answer.
def check_answer(guess, answer):
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print(f"You guess it right. The number is {answer}")

# Make function to set difficulty
def set_difficulty():
    level = input("Choose the dificulty level. 'easy' or 'hard' ")
    if level == "easy":
        return easy_level
    elif level == "hard":
        return hard_level
    else:
        print("Please choose a correct option")

attampts = set_difficulty()
print(f"You have {attampts} attampts left to guess the game.")

# Let the user guess a number.
guess = int(input("Make a guess: "))

check_answer(guess, answer)