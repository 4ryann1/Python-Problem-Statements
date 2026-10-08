# 2. Check Even or Odd
# Create a function check_even_odd(n) that accepts an integer and returns whether it is "Even" or "Odd".
#
# Example:
#
# Input: 17
# Output: Odd

def checkEvenOdd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Not Even"

print(checkEvenOdd(5))