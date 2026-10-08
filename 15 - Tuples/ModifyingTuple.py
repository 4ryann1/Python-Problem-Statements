"""Problem 10: Convert Tuple to List and Modify It

Create a Python program that accepts a tuple.
Convert the tuple into a list, add a new element, remove one element, and then convert the list back into a tuple.

Example:
Input: (10, 20, 30)
Add: 40
Remove: 20
Output:
Final tuple: (10, 30, 40)
"""

# Write your solution below.

tuple1 = (10, 20, 30)

list1 = list(tuple1)
list1.append(40)
list1.remove(20)
print(tuple(list1))