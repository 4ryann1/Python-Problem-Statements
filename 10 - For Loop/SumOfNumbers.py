# Calculate the sum of all numbers from 1 to N

number = int(input())

total_sum = 0
for i in range(1,number+1):
    total_sum = total_sum + i

print(total_sum)