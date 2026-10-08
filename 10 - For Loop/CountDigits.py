# 5. Count Digits
#
# Take an integer as input and count how many digits it contains using a for loop.
#
# Example:
#
# Input: 58392
# Output: 5 digits

num = int(input("Enter a number: "))
num = str(num)

count = 0
for digit in num:
    count += 1
print(count)