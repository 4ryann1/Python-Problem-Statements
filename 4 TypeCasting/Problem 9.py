# ==============================================================================
# PROBLEM STATEMENT 9: Sum of List Elements
# Task: Compute the sum of all numbers in a list without using the built-in sum() function.
# Goal: Practice accumulator variables, loops, and basic list iteration.
# Example: Input: [10, 20, 30, 40] -> Output: 100
# ==============================================================================

def custom_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

if __name__ == "__main__":
    num_list = [10, 20, 30, 40]
    print(f"List: {num_list}")
    print(f"Sum of elements: {custom_sum(num_list)}")
