# String Slicing
# Take a string as input and print:
#
# First 3 characters
# Last 3 characters
# Characters from index 2 to 5

user_string = input("Please enter a string: ")
if user_string:
    print("The First 3 characters of the string are:", user_string[0:3])
    print("The last 3 characters of the string are:", user_string[-3:])
    print("The characters from index 2 to 5 in the string are:", user_string[2:5])
else:
    print("The string is empty")
