"""Problem 3: Check if an Element Exists

Create a Python program that accepts a tuple and an element from the user.
Check whether the given element exists in the tuple.

Example:
Tuple: (10, 20, 30, 40, 50)
Element: 30
Output:
30 exists in the tuple.
"""

# Write your solution below.

numbers = (10, 20, 30, 40, 50)

element = int(input("Enter an element: "))

if element in numbers:
    print(element, "exists in the tuple.")
else:
    print(element, "does not exist in the tuple.")