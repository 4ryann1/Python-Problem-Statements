"""Problem 1: Create and Access a Dictionary

Create a dictionary containing a student's name, age, city, and course.
Print the complete dictionary and each value separately using its key.

Write your solution below.
"""

student = {
    "Name:": "Aryan",
    "Age:": 21,
    "City:": "Pune",
    "Course:": "AI and DS"
}
for key, value in student.items():
    print(key, value)