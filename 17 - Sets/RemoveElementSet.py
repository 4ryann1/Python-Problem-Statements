"""Problem 3: Remove an Element from a Set

Create a set and ask the user for an element to remove. Handle the case where it does not exist.
"""

# Write your solution below.

set = {12, 13, 14, 15}

user_input = int(input("Enter a number to remove from the set: "))

if user_input in set:
    set.remove(user_input)
else:
    print("Sorry, the number you entered is not in the set.")