"""
Problem 12: Create a Dictionary from Two Lists

Create a list of keys and a list of values. Build a dictionary by combining corresponding elements.

Write your solution below.
"""

keys = ["Name", "Age", "College", "City"]
values = ["Aryan", 21, "DYPTC", "Pune"]

dictionary = {}

count=0
for key in keys:
    if key not in dictionary.keys():
        dictionary[key] = values[count]
        count+=1

print(dictionary)
