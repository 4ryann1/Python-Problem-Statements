# Calculate Average Marks
# Take marks of 5 subjects as input and calculate the student's total and average marks.

marks1 = int(input("Enter marks 1: "))
marks2 = int(input("Enter marks 2: "))
marks3 = int(input("Enter marks 3: "))
marks4 = int(input("Enter marks 4: "))
marks5 = int(input("Enter marks 5: "))

total = marks1 + marks2 + marks3 + marks4 + marks5
print(f"The average marks is: {total / 5}")