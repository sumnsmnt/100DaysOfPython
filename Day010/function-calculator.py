

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
def calculator():
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))

        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")

        recalculation = input(f'''
        Type 'r' to recalculate with {result}, 
        type 'y' to continue with new calculation,
        or type 'n' to exit. ''')
        if  recalculation == "r":
            num1 = result
        elif  recalculation == "y":
            calculator()
        else:
            should_continue = False

calculator()