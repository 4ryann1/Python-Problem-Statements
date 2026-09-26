# Problem 12: Rotate a List
# Create a program that accepts a list and an integer K.
# Rotate the list to the right by K positions.
# Example:
# Input: [1, 2, 3, 4, 5], K = 2
# Output: [4, 5, 1, 2, 3]

# Write your solution below.

numbers = [1, 2, 3, 4, 5]
k = 2

for i in range(k):
    last = numbers.pop()
    numbers.insert(0, last)

print(numbers)