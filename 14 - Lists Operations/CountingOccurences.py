# Problem 10: Count Occurrences
# Create a program that accepts a list of numbers and asks the user for a number.
# Count how many times that number appears in the list without using the count() method.
#
# # Write your solution below.

list1 = [10, 10, 11, 12, 12, 10, 13, 12, 10, 10, 16, 15, 14]

unique_list = []
choice = int(input())
for i in list1:
    if i == choice:
        unique_list.append(i)
print(f"The number of times {choice} is appeared in the list is: {len(unique_list)}")