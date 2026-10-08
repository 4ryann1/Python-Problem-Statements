# Take an integer as input and check whether it is:
#
# Positive
# Negative
# Zero

number = int(input("Enter a number: "))

if number > 0:
    print(f"The number is positive: {number}")
elif number < 0:
    print(f"The number is negative: {number}")
elif number == 0:
    print(f"The number is zero: {number}")
else:
    print(f"Invalid input: {number}")