"""Problem 11: Remove Duplicate Elements from a Tuple

Create a Python program that accepts a tuple containing duplicate elements.
Create a new tuple containing only unique elements.

Example:
Input: (1, 2, 2, 3, 1, 4, 3)
Output:
Unique tuple: (1, 2, 3, 4)
"""

# Write your solution below.
tuple1 = (1, 2, 2, 3, 1, 4, 3)

tuple1 = set(tuple1)
tuple1 = tuple(tuple1)

print(f"The duplicates removed are: {tuple1}")