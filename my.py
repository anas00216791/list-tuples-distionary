# List in python

fruits: list =["apple","mango","banana","orange"]
# number:list = [1,2,3,4]
# mixed: list = ["apple", 1, 2.5, True]

# print("fruits =", fruits)
# print("number =", number)
# print("mixed =", mixed)
# Accessing List Elements

# fruits: list = ["apple", "banana", "cherry"]
# print(fruits[0]) 
# print(fruits)

# Modifying Lists

# fruits: list = ["apple", "banana", "cherry"]
# fruits[-3] = "watermelon" 
# print(fruits)

# List Slicing

# print(fruits[0:2]) 

# 2. Common List Methods

# fruits.append("mango")
# print(fruits)

# fruits.extend(["grape", "kiwi"])  
# print(fruits)

# Removing Elements from a List
# fruits.remove("banana")
# print(fruits)

# Pop Method

# deleted = fruits.pop(1) 
# print("deleted element = ", deleted) 
# print(fruits) 

# Sorting a List
# 1. Default Sorting (Ascending Order)

# numbers: list[int] = [3, 1, 4, 1, 5, 9] 
# numbers.sort()
# print(numbers)

# 2. Sorting in Descending Order (reverse=True)

# numbers = [4, 2, 9, 1]
# numbers.sort(reverse=True)
# print(numbers)

# 3. Sorting by String Length (key=len)

# words = ["apple", "kiwi", "banana"]
# words.sort(key=len)
# print(words)

# 4. Sorting by Last Character (key=lambda word: word[-1])

# words = ["apple", "kiwi", "banana"]
# words.sort(key=lambda word: word[-1])
# print(words)

# 5. Reverse Sorting

# numbers = [1,2,3,4,5, 6, 7, 8, 9,0]
# numbers.reverse()
# print(numbers)

# 3. Iterating Over Lists
# Using For Loop

# for fruit in fruits:
#     print(fruit)

# Using list comprehension

# Without if condition
# squared: list = [x**2 for x in [1, 2, 3, 4, 5] ] #  if x > 3 place this if condition and see
# print(squared, " : ", type(squared)) 
