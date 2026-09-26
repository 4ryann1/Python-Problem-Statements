# Problem 8: Second Largest Number
# Create a program that accepts a list of integers and finds the second largest unique number.
# Handle the case where a second largest number does not exist.
#
# # Write your solution below.

list1 = [10, 20, 400, 652, 45, 23, 32]
set1 = set(list1)

list2 = list(set1)
list2.sort()
unique=list2.reverse()

print(f"The second largest element in list1 is {list2[1]}")
