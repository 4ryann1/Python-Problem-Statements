# Count a Character
# Take a string and a character as input. Count how many times that character appears in the string.

user_string = input("Please enter a string: ")
character = input("Please enter a character: ")

occurence = user_string.count(character)
print(occurence)