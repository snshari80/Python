"""Module for basic operations."""
def say_hello():
    """Return a greeting."""
    return "Om Namashivaya!"

print(say_hello())

print('Hello! Do you want to try Python Mathamatics?')

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mulitply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": mulitply,
    "/": divide
}

def validation(choice):
    if choice in operations:
        a = input('Enter first number: ')
        b = input('Enter second number: ')
        print(f"The result is: {operations[choice](int(a), int(b))}")
    else:
        print("Invalid operation selected.")

choice = input('Enter the operation you want to perform:')
validation(choice)
