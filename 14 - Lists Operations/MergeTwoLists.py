# Problem 13: Merge Two Lists
# Create two lists of integers from user input and merge them into a single list.
# Then:
# - Print the merged list.
# - Print the sorted merged list.
# - Print the common elements between the two original lists.
#
# # Write your solution below.

length1 = int(input("Enter the length of first list: "))
list1 = []

length2 = int(input("Enter the length of second list: "))
list2 = []

count1 = 1
print("Enter the elements of the first list:")
while count1<=length1:
    number = int(input("Enter the number: "))
    list1.append(number)
    count1+=1

count2 = 1
print("Enter the elements of the second list:")
while count2<=length2:
    number = int(input("Enter the number: "))
    list2.append(number)
    count2+=1

list3 = list1 + list2
print(f"The merged list is {list3}")
print(f"The sorted list is {sorted(list3)}")

intersection = []
for item in list1:
    if item in list2:
        intersection.append(item)
print(f"The reversed list is {intersection}")