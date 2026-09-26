"""Problem 2: Tuple Length

Create a Python program that accepts or creates a tuple of elements and finds the number of elements in the tuple.

Do not use a loop for finding the length.

Example:
Input: ("Apple", "Banana", "Mango", "Orange")
Output:
Length: 4
"""

# Write your solution below.

list1 = []

count = 1
while count<=5:
    number = int(input("Enter a number: "))
    list1.append(number)
    count += 1

tuple1 = tuple(list1)

print(len(tuple1))