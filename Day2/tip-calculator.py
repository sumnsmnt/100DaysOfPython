#
name = input("Hi, What's your name?")

#
print("Welcome to Tip Calcualtor ", name)

#
bill = float(input("What is the total bill? \n"))

#
tip = int(input("What percentage of tip would you like to give? 10, 15, or 20? \n"))

#
person = int(input("How many person to split the bill? \n"))

#
tip_as_percent = tip /100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / person
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")