# 17. Login System
#
# Ask the user for:
#
# Username
# Password
#
# Check whether they match predefined credentials.
#
# Display:
#
# "Login successful"
# "Incorrect password"
# "Username not found"
#
# Try to handle the different cases using nested if-else.

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "fuckyou@123"

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == CORRECT_USERNAME:
    if password == CORRECT_PASSWORD:
        print("Welcome back user! Login Successful!")
    else:
        print("Wrong username or password! Please try again.")
else:
    print("User Not Found!")