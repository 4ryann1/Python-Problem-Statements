"""Problem 11: Remove a Key from a Dictionary

Create a student dictionary. Ask for a key to remove; if it exists, remove it and display the updated dictionary.

Write your solution below.
"""

student = {
    "Name" : "Aryan",
    "Age" : 25,
    "College" : "DYPTC",
    "Profession" : "Engineer"
}

choice = input("What would you want to delete: ")

if choice in student:
    del student[choice]
    print(student)
else:
    print("Key does not exist.")