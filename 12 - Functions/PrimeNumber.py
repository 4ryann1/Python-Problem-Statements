# 7. Prime Number Checker
# Create a function:
#
# is_prime(n)
#
# It should return True if the number is prime and False otherwise.
#
# Example:
#
# Input: 17
# Output: True
#
# Input: 20
# Output: False


def prime_number(n):
    if (n%2==0 or n%3==0 or n==1):
        return False
    else:
        return True

print(prime_number(22))