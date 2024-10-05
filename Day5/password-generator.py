# Generate a random password using letters, numbers and symbols.

# import random module as the password will be generated with random characters.
import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 

print("Welcome to Python Password Generator!")
# takes input from user
up_letter_choice = int(input("How many UPPERCASE letters you want? "))
lo_letter_choice = int(input("How many lowercase letters you want? "))
number_choice = int(input("How many numbers you want? "))
symbol_choice = int(input("How many special charecters you want? "))
# taking an empty list to store the password characters
password_list = []
# running a for loop for every variables to randomly generate characters, numbers and symbols
# I can either use [password_list.append(random.choice(upper_letters))]
# or can use this [password_list += random.choice(upper_letters)] both will do the same job.
for char in range(1, up_letter_choice +1):
    password_list.append(random.choice(upper_letters))

for char in range(1, lo_letter_choice +1):
    password_list.append(random.choice(lower_letters))

for char in range(1, number_choice +1):
    password_list.append(random.choice(numbers))

for char in range(1, symbol_choice +1):
    password_list.append(random.choice(symbols))

# I have all the characters but they are not shuffeled, to shuffle them use random.shuffle()
# print(password_list)
random.shuffle(password_list)
# print(password_list)

# now I have all the shuffled characters but they are in a list, to print them as a string running a for loop
password = ""
for char in password_list:
    password += char
print(f"Your Secure Password is: {password}")


# This the easy way to generate password, but here all characters will not be shuffled,
# like at first uppercase, lowercase, then number and symbols willbe printed.

# password = ""
# for char in range(1, up_letter_choice +1):
#     password += random.choice(upper_letters)

# for char in range(1, lo_letter_choice +1):
#     password += random.choice(lower_letters)

# for char in range(1, number_choice +1):
#     password += random.choice(numbers)

# for char in range(1, symbol_choice +1):
#     password += random.choice(symbols)

# print(password)