# 5. Number to Word
#
# Take a number from 0 to 5 and print it in words.
#
# Example:
#
# Input: 4
# Output: Four
#
# For any other number, print "Invalid number".

number = int(input("Enter a number between 0 to 5: "))

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case 4:
        print("Four")
    case 5:
        print("Five")
    case _:
        print("Invalid Number")