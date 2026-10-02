# Problem 1: Display Current Working Directory

# Write a Python program using the os module to display the current working directory.

# Requirements:
# - Import the os module.
# - Use the appropriate os function to get the current working directory.
# - Print the result.

# Hint:
# - Look for an os function related to "get current working directory".

import os

cwd = os.getcwd()
print(f"The Current working directory : {cwd}")