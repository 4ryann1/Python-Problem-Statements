# 3. Multiplication Table
#
# Take a number from the user and print its multiplication table from 1 to 10.
#
# Example:
#
# Input: 7
#
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 10 = 70

num = int(input("Enter a number: "))

print(f"The table of {num} is: ")
for i in range(1,11):
    print(f"{num} x {i} = {i*num}")