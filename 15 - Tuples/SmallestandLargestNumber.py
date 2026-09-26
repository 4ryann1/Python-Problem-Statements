"""Problem 8: Find Largest and Smallest Element

Create a Python program that accepts a tuple of numbers and finds the largest and smallest elements.

First try using Python's built-in max() and min() functions.
Then try solving it without using max() and min().

Example:
Input: (12, 5, 89, 23, 7)
Output:
Largest: 89
Smallest: 5
"""

# Write your solution below.

tuple1 = (12, 5, 89, 23, 7)

#Using max() and min() built-in functions in python
print("Largest: ", max(tuple1))
print("Smallest: ", min(tuple1))

#Without built-in functions in python
largest = tuple1[0]
smallest = tuple1[0]

for number in tuple1:
    if number>largest:
        largest = number
    if number<smallest:
        smallest = number

print("Largest: ", largest)
print("Smallest: ", smallest)