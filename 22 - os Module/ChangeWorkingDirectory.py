# Problem 2: Change the Working Directory

# Write a Python program that changes the current working directory to a directory provided by the user.

# Requirements:
# - Ask the user to enter a directory path.
# - Check whether the path exists.
# - If it exists, change to it and display the new working directory.
# - If it does not exist, display a suitable message.

# Hint:
# - Use os.path.exists() and os.chdir().

import os

directory = input("Enter the directory path: ")
if os.path.exists(directory):
    os.chdir(directory)
    print(f"The directory has been changed successfully.")
    print(f"The current working directory is {os.getcwd()}")
else:
    print("The specified directory does not exists.")