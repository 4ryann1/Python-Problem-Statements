# 8. Divisibility Checker
#
# Take a number and check:
#
# Divisible by both 3 and 5
# Divisible only by 3
# Divisible only by 5
# Not divisible by either

number = int(input("Enter a number: "))

if number%3==0 and number%5==0:
    print(f"The number {number} is divisible by 3 and 5")
elif number%3==0:
    print(f"The number {number} is divisible by 3")
elif number%5==0:
    print(f"The number {number} is divisible by 5")
else:
    print(f"Invalid Input: {number}")