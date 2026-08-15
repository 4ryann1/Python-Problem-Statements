# ==============================================================================
# PROBLEM STATEMENT 8: Multiplication Table Generator
# Task: Accept an integer N and print its multiplication table from 1 to 10.
# Goal: Practice for loops with range() and formatted string output (f-strings).
# Example: Input: 3 -> Output: 3 x 1 = 3, 3 x 2 = 6, ..., 3 x 10 = 30
# ==============================================================================

def generate_multiplication_table(n):
    table = []
    for i in range(1, 11):
        table.append(f"{n} x {i} = {n * i}")
    return "\n".join(table)

if __name__ == "__main__":
    num = 3
    print(f"Multiplication Table for {num}:")
    print(generate_multiplication_table(num))
