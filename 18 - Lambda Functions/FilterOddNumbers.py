# Problem 7: Filter Odd Numbers from a List
#
# Create a Python program that accepts a list of integers.
# Use a lambda function with filter() to extract all odd numbers from the list.
#
# Example:
# Input: [10, 15, 20, 25, 30]
# Output: [15, 25]

user_input = eval(input("Enter number: "))

odd_numbers = list(filter(lambda n: n % 2 != 0, user_input))
print(odd_numbers)