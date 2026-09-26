# Problem 11: Separate Positive, Negative and Zero
# Create a list of integers entered by the user. Create three separate lists:
# - Positive numbers
# - Negative numbers
# - Zeros
# Print all three lists along with their counts.
#
# Write your solution below.

positive_numbers = []
negative_numbers = []
zeros = []

all_numbers = []
print("You can enter 10 Numbers")
count = 1
try:
    while count<=10:
        number = int(input("Enter a number: "))
        all_numbers.append(number)
        count += 1
    print(f"The numbers entered are: {all_numbers}")

    for number in all_numbers:
        if number > 0:
            positive_numbers.append(number)
        elif number < 0:
            negative_numbers.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            break

    print(f"The numbers entered are: {positive_numbers}")
    print(f"The numbers entered are: {negative_numbers}")
    print(f"The numbers entered are: {zeros}")

except ValueError:
    print("Please Enter a Valid Number.")
