### if-else, if-elif-else statement ###

# 1. Write a program that takes height input from user and if condition matches print they can ride
# else print they cann't ride
print("Welcome to rollercoster!")
height = int(input("What's your height in cm? "))

# checking the heigth if height>120 print the if block 
# otherwise print the else block
# we have a nested if-elif-else block under the if block
if height >= 120:
    print("You can ride rollercoster ;)")
    age = int(input("What's your age? "))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 & age < 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride :(")


# 2. Write a program that works out whether if a given number is an odd or even number.
number = int(input("Enter a number to check odd or even: "))

# if the remainder is 0, that means it is even as it can be devided by 2
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")


# 3. Write a program that works out whether if a given year is leap year.
year = int(input("Which year you want to check? "))
if year % 4 == 0 & year % 100 == 0 | year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")

# we can write it as a nested if loop as well
# year = int(input("Which year you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is leap year")
#         else:
#             print(f"{year} is not leap year")
#     else:
#         print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

