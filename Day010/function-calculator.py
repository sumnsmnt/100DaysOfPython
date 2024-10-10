

# Addition function
def add(num1, num2):
    return num1 + num2

# Substraction function
def substract(num1, num2):
    return num1 - num2

# Multiplication function
def multiply(num1, num2):
    return num1 * num2

# Division function
def divide(num1, num2):
    return num1 / num2

# Oprations dictionary
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from above line: ")

calculation_function = operations[operation_symbol]
result = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")