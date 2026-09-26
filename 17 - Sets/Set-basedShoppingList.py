"""Problem 14: Set-Based Shopping List

Given purchased items and a shopping list, find still-needed items, unexpected purchases, and common items.
"""

# Write your solution below.

shopping_list = {"Eggs", "Milk", "Bread", "Chicken", "Beer", "Onion","Potatoes"}
still_needed_items = {"Eggs", "Milk"}
unexpected_items = {"Watch", "Shoes"}
common_items = shopping_list.intersection(still_needed_items)
print(f"The remaining items are: {still_needed_items}")