# 2. Print Even Numbers
#
# Take a number N and print all even numbers from 1 to N.
#
# Example:
#
# Input: 10
# Output: 2 4 6 8 10

num = int(input("Enter a number: "))

for i in range(0,num+1,2):
    print(i)