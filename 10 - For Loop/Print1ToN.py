# 1. Print Numbers from 1 to N
#
# Take a number N as input and print all numbers from 1 to N using a for loop.
#
# Example:
#
# Input: 5
# Output: 1 2 3 4 5

n = int(input("Enter the last Number: "))

print("The numbers are: ")
for i in range(1,n+1):
    print(i)
