# 7. Reverse a String
#
# Take a string as input and print it in reverse order using a for loop.
#
# Example:
#
# Input: Python
# Output: nohtyP

string1 = input("Enter a string: ")

reversed_String = ""

for i in range(len(string1) -1, -1, -1):
    reversed_String += string1[i]
print(reversed_String)