"""Problem 2: Add Elements to a Set

Create a set of three numbers. Ask the user for a number, add it, and display the updated set.
"""

# Write your solution below.

set = {1,2,3}

user_input = int(input("Enter a number: "))
set.add(user_input)
print(f"The number you added: {user_input} and the set becomes {set}")
