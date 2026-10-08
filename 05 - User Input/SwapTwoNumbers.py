# Swap Two Numbers
# Take two numbers from the user, swap their values, and print the values before and after swapping.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1, num2 = num2, num1

print(f"The original numbers are {num2} and {num1}")
print(f"The swapped numbers are {num1} and {num2}")
