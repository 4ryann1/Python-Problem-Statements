# Problem 5: Separate Files and Directories

# Write a Python program that separately displays files and subdirectories.

# Requirements:
# - Ask for a directory path.
# - Verify it exists.
# - Examine every item inside it.
# - Display files under a "Files" section.
# - Display directories under a "Directories" section.
# - Handle empty categories.

# Hint:
# - Use os.listdir(), os.path.join(), os.path.isfile(), and os.path.isdir().

import os

directory_path = input("Enter a directory path: ")

if os.path.isdir(directory_path):
    files = []
    directories = []
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            files.append(item)

        elif os.path.isdir(full_path):
            directories.append(item)

    print("\nFiles:")
    if files:
        for file in files:
            print(file)
    else:
        print("No Files Found.")

    print("\nDictionaries")
    if directories:
        for directory in directories:
            print(directory)
    else:
        print("No directories found.")

else:
     print("Invalid Path! The specified directory does not exist.")