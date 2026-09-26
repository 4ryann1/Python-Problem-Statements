"""Problem 13: Find Missing Numbers

Given existing numbers from 1 to 10 and the complete set 1 to 10, find the missing numbers.
"""

# Write your solution below.

complete_numbers = {1,2,3,4,5,6,7,8,9,10}
existing_numbers = {1,4,5,7,8,10}

remaining_numbers = complete_numbers - existing_numbers
print(f"The remaining numbers are: {remaining_numbers}")