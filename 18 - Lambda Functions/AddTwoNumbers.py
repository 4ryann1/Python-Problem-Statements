# Problem 5: Add Two Numbers Using Lambda
#
# Create a Python program that accepts two numbers.
# Use a lambda function to add the two numbers and display the result.
#
# Example:
# Input: 12 8
# Output: 20

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

sum = lambda x, y: x + y
print(sum(n1, n2))