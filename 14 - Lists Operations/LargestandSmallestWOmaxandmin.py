# Problem 5: Largest and Smallest Without max() and min()
# Create a program that accepts 10 integers into a list and finds the largest and smallest numbers without using the built-in max() and min() functions.
#
# # Write your solution below.

list1 = []

count = 1
while count <=10:
    number = int(input("Enter a number: "))
    list1.append(number)
    count += 1

print("The list is as follows:")
for number in list1:
    print(number, end=" ")

largest = list1[0]
smallest = list1[0]

for i in range(1, len(list1)):
    if list1[i]>largest:
        largest = list1[i]

    if list1[i]<smallest:
        smallest = list1[i]

print("The largest number is: ", largest)
print("The smallest number is: ", smallest)