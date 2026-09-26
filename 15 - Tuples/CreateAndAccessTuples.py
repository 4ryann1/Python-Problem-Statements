"""Problem 1: Create and Access a Tuple

Create a Python program that creates a tuple containing 5 integers.
Print the complete tuple and then print each element using its index.

Example:
Input: (10, 20, 30, 40, 50)
Output:
Tuple: (10, 20, 30, 40, 50)
First element: 10
Last element: 50
"""

# Write your solution below.

tuple1 = (10, 20, 30, 40, 50)

count = 0
for item in tuple1:
    print(f"The {item} item is present at index {count}")
    count += 1