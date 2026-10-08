# 3. Simple Calculator
#
# Take two numbers and an operator (+, -, *, /) as input.
#
# Use match-case to perform the selected operation.
#
# Example:
#
# Input:
# 10
# 5
# +
#
# Output:
# 15

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

operator = input("Enter operator(+,-,*,/): ")

match operator:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case _:
        print("Invalid Input!")