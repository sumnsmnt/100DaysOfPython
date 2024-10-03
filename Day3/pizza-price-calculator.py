# Based on user's order, workout on their final bill.
# Small Pizza: 15$, Medium Pizza: 20$, Large Pizza: 25$
# Pepperoni for small pizza: +2$
# Pepperoni for medium and large pizza: +3$
# Extra cheese for any size pizza: +1$

print("Welcome to Python Pizza Shop")
size = input("What sized Pizza you want? S, M or L \n")
add_pep = input("Do you want Pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0

if size == "S":
    bill +=15
elif size == "M":
    bill +=20
elif size == "L":
    bill +=25

if add_pep == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}")