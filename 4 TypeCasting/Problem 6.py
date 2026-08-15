# ==============================================================================
# PROBLEM STATEMENT 6: Factorial of a Number
# Task: Calculate the factorial of a given positive integer N (N! = N * (N-1) * ... * 1).
# Goal: Use a loop to accumulate the product of numbers from 1 to N.
# Example: Input: 5 -> Output: 120
# ==============================================================================

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    num = 5
    print(f"Factorial of {num} is: {calculate_factorial(num)}")
