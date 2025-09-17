"""Module for basic operations."""

# def say_hello():
#     """Return a greeting."""
#     return "Om Namashivaya!"

# say_hello()

# print('Hello! Do you want to try Python Mathematics?')

# def add(a, b):
#     """Return the sum of a and b."""
#     return a + b

# def subtract(a, b):
#     """Return the difference of a and b."""
#     return a - b

# def multiply(a, b):
#     """Return the product of a and b."""
#     return a * b

# def divide(a, b):
#     """Return the division of a by b, or an error message if b is zero."""
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b

# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide
# }

# def validation(operation_choice):
#     """Validate the operation and perform calculation."""
#     if operation_choice in operations:
#         a = input('Enter first number: ')
#         b = input('Enter second number: ')
#         print(f"The result is: {operations[operation_choice](int(a), int(b))}")
#     else:
#         print("Invalid operation selected.")

# user_choice = input('Enter the operation you want to perform: ')
# validation(user_choice)

def list_datatype():
    """Return a list of various data types."""
    demo_list = ['apple','banana','cherry','Mongo','dragon','butterfruit']
    # demo_listtwo = ['Mongo','dragon','butterfruit']
    # print(f'this is actually list ${demo_list}')
    # print(demo_list[-2])
    # print(demo_list[1:2])
    # if 'cherry' in demo_list:
    #     print(f'yes, apple is in the list index of it {demo_list.index("cherry")}')
    # print(demo_list.insert(5,'kiwi'))
    # demo_list[0:2] = ['Pomogranate']
    # demo_list.extend(demo_listtwo)
    # print(demo_list)
    # print(f'this is modified list ${demo_list}')
    for i in demo_list:
        print(i)
    for i in range(len(demo_list)):
        print(f'index of {demo_list[i]} is {i}')
    new_demo = [i for i in demo_list if 'd' in i]
    print(new_demo)
    return demo_list

list_datatype()

if __name__ == "__main__":
    print("This module is for learning python.")
