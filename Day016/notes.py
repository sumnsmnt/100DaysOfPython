####### Object Oriented Programming #######

# Let's take Waiter as an object
# So, Waiter has:
# (These are called attributes)
#     is_holding_plate = True
#     tables_responsible = [4,5,6]

# and Waiter does:
# (These are called methods)
#     def take_order(table, order):
#         # takes order to chef
#     def take_payment(amount):
#         # add money to resturant

# If I want to make different objects from these attributes and methods they will be
# called as a Object and the intial template will be called as a Class
# e.g. If I want to create 2 waiter called Suman & Sujan they will be called as Object
# and as they take the properties of waiter so, Waiter will be Class.

# # Use Turtle Object
# from turtle import Turtle, Screen
# tom = Turtle()
# print(tom)
# tom.shape("turtle")
# tom.color("red")
# tom.forward(111)

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


# import prettytable import PrettyTable
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Name", ["Suman", "Sujan", "Sajan"])
table.add_column("Age", ["26", "21", "24"])
print(table)
print(table.align)
