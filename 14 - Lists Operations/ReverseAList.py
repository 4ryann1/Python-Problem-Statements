# Problem 6: Reverse a List
# Create a program that accepts a list of numbers from the user and reverses the list.
# Do not use the built-in reverse() method or reversed() function.
#
# # Write your solution below.

#
list = []
count = 1
while count<=10:
    number = int(input("Enter a number: "))
    list.append(number)
    count += 1

print("The list is as follows:",list)

def reverse_list(list):
    left = 0
    right = len(list)-1

    while right>left:
        list[right], list[left] = list[left], list[right]
        right = right - 1
        left = left + 1
    return list

reversed_list = reverse_list(list)
print("The list is as follows:",reversed_list)