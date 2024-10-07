# Importing OS module to create the clear() function
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Importing random module to pick a random word from "words_hangman.py"
# Importing my custom modules 'words_hangman' and 'art_hangman' to use word_list, hangman_logo,
# and hangman_stages variables in this program.
import random
from words_hangman import word_list
from art_hangman import hangman_logo, hangman_stages

# Printing the Hangman Logo
print(hangman_logo)

# Choosing a random word from word_list and storing it's length
choosen_word = random.choice(word_list)
word_length = len(choosen_word)

# Taking a variable game_end to run the while loop and setting the lives_left to 6 as
# there are 7 element in the hangman_stages, so it will run from 0 to 6
game_end = False
lives_left = 6

# Testing the code
# print(choosen_word)

# Taking a empty variable to store the no of "_" that is equals to length of guessed word 
display = []
for _ in range(word_length):
    display += "_"

# Starting the while loop, until the game is over it will run again and again
while not game_end:
    # converting all the input letters into lowercase
    guess_letter = input("Guess a letter: ").lower()
    # evrytime loop runs, it will clear the screen
    clear()

    if guess_letter in display:
        print(f"You have already guessed the letter: {guess_letter}")
    
    for position in range(word_length):
        letter = choosen_word[position]
        if letter == guess_letter:
            display[position] = letter

    if guess_letter not in choosen_word:

        print(f"You guess: {guess_letter}, this is not in the word. You lose a life!")
        lives_left -= 1
        if lives_left == 0:
            game_end = True
            print("You Lose ")

    print(f"{' '.join(display)}")

    if "_" not in display:
        game_end = True
        print("You have Won")

    from art_hangman import hangman_stages
    print(hangman_stages[lives_left])