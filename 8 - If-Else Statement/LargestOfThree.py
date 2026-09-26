# 7. Largest of Three Numbers
#
# Take three numbers and find the largest number using conditional statements.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

if num1 > num2 and num1 > num3:
    print(f"The first number is the greatest number that is {num1}")
elif num2 > num3 and num2 > num1:
    print(f"The second number is the greatest number that is {num2}")
elif num3 > num2 and num3 > num1:
    print(f"The third number is the greatest number that is {num3}")
else:
    print(f"Invalid input: {num3}")