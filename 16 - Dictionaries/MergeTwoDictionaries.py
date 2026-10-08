"""Problem 10: Merge Two Dictionaries

Create two dictionaries and merge them into a single dictionary.

Write your solution below.
"""

student1 = {
    "name": "Aryan",
    "age": 25,
}

student2 = {
    "Profession" : "Engineer",
    "College": "DYPTC, Varale"
}

student3 = student1 | student2
print(student3)