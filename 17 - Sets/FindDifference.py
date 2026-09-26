"""Problem 7: Find Difference Between Two Sets

Create two sets and display Set 1 - Set 2 and Set 2 - Set 1.
"""

# Write your solution below.

set1 = {1,2,3,4,5,6}
set2 = {4,5,6,7,8,9}

difference1 = set1.difference(set2)
difference2 = set2.difference(set1)

print(difference1, difference2, sep = "\n") #Difference removes the common elements from the sets. It only keeps the unique elements from both the lists.