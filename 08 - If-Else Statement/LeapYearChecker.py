# 11. Leap Year Checker
#
# Take a year as input and determine whether it is a leap year.
#
# Hint: A year is a leap year if:
#
# It is divisible by 400, OR
# It is divisible by 4 but not by 100.

year = int(input("Enter a year: "))

if year%4==0:
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is not a leap year")
