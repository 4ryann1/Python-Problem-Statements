# Problem 2: Sum and Average
# Create a program that takes 10 numbers from the user, stores them in a list, and calculates:
# - Sum of all numbers
# - Average of the numbers
# - Count of numbers greater than the average
#
# # Write your solution below.

length_of_list = int(input("Enter the length of the list: "))

list_of_numbers = []
count = 1
while count <= 10:
    number = input("Enter the number: ")
    list_of_numbers.append(number)
    count += 1

print("The List is : ", list_of_numbers)

def average_sum_list(list_of_numbers):
    sum = 0
    for number in list_of_numbers:
        sum += number
    average = sum / len(list_of_numbers)
    return sum, average

average_sum_list(list_of_numbers)