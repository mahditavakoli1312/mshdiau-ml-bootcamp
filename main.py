# define a function for addition
def add(num1, num2):
    return num1 + num2

# define a function for subtraction
def subtract(num1, num2):
    return num1 - num2

# define a function for multiplication
def multiply(num1, num2):
    return num1 * num2

# define a function for division
def divide(num1, num2):
    return num1 / num2

# take user input for operation choice and numbers
operation = input("Select operation: +, -, *, / ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform the selected operation
if operation == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation selected")

