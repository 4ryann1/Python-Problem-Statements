# 6. Factorial of a Number
#
# Take a number N and calculate its factorial using a for loop.
#
# Example:
#
# Input: 5
# Output: 120

number = int(input("Enter a number: "))

factorial = 1
for i in range(1,number+1):
    factorial = factorial * i
print(factorial)