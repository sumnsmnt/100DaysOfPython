##### Funtions #####

# Create a function called greet(). Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
    print("Hello")
    print("World")
    print("Welcome")

greet()

# Functions that allow for input
def greet_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}?")

greet_name("Suman")

# Functions with more than one input
def greet_user(name, location):
    print(f"Hello {name}")
    print(f"What's the weather today at {location}?")

# greet_user("Suman", "Kolkata")
# greet_user("Kolkata", "Suman")

# Functions with keyword arguments
greet_user(location="Kolkata", name="Suman")


# 1. You are painting a wall. The instructions on the paint can says that 1 can of paint 
# can cover 5 square meters of wall. Given a random height and width of wall.
# Calculate how many cans of paint you'll need to buy. Result should be round up.
# number of cans = (wall height * wall width) / coverage per can

import math

def total_paints_can(height, width, cover):

    total_area = height * width
    number_of_cans = math.ceil(total_area / cover)
    print(f"You will need {number_of_cans} cans of paint to cover {total_area} sq.m. of area")

height_need = int(input("Enter height of the wall in m: "))
width_need = int(input("Enter width of the wall in m: "))
coverage = 5
total_paints_can(height=height_need, width=width_need, cover=coverage)


# 2. Check a number is prime or not
def prime_check(number):
    is_prime = True
    for num in range(2, number):
        if number % num == 0 :
            is_prime = False
    if is_prime:
        print(f"{number} is a Prime Number")
    else:
        print(f"{number} is not a Prime Number")


n = int(input("Check this number is prime or not? "))
prime_check(number=n)
