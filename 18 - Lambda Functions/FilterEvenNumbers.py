# Problem 6: Filter Even Numbers from a List
#
# Create a Python program that accepts a list of integers.
# Use a lambda function with filter() to extract all even numbers from the list.
#
# Example:
# Input: [1, 2, 3, 4, 5, 6]
# Output: [2, 4, 6]

user_input = eval(input("Input the list: "))

numbers = [int(x) for x in user_input]

even = list(filter(lambda i: i % 2 == 0, numbers))

print(even)