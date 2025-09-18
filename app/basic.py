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

# def list_datatype():
#     """Return a list of various data types."""
#     demo_list = ['apple','banana','cherry','Mongo','dragon','butterfruit']
#     demo_listtwo = ['Mongo','dragon','butterfruit']
#     print(f'this is actually list ${demo_list}')
#     print(demo_list[-2])
#     print(demo_list[1:2])
#     if 'cherry' in demo_list:
#         print(f'yes, apple is in the list index of it {demo_list.index("cherry")}')
#     print(demo_list.insert(5,'kiwi'))
#     demo_list[0:2] = ['Pomogranate']
#     demo_list.extend(demo_listtwo)
#     print(demo_list)
#     print(f'this is modified list ${demo_list}')
#     for i in demo_list:
#         print(i)
#     for i in range(len(demo_list)):
#         print(f'index of {demo_list[i]} is {i}')
#     new_demo = [i for i in demo_list if 'd' in i]
#     print(new_demo)
#     return demo_list

# list_datatype()/

# def tuple_datatype(data):
#     # print(f'this is actually tuple {data}')
#     # convert_list = list(data)
#     # # convert_list.append('kiwi')
#     # convert_list[1:2] = ['kiwi']
#     # convert_list.remove('cherry')
#     # convert_list.pop(3)
#     # data = tuple(convert_list)
#     # if len(data) == 4:
#     #     print('yes, it is 4')
#     *a, b, c = data
#     print(a)
#     print(b)
#     print(c)
#     print(f'this is modified tuple {data}')
#     return tuple(data) 

# tuple_datat= ('apple','banana','cherry','Mongo')
#tuple_datatype(tuple_datat)


def set_datatype(data_typeone,data_typetwos):
    # data_type2={'apple','banana','cherry','Mongo'}
    # data.add("kiwi")
    # data.update(data_type2)
    # data.remove('banana')
    # set1 = {"a", "b", "c" ,'b','a','c','d' , 1,2,3}
    # set2 = {"a", "b", "c" ,'b','a','c',1,2,3,4,5,6}
    # # set3 = set1 | set2
    # set3 = set1 & set2
    # set1.intersection_update(set2)
    # print(set1)
    # print(f'this is actual set ${set3}')
    # data.discard('Mongo')
    # if 'Mongo' not in data:
    #     print('yes, it is not in the set')
    # print(f'this is actually set {data}')
    set1 = data_typeone
    set2= data_typetwo
    # Union
    set3 = set1.union(set2)
    # Intersection
    set4 = set1.intersection(set2)
    # Difference
    set5 = set1.difference(set2)
    # Symmetric Difference
    set6 = set1.symmetric_difference(set2)
    print(f'Symmetric Difference: {set6}')
    print(f'Difference: {set5}')
    print(f'Intersection: {set4}')
    print(f'Union: {set3}')
    print(f'Set one: {set1}')
    print(f'Set two: {set2}')
    return


data_typeone={'apple','banana','cherry','Mongo',1,2,3,4,5,'apple','kiwi','banana'}
data_typetwo={'butterfruit','watermelon','jackfruit',1,2,3,4,5,5.6,6,6,7,8,9,'apple','kiwi','banana'}
set_datatype(data_typeone,data_typetwo)



if __name__ == "__main__":
    print("This module is for learning python.")
