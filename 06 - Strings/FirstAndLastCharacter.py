# First and Last Character
# Take a string from the user and print its first and last character.

user_string = input("Enter a string: ")

if user_string:
    print("First character:", user_string[0])
    print("Last character:", user_string[-1])
else:
    print("You did not enter a string")