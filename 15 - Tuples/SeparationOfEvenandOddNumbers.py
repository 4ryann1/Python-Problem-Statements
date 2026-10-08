"""Problem 9: Separate Even and Odd Numbers

Create a Python program that accepts a tuple of integers.
Create two new tuples:
1. One containing all even numbers.
2. One containing all odd numbers.

Example:
Input: (1, 2, 3, 4, 5, 6)
Output:
Even tuple: (2, 4, 6)
Odd tuple: (1, 3, 5)
"""

# Write your solution below.

tuple1 = (1, 2, 3, 4, 5, 6)
even_list = []
odd_list = []

for i in tuple1:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"The even tuple is: {tuple(even_list)}")
print(f"The odd tuple is: {tuple(odd_list)}")