"""Problem 3: Check if a Key Exists

Accept a dictionary and a key from the user.
Check whether the given key exists in the dictionary.

Write your solution below.
"""

student = eval(input("Enter a Dictionary: {Name:': 'Aryan', 'Age:': 21}: "))

key = input("Enter a key: ")

if key in student:
    print("Yes the key exists in the dictionary.")
if key not in student:
    print("The key does not exist in the dictionary.")