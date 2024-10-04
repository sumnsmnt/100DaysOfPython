# Create a Rock Paper Scissors Game and play with computer.

# Rock
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


add_image = [rock, paper, scissors]
import random

user = int(input("What you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user >= 3 or user < 0:
    print("You have typed an invalid number, You Lose.")

computer = random.randint(0, 2)

print(f"You choose {add_image[user]}")
print(f"Computer choose {add_image[computer]}")


if user == 2 and computer == 0:
    print(f"You Lose :(")
elif user == 0 and computer == 2:
    print(f"You Win :)")
elif computer > user:
    print(f"You Lose :(")
elif user > computer:
    print(f"You Win :)")
else:
    print("Match Tied")

