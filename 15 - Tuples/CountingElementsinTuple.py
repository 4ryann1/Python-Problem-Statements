"""Problem 4: Count an Element in a Tuple

Create a Python program that accepts a tuple and an element.
Find how many times the given element occurs in the tuple.

Example:
Tuple: (1, 2, 2, 3, 2, 4)
Element: 2
Output:
2 occurs 3 times.
"""

# Write your solution below.

tuple1 = (1, 2, 2, 3, 2, 4)
unique_elements = []

choice = int(input("Enter a element to check occurence: "))

count = 0
for i in tuple1:
    if choice == i:
        count = count + 1


print(f"{choice} occurs {count} times.")

