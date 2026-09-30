# 5. Multiplication Table of a Given Number
# Goal: Calculate values dynamically inside the loop.

# Logic: Multiply a target number by a counter running from 1 to 10.

n = int(input("Enter a Number: "))

print("----- Table -----")
i=0
while i<=10:
    print(f"{n} x {i} = {n*i}")
    i+=1
