# Day 7 of 100 Days of Python

**What I learn today:**
* Nested Loops (if-else, for, while)
* Module (builtin and custom)

**Project:**
* HANGMAN Game

**What the program does:**


**Flow of the program:**
(1)Start -> (2)Generate a random word -> (3)Generate as many blanks as letters in the word ->
(4)Ask the user to guess a letter -> (5)Is the guessed letter present in the word?
=> Yes -> replace the blank with the letter -> all the blanks filled? 
    => No -> (4)ask the user to guess a letter
    => Yes -> Game Over(exit)
=> No -> lose a life -> have they run out of life
    => No -> (4)ask the user to guess a letter
    => Yes -> Game Over(exit)