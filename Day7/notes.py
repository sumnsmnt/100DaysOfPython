# #################### STEP 1 ####################

# word_list = ["suman", "india", "world", "python"]

# # ToDo 1 - Randomly choose a word from the 'word_list' and assign it to a 
# # variable called 'choosen_word'.
# import random 
# choosen_word = random.choice(word_list)

# # ToDo 2 - Ask the user to guess a letter and assign their answer to a variable 
# # called 'guess_letter'. Make 'guess_letter' lowercase.
# guess_letter = input("Guess a letter: ").lower()

# # ToDo 3 - Check if the the letter user guess is one of the letters in the 'choosen_word'.

# for letter in choosen_word:
#     if letter == guess_letter:
#         print("letter found")
#     else:
#         print("letter not found")

# # testing the code
# print(choosen_word)


#################### STEP 2 ####################

# import random 
# word_list = ["suman", "india", "world", "python"]
# choosen_word = random.choice(word_list)

# # Testing the code
# print(choosen_word)

# guess_letter = input("Guess a letter: ").lower()

# # ToDo 1 - Create an empty list called 'display'. For each letter in the 'choosen_word',
# # add a "_" into the 'display' variable.
# # If the 'choosen_word' was "suman", 'display' should be ["_","_","_","_","_"] with 5 "_" 
# # representing each letter to guess.
# word_length = len(choosen_word)
# display = []
# # for letter in choosen_word:
# #     display.append("_")
# # print(display)
# for _ in range(word_length):
#     display += "_"
# print(display)

# # ToDo 2 - Loop through each position in the 'choosen_word'. If the letter at that position
# # matches 'guess_letter' then reveal that letter in the 'display' variable at that position.
# # e.g. If the user guess "m" and the choosen_word is "suman", then 'diplay' should be
# # ["_","_","m","_","_"]

# # for letter in choosen_word:
# #     if letter == guess_letter:
# #         print(letter, end=" ")
# #     else:
# #         print("_", end=" ")

# for position in range(word_length):
#     letter = choosen_word[position]
#     if letter == guess_letter:
#         display[position] = letter

# # ToDo 3 - Print display and you should see the guessed letter in the correct position and 
# # every other letter replaced with "_"
# print(display)


#################### STEP 3 ####################

# import random 
# word_list = ["suman", "india", "world", "python", "apple", "eye", "abracadabra"]
# choosen_word = random.choice(word_list)
# word_length = len(choosen_word)

# # Testing the code
# print(choosen_word)

# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# # ToDo 1 - Use a while loop to let the user guess again. The loop should only stop
# # once the user guess all the letters in the 'choosen_word' and 'display' has no more 
# # blanks ("_"). Then you can tell the user they have won.

# game_end = False
# while not game_end:
#     guess_letter = input("Guess a letter: ").lower()

#     # Chcek guessed letter
#     for position in range(word_length):
#         letter = choosen_word[position]
#         if letter == guess_letter:
#             display[position] = letter
#     print(display)

#     if "_" not in display:
#         game_end = True
#         print("You have Won")


# #################### STEP 4 ####################

# hangman_stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''','''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''']


# import random 
# word_list = ["suman", "india", "world", "python", "apple", "eye", "abracadabra"]
# choosen_word = random.choice(word_list)
# word_length = len(choosen_word)

# # ToDo 1 - Create a variable called 'lives_left' to keep track of the number of lives left.
# # Set 'lives_left' equals to 7.

# lives_left = 6
# print(type(lives_left))
# # Testing the code
# print(choosen_word)

# # Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"


# game_end = False
# while not game_end:

#     guess_letter = input("Guess a letter: ").lower()

#     # Chcek guessed letter
#     for position in range(word_length):
#         letter = choosen_word[position]
#         if letter == guess_letter:
#             display[position] = letter
#     print(display)

#     # ToDo 2 - If guess is not a letter in the 'choosen_word', then reduce 'lives_left' by 1.
#     # if 'lives_left' goes down to 0 then the game should stop and print "You Lose"

#     if guess_letter not in choosen_word:
#         lives_left -= 1
#         if lives_left == 1:
#             game_end = True
#             print("You Lose ")

#     # Join all the elements in the list and turn it into a String

#     if "_" not in display:
#         game_end = True
#         print("You have Won")
#     # ToDo 3 - Print the ASCII art from 'hangman_stages' that corresponds to the current number of
#     # 'lives_left' for  the user.
#     print(hangman_stages[lives_left])


#################### STEP 5 ####################

import random 

# Deleting the variable list, where I stored all the names.
# word_list = ["suman", "india", "world", "python", "apple", "eye", "abracadabra"]

# ToDo 1 - Update the word list to use the word_list from words_hangman.py.
# import words_hangman
# choosen_word = random.choice(words_hangman.word_list)
from words_hangman import word_list
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

# ToDo 3 - Import the logo from art_hangman.py and print it at the start of the game.

from art_hangman import hangman_logo
print(hangman_logo)

game_end = False
lives_left = 6

# Testing the code
print(choosen_word)

# Create blanks
display = []
for _ in range(word_length):
    display += "_"


while not game_end:

    guess_letter = input("Guess a letter: ").lower()

    # ToDo 4 - If the user has entered aletter they have already guessed, print the letter
    # and let them know.
    if guess_letter in display:
        print(f"You have already guessed the letter: {guess_letter}")
    
    # Chcek guessed letter
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess_letter:
            display[position] = letter
    print(display)


    if guess_letter not in choosen_word:
        # ToDo 5 - If the letter is not in the choosen_word, print out the letter and 
        # let them know it's not in the word.
        print(f"You guess: {guess_letter}, this is not in the word. You lose a life!")
        lives_left -= 1
        if lives_left == 0:
            game_end = True
            print("You Lose ")

    # Join all the elements in the list and turn it into a String
    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("You have Won")
    # ToDo 2 - Import the stages from art_hangman.py 
    from art_hangman import hangman_stages
    print(hangman_stages[lives_left])