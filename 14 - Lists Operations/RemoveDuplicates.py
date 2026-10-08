# Problem 7: Remove Duplicates
# Create a program that accepts a list containing duplicate values and creates a new list containing only unique values.
# Do not use set(). Preserve the original order of elements.
#
# # Write your solution below.

list1 = [10, 20, 10, 30, 40, 50]
unique_item = []

for item in list1:
    if item not in unique_item:
        unique_item.append(item)

print(unique_item)