# 6. Factorial Function
# Create a function factorial(n) that calculates and returns the factorial of a number.
#
# Example:
#
# Input: 5
# Output: 120
#
# Handle 0 correctly.

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))