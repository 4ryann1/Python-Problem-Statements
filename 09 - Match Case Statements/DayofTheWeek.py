# 1. Day of the Week
#
# Take a number from 1 to 7 and print the corresponding day.
#
# Example:
#
# Input: 3
# Output: Wednesday

day = int(input("Enter the Day:"))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid Input")



