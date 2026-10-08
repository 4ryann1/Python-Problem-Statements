"""Problem 14: Sort a Tuple

Create a Python program that accepts a tuple of numbers and displays its elements in ascending order.

Then display the elements in descending order.

Example:
Input: (40, 10, 30, 20, 50)
Output:
Ascending: (10, 20, 30, 40, 50)
Descending: (50, 40, 30, 20, 10)
"""

# Write your solution below.

tuple1 = (40, 10, 30, 20, 50)

tuple1_sorted = sorted(tuple1)
print("Decending order: ",tuple(tuple(reversed(tuple1_sorted))))

tuple2 = (tuple1_sorted)
print("Acending order: ",tuple2)
