# 8. Check for Prime Number
#
# Take a number as input and determine whether it is prime or not using a for loop.
#
# Example:
#
# Input: 17
# Output: Prime
#
# Challenge: Avoid using any built-in function for checking primality.

number = int(input("Enter a number: "))

is_prime = True

if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime Number")
else:
    print("Not Prime Number")