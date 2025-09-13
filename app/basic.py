# def sayHello():
#     return "Om Namashivaya!"

# print(sayHello())

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

choice = input('Enter the operation you want to perform:')

def validation(choice):
    if choice in operations:
        a = input('Enter first number: ')
        b = input('Enter second number: ')
        print(f"The result is: {operations[choice](int(a), int(b))}")
    else:
        print("Invalid operation selected.")
    
print(validation(choice))