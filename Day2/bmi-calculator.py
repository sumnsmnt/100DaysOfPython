# Ask the user to input height and weight and convert them into float data types
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# the formula to calculate bmi is (weight/height**2)
# Here I use round() function to get a whole number
bmi = round(weight / (height ** 2))

print(f"Your height is {height}, weigth is {weight} and BMI is: {bmi}")