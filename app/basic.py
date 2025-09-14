"""Module for basic operations."""

def say_hello():
    """Return a greeting."""
    return "Om Namashivaya!"

say_hello()

print('Hello! Do you want to try Python Mathematics?')

def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the division of a by b, or an error message if b is zero."""
    if b == 0:
        return "Error! Division by zero."
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def validation(operation_choice):
    """Validate the operation and perform calculation."""
    if operation_choice in operations:
        a = input('Enter first number: ')
        b = input('Enter second number: ')
        print(f"The result is: {operations[operation_choice](int(a), int(b))}")
    else:
        print("Invalid operation selected.")

user_choice = input('Enter the operation you want to perform: ')
validation(user_choice)
