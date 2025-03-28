
# 4. Tuples in Python

tuple1: tuple = tuple(["apple", "banana", "cherry"]) # cast a list into tuple
tuple2: tuple = (10, 20, 30) # tuple
mixed_tuple: tuple = ("hello! Anas Tariq Ali", 42, 3.14, True) # tuple

# print("tuple1      =", tuple1)
# print("tuple2      =", tuple2)
# print("mixed_tuple =", mixed_tuple)

tuple_1: tuple = (10, 20, 30) # tuple
tuple_2: tuple = (10, 20, 30) # tuple

# print("id(tuple_1) = ", id(tuple_1)) # unique memory address
# print("id(tuple_2) = ", id(tuple_2)) # unique memory address

# print("tuple_1 == tuple_2 = ", tuple_1 == tuple_2) 


tuple1: tuple      = tuple(["apple", "banana", "cherry"])  # cast a list into tuple
tuple2: tuple      = (10, 20, 30)  # tuple
mixed_tuple: tuple = ("hello", 42, 3.14, True)  # tuple

# print("tuple1      =", tuple1)
# # print("tuple2      =", tuple2)
# print("mixed_tuple =", mixed_tuple)

# Accessing elements in a tuple
# print("tuple1[0] =", tuple1[0])  # Accessing first element

# Tuple slicing
# print("tuple2[1:] =", tuple2[1:])  # Slicing from index 1

# Tuple length
# print("Length of tuple1:", len(tuple1))

# Iterating through a tuple
# print("Iterating through tuple2:")
for item in tuple2:
  print(item)

# Checking if an item exists in a tuple
# print("Is 20 in tuple2?", 20 in tuple2)

# Concatenating tuples
tuple3: tuple = tuple1 + tuple2
# print("tuple1 + tuple2 =", tuple3)

# Repeating tuples
tuple4: tuple = tuple2 * 2
# print("tuple2 * 2 =", tuple4)

# Nested tuples
nested_tuple = (tuple1, tuple2)
# print("nested_tuple =", nested_tuple)

# Unpacking tuples
a, b, c = tuple1
# print("Unpacking tuple1:", a, b, c)

# Using tuples as keys in dictionaries (because they are immutable)
my_dict = {tuple1: "This is a tuple key", tuple2: "Another tuple key"}
# print("Dictionary with tuple keys:", my_dict)
# prompt: print the complete list of methods and attribute of tuple, dont include dunders

# Get a list of all attributes and methods of a tuple
tuple_methods: list = [method for method in dir(tuple) if not method.startswith('__')]

# Print the list of methods (excluding dunder methods)
tuple_methods
tuple1: tuple = tuple(["apple", "banana", "cherry"])
# print(tuple1.count("apple"))  # Output: 1
# print(tuple1.index("apple"))  # Output: 0
# example_tuple: tuple = ('count', 'index')
# print(example_tuple) # Output: ('count', 'index')

# Python is Type Hint Language

# a: int = input ("Enter your name: ")
# print(a, type(a) )

