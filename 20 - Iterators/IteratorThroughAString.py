# Problem 2: Iterate Through a String

# Create a Python program that creates an iterator from a string and prints each character one at a time.

# Requirements:
# - Take a string as input.
# - Create an iterator using iter().
# - Use next() to print every character.
# - Stop when all characters have been displayed.

string = iter(input("Enter a String: "))

try:
    print(next(string))
    print(next(string))
    print(next(string))
    print(next(string))
    print(next(string))
    print(next(string))
    print(next(string))

except StopIteration:
    print(f"Error: StopIteration Error!!")