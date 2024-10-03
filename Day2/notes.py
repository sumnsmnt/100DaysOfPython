### Data Types ###

# String Data Type
print("123" + "321")

# Integer Data Type
print(123 + 321)

# Floting Point Data Type
print (1.23 + 12.3)

# Boolean Data Type
a = 2
print(a == 2)


### Type Error, Type Checking and Type Conversion ###

name_char = len(input("What is your name? "))
print(type(name_char))
new_name_char = str(name_char)
print("Your name has " + new_name_char + " characters")
print(type(new_name_char))
# Here I store the input value inside new_char variable, the input is string but I use len() 
# function that is interger data type. We can not concatinate integer data types with 
# string data types. That's why I convert the integer data type to string data type.
# To check data type we use type() function

# 1. Write a program that adds the digits in a 2 digit number. e.g. if the input is 49,
# then the output should be 4+9 = 13
number = input("Enter a 2 digit number: ")
first_digit = int(number[0])
second_digit = int(number[1])
result = first_digit+second_digit
print(result)
# we are taking a string input from user then substring it into 2 parts, then converting them
# into integer data type. At last add both variable inside result variable and print it.


### Mathematical Calculation ###
# The order of calculation ==> (), **, * /, + - [PEDMAS rule] 
# the calcualtion goes always from left to right.

# data type is float when we devide and prints actual number
print(11 / 3)
# data type is float when we use round() function and prints rounded number mentioned in
# the the line as here it will print upto 3 decimal points
# if we don't mention anything it will print whole number closest to the actual result.
print(round(11 / 3, 3))
# data type is int when we use // and it prints whole number
print(11 // 3)

### f - Strings ###
name = input("What is your name? ")
city = input("Where do you live? ")
age = int(input("How old are you? "))
future_age = age + 10
isStudent = True
print(f"Hi {name}, your are from {city}, currently you are {age} years old but after 10 years your age will be {future_age}, and you are student is {isStudent}")


# 2. Create a program using maths and f-Strings that tells us how many days, weeks, months
# we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# You have x days, y weeks, and z months left.
# Where x, y and z are the actual calculated numbers.
current_age = int(input("What is your age: "))
years_left = 90 - current_age
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months")