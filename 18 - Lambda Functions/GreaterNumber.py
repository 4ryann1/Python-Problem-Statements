# Problem 4: Find the Greater of Two Numbers Using Lambda
#
# Create a Python program that accepts two numbers.
# Use a lambda function to find and display the greater number.
#
# Example:
# Input: 15 9
# Output: 15

number1 = int(input())
number2 = int(input())

greater = lambda number1, number2: number1 if number1 > number2 else number2

result = greater(number1, number2)
print(result)
