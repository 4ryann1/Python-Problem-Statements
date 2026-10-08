"""Problem 15: Student Marks Tuple

Create a Python program that stores a student's marks in five subjects inside a tuple.

Display:
1. All marks
2. Total marks
3. Average marks
4. Highest marks
5. Lowest marks

Example:
Marks: (78, 85, 92, 67, 88)

Output:
Total: 410
Average: 82.0
Highest: 92
Lowest: 67
"""

# Write your solution below.

marks = (95, 96, 94, 97, 98)

while True:
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("All marks are as follows: ")
        for index, mark in enumerate(marks):
            print(f"Subject {index}: {mark}")
    elif choice == 2:
        total_sum = 0
        for mark in marks:
            total_sum += mark
        print(f"Total marks: {total_sum}")
    elif choice == 3:
        total_sum = 0
        for mark in marks:
            total_sum += mark
        print(f"Average marks: {(total_sum)/5}")
    elif choice == 4:
        print(f"Highest marks:{max(marks)}")
    elif choice == 5:
        print(f"Lowest marks:{min(marks)}")
    else:
        break