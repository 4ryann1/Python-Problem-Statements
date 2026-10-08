# 2. Age Validator
#
# Ask the user to enter their age.
#
# Requirements:
#
# Convert the input to an integer.
# Handle invalid/non-numeric input using try-except.
# If the age is negative, raise a ValueError.
# Display whether the age is valid.

try:
    age = input("Enter a number: ")
    age = int(age)
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is validated succesfully. {age} is valid.")

except Exception as error:
    print(f"Error: {error}")