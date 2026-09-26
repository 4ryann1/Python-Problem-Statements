# 4. Sum of Natural Numbers
#
# Take N as input and calculate the sum of all numbers from 1 to N using a for loop.
#
# Example:
#
# Input: 5
# Output: 15

n = int(input("Enter the number:"))

sum = 0
for i in range(1,n+1):
    sum += i
print(sum)
