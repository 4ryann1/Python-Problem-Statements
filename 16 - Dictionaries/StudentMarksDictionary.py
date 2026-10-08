"""
Problem 13: Student Marks Dictionary

Create a dictionary of 5 students and marks.
Calculate total, average, highest, lowest, and the name of the highest-scoring student.

Write your solution below.
"""

marks = {
    "English" : 98,
    "Mathematics": 90,
    "Physics": 91,
    "Chemistry": 92,
    "History": 94
}

total_sum = 0

for mark in marks.values():
    total_sum += mark
print("The total sum is",total_sum)

average = total_sum / 5
print("The average is",average)

highest = max(marks.values())
lowest = min(marks.values())
highest_scorer = max(marks, key=marks.get)
print("The highest is",highest)
print("The lowest is",lowest)
print("The highest score has been scored by: ",highest_scorer)