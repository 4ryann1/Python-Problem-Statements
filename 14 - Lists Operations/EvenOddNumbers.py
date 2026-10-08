# Problem 3: Even and Odd Numbers
# Create a list of numbers from 1 to 50. Create two separate lists:
# - One containing all even numbers
# - One containing all odd numbers
# Print both lists.
#
# # Write your solution below.

#List of Numbers
list1 = []
for i in range(1,50):
    list1.append(i)
print(list1)

#List of even Numbers
even_numbers = [i for i in list1 if i % 2 == 0]
print(even_numbers)

#List of odd numbers
odd_numbers = [i for i in list1 if i % 2 != 0]
print(odd_numbers)
