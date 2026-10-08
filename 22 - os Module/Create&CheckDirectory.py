# Problem 3: Create and Check a Directory

# Write a Python program that creates a new directory.

# Requirements:
# - Ask the user for a directory name.
# - Check whether it already exists.
# - If it does not exist, create it.
# - If it exists, display an appropriate message.
# - Confirm the final status.

# Hint:
# - Use os.path.exists() and os.mkdir().

import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("The path already exists.")
else:
    directory = os.mkdir(path)
    print(f"The new directory: {directory}")

if os.path.exists(path):
    print("Final status: directory exists.")
else:
    print("Final Status:  Directory does not exist.")