# Take both person's name and check for the number of times the letter in the word TRUE occures.
# Then check for the number of times the letters in the word LOVE occures.
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is x, you go together like coke and mentos."
# For love scores between 30 and 60, the message should be:
# "Your score is y, you are alright together."
# Otherwise, the message will be: "Your score is z."

'''
print("Welcome to the Love Calculator :)")
print("Your destiny is now on my hand ;p")

name1 = input("Enter your name ")
name2 = input("Enter your partner's name ")

your_name = name1.lower()
partner_name = name2.lower()

name1_char1 = your_name.count("t") + your_name.count("r") + your_name.count("u") + your_name.count("e")
name1_char2 = your_name.count("l") + your_name.count("o") + your_name.count("v") + your_name.count("e")

name2_char1 = partner_name.count("t") + partner_name.count("r") + partner_name.count("u") + partner_name.count("e")
name2_char2 = partner_name.count("l") + partner_name.count("o") + partner_name.count("v") + partner_name.count("e")

true_love1 = str(name1_char1 + name2_char1)
true_love2 = str(name1_char2 + name2_char2)

result = int(true_love1+true_love2)

if result < 10 and result > 90:
    print("You are like mentos")
elif result >= 30 and result < 50:
    print("You are alright together")
else:
    print("Your score is: ", result)
    
'''
# in the above code, I first conver both names into lower case, then take another variable and
# inside that I have calculated no of times "t","r","u" and "e" occours and add their counts.
# Same thing did for "l","o","v" and "e" for both names.
# Then I converted the data type into string and concatinate them.
# after that again I converted it into int to check conditions in a if-elif-else loop.

# Now see another approch to solve the problem, that is more readable

print("Welcome to the Love Calculator :)")

name1 = input("Enter your name ")
name2 = input("Enter your partner's name ")

# Concatinate both name and use lower() function to make all the letter lowercase
combined_string = name1 + name2
lower_case_string = combined_string.lower()

# Checking the whole string to find out total no of times t, r, u, e occours
t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

# all above values are interger so, adding them into true variable
true = t + r + u + e

# Checking the whole string to find out total no of times l, o, v, e occours
l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

# all above values are interger so, adding them into love variable
love = l + o + v + e

# at first converting both int value into string and concatinating them, later converting them into int
love_score = int(str(true) + str(love))

# checking the conditions using if-elif-else loop
if love_score < 10 and love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 30 and love_score < 70:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")