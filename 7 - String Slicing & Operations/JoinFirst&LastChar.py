# Join First and Last Characters
# Take a string from the user and print only its first and last character together.
# Example: Python → Pn

string = input("Enter a string: ")

if len(string) < 2:
    print("String is empty")
else:
    print(string[0] + string[-1])