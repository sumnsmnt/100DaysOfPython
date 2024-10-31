# take input from user about their weight and height
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

# calculate the BMI
bmi = round(weight / (height ** 2))

# running if-elif-else loop to print the bmi and it's type
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you have noraml weight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are clinically obese")


