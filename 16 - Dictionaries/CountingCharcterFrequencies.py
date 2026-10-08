"""Problem 8: Count Character Frequency

Accept a string and use a dictionary to count how many times each character occurs.

Write your solution below.
"""

string = input("Enter string: ")

dict = {}

for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print("\nCharacter Frequency:")
for key, value in dict.items():
    print(f"{key}: {value}")