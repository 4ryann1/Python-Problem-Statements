"""Problem 4: Count Number of Key-Value Pairs

Create or accept a dictionary and find the total number of key-value pairs.

Write your solution below.
"""

dictionary = {
    "name": "Aryan",
    "age": 21,
    "city": "Pune"
}

count = 0
for key, value in dictionary.items():
    print(f"{key}: {value}")
    count += 1

print(f"There are {count} key-value pairs in the dictionary.")