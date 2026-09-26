# 10. Simple Calculator
# Take two numbers and an operator (+, -, *, /) as input.
#
# Perform the appropriate operation using if-elif-else.
#
# Handle division by zero.

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

operator = input("Enter operator: ")

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    if number2 == 0:
        print("Number cannot be divided by zero")
    else:
        print(number1 / number2)
else:
    print("Invalid operator")

