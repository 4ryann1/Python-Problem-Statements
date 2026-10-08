# 3. Find the Largest Number
# Create a function find_largest(a, b, c) that accepts three numbers and returns the largest number.
#
# Example:
#
# Input: 10, 25, 15
# Output: 25

def find_largest(a,b,c):
    if a > b and a > c:
        print(f"{a} is the largest number.")
    elif b > a and b > c:
        print(f"{b} is the largest number.")
    elif c > a and c > b:
        print(f"{c} is the largest number.")
    else:
        raise ValueError


find_largest(1,2,3)