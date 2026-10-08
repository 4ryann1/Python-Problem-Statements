"""Problem 13: Find Common Elements in Two Tuples

Create a Python program that accepts two tuples and finds the elements that are common to both tuples.

Example:
Tuple 1: (1, 2, 3, 4, 5)
Tuple 2: (4, 5, 6, 7, 8)
Output:
Common elements: (4, 5)
"""

# Write your solution below.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

list1 = []

for element in tuple1:
    if element in tuple2:
        list1.append(element)
print(list1)