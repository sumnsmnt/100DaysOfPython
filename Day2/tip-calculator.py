# Welcome message
name = input("Hi, What's your name? ")
print("Welcome to Tip Calcualtor", name)

# We have to take 3 inputs from user - total bill amount, tip percentage & no of people 
bill = float(input("What is the total bill? \n"))
tip = int(input("What percentage of tip would you like to give? enter number only :) \n"))
person = int(input("How many person will split the bill? \n"))

# I have to find out bill per person, so start with total tip, then add the bill with it 
# and then devide the total bill with no of person
total_tip = bill * (tip / 100)
total_bill = bill + total_tip
bill_per_person = round(total_bill / person, 2)

print(f"Each person should pay: ${bill_per_person}")

# We can also format the round function as the round function will not print 2 decimal 
# values if there is no value in floating point till the 2 decimal point.
# That's why we we use format() function. It will print upto n decimal (what we menton in the line)
# even if there is no actual floating point value.

# per_person_amount = total_bill / person
# final_amount = "{:.2f}".format(per_person_amount)
# print(f"Each person should pay: ${final_amount}")