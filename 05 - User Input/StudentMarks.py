# Student Marks
# Take marks of 5 subjects from the user and calculate the total marks and percentage.

marks1 = int(input("Enter marks: "))
marks2 = int(input("Enter marks: "))
marks3 = int(input("Enter marks: "))
marks4 = int(input("Enter marks: "))
marks5 = int(input("Enter marks: "))

marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = marks/500

print(f"The marks you entered are {percentage}%")
