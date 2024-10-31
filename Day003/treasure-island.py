# Treasure Island Game

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

user_choice_01 = input('''
You\'re at a crossroad.
Where do you want to go? "left" or "right"\n
''').lower()

if user_choice_01 == "left":
    user_choice_02 = input('''
    You\'ve come to a lake. 
    There is an island in the middle of the lake. 
    Type "wait" to wait for a boat.
    Type "swim" to swim across.
    ''').lower()
    if user_choice_02 == "wait":
        user_choice_03 = input("""
        You arrive at the island unharmed.
        There is a house with 3 doors.
        One 'red', one 'yellow' and one 'blue'.
        Which color do you choose?
        """).lower()
        if user_choice_03 == "red":
            print("It's a room full of fire. Game Over.")
        elif user_choice_03 == "yellow":
            print("You have found the TRESURE. You WIN.")
        elif user_choice_03 == "blue":
            print("The room is full of water. Game Over.")
        else:
            print("The door does not exist. Game Over.")
    else:
        print("The Water is full of Crocodile. Game Over.")
else:
    print("You fell into a hole. Game Over.")