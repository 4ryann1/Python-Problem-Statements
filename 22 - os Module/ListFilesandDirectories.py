# Problem 4: List Files and Directories

# Write a Python program that displays all files and directories inside a user-specified directory.

# Requirements:
# - Ask for a directory path.
# - Verify that it exists and is a directory.
# - Display every item, numbered.
# - Handle an invalid path gracefully.

# Hint:
# - Use os.path.isdir() and os.listdir().

import os
path = input("Enter a directory: ")

if os.path.isdir(path):
    print("The directory path exists.")

    items = os.listdir(path)
    print("The items present in the directory are as follows:")
    for number,item in enumerate(items, start =1):
        print(f"{number}: {item}")
else:
    print("Invalid Path. Please import a valid path.")