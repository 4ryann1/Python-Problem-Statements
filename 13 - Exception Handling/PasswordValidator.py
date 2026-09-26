# 8. Password Validator
#
# Create a program that asks the user to create a password.
#
# Requirements:
#
# Password must contain at least 8 characters.
# If it contains fewer than 8 characters, raise ValueError.
# Handle empty input.
# Display "Password accepted" if valid.

try:
    user_password = input("Enter your password: ")
    if not user_password:
        raise ValueError("Password cannot be empty")

    if len(user_password) < 8:
        raise ValueError ("Password must be at least 8 characters")

    else:
        print("Password accepted")

except ValueError as error:
    print(f"Error: {error}")