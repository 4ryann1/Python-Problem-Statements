"""Problem 1: Create and Access a Set

Create a set containing 5 integers. Print the set and check whether a user-given element exists.
"""

# Write your solution below.

set = {1, 2, 3, 4, 5}

user_input = int(input("Enter a number: "))
if user_input in set:
    print(f"The element {user_input} exists")
else:
    print(f"Element {user_input} does not exist")

print(set)
