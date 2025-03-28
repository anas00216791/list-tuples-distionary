# Distionery

Pakistan: dict = ["Karachi_Lighting_City", "Lahore", "Peshawar", "Multan", "Islamabad", "Quetta", "Faisalabad", "Hyderabad", "Gujranwala", "Sialkot"]
Pakistan
# print(Pakistan)

person: dict = {
    "name": "Anas",
    "age": 20,
    "visited_cities": "Karachi_Lighting_City",
}
# print(person)

# Accessing Values

# print(person["name"])  # Output: Alice
# print(person.get("age", "99"))  # Output: 25, if not found it will return 99 (default value)

# Access a non-existent key
# print(person.get("country", "Pakistan"))

# Modifying a Dictionary

# Add a new key-value pair
person["email"] = "tariqanas825@gmail.com"
# print(person)

# Modify an existing value
# person["age"] = 20
# print(person)

# Deleting Items

person: dict = {'name': 'Anas', 'age': 20, 'email': 'tariqanas825@gmail.com', 'city': ['Karachi_Lighting_City', 'Lahore', 'Peshawar', 'Multan', 'Islamabad', 'Quetta', 'Faisalabad', 'Hyderabad', 'Gujranwala', 'Sialkot']}
# print(person)
# del person["city"]
# print(person)

age: int = person.pop("age", -1)
# print("Removed age:", age)
# print(person)

# print("\n-----\n")
#Again remove a key which is already removed to check the default value
age: int = person.pop("age", -1)
# print("key 'age' not found in dict so returning default value: ", age)

# 6. Dictionary Methods

# Get all keys
# print("person.keys()         = ", person.keys()  )  # Output: dict_keys(['name', 'email', 'city', 'age'])

# Get all values
# print("person.values()       = ", person.values())  # Output: dict_values(['Alice', 'alice@example.com', 'Los Angeles', 27])

# Get all key-value pairs
# print("person.items()        = ", person.items())  # Output: dict_items([('name', 'Alice'), ('email', 'alice@example.com'), ('city', 'Los Angeles'), ('age', 27)])

# Update the dictionary
person.update({"city": "Los Angeles", "age": 27})
# print("After: person.update  = ", person)

# Clear the dictionary
person.clear()
# print("After: person.clear() = ", person)  # Output: {}

# Duplicate Key Not Allowed

thisdict: dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 # this will overwrite the previous key:vlaue
}
# print(thisdict)

# 7. Iterating Over a Dictionary

# for key in thisdict:
    # print(key)
    # for key, value in thisdict.items():
        # print(key," : ", value)

# 8. Practical Examples

#  Create a phonebook
# phonebook: dict = {
#     "Alice": "123-456-7890",
#     "Bob": "987-654-3210",
#     "Charlie": "555-555-5555"
# }

# Add a new contact
# phonebook["David"] = "111-222-3333"

# Search for a contact
# name: str = input("Enter a name to search: ")
# if name in phonebook:
    # print(f"{name}'s phone number is {phonebook[name]}.")
# else:
    # print(f"{name} is not in the phonebook.")

# Count the frequency of words in a sentence

# sentence = "This is a sample sentence with sample words"
# words: list = sentence.split()
# word_count = {}

# for word in words:
    # if word in word_count:
        # word_count[word] += 1
    # else:
        # word_count[word] = 1
# print("Word Count:", word_count)

# Sort the dictionary by frequency (highest to lowest)
# sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
#
# Print the sorted word count
# print("Sorted Word Count:", sorted_word_count)

# my_dict = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # 1. Accessing Items
# print("1. Accessing Items")
# print("Name:", my_dict["name"])  # Accessing by key
# print("Age:", my_dict.get("age"))  # Accessing using get()
# print("City (using get):", my_dict.get("city"))

# # 2. Adding Items
# print("\n2. Adding Items")
# my_dict["email"] = "john@example.com"
# print("Dictionary after adding email:", my_dict)

# # 3. Modifying Items
# print("\n3. Modifying Items")
# my_dict["age"] = 31
# print("Dictionary after modifying age:", my_dict)

# # 4. Removing Items
# print("\n4. Removing Items")
# my_dict.pop("city")
# print("Dictionary after removing city (using pop):", my_dict)
# del my_dict["email"]
# print("Dictionary after removing email (using del):", my_dict)

# # 5. Dictionary Methods
# print("\n5. Dictionary Methods")
# print("Keys:", my_dict.keys())
# print("Values:", my_dict.values())
# print("Items:", my_dict.items())

# # 6. Clearing the Dictionary
# print("\n6. Clearing the Dictionary")
# my_dict.clear()
# print("Dictionary after clearing:", my_dict)

# # Adding items back for further examples
# my_dict = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # 7. Updating the Dictionary
# print("\n7. Updating the Dictionary")
# my_dict.update({"age": 32, "country": "USA"})
# print("Dictionary after updating:", my_dict)

# # 8. Iterating Through a Dictionary
# print("\n8. Iterating Through a Dictionary")
# print("Iterating through keys:")
# for key in my_dict:
#   print(key)

# print("\nIterating through values:")
# for value in my_dict.values():
#   print(value)

# print("\nIterating through items (key-value pairs):")
# for key, value in my_dict.items():
#   print(f"{key}: {value}")

# #9 checking if a key exist
# print("\n9. checking if a key exist")
# if "name" in my_dict:
#     print("Name exist")
# else:
#     print("Name do not exist")

# # 10. Dictionary Length
# print("\n10. Dictionary Length")
# print("Length of the dictionary:", len(my_dict))

# # 11. Creating a dictionary from iterable
# print("\n11. Creating a dictionary from iterable")
# iterable = [("key1", "value1"), ("key2", "value2"), ("key3", "value3")]
# new_dict = dict(iterable)
# print("new dictionary:", new_dict)

# # 12. Copying a dictionary
# print("\n12. Copying a dictionary")
# copied_dict = my_dict.copy()
# print("Copied dictionary:", copied_dict)

# # 13. Nested Dictionaries
# print("\n13. Nested Dictionaries")
# nested_dict = {
#     "person1": {"name": "Alice", "age": 25},
#     "person2": {"name": "Bob", "age": 30}
# }
# print("Nested dictionary:", nested_dict)
# print("Alice's age:", nested_dict["person1"]["age"])
# print("Bob's name:", nested_dict["person2"]["name"])

# Dictionary Comprehensions

original_dict = {'a': 1, 'b': 2, 'c': 3}
# print("original_dict = ", original_dict)
doubled_dict = {k: v*2 for k, v in original_dict.items()}
# print("doubled_dict  = ", doubled_dict)  # Output: {'a': 2, 'b': 4, 'c': 6}

# Practical Example

celsius_temps = [0, 10, 20, 30, 40]
fahrenheit_temps = {str(c)+"c":  str((c * 9/5) + 32)+"f" for c in celsius_temps}
print(fahrenheit_temps)  # Output: {0: 32, 10: 50, 20: 68, 30: 86, 40: 104}
