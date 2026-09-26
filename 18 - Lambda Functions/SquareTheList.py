# Problem 9: Square Every Element in a List
#
# Create a Python program that accepts a list of numbers.
# Use a lambda function with map() to find the square of every element.
#
# Example:
# Input: [2, 3, 4, 5]
# Output: [4, 9, 16, 25]

user_input = eval(input("Enter the List: "))

square_list = list(map(lambda x: x ** 2, user_input))
print(square_list)