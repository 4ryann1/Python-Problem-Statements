"""Problem 7: Find the Largest and Smallest Value

Create a dictionary of student names and marks.
Find the student with the highest marks and the student with the lowest marks.

Write your solution below.
"""

student_marks = {
    "Aryan" : 100,
    "Mayur" : 95,
    "Shiv": 58,
    "Krishna":96,
    "Rohit":0
}
print("Largest Value:",max(student_marks.values()))
print("Smallest Value:",min(student_marks.values()))