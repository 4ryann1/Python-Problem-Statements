"""Problem 5: Find the Index of an Element

Create a Python program that accepts a tuple and an element.
Find and display the index of the first occurrence of that element.

Example:
Tuple: (10, 20, 30, 20, 40)
Element: 20
Output:
First occurrence of 20 is at index 1.
"""

# Write your solution below.

tuple1 = (10, 20, 30, 20, 40)

element = int(input("Enter the element you want to find: "))

index = 0
for index, item in enumerate(tuple1):
    if item == element:
        print(f"{element} is at index {index}")

