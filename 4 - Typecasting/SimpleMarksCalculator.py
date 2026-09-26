# Simple Marks Calculator ⭐
# Store marks of three subjects as strings. Convert them into integers, calculate the total and average, and print the results.

marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))

marks1 = int(marks1)
marks2 = int(marks2)
marks3 = int(marks3)

total_marks = marks1 + marks2 + marks3
average_marks = total_marks / 3

print("The average marks is:", average_marks)
print("The total marks is:", total_marks)