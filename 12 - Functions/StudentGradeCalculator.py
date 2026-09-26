# 8. Calculate Student Result
# Create a function:
#
# calculate_result(marks)
#
# The function should accept marks of 5 subjects and calculate:
#
# Total marks
# Percentage
# Grade
#
# Example:
#
# Marks: 80, 75, 90, 85, 70
#
# Total: 400
# Percentage: 80%
# Grade: A

def calculate_result(marks1, marks2, marks3, marks4, marks5):
        total_marks = marks1 + marks2 + marks3 + marks4 + marks5
        percentage = (total_marks/500)*100
        grade = percentage
        if grade>=90 and grade<=100:
            print("Grade: A")
        elif grade>=80 and grade<=89:
            print("Grade: B")
        elif grade>=70 and grade<=79:
            print("Grade: C")
        elif grade>=60 and grade<=69:
            print("Grade: D")
        elif grade>=50 and grade<=59:
            print("Grade: E")
        else:
            print("Grade F")

        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage}")


print(calculate_result(90,98,97,96,97))