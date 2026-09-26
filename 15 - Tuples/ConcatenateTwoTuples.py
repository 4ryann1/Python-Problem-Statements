"""Problem 7: Concatenate Two Tuples

Create a Python program that creates or accepts two tuples and combines them into a single tuple.

Example:
Tuple 1: (1, 2, 3)
Tuple 2: (4, 5, 6)
Output:
Combined tuple: (1, 2, 3, 4, 5, 6)
"""

# Write your solution below.

Tuple1 = (1, 2, 3)
Tuple2 = (4, 5, 6)

combined = list(Tuple1 + Tuple2)
combined = tuple(combined)
print(combined)