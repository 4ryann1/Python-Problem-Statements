# Remove First and Last Character
# Take a string from the user and print the string after removing its first and last characters.

string = input("Enter a string: ")

string_new = string[1:len(string)-1]
print(string_new)