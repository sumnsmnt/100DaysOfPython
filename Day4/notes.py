##### MODULE #####

# Importing the random module
import random
# So I build my own module my_module.py and then importing my_module
import my_module

# Calling the random module to print random integer numbers between 1 to 10
random_integer = random.randint(1, 10)
print(random_integer)

# Calling the random module to print random integer, by default it prints between 0 to 1 (upto 0.99999...)
random_float = random.random()
print(random_float)

# Calling my custom module called my_module
print(my_module.pi)
print(my_module.name)
print(my_module.role)


# 1. Write a virtual coin toss program, that will randomly tell the user "Heads" or "Tails"
import random
random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# I can use random module to generate a random love score
love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

##### LISTS #####

fruits = ["apple", "banana", "mango"]
fruits[0] = "coconut"
fruits.extend(["guava", "cherry"])
fruits.append("pineapple")
print(fruits)


# 1. Write a program which will select a random name from a list of names. The person selected 
# will pay the bill.
import random

name_string = input("Enter everyone's names, seperated by a coma(,) \n")
# as I take the name input separated by coma, it's easy to split the names using split() funtion
names = name_string.split(", ")
# At first find out the length of names, means how many names are entered. Then I can pick a random
# number using random module, then simply print out the index. It will print a random name.
random_name = (len(names))
pick_a_name = random.randint(1, random_name)
final_name = names[pick_a_name]
print(f"{final_name} will pay the bill.")


# Now we can do this by using random.choice() as well, it will eliminate all this step.
# It will directly print out a random name from the list of names.
import random
name_string = input("Enter everyone's names, seperated by a coma(,) \n")
names = name_string.split(", ")
person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} will pay the bill.")


### Nested Lists ###
fruits = ["apple", "banana", "mango", "guava", "cherry"]
vegetables = ["potato", "tomato", "brinjal", "carrot"]

market = [fruits, vegetables]
print(market)
print(market[0][4])