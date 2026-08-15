# ==============================================================================
# PROBLEM STATEMENT 10: Prime Number Checker
# Task: Check whether a positive integer greater than 1 is a prime number.
# Goal: Combine loops, divisibility checks with modulo, and early termination.
# Example: Input: 11 -> Output: Prime; Input: 12 -> Output: Not Prime
# ==============================================================================

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    test_numbers = [11, 12, 2, 1]
    for num in test_numbers:
        result = "Prime" if is_prime(num) else "Not Prime"
        print(f"Number {num} is {result}")
