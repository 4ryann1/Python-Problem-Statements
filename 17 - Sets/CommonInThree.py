"""Problem 10: Find Common Elements in Three Sets

Create three sets and display elements common to all three.
"""

# Write your solution below.

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}
set3 = {4,5,6,10,11,12}

#Logic 1
common = set1.intersection(set2,set3)
print(common)

#Logic 2
# common_elements = set1 & set2 & set3
# print(common_elements)