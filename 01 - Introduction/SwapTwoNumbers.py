# Swap Two Numbers
# Take two numbers as input and swap their values.
# Example: a = 10, b = 20 → a = 20, b = 10

input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

input1, input2 = input2, input1

print("Input 1 is: ", input1)
print("Input 2 is: ", input2)