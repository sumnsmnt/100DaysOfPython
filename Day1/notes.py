# Here print() is a function and "Hello World" is a string
print("Hello World")

# 1. Write a program that prints the same as mentioned below
# Day 1 - Python Print Function
# The function is declared like this:
# print('what to print')
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")


### String Manipulation ###

print("Hello \n Suman \n How \n Are \n You?")
# \n creates a new line. So, the words after \n will be printed on the next line.

print("Hello" + "Suman")
print("Hello" + " " + "Suman")
# + is basically concatinating strings. So whatever i write inside "" this is considered as string
# and + is doing concatination of those strings.

# 2. Write a program that prints the same as mentioned below
# Day 1 - String Manipulation
# String Concatination is done with the "+" sign.
# e.g. print("Hello" + "World")
# New lines can be created with a backslash and n.
print("Day 1 - String Manipulation")
print('String Concatination is done with the "+" sign.')
print('e.g. print("Hello" + "World") \nNew lines can be created with a backslash and n.')


name = input("What's your name? ")
# Here input() is a funtion, inside input("") we give a prompt for the user.
# and I'm storing the input that is given by user inside a variable called name.

print("Hello " + input("What's your name? "))
# input() will get the input from the user
# then print() will print the word "Hello" and the user input

# 3. Print the no of characters in your name
# example if I give the input as "Suman" then it should print 5
name = input("What's your name? ")
name_length = str(len(name))
print("Your name has " + name_length + " characters")

# 4. Write a program that switches the values stored in the variables a and b
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")
c = b
b = a
a = c
print("After swapping the values of a & b")
print("a: ",a)
print("b: ",b)