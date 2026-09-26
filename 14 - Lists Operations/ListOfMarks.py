# Problem 1: Student Marks
# Create a Python program that stores the marks of 10 students in a list and:
# - Print the complete list.
# - Print the highest mark.
# - Print the lowest mark.
# - Calculate and print the average marks.
#
# # Write your solution below.

marks = [90, 80, 85, 87, 89, 91, 92, 98, 95, 93]

#Printing the complete list
print(f"The marks of students are {marks}")

#printing the highest marks
print(f"The highest marks are {max(marks)} in the list.")

#printing the lowest marks
print(f"The lowest marks are {min(marks)}")

#printing the average marks
def average_list(marks):
    sum = 0
    for mark in marks:
        sum += mark
    average = sum /len(marks)
    print(f"The average marks are {average}")
average_list(marks)