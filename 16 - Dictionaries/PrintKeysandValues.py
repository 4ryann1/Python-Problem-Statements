"""Problem 5: Print All Keys and Values

Create a dictionary of 5 products and prices.
Print all keys, all values, and each key with its corresponding value.

Write your solution below.
"""

Dictionary = {
    "Milk":70,
    "Eggs":14,
    "Bread":30,
    "Potatoes": 40,
    "Burger":250
}

print("\n-------All Products-------")
for product in Dictionary.keys():
    print(f"{product}")

print("\n-------All Prices--------")
for price in Dictionary.values():
    print(f"{price}")

print("\n-------All Products-------")
for product, price in Dictionary.items():
    print(f"{product}: {price}")
